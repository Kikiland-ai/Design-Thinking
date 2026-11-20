# BB8 mission plan: KiKi for knowledge workers (Google Startup Buildathon, 24-hour build)

Status: **Active**, v0.2 (scope agreed with Arpan 20 Nov, 03:15 IST)
Last updated: 2026-11-20 03:45 IST
Current phase: before the clock starts. The build runs **09:00 Fri 20 Nov → 09:00 Sat 21 Nov IST**.
Hub session: `google-ai-builder-de` (Claude Code, Arpan's machine, workspace `Google AI Builder/`)

## TL;DR

- **Objective:** go deep on the student route for real (narration-synced canvas, tutor mode on a decision graph, optionally a builder slice and an organisation view). Show breadth with trader and streamer **prototype videos** in the same KiKi formats and look. Pitch it as "deep where it counts, broad by design".
- **Present state:** plan v0.2, contracts and briefs ready. Drafting agents are writing the student tutor graph and the breadth storyboards into `personas/` before 09:00. No app code yet.
- **Primary uncertainty:** owners and capacity (not yet confirmed); the official rubric and final format; Odia review capacity at kickoff.
- **Immediate next action:** at 09:00 kickoff, confirm owners, review the student graph (physics and Odia, 30 min), freeze contracts §2, §4 and §6, and start S1, S2 and S3 at 10:00.

## Objective and success

### Objective

Prove that one KiKi system coaches knowledge workers deeply and in their language. Do it with a real, deep student build, plus sector prototypes that show the same formats re-targeted to trading and streaming, backed by a credible B2B story.

### Success criteria (at 09:00 Saturday)

1. Deployed: from C-AM-08, a juror can hear the narration with the canvas following, take the tutor conversation to a scorecard on real Gemini, and see the "next: lab" step, without the team's help.
2. Measured: tutor routing correct/20, turn p50/p90, cost per session.
3. Two breadth videos (45–60 s), labelled as prototypes, play in the deck.
4. A rehearsed pitch, twice and within time, that answers "are the other sectors real?" and "who pays?".

## Context

- **Event:** Google Startup Buildathon (Arpan's correction). The idea phase is passed. Jurors are likely technical and non-technical; get the official rubric (S7, by 13:00).
- **Scope decision (Arpan, 20 Nov):** "go deep in the student route, and just make visual enough or demo-able prototypes for trader or streamer personas, not real lab mode or tutor mode, could be just videos as well." The trader and streamer exist "to prove that the systems in place are breadth-wise scalable while being deep and personalised enough for each sector."
- **Code state (read-only maps, 20 Nov):** deployed on Firebase Hosting and Cloud Run (`kiki-api`, `kiki-lab`); ECE contracts hard-coded; no conversational code; the hosted lab trial budget is used up (so the lab demo is a recording); the lab-polling optimisation is in a separate lane. Details: [02 §1–3](02-build-plan-24h.md).

## Scope

### In scope

The tiers in [02 §2](02-build-plan-24h.md#2-scope-tiers): canvas sync, tutor mode (engine and UI) and deploy at Tier 0; the builder slice, organisation view and breadth videos at Tier 1.

### Non-goals

- Any Lab mode change: capture, polling, tracker, extension, annotation. The polling lane owns it.
- Real trader or streamer functionality.
- Generalising the ECE contracts (additive optional props only).
- Commits, pushes, deploys or publishing without the owner's go.

## Strategic context and intent threads

| Intent thread | Workstream | Why now | Decision or possibility served | Status | Stated or inferred |
|---|---|---|---|---|---|
| Student route deep and real | S1, S2, S3 (S4) | Arpan's scope call | The live demo | Active, critical | User-stated |
| Breadth as prototypes | S5, S6 | Prove the system scales across sectors | "Broad by design" slide and videos | Active | User-stated |
| B2B positioning and GTM | S7 | The jury scores the business | Beachhead (D5), pricing | Strategic bet | User-stated |
| Canvas in sync with narration | S1 | Pending actionable | Demo opening; shared scene prop | Active | User-stated |
| Lab-mode Gemini call reduction | Separate lane | Too many calls from polling | Cost and stability | Active, **not ours** | User-stated: don't disturb |

## Decisions already made

| Decision | Rationale | Date | Revisit when |
|---|---|---|---|
| Build window 09:00 Fri → 09:00 Sat IST | Arpan | 2026-11-20 | — |
| Student route deep and real; trader and streamer as visual prototypes or videos | Arpan | 2026-11-20 | — |
| Tutor mode lives inside the ECE app; ECE contracts get only additive optional props | Fastest real path; keeps the deployed demo safe | 2026-11-20 | After the buildathon |
| No Lab mode changes; the lab demo is a recording | Polling lane; hosted trial budget used up | 2026-11-20 | If the polling owner offers a live run |
| Tutor server is stateless; the graph decides and the model only labels | Cloud Run instances don't share memory; auditability | 2026-11-20 | — |

## Assumptions and unresolved questions

| Item | Type | Confidence | Impact if wrong | How to resolve |
|---|---|---:|---|---|
| Owners: Arpan S1, S5, S6; Akshita S2, S7; Aditth S3, S4; Aditya polling lane, then backup | Assumption | Medium | Schedule | Kickoff |
| About 17 productive hours per person | Assumption | Medium | Slack | Kickoff |
| Non-code drafting before 09:00 is fine under the rules | Assumption | Medium | Whether the drafts may be used | Official rules |
| Final format: live demo plus pitch, about 6 min | Assumption | Low | Demo length | S7 by 13:00 |
| C-AM-08 is the concept to sync | Assumption | Medium | Which cues get timed | Arpan at kickoff |
| Odia speakers can review the tutor lines at kickoff | Assumption | Medium | Odia quality on stage | Kickoff |
| A paid Gemini key with enough quota exists | Assumption | Medium | Routing and builder | S3 at 10:00 |

## Portfolio and priorities

| Initiative | ROI | TTV | Class | Status |
|---|---|---|---|---|
| Tutor mode for the student (engine and UI) | High | Slow | **Strategic bet** | Graph drafting |
| Canvas–audio sync and shared scene prop | High | Fast | Quick win | Ready |
| Breadth videos | High (for the story) | Medium | Bet, Tier 1 | Storyboards drafting |
| Builder slice (lecture → draft module) | Medium–high | Medium | Bet, Tier 1 | Ready |
| Organisation view | Medium | Fast | Quick win, Tier 1 | Ready |
| Spoken tutor lines; live replay of the sector flows | Medium | Medium | Tier 2 | Later |
| Any Lab mode change; generalising the ECE contracts | Low (in 24 h) | Slow | **Money pit** | Avoid |

## Session board

Every worker session follows [sessions/README.md](sessions/README.md) and reports into `reports/`.

| Session | Workstream | Proposed owner | Branch | Starts | Gates it reports at | Brief |
|---|---|---|---|---|---|---|
| **S0 hub** | Decisions, contracts, integration, measurements | Arpan + this session | — | Now | — | this file |
| S1 | Canvas sync, layout, shared scene prop | Arpan | `feat/canvas-sync` | 10:00 | 13:00 (prop), 15:00, 19:00 | [S1](sessions/S1-canvas.md) |
| S2 | Tutor UI in the student app; organisation view | Akshita | `feat/tutor-ui` | 10:00 | 13:00, 19:00, 22:00, 01:00 | [S2](sessions/S2-tutor-ui.md) |
| S3 | Tutor engine and Gemini routing | Aditth | `feat/tutor-api` | 10:00 | 13:00 (stub), 16:00, 19:00, 20:00 (numbers) | [S3](sessions/S3-tutor-engine.md) |
| S4 | Builder slice (T1) | Aditth (second session); Aditya backup | `feat/builder` | 13:00 | 17:00, 22:00 | [S4](sessions/S4-builder.md) |
| S5 | Content: student graph review; breadth content | Arpan | docs only | Drafts before 09:00 | 09:45, 15:00 | [S5](sessions/S5-content.md) |
| S6 | Breadth videos (T1) | Arpan; Aditya backup | outside repos | 15:00 | 21:00, 01:00 | [S6](sessions/S6-breadth-videos.md) |
| S7 | Story, GTM, deck, lab clip | Akshita | docs only | 09:00 | 13:00, 19:00, 01:00, 04:00 | [S7](sessions/S7-story-gtm.md) |
| — | Lab-polling optimisation | Current owner | existing | ongoing | own cadence | **do not disturb** |

## Blockers and unblockers

| Blocker | Why it blocks progress | Proposed unblocker | Input needed |
|---|---|---|---|
| Owners not confirmed | Sessions can't start cleanly at 10:00 | Confirm at the 09:00 kickoff | Team |
| Odia lines unreviewed | Odia on stage | 30-minute review at kickoff; the "Machine draft" chip until then | Odia speakers |
| Official rubric unknown | What to emphasise | S7 by 13:00 | Team lead |
| Hosted lab budget used up | No live MATLAB | Recorded clip. A reset is a production change and costs money | Owner's explicit approval, if ever |

## Now / Next / Later

### Now (03:45–09:00, no app code)

1. ~~Student tutor graph drafted~~ **Done (03:55):** `personas/ece-phase-error/`: 11 nodes, 3 misconceptions from the course, 5 learner turns per path, 20-reply routing set, all checks pass. The hub reviewed it, accepted P1–P3, added `nextSteps`, and recorded decisions in its README. **Needs at kickoff:** Odia review (30 min), ECE teacher check (15 min), Odia `why` lines for `nextSteps`.
2. ~~Breadth storyboards~~ **Done (04:10):** `personas/trader/` and `personas/streamer/`, each with a persona card, illustrative playbook excerpt, scenario, an 8-node graph-shaped tutor flow with a scripted path, and a 58 s storyboard. The hub checked them:
   - The trader's prices were re-derived independently with Black–Scholes: entry ₹90.23 vs the tick-rounded ₹90.25; exit ₹59.55 exact; −₹9,210 (−34%); straddle about 304 points.
   - The +₹40 / −₹48 / −₹23 split is a Shapley average over all six orderings, so it doesn't depend on order.
   - Guardrails are present: "Prototype · illustrative" on every frame, the not-investment-advice line, machine-draft chips, no product UIs or logos, GTA 6 as text only.
   - The generator scripts were moved from the scratchpad to `personas/tools/`, so numbers can be regenerated.
3. Arpan skims [02](02-build-plan-24h.md), `personas/ece-phase-error/README.md` and the two storyboards before kickoff.

### Kickoff checklist

09:00 to 10:00, before any session starts.

| # | Item | Who | Time |
|---|---|---|---|
| 1 | Confirm owners and rest blocks; confirm C-AM-08 as the synced concept | All | 5 min |
| 2 | Odia review of the student graph's lines, plus Odia `why` lines for its 3 `nextSteps` | Odia speakers | 30 min (in parallel) |
| 3 | ECE physics check of the student graph (README checklist) | ECE teammate | 15 min (in parallel) |
| 4 | Freeze contracts §2, §4 and §6 (v0.2 additions: named `ece` states, chip `route`, `nextSteps`, `hi-Latn`, forced-advance and scene-lock rules) | All owners | 5 min |
| 5 | Agree the cut lines ([02 §7](02-build-plan-24h.md#7-cut-lines)) and run a 10-minute pre-mortem | All | 15 min |
| 6 | Breadth content: skim both storyboards. Note any Hindi or Hinglish fix and plausibility doubts for a reviewer: IV 17.5% → 11% around the event; flat smile; invented OI; what "time to the right trade" means; the spread counterfactual's framing; prop desk vs broker; the stream's drop size, the 4-minute chat lead, "segment retention" | Arpan, plus a trader and a streamer if reachable | 10 min, then by 15:00 |
| 7 | Start S1, S2, S3 and S7 at 10:00 with their starter prompts | Owners | — |

### Next (09:00–01:00)

4. 09:00 kickoff: owners, graph review, contracts frozen, cut lines agreed, 10-minute pre-mortem.
5. 10:00: S1, S2, S3 and S7 start; S4 at 13:00; S6 at 15:00.
6. Gates: 13:00 skeleton · 19:00 tutor real end to end · 01:00 all deployed and dry run 1. The hub triages reports at each gate.

### Later (01:00–09:00)

7. Fix list; backup recordings; **feature freeze at 04:00**; two rehearsals; submission by 09:00.
8. After the buildathon: migrate ECE onto packs; native review; buyer conversations; make the sector flows live.

## Risks and controls

| Risk | Likelihood | Impact | Early signal | Mitigation or exit criterion |
|---|---:|---:|---|---|
| Tutor routing feels slow or dumb | Medium | High | Below 15/20; p90 above 4 s at 19:00 | Chips first (cut line); flash-lite; tighter node options |
| Odia lines read badly on stage | Medium | High | Reviewers flag many lines | Review at kickoff; English-first notch for the demo |
| Integration surprises late | Medium | High | Skeleton not running at 13:00 | Cut lines at 13:00 |
| Breadth videos read as fake features | Medium | Medium | Juror simulation | "Prototype · illustrative" label; say so on stage; show the shared formats |
| Collision with the polling lane | Low | Medium | Lab files touched | No Lab mode changes at all |
| Scope creep at 3 a.m. | High | High | New ideas after 01:00 | Freeze at 04:00; the hub says no |

## Completion criteria for this phase (before 09:00)

- The student graph and routing set pass the self-checks and are ready for the kickoff review.
- The breadth storyboards are ready for S6.
- Plan, contracts and briefs are at v0.2.

## Cold-pickup handoff

- **Last completed action (03:55):** reviewed the student tutor graph. Accepted its contract proposals (named `ece` states, chip `route`, `phi` not `phaseDeg`, forced-advance rule, `nextSteps`) and propagated them into 02, 05 and the S1–S3 briefs. Renamed the re-scoped briefs to S2-tutor-ui, S4-builder, S5-content and S6-breadth-videos.
- **Current working state:** all docs are new and uncommitted in `Design-Thinking/docs/knowledge-workers/`. The student graph and both breadth storyboards are drafted, checked by the hub and ready for the kickoff review. The generator scripts are in `personas/tools/`.
- **Exact next action:** run the [kickoff checklist](#kickoff-checklist) at 09:00. Then triage the first reports at the 13:00 gate.
- **Open these files first:** this file, [02 build plan](02-build-plan-24h.md), `personas/ece-phase-error/README.md`.
- **Do not repeat:** the code mapping ([02 §1](02-build-plan-24h.md#1-what-changed-from-v01) and v0.1 history); reading the October docs ([01 §2](01-kiki-for-knowledge-workers.md#2-why-kiki-existed-and-what-carries-over)).
- **Context that must not be lost:** don't disturb the polling lane; no Lab mode changes; honesty labels; commit as `arpanvihan5-sketch` with no AI attribution, only when asked.
- **Next intent checkpoint:** 09:00 kickoff.

## Change log

| Date | What changed | Why it changed |
|---|---|---|
| 2026-11-20 | v0.1 created | Scope widening and 24-hour plan requested |
| 2026-11-20 | Event renamed to Google Startup Buildathon | Arpan's correction |
| 2026-11-20 03:45 | v0.2: student-deep scope; trader and streamer as prototype videos; clock 09:00–09:00; lab-lite and generic workspace path dropped; S2, S4 and S6 re-scoped | Arpan's answers |
| 2026-11-20 03:55 | Student graph landed and reviewed; contract additions (named `ece` states, chip `route`, `nextSteps`, forced-advance and scene-lock rules; `phi`); briefs renamed | Drafting agent's proposals; clarity for teammates at 09:00 |
| 2026-11-20 04:10 | Breadth storyboards landed and checked (independent Black–Scholes, guardrails). `hi-Latn` accepted; prototype extension fields documented; payoff Tier 2 params noted; scripts moved to `personas/tools/`; kickoff checklist added | Storyboard agent's report and open questions |
