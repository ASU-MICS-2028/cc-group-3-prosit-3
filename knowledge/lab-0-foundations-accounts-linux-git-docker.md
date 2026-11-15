---
title: Lab 0 - cloud accounts, Linux CLI, Git/GitHub and Docker foundations
tags: [lab, prosit-1, cloud-basics]
source: Lab 0 handout (week00_lab)
---

Preliminary lab, done before Week 1. Individual work plus a paired check. About 2-3 h pre-lab setup, a 4 h in-class session and an optional 4-6 h homework extension.

**Objectives:** secure AWS, Azure and GCP accounts (MFA plus billing alert); navigate and permission files on Linux; commit, branch, push and merge with Git/GitHub (including a simple merge conflict); build and run a Docker image; clone and build a classmate's Docker project unchanged.

**Parts:** Pre-lab (install tools, create accounts, GitHub account). A: secure accounts (MFA, $5/month budget, non-root IAM user). B: Linux essentials (pwd/ls, mkdir -p with brace expansion, find, cp -r, ln -s, chmod 755/644/600). C: Git (config, init, remote add, push -u, feature branch, pull request, merge). D: Docker (nginx:alpine Dockerfile with HEALTHCHECK, .dockerignore, build/run/ps/logs/exec/inspect, partner clone-build-run, cleanup).

**Deliverables:** one PDF report (LastName_FirstName_Lab0.pdf) with screenshots P1-P3, A1-A3, B1-B3, C1-C3, D1-D4, plus repo URL and final image size.

**Rubric (100):** Title page 5; Introduction 10; Objectives 5; Pre-lab setup 10; Methodology 20; Results/evidence 15; Observations and analysis 15; Conclusion 10; References 5; Presentation 5. Reflection questions and the homework extension (users/processes, PR review, Docker Compose, IAM read-only user) are not graded.

For SmartCity Accra: every later lab assumes these four skills.

## Related
- [Every cloud account gets MFA and a $5 billing alert on day one](cloud-account-baseline-mfa-billing-alert.md)
- [Do daily work as a non-root IAM user, never the root account](never-use-root-account-for-daily-work.md)
- [Clone and build a partner's repo to catch files that were never committed](partner-clone-build-catches-uncommitted-files.md)
- [git push over HTTPS needs a token or SSH key, not your password](git-https-push-needs-personal-access-token.md)
