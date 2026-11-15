---
title: Pick three to five microservices per team, with sensible boundaries
tags: [scaling, process, lecture]
source: Lecture 4
---

Rule of thumb from the lecture: three to five services maximum per team; enough to show the pattern, not so many that you burn the semester and cloud credits. For AgroConnect the proposed boundaries were registration, farm details (CRUD against the database), and an SMS/USSD gateway (a feature-phone access layer) plus multilingual content.

Class discussion on whether SMS/USSD and farmer profile should be one service: arguments for separate included that USSD handles more than profile tasks and cannot carry images or map locations, and that a gateway should be an access layer, not merged with other services. Team size and time change the answer: a 20-person team with a year could split further.

## Related
- [Microservices let each part scale on its own](microservices-scale-independently.md)
- [Microservices avoid the single point of failure of a monolith](monolith-vs-microservices-single-point-of-failure.md)
