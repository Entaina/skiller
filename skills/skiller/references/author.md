# Author or improve a skill

Use this phase to materialize an approved definition as skill files. Consult the specification and best practices in `references/official-sources.md`; consult the official CLI documentation before using `npx skills init`. If scope, activation, or success criteria remain unclear, return to `references/define.md` instead of deciding them during authoring.

1. Start from the approved definition. For an existing skill, inspect its current content and the requested change; preserve existing behavior and paths unless a change or migration is agreed.
2. Read `references/layouts/README.md` and the selected layout file. For project-local, global, or multi-harness use, also read `references/targets/README.md`, every requested target file, and `references/targets/multi-target.md` when applicable. Verify current official target documentation before choosing discovery or installation paths.
3. Confirm the canonical destination and skill name. Create or update the skill directory and ensure the frontmatter `name` equals its directory name.
4. Write the approved description and valid frontmatter. Add `compatibility` only for real requirements. Avoid target-specific metadata or syntax unless the selected targets require it.
5. Author the reusable procedure with explicit boundaries, tricky cases, and checks. Preserve the approved scope; do not add unrelated capabilities while writing instructions.
6. Keep essential steps and warnings in `SKILL.md`. Add `references/` for details read on demand, `scripts/` for repeatable verifiable logic, and `assets/` for static resources only when needed. Use relative paths and document dependencies.
7. Keep repository documentation, CI, and publication infrastructure outside the skill directory. Add them only when the requested layout or publication workflow needs them.
8. Finish with `references/validate.md`. Do not publish merely because the files have been authored.

A valid minimal skill is `<skill-directory>/SKILL.md`, with no other files. `npx skills init` can provide a scaffold, but check its current behavior and place it at the destination selected through the applicable layout and target references. An empty scaffold is not a finished skill.
