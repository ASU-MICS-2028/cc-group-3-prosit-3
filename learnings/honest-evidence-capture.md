---
title: Capture evidence honestly: report the real result, label what is faked, never rewrite history
tags: [process, prosit-2]
source: Prosit 2 knowledge/sessions/2026-10-22-lab5-submission.md; Prosit 2 AGENTS.md; Prosit 2 CONTRIBUTING.md; Prosit 2 learnings/repo-and-tooling.md
---

Habits that paid off:
- **Report the real number.** The Lab 5 failover test passed 5 of 10 requests; the report said so instead of re-running until it looked good, and logged a follow-up task.
- **Say what is a stand-in.** Evidence from a second-account copy in Stockholm was labelled as such; synthetic data, simulated payments and a test licence register are labelled on screen and in the report.
- **Test the failure branch, not only the happy path** (bad input, repeats, outages, denied permissions, undo), and say which branches could not be tested. Never report a test as passing without running it.
- **Break it on purpose** to prove a test can fail.
- **Evidence files have fixed names from the lab checklist** in `evidence/labN/`, with the script that produced them beside them; a test script must not overwrite an old evidence file.
- **Do not edit history:** applied migrations, recorded evidence, accepted ADRs and session summaries stay; add a new one that replaces them.
- Assumptions are written as assumptions (the TURN cost note says "assumption, not measured" and refuses to quote an unconfirmed egress rate).

## Related
- [Capture least-privilege evidence with the IAM policy simulator](prove-iam-with-policy-simulator.md)
- [When the database is unreachable answer 503 with Retry-After; keep /health green, make /ready fail](health-stays-200-ready-fails-when-database-down.md)
