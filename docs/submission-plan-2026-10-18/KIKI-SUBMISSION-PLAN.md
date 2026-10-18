# KiKi: pitch deck and demonstration plan

Prepared 18 October 2026, India time. This is a content and production plan, not a completed pitch deck or a recording of the deployed application.

## Confirmed team and challenge context

- **Team:** APAA
- **Team leader:** Akshita Sahu
- **Official theme/title supplied by the team:** Media, Content & Digital Experiences
- **Theme scope:** AI solutions that transform how content is created, discovered, personalized, understood or experienced, including education.

**Team origin, confirmed by Akshita:** the team explored the official AI Builder Cup themes, chose Media, Content & Digital Experiences, identified gaps for students from regional-language backgrounds, and developed KiKi from that direction. No separate problem-statement ID has been supplied.

**Suggested wording for the deck or spoken introduction:**

> We started by exploring how AI could change the way people understand and experience content. Education stood out to us, especially for students from regional-language backgrounds. With KiKi, we chose to connect an explanation in a familiar language with the English terminology and practical work of an engineering course.

**Why this fits the theme:** KiKi changes how students understand and experience educational content through language support, interactive explanations and guidance while applying the concept. Language support, lessons and practical work should read as one connected content experience in the submission.

## The story to carry through both submissions

**KiKi is an AI learning companion designed for students from any regional-language background. It connects explanations in the learner's chosen language with technical vocabulary, interactive learning and live checks while they apply a concept.**

**Product audience:** students with regional-language backgrounds, including Kannada, Marathi, Odia and other languages. **Demo persona:** one Odia-speaking ECE student. **Current validated content/configuration:** the inspected implementation uses Odia/English and Analog Modulation. These are three different scopes. The product introduction must describe the broad audience before introducing the specific demonstration.

The product's value includes flexible language support, text/audio/interactive content, concept checks and live lab observation with criterion-based checking and guidance. Give the live lab pipeline equal narrative weight to language support.

Use one student, one subject and one experiment throughout the demonstration, after establishing the broader product. The recommended example is an illustrative ECE student, Bikash, who chooses Odia, studies Analog Communication and prepares for a DSB-SC modulation and coherent-demodulation lab. He demonstrates one configuration of KiKi. Explain DSB-SC once in everyday language: the student sends a message on a carrier signal, then tries to recover that message at the receiver.

The central question is simple: **Can the student connect the explanation they understood with the work they must do in the lab?** The demo answers it through observable actions.

Suggested opening copy:

> Students come to a course with different language backgrounds. KiKi brings explanations, technical terms and practical work into a learning experience they can follow. In this demo, we follow an ECE student who chooses Odia.

Suggested product description:

> Understand the idea in a language you're comfortable with. Explore it, check it, and apply it with KiKi checking your visible lab work as you go.

This is a problem framing, not a measured claim about all students. Bikash is an illustrative persona from the design repository, not a recruited participant or a testimonial. Use the confirmed theme-led origin above to explain why the team chose the problem. Do not turn that origin into a claimed classroom incident, interview study or learner testimonial.

The design repository's BB8/storytelling material was used as **local reference guidance**, not as a natively activated plugin. The narrative follows purpose, student benefit, actual experience and enabling features. The benefit of improved learning remains a hypothesis until evaluated with learners.

## What the repositories actually support

Fresh, separate `main` checkouts were inspected. Existing development worktrees were left unchanged.

| Repository | Inspected main revision | Meaning for this plan |
|---|---|---|
| kiki-web | `0ed7c069787a074fabcc58aaf4e3233f9d7f90ec` | PR #7, the Lab-mode screen-sharing implementation, is merged. Some status prose still describes its earlier branch state. The actual merge and code take precedence. |
| kiki-backend | `d70e0ceea9922a3c473c15d1c04698a21f57ee58` | Rechecked after the positioning correction. Main adds reconciliation notes over `e1cfd9f8`; runtime code is unchanged. Screen-reader baseline, floating guidance and the stored concept library are on main. |
| Design-Thinking | `2a6c843448d81062f89596b941516f8b7817ec79` | Source for the student journey, scientific content and product rationale. Earlier diode examples, pointer ideas and broad feature plans are not the current demo scope. |

### The application, from the student's point of view

The following walkthrough is the **Odia/ECE demonstration**, not a definition of KiKi's entire audience. Its live lab checks evaluate observable procedure criteria; an overall practical-proficiency grade is a separate assessment output.

