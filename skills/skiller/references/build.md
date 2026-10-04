# Build or improve a skill

Consult the specification and best practices in `references/official-sources.md`; consult the official CLI documentation if you intend to use `npx skills init`.

1. Read `references/layouts/README.md` and the file for the approved layout. For project-local, global, or multi-harness use, also read `references/targets/README.md`, every requested target file, and `references/targets/multi-target.md` when applicable. Verify current official documentation before choosing discovery or installation paths. Confirm the repository root and skill name; the frontmatter `name` must equal the skill directory name. If the user is working on an existing skill, inspect it and preserve its content and paths; agree on any migration first.
2. Write valid YAML frontmatter: `name` identical to the directory name, and a `description` covering the task and when the skill should activate. Add `compatibility` only for real requirements. Avoid agent-specific metadata or syntax unless justified.
3. Describe a reusable procedure with boundaries, tricky cases, and checks. Prefer instructions based on real domain knowledge over generic advice. Keep the main file concise; say when to read each reference. Use relative paths within the skill.
4. Add `references/` only for material read on demand, `scripts/` for repeatable, verifiable logic, and `assets/` for static resources. Document dependencies and verify executable scripts.
5. Do not put repository documentation or GitHub workflows inside the skill directory. That infrastructure belongs to the repository root and is needed only for distribution or publication.
6. Finish with `references/validate.md`. Do not publish merely because the files have been created.

A valid minimal skill is `<skill-directory>/SKILL.md`, with no other files. `npx skills init` can provide a starting point, but check its current behavior and place the scaffold at the destination selected through the applicable layout and target references. An empty scaffold is not a finished skill.
