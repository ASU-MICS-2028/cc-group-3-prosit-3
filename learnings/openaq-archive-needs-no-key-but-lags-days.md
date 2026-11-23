---
title: OpenAQ's v3 API needs a key, but its public S3 archive does not; the archive runs a few days behind
tags: [iot, data, ml]
source: issue #19 (evidence/lab12/19-*)
---

OpenAQ's v3 API answers `401 Unauthorized` without an `X-API-Key` header, and v2 is gone (`410`). The same data sits in a public S3 bucket, `openaq-data-archive`, with one gzipped CSV per station per day at `records/csv.gz/locationid=<id>/year=<yyyy>/month=<mm>/`. Listing it over plain HTTPS needs no key or AWS account. On 23 Nov 2026 the newest file for Madina Zongo Junction (location 3025587) was 19 Nov, so the archive is good for "a real day" but not for "right now".

The Accra station we used is a low-cost sensor that reports irregularly: 20 to 44 readings a day, about every 17 minutes when it does report. Code that expects one reading a minute needs to cope with gaps.

Against that day our simulator was too high and too noisy for November. Madina had a mean of 24.5 µg/m³ (sd 8.4); the simulator's five stations had means of 53 to 67 (sd 14). The simulator's harmattan ×1.8 starts on 1 Nov, and the harmattan usually arrives later. One station and one day is not enough to recalibrate, but it is a sign the knob is set too early.

## Related
- [Optional: feed 24 hours of real Accra PM2.5 from OpenAQ through the same MQTT pipeline](../knowledge/openaq-real-pm25-data-option.md)
- [Write every reading to a local spool first, so one path covers normal running and DB outages](bridge-writes-to-a-local-spool-first.md)
