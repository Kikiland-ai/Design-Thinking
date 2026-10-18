# KiKi: regional-language product scope, backend pipelines and UI changes

Updated 18 October 2026 after Akshita's clarification. This is a source-grounded correction and implementation handoff. Application source has not been changed by this planning update.

## Product statement

> KiKi is an AI learning companion designed for students from any regional-language background. It brings flexible language support, interactive learning and live lab checks into one journey from understanding an idea to applying it.

Kannada, Marathi and Odia are examples of the intended audience's languages. The demonstration follows an ECE student who chooses Odia. Language, course and experiment are properties of that demonstration, rather than a narrow definition of the product.

The earlier submission plan incorrectly put the Odia persona into the product definition. It also gave too little prominence to the live observation/criterion-checking pipeline. Both submission plans now correct that framing.

## The connected backend pipelines

### 1. Source text to language-supported explanation

**Input:** prepared English sentences, stable source/sentence IDs, source references, glossary and protected scientific literals, plus learner language preferences.

**Current path:** validate prepared source; translate to Odia-led text; refine the mixed explanation against the original source; validate language spans, protected English terms, numerical values and scientific literals; save the stages and provenance.

**Student benefit:** adjust the explanatory language while retaining formal terms and scientific content. The language policy is more than replacing English words with regional-language synonyms.

**What is generic in the design:** prepared-source processing, explicit profiles, staged jobs, stage reuse, ownership, cancellation/retry and provenance can support language-configured implementations.

**What is specialized in the current code:** the target language, prompt grammar, output script checks and accepted language-span codes are Odia-specific. The current endpoint is not a working arbitrary-language API.

Source: `contracts/mixed_language.py`, `prototypes/mixed_language/service.py`, `prototypes/mixed_script/pipeline.py`.

### 2. Mixed explanation to spoken explanation

**Input:** validated mixed text and a speech-ready representation. Formulas/units have spoken expansions while display text preserves the authored notation.

**Current path:** reuse validated text; generate WAV through the speech adapter; inspect media and retain provider/hash provenance; deliver text readiness separately from audio readiness. Failed speech need not discard usable text. Retry resumes the appropriate saved stage.

**Student benefit:** read and listen to the same explanation, with available playback controls.

**For language expansion:** the selected language must reach the speech script and pronunciation policy, clip manifest, actual asset delivery and player. Check the exact model/voice/language behavior with native speakers. A multilingual model does not by itself establish pronunciation quality for the application's use case.

**Current limits:** no evaluated sentence-level alignment. Do not fabricate word highlighting or automatically synchronized scene transitions. Saved recordings contain review state and exact language coverage.

Source: `prototypes/mixed_script/speech.py`, mixed-language service, web `CONCEPT_MEDIA.md` and `media_models.py`.

### 3. Concept content to interactive explanation and reusable media

**Input:** authored concept placards, semantic scene definitions, narration and source/version metadata.

**Current path:** query the stored concept library; validate packet/assets; project compatible media through the existing web publisher; publish an immutable revision with content-addressed assets; render only allowed scene types; fetch matching language recordings through the authenticated API.

**Student benefit:** manipulate a scientific parameter and connect the resulting curve/readout with the explanation. The scene demonstrates an ideal teaching model, while the real lab supplies separate experimental evidence.

**Language-general structure:** the same scientific relationship can support different language renditions. Language-specific labels, glossary, explanation and speech should stay bound to the same source/scene revision.

**Current evidence:** ten stored concept packets and semantic scenes, with a narrower frontend renderer/audio projection. The recovered content is present, but some original generation orchestration is absent. Do not describe a complete arbitrary-course diagram-generation pipeline as recovered or deployed.

Source: `prototypes/concept_library/library.py`, `web_adapter.py`, recovered-content handoff and web scene registry.

### 4. Shared workspace to live checking and guidance

**Input:** an explicitly shared browser tab, the selected experiment/model, current checkpoint/action, expected values and current session context.

**Current path:**

1. Start from the saved preparation in KiKi Lab mode.
2. Bind the extension and choose the actual MATLAB browser tab.
3. Capture sampled frames and mask KiKi's windows before encoding/upload.
4. Admit an owned, fresh frame with its exact session/checkpoint/view context.
5. Ask Gemini for criterion/action findings supported by the visible pixels.
6. Return **match**, **mismatch** or **unknown**, with evidence. Hidden settings and occluded wires remain unknown.
7. Validate complete provider output and recheck freshness/context. Provisional streamed findings do not move the guide.
8. Combine the accepted observations through the tracker. Visible progress generally needs two matching observations from distinct frames.
9. Update the authored current/next action and display it in the floating windows.
10. Preserve observations, reports and action history with the session journal.

