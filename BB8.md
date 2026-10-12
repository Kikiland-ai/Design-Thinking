# Use BB8 in this repository

BB8 0.2.1 is bundled under `bb8/`, with 21 unchanged packaged skills.
The reference adapter is 0.1.0. Start with [AGENTS.md](AGENTS.md) and
[the BB8 usage guide](bb8/docs/BB8-GUIDE.md).

## Repo actions

Ask a host agent with this checkout and file tools:

> Use BB8 to implement [desired behavior] in [explicit scope]. Use
> engineering-implementation, present Now / Next / Later, make the local
> changes, and run the relevant checks. Report changed files and actual results.

For a failure, use engineering-debugging. For a read-only assessment, use
engineering-review. BB8 provides the procedures; the host performs the work.
Commit and push only when the user's task authorizes them.

## Validate and prepare reference instructions

```sh
python bb8/adapters/reference/bb8.py validate
python -B bb8/tests/test_reference_adapter.py
python bb8/adapters/reference/bb8.py prepare \
  --task 'Review the reference adapter for correctness' \
  --skill engineering-review \
  --scope bb8/adapters/reference/bb8.py \
  --mode read-only \
  --tool read \
  --reference harness/references/engineering-principles.md
```

Pass the prepared packet to an existing IDE, CLI, or chat agent through its
supported input mechanism. The loader does not execute a model or tools.

Native plugin discovery requires separate host registration. Repository files
alone do not activate BB8 in a hosted session. See the
[original setup runbook](bb8/SESSION-SETUP-RUNBOOK.md). The `bb8/` root itself is
the self-hosted capability directory; a hosted ZIP must have that sole top-level
directory.

## New repos in Kikiland-ai

See [the organization rollout proposal](bb8/docs/ORG-ROLLOUT.md). A template
includes BB8 only when repo creation uses the template. Covering all creation
paths requires an org-installed GitHub App or provisioning service handling
`repository.created`; it has not been installed by this change.
