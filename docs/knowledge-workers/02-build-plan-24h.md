# 24-hour build plan

v0.2 · 20 Nov 2026, 03:30 IST · Status: **Scope agreed by Arpan; owners to confirm at kickoff** · Clock: **09:00 Fri 20 Nov → 09:00 Sat 21 Nov IST** · Interfaces: [05 contracts](05-contracts-v0.md) · Sessions: [MISSION](MISSION.md)

## 0. The plan on one page

**Scope (Arpan, 20 Nov):** go deep on the **student route**, for real. The **trader** and **streamer** are not build slices. They are visual, demo-able prototypes, videos where that is enough. Their job is to show that the system scales across sectors while staying deep and personalised for each.

**Goal at 09:00 Saturday.** A deployed student journey where Bikash:

1. **Learns** C-AM-08, with the canvas moving in step with KiKi's narration.
2. **Talks it through** with KiKi in tutor mode on a medium-difficulty phase-error problem. The decision graph lights up, the phase scene moves with the conversation, and a scorecard comes from his own words.
3. **Is pointed to the lab** (the recorded MATLAB clip with live checks).

Optionally, the professor's lecture notes become a draft module, and an organisation view shows a cohort's gaps by dimension. Two short videos then show the same KiKi coaching a trader and a streamer.

**Capacity versus load.** About 60 human hours (4 people × ~17, minus ~8 for the lab-polling lane). Tier 0 is about 29 hours likely (41 worst), and Tier 0 plus Tier 1 about 44 (64 worst). That leaves roughly 25% slack at the likely estimate. The slack is the point: it absorbs the surprises.

## 1. What changed from v0.1

| v0.1 (before the scope call) | v0.2 (now) |
|---|---|
| Trader was the tutor-mode hero | **The student is the tutor-mode build**, on the existing phase scene |
| A new domain-agnostic workspace path for new personas | **No new path.** Tutor mode lives inside the ECE app; ECE contracts get only additive, optional props |
| Content factory producing trader and streamer packs | A **thin builder slice for the student route** (lecture notes → draft module), Tier 1 |
| Lab-lite on the streamer's dashboard | **Dropped.** No Lab mode changes at all; the polling lane is untouched |
| Trading and streaming React scene templates | **Videos draw their own visuals.** React templates only if a live replay happens (Tier 2) |

## 2. Scope tiers

**Tier 0: the demo fails without it. Tier 1: weaker without it. Tier 2: only if Tier 0 and Tier 1 are green at 01:00.**

| # | Item | Tier | Session | Likely h | Worst h |
|---|---|---|---|---:|---:|
| 1 | Canvas–audio sync and side-by-side layout on C-AM-08; a scene control prop shared with tutor mode | T0 | S1 | 5 | 8 |
| 2 | Tutor engine: `/tutor/turn` with Gemini routing on the student graph | T0 | S3 | 6 | 9 |
| 3 | Tutor UI inside the ECE app: conversation, chips, graph map, phase-scene cues, scorecard feeding the rings; entry points from the concept page and a missed check question | T0 | S2 | 7 | 10 |
| 4 | Student tutor graph and routing set: final review of the draft (drafted before 09:00) | T0 | S5 | 1 | 2 |
| 5 | Deploy: Hosting plus a `kiki-api` revision with the tutor route; Gemini key in Secret Manager; smoke test; recorded fallbacks | T0 | S2 + S3 | 3 | 5 |
| 6 | Lab: choose and trim the recorded MATLAB clip for "Do" (the hosted trial budget is used up) | T0 | S7 | 0.5 | 1 |
| 7 | Pitch: deck, demo script, two rehearsals | T0 | S7 + all | 6 | 8 |
| | **Tier 0 subtotal** | | | **28.5** | **43** |
| 8 | Builder slice: Library lecture text → outline → one concept compiled (English source, Odia rendition, terms kept, an existing scene suggested) → preview, labelled draft | T1 | S4 | 6 | 9 |
| 9 | Organisation view for the student route: an illustrative cohort's gaps by dimension | T1 | S2 | 3 | 5 |
| 10 | Breadth videos: trader and streamer (45–60 s each) and a "Same KiKi. Different sector." end card, from the storyboards drafted before 09:00 | T1 | S6 | 6 | 9 |
| | **Tier 0 + Tier 1** | | | **43.5** | **66** |
| 11 | KiKi's tutor lines spoken (pre-generated Odia and English TTS) | T2 | S3/S4 | 2 | 3 |
| 12 | Live scripted replay of the trader and streamer flows through the real tutor UI (needs React candles, payoff and line scenes) | T2 | S1 + S2 | 6 | 9 |
| 13 | Builder run on the trader and streamer playbooks, shown in the videos | T2 | S4 | 2 | 3 |

**Out of scope:** any Lab mode change (the polling lane owns Lab mode); on-screen annotation; generalising the ECE contracts; real trader or streamer functionality; voice replies.

## 3. How the student slice fits together

```text
Concept page (C-AM-08)                     Concept check
  placards + Listen ──► canvas follows       missed phase question
  narration cues (S1)                              │
        │                                          │
        └──── "Talk it through with KiKi" ◄────────┘
                          │
                Tutor screen (S2)  ◄── POST /tutor/turn (S3, Gemini routing)
      phase scene moves with each node (S1's control prop)
      graph map lights up · chips or free text · Odia/English by the dial
                          │
         Scorecard → concept / words / expression evidence → rings
                          │
         "Next: try the phase fault in the lab" → recorded MATLAB clip
```

