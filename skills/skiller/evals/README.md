# Skiller evals

These are proposed behavioral tests, not a certificate of skill quality. `evals.json` tests the **define, author, validate, extract, doctor and publish** boundaries. `trigger-queries.json` tests implicit activation and near-miss requests (fixed 12 train / 8 validation split).

## Run the safe subset

From the repository root, with Python 3.11+ and Pi installed:

```bash
python3 scripts/evals.py validate
python3 -m unittest discover -s tests -v
python3 scripts/evals.py quality --ids define-scope validate-broken --baseline --model PROVIDER/MODEL
python3 scripts/evals.py activation --query-ids p-define n-use --repeats 1 --model PROVIDER/MODEL
```

Omit `--ids` to run all nine `read_only` quality cases. Run `activation --split train --repeats 3`, then `--split validation` to check generalization. Model runs cost tokens. Pin a model when comparing iterations.

**The runner allows only Pi's `read` tool**, disables other skills, extensions and project instructions, uses a fresh session and directory for every run, and cannot execute `manual_sandbox` cases even when their IDs are passed. It loads Skiller explicitly as an available skill for quality/activation; a trigger counts only if the agent actually reads its `SKILL.md`. Baselines use the same prompt without the skill. Results go into ignored `.eval-workspace/iteration-*/`: trace, response, fixture hashes, mechanical grades, tokens/time and a `review.md` checklist. Assertions about correctness and safety remain **pending human review**. Check both the final output and the trace for unsupported claims, calls outside scope, and requested confirmation. Mechanical no-write checks alone do not establish that Skiller helped.

## Completion-loop regressions

The partial-distribution fixture deliberately has an authored skill and a development-only README, but no installation instructions or release-please infrastructure. Keep those omissions: they reproduce a real failure, not unfinished test data.

- `distribution-gaps`: inspect the whole local outcome and identify both omissions.
- `publication-resume`: preserve an agreed publication objective across a short approval reply, without treating a push as completion. The read-only prompt supplies previous-turn context; it is not an actual multi-turn execution test.
- `git-only-scope`: honor an explicitly narrowed upload-only request instead of forcing publication work.
- `publication-blocked`: preserve evidence of completed work, stop unchanged failing retries and report remaining verification as blocked.
- `publication-repair-loop`: manually stage the actual repair/approval/fake-push conversation and inject a failed verification in a disposable sandbox. Verify artifacts and tool ordering, not merely the agent's explanation.

Offline unit tests check fixture omissions, case coverage and sandbox exclusion; they do not prove that a model follows the loop. Read-only model runs can assess diagnosis and planning, but cannot prove repair, push ordering or remote verification. Those assertions remain pending until the sandbox case is executed and reviewed.

`manual_sandbox` cases (doctor checks, local extraction, publication without consent, and the publication repair loop) are **not runnable by this tool**. Review them only in a disposable sandbox with fake `gh`/git credentials, disabled external network, and explicit permission for any side effects. Never run the publication probe against a real account. Compare the original and copied skill for extraction and verify no remote operation occurred. Recording the evidence and PASS/FAIL for each assertion is a human step, not an automatic score.

CI validates fixtures and runner code offline; it never invokes a model or GitHub. Do not commit generated traces, secrets or local output. Official guidance: [output evaluations](https://agentskills.io/skill-creation/evaluating-skills) and [activation evaluations](https://agentskills.io/skill-creation/optimizing-descriptions).