1. **Sign in and set preferences.** Google sign-in establishes the learner. The app saves their course enrollment and language preferences. Self-reported Odia/English confidence is a preference, not an assessed score.
2. **Open the chapter.** Analog Modulation contains ten concepts, each with four lesson placards. The chapter view shows prerequisites and actual check results.
3. **Read with the support they choose.** The five-level dial changes authored Odia/English presentation and term support. English technical words retain their identity. A glossary offers meaning and pronunciation support. The dial does not silently generate a fresh lesson at every movement.
4. **Explore the idea.** C-AM-04 includes the DSB-SC signal/spectrum visual. C-AM-08 has an integrated, allowlisted phase-recovery scene and narration delivery contract. Those media need publication to the connected environment before recording them as deployed functionality.
5. **Check understanding.** Five-question concept checks score on the server. A pass is at least 3/5. The ten-question chapter test requires at least 8/10 and all ten concept checks. Feedback links back to relevant concepts. Existing retry questions repeat the authored set; fresh equivalent-question generation is not implemented.
6. **Prepare for the lab.** The student selects DSB-SC, reads twelve authored checkpoints and saves their prediction, project reference and observations. Seven relevant concept checks inform theory readiness. The chapter test is not required for this lab.
7. **Start screen guidance from Lab mode.** In the merged implementation, the student opens MATLAB Online, binds the KiKi extension to that tab, and explicitly shares that same Chrome tab. The browser captures sampled images. KiKi masks its own windows before sending them for analysis.
8. **Perform the work with live checks.** Gemini evaluates readable blocks, parameters and connections against the current authored criteria, returning match, mismatch or unknown with evidence. The backend validates the observation/context and decides when the current/next action can move forward. Floating windows display the accepted guidance inside MATLAB. The student places blocks, changes settings, connects wires and runs the model.
9. **Investigate a fault.** The full authored experiment compares baseline recovery, changes the receiver's local-carrier phase, inspects the effect, then restores the original setting. The student records an observation and explanation. Those reports are not automatically assessed practical proficiency.
10. **Resume saved work.** The app saves lesson position, attempts and preparation notes. A session link locates an account-owned preparation. KiKi does not save an unsaved external Simulink model on the student's behalf. Cross-device resume needs a shared hosted URL and actual device acceptance.

The current screen-guidance UI permits practice while theory checks are pending. It shows readiness but does not enforce the older journey's strict prerequisite gate for that practice mode. Do not claim that the integrated implementation blocks every lab until all seven checks pass. For a clean demonstration, use an account that has genuinely completed the relevant checks, or leave the pending state visible and explain it.

### Backend capabilities and the boundary for each

| Capability | What is present | Submission treatment |
|---|---|---|
| Mixed-language text | Prepared English source, references, glossary and protected values pass through translation/refinement and validation. Independent Odia/English preferences inform the job. | Explain Gemini's role. Do not claim an arbitrary uploaded textbook already becomes a complete reviewed course. |
| Speech jobs | Durable job admission, text-before-audio readiness, WAV delivery, bounded retry/cancel and saved stage reuse exist in the unified Python app. Real provider recordings exist. | Show ordinary playback from published assets. A generation dashboard/API tour is unnecessary for the main student story. |
| Stored concept library | Ten concept packets, forty placards, twenty-two narration clips and ten semantic scenes are preserved. SQLite holds metadata; asset files hold audio/graphics. | These are stored draft content assets, not ten fully published connected lesson experiences. The local database counts were inspected; audio bytes were not replayed in this review. |
| Frontend media compatibility | The export adapter currently projects sixteen compatible recordings across C-AM-01/02/03/08 and the C-AM-08 phase scene. Six whole-concept recordings and other scene types are outside the current app projection. | Prioritize one working C-AM-08 example. Do not say that all ten scenes are integrated. Preserve the existing C-AM-08 English audio when publishing additional content. |
| Screen capture | Explicit browser-tab sharing, receipt/provenance, lifecycle controls, owned sessions and fresh-frame admission exist. The Python path uses WebSockets. | Show sharing initiated from KiKi. Do not call sampled screenshots continuous video streaming. |
| Live assessment of observable lab actions | Gemini compares readable workspace evidence with authored action/checkpoint criteria and returns match, mismatch or unknown. The service validates completed results, freshness/context and repeated evidence before updating guidance. | Show one genuine visible-action check and, if reproducible, a mismatch or unclear-view case. Define this as live criterion-based checking; it is separate from a final practical-proficiency grade. |
| Lab tracking | Twelve checkpoints and forty ordered beginner actions cover construction, settings, wiring, running, comparison and phase-fault repair. Some actions need explicit student confirmation. | Say “screen-inferred action tracking” or “guided procedure.” A manual save/report is a student confirmation. |
| Floating KiKi windows | A Chrome extension displays current/next instructions, accepted observation and pause/resume inside MATLAB Online. | This is the supported guidance form. Do not present the stopped annotation/pointer experiment as implemented. |
| Main-app integration | Firebase-protected API relay, Firestore preparation-to-execution link, tickets, frame masking, SSE decisions and the Lab-mode connection panel are merged into kiki-web. | Code integration exists. The repository records automated controlled-target acceptance, not a completed integrated live MATLAB/Gemini acceptance run. |
| Upload and Library | PDF/PPTX/text extraction and Firestore text records exist. The current Library shows static upload-history cards. | Optional evidence in the deck. Do not imply that uploading automatically recompiles the curated Analog Modulation course or that originals are downloadable. |
| Concept assessment and feedback | kiki-web's API owns authored MCQ scoring, feedback, attempts and progress. Live lab criteria are evaluated through the separate observation/tracker pipeline above. | Explain both assessment paths. Do not attribute existing MCQ scoring to Gemini. Handwriting/OCR, viva grading and academic-English evaluation remain future directions. |

