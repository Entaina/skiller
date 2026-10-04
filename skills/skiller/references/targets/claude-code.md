# Claude Code

## Official sources

- [Claude Code skills documentation](https://code.claude.com/docs/en/skills)

## Discovery

- Project location: `.claude/skills/<name>/SKILL.md`.
- Personal location: `~/.claude/skills/<name>/SKILL.md`.
- Claude Code also supports nested project `.claude/skills/` directories, managed enterprise locations, additional directories, plugins, and account-synced skills. Consult the official source before using those modes.
- Skill directories in personal and project locations may be symbolic links.

## Compatibility

Prefer standard Agent Skills fields for a skill intended for other harnesses. Claude Code supports additional frontmatter and body features; use them only when the skill is intentionally Claude-specific or when other requested targets have been checked for compatibility.

Do not use reserved local skill directory names such as `synced` or names reserved for account-synced skills. Recheck the official source because reserved names and collision behavior can change.

## Verification

Claude Code watches existing skill directories and normally detects `SKILL.md` changes during a session. If a top-level skills directory did not exist when the session started, use `/reload-skills` as documented. Confirm the skill appears in the skill or command UI, then test one explicit invocation and one description-based invocation.
