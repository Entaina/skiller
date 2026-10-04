# Multiple targets

## Official sources

- Read the `Official sources` section in every selected target file.
- [Official skills.sh CLI](https://github.com/vercel-labs/skills#readme), when considering its multi-target installation support.

Read every individual target file requested by the user before choosing a location. Keep one canonical editable skill directory. When targets require different discovery paths, a project can use this topology:

```text
<project>/
├── skills/
│   └── <skill-name>/          # canonical skill unit
├── <target-a-container>/
│   └── <skill-name> -> ../../skills/<skill-name>
└── <target-b-container>/
    └── <skill-name> -> ../../skills/<skill-name>
```

The links are illustrative. Confirm support in every selected target and operating environment before creating them. A neutral canonical directory is not automatically discoverable.

Prefer, in order:

1. One discovery location explicitly supported by every requested target.
2. A supported multi-target installer that points target locations to one canonical copy.
3. Project-managed symbolic links after confirming every target and platform follows them.
4. Synchronized copies only when installation or links cannot work.

Do not call a path universal merely because several targets support it. Record the canonical source, every installed path, installation method, and reload command.

Validate each target independently. Report format validity, path discovery, loading, and activation as separate results; success in one harness does not prove success in another.
