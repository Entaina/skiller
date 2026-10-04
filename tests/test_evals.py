"""Offline tests for Skiller eval data and isolation; no model or network."""

import argparse
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import evals


class EvalTests(unittest.TestCase):
    def test_cases_and_safe_fixtures(self):
        cases, queries = evals.load_cases()
        self.assertEqual(len(cases), 8)
        self.assertEqual(sum(c["mode"] == "read_only" for c in cases), 5)
        self.assertEqual(len(queries), 20)
        self.assertEqual(sum(q["should_trigger"] for q in queries), 10)
        self.assertEqual(sum(q["split"] == "validation" for q in queries), 8)

    def test_skill_presence_is_not_activation(self):
        listed = {"type": "message_start", "message": {"role": "system", "content": str(evals.SKILL)}}
        self.assertFalse(evals.consulted([listed]))
        tool = {"type": "message_end", "message": {"role": "assistant", "content": [
            {"type": "toolCall", "name": "read", "arguments": {"path": str(evals.SKILL / "SKILL.md")}}]}}
        self.assertTrue(evals.consulted([tool]))

    def test_fixture_hashes_notice_modifications_and_deletions(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            (directory / "input.md").write_text("source", encoding="utf-8")
            before = evals.fixture_hashes(directory, ["input.md"])
            (directory / "input.md").write_text("changed", encoding="utf-8")
            self.assertNotEqual(before, evals.fixture_hashes(directory, ["input.md"]))
            (directory / "input.md").unlink()
            self.assertNotEqual(before, evals.fixture_hashes(directory, ["input.md"]))

    def test_manual_cases_cannot_execute(self):
        cases, _ = evals.load_cases()
        with tempfile.TemporaryDirectory() as tmp:
            args = argparse.Namespace(ids=["publish-no-consent"], workspace=tmp)
            with self.assertRaisesRegex(ValueError, "manual_sandbox"):
                evals.quality(args, cases)
            self.assertEqual(list(Path(tmp).iterdir()), [])

    def test_regex_grade_has_output_evidence(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            (directory / "response.txt").write_text("Missing description in frontmatter.\n", encoding="utf-8")
            case = {"id": "fixture", "expected_output": "Report a missing field", "assertions": ["Reports the field"],
                    "checks": [{"type": "response_regex", "pattern": "description"}]}
            graded = evals.grade(case, directory, {}, [])
            self.assertTrue(graded[0]["passed"])
            self.assertIn("description", graded[0]["evidence"])

    def test_runner_passes_read_only_tools_to_process(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            fake = directory / "fake-pi"
            fake.write_text("#!/usr/bin/env python3\n"
                            "import json, sys\n"
                            "assert '--tools' in sys.argv and sys.argv[sys.argv.index('--tools')+1] == 'read'\n"
                            "assert '--no-extensions' in sys.argv and '--no-context-files' in sys.argv and '--no-skills' in sys.argv and '--skill' in sys.argv\n"
                            "print(json.dumps({'type':'message_end','message':{'role':'assistant','content':[{'type':'text','text':'OK'}], 'usage':{'totalTokens':3}}}))\n"
                            "print(json.dumps({'type':'agent_end'}))\n", encoding="utf-8")
            fake.chmod(0o755)
            args = argparse.Namespace(pi=str(fake), model=None, timeout=10)
            run, checks = evals.execute(args, "Review this", directory / "case", True,
                                       ["evals/files/broken-skill/SKILL.md"])
            self.assertEqual(run["status"], "ok")
            self.assertEqual(run["total_tokens"], 3)
            self.assertTrue(checks["no_output_files"])
            self.assertTrue(checks["fixtures_unchanged"])
            self.assertFalse(run["skill_consulted"])  # Listed but not read by the fake agent.


if __name__ == "__main__":
    unittest.main()
