---
title: Integrity is protected with checksums, hashing and digital signatures
tags: [security, lecture]
source: Lecture 3
---

The lecture named three ways to detect or prevent unauthorized change:

- Checksum: a simple check on transmitted data, such as counting bits; if you expect a 64-bit stream and receive fewer, something dropped. It is useful but not a complete solution.
- Hashing: a hash function changes completely if even one bit changes, so it detects tampering far better than a plain checksum.
- Digital signatures: a value computed from the digital document and attached to it; they also give non-repudiation. The lecturer said these come later in the course.

Access control (who may write) complements these by stopping changes in the first place.

For SmartCity Accra: sensor messages could carry a checksum or signature so the broker or pipeline can reject altered readings.

## Related
- [Integrity covers data, services and systems, and applies to automated processes too](integrity-covers-data-and-services.md)
- [Authenticity means the sender and data are genuine, which gives non-repudiation](authenticity-and-non-repudiation.md)
