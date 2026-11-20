# Judge story: deep where it counts, broad by design

v0.2 · 20 Nov 2026 · Status: **Proposed** · Audience: Google Startup Buildathon jurors, technical and non-technical · Owner: S7 (story and GTM)

**Scope behind this story (Arpan, 20 Nov):** the student route is the real, deep build. The trader and streamer are visual prototypes. Their job is to show the system scales across sectors while staying deep and personalised for each.

## 1. The answer first

> **KiKi turns an organisation's know-how into multilingual, hands-on coaching. We built it deep for one learner, an Odia-medium engineering student, from lesson to lab, and designed every part so that taking it to a new sector is a content job, not a rebuild. The trader and the streamer show what that looks like.**

Short lines to reuse:

- "Deep where it counts. Broad by design."
- "Laws, odds and audiences. If KiKi can coach all three, it can coach your team."
- "Your people think in many languages. Your onboarding speaks one."

## 2. The argument (pyramid)

**Situation.** Every organisation brings people into roles where the knowledge lives in English documents and in senior colleagues' heads, and the work happens inside specific tools.

**Complication.** People lose months, and in trading real money, to two things that are not ability: the working language, and the know-how nobody wrote down. Experience alone doesn't fix it. SEBI's FY26 study of individual F&O traders (as reported by Business Today, 14 Nov 2026) found 87.7% lost money, and the share of loss-makers rose with experience. *Verify against the primary report before quoting.*

**Question.** How do you make expert know-how learnable by everyone, in their language, inside real work, with evidence a manager can trust?

**Answer: KiKi.**

| Point | Proof on stage |
|---|---|
| 1. **Learn:** short lessons in the learner's language, with visuals that move with the narration | Live: the C-AM-08 placard. As KiKi says the carrier slips to 60°, the scope moves there and the signal halves. Odia ↔ English on the dial |
| 2. **Reflect:** KiKi talks a problem through on a decision graph until the reasoning is clear | Live: Bikash missed a phase question. "Talk it through with KiKi." The graph map lights up, the scene follows the conversation, and the scorecard comes from his own words |
| 3. **Do:** coaching inside the real tool, with the learner always acting | Recorded: the MATLAB lab with live checks (4.7 s median from frame to guidance, 17 Oct trial) |
| 4. **Create:** an organisation's own material becomes a draft module | Live, if Tier 1 lands: a professor's lecture PDF → outline → a compiled concept in Odia and English, labelled draft |
| 5. **It travels to other sectors** | Two short prototypes, trader and streamer, in the same KiKi: their visuals, their words, their language. The trader's flow is written in the same graph format the student's tutor runs on today |

## 3. Why depth in one domain and breadth by design is the right proof

This is the core of the pitch. Jurors have heard "an AI tutor for everything" many times.

1. **Breadth claims are cheap; depth is expensive and convincing.** One learner, end to end and real (language, lesson, reasoning, lab, evidence), shows KiKi works rather than demos.
2. **Generality lives in the formats, not the slides.** The tutor runs on a decision graph; lessons run on placards, terms and cues; evidence runs on four dimensions. None of these formats knows it is about electronics. The trader's and the streamer's flows are written in the same formats. Show the two graph files side by side.
3. **The sectors were chosen where a generic tutor breaks:**
   - **Laws (engineering):** it breaks on correctness.
   - **Odds (trading):** it breaks on judgement, because a good decision can lose money.
   - **Audiences (streaming):** it breaks on taste, because there is no answer key, only live metrics.
4. **Personalised per sector, not skinned.** Each sector gets its own visuals (scope, payoff chart, retention curve), its own canonical words (carrier and sideband; theta and IV; CCV and retention), its own metrics, and its own language.
5. **A platform designed for many sectors, sold into one first.** Name the beachhead (D5 in [01](01-kiki-for-knowledge-workers.md)).

| Corner | Where it applies |
|---|---|
| Laws | Engineering, manufacturing, field service, clinical procedures, compliance |
| Odds | Finance, insurance, sales forecasting, operations, risk |
| Audiences | Media, marketing, sales, customer success, design |

## 4. Demo narrative (about 6 minutes; adjust to the slot)

