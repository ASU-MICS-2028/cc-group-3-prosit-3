---
title: A scan gate can turn red when no code changed; fix by bumping, not by deleting the scan
tags: [ci-cd, security, prosit-2]
source: Prosit 2 learnings/infra.md (section 6); Prosit 2 knowledge/sessions/2026-10-30-cicd-pipeline.md
---

A newly published vulnerability in a dependency fails the Trivy step on the next PR even though the diff is unrelated. Fix: update that package (`npm update <name>`) and check the lockfile diff is tiny; if it truly does not affect the app, add it to `.trivyignore.yaml` with a reason and the task that removes it. Never delete the scan.

First scans found real issues: a request-crashing `body-parser` bug, npm left inside the runtime image (removed; the server only needs `node`), a load balancer passing malformed headers, and a load balancer allowed to send traffic anywhere (now only inside the VPC). CodeQL later flagged routes with no rate limit.

Related gotcha: a local `npm update` with a different npm version can rewrite the whole lockfile (it dropped platform markers the Alpine image needs). Check `git diff --stat` on the lockfile.

Also: CI on the frontend needed Node 24; jsdom and vitest versions failed on Node 20.

## Related
- [CI/CD shape that worked: test everything, scan, then deploy only what changed on merge to main](cicd-pipeline-shape-test-scan-deploy-changed.md)
- [Branch protection with one approval, and the traps of stacked pull requests](branch-protection-and-stacked-pr-traps.md)
