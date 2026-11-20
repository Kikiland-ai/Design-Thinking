# KiKi scope cleanup ledger

## Decision

KiKi’s hackathon focus is helping students overcome barriers to entering STEM. The first audience is Odia-medium students entering engineering. KiKi helps them understand technical concepts in Odia and English, build the English vocabulary used in coursework, and practise those concepts in a lab. The second mentor’s feedback, as relayed in the cleanup request, reinforced the original direction. Selling in any market is difficult, so the team is focusing on a specific student problem it can solve and demonstrate.

The existing [Odia ECE student journey](../ux/student-journey-odia-ece.md) and [Analog Modulation learning case](../../data-model/ANALOG-MODULATION.md) are the starting records for the STEM work.

## Git evidence

The working branch was fast-forwarded to `origin/main` at [`45180af`](https://github.com/Kikiland-ai/Design-Thinking/commit/45180af3f589bfdb11711766a4f8fbbc339a8ce9), *Widen KiKi to knowledge workers and plan the 24-hour buildathon*. Git dates the commit **20 November 2026, 09:05 IST (03:35 UTC)**. No reachable commit was dated 19 November UTC. The commit subject and content identify the widening work described in the request. Git records commit times, so the original drafting dates are unverified.

The diff against [`2a6c843`](https://github.com/Kikiland-ai/Design-Thinking/commit/2a6c843448d81062f89596b941516f8b7817ec79) contained **39 additions and zero modifications, deletions, or renames**. Every addition was under `docs/knowledge-workers/`. No tracked file outside that directory referenced the new material by path or tutor bundle name. The audit covers the Design-Thinking checkout and fetched refs.

## File ledger

All paths in this table are relative to `docs/knowledge-workers/` in `45180af`. Each original path was newly added. The commit remains available for historical reference, including student technical notes embedded in the broader plans.

| Original path | Disposition | Contents |
| --- | --- | --- |
| `01-kiki-for-knowledge-workers.md` | Removed | General knowledge-worker positioning and B2B onboarding hypotheses |
| `02-build-plan-24h.md` | Removed | Combined student build, organisation view and sector videos |
| `03-clarity-map.md` | Removed | Assumptions and decisions for the widened build |
| `04-judge-story.md` | Removed | Pitch and demo script arguing for sector breadth |
| `05-contracts-v0.md` | Removed | Shared interface proposal spanning student and non-student routes |
| `MISSION.md` | Removed | Widened buildathon mission and session board |
| `README.md` | Removed | Index and summary of the widening package |
| `personas/ece-phase-error/README.md` | [Moved](../prototypes/ece-phase-error/README.md) | Odia ECE phase-error teaching flow and review notes |
| `personas/ece-phase-error/graph.json` | [Moved](../prototypes/ece-phase-error/graph.json) | Bilingual tutor graph for coherent demodulation |
| `personas/ece-phase-error/routing-set.json` | [Moved](../prototypes/ece-phase-error/routing-set.json) | Sample learner replies for the phase-error tutor |
| `personas/streamer/persona.md` | Removed | GTA 6 streamer persona |
| `personas/streamer/playbook-excerpt.md` | Removed | Streamer onboarding source material |
| `personas/streamer/scenario.json` | Removed | Illustrative stream analytics |
| `personas/streamer/storyboard.md` | Removed | Streamer breadth video |
| `personas/streamer/tutor-flow.json` | Removed | Generated streamer coaching flow |
| `personas/tools/README.md` | Removed | Instructions for the widening package’s generators and checks |
| `personas/tools/linkcheck.py` | Removed | Link checker for the widening package |
| `personas/tools/streamer_build.py` | Removed | Streamer scenario generator |
| `personas/tools/streamer_graph_draft.json` | Removed | Streamer tutor graph source |
| `personas/tools/streamer_scenes.json` | Removed | Streamer scene data |
| `personas/tools/trader_build.py` | Removed | Trader scenario generator |
| `personas/tools/trader_graph_draft.json` | Removed | Trader tutor graph source |
| `personas/tools/trader_scenes.json` | Removed | Trader scene data |
| `personas/tools/tutor_build.py` | Removed | Assembler for trader and streamer tutor flows |
| `personas/tools/validate_ece_graph.py` | [Moved](../prototypes/ece-phase-error/validate_ece_graph.py) | Standalone structural validator for the student tutor draft |
| `personas/trader/persona.md` | Removed | F&O trader persona |
| `personas/trader/playbook-excerpt.md` | Removed | Options desk onboarding source material |
| `personas/trader/scenario.json` | Removed | Illustrative options trade data |
| `personas/trader/storyboard.md` | Removed | Trader breadth video |
| `personas/trader/tutor-flow.json` | Removed | Generated trader coaching flow |
| `reports/README.md` | Removed | Reporting template for the widened build |
| `sessions/README.md` | Removed | Widened session index and reporting rules |
| `sessions/S1-canvas.md` | Removed | Canvas brief tied to the widened plan and contracts |
| `sessions/S2-tutor-ui.md` | Removed | Tutor UI and organisation view brief |
| `sessions/S3-tutor-engine.md` | Removed | Tutor runtime brief tied to the widened contracts |
| `sessions/S4-builder.md` | Removed | Lecture-note builder brief tied to the widened plan |
| `sessions/S5-content.md` | Removed | Student tutor and breadth-video content brief |
| `sessions/S6-breadth-videos.md` | Removed | Trader and streamer production brief |
| `sessions/S7-story-gtm.md` | Removed | Widened pitch, market and business model brief |

## Result and handoff

- **Completed.** Removed 35 files and moved the four student-only tutor files to [the ECE phase-error prototype](../prototypes/ece-phase-error/README.md) as requested. The graph and routing examples match the original bytes. The README records the student-specific integration notes and review status. The wider plan and contracts are available in Git history.
- **Verified.** The scope rollback originally matched the pre-widening tracked tree. The follow-up aligned the README, backend active plan and linked handoff guides. The only new paths are this ledger and the four prototype files. The tutor validator checked 11 nodes, 12 paths and 20 routing examples. All four lesson ledgers passed and all 13 seeded validator errors were caught. BB8 package and discovery-file checks passed.
- **Next.** Continue from the student journey and Analog Modulation case. The phase-error draft still needs a native Odia review, an ECE teacher review and verification in the live app before it can be presented as reviewed and integrated.