### Language flexibility: product scope and current implementation

The intended product supports a learner-selected regional language and adjustable English support. The current code still specializes that pipeline to Odia:

- `contracts/mixed_language.py`: `LanguageProfile` accepts `english_proficiency` and `odia_proficiency`; there is no general target-language field.
- `prototypes/mixed_script/pipeline.py`: `validate_input` requires `support_language: "or"`, Odia script and the Odia-led mode. Output span validation accepts `or`/`en` and checks Odia characters. Prompts also explicitly request Odia.
- `prototypes/mixed_language/service.py`: profile instructions still specify Odia-led grammar.
- Web/API profile contracts restrict the learning language to `or`/`en`; lesson text uses a fixed `{en, or}` pair. Dial, glossary, narration and review fields also contain language-specific assumptions.

Therefore, the pitch should present KiKi's **general regional-language product design**, while the evidence caption identifies the **Odia/ECE configuration demonstrated here**. To claim a working Kannada/Marathi switch, generalize and validate the request, generation, content/media and UI paths together. Model capability by itself does not make the existing application's language-specific validators accept those outputs.

See `KIKI-MULTILINGUAL-UI-AND-PIPELINES.md` for the pipeline audit and exact UI/contract changes. This correction updates the submission plans and supplies an implementation handoff; it does not silently change live application behavior.

### What is demonstrated versus what still needs acceptance

- **Historical real-tool evidence:** the backend records a 17 October MATLAB Online/Gemini run, with 79 reads and progress from CP-DSB-01 to CP-DSB-06, using the separate reader and floating windows.
- **Merged integration evidence:** the web repository records 180 frontend tests, 118 API tests and a real-extension/native-capture/Python test with an injected simulated analyzer. These are recorded results from the repository, not suites rerun during this planning review.
- **Still to prove:** the deployed main app, actual Firebase sign-in, published media, production extension, live MATLAB/Gemini reads, reconnect and saved state together on the exact submission release.
- **Cloud Run:** required by the supplied rules, but no working Cloud Run deployment is established by the inspected source. Treat it as pending until the hosting team supplies and verifies the real deployment.
- **Public access:** all three GitHub URLs returned anonymous HTTP 404 during this review. Authenticated Git access worked. Resolve the repository visibility/access issue before submission.

## The prescribed PowerPoint, slide by slide

The attached file was extracted and all sixteen slides were rendered and visually inspected. It is 16:9 with an organizer header, white content area and bottom rule on most content slides. Keep the existing Google Cloud/AI Builder Cup branding and required section order. Use KiKi artwork and product screenshots within that frame.

The numbering below is the **original template numbering**. Slide 2 is a download instruction, slide 15 is blank, and slide 16 is the organizer's thank-you screen. Preserve a mapping if the instruction/blank slides are removed from the submission copy.

Use native text for claims and captions so both people and automated readers can interpret them. The AI evaluator's rubric is unknown. Clear wording, explicit technology roles and matching evidence are useful; no writing approach can guarantee how an evaluator or AI detector will classify a submission.

### Original slide 1: Team Details

**Purpose:** identify the team, selected challenge and product immediately.

**Fill the prescribed fields:**

- Team name: **APAA**
- Team leader name: **Akshita Sahu**
- Problem Statement / selected theme: **Media, Content & Digital Experiences**

Use the exact official theme wording in the template field. No separate ID has been supplied, so do not invent one. If the form distinguishes a theme from a specific problem statement, identify this as the selected theme and describe KiKi's problem immediately below it.

**Add one concise product line beneath those fields:**

> KiKi connects learning in your chosen language with interactive explanations and live checks as you apply the idea.

**Visual:** a small KiKi logo beside the product line. Preserve the organizer's top banner. No screenshot collage or extra opening slide is needed.

**Avoid:** substituting a self-written problem statement for the official selected challenge, or assuming KiKi is also the team's registered name.

### Original slide 2: Download instructions

This tells participants how to download and edit the template. It is not a pitch-content prompt.

**Recommendation:** omit this instruction slide from the submission copy, retaining all required content sections in their original order. If the portal explicitly requires every slide unchanged, keep it as an organizer instruction page. Do not replace it with an unrequested problem/market slide and silently change the section mapping.

### Original slide 3: Brief about the idea

**Message:** the concept, the words and the lab belong in the same journey.

**Suggested slide copy:**

> **Understand the idea in a language you're comfortable with. Apply it with help that follows your work.**
>
> KiKi is designed for students from regional-language backgrounds. It connects flexible language support, interactive explanations and concept checks with live lab observation and guidance.
>
> This demonstration follows an Odia-speaking ECE student through Analog Modulation and a Simulink lab.

