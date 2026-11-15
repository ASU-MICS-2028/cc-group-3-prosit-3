---
title: Branch protection with one approval, and the traps of stacked pull requests
tags: [process, ci-cd, prosit-2]
source: Prosit 2 CONTRIBUTING.md; Prosit 2 docs/decisions.md D-021; Prosit 2 learnings/repo-and-tooling.md (section 6)
---

Setup: `main` requires a pull request with 1 approval, no bypass, squash-merge. Requiring approval from the path's code owner blocked merges, so it was dropped (CODEOWNERS still requests the right reviewer; any teammate may approve; nobody approves their own PR). Branch names: `feat/`, `fix/`, `chore/`, `docs/`, `labN/`. Commit messages imperative and scoped, such as `feat(infra): ...`.

Traps:
- Stacked PRs: GitHub groups them and the normal merge button and `gh pr merge` refuse. Avoid stacking; if it happens, use the merge-async API call with `merge_action=direct_merge`.
- Deleting a merged branch closes every PR built on it. Move the next PR first with `gh pr edit <next> --base main`, merge main in, then push a commit (an empty one works) because CI does not rerun on a base change.
- Merging to main does not deploy unless a deploy job exists.
- GitHub keeps one waiting run per branch, so a burst of merges can cancel older waiting deploy runs; compare against the last green main run instead of the previous commit.

Definition of done in the PR template: works, failure paths tried, evidence saved, notes updated, ADRs, task status, no secrets, cost tracker, AI use declared.

## Related
- [CI/CD shape that worked: test everything, scan, then deploy only what changed on merge to main](cicd-pipeline-shape-test-scan-deploy-changed.md)
- [Put the team's working rules in AGENTS.md so every teammate's coding assistant follows them](shared-agent-instructions-in-the-repo.md)
