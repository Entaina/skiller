---
name: skiller
description: Define, author, extract, validate, and publish Agent Skills. Use when someone wants to turn an idea or repeatable task into a skill, improve an existing skill, extract a local skill into its own distributable repository, check its compliance with Agent Skills, or publish it on GitHub for installation with skills.sh and versioning with release-please.
compatibility: Publishing requires git, authenticated gh, GitHub access, and permission to configure GitHub Actions; checking installation requires Node.js and npx.
---

# Skiller

Help take a skill from an idea to a distributable repository. Do not confuse the installable skill with the repository hosting it. Resolve relative paths from this skill's directory when reading references and templates.

## Agree on the outcome

Identify the requested outcome and its completion criteria before acting. Use the conversation and inspected files; ask only for missing decisions. A short follow-up such as "create it and push" continues the agreed publication goal unless the user explicitly narrows it to a Git-only operation.

Keep track of the objective, destination, relevant approvals, evidence, and remaining gaps in the conversation. Do not require a new tracking file. Reuse approvals only for the same scope and destination; changed files or remote effects may need renewed consent. Preparing local files never authorizes publication.

## Control loop: observe → evaluate → act → verify

Repeat this loop until the agreed outcome is demonstrated or progress requires the user:

- **Observe:** inspect the actual state and available evidence. Load the relevant methods below. Do not assume earlier actions succeeded or repeat side effects that have already succeeded.
- **Evaluate:** compare the whole state with the completion criteria, not just the last command. Mark each criterion satisfied, missing, or unverified; use not applicable only with a reason. If all required criteria are satisfied, stop. Otherwise choose the next gap that can be resolved within scope.
- **Act:** perform the smallest permitted action that resolves that gap, using the applicable reference. For an inspection-only request, report the gap instead of modifying anything. Pause for missing decisions, authorization, or prerequisites; do not silently omit required work.
- **Verify:** inspect the resulting artifact or command result, record concrete evidence, then evaluate the whole outcome again. An attempted command, existing file, or successful push is not proof of a complete publication.

Do not repeat a failing action unchanged. If there is no progress, stop and explain the blocker and next decision. Bound waits for asynchronous checks; report pending work rather than polling forever. Do not broaden the goal, invent more improvements, recreate repositories, reinstall unnecessarily, or publish another version to keep the loop moving.

On completion or pause, state the achieved outcome, evidence, and outstanding gaps. Distinguish local preparation, remote upload, verified publication, and an actual release. For doctor-only requests, retain the narrow report format in its reference instead of adding unrelated diagnostics.

## Completion criteria by outcome

Apply only the criteria for the agreed scope:

- **Definition:** reviewable capability, boundaries, inputs, outputs, constraints, and acceptance examples; no files or destination choices required.
- **Authored or extracted skill:** approved behavior materialized in the selected layout, required resources and references intact, validation results and behavioral-test limitations reported; extraction also preserves the original. A minimal local skill does not require distribution infrastructure.
- **Distribution repository prepared:** the skill is ready locally, and the repository has a README with actual identity, installation command, access requirements and versioning explanation; contributor instructions; and the release-please workflow, configuration and manifest for the selected branch and intended first version. Inspect content and coherence, not just file existence. Follow the publication reference for strategy-specific files. Remote authorization may still be pending.
- **Publication verified:** local distribution criteria plus the agreed remote/branch and push verified, remote discovery and temporary installation tested, and Actions/release-please results inspected. Verify the release PR and its version when releasable changes exist; an already-published repository with no releasable changes need not produce another PR. Missing or waived checks remain explicitly unverified, not passed. A push alone is only an upload.
- **Release, when separately requested:** the authorized release PR is merged and the expected tag and GitHub Release are verified. Publication normally stops with the release PR open; never merge it merely to satisfy the loop.
- **Validation or doctor report:** requested checks performed where possible and findings distinguished from blocked or unverified checks. A complete report does not mean the skill or infrastructure passed; do not repair or publish as an unsolicited next step.

For end-to-end creation or extraction, cover all agreed local and publication outcomes, with human review before publication. For an explicitly Git-only request, verify that upload and disclose excluded publication work without adding it.

## Load methods based on the next gap

- **Define**: read [official sources](references/official-sources.md) and [define](references/define.md). Establish scope, activation, constraints, and acceptance criteria without choosing paths or writing files.
- **Doctor**: read [doctor](references/doctor.md). Unless the user explicitly narrows the scope, check only local tools, GitHub CLI authentication, and relevant repository or organization permissions. Report each local tool and each permission on its own line; do not run skill discovery, installation, validation, workflow inspection, or unrelated diagnostics.
- **Author or improve**: read [official sources](references/official-sources.md), [author](references/author.md), and [validate](references/validate.md). Materialize an approved definition without redefining its scope. If behavioral requirements are unclear, return to define.
- **Extract**: read [official sources](references/official-sources.md), [extract](references/extract.md), and [validate](references/validate.md). Copy a project-local or user-local skill into an independent distribution repository. Never remove or replace the original as part of extraction.
- **Validate**: read [official sources](references/official-sources.md) and [validate](references/validate.md). Inspect the skill's own structure and behavior; report issues before changing existing content. Use [doctor](references/doctor.md) separately if environment checks are needed.
- **Publish**: read [official sources](references/official-sources.md), [doctor](references/doctor.md), [validate](references/validate.md), and [publish](references/publish.md). Check infrastructure with doctor and the skill itself with validate. Accept an existing skill; do not re-author it by default.

Consult the current official documentation listed in `references/official-sources.md` before defining, authoring, extracting, validating, or writing installation commands. If it is unavailable, say so and do not claim that unverified behavior has been checked.

## Choose the destination

Read the [layout index](references/layouts/README.md) during authoring or extraction whenever locating or moving a skill source, then load the file for the selected layout. Layout references cover only supported repository placement: distribution repositories and project-local sources. Treat other existing placements as migration cases under authoring and validation rather than adding a layout for every exception. Use define, author, and validation guidance for the skill unit's behavior and internal structure.

For project-local, global, or multi-harness use, read the [target index](references/targets/README.md), then load each requested target file and `multi-target.md` when applicable. Do not assume any discovery directory is universal. Ask when the target or scope is unclear, keep one canonical copy, and ensure the frontmatter `name` matches its skill directory.

## Boundaries and safety

- Do not publish secrets, credentials, personal paths, temporary files, or unrelated material. Inspect the files before uploading them.
- Preserve existing files: do not overwrite `README.md`, `AGENTS.md`, `SKILL.md`, or release configuration without comparing them and agreeing on the changes.
- Extraction is copy-only: never delete, move, rename, replace, or relink the original skill unless the user requests that separate operation and explicitly confirms its exact path.
- Show the destination, visibility, and planned files, and **ask for explicit confirmation before creating a remote repository, pushing, or changing remote settings**. Preparing local files is not the same as publishing them.
- Before pushing a publication, check the repository's Actions settings and workflow token permissions as described in `references/publish.md`; the default `GITHUB_TOKEN` needs no custom secret. Report inaccessible settings as unverified, not as passing.
- Do not claim that a GitHub Release means `skills.sh` installs a pinned version: verify installation and the release lifecycle separately.