**Visual plan:** approximately 40% text at left and 60% product evidence at right. Use one clear lesson screenshot with Odia explanation and an English term visible. Add a smaller, readable crop of the corresponding MATLAB guidance window below it. Caption: “The same concept, from lesson to lab.”

**Why visual evidence helps:** a first-time viewer can immediately see what “bilingual” means and where guidance appears. Do not use a stock photo of students in place of the interface.

**Narrative bridge:** “The challenge is carrying that understanding into the language and tools of the course.”

**Theme connection for speaker notes:** “We chose Media, Content & Digital Experiences because KiKi changes how educational content is understood and used, from a bilingual explanation to an interactive example and a real lab task.”

### Original slide 4: Opportunities

The template asks about difference from existing ideas, how the solution addresses the problem, and its USP. Answer all three explicitly.

**Suggested slide copy:**

**Opportunity**
> A student often moves between an explanation, a technical glossary and a lab manual. KiKi keeps these steps connected around the concept they are studying.

**How it helps**
> The student chooses language support, explores and checks the idea, then receives live checks and the next action while working in the actual simulator.

**USP**
> Flexible regional-language learning linked to live lab checks and guidance, with the student performing every action.

**Visual plan:** a compact comparison, not an unsupported competitor ranking:

| Learning resource | Role it can serve | KiKi's proposed connection |
|---|---|---|
| Translation/explanation | Understand the material | Preserve the English terms inside the lesson |
| Video or lab manual | See a worked procedure | Use the visible workspace to guide the current action |
| Quiz | Check answers | Keep feedback and the next relevant concept in the same journey |

This compares resource roles, not verified product limitations. Do not claim named competitors lack these features without a separate current comparison.

**Confirmed origin line, best used in speaker notes:** “While exploring Media, Content & Digital Experiences, we identified a gap for students from regional-language backgrounds. We chose to connect understanding the lesson with using its English terms and applying it in the lab.” This explains the team's motivation without claiming a completed interview study or personal classroom incident.

### Original slide 5: List of features offered by the solution

**Message:** show the useful capabilities in the order a student needs them.

**Suggested feature copy:**

1. **Language support the student controls.** A chosen learning language, adjustable English support and technical-term meanings. The demonstration uses Odia/English.
2. **Concepts made visible.** Interactive signal examples and available narration.
3. **Checks with useful feedback.** Saved answers, server scoring and links to revisit missed concepts.
4. **A prepared lab session.** Predictions, twelve checkpoints and saved notes.
5. **Live lab checks beside the work.** Opt-in screen reading checks visible actions against criteria and updates the floating current/next instructions.
6. **A place to return to.** Saved lesson position, check history and lab preparation.

**Visual plan:** two large crops only: the dial/glossary and floating Now/Next windows. Associate the remaining features with short text labels. Six tiny full-screen screenshots will be unreadable.

**Release gate:** “available narration” and live guidance refer only to what works on the submitted deployed release. If media is not published, remove narration from this slide instead of showing a sample-mode screen as live.

**Keep the scope explicit:** regional-language flexibility is part of the product design. Only claim particular languages/courses as available after their complete path works. Handwriting marking, viva assessment, teacher analytics and automatic upload-to-course generation remain separate development directions. Do not promise autonomous lab operation or guaranteed mastery.

### Original slide 6: Process flow diagram or Use-case diagram

**Message:** one learning journey connects theory to practice.

**Diagram specification:** use five large readable stages across the slide, with a short revision loop below:

1. **Choose Analog Modulation**
2. **Learn with the chosen language support**
3. **Check the concept**
4. **Prepare the DSB-SC experiment**
5. **Share the lab workspace, perform actions and receive live checks**

Add a caption below the flow: “Demo configuration: Odia · ECE · Analog Modulation · Simulink Online.”

From “Check,” a below-threshold branch returns to “Revisit the missed concept.” From the lab, a line leads to “Save observations and continue later.” Keep arrows as diagram connectors, rather than writing an entire sentence as a chain of symbols.

**Small factual note:** “Concept check: 3/5 to pass. Chapter test: 8/10 after ten concept checks. Lab readiness uses seven relevant concept checks.” The practice implementation currently shows readiness and allows practice while checks remain pending.

**Visual:** diagram, not screenshots. Do not mix architecture components into this student flow.

### Original slide 7: Wireframes/Mock diagrams of the proposed solution (optional)

**Recommended use:** demonstrate how the same product fits reading and practical work. Because a prototype exists, label these **“Implemented interface layouts”** rather than pretending current screenshots are wireframes.

**Suggested slide copy:**

> **Reading stays focused. Lab guidance stays beside the simulator.**
>
> On a phone, the concept and word meaning remain readable. On a laptop, the student sees the current lab action while working in MATLAB Online.

**Visual plan:** a phone-sized crop of the concept/glossary on the left, and a larger laptop MATLAB view with the floating windows on the right. Annotate only two details: “Choose language support” and “See the current action.”

