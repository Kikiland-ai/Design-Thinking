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
