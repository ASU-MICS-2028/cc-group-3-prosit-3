---
title: Questions the instructor and peers asked at the Prosit 1 presentations
tags: [course, process, lecture]
source: Lecture 7
---

At the Prosit 1 presentations the same kinds of question were put to several groups. Expect them again for SmartCity Accra.

- Scaling: "What metric triggers scale-out and why?" A vague answer ("traffic goes up") drew follow-ups. Name the policy and metric (for example request count per target) and justify it.
- Logs and metrics: "What do you actually use them for?" Collecting them is not enough; say which alarms, audits or forecasts they feed.
- Security: "Where is your firewall and where is your security focus?" Answers should name layers (network, application, data), not just "we have security groups".
- Reactive versus proactive: one group admitted its approach was reactive (flag and review incidents). The instructor wanted vulnerabilities looked at and hardening done.
- Anything marked as implemented should be demonstrable; a feature that only worked in a sandbox should be described as such.
- The instructor suggested using AI test-generation tools to cover rare code paths that normal tests miss, since rare branches are where hidden bugs live.

## Related
- [AgroConnect scales on ALBRequestCountPerTarget (500 per minute), not CPU](agroconnect-target-tracking-request-count-decision.md)
- [What a useful CloudWatch dashboard and alarm set looked like in Prosit 1](cloudwatch-alarms-and-dashboard-practice.md)
- [What the instructor expects from a prosit report and presentation](prosit-report-and-presentation-expectations.md)
