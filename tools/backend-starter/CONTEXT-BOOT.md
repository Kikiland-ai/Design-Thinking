# Start a session by loading context only

The first task in a new session is to establish the right project context and then wait for the user's thoughts. The user has explicitly said they do not want the session to start building automatically. This protocol supersedes earlier startup prompts or handoff notes that immediately proposed scaffolding an API.

## Read in this order

1. `AGENTS.md`, `SETUP.md`, and this file: current session scope and operating rules.
2. `context/README.md`, `context/KNOWN-GAPS.md`, and `context/design-thinking/SOURCE.json`: source precedence, unavailable references, and the exact imported revision. The manifest inventories files; it does not mean their contents have been read.
3. [Active plan](docs/plans/active.md) for the current STEM scope, completed work, pending reviews, and first-session boundary.
4. Within `context/design-thinking/`, read `docs/plans/kiki-scope-cleanup.md` for the scope decision when present. Read `docs/ux/student-journey-odia-ece.md` for the confirmed learner flow. Use `data-model/ANALOG-MODULATION.md` and `docs/prototypes/ece-phase-error/README.md` when present, then `docs/ux/experiment-recommendation-simulink.md` for the proposed lab and its trial. Report files absent from an older pin.
5. `context/design-thinking/docs/prototypes/backend-prototype-directions.md` and `docs/plans/backend-prototype-handoff.md` within that snapshot: the revised seven directions and their reasoning. Their suggested build order is background, not permission to execute.
6. `context/design-thinking/data-model/README.md` and `types/content.ts`, `types/intake.ts`, `types/learner.ts` within that data-model directory: reusable contracts and reconciliation needs.
7. The original `AI_Builder_Cup_Product_Vision.docx` and `AI_Builder_Cup_Technical_Architecture.docx` in `context/design-thinking/`: purpose, intended agent/workflow boundaries, and initial constraints. Extract readable text with available file tools; if unavailable, report that rather than claiming to have read them.

Use supporting working-doc sections, transcript passages, and component/ledger sources only as needed to resolve something in the core context. Do not automatically read every historical screen, asset, or archived document. The source index points to the right materials without treating all 130 files as equally current.

Apply the [source precedence](context/README.md). Use current user instructions and agreed decisions first, then the active scope and confirmed journey. Use the prototype directions and original demo as references. Report any unresolved decision before proceeding. Technical stack and module recommendations remain proposals until the user chooses how to proceed.

## Verify without starting work

If a checkout and command tools are available, use read-only repository inspection to confirm the selected repo/branch and run `python scripts/verify-context.py`. A source integrity pass verifies the snapshot bytes, not full source comprehension. Do not install tools or dependencies merely to complete this check. If the checkout, required files, or read capability is missing, state exactly what could not be loaded.

Do not scaffold code, create implementation plans/files, install dependencies, start emulators/services, invoke live model/render/tool trials, change configuration, commit, push, or deploy as part of context boot. This also means do not update the active plan during the read-only pass. User thoughts and design discussion do not automatically authorize implementation; proceed with building when the user actually requests it.

## Report context readiness, then wait

Finish with a short report containing:

- Repository/branch and pinned source revision actually inspected.
- Core files actually read, plus any required source that was inaccessible.
- A concise understanding of the product, the seven prototype directions, and the two annotation uses.
- Confirmed decisions versus recommendations, pending trials, and any consequential source conflict.
- Confirmation that no implementation has begun and the session is waiting for the user's thoughts.

A short prompt that invokes this protocol is sufficient if the next session has access to this checkout. It cannot guarantee retrieval in a session with no repo/file access; the readiness report makes that failure visible.
