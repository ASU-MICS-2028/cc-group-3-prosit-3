---
title: Block, object and file storage serve different jobs
tags: [lecture, storage, cloud-basics]
source: Lecture 6
---

- **Block**: fixed-size low-level blocks attached to a VM. AWS EBS, Azure Managed Disks, GCP Persistent Disk. Best for database volumes and VM boot disks.
- **Object**: whole objects plus metadata, accessed over an HTTP API. AWS S3. Best for photos, audio, backups and other large unstructured files.
- **File**: shared POSIX-like file system many machines mount. AWS EFS, Azure Files, GCP Filestore. Best for shared configuration or legacy apps needing a real file system.

Course project example: farm photos, crop disease images and multilingual audio go to object storage; the VM's own disk is block storage; shared file storage is almost never needed.

For SmartCity Accra: the time-series database volume is block; archived raw data and model artefacts are object (S3); shared file storage is rarely required.

## Related
- [Structured, semi-structured and unstructured data need different stores](structured-semi-structured-unstructured-data.md)
- [Lab 4 - managed Postgres, private object storage and an offline-capable PWA](lab-4-managed-database-storage-offline-pwa.md)
