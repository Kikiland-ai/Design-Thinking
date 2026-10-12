# BB8 in new organization repositories

Status: proposal only. No org configuration or repository creation has occurred.
This proposal applies if the supplied target organization uses GitHub.

## Starter layout

Include `bb8/` with the unchanged skill/harness source and the portable adapter.
Merge `AGENTS.fragment.md` into each target's existing root `AGENTS.md` without
overriding repo conventions. Keep the BB8 version and source checksum recorded.
Do not use org-wide default instructions as proof of native plugin activation.

## Template route

Use a designated organization repository template containing these files. New
repos created from the template inherit them. Repos created using other paths
do not. Later template changes do not automatically update existing repos.
This is suitable when repo creation is controlled by an agreed provisioning path.

## Every-new-repo route

An organization-installed GitHub App or provisioning service handles
`repository.created`. Install with access to all intended repositories,
including future repos, and minimal Metadata-read, Contents-write, and
Pull-requests-write permissions for a PR-based rollout. An org administrator
must arrange the installation and secure webhook handling in its normal
platform setup; this session does not request or access credentials.

The handler should:

1. Verify the event signature and organization identity; deduplicate deliveries.
2. Wait until the repository has a usable default-branch head. Define a separate
   org-approved policy for empty repositories before creating their first commit.
3. Load a pinned, reviewed BB8 release; validate exact 21-skill inventory and links.
4. Check for existing BB8 instructions. Preserve existing AGENTS.md content and
   avoid replacing local changes or another BB8 version without an update policy.
5. Add missing BB8 files and a root instruction pointer in one branch/commit.
6. Open a PR when branch protection or organization policy requires review.
   Direct default-branch writes require an explicit organization policy.
7. Record bootstrap state and expose failed events for retries.

Event-driven bootstrapping is eventually consistent, not an atomic part of repo
creation. For BB8 to be present at the first commit, enforce creation through
the template-backed provisioner. A webhook fallback can cover other paths.

## Limits and maintenance

An org `.github` repo provides supported default community files; it does not
copy arbitrary AGENTS.md, skills, or workflows into every new repository.
Organization rulesets can govern changes, but do not install BB8 files.
Repository files alone do not activate a native plugin in IDE or hosted agents.

Pin and periodically upgrade BB8 through reviewed update PRs. Each host still
needs its own supported plugin registration or explicit reference-loading path.
