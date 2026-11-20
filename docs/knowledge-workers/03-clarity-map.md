# Clarity map: what we know, what we don't, and how we find out

v0.2 · 20 Nov 2026 · Status: **Proposed** · Owner: the hub session (see [MISSION](MISSION.md))

The aim is to turn vague worry into a short list of questions with owners and deadlines. **H0 = 09:00 Fri IST.** Gates: H4 = 13:00, H10 = 19:00, H16 = 01:00, H19 = 04:00 freeze, H24 = 09:00 Sat (see [02 build plan](02-build-plan-24h.md)).

## 1. Known knowns: built and proven (say these with confidence)

| What | Evidence | Boundary |
|---|---|---|
| The ECE app is deployed | Firebase Hosting `kiki-512012.web.app`; API `kiki-api` and lab engine `kiki-lab` on Cloud Run; Firestore `kiki-firedb`; CI on `main` (kiki-web `apps/web/active.md`, 19 Nov) | No signed-in walkthrough since the 19 Nov redeploy |
| Bilingual lesson, 5-notch dial, glossary, server-scored checks | kiki-web `features/learning`, `language.ts`; 259 web and 155 API tests recorded 18 Oct | Content exists in Odia and English only; Odia and scientific review still pending |
| Live lab checks in real MATLAB Online | 17 Oct trial: 79 reads, 4.7 s median, 10.1 s p90, checkpoint 1 → 6; floating Now/Next windows | Lab allowance currently used up (`KIKI_TRIAL_MAX_CHECKS=5`); checkpoints 5–12 not accepted |
| Narration | Odia clips for all 10 concepts, generated in advance with Gemini TTS | English for C-AM-08 only; no timing cues; unreviewed |
| The architecture generalises on paper | Two agents (orchestrator, copilot); subject-agnostic data model; the 12 Oct backend directions cover the new ledger | The shipped web and API contracts are ECE-specific (`C-AM-*` IDs, `{en, or}` text, exactly 10 × 4) |

## 2. Known unknowns: we know the question, we need the answer

