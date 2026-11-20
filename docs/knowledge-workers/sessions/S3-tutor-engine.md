# S3 · Tutor engine: stateless decision-graph runtime with Gemini routing

Owner: Aditth (proposed) · Repo: kiki-web (`apps/api`) · Branch: `feat/tutor-api` · Tier: T0 · **On the critical path** · v0.2 (student-deep scope)
Estimate: 6 h (worst 9) plus 1.5 h deploy share · Starts 10:00 · Stub 13:00 · Real routing 19:00 · Numbers 20:00 · Reports: 13:00, 16:00, 19:00, 20:00 · Rules: [sessions/README.md](README.md)

## Objective and why

Tutor mode is KiKi's new core: a state-aware agent that walks a decision graph with the student, asks, cues the canvas, and reaches a conclusion with them. It is the original architecture's Learning Orchestrator with a finite action set (`AI_Builder_Cup_Technical_Architecture.docx`). **The graph decides; the model only labels the student's reply.** That makes it auditable, consistent with the course, and hard to derail. The build target is the student graph on coherent-detection phase error (C-AM-08).

## Read first

- `apps/api`: the FastAPI app, its Firebase ID-token auth dependency, route and settings patterns, `pyproject` (uv). Note: `apps/api` has no LLM SDK yet.
- The graph and routing set (drafted before 09:00, reviewed at kickoff): `Design-Thinking/docs/knowledge-workers/personas/ece-phase-error/graph.json`, `routing-set.json`, `README.md`.
- Patterns only (do not import from frozen code): kiki-backend `prototypes/json_stream/provider.py` (Gemini calls, key rotation) and `contracts/lab_tracking.py` (allowed IDs as response-schema enums).
- Models the team already uses: `gemini-3.5-flash-lite` (lab) and `gemini-3.8-flash` (text). Check the exact current names before use.
- Contracts: [05 §4 tutor](../05-contracts-v0.md#4-tutor-mode), [§6 evidence](../05-contracts-v0.md#6-evidence-and-cohort).

## Deliverables

1. **Graph files bundled with the API:** copy the reviewed graph to `apps/api/.../tutor_graphs/ece-phase-error.json` at 10:00. Add `GET /tutor/graphs/{id}`, which S2 needs for the graph map.
2. **Graph validator** (CLI and test): unique ids, every `next` exists, every node reachable from `start`, every path ends at a `conclusion`, `say` present in `en` and `or`.
3. **`POST /tutor/turn`**, authenticated and **stateless** (decision A2): the request carries the state; the response returns the updated state, KiKi's lines, the canvas cue, the route label, evidence, and the scorecard at the end.
4. **One Gemini call per turn.** The response schema's `label` enum is the node's `expect` ids + `misconceptions` ids + `unclear` + `off_topic`. Also return `quote`, `confidence`, and `expression {clarity, termsUsed}`. Minimal thinking. Prompt in a versioned file; it handles English, Odia, code-mixed and romanised Odia replies.
5. **Transitions:**
   - expect → its `next`;
   - misconception → its `next` (usually a `show` node that moves the phase scene);
   - `unclear` → the next hint rung (question, nudge, worked step, answer), then advance with level `not_yet`;
   - `off_topic` → restate the question;
   - a chip reply → routed like text (no model call needed if the chip maps to a label).
6. **The `ack`:** at most one short sentence, in the language of the dial, written by the model. KiKi's question is always the node's scripted `say`.
7. **Evidence and scorecard:** an `EvidenceEvent` per routed turn. The scorecard aggregates per metric with quotes. Next steps come from the graph's `nextSteps`: show each entry whose `when` matches the session (metric level, or a misconception that fired), plus every entry without `when`.
7a. **Routing rules (hub decisions, 03:55; contract §4):**
   - A chip with a `route` routes without a model call and earns no words or expression evidence.
   - After the fourth hint, advance through the node's **first** `expect` branch and record `not_yet`.
   - Words evidence comes from `expression.termsUsed` matched against `caseData.targetTerms`; expression evidence from `expression.clarity` on English or mixed free-text replies.
8. **Routing harness:** run the 20 labelled replies; report correct/20 and p50/p90 latency for flash-lite and flash. Pick on accuracy first, latency second.
9. **Tests** with a fake model: transitions, hint ladder, off-topic, chips, invalid model output → `unclear` (never a crash), idempotent `clientTurnId` (per instance).

## Acceptance

- By 19:00, the full student graph runs end to end with S2's UI on real Gemini.
- Never returns a node outside the graph.
- By 20:00, numbers reported: routing correct/20 (target 16 or better) and turn latency p50/p90 (target p90 at or below 4 s).
- The Gemini key comes from the environment or Secret Manager; user text is not logged outside a debug flag.
- Deployed as a new `kiki-api` revision only with the owner's go.

## Stub first (by 13:00)

A scripted `/tutor/turn` that walks the graph on chip choices or simple keywords, plus `GET /tutor/graphs/{id}`, so S2 can build the UI. Swap in Gemini on the first node as soon as the stub is handed over.

## Starter prompt

```text
You are session S3 (Tutor engine) of the KiKi buildathon (student-deep scope, v0.2). Working repo: kiki-web, apps/api.
Read in order: Google AI Builder/CLAUDE.md; kiki-web AGENTS.md;
Design-Thinking/docs/knowledge-workers/sessions/README.md;
Design-Thinking/docs/knowledge-workers/sessions/S3-tutor-engine.md;
Design-Thinking/docs/knowledge-workers/05-contracts-v0.md sections 4 and 6;
Design-Thinking/docs/knowledge-workers/personas/ece-phase-error/README.md and graph.json.
Check the branch and status, confirm which Gemini key and models we may use, then tell me your
plan for the 13:00 stub before editing. Commit only when I say; no AI attribution.
Report to the hub as sessions/README.md describes.
```
