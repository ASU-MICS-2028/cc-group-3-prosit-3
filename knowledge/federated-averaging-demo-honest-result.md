---
title: Averaging two parties model weights may lose to a local model, and that is a legitimate result
tags: [lab, ml, privacy]
source: Lab 14 (week14_lab_Students) Part A Option 3 and Troubleshooting
---

Option 3: split the data into two parties (e.g. two neighbourhoods), fit a linear regression on hour for each, average coefficients and intercepts (raw data never combined), and compare MAE of A, B and federated on the full set. The lab says a two-party, one-round demo losing to a local model is expected: real federated learning needs many parties and rounds. Document it honestly.

## Related
- [If the model does not beat the baseline, report it and explain why; do not fabricate](honest-reporting-model-loses-to-baseline.md)
- [Lab 14 overview: advanced feature test, capstone integration, final architecture doc, presentation](lab-14-advanced-feature-capstone-final-presentation.md)
