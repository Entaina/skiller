# Doctor: infrastructure checks

Doctor answers **“Does this environment have the local tools, GitHub authentication, and permissions required for the requested work?”** It does not validate the skill, test discovery or installation, inspect the working tree, or review workflow files. Use [validate](validate.md) for the skill itself and [publish](publish.md) for publication behavior.

This is a read-only checklist, not an executable script. Unless the user narrows the scope, check only the three areas below. Report only what was actually verified.

## Before you start

- Check in the user's environment and adapt commands to its shell.
- Do not install tools, log in, create repositories, push, or change settings without explicit permission.
- Never disclose credentials, tokens, or the full output of authentication commands.
- A tool being present does not prove that it is authenticated or has access to a repository.

## 1. Local tools

Check each tool relevant to the requested workflow and report it on its own line. Do not combine tools into one result.

The usual tools are:

- `skills-ref` for optional Agent Skills format validation.
- `node`, `npm`, and `npx` for skills.sh CLI operations.
- `git` for repository operations.
- `gh` for GitHub authentication and access checks.
- A compatible agent executable when activation testing is requested.

Only check whether each executable is available; functional tests belong to their respective workflows. An absent optional tool such as `skills-ref` is `[OPT]`, not a failure.

## 2. GitHub CLI authentication

If `gh` is available, run `gh auth status`. Report one concise authentication line without account details, hosts, scopes, or tokens. If `gh` is absent, authentication is unverified rather than a duplicate failure.

## 3. Repository and organization permissions

When a target can be inferred from `origin` or supplied by the user, check only the permissions relevant to the requested operation. Examples include:

- Repository read access: `gh repo view <owner>/<repo>`.
- Repository push access: `gh api repos/<owner>/<repo> --jq '.permissions.push'`.
- Repository administration access when settings may need changing: `gh api repos/<owner>/<repo> --jq '.permissions.admin'`.
- Relevant Actions settings or organization policy when publication requires them, such as whether Actions is enabled and whether Actions may create pull requests.

Report each permission separately. A missing value, `403`, or inaccessible organization policy is `[?]`, not a pass or failure. A repository that does not yet exist is also unverified; creating it requires explicit confirmation. Never change a repository or organization setting during doctor.

## Report the results

Use [the doctor report template](../assets/templates/doctor-report.txt) as chat output, not as a command or fenced block. Include only these sections:

1. Local tools — one line per tool.
2. GitHub CLI authentication — one line.
3. Repository / organization permissions — one line per permission checked.

Statuses:

- `[OK]` — performed and passed.
- `[FAIL]` — a required check failed; give one short next step.
- `[?]` — could not verify.
- `[OPT]` — an optional tool is absent.
- `[SKIP]` — the user excluded the check or no target exists.

End with `Result: <n> OK / <n> FAIL / <n> unverified`, counting only `[OK]`, `[FAIL]`, and `[?]`. Do not add discovery results, installation tests, workflow inspection, compatible-agent inventories, Git status, or other diagnostics unless the user explicitly requests them.
