# S5 · Content: the student tutor graph, and the breadth content for the videos

Owner: Arpan (proposed) · Where: `Design-Thinking/docs/knowledge-workers/personas/` · Tier: T0 (student graph), T1 (breadth content) · v0.2 (student-deep scope)
Estimate: 1 h of review at kickoff plus about 1 h handing over and fixing · Drafts written before 09:00 by the hub's drafting agents · Reports: 09:45, 15:00 · Rules: [sessions/README.md](README.md)

## Objective and why

Two content jobs, both mostly drafted before the clock starts:

1. **The student tutor graph** (critical path). The engine (S3) and the tutor UI (S2) both need it at 10:00. Its physics must be right, and its Odia must read naturally.
2. **The trader and streamer content** for the breadth videos (S6): persona cards, illustrative playbook excerpts, scenario numbers, graph-shaped tutor flows, storyboards. These show the same system re-targeted at two sectors. They are prototypes, not build slices.

## Drafts waiting at 09:00

| Folder | Contents |
|---|---|
| `personas/ece-phase-error/` | `graph.json` (8–12 nodes, Odia and English), `routing-set.json` (20 labelled replies), `README.md` (path, metrics, scene states, review checklist) |
| `personas/trader/` | `persona.md`, `playbook-excerpt.md`, `scenario.json` (checked with Black–Scholes), `tutor-flow.json`, `storyboard.md` |
| `personas/streamer/` | Same set, for the GTA 6 launch-week stream |

## Kickoff review (09:00–09:45)

1. **Physics (ECE teammate):** the phase-error reasoning, the numbers (cos 60° = 0.5, cos 90° = 0), and the misconceptions are the ones students actually have.
2. **Odia (native speakers):** every `say.or` line reads naturally, and English terms stay English. Fix in place; mark reviewed lines in the README.
3. **Hand-off at 10:00:** S3 copies the reviewed graph into the API; S2 reads it for the UI.
4. **Breadth content (by 15:00):** a quick plausibility pass on the trader and streamer drafts (a trading or streaming friend if one is reachable), then hand to S6.

## Guardrails

- Trader: process, not picks. Past, illustrative trade only; disclaimer on screen.
- Streamer: GTA 6 by name only; no publisher logos, artwork or footage.
- Hindi and Hinglish are machine drafts unless a native speaker has reviewed them. Names are placeholders. All data is illustrative.

## Starter prompt

```text
You are session S5 (Content) of the KiKi buildathon (student-deep scope, v0.2).
Read in order: Google AI Builder/CLAUDE.md;
Design-Thinking/docs/knowledge-workers/sessions/README.md;
Design-Thinking/docs/knowledge-workers/sessions/S5-content.md;
Design-Thinking/docs/knowledge-workers/05-contracts-v0.md section 4;
Design-Thinking/docs/knowledge-workers/personas/ece-phase-error/README.md.
Help me review the student graph: run the graph checks, list every Odia line for our native
speakers, and flag any physics or misconception that looks off. Edit only files under
Design-Thinking/docs/knowledge-workers/personas/. Commit only when I say; no AI attribution.
Report to the hub as sessions/README.md describes.
```
