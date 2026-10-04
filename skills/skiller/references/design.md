# Design a skill

Before designing or reviewing a design, **always** consult the Agent Skills specification and best practices linked in `references/official-sources.md`. Also consult the activation guide when writing the `description` field. If the sources are unavailable, disclose that limitation.

1. Ask for a real use case, example tasks, and previous corrections. Avoid generating generic procedures without domain expertise or source material.
2. Define one coherent capability: which requests should activate the skill, which similar requests **should not**, and what is out of scope. Do not combine unrelated capabilities merely because they use the same tools.
3. Identify inputs, expected outputs, environment dependencies, permissions, and external actions that require confirmation. Read `references/layouts/README.md` and the file for each proposed layout. If the skill is project-local, global, or multi-harness, read `references/targets/README.md`, every requested target file, and `references/targets/multi-target.md` when applicable before selecting paths.
4. Decide which knowledge belongs in `SKILL.md` (essential steps and warnings), which details belong in on-demand `references/`, and whether scripts or assets are needed. Do not create directories by habit.
5. Propose a lowercase, hyphenated name and a specific description explaining **what the skill does and when to use it**. Check that the name and directory will meet the specification.
6. Present a short design with 2–3 test requests and at least one request that should not activate the skill. Ask for review before building if decisions remain open.

Designing does not automatically create a repository or release infrastructure.
