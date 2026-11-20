# ECE tutor graph: phase error in a coherent receiver

Draft v0 · 20 Nov 2026 · [Tutor graph](graph.json) (`kiki-tutor-graph/v0`) · [Routing examples](routing-set.json)

> **Machine draft.** All Odia (`or`) text is a machine draft. A native Odia speaker must review it before it is shown as reviewed. An ECE teacher has not checked the content yet. `caseData.review` carries this state.

The tutoring exercise builds on concept `C-AM-08` and lab checkpoint `CP-DSB-11` in the [Analog Modulation learning case](../../../data-model/ANALOG-MODULATION.md).

## The problem

KiKi's framing: "In your coherent receiver, the local carrier has the right frequency but is 60° out of phase with the transmitter's carrier. What fraction of the message amplitude do you recover, what happens at 90°, and why?" Target reasoning: the receiver output is m(t) cos φ, so 0.5 at 60° and 0 at 90° (ideal).

What the course content changed in the brief's framing:

- **Fraction of the aligned amplitude, after recovery gain 2.** The course states recovery as "ideal gain-corrected … m(t)*cos(phi)" with matched frequency and unit carriers (ledger C-AM-06 and C-AM-08, worked question W-AM-08). The filter alone gives ½ m(t) cos φ, and KiKi says so, so "a quarter" never comes up.
- **90° is "the ideal message vanishes", not "nothing at all".** The course's own C-AM-08 misconception (M-AM-08, check Q-AM-08-4) is that a finite filter can leave ripple. `show-90` says so.
- **Angles are in radians in the lab.** The transmitter carrier Phase is pi/2, and the fault sets the Local carrier Phase to pi (a 90° relative error; fault F-AM-PHASE, checkpoint CP-DSB-11). C-AM-01 asks which shift is a quarter cycle (pi/2). This grounds the angle-units misconception.
- **Misconceptions.** `phase-does-not-matter` (C-AM-06 misconception M-AM-06; distractor "1" in Q-AM-08-1), `any-error-loses-all` (M-AM-06's correction: mismatch "reduces or changes" the message) and `angle-unit-mixup` (C-AM-01). A linear guess routes to `unclear`, and the calc-60 nudge covers it.
- **Term forms:** coherent demodulation, local oscillator (the lab block is "Local carrier"), lowpass filter, recovery gain, phase error.

## Path

```text
predict-60  probe  "All, part or none at 60°?"                        [aligned]
  ├ part-survives ───────────────────────────────────────────────────┐
  ├ phase-does-not-matter ─→ show-phase-matters   [phi-60-trace] ─────┤
  └ any-error-loses-all ───→ show-part-survives   [phi-60-trace] ─────┤
why-cos     probe  "How does φ change m(t) at the output?"       ◄────┘
  ├ scaled-by-cos ───────────────────────────────────────────────────┐
  ├ half-factor-only (partial) ┬→ show-cos-factor [phi-60-trace] ─────┤
  └ phase-does-not-matter ─────┘                                      │
calc-60     probe  "What fraction of the aligned amplitude at 60°?" ◄┘
  ├ half ────────────────────────────────────────────────────────────┐
  └ angle-unit-mixup ──────→ show-angle-units     [phi-60] ───────────┤
predict-90  probe  "What comes out at 90°, and why?"             ◄────┘
  └ vanishes | angle-unit-mixup | phase-does-not-matter → show-90 [phi-90]
explain-english probe "Explain it in English, in one or two sentences"
  └ clear-explanation | partial-explanation → conclusion [recap]
```

Every probe also has `unclear` (the next hint rung: question, nudge, worked step, answer) and `off_topic` (restate). The graph is acyclic: 12 paths, each exactly 5 learner turns, because show nodes auto-advance. That fits the demo's 4–6 turns.

## Nodes, metrics and dimensions

| Node | Branches → metric (dimension) | Canvas |
|---|---|---|
| predict-60 | part-survives `ok`; phase-does-not-matter, any-error-loses-all `not_yet` → conceptual-understanding (concept) | aligned |
| why-cos | scaled-by-cos `ok`; half-factor-only `partial`; phase-does-not-matter `not_yet` → conceptual-understanding (concept) | phi-60-trace |
| calc-60 | half `ok`; angle-unit-mixup `not_yet` → calculation-accuracy (concept) | phi-60-trace |
| predict-90 | vanishes `ok`, angle-unit-mixup `not_yet` → calculation-accuracy (concept); phase-does-not-matter `not_yet` → conceptual-understanding | phi-60 |
| explain-english | clear-explanation `ok`; partial-explanation `partial` → articulation (english) | recap |
| any free-text turn | `expression.termsUsed` → terms (words); `expression.clarity` on English or mixed replies → articulation (english) | none |

The proposed tutor runtime matches `termsUsed` against `caseData.targetTerms` on free-text replies. Chip replies earn no vocabulary or English-expression evidence.

## Canvas: real names used

**Scene.** `scenes[0]` is `{ id: "phase-recovery", template: "ece", params: { renderer: "coherent-phase-recovery/v1", conceptId: "C-AM-08" } }`. It resolves to artifact `SCENE-AM-08-phase-recovery` in the C-AM-08 manifest.

**Props (kiki-web).**

- In the source snapshot used for this draft, `PhaseRecoveryScene({ scene })` takes only `scene`. The angle is local state `phi`, seeded from `scene.controls[0].default` in `apps/web/src/features/learning/PhaseRecoveryScene.tsx:12-14`. The proposed control prop takes `{ phi }`, highlight targets, hidden elements and a lock flag.
- The artifact's control is **`phi`**: unit `degree`, 0–180, step 15, default 60. The output is `fraction` ("Signed recovery fraction"), and `comparisonDegrees` is [0, 60, 90]. Sources: `apps/web/src/fixtures/concept-media-C-AM-08.json:328-344`; schema `apps/web/src/contracts/concept-media.ts:35-46`; maths `recoveryFraction(phiDegrees)` = cos(φ·π/180) in `features/learning/phase-math.ts:4`.
- The scene takes `phi` in degrees. The separate CamCanvas contract uses `phase` (`data-model/media/cam-contract/policies.json`).

**Targets** for `highlight`, `hide` and `annotate.target`. Walkthrough targets are kept verbatim (with spaces) from `kiki-web/data-model/media/cam-contract/scenes.json` → `C-AM-08.scene.walkthrough`.

| Target | Source | Element in `PhaseRecoveryScene.tsx` |
|---|---|---|
| `aligned-trace`, `recovered-trace` | data-testid | the two trace paths, :29–30 |
| `recovery-fraction` | data-testid | the cos φ readout, :36 |
| `relative phase error` | walkthrough (concept, marker) | the φ control label, :39 |
| `frequency mismatch` | walkthrough (concept, marker) | the caption "frequency matched", :26 |
| `Carrier mismatch` | walkthrough (words, sweep) | the whole scene |
| `comparison-presets` | **proposed id, does not exist yet** | the preset button group, :41 |

**States** use `values: { phi }`. `aligned` sets φ to 0 and hides the presets. `phi-60-trace` sets φ to 60 and hides the readout and presets. `phi-60` sets φ to 60 and shows the readout. `phi-90` sets φ to 90. `recap` sets φ to 60 with the `Carrier mismatch` sweep. The `hide` list keeps the answers out of the preset buttons, readout and accessible text during relevant probes. Each node's canvas replaces the previous one, annotations included. A node without a canvas keeps the current scene.

## Draft integration notes

- The draft uses named `states` on the `ece` scene. `TutorNode.canvas.state` names a state containing `phi`, highlights and hidden elements. Lock the scene controls during probes and unlock them after the conclusion. The preset button group needs a `comparison-presets` target.
- A chip with `route` goes directly to that label. The "Use a model sentence" chip routes to `partial-explanation` because the learner did not write the sentence.
- After the fourth hint, advance through the first `expect` branch and record `not_yet`. Each probe lists its `ok` branch first.
- Start at `predict-60` when a student enters after missing `Q-AM-08-1` or `Q-AM-08-2`. The entry line is “You missed a phase question. Let's talk it through.”
- The scorecard always suggests lab checkpoint `CP-DSB-11`. It suggests `C-AM-06` when conceptual understanding is `not_yet` and `C-AM-01` when the `angle-unit-mixup` label occurs. The `nextSteps` explanations still need Odia copy.

The API bundle location and live app integration need verification. The prior interface proposal is available in Git history. [Tutor mode contract](https://github.com/Kikiland-ai/Design-Thinking/blob/45180af3f589bfdb11711766a4f8fbbc339a8ce9/docs/knowledge-workers/05-contracts-v0.md#4-tutor-mode)

## Routing set

20 replies over 5 probes (5/4/4/4/3). Every expect id appears at least once. Each misconception appears twice, `unclear` three times and `off_topic` twice. By language: en 9; or 6 (4 in Odia script, 2 romanised); mixed 5 (romanised, code-mixed). Here `or` means Odia with English technical terms, as the app writes it; `mixed` means switching beyond the terms. Three replies test router discipline: a time-shift idea at why-cos (`unclear`), a linear guess at calc-60 (`unclear`), and a ripple caveat at predict-90 (still `vanishes`).

Run the structural check from the repository root. It checks graph reachability, branch references, hint and chip structure, and routing examples.

```sh
python -I docs/prototypes/ece-phase-error/validate_ece_graph.py docs/prototypes/ece-phase-error
```

## Review checklists

**Odia speaker (30 min)**

- [ ] Polite ଆପଣ register throughout, and the tone suits a first-year student.
- [ ] Technical terms stay in Latin script with the lesson's casing (Phase error, Local carrier, Lowpass filter, Recovery gain).
- [ ] Each line sounds natural read aloud (TTS comes later).
- [ ] Check these words: ତଫାତ, ଘୁଞ୍ଚିଛି, ଆଂଶିକ, କମ Frequency ଅଂଶ, ବାସ୍ତବ, ଓଲଟା, ନମୁନା ବାକ୍ୟ, and the four metric labels.
- [ ] The romanised and code-mixed routing replies sound like real students.
- [ ] Nothing reads as "wrong"; misconception lines stay neutral.

**ECE teacher (15 min)**

- [ ] Framing: matched frequency, unit carriers, ideal lowpass filter, recovery gain 2, answer as a fraction of the aligned amplitude.
- [ ] The maths in the why-cos hints and show-cos-factor (product identity, ½ m(t) cos φ, gain 2).
- [ ] The 90° wording: the ideal message vanishes, and a real filter can leave a little ripple.
- [ ] The three misconceptions are realistic. Is it fine to leave linear falloff to the hint ladder?
- [ ] No hint rung gives the answer too early.
- [ ] The `ok` bar for explain-english: reason plus result, with at least two course terms.
