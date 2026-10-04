# Extract a local skill

Use this workflow to copy a skill from a project-local or user-local location into its own distribution repository. Extraction prepares an independent local repository; remote creation and pushing belong to `references/publish.md`.

## Preservation rule

Treat the source skill as read-only by default. Extraction copies the skill; it does not move, rename, replace, unlink, or delete the original. The request to extract a skill never implies permission to remove its source.

Any later cleanup, deletion, or replacement of the original is a separate operation chosen by the user. Show the exact affected path and request explicit confirmation after the extracted copy has been validated. Leaving the original in place is always valid.

## Workflow

1. Consult `references/official-sources.md`, then identify the source path, skill name, current target harnesses, intended audience, and destination repository path. Read `references/layouts/project-local.md` for the source and `references/layouts/distribution-repository.md` for the destination. Read the applicable target files when discovery or target-specific features matter.
2. Validate the source in place with `references/validate.md`. Report existing issues before changing anything. Do not modify the source unless the user separately asks to improve it.
3. Present an extraction plan containing the read-only source, destination, resulting `skills/<name>/` path, files to copy, target-specific features, and references that need adjustment. Inspect an existing destination before writing and do not overwrite files blindly.
4. Inventory the complete skill unit and its dependencies. Check relative references, scripts, assets, files outside the skill directory, personal paths, secrets, private documentation, licenses, project-specific assumptions, and harness-specific metadata. For each external dependency, propose whether to bundle it, replace it, document it as a requirement, or omit it with approval.
5. Create the distribution layout and copy the complete skill unit into `skills/<name>/`. Preserve the original source unchanged. Keep the copied frontmatter `name` aligned with the destination skill directory.
6. Change only the extracted copy to repair paths, remove private material, or improve portability. Do not silently generalize project-specific behavior; obtain approval when extraction changes scope, activation, inputs, outputs, or constraints.
7. Prepare minimal repository documentation if requested. Initialize or connect local Git only after checking the destination. Do not create a remote, change remote settings, or push during extraction.
8. Validate the extracted copy independently. Compare it with the source definition and behavior, check that copied resources resolve from the new location, and test every requested target that is available.
9. Report both paths, validation results, remaining portability limits, and which copy is intended to be the distribution source. State explicitly that the original still exists. If two editable copies will remain, document how the user intends to keep them synchronized or which one is canonical.
10. Continue with `references/publish.md` only when the user asks to publish. Publication still requires its own checks and explicit confirmation for remote side effects.

Extraction is complete when the standalone local repository is valid and the original skill remains untouched. It does not include cleanup of the original location.
