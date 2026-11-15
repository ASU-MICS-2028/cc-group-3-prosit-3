---
title: Course availability targets: HealthConnect 99.7%, SmartCity 99.5%, and what nines mean
tags: [course, reliability]
source: Prosit 2 knowledge/lectures.md (Week 2); Prosit 2 knowledge/brief.md
---

The Week 2 lecture names 99.7% for HealthConnect (also in the Prosit 2 brief, with 2G-capable telemedicine, 50,000+ records and 1,000+ concurrent users) and 99.5% for SmartCity.

Downtime allowed per year: 99% is 3.65 days; 99.9% is 8.76 hours; 99.95% is 4.38 hours; 99.99% is 52.6 minutes. So 99.5% allows about 1.8 days a year (roughly 3.6 hours a month) and 99.7% about 26 hours a year (about 2.2 hours a month); those two figures are computed here, not quoted from the slides.

Series parts multiply: two 99.9% components in series give about 99.8%. Add redundancy to raise it. The target should be stated in an ADR together with RTO and RPO.

HealthConnect honest note: single-AZ database, one NAT and one call server meant it did not claim the target by design.

## Related
- [Syllabus plan for Weeks 10 to 15 (Prosit 3 and exams)](course-schedule-weeks-10-to-15.md)
- [HealthConnect's known weak points, useful input for a consolidated architecture review](healthconnect-known-weak-points.md)
