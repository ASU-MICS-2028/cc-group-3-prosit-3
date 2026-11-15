---
title: Out-of-band AWS changes (drift) can silently block terraform apply and stall deployments
tags: [iac, aws, prosit-2]
source: Lecture 11 (our team's lessons)
---

AWS created resources we had not declared, so Terraform saw differences and apply kept failing silently, pausing deployments for days. Lessons: watch pipeline failures actively, avoid console changes, run plan regularly to detect drift.

## Related
- [Tests can pass for the wrong reason; test each rule separately and on real devices](tests-can-pass-for-the-wrong-reason.md)
