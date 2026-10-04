#!/usr/bin/env python3
"""Run Skiller's read-only evals in isolated Pi processes. No external Python packages."""

import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "skiller"
EVALS = SKILL / "evals"


def load_cases():
    quality = json.loads((EVALS / "evals.json").read_text(encoding="utf-8"))
    triggers = json.loads((EVALS / "trigger-queries.json").read_text(encoding="utf-8"))
    if quality.get("skill_name") != "skiller" or not isinstance(quality.get("evals"), list):
        raise ValueError("expected skill_name=skiller and evals array")
    cases = quality["evals"]
    for group, values in (("quality", cases), ("activation", triggers)):
        if not isinstance(values, list) or not all(isinstance(item, dict) for item in values):
            raise ValueError(f"{group} must be an array of objects")
        ids = [item.get("id") for item in values]
        if len(ids) != len(set(ids)) or not all(isinstance(i, str) and re.fullmatch(r"[a-z0-9-]+", i) for i in ids):
            raise ValueError(f"invalid or duplicate {group} IDs")
    for case in cases:
        if case.get("mode") not in {"read_only", "manual_sandbox"}:
            raise ValueError(f"invalid mode in {case['id']}")
        if not all(isinstance(case.get(k), str) and case[k].strip() for k in ("prompt", "expected_output")):
            raise ValueError(f"missing prompt/expected_output in {case['id']}")
        if not isinstance(case.get("assertions"), list) or not case["assertions"] or not all(isinstance(a, str) for a in case["assertions"]):
            raise ValueError(f"missing assertions in {case['id']}")
        for check in case.get("checks", []):
            if check.get("type") not in {"no_output_files", "fixtures_unchanged", "response_regex"}:
                raise ValueError(f"unknown check in {case['id']}: {check}")
            if check["type"] == "response_regex":
                if not isinstance(check.get("pattern"), str):
                    raise ValueError(f"missing response_regex pattern in {case['id']}")
                re.compile(check["pattern"])
        for file in case.get("files", []):
            path = Path(file)
            if path.is_absolute() or ".." in path.parts or not (SKILL / path).is_file():
                raise ValueError(f"missing/unsafe fixture in {case['id']}: {file}")
    if not isinstance(triggers, list) or len(triggers) < 2:
        raise ValueError("expected trigger queries")
    for query in triggers:
        if not isinstance(query.get("query"), str) or not query["query"].strip() or type(query.get("should_trigger")) is not bool or query.get("split") not in {"train", "validation"}:
            raise ValueError(f"invalid activation query: {query}")
    return cases, triggers


