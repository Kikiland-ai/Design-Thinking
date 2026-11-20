# Known source and capability gaps

## Earlier source reference

The October pin of `design-thinking/docs/ux/student-journey-odia-ece.md` links to:

`../../../UX Working Doc — Bilingual STEM Learning (AI Builder Cup).md`

That file was outside the Design-Thinking repository. The latest journey points to the checked-in working doc export for background and still identifies the original as an external source. Older pins retain the original link.

Private live Claude artifacts are referenced but were not retrieved. Their URLs are not imported document contents. The source snapshot preserves all working relative links; it does not invent files for inaccessible references.

## Product capability trials still pending

- Real mixed Odia–English synthesis, pronunciation lexicon, and reliable timing cues.
- Scientific/linguistic review of generated graphics and placeholder Odia.
- A synchronized media player beyond the old fixed-timer walkthrough.
- Selection and execution of the proposed DSB-SC experiment in Simulink Online.
- A supported real-tool observation/highlighting connection; the existing lab guide is an in-app mock.
- Backend runtime, credentials, provider quotas, and datastore/authorization integration.

These are explicit tasks to resolve, not hidden prerequisites treated as already complete. Keep fixture/live status and trial results in `docs/plans/active.md`.

## Resolved during source carryover

The earlier prototype review identified old component colour assignments. The carryover now includes the component guides, bundles, tokens, and Kiki artwork updates through `73d16c0`, aligning green with concept and blue with practical. This source update does not establish speech timing, general image markup, or real-tool guidance.
