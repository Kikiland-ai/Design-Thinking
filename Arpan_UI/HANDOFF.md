# BB8 handoff — Arpan UI resources

Status: Complete for local resource packaging; UI implementation not started

Updated: 13 October 2026

## Objective and success

User request: create an `Arpan_UI` folder with all necessary documents/resources for Arpan's allotted portions. Success is a readable, portable snapshot containing the current plans, actual data/assets, visual demos and their required local references, plus clear scope/continuation and integrity checks.

## Current state and decisions

The folder copies the local working tree at source commit `806ba09077b0337374369a530a5dca1ae6ca94ad`, including the uncommitted UI plans and new data-model package. Copied files preserve their original bytes and relative source layout under `reference/`. Root BB8/discovery guidance is copied as a separate working reference. Five supplied updated HTML exports are included; the older Downloads walkthrough and duplicate offline ZIP are omitted.

Confirmed product choices are listed in [START_HERE](START_HERE.md): React/Python/Firebase, Google-only sign-in, full laptop web functionality with adaptive phone layouts, current colours and the Analog Modulation/DSB-SC case. Older working docs and prototypes are supporting references. No original source files were modified by packaging.

## Scope, dependencies and risks

Arpan owns the kit, map/lessons/terms/media and lab/hardware presentation. Shared props/routes/schema and the frontend scaffold need agreement with Akshita. Fixture-backed UI can begin before her entire workstream completes; real evidence/services/adapter integration is a later dependency.

Draft ECE/Odia content requires review. Actual speech, image composition/evaluation and Simulink integration are unverified. Copied backend-starter templates contain six anticipated destination links; the manifest records them. Current plan/journey/model/design links resolve in the bundle. There is no installed app runtime, service credential or deployment in this snapshot.

## Now / Next / Later

- **Now, complete:** local resources, start-here instructions, Claude prompt, source manifest and portable reference layout.
- **Next:** Arpan reads the current plans and shares the minimum component/API agreement with Akshita; implement the shared kit and one responsive Analog Modulation lesson slice in the actual frontend checkout.
- **Later:** real Python/media/assessment services, live Simulink connection, expanded hardware work and full release checks.

## Checks and cold-pickup continuation

`verify_bundle.py` checks every copied file's hash and required entry points. Run the ledger/case tests and BB8/discovery checks on the bundled references when needed. Packaging checks establish resource completeness and consistency, not working UI/live services.

Completed packaging checks: 308 copied source-file hashes match; 73 existing local document targets resolve; six future backend-starter destination links are documented; all four ledgers and the bilingual case validate; all 28 case tests pass; BB8 package and Claude/Codex discovery checks pass. Expected draft-content/estimated-weight warnings remain. Native Odia review and actual lab/media execution were not performed. A separate ZIP preserves the same folder for sharing.

**Last completed action:** packaged the authorized current sources and five demos without changing originals.

**Exact next action:** read START_HERE and use CLAUDE_START_PROMPT; agree the shared scaffold/props/contracts and begin Arpan's first slice.

**Do not repeat:** old phase specifications, stale Google+password choices, phone-first sequencing, swapped colours, or demo state treated as observed lab progress.
