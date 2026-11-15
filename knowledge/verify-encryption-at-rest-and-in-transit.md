---
title: Verify encryption at rest and TLS; do not assume defaults
tags: [security, storage, databases]
source: Lab 6 Part B and Troubleshooting
---

At rest: screenshot the DB encryption setting; aws s3api get-bucket-encryption and get-public-access-block. In transit: obtain a certificate (Let's Encrypt/Certbot or the load balancer's managed cert); curl -v http:// must refuse or 301/302 to https, and curl -v https:// must give a valid handshake and 200. Self-signed is fine only for local tests.

"The default probably handles it" is not evidence.

SmartCity Accra: apply TLS to MQTT as well as HTTP.

## Related
- [Least privilege - attach a scoped role and prove one allowed and one denied action](least-privilege-iam-prove-allow-and-deny.md)
- [Audit logging - record who did what to which record, and await the write](audit-log-who-what-when-await-the-write.md)
