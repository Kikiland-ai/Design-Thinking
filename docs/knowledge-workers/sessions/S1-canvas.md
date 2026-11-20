# S1 · Canvas: narration-synced canvas, layout, and the shared scene control

Owner: Arpan (proposed) · Repo: kiki-web · Branch: `feat/canvas-sync` · Tier: T0 · v0.2 (student-deep scope)
Estimate: 5 h (worst 8) · Starts 10:00 · **Scene control prop by 13:00 (S2 depends on it)** · Sync done 15:00 · Reports: 13:00, 15:00, 19:00 · Rules: [sessions/README.md](README.md)

## Objective and why

1. On the C-AM-08 placard, the canvas moves on its own as KiKi narrates. When the narration says the carrier slips to 60°, the scene goes to 60° and marks the recovered signal. On wide screens the canvas sits beside the text. This is a pending actionable from Arpan, and the opening moment of the demo.
2. **One control prop, two drivers.** The same optional prop lets tutor mode (S2) set the scene per graph node. Build it once, and build it first.

**Demo concept:** C-AM-08 (phase recovery), assumed. Confirm with Arpan at kickoff before timing cues.

## Read first (kiki-web, from the 20 Nov code map)

- `apps/web/src/ui/learning/AudioPlayer.tsx`: plain `<audio>`; `currentTime` is private state set in `onTimeUpdate` (about L176); the handle exposes only `pause()`.
- `apps/web/src/features/learning/LessonScreen.tsx`: the placard `<article>` (about L256–325) renders title → Listen → text → optional English → `scenesFor()` scenes → sources; player copy about L276.
- `LessonScreen.module.css` (single column below 1200 px, about L307; 68ch text, L331; steps column at 1200 px or wider, L338); `sketchbook.css` (learning area 1180 px, about L67).
- `features/learning/scenes.tsx` (trusted renderer registry), `CamCanvas.tsx` (copy at L24), `PhaseRecoveryScene`, `DsbDiagrams.tsx:33` (term chip → highlight: the model to follow), `src/media/cam-models.mjs` (slider step grid about L6).
- The C-AM-08 scene's authored `walkthrough` (`{target, mark, dim, say}`): validated but never rendered. Use it for marks and highlight targets.
- `contracts/concept-media.ts:23` and `apps/api/.../media_models.py:38-42` (timing is `clip_duration_only`); `apps/web/CONCEPT_MEDIA.md:161`, which is why the cues are labelled manual.
- The student tutor graph draft: `Design-Thinking/docs/knowledge-workers/personas/ece-phase-error/README.md`, which lists the scene states tutor mode will request.
- Contracts: [05 §2 cue track](../05-contracts-v0.md#2-cue-track-shared-by-the-ece-sync-and-pack-lessons), [§3 scenes](../05-contracts-v0.md#3-scenes).

## Deliverables

1. **Scene control prop, by 13:00.** An optional, backward-compatible prop on `PhaseRecoveryScene` (and `CamCanvas` if cheap). Without the prop, behaviour is unchanged. It takes:
   - **`phi`:** the angle in degrees, 0–180, step 15. The scene's existing local state, seeded from `scene.controls[0].default` (`PhaseRecoveryScene.tsx:12-14`).
   - **`highlight`:** target ids: `aligned-trace`, `recovered-trace`, `recovery-fraction` (existing test ids), or the walkthrough targets (`relative phase error`, `frequency mismatch`, `Carrier mismatch`).
   - **`hide`:** targets to hide. Add `data-testid="comparison-presets"` to the preset button group (about L41). The tutor hides it and `recovery-fraction`, because they print the answers ("cos = 0.50", "cos = 0.00").
   - **`annotate`:** walkthrough marks.
   - **`locked`:** disables the slider and presets during a tutor question.

   When unlocked, a manual slider move takes over until the next external update. The named states the tutor uses (`aligned`, `phi-60-trace`, `phi-60`, `phi-90`, `recap`) are defined in `personas/ece-phase-error/graph.json` (`scenes[0].states`).
2. **Audio clock.** `onTime(t)` exposed from AudioPlayer through NarrationPlayer into LessonScreen state (time updates or `requestAnimationFrame`).
3. **Cue loader and hook.** Cue files at `features/learning/cues/<renditionId>.json` in the shared format; `useCueTrack(time, cues)` returns the last cue with `t ≤ time`.
4. **Cues for C-AM-08, Odia and English:** 6–10 per clip. Tip: `ffmpeg -i clip.wav -af silencedetect=noise=-35dB:d=0.25 -f null -` lists pauses (sentence boundaries); a person assigns each sentence a state.
5. **Layout.** At 1200 px and wider, the canvas sits beside the placard text and stays in view (sticky) while the text scrolls; stacked below that. Check 390, 768, 1280 and 1440 px.
6. **Copy.** Replace "no sentence timing" (`LessonScreen.tsx:276`, `CamCanvas.tsx:24`) with an honest "Visuals follow the narration (manual timing)".

## Acceptance

- Playing C-AM-08 moves the scene through the authored states at the right sentences, in both languages.
- Seeking re-syncs, pausing holds, speed changes stay in sync, and reduced motion shows states without animation.
- S2 can drive the same scene from a tutor node through the prop.
- Nothing overflows at the four widths. Existing tests stay green; add unit tests for cue selection (seek, pause, rate) and one browser test.

## After 15:00, if green

Help S2 with tutor screen polish, then demo assets. React scene templates for trading and streaming are **Tier 2 only** (a live replay); the breadth videos draw their own visuals.

## Do not touch

Lab files (see the rules); ECE contract types beyond optional props; hash-pinned scene and manifest files.

## Starter prompt

```text
You are session S1 (Canvas) of the KiKi buildathon (student-deep scope, v0.2). Working repo: kiki-web.
Read in order: Google AI Builder/CLAUDE.md; kiki-web AGENTS.md;
Design-Thinking/docs/knowledge-workers/sessions/README.md;
Design-Thinking/docs/knowledge-workers/sessions/S1-canvas.md;
Design-Thinking/docs/knowledge-workers/05-contracts-v0.md sections 2 and 3;
Design-Thinking/docs/knowledge-workers/personas/ece-phase-error/README.md.
Confirm the demo concept with me (C-AM-08 assumed), check the branch and status, then tell me
your plan, starting with the scene control prop S2 needs by 13:00. Commit only when I say;
no AI attribution. Report to the hub as sessions/README.md describes.
```
