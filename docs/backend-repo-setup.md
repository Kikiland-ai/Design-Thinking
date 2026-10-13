# Move backend work to Kikiland-ai/kiki-backend

12 October 2026 · Reproducible context handoff

The revised directions and handoff were committed in `aeca76b`. The carryover baseline is **`73d16c0d967a5d81dd74f1f28ef0defc48c8a778`**, which also includes the subsequently reviewed green-concept/blue-practical component guides and artwork updates. Use that reviewed commit as the product baseline, even if `main` later changes. A new backend repo needs both a checked-in context snapshot and its own runtime/decision history; it cannot rely on the old chat being available.

## What carries over

The exporter copies committed product material at that exact SHA, preserving original relative paths under `context/design-thinking/`:

- Revised prototype proposal and handoff; latest student journey and Simulink recommendation.
- Working docs, diagrams, original vision/architecture DOCX files, transcript, README, and handover.
- Data-model types, subject profiles, worked ledgers, validator, migration tools, and clearly historical archives.
- Design-system components/assets and the clickable prototype as implementation references. These support speech, graphics, annotation, and source-link inspection; they are not placed in the backend runtime.

The complete supporting directories preserve working local links and scripts, while `context/README.md` labels current versus superseded sources. `context/KNOWN-GAPS.md` records the one pre-existing missing local UX reference and unverified capabilities. `SOURCE.json` records source repo/commit and per-file hashes. The source snapshot is a baseline, not an unreviewed rolling sync.

At the new repo root, the bundle installs BB8, Codex/Claude wrappers, local marketplace metadata, validation CI, backend agent instructions, source-integrity CI/checker, runtime-version suggestions, `.env.example`, Firebase emulator configuration, and the first-session `SETUP.md`. BB8 native hosted installation is separate; no organization automation is assumed active.

## Create and import

The attempted creation of the user's selected private `Kikiland-ai/kiki-backend` repo returned `Forbidden` through the current environment's GitHub CLI. The source repo push succeeded. Create the new **private, empty** repository in GitHub (no README/gitignore/license), or use an appropriately authorized local CLI:

```sh
gh repo create Kikiland-ai/kiki-backend --private
```

A committed local starter is already prepared at `/workspace/kiki-backend`; its initial push returned `Repository not found`. Once the empty remote is created and the environment identity has access, the short continuation is:

```sh
git -C /workspace/kiki-backend push -u origin main
```

For a different machine/environment, use the reproducible bundle/import steps below.

From this Design-Thinking checkout, build the starter:

```sh
python tools/prepare_backend_starter.py \
  --source-revision 73d16c0d967a5d81dd74f1f28ef0defc48c8a778 \
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

The later environment configuration starts with fixture modes and Firebase emulators. Attach real model/speech credentials through supported secrets/identity configuration when needed; they do not transfer from GitHub, files, or chat. Configure provider/download destinations using the supported network settings and preserve proxy/CA configuration. These are reference instructions, not context-boot actions. See [CONTEXT-BOOT.md](../tools/backend-starter/CONTEXT-BOOT.md) and [SETUP.md](../tools/backend-starter/SETUP.md) for the context-only prompt and later runtime guidance.

Root instructions make the next agent read sources in order, reconcile older types with newer confirmed decisions, and maintain `docs/plans/active.md` plus backend decisions. Relevant docs are local and versioned; private live Claude links are not assumed available. The two immediate unverified capabilities remain actual mixed-language speech and actual Simulink observation/highlighting.

## Completion boundary

The current work prepares the import and setup. Repo creation/population, configured cloud services, and a running backend are only complete after the corresponding commands and smoke checks succeed. The documentation does not claim those happened merely because a bundle was produced.
