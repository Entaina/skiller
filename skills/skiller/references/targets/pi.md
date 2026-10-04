# Pi

## Official sources

- [Pi skills documentation](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/skills.md)
- [Pi settings reference — resources](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/settings.md#resources)
- [Pi packages](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/packages.md)

## Discovery

- Portable project location: `.agents/skills/<name>/SKILL.md`.
- Portable user location: `~/.agents/skills/<name>/SKILL.md`.
- Pi discovers project `.agents/skills/` directories from the working directory through its ancestors, stopping at the repository root.
- Pi can also load skill files or directories declared through settings and skills exposed by Pi packages.
- Pi discovers directories containing `SKILL.md` recursively and prefers the directory form over standalone Markdown skills.

## Compatibility

Use standard Agent Skills frontmatter for portability. Pi supports `disable-model-invocation: true`. Match `name` to the parent directory even though Pi itself does not require or warn about that mismatch, because other implementations may enforce it.

## Verification

Run Pi where the project skill is discoverable, inspect startup diagnostics, and check `/skill:<name>`. After editing during an active session, run `/reload` and test one explicit and one description-based invocation.

For distribution through npm or git specifically as a Pi customization bundle, consult Pi package documentation rather than assuming a raw skill repository is a Pi package.
