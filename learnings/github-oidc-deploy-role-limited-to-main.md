---
title: Deploy from GitHub Actions with OIDC, no stored keys, and trust only the main branch
tags: [ci-cd, iam, prosit-1, prosit-2]
source: Prosit 1 docs/ci-cd-and-operations.md (section 3); Prosit 2 learnings/infra.md (item 14); Prosit 2 knowledge/sessions/2026-10-30-cicd-pipeline.md
---

GitHub Actions exchanges a short-lived OIDC token for temporary AWS credentials, so no access keys sit in GitHub. Prosit 1's trust policy accepted `repo:<org>/<repo>:*` (any branch). Prosit 2 tightened it to `ref:refs/heads/main` only and replaced `*` resources with the specific ECR repositories, the ASG, the image-tag parameter, the S3 bucket and the one CloudFront distribution.

The deploy role can push images, replace servers, upload the PWA and invalidate the CDN. It cannot change infrastructure or read secrets or the database, which is intentional: `terraform apply` stays a human step after reading the plan.

Verify with the policy simulator and keep the output as evidence.

SmartCity: same role shape for device-firmware or ML-model deploys; scope S3 and model-registry actions to named resources.

## Related
- [CI/CD shape that worked: test everything, scan, then deploy only what changed on merge to main](cicd-pipeline-shape-test-scan-deploy-changed.md)
- [Capture least-privilege evidence with the IAM policy simulator](prove-iam-with-policy-simulator.md)
