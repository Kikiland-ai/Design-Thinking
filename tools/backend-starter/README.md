# Kiki backend starter

This starter carries the Design-Thinking product context and BB8 into a separate backend repository. It does not contain a running backend yet.

1. Read the [active plan](docs/plans/active.md) for the Odia ECE scope and current review status.
2. Follow [CONTEXT-BOOT.md](CONTEXT-BOOT.md) to load context, report readiness, and wait for the user's direction.
3. Read the [source map](context/README.md) for source precedence and the student materials included in the snapshot.
4. Run `python scripts/verify-context.py` to check the imported source snapshot if command access is available. [Environment setup](SETUP.md)

`context/design-thinking/SOURCE.json` records the source repo, exact commit, and SHA-256 for every copied product file. `STARTER-MANIFEST.json` describes the initial starter bundle; it is not a permanent freeze on new backend code. The source snapshot is a traceable baseline, while backend decisions and progress belong in this repository.

No credentials, Google Cloud project, API access, native BB8 plugin activation, generated speech, graphics engine, or Simulink connection are established by importing these files.
