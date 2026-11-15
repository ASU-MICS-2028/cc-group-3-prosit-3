---
title: What slowed the team down in Prosits 1 and 2, and how to avoid it in Prosit 3
tags: [process, prosit-1, prosit-2]
source: Prosit 2 knowledge/sessions (2026-10-18, 10-22, 10-26, 10-30, 11-06); Prosit 2 learnings/infra.md (section 6); Prosit 2 learnings/lab7-webrtc.md; Prosit 1 docs/learnings.md
---

1. **Deadlines differed from the syllabus every time** (Lab 5 due 22 Oct, not the syllabus date; Lab 5 was built in two hours, with only Part A existing at 21:58). Take dates from Canvas or the README and confirm early.
2. **Lab handouts did not fit our project** (Lab 5 was the AgroConnect wrap-up; Lab 6 starter code used integer ids and an Aurora-only policy). Decide early, write an ADR, and say it in the report.
3. **CI/CD came late** because the course schedules it for Week 9; everything shipped by hand from one laptop and a merge did not update AWS.
4. **Single-person bottlenecks**: AWS access per person with MFA meant nobody else could reach the team account that night; one person held every deploy.
5. **Local tooling**: Docker crashing at 96% disk (keep 20 GB free), ARM images for x86 servers, Node version mismatches, one npm rewriting a lockfile.
6. **Console-only or region gaps** (Amplify, HealthLake, instance capacity).
7. **Scope**: the full brief was far bigger than four weeks; breadth-first with labelled sandbox mode, a tier plan and a freeze date (D-029, D-035) worked.
8. **Stale credentials and emails**: SNS confirmations lapsing, a stray plaintext password file.
9. **Late multi-PR merging**: stacked PRs and deleted branches closing others.

## Related
- [Cost tracking and teardown: what keeps billing and what to delete by hand](cost-tracking-and-teardown-checklist.md)
- [CI/CD shape that worked: test everything, scan, then deploy only what changed on merge to main](cicd-pipeline-shape-test-scan-deploy-changed.md)
