# Codex

## Official sources

- [OpenAI skills documentation](https://developers.openai.com/codex/skills)
- [OpenAI plugin documentation](https://developers.openai.com/plugins/build/plugins)

## Discovery

- Repository locations: `.agents/skills/<name>/SKILL.md` in directories from the current working directory up to the repository root.
- User location: `~/.agents/skills/<name>/SKILL.md`.
- Administrator location: `/etc/codex/skills/<name>/SKILL.md`.
- Codex supports symbolic-linked skill directories and follows their targets.

## Compatibility

Keep `SKILL.md` within the Agent Skills specification for portability. Codex can use optional `agents/openai.yaml` metadata for OpenAI-specific UI, invocation policy, and dependencies; add it only when requested and treat it as a target extension rather than part of the portable skill core.

OpenAI's current documentation distinguishes local skill folders from reusable plugin distribution. Consult the official plugin guidance when the requested distribution target is specifically ChatGPT or Codex; do not assume another ecosystem's publication flow is equivalent.

## Verification

Codex normally detects skill changes automatically. If a change does not appear, restart Codex. Use `/skills` or `$<name>` for explicit selection, then test one explicit and one description-based invocation.
