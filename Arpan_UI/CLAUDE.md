# Claude Code repository instructions

@AGENTS.md

BB8 skills are exposed under `.claude/skills/`. For coordinated work, invoke
`/bb8` or ask to use BB8. The wrappers point to the canonical instructions
under `bb8/skills/`; load only the selected skill and the references it needs.

Do not assume all repository files were loaded or indexed. For a repo action,
identify the explicitly scoped files needed, read them, and state what was
actually inspected. Follow repository instructions and the user's authorization.

Commits and pull requests made for the user must not credit Claude: no
`Co-Authored-By: Claude` trailer, no "Generated with Claude Code" line, and no
other text saying Claude or an AI made the change.
