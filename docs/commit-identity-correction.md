# Commit identity correction

13 October 2026

The authenticated GitHub connection was verified as `arpanvihan5-sketch`, user id `317357476`. The execution image's global Git configuration instead named Aditya Patro with an email GitHub associated with `adityathenerd`. Git uses this local configuration for author/committer metadata independently of the authenticated push identity.

Four Design-Thinking commits and five kiki-backend commits had that incorrect attribution. At the user's explicit request, their author and committer headers were corrected to `arpanvihan5-sketch` with `317357476+arpanvihan5-sketch@users.noreply.github.com`. Their timestamps, messages, and file trees were preserved. Descendants necessarily acquire new ids because their parent ids change; existing other contributors' author metadata was preserved.

The source baseline formerly identified as `9a7f369` is now `73d16c0d967a5d81dd74f1f28ef0defc48c8a778`; its file tree is identical. The earlier direction commit is now `aeca76b77c7cc943c8951a8183e4017a0ee2fe7b`. Exporter tests, setup guidance, and starter references were updated to the corrected source ids. Backend SOURCE.json and BB8/starter provenance are reconciled separately without altering the pinned product file bytes.

Global and repository-local author defaults were corrected. Root agent instructions and the reusable starter now require verification of author/committer identity before future commits, including in a fresh environment. Unchanged BB8 skill content was not modified.

The user authorized replacing the published histories. Updates use explicit expected-head leases so concurrent work is not overwritten. Local recovery bundles and old-to-new maps are retained outside both repos; no old-history backup branch is published. Old object links or GitHub contribution caches can persist after a branch history is replaced; the corrected main histories establish the current attribution.

Existing environments/clones must account for the history rewrite before continuing. Preserve uncommitted work and local-only commits, then use a fresh checkout or an explicit reconciliation; an ordinary pull of the old branch may recreate the old history. Do not force-reset a dirty checkout.
