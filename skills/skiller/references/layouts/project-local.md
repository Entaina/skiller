# Project-local skill

Use this layout when the canonical skill source belongs to an existing project rather than a separate distribution repository.

```text
<project>/
└── <canonical-skill-container>/
    └── <skill-name>/    # skill unit
```

This layout does not decide whether the canonical container is also a harness discovery path. Select the target references under `references/targets/` to choose discovery locations, installation, links, and synchronization. A location supported by one harness may be ignored by another.

Commit the skill unit when it should be shared with project contributors. Check project trust and security implications because a project-local skill can instruct a harness to use tools or scripts. Authoring and validation define the unit's internal contents.
