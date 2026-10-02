# Agent instructions

The installable skill lives in `skills/`. Edit its `SKILL.md` and resources while preserving relative paths; the repository root contains documentation and publication configuration. Do not add credentials or personal paths.

When making commits destined for the default branch, use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) so release-please can propose the next version:

- `feat: add a capability` — new functionality.
- `fix: correct an instruction` — a fix.
- `feat!: change the skill contract` — a breaking change (describe the impact).

Do not assume these instructions enforce Git policy: if a message does not follow the convention, release-please may not include the change in a release.