def save(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def message_text(message):
    return "\n".join(p["text"] for p in message.get("content", []) if isinstance(p, dict) and p.get("type") == "text")


def consulted(events):
    """A listed skill is not a triggered skill; require an actual SKILL.md read."""
    target = (SKILL / "SKILL.md").resolve()
    for event in events:
        if event.get("type") != "message_end" or event.get("message", {}).get("role") != "assistant":
            continue
        for part in event["message"].get("content", []):
            if isinstance(part, dict) and part.get("type") == "toolCall" and part.get("name") == "read":
                candidate = part.get("arguments", {}).get("path")
                if isinstance(candidate, str) and Path(candidate).resolve() == target:
                    return True
    return False


def fixture_hashes(directory, paths):
    return {str(path): hashlib.sha256((directory / path).read_bytes()).hexdigest() if (directory / path).is_file() else None for path in paths}


def execute(args, prompt, directory, with_skill, fixtures=()):
    directory.mkdir(parents=True)
    for filename in fixtures:
        target = directory / filename
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(SKILL / filename, target)
    before = fixture_hashes(directory, fixtures)
    command = [args.pi, "--mode", "json", "--print", "--no-session", "--no-extensions",
               "--no-context-files", "--no-skills", "--tools", "read", "--thinking", "off"]
    if with_skill:
        command += ["--skill", str(SKILL)]
    if args.model:
        command += ["--model", args.model]
    command += ["--", prompt]
    env = os.environ.copy()
    env.pop("PI_SESSION_ID", None)
    env.pop("PI_SESSION_FILE", None)
    started = time.monotonic()
    try:
        result = subprocess.run(command, cwd=directory, env=env, text=True, capture_output=True, timeout=args.timeout)
        duration = round((time.monotonic() - started) * 1000)
        (directory / "trace.jsonl").write_text(result.stdout, encoding="utf-8")
        (directory / "stderr.txt").write_text(result.stderr, encoding="utf-8")
        events = [json.loads(line) for line in result.stdout.splitlines() if line.strip()]
        response = "\n".join(message_text(e["message"]) for e in events
                             if e.get("type") == "message_end" and e.get("message", {}).get("role") == "assistant"
                             and message_text(e["message"])).strip()
        (directory / "response.txt").write_text(response + "\n", encoding="utf-8")
        usage = [e["message"].get("usage", {}) for e in events if e.get("type") == "message_end" and e.get("message", {}).get("role") == "assistant"]
        run = {"status": "ok" if result.returncode == 0 and response and any(e.get("type") == "agent_end" for e in events) else "error",
               "exit_code": result.returncode, "duration_ms": duration,
               "total_tokens": sum(u.get("totalTokens", 0) or 0 for u in usage),
               "skill_consulted": consulted(events), "read_only_tools": True}
    except (subprocess.TimeoutExpired, json.JSONDecodeError) as exc:
        run = {"status": "error", "error": str(exc), "duration_ms": round((time.monotonic() - started) * 1000)}
        (directory / "error.txt").write_text(str(exc), encoding="utf-8")
    # Capture state before writing grading metadata. Read-only tool policy is a second safeguard.
    generated = sorted(str(p.relative_to(directory)) for p in directory.rglob("*") if p.is_file()
                       and str(p.relative_to(directory)) not in set(fixtures)
                       and str(p.relative_to(directory)) not in {"trace.jsonl", "stderr.txt", "response.txt", "error.txt"})
    checks = {"no_output_files": not generated, "fixtures_unchanged": before == fixture_hashes(directory, fixtures)}
    run["generated_files"] = generated
    save(directory / "timing.json", run)
    return run, checks


def grade(case, directory, checks, generated):
    response = (directory / "response.txt").read_text(encoding="utf-8") if (directory / "response.txt").is_file() else ""
    graded = []
    for item in case.get("checks", []):
        kind = item["type"]
        if kind == "response_regex":
            match = re.search(item["pattern"], response, re.IGNORECASE)
            graded.append({"type": kind, "pattern": item["pattern"], "passed": bool(match),
                           "evidence": f"Matched: {match.group(0)!r}" if match else "No match in response"})
        else:
            graded.append({"type": kind, "passed": checks[kind], "evidence":
                           "Generated files: " + repr(generated) if kind == "no_output_files"
                           else "Fixture SHA-256 unchanged=" + str(checks["fixtures_unchanged"])})
    save(directory / "grading.json", {"mechanical": graded, "human_status": "pending", "assertions": case["assertions"]})
    (directory / "review.md").write_text(
        f"# {case['id']} — review pending\n\nExpected: {case['expected_output']}\n\n" +
        "Review response AND trace. Mark each assertion PASS or FAIL with a quote or tool-call reference.\n\n" +
        "\n".join(f"- [ ] {a} — PASS/FAIL; evidence: " for a in case["assertions"]) + "\n", encoding="utf-8")
    return graded


def output_dir(args):
    base = Path(args.workspace).resolve()
    base.mkdir(parents=True, exist_ok=True)
    dest = base / ("iteration-" + dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%S%fZ"))
    dest.mkdir()
    return dest


def quality(args, cases):
    selected = [c for c in cases if c["mode"] == "read_only" and (not args.ids or c["id"] in args.ids)]
    manual = [c["id"] for c in cases if c["mode"] == "manual_sandbox"]
    if args.ids and set(args.ids) & set(manual):
        raise ValueError("manual_sandbox cases cannot be run by this read-only runner: " + ", ".join(sorted(set(args.ids) & set(manual))))
    if not selected:
        raise ValueError("no read_only cases selected")
    dest = output_dir(args)
    rows = []
    failed = False
    for case in selected:
        row = {"id": case["id"]}
        for label in (["with_skill", "without_skill"] if args.baseline else ["with_skill"]):
            run_dir = dest / case["id"] / label
            run, check_values = execute(args, case["prompt"], run_dir, label == "with_skill", case.get("files", []))
            graded = grade(case, run_dir, check_values, run["generated_files"])
            row[label] = {**run, "mechanical_passed": sum(c["passed"] for c in graded), "mechanical_total": len(graded)}
            failed |= run["status"] != "ok" or (label == "with_skill" and (not run.get("skill_consulted") or any(not c["passed"] for c in graded)))
        rows.append(row)
        print(f"{case['id']}: consulted={row['with_skill'].get('skill_consulted')}, mechanical={row['with_skill']['mechanical_passed']}/{row['with_skill']['mechanical_total']}", flush=True)
    save(dest / "benchmark.json", {"mode": "quality", "model": args.model or "Pi default", "human_status": "pending",
                                   "read_only": True, "cases": rows})
    print(f"Results: {dest}")
    return int(failed)


def activation(args, queries):
    selected = [q for q in queries if (args.split == "all" or q["split"] == args.split) and (not args.query_ids or q["id"] in args.query_ids)]
    if not selected:
        raise ValueError("no activation queries selected")
    dest = output_dir(args)
    rows = []
    failed = False
    for query in selected:
        runs = []
        for repeat in range(1, args.repeats + 1):
            run, _ = execute(args, query["query"], dest / query["id"] / f"run-{repeat}", True)
            runs.append(run)
            failed |= run["status"] != "ok"
        count = sum(r.get("skill_consulted", False) for r in runs)
        rate = count / args.repeats
        row = {"id": query["id"], "split": query["split"], "should_trigger": query["should_trigger"],
               "triggers": count, "runs": args.repeats, "rate": rate,
               "passed": rate >= 0.5 if query["should_trigger"] else rate < 0.5}
        rows.append(row)
        print(f"{query['id']}: {count}/{args.repeats} (expected {query['should_trigger']})", flush=True)
    save(dest / "benchmark.json", {"mode": "activation", "model": args.model or "Pi default", "cases": rows,
                                   "passed": sum(r["passed"] for r in rows), "total": len(rows)})
    print(f"Results: {dest}")
    return int(failed or any(not row["passed"] for row in rows))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["validate", "quality", "activation"])
    parser.add_argument("--workspace", default=str(ROOT / ".eval-workspace"))
    parser.add_argument("--pi", default="pi")
    parser.add_argument("--model", help="pin provider/model for comparable runs")
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--ids", nargs="+", help="quality IDs (read_only only)")
    parser.add_argument("--baseline", action="store_true", help="also run without skill")
    parser.add_argument("--split", choices=["all", "train", "validation"], default="all")
    parser.add_argument("--query-ids", nargs="+", help="activation query IDs")
    parser.add_argument("--repeats", type=int, default=3)
    args = parser.parse_args()
    try:
        cases, triggers = load_cases()
        if args.command == "validate":
            print(f"Valid: {len(cases)} quality cases ({sum(c['mode']=='read_only' for c in cases)} read-only), {len(triggers)} trigger queries")
            return 0
        if args.repeats < 1 or args.timeout < 1:
            raise ValueError("repeats and timeout must be positive")
        return quality(args, cases) if args.command == "quality" else activation(args, triggers)
    except (ValueError, OSError) as exc:
        parser.exit(2, f"evals: {exc}\n")


if __name__ == "__main__":
    sys.exit(main())
