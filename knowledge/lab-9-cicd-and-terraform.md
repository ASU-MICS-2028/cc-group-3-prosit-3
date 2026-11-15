---
title: Lab 9 - CI/CD pipeline with security scan and approval gate, plus Terraform
tags: [lab, prosit-2, ci-cd]
source: Lab 9 handout (week09_lab_Students)
---

Week 9, 3 h, team. Closes Prosit 2 (HealthConnect).

**Objectives:** CI with build, test and gated deploy; at least three automated tests; a secret-scanning step proven to catch a committed secret; a protected environment needing manual approval; IaC replacing at least one console-built resource; consolidate the package.

**Parts:** A Jest+supertest tests and a GitHub Actions workflow (checkout, setup-node, npm ci, jest, docker build); deliberately break a test. B gitleaks action; push a fake key on a throwaway branch. C deploy job with needs and environment: production with required reviewers. D Terraform VPC (init, plan, apply). E decommissioning checklist incl. a data-retention sentence.

**Deliverables:** passing and failing runs; secret-scan catch; paused-then-approved deploy; .tf plus plan output; checklist; 300-word report, updated diagram, sustainability and community-ownership paragraph, repo link (before Week 10).

**Rubric:** pipeline 25%; security smoke test 15%; IaC valid and applied 20%; sustainability plan 15%; report and completeness 15%; decommissioning 10%.

Extension: blue/green, Terraform module, deploy notification. Next: SLOs for SmartCity (SRE book Ch. 4).

## Related
- [CI/CD pipeline shape - build, test, scan, approval-gated deploy](ci-pipeline-build-test-gated-deploy.md)
- [Prove the safety net - break a test and commit a fake secret on purpose](prove-the-pipeline-works-break-it-on-purpose.md)
- [Scan for committed secrets in CI with gitleaks](secret-scanning-with-gitleaks-in-ci.md)
- [Terraform workflow - init, plan, apply; import or destroy pre-existing resources](terraform-init-plan-apply-and-import.md)
