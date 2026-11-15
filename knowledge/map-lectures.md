---
title: Lectures by week (map)
tags: [lecture, process]
source: index of the notes below
---

Every note that came from a lecture, grouped by lecture. Transcripts are not in the repo; these notes are the summary.

**Lecture 1**

- [Course learning outcomes (what quizzes and exams are built from)](course-learning-outcomes.md)
- [Data centre siting, latency and energy trade-offs](data-centre-siting-latency-and-energy.md)
- [ICS 534 grading weights and the late-work penalty ladder](course-grading-weights-and-late-penalties.md)
- [Lectures, labs, then prosit - how the course is structured](lectures-labs-prosit-course-structure.md)
- [Stop idle cloud resources to protect credits](stop-idle-resources-protect-credits.md)
- [The course is platform-agnostic - justify every provider choice](justify-provider-choice-platform-agnostic.md)
- [Three prosits - AgroConnect, HealthConnect, SmartCity](three-prosits-agroconnect-healthconnect-smartcity.md)
- [Use managed payment APIs and keep payments as a separate service](use-managed-payment-apis.md)
- [Use more than one provider and read the SLA for availability](multiple-providers-for-availability.md)

**Lecture 2**

- [AI use rules - verify output, never fabricate data](ai-use-rules-verify-never-fabricate.md)
- [Capex versus opex - why elastic cloud capacity beats owned servers](capex-vs-opex-elasticity.md)
- [Choosing a service model - time to market and data sensitivity](choosing-service-model-time-and-data-sensitivity.md)
- [Containers are lighter than VMs because they share the host kernel instead of bundling an OS](containers-vs-virtual-machines.md)
- [Data residency laws and consent drive where data may live](data-residency-and-consent.md)
- [Five essential characteristics of cloud computing](five-essential-cloud-characteristics.md)
- [Ground rules for community-engaged prosits (consent, sign-off)](agroconnect-community-ground-rules.md)
- [History of computing - heavy lifting keeps moving to the provider](cloud-computing-history-heavy-lifting-shifts-to-provider.md)
- [IaaS, PaaS, SaaS - control versus convenience](iaas-paas-saas-control-vs-convenience.md)
- [Lectures, labs, then prosit - how the course is structured](lectures-labs-prosit-course-structure.md)
- [Mix service models per component, not one for the whole system](mixing-service-models-per-component.md)
- [Netflix lesson - design for failure and auto-scale to demand](netflix-design-for-failure-and-auto-scaling.md)
- [NIST definition of cloud computing (SP 800-145)](nist-cloud-definition.md)
- [Problem-based learning cycle - Clarify, Explore, Systemize, Implement](pbl-clarify-explore-systemize-implement.md)
- [Public, private, hybrid and community cloud](cloud-deployment-models.md)
- [Serverless - pay per function invocation, not per server](serverless-pay-per-invocation.md)
- [Stop idle cloud resources to protect credits](stop-idle-resources-protect-credits.md)
- [The course is platform-agnostic - justify every provider choice](justify-provider-choice-platform-agnostic.md)
- [Three prosits - AgroConnect, HealthConnect, SmartCity](three-prosits-agroconnect-healthconnect-smartcity.md)
- [Use managed payment APIs and keep payments as a separate service](use-managed-payment-apis.md)
- [Week zero prerequisites (Linux, Docker, GitHub, databases)](week-zero-prerequisites.md)
- [What you still own on IaaS (patching, firewall, backups, scaling)](iaas-responsibilities-you-still-own.md)

**Lecture 3**

