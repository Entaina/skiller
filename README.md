# skiller

Define, author, extract, validate, and publish Agent Skills.

## Installation

Install this skill from GitHub with [skills.sh](https://skills.sh/):

```bash
npx skills add entaina/skiller --skill skiller
```

By default, installation is local to the current project. Add `-g` to install it globally. See the [CLI documentation](https://github.com/vercel-labs/skills#readme) to select an agent or update an installation.

Review a skill's contents before installing it. Private repositories require GitHub access.

## Requirements

- **Install and check discovery:** Node.js with npm and `npx`, plus network access. You also need a compatible agent to use the installed skill.
- **Validate:** Review the skill's structure and behavior; `skills-ref` is optional for format checks.
- **Publish:** additionally `git`, an authenticated [GitHub CLI (`gh`)](https://cli.github.com/), repository access, and permission to configure GitHub Actions. Release Please runs in GitHub Actions using its default `GITHUB_TOKEN`; it does not require a local install or a personal access token.

Doctor checks only local tools, GitHub CLI authentication, and relevant repository or organization permissions. It reports each tool and permission separately. See [doctor](skills/skiller/references/doctor.md); [validate](skills/skiller/references/validate.md) checks the skill itself.

## Versions

Changes are managed with [release-please](https://github.com/googleapis/release-please-action): conventional commits (`feat:`, `fix:`) feed a release PR with a changelog. Merging that PR creates a tag and GitHub Release. The installation command above installs the skill from the repository; it **does not pin a GitHub Release version**.

## Contributing

Use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) for merged changes so release-please can determine the next version. For example, `feat: add a use case` or `fix: correct an instruction`. Agent instructions are in `skills/skiller/SKILL.md`.
