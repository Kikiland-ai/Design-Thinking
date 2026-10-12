# Repository agent instructions

## BB8

For consequential or multi-step work, read `bb8/AGENTS.md` and use
`bb8/skills/bb8/SKILL.md` with `bb8/harness/system-prompt.md`. Follow the
applicable repository instructions and the user's explicit task scope.
Use an engineering specialist for implementation, debugging, review, or tests.
For simple tasks, invoke the relevant specialist directly where useful.

The bundled files provide reference guidance. Native plugin discovery requires
separate host registration; do not claim it occurred merely because these
files exist in the checkout. Host tools perform authorized reads, edits, and
checks. Do not retrieve prior projects, chats, memory, vaults, or credentials.

Validate the BB8 package from the repository root with:

```sh
python bb8/adapters/reference/bb8.py validate
```

## Skill discovery and file inspection

Codex repository skill wrappers live under `.agents/skills/`. Claude Code
wrappers live under `.claude/skills/`, and `CLAUDE.md` imports these instructions.
The canonical skill content remains in `bb8/skills/`. Read the selected skill
and resolve its references relative to that canonical file.

For each repo task, identify and read the relevant files within the user's
explicit scope. Report what was inspected and what was unavailable. Do not
claim every file was indexed or loaded. A file catalogue is a navigation aid,
not evidence that a host loaded all content or created an embedding index.

Verify generated discovery files with:

```sh
python bb8/adapters/discovery/sync.py --check
```
