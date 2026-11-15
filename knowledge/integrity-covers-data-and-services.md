---
title: Integrity covers data, services and systems, and applies to automated processes too
tags: [security, lecture]
source: Lecture 3
---

Integrity means data stays accurate, complete and unaltered except by authorized people or processes. "Authorized process" matters: a script or software component that updates records automatically must also be authorized, and an unauthorized change by a process is still an integrity breach.

Integrity is wider than data. A corrupted or malfunctioning service, or damaged hardware, is also an integrity problem; if one small component of a multi-service system is spoiled, the whole system loses integrity. The lecture separated data integrity, service integrity and system integrity.

Example from the lecture: a 500 transfer must debit 500 from one account and credit 500 to the other; receiving 5000 instead is an integrity failure. Students' exam scores should be changeable only by the instructor.

For SmartCity Accra: a tampered PM2.5 reading or a faulty ingestion service would produce wrong forecasts and wrong alerts.

## Related
- [Integrity is protected with checksums, hashing and digital signatures](integrity-techniques-checksum-hash-signature.md)
- [The CIA triad (confidentiality, integrity, availability) is the core of security](cia-triad.md)
- [Compromising one security goal often breaks the others](security-goals-are-interlinked.md)
