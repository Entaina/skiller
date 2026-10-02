# Validate a skill

Consult the specification and evaluation guides in `references/official-sources.md`. Report failed checks separately from checks you could not run; never claim a test passed if you did not run it.

1. Check `skills/<name>/SKILL.md`, valid YAML, required fields, `name` rules, agreement between name and directory, and the existence of referenced paths. If an existing skill has a different layout, validate its current state before proposing changes.
2. Check that the description explains what the skill does and when to use it, that instructions are specific, and that resources, scripts, permissions, and boundaries are documented. Look for credentials, local paths, generated files, and broken links.
3. Run `skills-ref validate skills/<name>` if doctor confirmed it is available (check its current syntax in the specification). This checks the skill's format; manual review remains necessary. Tool availability belongs to doctor, not this checklist.
4. Try at least two real requests that should activate the skill and one similar request that should not. Review the result, not just whether the agent read the file. Record what was tested and what remains. If the agent client does not expose activation, say so explicitly; check client availability in doctor.
5. Fix issues, validate again, and seek human review of the instructions and behavior before publishing.

Local tool availability, GitHub CLI authentication, and repository or organization permissions belong to [doctor](doctor.md), not skill validation. skills.sh discovery and installation are separate workflow checks.
