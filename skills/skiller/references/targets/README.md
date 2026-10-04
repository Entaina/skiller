# Target selection

Read this index for project-local, user-global, or multi-harness use. The Agent Skills format is portable, but discovery paths, precedence, reload behavior, and extensions are target-specific.

Select every requested target:

- [Pi](pi.md)
- [Claude Code](claude-code.md)
- [Codex](codex.md)
- [Multiple targets](multi-target.md)
- [Unknown or undocumented target](unknown-target.md)

For each target, determine project and user locations, recursive discovery, link handling, reload behavior, name collisions, supported frontmatter, and a concrete discovery test. Ask before creating files when the target or scope is unclear.

Keep target-specific claims in the corresponding file. Every target file must contain an `## Official sources` section before its discovery, compatibility, installation, or verification guidance. Add another `<target-id>.md` only from verified official sources and update this index. If no official source is available, mark the target unverified instead of using third-party claims as authoritative. Do not infer one harness's behavior from another.
