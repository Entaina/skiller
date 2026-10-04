# Official sources

Consult the relevant pages **in their current form**, rather than relying only on remembered links or examples. If the connection fails, state which checks remain outstanding; do not invent tool behavior.

## Agent Skills format and quality

- [Specification](https://agentskills.io/specification.md): `SKILL.md` requirements, frontmatter, names, references, and progressive disclosure. Consult when building, moving, or validating a skill.
- [Best practices](https://agentskills.io/skill-creation/best-practices.md): **always consult before designing or reviewing a design**; ground the skill in real expertise, choose a coherent scope, and test it on real tasks.
- [Descriptions and activation](https://agentskills.io/skill-creation/optimizing-descriptions.md): consult when writing or debugging the `description` field.
- [Evaluation](https://agentskills.io/skill-creation/evaluating-skills.md): consult when planning quality and activation tests.

## Creation, discovery, and installation

- [Official skills.sh CLI](https://github.com/vercel-labs/skills#readme): consult before using `npx skills init`, `npx skills add ... --list`, or writing an installation command in the README. Check that the layout and options are still supported.
- [CLI reference](https://skills.sh/docs/cli): consult as a supplement; cross-check specific options against the project's README if they differ.
- For project-local, global, or multi-harness use, follow `references/targets/README.md` and consult the current official documentation of every target before selecting a path or claiming automatic discovery. The Agent Skills specification does not define a universal container directory. Record stable target-specific guidance in `references/targets/<target-id>.md` only when a real task requires it, and keep that target's links in its own `## Official sources` section.

`skills.sh` installs skills hosted on GitHub; there is no additional package registry to publish to. Appearance in its public directory depends on its discovery mechanisms, not on creating a GitHub Release.

## Releases

- [Official release-please action](https://github.com/googleapis/release-please-action#readme): check the format, permissions, strategy, and `GITHUB_TOKEN` limitations before preparing or troubleshooting a publication.
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/): consult when advising on the commit messages that release-please interprets.