**Updates in v0.2 (Arpan's answers, 20 Nov 03:15 IST):**

| Item | Now |
|---|---|
| K1 | **Resolved:** the clock runs 09:00 Fri → 09:00 Sat IST. Whether non-code drafting before 09:00 is allowed is assumed yes, not confirmed |
| K4, K5 | **Lower stakes:** the trader and streamer are prototype videos now. A plausibility pass is still worth it |
| K6 | **Proposed:** Odia and English in the build; Hindi (trader) and Hinglish (streamer) in the prototypes, labelled machine draft |
| K8 | **Applies to the student tutor:** measure by 20:00 |
| K9, K10 | **No longer apply:** no Lab mode changes and no lab-lite in this build |
| K14 | **Resolved:** the lab beat uses the recorded MATLAB clip |
| K2, K3, K7, K11–K13, K15–K16 | Still open; owners as listed |

| # | Question | Why it matters | Working assumption until answered | Owner | Resolve by | How |
|---|---|---|---|---|---|---|
| K1 | When does the 24-hour clock start, and what may be prepared before it? Can the existing codebase be extended? | Decides whether content, graphs and schemas can be prepared now | Extending is allowed; non-code preparation is allowed | Team lead | Before H0 | Official brief or organiser |
| K2 | Judging rubric and final format: live demo, video or deck; minutes; who the jurors are | Decides what is built versus shown | Live demo plus startup pitch, 5–7 min, technical and non-technical jurors | Team lead | Before H0 | Official brief |
| K3 | Who is in the 24 hours, for how long, in which roles; who runs the lab-polling work | Sets capacity | 4 people, about 17 productive hours each; polling work takes about 8 of one person's hours | Arpan | Before H0 | Team call |
| K4 | Who reviews the trader and streamer content for domain accuracy | A juror who trades or streams will spot an error in seconds | One reviewer per persona, 30 minutes each | Arpan | H6 | Friends, mentors, communities |
| K5 | Real or illustrative trade case and stream analytics | Credibility versus time | Illustrative but realistic, labelled as illustrative | Persona studio | H4 | Built from public market and platform patterns |
| K6 | Language per persona, and a native reviewer for each | Quality of the multilingual claim | Odia (ECE), Hindi (trader), streamer to decide | Arpan | Before H0 | Team |
| K7 | Gemini quota and billing for generation and TTS (429s seen in October after four quick TTS calls) | Content factory throughput | A paid-tier key is available | Backend | H1 | Quota check and a small batch run |
| K8 | Tutor latency per turn | Whether the conversation feels alive | One model call per turn; scripted lines use pre-generated audio | Tutor engine | H8 | Measure p50/p90 per turn |
| K9 | Timeline and interface changes of the lab-polling work | Collision risk with anything else touching Lab mode | Lab-lite uses its own one-shot route and does not touch capture or polling code | Lab owner | H1 | Short sync |
| K10 | How accurate Gemini's boxes are on dense charts and dashboards | Credibility of on-screen annotation | Coarse boxes on a snapshot are acceptable; a live overlay is a stretch | Lab-lite | H8 | Test on 5 real screenshots |
| K11 | Compliance wording for the trader | Regulatory exposure; juror trust | "Process, not picks": historical or paper trades only, no recommendations | GTM | H12 | Draft a disclaimer and a stage line |
| K12 | Evidence that an organisation would buy | Startup jurors ask about validation | No buyer conversations yet; present hypotheses and a validation plan | GTM | Pitch | 2–3 quick conversations if any are possible |
| K13 | Is production healthy after the 19 Nov redeploy? | Demo reliability | Yes, unverified | Frontend lead | H2 | Signed-in walkthrough |
| K14 | Can we show live MATLAB at all? (allowance used up; MathWorks hours) | The ECE "Do" moment | Use the recorded lab clip; live only if allowance and licence are reset | Lab owner | H2 | Check config and licence |
| K15 | Rules for referring to GTA 6 and showing game footage | Legal and juror perception | Name-only references; no publisher art; our own charts | GTM | H12 | Check the publisher's content policy |
| K16 | Privacy of screen sharing in a B2B setting | A predictable buyer objection | Captures stay private to the learner; only dimension evidence reaches the organisation | GTM | Pitch | Write the policy line |

## 3. Unknown knowns: things the team knows but hasn't said out loud

These cause the worst late-night arguments. Decide them explicitly at kickoff.

1. **What "depth" means for this build.** Proposed: the full Learn → Do → Reflect → Evidence loop is visible for every persona, and one mode is deep per persona.
2. **Who the first buyer is.** Each teammate may picture a different customer.
3. **Whether Odia stays the brand's anchor** or becomes one language among many.
4. **Whether the ECE app and the new workspaces look like one product.** Proposed: one landing, one design system, two code paths.
5. **Who owns the demo narrative and who presents.**
6. **What gets cut first when behind.** Agree the cut lines before H0, not at H14.

**Exercise (10 minutes at kickoff):** each person answers the six in one line each. The hub reconciles differences and records the decisions below.

## 4. Unknown unknowns: tripwires that surface them early

Unknown unknowns can't be listed, so the plan builds tripwires that make them show up while there is still time.

| Tripwire | When | What it surfaces |
|---|---|---|
| **Walking skeleton** on the deployed stack: sign-in → workspace → one tutor turn through Gemini → one canvas cue | H4 | CORS, auth, secrets, Cloud Run timeouts, quota, build guards |
| **Pre-mortem**: "It's the showcase and we lost. Why?" Three reasons each; the top five become owned risks | Kickoff, 15 min | Fears nobody voiced |
| **Sceptical-juror simulation**: a fresh session or a friend plays one technical and one business juror against the rubric | H12 and H18 | Questions we cannot answer yet |
| **Domain reviewer pass**, 30 minutes per persona | H6–H8 | Domain errors, wrong jargon, implausible scenarios |
| **Two timed dry runs** on the deployed build, on the venue network if possible | H16 and H20 | Latency, flaky steps, timing overrun |
| **15% unassigned slack**, feature freeze at H19 | Whole build | Absorbs the surprises above |
| **"New unknowns" line** in every session report, triaged by the hub at each checkpoint | Every report | Drift and silent blockers |

## 5. Architecture and scope decisions

| # | Decision | Rationale | Status | Revisit when |
|---|---|---|---|---|
| A1 | **v0.2:** tutor mode is built **inside the ECE app** for the student. ECE contracts get only additive, optional props. No generic workspace path in this build; the sector personas are prototype videos | The ECE contracts are coupled across about 15–20 TypeScript and Python files; the student is the only real build slice | Agreed (scope) | After the buildathon: migrate ECE onto packs |
| A2 | The tutor runtime is **stateless on the server**. Session state travels with each turn; evidence is written at the end | Cloud Run instances don't share memory; no new persistence work | Proposed | If sessions must resume across devices |
| A3 | **v0.2: dropped for this build.** No Lab mode changes at all. The lab beat is the recorded MATLAB clip. (Lab-lite stays a product idea: a user-triggered one-shot read with an annotated snapshot) | Scope is student-deep; the polling lane owns Lab mode | Agreed (scope) | After the buildathon |
| A4 | Factory narration is **synthesised one sentence at a time**, so cue timestamps are exact by construction. ECE cues are timed by hand and labelled "manual timing" | No alignment model is evaluated; the October audit forbids fabricated alignment | Proposed | When a validated aligner exists |
| A5 | Scenes are **deterministic templates**. Gemini picks a template and its parameters, validated against a schema; it never generates drawing code | Matches backend direction 3; keeps visuals correct | Proposed | — |
| A6 | **v0.2:** tutor graphs are bundled with the API (`GET /tutor/graphs/{id}`). Packs remain the shape for the builder's draft output and the sector flows | Simplest path for one real graph | Proposed | When organisations edit their own graphs |
