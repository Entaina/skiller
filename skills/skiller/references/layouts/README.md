# Layout selection

Read this index whenever locating or moving a skill source. Layout references describe only where the skill unit lives within a repository or project. They treat the skill as an opaque directory and must not define its internal files, metadata, or resource structure; those concerns belong to definition, authoring, and validation.

Choose the relevant reference:

- [Distribution repository](distribution-repository.md): source intended for publication or installation by others.
- [Project-local skill](project-local.md): source maintained directly inside an existing project.

Do not turn every legacy or unusual placement into a supported layout. Inspect existing nonstandard sources in place and handle their migration through authoring and validation guidance.

Target discovery paths, installation, links, and multi-target synchronization belong under `references/targets/`. Before selecting a layout, record the canonical source path, intended distribution, target harnesses, and project/global scope.
