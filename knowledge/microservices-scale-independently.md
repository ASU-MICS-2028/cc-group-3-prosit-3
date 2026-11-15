---
title: Microservices let each part scale on its own
tags: [scaling, lecture]
source: Lecture 4
---

In a tightly integrated monolith you must scale everything to scale one module. With microservices you scale only the busy one. Lecture example: in AgroConnect, farmer registration (about 15,000 farmers) spikes only in a planting-season peak, while the SMS/USSD gateway has a different load, so they should scale separately and not hog resources together.

For SmartCity Accra: the MQTT ingestion path may need many instances during a storm while the reporting API stays small.

## Related
- [Microservices avoid the single point of failure of a monolith](monolith-vs-microservices-single-point-of-failure.md)
- [Pick three to five microservices per team, with sensible boundaries](microservice-boundaries-three-to-five-per-team.md)
