# Validate a skill

Consult the specification and evaluation guides in `references/official-sources.md`. Report failed checks separately from checks you could not run; never claim a test passed if you did not run it.

1. Check `<skill-directory>/SKILL.md`, valid YAML, required fields, `name` rules, agreement between name and directory, and the existence of referenced paths. Validate the canonical source and destination against the selected file under `references/layouts/`. For project-local, global, or multi-harness use, apply every selected file under `references/targets/` and verify that each intended harness officially discovers the chosen location. If an existing skill has a different layout, validate its current state before proposing changes.
2. Compare the authored skill with its approved definition when available. Check that scope, activation boundaries, inputs, outputs, permissions, and constraints have not drifted. Check that instructions are specific and that resources and scripts are documented. Look for credentials, personal paths, generated files, and broken links.
3. Run `skills-ref validate <skill-directory>` if doctor confirmed it is available (check its current syntax in the specification). This checks the skill's format; manual review remains necessary. Tool availability belongs to doctor, not this checklist.
4. Run the acceptance requests from the approved definition, or define equivalent cases if none exist: at least two that should activate the skill and one similar request that should not. For a project-local skill, test discovery and activation in every requested harness when available. Review the result, not just whether the harness read the file. Record what was tested and what remains. If a harness does not expose activation, say so explicitly; check client availability in doctor.
5. Fix issues, validate again, and seek human review of the instructions and behavior before publishing.

Local tool availability, GitHub CLI authentication, and repository or organization permissions belong to [doctor](doctor.md), not skill validation. skills.sh discovery and installation are separate workflow checks.
