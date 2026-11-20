# Backend implementation continuation

Updated 20 November 2026. The first session verifies its imported context and waits for the user's direction.

## Objective

Help students overcome language barriers to entering STEM. KiKi’s first audience is Odia-medium students entering engineering. The second mentor reinforced the decision to focus the hackathon on a specific student problem. The seven backend directions remain proposal material for planning a student-focused implementation.

## Current decisions

- **Student-led language support.** The learner controls the Odia–English mix. Keep English technical terms stable and track concept understanding, vocabulary, academic English, and practical work independently.
- **Progression.** Concept checks require 60% and chapter tests 80%. Preparation is open anytime. To execute a lab, the student passes the checks for its prerequisites and opens the software. Lab guidance activates once the connection is confirmed.
- **Worked case.** Use the Odia ECE journey and the Analog Modulation lesson ledger. The retained phase-error tutor covers concept `C-AM-08`. Its graph and routing fixtures passed structural checks. The proposed DSB-SC lab is in Simulink Online.
- **Pending verification.** The tutor needs native Odia review, ECE teacher review, and live app verification. Confirm real model execution and workspace observation before treating live lab guidance as available.

## Baseline

Read the [source map](../../context/README.md) and the generated `context/design-thinking/SOURCE.json` for the exact revision and available content. A snapshot of the current Design-Thinking revision includes `docs/plans/kiki-scope-cleanup.md`, `data-model/ANALOG-MODULATION.md`, and `docs/prototypes/ece-phase-error/README.md` under `context/design-thinking/`. For an older pin, use this plan for the current scope and report which source files are absent. [Upstream scope decision](https://github.com/Kikiland-ai/Design-Thinking/blob/main/docs/plans/kiki-scope-cleanup.md)

## Now

Follow the [context boot instructions](../../CONTEXT-BOOT.md) in read-only mode. Load the core sources, verify the snapshot if tools are available, report what was read or missing, and wait for the user's direction.

## Next

Use the Odia ECE journey and Analog Modulation case to discuss the first implementation slice. Begin implementation when the user requests it and carry forward the tutor and Simulink review status.

## Open questions and boundaries

- Actual Odia–English speech intelligibility/pronunciation and timing are untested.
- Graphics scientific fidelity and rendering/runtime dependencies are untested.
- Simulink account/model access, observation and overlay mechanisms are untested.
- Mastery evidence comes from learner responses and practical work. Media consumption is recorded separately.
- Image/diagram anchors and live-screen anchors have separate lifetime/geometry contracts.
- Backend creation, remote push, credentials, and CI results must be recorded from actual execution; importing files does not establish them.

## Session log and exact next action

The Design-Thinking scope cleanup retained the four-file tutor draft with the student prototypes. On first boot, verify the pinned snapshot and report whether it contains the current scope record and tutor draft. After authorized implementation, record the checks, failures, changed files, and exact continuation point here.
