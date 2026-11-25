import sys
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from what_if import compare, warnings  # noqa: E402

T0 = datetime(2026, 11, 1, tzinfo=timezone.utc)


def storm(peak, at_min=0):
    """A drain rising 2 cm a minute from 20 cm to `peak`, then falling 2 cm a minute back to 20."""
    up = list(range(20, peak + 1, 2))
    return [(T0 + timedelta(minutes=at_min + i), float(v)) for i, v in enumerate(up + up[::-1])]


class WhatIfTest(unittest.TestCase):
    def test_lower_line_warns_earlier_for_the_same_storm(self):
        readings = storm(80)
        base, low = warnings(readings, 60, 50), warnings(readings, 40, 30)
        self.assertEqual(len(base), 1)
        self.assertEqual(base[0][2], 80)                     # peak recorded
        self.assertEqual(compare(base, low), ([10.0], 0))    # 40 -> 60 cm at 2 cm/min = 10 min earlier

    def test_storm_below_todays_line_is_an_extra_warning(self):
        readings = storm(50)
        self.assertEqual(warnings(readings, 60, 50), [])
        self.assertEqual(compare([], warnings(readings, 40, 30)), ([], 1))


if __name__ == "__main__":
    unittest.main()
