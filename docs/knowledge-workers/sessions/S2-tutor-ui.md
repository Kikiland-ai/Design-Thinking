# S2 · Tutor UI in the student app, entry points, scorecard; organisation view

Owner: Akshita (proposed) · Repo: kiki-web (`apps/web`) · Branch: `feat/tutor-ui` · Tier: T0 (tutor UI), T1 (organisation view) · v0.2 (student-deep scope)
Estimate: tutor UI and entry points 7 h (worst 10) · organisation view 3 h (worst 5) · deploy share 1.5 h · Starts 10:00 · Reports: 13:00, 19:00, 22:00, 01:00 · Rules: [sessions/README.md](README.md)


## Objective and why

Make tutor mode real for the student and visibly state-aware. Bikash reaches it from the C-AM-08 concept page, or from a concept-check question he missed. KiKi walks a decision graph with him while the phase scene moves with the conversation, and the session ends in a scorecard built from his own words. This is the demo's centrepiece. **The graph decides; the model only labels replies** (S3).

## Read first

- `apps/web/src/App.tsx` (route conventions), `features/learning/LessonScreen.tsx` (where the concept page's actions live), the concept-check feedback screen (the assessment state and feedback components), `services/create-services.ts`, auth.
- Reusable kit: `ui/learning/` (Sheet, TermChip, AudioPlayer), `Kiki.tsx` poses (listening, thinking, speaking, asking), `language.ts` and `useDialLevel.ts` (dial notch → which language leads).
- S1's scene control prop on `PhaseRecoveryScene` (ready by 13:00; until then use a local stub prop).
- The graph: `Design-Thinking/docs/knowledge-workers/personas/ece-phase-error/` (`graph.json`, `README.md`). S3 serves it at `GET /tutor/graphs/{id}`.
- Contracts: [05 §4 tutor](../05-contracts-v0.md#4-tutor-mode), [§6 evidence and cohort](../05-contracts-v0.md#6-evidence-and-cohort).

## Deliverables

1. **Tutor screen** in a new `features/tutor/` folder, on a route consistent with the app's conventions (for example `/learn/C-AM-08/talk`):
   - the phase scene, large, driven by each node's `canvas` through S1's prop;
   - the conversation: KiKi's `ack` and `say`, the user's text box, and the node's chips;
   - Kiki's "thinking" pose during the call;
   - the problem card at the top.
2. **Graph map:** a small node-and-edge map from `GET /tutor/graphs/{id}`, with the current node lit, the visited path drawn, and screen-reader labels ("Step 3 of about 8: what the receiver multiplies by").
3. **Language follows the dial.** Notches 1–3 lead with `say.or`; notches 4–5 with `say.en`. Show a small "Machine draft" chip on Odia lines until the team marks them reviewed.
4. **Scorecard:** each metric's level (ok, partial, not yet) with the user's quoted words, coloured by dimension (green concept, red words, yellow expression, blue practice), plus next steps: "Try the phase fault in the lab" and "Revisit placard 2".
5. **Entry points (additive):** a "Talk it through with KiKi" action on the C-AM-08 concept page, and a "Talk it through" link on the feedback for a missed phase question (Q-AM-08-1 or Q-AM-08-2). **Both start at the graph's first node** (hub decision, 03:55). From a missed question, show one context line above the problem card: "You missed a phase question. Let's talk it through."
5a. **Scene behaviour (hub decision, 03:55).** Resolve each node's `canvas.state` from the graph's `scenes[0].states`. Pass `phi`, `highlight`, `hide` and `annotate` to S1's prop, with `locked` on during every probe. Unlock after the conclusion so the student can explore. A node without `canvas` keeps the current scene.
6. **Persist evidence (T1):** show "Talked it through: concept ok, expression partial" on the concept card. Only through an additive API route agreed with S3; don't change the existing rings logic during the build.
7. **Organisation view (T1):** a route such as `/class/analog-modulation` showing an illustrative cohort's gaps per concept, split by type (concept, words, expression, practice), from a fixture in contract §6 shape, labelled "Illustrative cohort".

## Acceptance

- From the C-AM-08 page and from a missed check question, the student reaches the tutor.
- With S3's stub at 13:00 and real routing at 19:00, the whole graph runs to the scorecard.
- The scene follows each node; chips and free text both work; the dial's language is respected.
- Responsive from 390 to 1440 px; keyboard reachable; lint, typecheck, unit tests and build green; a browser test for concept page → tutor → scorecard.

## Coordination and deploy

- Route registration in `App.tsx` and the concept page action are shared files. Keep changes additive and small.
- Use a Firebase Hosting **preview channel** until the 01:00 gate. Production deploy only with the owner's go.

## Starter prompt

```text
You are session S2 (Tutor UI) of the KiKi buildathon (student-deep scope, v0.2). Working repo: kiki-web, apps/web.
Read in order: Google AI Builder/CLAUDE.md; kiki-web AGENTS.md;
Design-Thinking/docs/knowledge-workers/sessions/README.md;
Design-Thinking/docs/knowledge-workers/sessions/S2-tutor-ui.md;
Design-Thinking/docs/knowledge-workers/05-contracts-v0.md sections 4 and 6;
Design-Thinking/docs/knowledge-workers/personas/ece-phase-error/README.md.
Check the branch and status, then tell me your plan for the 13:00 walking skeleton
(tutor screen + entry point + S3 stub + scene cue) before editing. Commit only when I say;
no AI attribution. Report to the hub as sessions/README.md describes.
```
