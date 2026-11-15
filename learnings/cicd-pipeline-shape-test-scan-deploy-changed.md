---
title: CI/CD shape that worked: test everything, scan, then deploy only what changed on merge to main
tags: [ci-cd, security, prosit-2]
source: Prosit 2 docs/decisions.md D-030; Prosit 2 knowledge/sessions/2026-10-30-cicd-pipeline.md; Prosit 2 learnings/infra.md (item 14)
---

One workflow on every PR and every push to main:
1. Tests for all parts (Terraform fmt/validate, API with a real Postgres, schema tests, Lambda tests, frontend, call page).
2. Security job: gitleaks over the full git history; Trivy on lockfiles (HIGH/CRITICAL with a fix fails) and on Terraform and Dockerfiles, with accepted findings listed with a reason in `.trivyignore.yaml`; CodeQL and Dependabot added as separate files.
3. On main only, deploy what changed: scan the API image before pushing so a vulnerable image never reaches ECR, pin the new image tag in an SSM parameter, roll the servers (instance refresh), smoke-test `/health`. Static site: build, upload, invalidate, smoke-test.

Why it was late: the course schedules CI/CD for Week 9, nobody recorded that as a decision, and the Prosit 1 `deploy.yml` was not copied. Until then every deploy was images built on one laptop, and "merging a PR does not update AWS" caught people out.

Not automated on purpose: `terraform apply`. Also: images must be built `--platform linux/amd64` on ARM Macs; instances give up pulling after about 90 s if ECR is empty.

## Related
- [A scan gate can turn red when no code changed; fix by bumping, not by deleting the scan](security-scan-gates-can-go-red-without-code-changes.md)
- [Roll servers with instance refresh at MinHealthy 100 and MaxHealthy 200 to avoid downtime](rolling-deploy-instance-refresh-minhealthy-100.md)
