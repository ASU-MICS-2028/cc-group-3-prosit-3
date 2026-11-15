---
title: Prove the safety net - break a test and commit a fake secret on purpose
tags: [ci-cd, security]
source: Lab 9 intro and Parts A-B
---

A pipeline only counts if failure really blocks deployment. Change an assertion to something false, push, confirm the run fails, fix. Likewise for security checks. Do the fake-secret test on a throwaway branch and delete it afterward.

## Related
- [Scan for committed secrets in CI with gitleaks](secret-scanning-with-gitleaks-in-ci.md)
- [CI/CD pipeline shape - build, test, scan, approval-gated deploy](ci-pipeline-build-test-gated-deploy.md)
