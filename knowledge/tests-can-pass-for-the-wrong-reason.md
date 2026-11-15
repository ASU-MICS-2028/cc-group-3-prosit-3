---
title: Tests can pass for the wrong reason; test each rule separately and on real devices
tags: [process, ci-cd, prosit-2]
source: Lecture 11 (our team's lessons)
---

Lessons we presented: a test that expects rejection can pass because a different rule (consent) rejected first, so test one parameter at a time; unit tests used full birth dates and missed that real users entered only a year, found only by recording the demo on a real phone; hundreds of tests can still miss a scenario nobody wrote.

## Related
- [Add a human testing stage where a teammate uses the app like a real user and logs issues](human-testing-stage-before-release.md)
- [Out-of-band AWS changes (drift) can silently block terraform apply and stall deployments](configuration-drift-blocks-terraform-apply.md)
