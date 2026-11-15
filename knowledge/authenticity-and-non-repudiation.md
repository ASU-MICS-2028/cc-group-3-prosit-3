---
title: Authenticity means the sender and data are genuine, which gives non-repudiation
tags: [security, lecture]
source: Lecture 3
---

Authenticity is verifying the origin and validity of data and communication, and that users are genuine and not impersonators. Non-repudiation means a sender cannot deny having sent something ("repudiation" means denial). If authenticity is assured, the sender cannot deny it, so authenticity provides non-repudiation.

The lecture's analogy: a bank compares your signature with the one on file; a digital signature is stronger because it is computed from the document and attached to it, so denial is not plausible (unless the account itself was taken over).

Authenticity can be seen as related to confidentiality (checking that the person is really the authorized one) and to integrity (the sender's identity), which is why it is listed as an added goal.

For SmartCity Accra: the broker should know a message really came from a registered sensor, not an impostor.

## Related
- [The CIA triad extends to a five-goal pentad with authenticity and accountability](cia-pentad-five-security-goals.md)
- [Integrity is protected with checksums, hashing and digital signatures](integrity-techniques-checksum-hash-signature.md)
- [Accountability means every action can be traced to a user, through system logs](accountability-and-system-logs.md)
