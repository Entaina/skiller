---
name: skiller
description: Design, build, validate, and publish Agent Skills. Use when someone wants to turn an idea or repeatable task into a skill, improve an existing skill, check its compliance with Agent Skills, or publish it on GitHub for installation with skills.sh and versioning with release-please.
compatibility: Publishing requires git, authenticated gh, GitHub access, and permission to configure GitHub Actions; checking installation requires Node.js and npx.
---

# Skiller

Help take a skill from an idea to a distributable repository. Do not confuse the installable skill with the repository hosting it. Resolve relative paths from this skill's directory when reading references and templates.

## Choose a path based on the user's intent

- **Design**: read [official sources](references/official-sources.md) and [design](references/design.md). If the user is still exploring, present a design before writing files.
- **Doctor**: read [doctor](references/doctor.md). Unless the user explicitly narrows the scope, check only local tools, GitHub CLI authentication, and relevant repository or organization permissions. Report each local tool and each permission on its own line; do not run skill discovery, installation, validation, workflow inspection, or unrelated diagnostics.
- **Build or improve**: read [official sources](references/official-sources.md), [build](references/build.md), and [validate](references/validate.md). If the requirements are unclear, start with design.
- **Validate**: read [official sources](references/official-sources.md) and [validate](references/validate.md). Inspect the skill's own structure and behavior; report issues before changing existing content. Use [doctor](references/doctor.md) separately if environment checks are needed.
- **Publish**: read [official sources](references/official-sources.md), [doctor](references/doctor.md), [validate](references/validate.md), and [publish](references/publish.md). Check infrastructure with doctor and the skill itself with validate. Accept an existing skill; do not rebuild it by default.
- **End-to-end**: design → build → validate → doctor → publish, with human review before publication.

Consult the current official documentation listed in `references/official-sources.md` before designing, building, validating, or writing installation commands. If it is unavailable, say so and do not claim that unverified behavior has been checked.

## Choose the destination

Read the [layout index](references/layouts/README.md) whenever locating or moving a skill source, then load the file for the selected layout. Layout references cover only supported repository placement: distribution repositories and project-local sources. Treat other existing placements as migration cases under build and validation rather than adding a layout for every exception. Use design, build, and validation guidance for the skill unit's internal structure.

For project-local, global, or multi-harness use, read the [target index](references/targets/README.md), then load each requested target file and `multi-target.md` when applicable. Do not assume any discovery directory is universal. Ask when the target or scope is unclear, keep one canonical copy, and ensure the frontmatter `name` matches its skill directory.

## Boundaries and safety

- Do not publish secrets, credentials, personal paths, temporary files, or unrelated material. Inspect the files before uploading them.
- Preserve existing files: do not overwrite `README.md`, `AGENTS.md`, `SKILL.md`, or release configuration without comparing them and agreeing on the changes.
- Show the destination, visibility, and planned files, and **ask for explicit confirmation before creating a remote repository, pushing, or changing remote settings**. Preparing local files is not the same as publishing them.
- Before pushing a publication, check the repository's Actions settings and workflow token permissions as described in `references/publish.md`; the default `GITHUB_TOKEN` needs no custom secret. Report inaccessible settings as unverified, not as passing.
- Do not claim that a GitHub Release means `skills.sh` installs a pinned version: verify installation and the release lifecycle separately.
