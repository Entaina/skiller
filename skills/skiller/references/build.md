# Build or improve a skill

Consult the specification and best practices in `references/official-sources.md`; consult the official CLI documentation if you intend to use `npx skills init`. The `init` command is optional: check its current syntax and output before adapting it to `skills/<name>/`.

1. From the approved design, create `skills/<name>/SKILL.md` in the local project. If the user is working on an existing skill, inspect it and preserve its content and paths; agree on any migration first.
2. Write valid YAML frontmatter: `name` identical to the directory name, and a `description` covering the task and when the skill should activate. Add `compatibility` only for real requirements. Avoid agent-specific metadata or syntax unless justified.
3. Describe a reusable procedure with boundaries, tricky cases, and checks. Prefer instructions based on real domain knowledge over generic advice. Keep the main file concise; say when to read each reference. Use relative paths within the skill.
4. Add `references/` only for material read on demand, `scripts/` for repeatable, verifiable logic, and `assets/` for static resources. Document dependencies and verify executable scripts.
5. Do not put the repository README or GitHub workflows **inside** `skills/<name>/`. That infrastructure belongs to the publication phase.
6. Finish with `references/validate.md`. Do not publish merely because the files have been created.

A valid minimal example is `skills/my-skill/SKILL.md`, with no other files. `npx skills init` can provide a starting point, but an empty scaffold is not a finished skill.
