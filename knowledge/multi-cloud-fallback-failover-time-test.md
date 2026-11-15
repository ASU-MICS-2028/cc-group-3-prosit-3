---
title: Host a static fallback on a second cloud and time the manual failover
tags: [lab, reliability, cloud-basics]
source: Lab 14 (week14_lab_Students) Part A Option 2
---

Option 2: deploy a static fallback page on a second provider (e.g. S3 website if the primary is Azure/GCP), simulate the primary being down by stopping its service, then time how long a human takes to redirect traffic (DNS or config change). That duration is the failover-time finding.

## Related
- [Lab 14 overview: advanced feature test, capstone integration, final architecture doc, presentation](lab-14-advanced-feature-capstone-final-presentation.md)
