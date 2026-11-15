---
title: AgroConnect picked af-south-1 by measuring latency from Ghana (74 ms median)
tags: [prosit-1, aws, networking]
source: Prosit 1 docs/architecture-decisions.md ADR-001; Prosit 1 docs/empirical-research.md; Lecture 7
---

The team measured TCP connect time and HTTP request round trip from Ghana to health endpoints in many regions. Median request RTT: AWS af-south-1 (Cape Town) 74 ms; eu-south-2 112; AWS eu-west-2 117; Azure uksouth 116; GCP europe-west9 127; Azure southafricanorth 129; AWS eu-west-1 134; us-east-1 175; Azure eastus 192. Cape Town was about 36% faster than Europe.

Consequences recorded: data stays on the continent; inter-region transfer is charged and af-south-1 prices some services slightly above us-east-1. African providers (MainOne, Rack Centre) were considered qualitatively (strong at colocation and private cloud) but not measured; AWS won on managed-service breadth.

The static app is served from edge locations (including Lagos) so cached files cost no region hop. There is no region in Ghana, so health data in Cape Town crosses a border, which the residency write-up for Prosit 2 had to state.

SmartCity: repeat the method (measure from Accra) if a design considers an edge or another region, and note that IoT devices add their own link latency.

**Also (Lecture 7):** One Prosit 1 team tested latency from users to regions across three providers (AWS, Azure and GCP) before deciding where to host. AWS af-south-1 (Cape Town) gave the lowest latency, and they chose it because their users had weak connections.

Takeaway: show a measured comparison rather than assuming a region. The same brief for Prosit 3 names af-south-1, so measured latency from Accra to it, and to the nearest alternative, is useful evidence for the design.

## Related
- [AgroConnect AWS infrastructure inventory: network, compute, data, security, observability, cost](agroconnect-aws-infrastructure-inventory.md)
- [HealthConnect treats Ghana's Act 843 as the law and HIPAA only as a safeguards checklist](healthconnect-act-843-and-hipaa-stance.md)
- [Geography-aware networking and CDNs](geography-aware-networking-and-cdns.md)
- [Offline-first design for unreliable connectivity](offline-first-design-for-low-connectivity.md)