**This is live assessment of observable procedure criteria.** It checks what the student has visibly configured or connected and whether the evidence supports the next step. That capability should be central in the pitch and demo.

**A separate claim:** an overall practical-proficiency grade, scientific comprehension, correctness of an unobserved action or expert-validated explanation. The current projection explicitly marks screen-inferred/student-reported progress as separate from assessment of those outcomes. Calling the existing workflow “live lab checks” preserves its actual value without implying those extra outputs.

The checking mechanics do not depend on the student being Odia-speaking. The current authored experiment is nevertheless DSB-SC and its displayed current/next procedure is primarily English. To offer the lab guidance in another selected language, localize the explanatory presentation while retaining canonical criterion IDs, block names, exact values and the same decision gates.

Source: `prototypes/lab_tracking/analysis.py`, `procedure.py`, `guided.py`, `service.py`, `prototypes/json_stream/analysis.py`, web `LabConnection.tsx` and capture/relay implementation.

### 5. Student response to feedback and saved continuation

**Concept assessment:** the web API assigns/scored authored MCQs, saves drafts/results and links feedback to missed concepts. Gemini does not currently grade those MCQs.

**Lab evidence:** visible findings, checkpoint history and student prediction/observation/explanation are distinct records. A student confirmation is labelled as such. It cannot be silently substituted for model-observed evidence.

**Continuation:** Firestore owns application progress/preparation links; the lab backend owns its current lab journal/state. The external simulator owns the model file. Resuming a saved preparation is different from transferring a live capture connection.

**Product benefit:** return to a useful next activity without collapsing reading, answers and practical work into a single unsupported mastery score.

## Concrete multilingual blockers found in the current source

| Layer | Current specialization | Required generalization |
|---|---|---|
| Job profile | `english_proficiency`, `odia_proficiency` | Selected learning-language code and a confidence value associated with that language; independent English support |
| Prepared-source validator | Exact Odia mode and script | Configured allowed language/script policy with unchanged preservation checks |
| Prompt | Odia-led grammar and native Odia instructions | Versioned language-specific prompt policy selected by the request/configuration |
| Output validation | Only `or`/`en`, Odia Unicode validation | Validate the selected script/language spans and preserve formal terms/values |
| App profile | Python and Zod restrict language to `or`/`en` | One shared supported-language contract with safe migration of existing profiles |
| Lesson DTO | Fixed `{en, or}` text | Versioned language-indexed renditions or an equivalent explicitly negotiated response |
| Glossary | English term and Odia meaning/pronunciation fields | Meanings and pronunciation support keyed by selected language |
| Media | Specific `or`/`en` clips and `nativeOdia` review fields | Language-bound narration/review metadata, availability and verified fallback |
| Scene delivery | Specific allowlisted renderers/content | Preserve scientific behavior and add localized labels/renditions without executing arbitrary scene code |
| Lab guidance | English authored current/next text | Localized presentation keyed to canonical action/criterion IDs; exact software labels and settings preserved |
| UI/fonts | Odia-specific labels and Noto Sans Oriya | Dynamic labels, script-appropriate fonts and layout verification for enabled languages |

These are implementation requirements, not reasons to describe the overall product as Odia-only. They are also why replacing the word “Odia” everywhere cannot establish working support for Kannada or Marathi.

## UI changes to make the product idea clear

### Welcome and sign-in

Current `features/auth/Welcome.tsx` says “Understand engineering in Odia.” Replace the product-level sentence with:

> Learn in a language you're comfortable with. Keep the technical terms. Put the idea to work.

A separate scope line can say:

> Explore the demo: ECE · Analog Modulation · Odia and English.

Keep the existing “Your learning. Your language.” identity on sign-in. Change the single-language helper into an entry to language preferences. The main promise should also expose lab checking, for example: “KiKi checks your visible lab work and helps you find the next step.”

### Onboarding and Profile

- Ask **“Which language would you like to learn in?”**
- Read selectable languages and capability/availability from the same contract the backend actually supports. Kannada/Marathi must not be enabled options that later fail against an Odia-only API.
- If the current submission still has one available regional configuration, state availability locally in this control. Keep the broader product introduction above it.
- Bind **“How comfortable are you in [selected language]?”** dynamically. Preserve a separate English-confidence question and the learner's control over support.
- A selected language must affect the actual content request/rendition. Do not save a Kannada preference and keep serving unlabelled Odia text.

Relevant files: `features/onboarding/Onboarding.tsx`, `features/profile/Profile.tsx`, `contracts/profile.ts`; API `models.py` and profile persistence.

