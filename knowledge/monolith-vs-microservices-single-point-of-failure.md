---
title: Microservices avoid the single point of failure of a monolith
tags: [scaling, reliability, lecture]
source: Lecture 4
---

In a monolith, one broken module can take everything down. Splitting into microservices gives redundancy and isolates failures. The lecturer stressed this is an architecture decision made when you design, not after development. Modernizing an old project (deploy it, split it, get feedback) was suggested as an exercise.

Example context: the course's AgroConnect prosit moved from a monolith to microservices.

For SmartCity Accra: a failing forecasting service should not stop sensor ingestion.

## Related
- [Microservices let each part scale on its own](microservices-scale-independently.md)
- [Pick three to five microservices per team, with sensible boundaries](microservice-boundaries-three-to-five-per-team.md)
