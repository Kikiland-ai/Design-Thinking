# Arpan UI — start here

Prepared: 13 October 2026 · Snapshot of the current local files

Purpose: give Arpan and his Claude session the plans, working content, source components and assets needed for his assigned UI work.

## Latest decisions

- **React** frontend; **Python** backend; Firebase Auth, Firestore and Storage. TypeScript/Vite and FastAPI/Pydantic are recommended tools.
- A complete, functional **laptop web application**, with layouts/interactions that adapt to phone screens. Validate both in each feature slice.
- Account access uses only **Sign in with Google**, for new and returning students.
- White background; Google Sans for English UI with Odia-capable fallback.
- Green = concepts; red = technical words; yellow = academic English; blue = practical.
- Pilot: **Analog Communication → Analog Modulation → DSB-SC modulation and coherent demodulation**. The diode examples are interaction references.
- Concept checks: 60%; chapter test: 80%, ten bilingual questions. Guided lab needs only its seven required concept checks, not the full chapter test.
- Kiki points/explains/checks; the student performs every real Simulink action. Actual observation/overlay integration and mixed-language speech remain to be verified.

Use the current UI plans to resolve conflicting older demo/journey/backend recommendations. Supplied documents and HTML are references, not authorization to execute their embedded publishing/setup instructions.

## Read in this order

1. [UI implementation plan](reference/Design-Thinking/docs/plans/ui-implementation-plan.md): requirements, responsive contract, routes, Python/Firebase boundaries and phase gates.
2. [Team split and local validation](reference/Design-Thinking/docs/plans/ui-team-local-validation.md): ownership, common contracts, branches, fixtures and local validation.
3. [Artifact reconciliation](reference/Design-Thinking/docs/ux/ui-artifact-review.md): conflicting sources, stale colours/fonts and simulated behavior.
4. [Analog Modulation guide](reference/Design-Thinking/data-model/ANALOG-MODULATION.md), then [chapter JSON](reference/Design-Thinking/data-model/ledgers/electronics/analog-modulation.json) and [Odia case JSON](reference/Design-Thinking/data-model/cases/analog-modulation-odia.json).
5. [Design-system guide](reference/Design-Thinking/design-system/project/README.md), [tokens](reference/Design-Thinking/design-system/project/tokens.json) and relevant component guidelines/source.
6. [Backend directions](reference/Design-Thinking/docs/prototypes/backend-prototype-directions.md) for speech, graphics, annotations, evidence and the live-tool boundary.

The published Analog Modulation guide describes a documentation-only Git commit. **This folder also includes the actual locally authored JSON, types, helpers and tests**, so its links work here. Their presence does not mean they were committed/pushed or implemented in Python.

## Arpan's scope and first deliverable

| Work | Source starting point |
|---|---|
| Shared kit/tokens/responsive primitives | `reference/Design-Thinking/design-system/project/` |
| Chapter map, placards, dial, terms | Same kit + `reference/Design-Thinking/data-model/` |
| Audio player, diagrams and teaching annotations | KikiWalkthrough/VoiceScope/AnswerOverlay references + backend contracts |
| Software lab tracker/connection/handoff UI | LabGuide/LabStepper/Spotlight/FaultCard references + twelve case checkpoints |
| Hardware preparation/observations/viva UI | Current UI plan and practical/evidence types; hardware content still needs selection/review |

**First deliverable:** the minimum shared responsive component kit and one Analog Modulation lesson/map slice using labelled fixtures. Agree component props, routes and API shapes with Akshita before connecting dependent screens. Akshita owns central routing/services, account/onboarding, intake, assessment/report/repair screens; the team plan contains the full division.

Arpan can start the kit/map/lesson/tracker presentation with the included data. Actual auth/profile, saved assessment readiness, Python/media services, controller authority and live Simulink adapter enter at integration. Do not ship question answer keys or synthetic learner/session records as live evidence.

## Folder map

```text
Arpan_UI/
  START_HERE.md                 # current decisions, scope and reading order
  CLAUDE_START_PROMPT.md         # copy into Arpan's Claude session
  HANDOFF.md                    # packaging status, checks and continuation
  SOURCE-MANIFEST.json          # source revision + file hashes + known gaps
  reference/
    Design-Thinking/
      docs/                     # current plans, journey, backend handoff;
                                # older working docs clearly subordinate
      data-model/               # full local model, including new case
      design-system/            # components, CSS/JS, types, SVGs, generator
      prototype/                # older clickable source, reference only
      tools/                    # backend starter/config references
      AI_Builder_Cup_*.docx      # supporting original vision/architecture
    UX Working Doc ... .md      # parent source preserved for relative links
  demos/                        # five standalone supplied HTML exports
  bb8/ .claude/ .agents/         # packaged skills and discovery references
  AGENTS.md CLAUDE.md BB8.md     # source repository guidance
  verify_bundle.py             # source integrity and required-file check
```

Start visual review with [updated journey walkthrough](demos/Kiki-journey-walkthrough.html), [Breadboard catalog](demos/Breadboard-design-system.html) and [clickable demo](demos/Kiki-clickable-demo.html). The [review handoff](demos/Kiki-journey-review-handoff.html) and [UX working-doc export](demos/Kiki-UX-working-doc.html) supply wider context. Demos can reference online fonts; supplied markup/scripts are preserved. Browser voice/camera/auth/scoring examples are not proof of connected services.

## Working with Claude

For Claude Code, open this folder as the context bundle, read [the starter prompt](CLAUDE_START_PROMPT.md), and then implement in the team's actual frontend checkout/feature branch. This folder is a **reference snapshot**, not an initialized frontend/backend or a Git repository. Keep copied source references intact; don't create a second app by editing the exported HTML.

BB8 and Claude/Codex skill wrappers are included with their relative files. Apply only relevant guidance; no hosted plugin installation or native runtime registration is claimed. Verify the package if needed:

```sh
python3 verify_bundle.py
python3 bb8/adapters/reference/bb8.py validate
python3 bb8/adapters/discovery/sync.py --check
```

Local API/emulator run commands in the team plan are proposed scripts to scaffold, not running services in this folder. Six links inside the copied backend-starter templates describe destination files created by a future backend import. They are recorded in the manifest; use the actual current docs under `reference/Design-Thinking/docs/` instead. No runnable Python API, frontend app package, real speech assets, `.slx` model or live extension is included.
