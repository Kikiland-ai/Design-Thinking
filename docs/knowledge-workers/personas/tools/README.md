# Persona tools

These scripts generated and checked the persona content. They were moved here from a session scratchpad so the team can regenerate after a reviewer changes a number. Run them with `py -3 -I <script>` from this folder.

| Script | What it does | Writes |
|---|---|---|
| `trader_build.py` | Builds the illustrative trade: candles, legs, Black–Scholes prices (rate 6.5%, flat IV, calendar days / 365, prices rounded to ₹0.05 ticks), the Shapley split of the loss into spot, IV and time, and the `bsCheck` results | `../trader/scenario.json`, `trader_scenes.json` |
| `streamer_build.py` | Builds the illustrative stream: viewers and chat per minute, segment bands, the drop at about 40:00 and the recovery after 60:00, plus consistency checks | `../streamer/scenario.json`, `streamer_scenes.json` |
| `tutor_build.py` | Assembles each sector's graph-shaped tutor flow from the `*_graph_draft.json` and `*_scenes.json` files and checks graph shape and the scripted path | `../trader/tutor-flow.json`, `../streamer/tutor-flow.json` |
| `validate_ece_graph.py` | Checks the student graph and its routing set. Usage: `py -3 -I validate_ece_graph.py ../ece-phase-error` | nothing |
| `linkcheck.py` | Checks every relative link and anchor in a docs folder. Usage: `py -3 -I linkcheck.py ../..` | nothing |

**Order after editing a number:** run `trader_build.py` or `streamer_build.py` first, then `tutor_build.py`. The build scripts write the persona files at absolute paths under `Design-Thinking/docs/knowledge-workers/personas/`. Moving the repo means updating `OUT_DIR` / `BASE` at the top of each script.

All data is illustrative. Hindi and Hinglish text is a machine draft.
