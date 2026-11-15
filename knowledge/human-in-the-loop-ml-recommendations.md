---
title: Keep a human approving high-stakes ML recommendations
tags: [ml, mlops, lecture]
source: Lecture 7
---

A Prosit 1 team used a hosted foundation model (via Amazon Bedrock) to analyse crop photos for disease. They deliberately did not let it act alone: the model produces a recommendation, and an extension officer must approve it before the farmer sees it.

Why it matters: model outputs can be wrong, and a person in the loop limits harm and builds trust. The same team admitted the automated image pipeline was partly manual and that image compression could slightly hurt model quality.

For SmartCity Accra: flood and waste alerts from ML forecasts could go to an operator for confirmation before triggering public notices.

## Related
- [Offline-first design for unreliable connectivity](offline-first-design-for-low-connectivity.md)
- [Reviewing technical papers and checking reproducibility](paper-review-and-reproducibility.md)
