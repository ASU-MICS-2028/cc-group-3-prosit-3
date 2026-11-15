---
title: Compromising one security goal often breaks the others
tags: [security, lecture]
source: Lecture 3
---

The goals are not standalone. Example from the lecture: a leaked password (confidentiality lost) lets an attacker change it, which locks you out (availability lost) and can allow altered data (integrity lost). Similarly, an integrity fault that takes a service down creates an availability problem, and that makes the system unreliable.

Reliability and dependability follow from security: if you cannot trust the system, you cannot rely on it. Some people argue authenticity or reliability fold into the main three; the lecturer's point was to classify each incident clearly and name the right countermeasure.

Exam tip given in class: do not just repeat the lecture examples, think of your own.

For SmartCity Accra: when designing threats, trace the chain, for example stolen API key to fake sensor data to wrong flood alert.

## Related
- [The CIA triad (confidentiality, integrity, availability) is the core of security](cia-triad.md)
- [The CIA triad extends to a five-goal pentad with authenticity and accountability](cia-pentad-five-security-goals.md)