**Evidence rule:** a responsive browser viewport is acceptable if labelled as such. Do not label it a physical-phone test. Do not imply cross-device screen-sharing control is implemented.

If these are identical to slide 11, omit this optional slide rather than repeat the same screenshots.

### Original slide 8: Architecture diagram of the proposed solution

**Message:** identity, learning records and AI guidance have clear owners.

**Recommended diagram, to be reconciled against the actual deployment:**

- **Student browser:** React/TypeScript KiKi app, plus explicitly shared MATLAB tab and KiKi extension.
- **Firebase Authentication:** Google sign-in. The browser sends its ID token to KiKi's API.
- **KiKi application API on Cloud Run:** validates identity, course enrollment and preparation ownership. Serves lessons, scores authored checks and forwards allowed lab requests.
- **Cloud Firestore:** profiles, enrollment, versioned learning content, reading position, attempts, preparation notes and preparation/execution links.
- **KiKi lab/AI service on Cloud Run:** frame admission, Gemini adapter, validation, authored procedure and accepted current/next guidance.
- **Gemini:** language-conditioned content/speech preparation and image-based evaluation of visible lab actions against authored criteria. The current language implementation is Odia/English.
- **Private media storage:** published narration/scene assets, only if actually configured.
- **Durable lab/job store:** show the storage actually chosen by the hosting team. In the inspected backend this is local SQLite/file state. Do not relabel it Firestore without a completed migration.

Label the two important paths: **“Saved learning and checks”** and **“Opt-in lab screen analysis.”** The accepted guidance returns through the application API to the app/extension; the browser does not hold backend proxy secrets or Gemini keys.

**Suggested caption:**

> Firebase identifies the learner. Firestore keeps their learning records. Python services coordinate the content and lab pipelines. Gemini supports mixed-language media and live checking of visible lab work.

**Status note while planning:** Cloud Run boxes are the required target deployment, not verified current infrastructure. Update them to “deployed” only after the team proves the submitted route actually uses them. Do not substitute the private Worker/D1 QA prototype for the production path.

**Critical hosting implication:** Cloud Run's writable container filesystem does not persist after an instance stops. The lab backend currently needs persistent SQLite/file state and also retains some state in memory. A durable supported store and tested restart/reconnect behavior are required. Merely limiting the service to one instance does not make its filesystem durable. Cloud Run also applies request timeouts to WebSockets and provides only best-effort reconnect affinity. See [container storage](https://docs.cloud.google.com/run/docs/container-contract#file_system) and [WebSocket guidance](https://docs.cloud.google.com/run/docs/triggering/websockets).

### Original slide 9: Technologies to be used in the solution

**Message:** each required technology performs a concrete job.

**Suggested table:**

| Technology | Its role in KiKi | Visible evidence |
|---|---|---|
| Firebase Authentication | Google sign-in and learner identity | A new evaluator can sign in without an invitation |
| Cloud Firestore | Learning content, saved progress, check attempts and preparation notes | Save, reload and retrieve the same state |
| Cloud Run | Hosts the Python application API and lab/AI service, as deployed | Actual service revision and working request path |
| Gemini | Prepares mixed-language text/speech and evaluates visible actions in opted-in lab screenshots | Published audio plus one genuine criterion check and guidance update |
| React + TypeScript | Responsive learner interface | Lesson and Lab mode |
| Python + FastAPI | Ownership checks, server scoring, lab orchestration and provider calls | Working integrated API |
| Chrome extension + Simulink Online | Places guidance beside the real tool | Floating windows and student-performed action |

**Visual:** this table plus, if space allows, a small verified Cloud Run service crop. Full console dashboards are usually less useful than the architecture diagram. Use the exact deployed names/models in speaker notes, not a wall of version numbers on the slide.

Firebase and Firestore should both be named explicitly because the instructions name them separately. Describe Firebase Authentication as the identity feature, and Cloud Firestore as the database. Do not claim Gemini grades the current MCQs.

### Original slide 10: Estimated implementation cost (optional)

**Message:** reusable lesson media and sampled analysis make cost measurable, but live labs are not free by assumption.

**Suggested main copy:**

> Lesson media is prepared once and reused. Live lab cost depends mainly on how often KiKi analyses the workspace.

**A defensible illustrative estimate:**

- Planning workload: **100 ten-minute lab sessions per month**.
- Assumed average: **one admitted Gemini analysis every eight seconds**, or about **75 analyses per session**. This is a workload assumption, not the two-second screenshot capture rate or measured production average.
- Assumed tokens per analysis: **6,000 input and 1,000 output**, including all billable output. Replace with actual runtime usage.
- At the checked Gemini 3.5 Flash-Lite standard rates of **US$0.30 per million input tokens and US$2.50 per million output tokens**, screen analysis would be **about US$32.25/month** under those assumptions: `7,500 × ((6,000 × 0.30 + 1,000 × 2.50) / 1,000,000)`.

