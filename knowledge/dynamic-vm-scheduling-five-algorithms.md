---
title: Dynamic VM scheduling by chaining five existing algorithms
tags: [scaling, cloud-basics, lecture]
source: Lecture 9
---

Uneven load across VMs wastes money (idle VMs are paid for), slows tasks, and can overload a VM until it fails. Scheduling means placing tasks on VMs by their CPU and memory, like assigning lecturers to courses by specialty.

The reviewed paper chained five steps: share tasks (round robin with sunflower optimisation, favouring low cost), plan (hybrid ant-colony and genetic algorithm, avoiding busy VMs), watch (least response time), predict load from history, and move tasks (threshold plus least recently used).

Reviewer verdict: it invented no new method and claimed 95 percent task success, but tested only 100 tasks in a simulator and never tested each step on its own. The instructor wanted the reviewer to propose a follow-up (for example improve one step for a stated goal such as cost) suitable for an MSc project.

## Related
- [Threshold load balancing, stop at 75 percent and resume below 25 percent](threshold-load-balancing-75-25.md)
- [Cloud research relies on simulators because providers rarely share real data](simulators-vs-real-cloud-data.md)
