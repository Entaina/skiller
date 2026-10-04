# Distribution repository

Use this as Skiller's default source layout for a repository intended to distribute one or more skills:

```text
<repository>/
├── README.md
├── skills/
│   └── <skill-name>/    # skill unit
└── ... repository infrastructure
```

Use the same layout for a one-skill repository. Keep repository documentation, CI, release configuration, and other infrastructure outside the skill unit. Authoring and validation define what belongs inside that unit.

This is a source layout, not a universal harness discovery path. Validate installation separately for every requested target. A target may install, copy, or link `skills/<name>/` into another location.