### Language dial and lessons

Build the labels from the selected language. For Kannada, suitable labels would be:

1. Kannada with English terms and meanings.
2. Mostly Kannada.
3. Kannada and English.
4. Mostly English.
5. English with Kannada help.

Use the same pattern for Marathi, Odia or another enabled configuration. These levels describe presentation support, not measured proficiency or exact word percentages.

Preserve reading position and earned scores when changing the display language. Load the chosen rendition and correctly label unavailable content. English technical terms, equations and units should retain stable identities across renditions.

Relevant files: `contracts/profile.ts` (`DIAL_LABELS`), `contracts/api.ts` (`LanguageCode`, `BilingualText`), `features/learning/language.ts`, `LessonScreen.tsx`, term/glossary and narration contracts.

### Audio and interactive explanations

- Show the actual playback language beside Listen.
- Select narration by concept, placard, language and media revision.
- If the chosen language has no clip, explain that precisely while keeping its text usable. A different-language clip should not play as an invisible fallback.
- Keep scene controls language-aware while preserving scientific numerical behavior.
- Support the selected script's glyphs and text expansion. Kannada and Marathi require their own checks; a successful Odia layout is not their acceptance evidence.

### Live lab panel and windows

Make **live checking** visible in the UI hierarchy as well as the pitch:

- **Sharing:** active, paused or disconnected.
- **Current action:** the exact authored task.
- **Latest check:** accepted observed evidence, mismatch or an unclear view, when exposed by the server.
- **Next action:** the backend's committed instruction.

Suggested status wording, to map to real backend states:

- Inference pending: **“Checking the visible settings…”**
- Accepted match: **“The visible settings match this step.”**
- Accepted mismatch: **“This visible value differs from the step.”** Show the actual observed/expected value only if returned and readable.
- Unknown: **“Bring the relevant settings into view.”**
- Manual confirmation: **“Confirmed by you.”**

Never derive these statuses solely from an optimistic client timer or a provisional SSE message. Keep freshness/context and canonical criterion decisions on the backend. Avoid displaying “not assessed” as though no checking occurs: explain specifically that live procedure checks are separate from a final proficiency grade. Any eventual change to existing assessment guards needs its own backend contract and evidence.

Localized windows must preserve exact block names, menu labels, formula values and checkpoint IDs. The student continues to perform all actions.

### Home, course and demo identity

Show **Learning language: [selected language]** and the actual selected course. Put **Demo course** near the constrained ECE catalog where needed. The brand-level copy should not imply ECE or Analog Modulation is the only possible product context.

Do not add selectable courses with no actual catalog behind them. General audience positioning and released course availability should be clear in different places.

## Implementation order

1. **Product copy and demo labels:** welcome, submission copy, captions and explanation of live checks. These can change without pretending a new language is already available.
2. **Language contract:** decide the shared language configuration and backward-compatible profile/content representation. Keep existing Odia records and progress intact.
3. **Backend text and speech policy:** generalize requests, prompts, script/span validators, review metadata and asset keys together.
4. **One additional complete language:** use Kannada or Marathi to prove profile → text → glossary → audio → UI → saved continuation, and localized lab explanation where supported.
5. **UI behavior and rendering:** dynamic labels, font support, language-specific availability and responsive/keyboard behavior.
6. **Evidence:** record the successful second-language path and repeat live lab checking on the actual integrated release. Only then enable and claim that additional language as working.

This is an implementation handoff for the team's current work, not an instruction to publish unvalidated options or alter production during submission planning.

## Submission changes already made

- Broader audience in the product definition, slide 1, idea/USP/features and form description.
- Odia/ECE explicitly labelled as one demonstration configuration.
- Live criterion-based assessment/checking promoted in the feature list, architecture, technology explanation and video action sequence.
- Language rollout described as validation and release of additional configurations rather than changing an Odia-only product's identity.
- Intro narration updated; total video lengths remain 3:00 and 3:30.

## Source boundary

Rechecked backend main `d70e0ceea9922a3c473c15d1c04698a21f57ee58`; compared it with the earlier `e1cfd9f8` review. Only the active reconciliation record changed. Web main remains `0ed7c069787a074fabcc58aaf4e3233f9d7f90ec`.

Inspected the actual language profile, prompt/span/source validation, job service, lab analyzer and streaming decision path, repeated-evidence policy, progress projection, concept-library publisher adapter, welcome/onboarding/profile/lesson language contracts and the existing integration record. No new model call or real language-quality trial was run. No application source, account data, deployment or cloud configuration was changed.
