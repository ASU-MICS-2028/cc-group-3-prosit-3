---
title: Lab 8 - structured peer design review and midterm preparation
tags: [lab, prosit-2, process]
source: Lab 8 handout (week08_lab_Students); Prosit 2 knowledge/labs.md; Prosit 2 knowledge/sessions/2026-10-27-architecture-diagram.md
---

Week 8, 3 h, team plus partner team. No new code: review what you built.

**Objectives:** present your architecture to outsiders; defend decisions without getting defensive; review another team using four fixed questions; find one concrete gap; revise the diagram in response (the revision is graded); consolidate Weeks 1-7 by active recall.

**Parts:** A 5-minute walkthrough (diagram, one proud decision, one known weakness). B review rounds: Round 1 and 2 each 25 min, Round 3 40 min for the private revision. C optional pre-midterm resource audit script.

**Deliverables:** before and after diagram screenshots (B1, B2); 200-word written peer review (one strength, one risk, one grading question), due end of Week 8.

**Rubric:** quality of live questions 30%; quality of responses 30%; written feedback 30%; evidence of real revision 10%.

Midterm prep: timed 15-minute answers to the three lecture scenarios, teach-back drill, self-made cheat sheet, and a checklist (scalability vs elasticity vs fault tolerance, VPC sketch, SQL vs NoSQL, least privilege, serverless fit).

**Also (Prosit 2 knowledge/labs.md; Prosit 2 knowledge/sessions/2026-10-27-architecture-diagram.md):** No new code. Paired with another team: prepare a 5-minute walkthrough (diagram from client to API to data to security to events, one decision proud of, one known weakness). Round 1 the other team asks four questions in order: where does this break at 10x load; the single weakest security link; what happens if the network drops mid-consultation or the database is briefly unreachable; one open question. Round 2 swap roles. Round 3 revise the diagram to fix at least one gap.

Deliverables: screenshot B1 ("before" with the gap circled) and B2 ("after" with the change highlighted and a caption), plus a 200-word written peer review (strength, risk, one question). Rubric: live questions 30, answers 30, written feedback 30, real revision 10; 60% is live, so everyone must explain every part. Optional: a pre-midterm audit script listing running compute across AWS, Azure and GCP.

Midterm checklist: scalability vs elasticity vs fault tolerance; sketch a VPC from memory; SQL vs NoSQL for three datasets; least privilege plus one at-rest and one in-transit mechanism; when serverless is and is not right; three practice scenarios.

## Related
- [Architecture review with four fixed questions](peer-review-four-question-framework.md)
- [Audit running compute on all three clouds before milestones](cross-provider-resource-audit-script.md)
- [Lab 9 - CI/CD pipeline with security scan and approval gate, plus Terraform](lab-9-cicd-and-terraform.md)
- [Lab 7 - event-driven serverless reminders and a WebRTC video call](lab-7-event-driven-serverless-and-webrtc.md)
- [HealthConnect's known weak points, useful input for a consolidated architecture review](healthconnect-known-weak-points.md)