This is **only the vision-analysis component**, not the full operating cost. Add the selected Cloud Run configuration, Firestore reads/writes/storage, media storage/transfer, content/TTS generation, logs/builds and any external MATLAB licensing. Show separately if the evaluation uses an existing institutional MATLAB entitlement. Do not convert to INR without stating the rate/date.

**Visual:** four plain cost rows: AI screen analysis; hosting; database/media; one-time content preparation. Label estimates and assumptions in legible text. Replace the non-AI rows with actual configuration estimates before claiming a total. If the team cannot finish a credible total, omit this optional slide instead of presenting the partial figure as the price of KiKi.

Price references checked for this plan: [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing), [Cloud Run pricing](https://cloud.google.com/run/pricing), [Firebase pricing](https://firebase.google.com/pricing). Verify the deployed model and billing method still match before finalizing.

### Original slide 11: Snapshots of the prototype

**Message:** these are the real interfaces behind the story.

Use **three screenshots**, with the MATLAB image taking the largest area. Suggested composition: two readable crops in the left 40% and the lab screenshot in the right 60%.

1. **Bilingual lesson and glossary.** Caption: “Odia explanation, English terminology.” Include the actual technical word and meaning.
2. **A real submitted check and feedback.** Caption: “Feedback tied to this attempt.” Use the actual earned result, not a manufactured 5/5.
3. **MATLAB Online with KiKi's windows.** Caption: “The student acts. KiKi reads the visible workspace and updates the guide.” Show identifiable tool UI, a useful Now/Next action and the matching blocks/settings.

Use unique captures/crops here rather than duplicating slide 3/5 images. Keep one sentence of caption per image. Do not put invented floating windows over a screenshot.

If the lab image comes from the earlier standalone reader, label that fact. Prefer a fresh capture from the deployed integrated release so the prototype, video and links all describe the same product.

### Original slide 12: Prototype Performance report/Benchmarking

**Message:** report measured behavior and its scope.

**Usable historical evidence, with explicit label:**

> **Real MATLAB Online trial, 17 October. Separate reader with Gemini and KiKi windows.**
>
> 79 screen reads. 78 committed reads and one provider 503 recorded. Guided progress moved from checkpoint 1 to checkpoint 6.
>
> Frame received to committed guidance: **4.7 s median**, **10.1 s p90**.

**Below that, a separate current-integration row:**

> The merged app has recorded automated extension/capture/Python integration acceptance with a simulated analyzer. Live integrated and hosted acceptance remains to be measured.

The historical numbers come from repository trial notes, not an independent remeasurement or a population study. “78 committed” is not “98.7% visual accuracy.” The metric begins at server frame receipt, not when the student clicks, and ends at committed guidance, not necessarily visible overlay paint. Progress to checkpoint 6 is not proof that all twelve checkpoints were completed or that the student mastered the topic.

**Visual:** two adjacent latency bars labelled 4.7 s median and 10.1 s p90, plus a small trial-scope note. Add a test summary only if it fits. Do not make a learning-improvement chart without learner data.

**Better before submission:** replace or supplement the historical row with a hosted run: count, date, exact release/model, start/end definition, median/p90, failures and number of users. A small real measurement is more useful than an invented accuracy percentage.

**Meaningful checks to record:** save/reload succeeds; screen action produces a committed change; pause stops analysis; stop/reconnect is clear; another account cannot open the session; the actual tool model survives separately in MATLAB. Report pass/fail counts with denominators if measured.

### Original slide 13: Additional Details/Future Development (if any)

**Message:** finish the first learning loop before broadening it.

**Suggested slide copy:**

**Next release**
> Complete hosted acceptance, review Odia/scientific content and pronunciation, and publish compatible media for the remaining concepts.

**After the first student pilot**
> Add separately evaluated English-expression tasks, stronger practical evidence review and more engineering chapters.

**Longer term**
> Validate and release additional regional-language configurations, courses and supported lab tools through the same learning and live-checking workflow.

Language flexibility belongs in the main product description as well. This roadmap line concerns rollout and evaluation of additional configurations, not a change from an Odia-only product identity.

**Visual:** a short staged roadmap with dependencies. Use text labels, not a dense feature cloud. State that handwriting marking, viva assessment, hardware labs and teacher dashboards are planned if mentioned.

Do not make the roadmap look as though evaluation-critical deployment will happen after submission. The deployed prototype must already work when submitted.

### Original slide 14: Provide links

Preserve the required link categories and make them clickable.

**Suggested content:**

- **GitHub public repository:** kiki-web and kiki-backend, with an entry README linking both. Link Design-Thinking as supporting product/content material if it is also accessible and intended for release.
- **Demo video:** `[publicly viewable final video URL]` with its actual duration.
- **Final product:** `[deployed KiKi HTTPS URL]`.

**Short evaluator access note:**

> Start with Analog Communication → Analog Modulation. Google sign-in is available to new users. For live lab guidance, use desktop Chrome, the KiKi extension and a MATLAB Online account with access to Simulink.

This access note must describe the actual release. Provide a publicly accessible extension package and short installation guide if there is no store listing. A private package or localhost-only extension allowlist can block the headline feature even when the website opens.

**Visual:** plain readable links. A product QR is optional, but it cannot replace clickable URLs or a route a desktop evaluator can follow.

**Do not submit:** localhost, owner-private Sites previews, invitation-only videos, private repositories, a preview that bypasses the real backend, or a route requiring team approval to use.

### Original slide 15: Blank branded content slide

No required prompt appears here. Recommended: omit it rather than insert an unrelated slide. If retaining every template slide is explicitly required, use a small evidence/access appendix with the exact demo environment and benchmark scope. Do not move mandatory sections out of their prescribed positions.

### Original slide 16: Thank you

Retain the organizer's thank-you artwork. If adding one unobtrusive sentence fits without covering the artwork:

> KiKi helps students carry an idea from a familiar language into practical engineering work.

No extra feature claims or final wall of text.

## Visual evidence priorities

**Highest priority:** a readable bilingual lesson, the real glossary, a phase/signal interaction, actual result feedback, Lab mode's sharing control, and MATLAB with a genuine guidance update.

**Supporting evidence:** saved preparation after reload, a responsive concept view, static upload history and the deployed service configuration. These support the story but should not displace the main student journey.

**Use diagrams instead of screenshots** on the student flow and architecture slides. **Use screenshots instead of paragraphs** for language support, the lesson interaction, feedback and the lab experience.

Capture at 1920×1080 or higher where possible. Crop to the evidence instead of shrinking the entire browser. Keep enough browser/tool context to identify the real app. Use native text captions, a consistent KiKi spelling and the current Engineering Sketchbook interface. Avoid stock classroom imagery and decorative AI artwork where a real product action answers the evaluator's question.

Keep the template's title/footer area clear. Aim for roughly 40–65 main-copy words on explanation slides, with short captions. Architecture and features may need labels rather than prose. Test the exported deck at normal viewing size and in a PDF/image render, especially Odia glyphs, link readability and screenshot text.

The evidence asset list is in `KIKI-CAPTURE-LIST.csv`. The full recording sequence and read-aloud script are in `KIKI-DEMO-VIDEO-PLAN.md`.

## Brief description for the submission form

**Selected theme:** Media, Content & Digital Experiences. **Team:** APAA. **Team leader:** Akshita Sahu.

**Use this version only after the described services and media are actually deployed and verified:**

> KiKi is an AI learning companion designed for students from regional-language backgrounds. It connects explanations in the learner's chosen language with technical vocabulary, interactive examples, concept checks and live lab guidance. Our demonstration follows an Odia-speaking ECE student through Analog Modulation and a DSB-SC experiment in Simulink Online. Gemini supports mixed-language text and speech preparation and evaluates visible lab actions against authored checkpoint criteria. KiKi updates the guide while the student builds and runs the model. Firebase Authentication handles Google sign-in. Cloud Firestore stores profiles, lesson progress, check attempts and lab preparation. Cloud Run hosts our Python APIs and lab service. The current demonstrated language configuration is Odia/English; live procedure checks remain separate from an overall practical-proficiency grade.

If media is absent, remove speech/playback claims from the final submission and demo. If Cloud Run is not in the working request path, do not submit this paragraph as fact: complete that requirement or resolve the mismatch with the organizer.

## Submission release checks

These checks directly follow the supplied mandatory rules and the inspected implementation's actual dependencies.

1. **One exact release:** freeze the deployed frontend/API/backend revisions, media revision, extension build and model configuration. Capture the deck/video from that release.
2. **Public entry:** open the product URL in a fresh browser. Verify Google auth, authorized domain configuration and new-account onboarding without a team allowlist. A publicly reachable app can still require sign-in for private learner records; the evaluator must be able to complete it without an invitation.
3. **Headline lab access:** publish extension setup, allow the actual production origin, provide the required MATLAB/Simulink access instructions, and repeat the integrated real-tool trial. If licensing makes the full feature inaccessible to evaluators, resolve it before presenting the app as fully evaluable. A recording alone does not satisfy a working-prototype requirement.
4. **Cloud Run in use:** confirm successful live requests pass through the deployed services. Verify HTTP, incremental SSE, WebSocket capture, timeout/reconnect, ownership and provider errors. A service health page alone does not prove this path.
5. **Durable state:** preserve lab/job progress across an actual restart/redeployment using a supported durable store. Reconcile worker-local tickets and local SQLite/in-memory assumptions. One warm instance is not a persistence guarantee.
6. **Media actually available:** fetch/play the exact scene/audio used in the video through the authenticated production API. If assets are missing, the app intentionally falls back to text; that does not establish the narration claim.
7. **Saved state:** complete one actual check, view feedback, save preparation, reload and reopen it. Use real earned results. Have the student perform the lab actions and save their external model.
8. **Public source:** test both code repositories anonymously. Make source and supporting materials accessible throughout evaluation through the team's authorized release process. Verify that LFS narration assets can actually be downloaded and document `git lfs pull` where needed. A visible pointer file is not the audio file.
9. **Video access and duration:** watch the uploaded version from beginning to end in a signed-out browser. Check its displayed duration, captions, audio and permissions. No request-access screen.
10. **Deck format and links:** export from a copy of the supplied PPTX. Retain all required sections, test hyperlinks, and inspect rendered slides. Remove every unresolved bracketed field before uploading.
11. **Evaluation availability:** keep services, provider quota/billing, repositories, media, video and extension downloads available for the full evaluation period. Verify the complete student path again after the final deployment.

## Evidence and source map

Repository links below identify the inspected revision. They may remain inaccessible to anonymous readers until the team fixes public access.

| Source | What it establishes |
|---|---|
| [kiki-web main snapshot](https://github.com/Kikiland-ai/kiki-web/tree/0ed7c069787a074fabcc58aaf4e3233f9d7f90ec) | Actual main includes the integration merge, rather than only the earlier branch plan |
| [web status record](https://github.com/Kikiland-ai/kiki-web/blob/0ed7c069787a074fabcc58aaf4e3233f9d7f90ec/apps/web/active.md) | Recorded acceptance, media/storage boundaries and feature history |
| [Lab-mode implementation](https://github.com/Kikiland-ai/kiki-web/blob/0ed7c069787a074fabcc58aaf4e3233f9d7f90ec/apps/web/LAB_SCREEN_SHARE_IMPLEMENTATION.md) | Integrated relay, capture, masking, extension and acceptance limits |
| [Lab connection UI](https://github.com/Kikiland-ai/kiki-web/blob/0ed7c069787a074fabcc58aaf4e3233f9d7f90ec/apps/web/src/features/labs/LabConnection.tsx) | Real controls and labels to use in the recording |
| [lesson language rules](https://github.com/Kikiland-ai/kiki-web/blob/0ed7c069787a074fabcc58aaf4e3233f9d7f90ec/apps/web/src/features/learning/language.ts) | Five authored presentation modes, not on-demand generation |
| [media contract](https://github.com/Kikiland-ai/kiki-web/blob/0ed7c069787a074fabcc58aaf4e3233f9d7f90ec/apps/web/CONCEPT_MEDIA.md) | C-AM-08 scene, audio delivery, review state, no alignment and connected publication dependency |
| [backend active record](https://github.com/Kikiland-ai/kiki-backend/blob/e1cfd9f8a3af607c9f461bac1c9fd49267544a31/docs/plans/active.md) | Main promotions and historical real MATLAB run notes |
| [frontend API handoff](https://github.com/Kikiland-ai/kiki-backend/blob/e1cfd9f8a3af607c9f461bac1c9fd49267544a31/docs/handoffs/frontend-api.md) | Unified Python routes, mixed-language jobs and cloud/persistence boundaries |
| [production integration decision](https://github.com/Kikiland-ai/kiki-backend/blob/e1cfd9f8a3af607c9f461bac1c9fd49267544a31/docs/decisions/0010-kiki-web-api-fronts-lab-execution.md) | Browser uses kiki-web's Firebase-protected API, not the private demo reader |
| [stored content library](https://github.com/Kikiland-ai/kiki-backend/blob/e1cfd9f8a3af607c9f461bac1c9fd49267544a31/prototypes/concept_library/README.md) | Ten concepts, narration inventory, export compatibility and deferred publication |
| [screen-reader baseline](https://github.com/Kikiland-ai/kiki-backend/blob/e1cfd9f8a3af607c9f461bac1c9fd49267544a31/docs/baselines/screen-reader-v1.md) | Twelve checkpoints, frame/progress semantics and scientific experiment values |
| [authored beginner procedure](https://github.com/Kikiland-ai/kiki-backend/blob/e1cfd9f8a3af607c9f461bac1c9fd49267544a31/prototypes/lab_tracking/procedure.py) | Forty ordered actions, explicit confirmation boundaries and exact settings |
| [floating guidance implementation](https://github.com/Kikiland-ai/kiki-backend/blob/e1cfd9f8a3af607c9f461bac1c9fd49267544a31/prototypes/floating_guidance/README.md) | Extension behavior and local versus real-model acceptance levels |
| [illustrative student journey](https://github.com/Kikiland-ai/Design-Thinking/blob/2a6c843448d81062f89596b941516f8b7817ec79/docs/ux/student-journey-odia-ece.md) | Why language, technical vocabulary and lab work belong together; proposals are not implementation evidence |

Also inspected relevant application routes, result UI, API composition/configuration, document-text handling, backend composition/job transport, deployment notes and recovered-media handoff. This is a targeted source review, not a claim that every repository file was audited. No new paid model call, cloud change, deployment, account-data edit, code test-suite run or public publication was performed.
