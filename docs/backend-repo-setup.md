# Move backend work to Kikiland-ai/kiki-backend

Updated 20 November 2026 · Reproducible context handoff

The 20 November scope decision restores KiKi’s focus on students entering STEM. For a new or explicitly refreshed snapshot, pin a reviewed Design-Thinking commit that includes the [scope cleanup ledger](plans/kiki-scope-cleanup.md), the [Analog Modulation case](../data-model/ANALOG-MODULATION.md), and the [phase-error tutor draft](prototypes/ece-phase-error/README.md). The starter's [active plan](https://github.com/Kikiland-ai/Design-Thinking/blob/main/tools/backend-starter/docs/plans/active.md) carries those decisions into the backend's `docs/plans/active.md`.

The October starter used `73d16c0d967a5d81dd74f1f28ef0defc48c8a778` as its reviewed pin. That pin has the student journey and prototype proposals. A source refresh updates the recorded commit and its file hashes together while keeping backend decisions in the backend repo.

## What carries over

The exporter copies committed product material at the chosen SHA and preserves original relative paths under `context/design-thinking/`.

- Current scope record, student journey, Analog Modulation case, phase-error tutor draft, and Simulink recommendation.
- October prototype proposal and handoff as implementation references.
- Working docs, diagrams, original vision/architecture DOCX files, transcript, README, and handover.
- Data-model types, subject profiles, worked ledgers, validator, migration tools, and clearly historical archives.
- Design-system components/assets and the clickable prototype as implementation references. These support speech, graphics, annotation, and source-link inspection; they are not placed in the backend runtime.

The copied directories preserve relative links and scripts. `context/README.md` explains source precedence, `context/KNOWN-GAPS.md` records missing references and pending trials, and `SOURCE.json` records the exact Git commit and per-file hashes.

At the new repo root, the bundle installs BB8, Codex/Claude wrappers, local marketplace metadata, validation CI, backend agent instructions, source-integrity CI/checker, runtime-version suggestions, `.env.example`, Firebase emulator configuration, and the first-session `SETUP.md`. BB8 native hosted installation is separate; no organization automation is assumed active.

## Create and import

The October handoff logged a `Forbidden` response when creating `Kikiland-ai/kiki-backend` and `Repository not found` when pushing its local starter. Check the target repo's current state before using the empty-repo procedure. If a new private, empty repo is needed, an authorized user can create it in GitHub or run the following command.

```sh
gh repo create Kikiland-ai/kiki-backend --private
```

From this Design-Thinking checkout, review the current committed `HEAD` for the scope, case and tutor files listed above, then build the starter using its exact SHA.

```sh
python tools/prepare_backend_starter.py \
  --source-revision "$(git rev-parse HEAD)" \
  --output /tmp/kiki-backend-starter.zip
```

The exporter reads a Git archive at the pinned revision, not uncommitted files. It packages locally, performs no network writes, and refuses to overwrite its output. It uses the checked-in starter templates alongside the pinned product/BB8 source; its manifest records the generator hash and each starter file hash.

Then import into the empty repo:

```sh
git clone https://github.com/Kikiland-ai/kiki-backend.git /workspace/kiki-backend
unzip -n /tmp/kiki-backend-starter.zip -d /workspace/kiki-backend
cd /workspace/kiki-backend
python scripts/verify-context.py
python bb8/adapters/reference/bb8.py validate
python bb8/adapters/discovery/sync.py --check
node context/design-thinking/data-model/validate.js context/design-thinking/data-model/ledgers
git add .
git diff --cached --check -- . ':!bb8/**' ':!context/design-thinking/**'
git commit -m 'Initialize backend with pinned product context and BB8'
git branch -M main
git push -u origin main
```

If the new repo already contains code/instructions, import into an isolated checkout and review collisions rather than extracting over it. This empty-repo procedure is not a merge workflow.

The scoped whitespace check checks newly authored starter files; copied BB8/product sources retain their original bytes, including legacy line endings/Markdown breaks. `.gitattributes` prevents checkout conversion in these preserved directories, and the integrity checker verifies their hashes.

## Set up the new work environment

Select **Kikiland-ai/kiki-backend**, branch **main**, and use its root as the workspace. The first session follows CONTEXT-BOOT.md: read core sources, report what was loaded or missing, and wait for the user's thoughts. It must not install, scaffold, configure, or start services automatically. Once the user requests implementation, provide Node 22, Python 3.12, Git, and Java 21 for emulators; after dependencies are locked, setup can use `npm ci` and the backend's declared checks. The starter itself has no npm lockfile or API yet.

The later environment configuration starts with fixture modes and Firebase emulators. Attach real model/speech credentials through supported secrets or identity configuration when needed. Configure provider/download destinations using the supported network settings and preserve proxy/CA configuration. The destination repo includes `CONTEXT-BOOT.md` for the first read-only session and `SETUP.md` for later runtime guidance. [Context boot template](https://github.com/Kikiland-ai/Design-Thinking/blob/main/tools/backend-starter/CONTEXT-BOOT.md) · [Setup template](https://github.com/Kikiland-ai/Design-Thinking/blob/main/tools/backend-starter/SETUP.md)

Root instructions make the next agent read sources in order, reconcile older types with newer confirmed decisions, and maintain `docs/plans/active.md` plus backend decisions. Relevant docs are local and versioned; private live Claude links are not assumed available. The two immediate unverified capabilities remain actual mixed-language speech and actual Simulink observation/highlighting.

## Completion boundary

The current work prepares the import and setup. Repo creation/population, configured cloud services, and a running backend are only complete after the corresponding commands and smoke checks succeed. The documentation does not claim those happened merely because a bundle was produced.
