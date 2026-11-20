# S6 · Breadth videos: the same KiKi, coaching a trader and a streamer

Owner: Arpan (proposed; made the October submission video with Hyperframes), with Aditya as backup · Where: videos in `Google AI Builder/breadth-videos/` (outside the repos: large binaries); sources and notes alongside them · Tier: T1 · v0.2 (student-deep scope)
Estimate: 6 h (worst 9) · Starts 15:00 · Trader cut 21:00 · Streamer cut 24:00 · Final with end card 01:00 · Reports: 21:00, 01:00 · Rules: [sessions/README.md](README.md)


## Objective and why

Jurors must believe the system that runs the student route scales to very different sectors while staying deep and personalised for each. Two videos of 45–60 s each show KiKi's three modes and its evidence in a trader's world and a streamer's world. They use the sector's own visuals, terms and language, in the same KiKi look. They are **prototypes and say so**; the student route is the working build.

## Inputs

- **Ready (04:10, hub-checked):** storyboards (58 s each, shot lists with on-screen text, narration, colours and the generic terminal and dashboard specs), scenario numbers and graph-shaped tutor flows with the exact scripted turns, in `Design-Thinking/docs/knowledge-workers/personas/trader/` and `personas/streamer/` (`storyboard.md`, `scenario.json`, `tutor-flow.json` → `scriptedPath`, `persona.md`). Plausibility notes from reviewers arrive by 15:00.
- **Numbers on screen:** the trader's loss split (+₹40 move, −₹48 IV, −₹23 time) is a Shapley average, so it doesn't depend on order. If a reviewer changes a number, regenerate with `personas/tools/` (see its README) before rendering.
- **Language default unless changed at kickoff:** KiKi's trader lines in Devanagari Hindi (`hi`) with English market terms; Ravi's typed replies in romanised Hinglish (`hi-Latn`), the way traders type; the streamer entirely in `hi-Latn`. Every non-English block carries the "Machine draft" chip the storyboard specifies.
- **Do beat wording:** KiKi's window says "Snapshot", matching what lab-lite would actually do. Keep it.
- KiKi's look: the real screens in `Google AI Builder/KIKI-FULL-SCREEN-HIGHLIGHTED-SCREENSHOTS/.../CONTACT-SHEET.jpg` and the app's styles (white sketchbook pages, ink text, Google colours used sparingly, dark scope panels, the floating Now/Next guidance window).
- Tools on Arpan's machine: the `hyperframes` skill (the composition framework used for the October video), FFmpeg, and `brag-output/` as a working reference for the October build scripts.

## Deliverables

1. `trader.mp4` (45–60 s), with Learn, Reflect, Do and Evidence beats in this order:
   - **Learn:** a Hindi placard with English market terms as chips, and the payoff visual moving with the narration.
   - **Reflect:** "Why was this a bad call?" in 4–6 turns, with a small decision-graph map lighting up and the chart or payoff changing.
   - **Do:** KiKi's floating guidance with a few marks over a **generic, unbranded** trading terminal.
   - **Evidence:** a four-colour scorecard and one line of cohort view.
2. `streamer.mp4` (45–60 s), the same beats: Hinglish, a retention or viewers chart, marks over a generic stream-analytics dashboard, and "Why did engagement fall at minute 40?"
3. An end card or short montage: "Same KiKi. Different sector." It can open or close the breadth part of the pitch.
4. Captions (burned in, or an SRT alongside). "Prototype · illustrative" visible on every frame. The trader disclaimer: "Education on a past, illustrative trade. Not investment advice."
5. A short `README.md` in the videos folder: sources, what is illustrative, which languages are machine drafts, and the music licence status (use none, or a clearly licensed track; the October music licence was never confirmed).

## Guardrails

- No real product UIs, logos or brand marks: no broker, no charting platform, no Twitch, no game publisher. GTA 6 by name only; no game artwork or footage.
- Don't present the videos as working features. On stage: "Here is how the same system looks in trading and streaming."

## Acceptance

- Each video is readable at 1080p, under 60 s, plays in the deck, and is labelled as a prototype.
- The team has watched each one start to finish.

## Starter prompt

```text
You are session S6 (Breadth videos) of the KiKi buildathon (student-deep scope, v0.2).
Read in order: Google AI Builder/CLAUDE.md;
Design-Thinking/docs/knowledge-workers/sessions/README.md;
Design-Thinking/docs/knowledge-workers/sessions/S6-breadth-videos.md;
Design-Thinking/docs/knowledge-workers/personas/trader/storyboard.md and streamer/storyboard.md.
Use the hyperframes skill. Build the trader video first. Output to
C:\Users\Arpan Vihan\Downloads\Google AI Builder\breadth-videos\. No real brand UIs or logos.
Show me a first rough cut before polishing. Report to the hub as sessions/README.md describes.
```
