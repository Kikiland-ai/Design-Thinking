# Worker sessions: shared rules and how to report

Each worker session owns one workstream from the [build plan](../02-build-plan-24h.md). It reads its brief, builds against [contracts v0](../05-contracts-v0.md), and reports to the hub. The hub (S0) holds the [mission plan](../MISSION.md), decides interface changes and integrates.

## Start a session

Open Claude Code in the repo the brief names. Paste the brief's **starter prompt**. The session reads, in order:

1. The workspace `CLAUDE.md` (`Google AI Builder/CLAUDE.md`) and the repo's own `AGENTS.md` / `CLAUDE.md`.
2. This file.
3. Its brief in this folder.
4. The contract sections the brief lists.

It then states its plan to its owner before editing anything.

## Rules for every session

1. **Stay in your lane.** Edit only the paths your brief lists. If you need something from another lane, ask in a report; don't edit it.
2. **Never touch the lab-polling lane:** `apps/web/src/features/labs/lab-capture.ts`, `lab-cadence.js`, the capture, WebSocket and check-stream code in kiki-web and kiki-backend, and `kiki-backend/prototypes/lab_tracking/*` (frozen by CI). A teammate is optimising these separately.
3. **Don't change the ECE contracts** (`contracts/learning.ts`, `concept-media.ts`, `cam-canvas.ts`, `learning_models.py`, `media_models.py`) except where your brief says so. S1 may add optional, backward-compatible props only.
4. **Contracts are owned by the hub.** Additive optional fields: go ahead, then report. Renames, removals and type changes: propose in a report and wait.
5. **Git.** Work on your brief's feature branch from an up-to-date `main`. Commit only when your owner says so, as `arpanvihan5-sketch` (check `git var GIT_AUTHOR_IDENT`), with **no AI attribution** in messages or PRs. Never push, merge, deploy or change cloud resources without your owner's explicit go.
6. **Secrets.** Gemini keys stay server-side (`apps/api` reads them from the environment or Secret Manager). Never print or commit `.env*` contents.
7. **Honesty.** Label illustrative data as illustrative, unreviewed languages as machine drafts, and manual timing as manual. Don't fake a live capability with a canned response unless it is labelled as a fallback.
8. **Measure.** Record time spent against your estimate, plus the numbers your brief asks for (E1–E6).
9. **Tests.** Keep `npm run lint`, `typecheck`, `test` and `build` green in `apps/web`, and `uv run pytest` green in `apps/api`. Add focused tests for what you build.

## Report to the hub

**When:** at each checkpoint your brief lists, whenever you are blocked, and whenever you want to change a contract.

**Where:** write `../reports/<session>-H<hour>.md`, for example `reports/S3-H04.md`, using the template in [reports/README.md](../reports/README.md).

**Notify:**

- **Sessions on Arpan's machine:** send the hub a cross-session message, to `google-ai-builder-de`. Make the first line a self-contained status, for example: `S3 report H4: amber, Gemini rejects the enum schema; workaround in progress. See docs/knowledge-workers/reports/S3-H04.md`. If the message is held for approval, the report file still stands.
- **Sessions on other machines:** commit the report file to the shared docs branch when your owner allows, or paste it into the team chat. Arpan relays it to the hub.

**What the hub does with it:** triages it at the gate, updates the session board and decisions in `MISSION.md`, answers contract proposals, and sends re-briefs if scope changes.

## Status colours

- **Green:** on plan for the next gate.
- **Amber:** at risk; a cut line may apply; the hub should know now.
- **Red:** blocked or will miss the gate; needs a decision.
