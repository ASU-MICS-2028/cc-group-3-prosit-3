---
title: CI/CD pipeline shape - build, test, scan, approval-gated deploy
tags: [ci-cd, lab]
source: Lab 9 Parts A and C
---

GitHub Actions workflow in .github/workflows: on push; job build-test (checkout, setup-node, npm ci, npx jest, docker build tagged with github.sha); deploy job with needs: build-test and environment: production, which pauses for required reviewers, then runs e.g. kubectl set image with the sha tag. Need at least three meaningful tests (health, valid create, missing-fields rejected).

Fixes: auth failures are often secret-name typos; the approval gate fails to appear if environment: does not match the GitHub Environment name.

SmartCity Accra: reuse for ingest, API and ML containers.

## Related
- [Prove the safety net - break a test and commit a fake secret on purpose](prove-the-pipeline-works-break-it-on-purpose.md)
- [Scan for committed secrets in CI with gitleaks](secret-scanning-with-gitleaks-in-ci.md)
- [Tests pass locally but fail in CI - look for environment differences](ci-tests-pass-locally-fail-in-ci.md)
