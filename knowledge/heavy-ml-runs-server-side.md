---
title: Heavy ML inference belongs on the server, not on low-end devices
tags: [lecture, ml, edge]
source: Lecture 6
---

Crop disease detection from photos is too heavy for basic phones, and image quality from low-end cameras is poor. Design: the device captures the image, the server runs the model. Pretrained models can be reused or fine-tuned instead of training from scratch, but you must understand what they do.

Typical ML workflow mentioned: exploratory data analysis first, then choose supervised or unsupervised methods, regression to predict.

For SmartCity Accra: edge devices send readings; forecasting runs in the cloud.

## Related
- [Get core features working before attempting advanced extras](core-features-before-advanced-features.md)
- [Offline-first design for unreliable connectivity](offline-first-design-for-low-connectivity.md)
