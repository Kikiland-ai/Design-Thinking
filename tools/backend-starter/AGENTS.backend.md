## Kiki backend context and implementation

Before substantive work, read `SETUP.md`, `context/README.md`, the source prototype directions and handoff, then the relevant v2 contracts. Use the source precedence rules; old mock UI and build-plan defaults do not supersede the latest confirmed journey or the user's current instructions.

Treat `context/design-thinking/` as a pinned source snapshot. Do not casually rewrite its documents or types as implementation progresses. Record new decisions in `docs/decisions/`, current work in `docs/plans/active.md`, and implement reconciled runtime schemas in `contracts/`. An explicit source refresh must update the source revision and file hashes together.

Implement small vertical slices with actual runtime validation. Maintain separate concept, terminology, English, and practical evidence. The student controls language and performs lab actions. GIF export retains an editable semantic scene. Mixed-language speech returns real timing cues. Image annotation and live screen annotation have separate targets/lifecycles. No mock implies a live provider/tool works.

Use `python scripts/verify-context.py`, BB8 checks, and the backend's actual test commands. Do not commit credentials or credit an AI in commit/PR messages. Update the active plan with what ran, what failed, and the exact next action at session end. Carry continuity through these files rather than assuming chat memory transfers.
