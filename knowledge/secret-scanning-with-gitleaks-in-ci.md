---
title: Scan for committed secrets in CI with gitleaks
tags: [ci-cd, security]
source: Lab 9 Part B
---

Add gitleaks/gitleaks-action@v2 as a pipeline step; it fails the build when secrets look present. Verify with a fake key string on a throwaway branch (the lab uses an AWS-key-like string), then delete the branch locally and remotely.

The repo for SmartCity is public, so this is essential. Keep real credentials in GitHub Secrets or a secrets manager.

## Related
- [Prove the safety net - break a test and commit a fake secret on purpose](prove-the-pipeline-works-break-it-on-purpose.md)
- [git push over HTTPS needs a token or SSH key, not your password](git-https-push-needs-personal-access-token.md)
