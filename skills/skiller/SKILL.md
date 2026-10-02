---
name: skiller
description: Design, build, validate, and publish Agent Skills. Use when someone wants to turn an idea or repeatable task into a skill, improve an existing skill, check its compliance with Agent Skills, or publish it on GitHub for installation with skills.sh and versioning with release-please.
compatibility: Publishing requires git, authenticated gh, GitHub access, and permission to configure GitHub Actions; checking installation requires Node.js and npx.
---

# Skiller

Help take a skill from an idea to a distributable repository. Do not confuse the installable skill with the repository hosting it. Resolve relative paths from this skill's directory when reading references and templates.

## Choose a path based on the user's intent

- **Design**: read [official sources](references/official-sources.md) and [design](references/design.md). If the user is still exploring, present a design before writing files.
- **Build or improve**: read [official sources](references/official-sources.md), [build](references/build.md), and [validate](references/validate.md). If the requirements are unclear, start with design.
- **Validate**: read [official sources](references/official-sources.md) and [validate](references/validate.md). Report issues before changing existing content.
- **Publish**: read [official sources](references/official-sources.md), [validate](references/validate.md), and [publish](references/publish.md). Accept an existing skill; do not rebuild it by default.
- **End-to-end**: design → build → validate → publish, with human review before publication.

Consult the current official documentation listed in `references/official-sources.md` before designing, building, validating, or writing installation commands. If it is unavailable, say so and do not claim that unverified behavior has been checked.

## Expected structure

For a new repository, put the installable unit in `skills/<name>/SKILL.md`, with `references/`, `scripts/`, and `assets/` only when needed. Keep `README.md`, `AGENTS.md`, and release-please files at the repository root. If an existing skill is at the root or another location, propose a migration and check relative references before moving anything.

## Boundaries and safety

- Do not publish secrets, credentials, personal paths, temporary files, or unrelated material. Inspect the files before uploading them.
- Preserve existing files: do not overwrite `README.md`, `AGENTS.md`, `SKILL.md`, or release configuration without comparing them and agreeing on the changes.
- Show the destination, visibility, and planned files, and **ask for explicit confirmation before creating a remote repository, pushing, or changing remote settings**. Preparing local files is not the same as publishing them.
- Do not claim that a GitHub Release means `skills.sh` installs a pinned version: verify installation and the release lifecycle separately.
