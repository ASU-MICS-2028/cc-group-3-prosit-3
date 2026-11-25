# Lab 14 Part A: what-if replay of the flood warning line

Issue #45. Script [`api/what_if.py`](../api/what_if.py), output [`evidence/lab14/45-what-if-output.txt`](../evidence/lab14/45-what-if-output.txt), test `api/tests/test_what_if.py`.

**What we tried.** A small digital-twin test: try a policy change on recorded readings before changing the real system. The policy is the flood warning line. Today a warning opens at 60 cm and closes under 50 cm. We generated 30 days of drain readings with the simulator (seed 45): two gauges, 122,331 readings. We fed them, in time order, through the same `decide()` function the live alert checker runs, at the 60 cm line and at two lower lines, 50 and 40 cm.

**What happened.**

| Line | Warnings | Matched to a 60 cm warning | How much earlier | Extra | Hours under warning |
| --- | --- | --- | --- | --- | --- |
| 60 cm (today) | 129 | 129 | none | 0 | 103 |
| 50 cm | 153 | 128 | 6–10 min, mean 7 | 25 | 162 |
| 40 cm | 163 | 118 | 12–79 min, mean 16 | 45 | 271 |

- At 50 cm, warnings come about 7 minutes earlier, but there are 25 extra ones, for storms that never reached 60 cm. Time under warning rises by 57%.
- At 40 cm, warnings come 16 minutes earlier and there are 45 extra. Time under warning is 2.6 times today's.
- At 40 cm, the drain often doesn't fall back below 30 cm between storms, so one warning runs on through several storms. That causes the 79-minute maximum.
- The rising-fast alert already gives 7–23 minutes' notice (#25), with no extra warnings. **We keep 60 cm.**

**Limits.**
- The readings are simulated. Our storms come about every 7 hours per gauge, far more often than in real Accra.
- We have no record of real floods, so "extra" means "the water never reached 60 cm", not "a false alarm".
- The replay checks every reading, while the live checker runs every 30 seconds.

**What production would need.**
- A rainy season of real readings from each drain.
- AMA or NADMO records of which streets actually flooded, so each warning can be scored as a hit or a false alarm.
- A warning line set for each drain.
- This replay run automatically, as a CI check, whenever someone proposes a new line.
