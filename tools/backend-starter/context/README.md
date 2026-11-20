# Product source of truth and reading order

The snapshot in `design-thinking/` preserves original paths so document links, media/component references, and ledger scripts stay usable. It includes current and older documents; inclusion does not make every document current.

## Authority and precedence

1. The user's current explicit instructions and subsequently agreed backend decisions.
2. The [active plan](../docs/plans/active.md) records the current STEM scope. The snapshot’s `design-thinking/docs/plans/kiki-scope-cleanup.md`, when present, preserves the scope decision and reasoning. `design-thinking/docs/ux/student-journey-odia-ece.md` governs the confirmed learner flow, progression, colours, language control, and lab activation.
3. The Analog Modulation case and phase-error tutor draft, when present, give the current worked example. The seven prototype directions and October handoff provide earlier backend proposals for speech, graphics, and both annotation modes.
4. Original vision/architecture, working docs, and handover: rationale and detailed feature references, subject to the newer decisions above.
5. Types, ledgers, component kit, and clickable demo: implementation seeds, requiring the reconciliation identified in the prototype proposal.

The Simulink recommendation is a proposed experiment and an untested connection. Original Odia text needs review; sample past-paper weights are estimates. Archives and the old mock rectifier guide are historical/reference material. Private live Claude documents were not accessed; inaccessible links are not transferred knowledge.

See [KNOWN-GAPS.md](KNOWN-GAPS.md) for the pre-existing missing local reference and pending capability trials.

The carryover baseline includes the subsequent component/guide/artwork updates through `73d16c0`: concept is green and practical is blue. The prototype proposal's earlier audit mentions the old component colours; that particular component issue is now resolved in the imported references. Remaining schema/timing/scene/anchor reconciliation still applies.

## Open these first

- [Active plan and scope](../docs/plans/active.md)
- [Current student journey](design-thinking/docs/ux/student-journey-odia-ece.md)
- [Lab recommendation](design-thinking/docs/ux/experiment-recommendation-simulink.md)
- For the latest scope and worked example, open `design-thinking/docs/plans/kiki-scope-cleanup.md`, `design-thinking/data-model/ANALOG-MODULATION.md`, and `design-thinking/docs/prototypes/ece-phase-error/README.md` where included in the pinned snapshot.
- [October prototype directions](design-thinking/docs/prototypes/backend-prototype-directions.md) and [handoff](design-thinking/docs/plans/backend-prototype-handoff.md)
- [Data-model README](design-thinking/data-model/README.md), then `types/content.ts`, `types/intake.ts`, and `types/learner.ts`

For speech/graphics/annotation work, inspect component READMEs for `KikiWalkthrough`, `VoiceScope`, `LabGuide`, `Spotlight`, and `AnswerOverlay`, and relevant `bundle.js` sections. For scope/rationale, read the original DOCX files and working-doc feature specs. Do not load every file by default.

## Updates and ownership

`SOURCE.json` pins a reviewed commit and hashes of copied product sources. A backend session does not silently pull updates from upstream. When refreshed, compare changes against backend decisions/contracts, update this baseline explicitly, and record what changed. Keep runtime contracts separate from unchanged source types; document migrations and compatibility in backend ADRs.
