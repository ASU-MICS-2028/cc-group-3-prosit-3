---
title: af-south-1 costs 29% more and emits about twice as much as us-east-1 for the same servers
tags: [sustainability, cost, aws]
source: PR for #13 (evidence/lab11/13-carbon-estimate.py)
---

For our stack (≈19 kWh a month by the Cloud Carbon Footprint method), Cape Town's grid (757 gCO2e/kWh) gives 14.5 kg CO2e a month against 7.0 kg in us-east-1 (365 g/kWh). A t4g.small costs $0.0217/h in af-south-1 against $0.0168/h in us-east-1. What we pay for is latency (74 ms from Ghana vs 175 ms) and keeping data in Africa.

Google publishes much cleaner options (Paris 16 g/kWh, 96% carbon-free), but Johannesburg is 641 g/kWh with 15% carbon-free, so changing provider doesn't fix a South African grid. Changing region does. Without leaving Africa, the lever is running less: scale to the minimum at night, schedule batch jobs, and tear things down.

## Related
- [Estimate carbon with the provider tool, or justify a lower-carbon region manually](../knowledge/region-carbon-intensity-sustainability-estimate.md)
- [AgroConnect picked af-south-1 by measuring latency from Ghana (74 ms median)](../knowledge/agroconnect-region-selection-by-latency.md)
- [fck-nat instance versus managed NAT Gateway: about $3 versus $32 a month](fck-nat-vs-nat-gateway.md)
