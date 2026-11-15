---
title: Structured, semi-structured and unstructured data need different stores
tags: [lecture, databases, storage]
source: Lecture 5; Lecture 6
---

- **Structured**: fixed schema (rows and columns), queried with SQL. Example from Lecture 6: farmer profile (name, phone, region, language).
- **Semi-structured**: files with loose structure such as JSON or logs.
- **Unstructured**: free-form content such as social media posts, images, video, voice notes.

Variety is one of the Vs of big data: users are not forced to submit text only, so systems need stores that accept other forms. A plain SQL database does not suit unstructured data; use object storage or a NoSQL store.

For SmartCity Accra: sensor readings (timestamp, device id, value) are structured and fit a time-series or SQL database; raw images or exported reports belong in object storage.

## Related
- [Choose SQL for fixed-schema data and NoSQL or object storage for flexible data, and justify it](sql-vs-nosql-choice.md)
- [Block, object and file storage serve different jobs](block-object-file-storage.md)
- [Big data is described by Volume, Velocity, Variety (and Veracity)](big-data-four-vs.md)
