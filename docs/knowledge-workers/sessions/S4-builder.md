# S4 · Builder slice: a professor's lecture notes → a draft KiKi module

Owner: Aditth (proposed, as a second session alongside S3), with Aditya as backup after the polling work · Repo: kiki-web (`apps/api` routes plus one `apps/web` preview page) · Branch: `feat/builder` · Tier: T1 · v0.2 (student-deep scope)
Estimate: 6 h (worst 9) · Starts 13:00 · Outline by 17:00 · Compiled preview by 22:00 · Reports: 17:00, 22:00 · Rules: [sessions/README.md](README.md)


## Objective and why

This is the "tribal knowledge builder" from the brief, shown on the student route. An organisation (here a college or a professor) turns its own material into a KiKi module. It is the B2B buyer's entry point, and it shows that content is generated from the organisation's sources rather than hand-authored. The Library already extracts text from uploaded PDFs and PPTX files into Firestore; this slice turns that text into a **draft** module.

## Read first

- kiki-web Library: the upload and text extraction path, and the Firestore text records (see `apps/web/src/features/library/` and the matching `apps/api` routes).
- The lesson shape the app already uses: four placards (definition, concept, application, recap), terms with English spelling plus Odia pronunciation and meaning (`contracts/learning.ts`). **Read it for shape; don't change it.**
- kiki-backend `prototypes/mixed_script/pipeline.py`: preservation checks (protected terms, numbers, literals). Its validators are Odia-only; don't copy them as they are.
- The existing scene renderers in `features/learning/scenes.tsx`: the builder only *suggests* one of them; it never generates drawing code.
- Contracts: [05 §1](../05-contracts-v0.md#1-domain-pack) for the draft's shape (concepts, placards, terms, provenance, review state).

## Deliverables

1. **`POST /builder/outline`:** from a Library document's text (or pasted text), return modules → concepts (MECE, 2–5 per level), each with a goal and source locators. Target: about 15 s or less.
2. **`POST /builder/compile`:** for one chosen concept, return four placards in the English source, an Odia rendition at dial level 2 (Odia with English terms), terms (English spelling, Odia pronunciation, Odia meaning, all drafts), a suggested existing scene renderer with a one-line reason, source locators, and review state `draft`.
3. **Language-generic code:** the target language is a parameter; validation uses a script-range table (`or`, `hi`, `ta`, `te`, `bn`, `mr`, `kn`) and preserves terms, numbers and units.
4. **Preview page**, for example `/library/:docId/build`: outline → choose a concept → compiled placards with term chips, an "Odia: machine draft" label, the suggested scene, and the source tags. **No writes into the published lesson catalogue.**
5. **Provenance in every response:** model, prompt version, timestamp, source document id.

## Acceptance

- On a real Analog Communication lecture PDF already in the Library, the outline comes back in about 15 s or less.
- One concept compiles with terms and numbers preserved, Odia labelled as a machine draft, and sources shown.
- Nothing in the published ECE lesson path changes.

## Starter prompt

```text
You are session S4 (Builder slice) of the KiKi buildathon (student-deep scope, v0.2). Working repo: kiki-web.
Read in order: Google AI Builder/CLAUDE.md; kiki-web AGENTS.md;
Design-Thinking/docs/knowledge-workers/sessions/README.md;
Design-Thinking/docs/knowledge-workers/sessions/S4-builder.md;
Design-Thinking/docs/knowledge-workers/05-contracts-v0.md section 1.
Check the branch and status, confirm the Gemini key and model with me, then tell me your plan
for the outline step before editing. Do not change the published lesson catalogue or its contracts.
Commit only when I say; no AI attribution. Report to the hub as sessions/README.md describes.
```