| Time | Act | What the jurors see | Live or recorded |
|---|---|---|---|
| 0:00–0:30 | Hook | Three people, one problem: the work happens in a language and with know-how they weren't given. Then: "We went deep on one." | Slide |
| 0:30–1:30 | **Learn** | C-AM-08 narration with the canvas following; the dial flips Odia ↔ English | Live |
| 1:30–3:15 | **Reflect** | The missed phase question → "Talk it through with KiKi" → 4–6 turns. The graph map lights up and the scene moves to 60°, then 90°. Scorecard: concept ok, calculation ok, expression partial. "Next: try the phase fault in the lab" | Live (recorded backup) |
| 3:15–3:45 | **Do** | 20 s of the real MATLAB lab with live checks and the Now/Next window | Recorded |
| 3:45–4:15 | **Create** (if Tier 1 lands) | The professor's PDF → outline → compiled concept, labelled draft. Otherwise one slide | Live or slide |
| 4:15–5:15 | **Broad by design** | Trader video, then streamer video (about 25 s each from the 45–60 s cuts), then the end card "Same KiKi. Different sector." | Recorded, labelled prototype |
| 5:15–5:35 | **Evidence** | Organisation view: a cohort's gaps by type (if Tier 1 lands) | Live or slide |
| 5:35–6:00 | Close | Beachhead, pricing, the line | Slide |

Every live AI step has a recorded backup. The demo never waits more than about 4 seconds without visible progress.

## 5. Pitch deck skeleton (startup format)

1. **KiKi**, with the one-line answer.
2. **Problem:** three people, one problem; the verified SEBI number.
3. **Insight:** performance lost to language and unwritten know-how, not ability.
4. **Product:** Learn, Do, Reflect, Create, Evidence.
5. **Live demo:** the student, deep.
6. **Broad by design:** the formats; laws, odds, audiences; the two prototype videos.
7. **How it works:** Gemini (structured routing, screen understanding, multilingual speech), Cloud Run, Firebase; decision graphs; deterministic scenes.
8. **Business model:** who buys (onboarding and L&D owners; colleges), when (onboarding and transitions), pricing (per seat plus per-pack setup), measured cost per session.
9. **Go-to-market:** beachhead, first customers' profile, expansion path.
10. **Positioning:** learning platforms, AI tutors, digital adoption platforms; KiKi's intersection. Categories only, unless a named comparison has been checked.
11. **Proof so far:** deployed, measured numbers, the pilot plan.
12. **Team and ask.**

## 6. Evidence to collect during the build

| Claim | Number we need | Status |
|---|---|---|
| The tutor routes correctly | Correct branch on N of 20 labelled student replies | Measure by 20:00 |
| It responds fast enough | Turn p50/p90 | Measure by 20:00 |
| It is affordable | Cost per tutor session | Measure by 01:00 |
| The lab works in a real tool | 4.7 s median, 10.1 s p90, checkpoint 1 → 6 (17 Oct) | Have |
| New sectors are content work | Hours to author each sector flow in the same graph format | Log during the build |
| Multilingual, honestly | Odia and English in the build; Hindi and Hinglish in the prototypes as machine drafts | Count at 04:00 |
| Learning impact | Not yet measured. Show the scorecard and the pilot plan | Say so plainly |

## 7. Questions jurors will ask

| Question | Answer in one breath |
|---|---|
| Why only one deep domain? | Depth is what proves it works. The other two show the formats travel; making them live is authoring packs and graphs, not new engineering |
| Are the trader and streamer real? | They are prototypes in the same formats and look. The student route is the working build, and we say that on the slide |
| Isn't this ChatGPT with a prompt? | Open the graph. The model only labels the student's reply against allowed options; the graph decides the next step, and every line KiKi asks is reviewed content |
| How do you stop hallucination? | Lessons come from course or organisation sources with source tags and review states; visuals are deterministic; tutor routing is constrained to enums |
| Trading advice is regulated | Process, not picks: KiKi reviews past or paper trades and never recommends a live one |
| Who pays? | Onboarding and L&D owners in organisations hiring across language backgrounds, starting with the beachhead. Creator agencies would pay for the streamer use case; it is not our first market |
| How do you know students learn? | Each session ends with evidence split four ways. A proper pilot measures the concept-versus-expression gap shrinking; we haven't run it yet |
| Unit economics? | Content is generated once. Measured cost: X per tutor session. Priced per seat |
| Screen sharing at work is sensitive | Capture is opt-in per tab, KiKi masks its own windows, and organisations see dimension-level evidence, never screens |
| Why Gemini and Google Cloud? | Structured outputs for routing, screen understanding, multilingual speech, and Cloud Run with Firebase already serving the app |
| What did you build in these 24 hours? | Be exact. Before: the ECE app, lab checks, Odia narration. During: canvas sync, tutor mode, the builder slice, the organisation view, and the two sector prototypes |

## 8. Honesty boundaries (non-negotiable on stage)

- Breadth videos carry "Prototype · illustrative" on screen and are introduced as prototypes.
- Say "illustrative" for scenarios and cohort data, and "machine draft" for unreviewed languages, including any Odia not yet reviewed.
- Call the ECE cue timing manual.
- Don't call personas users or testimonials.
- Say Cloud Run only for request paths that actually use it (the ECE app does as of 19 Nov; recheck the tutor route after deploy).
- Don't quote the SEBI figure without the primary source.