- [Accountability means every action can be traced to a user, through system logs](accountability-and-system-logs.md)
- [Authenticity means the sender and data are genuine, which gives non-repudiation](authenticity-and-non-repudiation.md)
- [Availability is about the system being up; accessibility is a different idea](availability-vs-accessibility.md)
- [Compromising one security goal often breaks the others](security-goals-are-interlinked.md)
- [Confidentiality is non-disclosure of any data; privacy is an individual's control over their own data](confidentiality-vs-privacy.md)
- [Cyber threats evolved from viruses and worms to ransomware, APTs and AI-powered attacks](threat-landscape-viruses-to-ai-attacks.md)
- [Cybersecurity, information security and computer security differ by what is protected](cybersecurity-vs-information-vs-computer-security.md)
- [Delay and degraded quality of service count as an availability failure](quality-of-service-deviation-is-availability-issue.md)
- [Insiders are anyone related to the organization, not only employees](insider-threats-need-not-be-employees.md)
- [Integrity covers data, services and systems, and applies to automated processes too](integrity-covers-data-and-services.md)
- [Integrity is protected with checksums, hashing and digital signatures](integrity-techniques-checksum-hash-signature.md)
- [Keep systems available with backups, redundancy and failover](availability-mechanisms-backup-redundancy-failover.md)
- [Logging for accountability trades off against privacy, and policy sets the balance](accountability-logging-vs-privacy.md)
- [The CIA triad (confidentiality, integrity, availability) is the core of security](cia-triad.md)
- [The CIA triad extends to a five-goal pentad with authenticity and accountability](cia-pentad-five-security-goals.md)

**Lecture 4**

- [A cluster is many servers stacked together; heavy jobs like LLM training rent whole clusters](compute-clusters-for-heavy-workloads.md)
- [A VM can be shipped as an appliance, but CPU architecture still matters](vm-appliance-and-cpu-architecture-portability.md)
- [Amdahl's law - the serial portion caps speedup no matter how many cores you add](amdahls-law.md)
- [Cloud work builds on operating systems and networking basics](cloud-engineers-need-os-and-networking-fundamentals.md)
- [Containers are lighter than VMs because they share the host kernel instead of bundling an OS](containers-vs-virtual-machines.md)
- [Containers fix the "works on my machine" dependency problem](works-on-my-machine-problem.md)
- [Data centers protect data with physical and software security layers](data-center-layered-security.md)
- [DevOps joins software development and IT operations](devops-joins-development-and-operations.md)
- [Distributed computing spreads work over many sites with a master node coordinating](distributed-computing-master-node-map-reduce.md)
- [Do not put frontend, backend and database on the same host](separate-tiers-across-hosts-and-networks.md)
- [Docker core concepts: image, container, Dockerfile, registry](docker-image-container-dockerfile-registry.md)
- [Immutable infrastructure: replace the image, never patch a running container](immutable-infrastructure.md)
- [Liveness probes ask "is it stuck?" and readiness probes ask "can it take traffic?"](liveness-vs-readiness-probes.md)
- [Microservices avoid the single point of failure of a monolith](monolith-vs-microservices-single-point-of-failure.md)
- [Microservices let each part scale on its own](microservices-scale-independently.md)
- [Pick three to five microservices per team, with sensible boundaries](microservice-boundaries-three-to-five-per-team.md)
- [SSH gives secure remote access; ports sit at the transport layer](ssh-ports-and-osi-layers.md)

**Lecture 5**

- [Amdahl's law - the serial portion caps speedup no matter how many cores you add](amdahls-law.md)
- [Big data is described by Volume, Velocity, Variety (and Veracity)](big-data-four-vs.md)
- [CAP theorem - a distributed system can guarantee only two of consistency, availability, partition tolerance](cap-theorem.md)
- [Data-intensive computing moves work to data spread across servers, not data into one machine's RAM](data-intensive-computing-distribute-chunks.md)
- [Exam and quiz format - mixed question types, calculation heavy, 3-hour final](exam-and-quiz-format.md)
- [Google File System splits data into 64 MB chunks with a lightweight metadata master](gfs-chunking-and-lightweight-master.md)
- [In-memory data in a container is lost on restart; make it persistent](persistent-data-vs-in-memory-containers.md)
- [IPv6 is gradually replacing IPv4 and is what makes IoT addressing possible at scale](ipv6-and-iot.md)
- [Offline-first design for unreliable connectivity](offline-first-design-for-low-connectivity.md)
- [Pick consistency or availability by what a wrong answer costs (bank vs social media)](cap-choice-bank-vs-social-media.md)
- [Replication keeps data safe when a server fails, at the cost of duplicates](replication-for-fault-tolerance.md)
- [Structured, semi-structured and unstructured data need different stores](structured-semi-structured-unstructured-data.md)
- [TCP is reliable, UDP is fast and lossy, QUIC is Google's newer transport](tcp-vs-udp-vs-quic.md)

**Lecture 6**

- [AI use rules - verify output, never fabricate data](ai-use-rules-verify-never-fabricate.md)
- [Attackers with a shell can hide their tracks, so protect and ship logs](audit-logs-can-be-tampered.md)
- [Block, object and file storage serve different jobs](block-object-file-storage.md)
- [CAP theorem - a distributed system can guarantee only two of consistency, availability, partition tolerance](cap-theorem.md)
- [Choose SQL for fixed-schema data and NoSQL or object storage for flexible data, and justify it](sql-vs-nosql-choice.md)
- [Core PWA technologies are the service worker, web app manifest and cache API](pwa-core-technologies.md)
- [Data residency plan - shard by country and keep personal data in its home region](data-residency-plan-sharding-by-country.md)
- [Do not put frontend, backend and database on the same host](separate-tiers-across-hosts-and-networks.md)
- [Exam and quiz format - mixed question types, calculation heavy, 3-hour final](exam-and-quiz-format.md)
- [Firewalls should block persistent flooding sources to stop DDoS](ddos-protection-firewall-blocking.md)
- [Get core features working before attempting advanced extras](core-features-before-advanced-features.md)
- [Heavy ML inference belongs on the server, not on low-end devices](heavy-ml-runs-server-side.md)
- [Lab 4 - managed Postgres, private object storage and an offline-capable PWA](lab-4-managed-database-storage-offline-pwa.md)
- [Offline sync needs a conflict resolution strategy, like merging in Git](offline-sync-conflict-resolution.md)
- [Offline-first design for unreliable connectivity](offline-first-design-for-low-connectivity.md)
- [Pick consistency or availability by what a wrong answer costs (bank vs social media)](cap-choice-bank-vs-social-media.md)
- [Prefer SSH keys with a passphrase over password logins to servers](ssh-keys-over-passwords.md)
- [SmartCity project uses sensors and Python libraries; it is the third project and part of the final exam](smartcity-uses-python-and-sensors.md)
- [Structured, semi-structured and unstructured data need different stores](structured-semi-structured-unstructured-data.md)
- [Users and insiders are usually the weakest security link](users-are-weakest-security-link.md)

**Lecture 7**

- [AgroConnect picked af-south-1 by measuring latency from Ghana (74 ms median)](agroconnect-region-selection-by-latency.md)
- [AgroConnect scales on ALBRequestCountPerTarget (500 per minute), not CPU](agroconnect-target-tracking-request-count-decision.md)
- [fck-nat instance versus managed NAT Gateway: about $3 versus $32 a month](../learnings/fck-nat-vs-nat-gateway.md)
- [Geography-aware networking and CDNs](geography-aware-networking-and-cdns.md)
- [Keep a human approving high-stakes ML recommendations](human-in-the-loop-ml-recommendations.md)
- [Keep servers and databases in private subnets behind the load balancer](private-subnets-behind-load-balancer.md)
- [Offline-first design for unreliable connectivity](offline-first-design-for-low-connectivity.md)
- [Pull-request checks then image build then rolling refresh](ci-checks-and-deploy-pipeline-prosit-1.md)
- [Questions the instructor and peers asked at the Prosit 1 presentations](prosit-1-presentation-qa-themes.md)
- [Terraform workflow - init, plan, apply; import or destroy pre-existing resources](terraform-init-plan-apply-and-import.md)
- [What a useful CloudWatch dashboard and alarm set looked like in Prosit 1](cloudwatch-alarms-and-dashboard-practice.md)
- [What the instructor expects from a prosit report and presentation](prosit-report-and-presentation-expectations.md)

**Lecture 8**

- [After Prosit 1 as a quick translation, Prosit 2 needs real engineering and database design](prosit-2-expects-engineering-and-database-design.md)
- [Essay answers are marked on the itemized points, not word count](essay-graded-by-itemized-points.md)
- [Quizzes continue after the mid-semester break, with a paper answer option](quizzes-and-paper-option.md)

**Lecture 9**

- [A load balancer presents one virtual IP and translates to real servers](load-balancer-virtual-ip-and-nat.md)
- [Alibaba's next-generation load balancer takes the data path out of the balancer](nglb-full-bypass-load-balancer.md)
- [Cloud research relies on simulators because providers rarely share real data](simulators-vs-real-cloud-data.md)
- [Data leakage, repeated runs and sanity-checking ML metrics](ml-evaluation-leakage-and-repeated-runs.md)
- [Deadline-aware GPU scheduling across mixed GPU types](gpu-deadline-scheduling-mixed-gpus.md)
- [Direct server return (DNAT) versus full NAT](direct-server-return-dnat-vs-fnat.md)
- [Dual-zone redundancy means each zone runs at about 50 percent](dual-zone-redundancy-50-percent-headroom.md)
- [Dynamic VM scheduling by chaining five existing algorithms](dynamic-vm-scheduling-five-algorithms.md)
- [Federated learning with edge-level averaging keeps data local](federated-learning-at-the-edge.md)
- [Multi-cloud data recovery with erasure coding and encryption](multi-cloud-data-recovery-erasure-coding.md)
- [Nano services on IoT sensors and the cache eviction choice](nano-services-iot-lru-vs-lfu.md)
- [Networking fundamentals (OSI and TCP/IP) are assumed course background](networking-fundamentals-prerequisite.md)
- [Per-service idle timeouts instead of one global timeout](per-service-idle-timeouts.md)
- [Reviewing technical papers and checking reproducibility](paper-review-and-reproducibility.md)
- [Threshold load balancing, stop at 75 percent and resume below 25 percent](threshold-load-balancing-75-25.md)

**Lecture 10**

- [A progress report states what was specified, what is built, and what is outstanding](progress-report-format-specified-built-outstanding.md)
- [AI use rules - verify output, never fabricate data](ai-use-rules-verify-never-fabricate.md)
- [Build the Smart City pipeline end to end on synthetic data now; plug in sensors later](smart-city-build-pipeline-first-hardware-later.md)
- [Deduplication with short hashes lets anyone who learns the hash claim a file; proof of ownership fixes it](proof-of-ownership-cloud-deduplication.md)
- [Edge compute lets sensitive data be used locally instead of moved to the cloud](edge-inference-keeps-data-on-premises.md)
- [Edge devices with CPU and GPU on one chip share memory, enabling zero-copy inference](edge-ai-shared-memory-zero-copy.md)
- [Four places to run ML: cloud, separate CPU+GPU, CPU-only, or a single-chip edge device](edge-vs-cloud-vs-cpu-gpu-tradeoffs.md)
- [IoT loop: sense at the edge, communicate over MQTT to a central store, compute and control](iot-sense-communicate-compute-control.md)
- [MapReduce is the batch-processing paradigm for when a design that works at 1,000 users meets millions](mapreduce-batch-processing-for-scale.md)
- [Pre-record a screen capture with voiceover so a live failure cannot derail the demo](pre-record-demos-screen-capture-with-voiceover.md)
- [SNS fan-out to one SQS queue per consumer, batch size 1, dead-letter queue each](../learnings/sns-fanout-sqs-per-consumer-and-dlq.md)
- [The prosit project counts toward the final exam grade (20 points instead of 40)](course-prosit-counts-toward-final-exam.md)

**Lecture 11**

- [Add a human testing stage where a teammate uses the app like a real user and logs issues](human-testing-stage-before-release.md)
- [Build the Smart City pipeline end to end on synthetic data now; plug in sensors later](smart-city-build-pipeline-first-hardware-later.md)
- [Check that a service and instance type exist in af-south-1 before designing around it](../learnings/check-service-availability-in-af-south-1.md)
- [Client-generated IDs, record versions and cursor downloads make sync safe on flaky networks](idempotent-ids-and-versions-for-flaky-connectivity.md)
- [IoT loop: sense at the edge, communicate over MQTT to a central store, compute and control](iot-sense-communicate-compute-control.md)
- [k6 load test showed the database connection pool, not the API, was the limit](load-test-reveals-database-connection-pool-bottleneck.md)
- [Law says whether you may collect, a framework says how to protect, a standard says what shape the data takes](regulation-vs-standard-roles-act-843-hipaa-fhir.md)
- [MapReduce is the batch-processing paradigm for when a design that works at 1,000 users meets millions](mapreduce-batch-processing-for-scale.md)
- [Out-of-band AWS changes (drift) can silently block terraform apply and stall deployments](configuration-drift-blocks-terraform-apply.md)
- [Prosit 3 shifts focus from running in the cloud to scaling to millions of users](prosit-3-focus-scaling-and-distributed-processing.md)
- [SNS fan-out to one SQS queue per consumer, batch size 1, dead-letter queue each](../learnings/sns-fanout-sqs-per-consumer-and-dlq.md)
- [Tests can pass for the wrong reason; test each rule separately and on real devices](tests-can-pass-for-the-wrong-reason.md)
- [Three ways to make synthetic data: LLM prompts with a schema, GANs, or distribution parameters](synthetic-data-for-testing-without-real-data.md)
- [Validate at front end, API and database; range limits catch impossible values](database-as-last-line-of-defense-range-checks.md)

## Related
- [Course facts (map)](map-course.md)
- [Labs 0–14 (map)](map-labs.md)
