---
title: Choose SQL for fixed-schema data and NoSQL or object storage for flexible data, and justify it
tags: [lecture, databases]
source: Lecture 6
---

The course asks you to justify the data model, not just pick one. Farmer profile data (name, phone, region, language, farm details) is fairly structured and relational, so a SQL database such as PostgreSQL fits; the lecturer recommended it as open source and free. Unstructured items (photos, audio) go elsewhere.

Questions to ask: is the schema fixed? Do you need joins and transactions? What is the form of each kind of data?

For SmartCity Accra: sensor readings have a fixed shape but arrive in time order, which is why a time-series database is the natural choice; city metadata (sites, device registry) is relational.

## Related
- [Structured, semi-structured and unstructured data need different stores](structured-semi-structured-unstructured-data.md)
- [Block, object and file storage serve different jobs](block-object-file-storage.md)
