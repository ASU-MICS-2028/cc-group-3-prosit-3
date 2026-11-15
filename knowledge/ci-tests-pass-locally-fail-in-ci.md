---
title: Tests pass locally but fail in CI - look for environment differences
tags: [ci-cd, process]
source: Lab 9 Troubleshooting
---

Usual causes: missing environment variable, or a test needing a locally running database the runner lacks. Use a test container or a mocked connection. Export the Express app from server.js so tests can import it without starting a server.

## Related
- [CI/CD pipeline shape - build, test, scan, approval-gated deploy](ci-pipeline-build-test-gated-deploy.md)
- [Clone and build a partner's repo to catch files that were never committed](partner-clone-build-catches-uncommitted-files.md)