**The shared piece:** S1 adds one optional prop to the phase scene that takes an external state: the angle `{ phi: 60 }`, highlights, a `hide` list and a walkthrough mark, plus a `locked` flag. `hide` matters because the preset buttons print "cos = 0.50" and the readout prints the fraction, which would give the tutor's answers away. Narration cues and tutor nodes both drive the scene through this prop. **S1 delivers it by 13:00**, and S2 depends on it.

## 4. Workstreams and owners

| Session | Workstream | Proposed owner | Starts | Done by |
|---|---|---|---|---|
| S1 | Canvas sync, layout, shared scene prop | Arpan | 10:00 | Prop 13:00; sync 15:00 |
| S2 | Tutor UI in the ECE app, entry points, scorecard; organisation view | Akshita | 10:00 | Tutor 19:00; organisation view 22:00 |
| S3 | Tutor engine and Gemini routing; deploy share | Aditth | 10:00 | Stub 13:00; real 19:00; numbers 20:00 |
| S4 | Builder slice (T1) | Aditth (second session); Aditya backs up after the polling work | 13:00 | 22:00 |
| S5 | Content: student graph final; breadth content handed to S6 | Arpan | Drafts before 09:00 | Review 09:30 |
| S6 | Breadth videos (T1) | Arpan (made the October video with Hyperframes); Aditya as backup | 15:00 | Trader 21:00; streamer 24:00 |
| S7 | Story, GTM evidence, deck, rehearsals | Akshita (lead) | 09:00 | Deck 04:00; rehearsed by 07:00 |
| — | Lab-polling optimisation | Current owner | — | Own plan. **Do not disturb** |

## 5. Schedule (IST)

| Time | Block | What happens | Gate at the end |
|---|---|---|---|
| 03:15–09:00 | **Before the clock** (no app code) | Hub re-scopes the docs. Drafts appear in `personas/`: the student tutor graph and routing set, and the trader and streamer storyboards. | Drafts ready to review |
| 09:00–10:00 | **Kickoff** | Confirm owners. Odia speakers review the graph's Odia lines (30 min). Freeze contracts §2, §4, §6. 10-minute pre-mortem. Agree the cut lines below. | Owners and contracts fixed |
| 10:00–13:00 | **Walking skeleton** | S1: audio clock and scene control prop; one cue moves the scene. S2: tutor screen and entry point calling the stub. S3: stub that walks the graph, then Gemini on the first node; graph validator. S7: rubric mapping, evidence. | **13:00:** tutor screen ↔ stub ↔ scene cue works end to end; a preview deploy works |
| 13:00–19:00 | **The deep slice** | S1: all C-AM-08 cues (Odia and English), layout, marks, tests. S2: full tutor UI with chips, graph map, scorecard → rings, Odia/English. S3: full runtime, hints, evidence; routing test on 20 replies. S4: builder outline. S6 starts at 15:00. | **19:00:** student tutor works end to end on real Gemini; canvas sync done |
| 19:00–01:00 | **Breadth and B2B** | S2: organisation view; production deploy with the owner's go. S4: compiled concept preview. S6: trader video (21:00), streamer video (24:00). S3: latency, cost, robustness. Staggered rests. | **01:00:** all deployed; timed dry run 1 |
| 01:00–04:00 | **Fix and fallbacks** | Dry-run fix list. Record backup takes of the live student flow. | **04:00: feature freeze** |
| 04:00–07:00 | **Pitch** | Final deck; rehearsal × 2; juror Q&A drill. | Rehearsed twice within time |
| 07:00–09:00 | **Buffer** | Final checks; submission. | Submitted by 09:00 |

**Rest rule:** staggered 3-hour rests between 19:00 and 04:00. S2's and S3's owners are never asleep at the same time before 01:00. Nobody rests after 04:00.

## 6. Critical path

Graph reviewed (09:30) → S3 stub and S1 scene prop (13:00) → S2 tutor UI on the stub → S3 Gemini routing (19:00) → deploy → dry run (01:00). Everything else hangs off this path and can be cut.

## 7. Cut lines

Agreed at kickoff and applied without debate.

| Time | If this is true | Do this |
|---|---|---|
| 13:00 | The tutor skeleton isn't running end to end | Tutor UI goes chips-first with scripted routing while Gemini routing continues behind it. The builder drops to a mock preview |
| 19:00 | Routing is below about 15/20, or turn p90 is above 4 s | Chips become the primary reply; free text stays as a secondary option |
| 19:00 | Narration cues drift or fight the slider | Keep 3–4 key states only |
| 22:00 | The builder isn't working | Show the outline step only, or drop it |
| 01:00 | A breadth video isn't done | Show one video plus stills from the other storyboard. The organisation view becomes a slide |
| 04:00 | Anything is flaky | It leaves the demo. Nothing gets patched live |

## 8. What to measure (it becomes pitch evidence)

| # | Measure | How |
|---|---|---|
| E1 | **Sector packs are content, not engineering**: hours to author each sector's flow in the same graph format the student tutor runs | The hub logs start and finish times. Show the trader's graph JSON beside the student's |
| E2 | Tutor routing accuracy and latency (student) | 20 labelled replies; turn p50/p90 |
| E3 | Canvas sync | Manual cue timing, stated as such |
| E4 | Cost per tutor session | Tokens × price |
| E5 | Languages | Odia and English in the build. Hindi and Hinglish in the prototypes, labelled machine draft |
| E6 | Existing lab evidence | 17 Oct MATLAB trial: 4.7 s median, 10.1 s p90, checkpoint 1 → 6 |
