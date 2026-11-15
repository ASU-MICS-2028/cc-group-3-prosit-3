---
title: Scaling, reliability and monitoring (map)
tags: [process]
source: index of the notes below
---

Auto-scaling, load balancing, golden signals, alerts, load tests, failure design.

**Taught or given**

- [A cluster is many servers stacked together; heavy jobs like LLM training rent whole clusters](compute-clusters-for-heavy-workloads.md)

- [A load balancer presents one virtual IP and translates to real servers](load-balancer-virtual-ip-and-nat.md)

- [A scheduled function in another region pings /health so outages are noticed even if dashboards are down](synthetic-canary-health-check.md)

- [A target-tracking policy keeps average CPU near a set value (Lab 10 uses 70%, min 1, max 4)](target-tracking-cpu-auto-scaling-policy.md)

- [Add a dead-letter queue and make consumers idempotent](dead-letter-queue-and-idempotent-consumers.md)

- [Alibaba's next-generation load balancer takes the data path out of the balancer](nglb-full-bypass-load-balancer.md)

- [Amdahl's law - the serial portion caps speedup no matter how many cores you add](amdahls-law.md)

- [CAP theorem - a distributed system can guarantee only two of consistency, availability, partition tolerance](cap-theorem.md)

- [Client-generated IDs, record versions and cursor downloads make sync safe on flaky networks](idempotent-ids-and-versions-for-flaky-connectivity.md)

- [Data-intensive computing moves work to data spread across servers, not data into one machine's RAM](data-intensive-computing-distribute-chunks.md)

- [Direct server return (DNAT) versus full NAT](direct-server-return-dnat-vs-fnat.md)

- [Distributed computing spreads work over many sites with a master node coordinating](distributed-computing-master-node-map-reduce.md)

- [Dual-zone redundancy means each zone runs at about 50 percent](dual-zone-redundancy-50-percent-headroom.md)

- [Dynamic VM scheduling by chaining five existing algorithms](dynamic-vm-scheduling-five-algorithms.md)

- [Generate controlled CPU load with stress-ng to see monitoring work](stress-ng-generate-cpu-load-for-monitoring.md)

- [Google File System splits data into 64 MB chunks with a lightweight metadata master](gfs-chunking-and-lightweight-master.md)

- [Host a static fallback on a second cloud and time the manual failover](multi-cloud-fallback-failover-time-test.md)

- [If CPU stays low under load, scale on requests per target instead](scaling-not-triggering-io-bound-use-request-count.md)

- [k6 load test showed the database connection pool, not the API, was the limit](load-test-reveals-database-connection-pool-bottleneck.md)

- [k6 stages ramp virtual users up and down so you can watch scaling react](k6-ramping-load-test.md)

- [Liveness probes ask "is it stuck?" and readiness probes ask "can it take traffic?"](liveness-vs-readiness-probes.md)

- [Log one JSON line per request so the dashboard has real error-rate and latency data](structured-request-logging-middleware.md)

- [MapReduce is the batch-processing paradigm for when a design that works at 1,000 users meets millions](mapreduce-batch-processing-for-scale.md)

- [Measure connection quality with real stats](webrtc-measure-real-stats-not-impressions.md)

- [Microservices avoid the single point of failure of a monolith](monolith-vs-microservices-single-point-of-failure.md)

- [Microservices let each part scale on its own](microservices-scale-independently.md)

- [Multi-cloud data recovery with erasure coding and encryption](multi-cloud-data-recovery-erasure-coding.md)

- [Netflix lesson - design for failure and auto-scale to demand](netflix-design-for-failure-and-auto-scaling.md)

- [One dashboard must show latency, traffic, errors and saturation](four-golden-signals-dashboard.md)

- [Per-service idle timeouts instead of one global timeout](per-service-idle-timeouts.md)

- [Pick consistency or availability by what a wrong answer costs (bank vs social media)](cap-choice-bank-vs-social-media.md)

- [Pick three to five microservices per team, with sensible boundaries](microservice-boundaries-three-to-five-per-team.md)

- [Prove Kubernetes self-healing by deleting a Pod on purpose](kubernetes-self-healing-delete-pod-demo.md)

- [Prove resilience by stopping the DB while the simulator keeps publishing](buffer-test-stop-database-mid-stream.md)

- [Replication keeps data safe when a server fails, at the cost of duplicates](replication-for-fault-tolerance.md)

- [Rerun k6 at a much higher ramp (e.g. 500 users) to find what breaks first](stress-test-find-breaking-point.md)

- [Scale out vs up, and lead, lag or match capacity strategies](horizontal-vs-vertical-scaling-and-capacity-planning.md)

- [Test load-balancer failover by stopping an instance](load-balancer-health-check-failover-test.md)

- [Threshold load balancing, stop at 75 percent and resume below 25 percent](threshold-load-balancing-75-25.md)

- [Use more than one provider and read the SLA for availability](multiple-providers-for-availability.md)

- [What a useful CloudWatch dashboard and alarm set looked like in Prosit 1](cloudwatch-alarms-and-dashboard-practice.md)

- [Write one SLO for the ingestion tier and compute its monthly error budget](slo-and-error-budget-exercise.md)

**Found out by doing** (in `learnings/`)

- [A load balancer cuts silent connections after 60 seconds, so ping every 25](../learnings/websocket-idle-timeout-needs-heartbeat.md)

- [Check that a service and instance type exist in af-south-1 before designing around it](../learnings/check-service-availability-in-af-south-1.md)

- [Roll servers with instance refresh at MinHealthy 100 and MaxHealthy 200 to avoid downtime](../learnings/rolling-deploy-instance-refresh-minhealthy-100.md)

- [The outbox gap: saving data then publishing can lose the event](../learnings/outbox-pattern-for-lost-events.md)

- [Unconfirmed SNS email subscriptions are silently deleted after three days](../learnings/alarm-email-subscriptions-expire-after-3-days.md)

- [When the database is unreachable answer 503 with Retry-After; keep /health green, make /ready fail](../learnings/health-stays-200-ready-fails-when-database-down.md)

## Related
- [Lectures by week (map)](map-lectures.md)

- [SmartCity Accra brief and our scope (map)](map-smartcity-brief.md)

- [Labs 0–14 (map)](map-labs.md)

- [Course facts (map)](map-course.md)
