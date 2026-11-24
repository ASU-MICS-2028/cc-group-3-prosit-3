import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from alerts import decide  # noqa: E402


class DecideTest(unittest.TestCase):
    def test_opens_a_warning_at_the_line_with_the_numbers_in_plain_words(self):
        self.assertEqual(decide(61.4, 58, []),
                         [("open", "flood_warning", "Drain level 61 cm, at or above the 60 cm warning line")])

    def test_no_second_warning_and_no_close_between_50_and_60(self):
        self.assertEqual(decide(70, 69, ["flood_warning"]), [])
        self.assertEqual(decide(55, 60, ["flood_warning"]), [])

    def test_closes_below_50(self):
        self.assertEqual(decide(49, 52, ["flood_warning"]), [("close", "flood_warning")])

    def test_fast_rise_opens_an_anomaly_and_settling_closes_it(self):
        self.assertEqual(decide(40, 22, []), [("open", "anomaly", "Drain level rose 18 cm in 15 minutes, now 40 cm")])
        self.assertEqual(decide(45, 38, ["anomaly"]), [])            # still rising 7 cm: stays open
        self.assertEqual(decide(45, 43, ["anomaly"]), [("close", "anomaly")])

    def test_no_history_is_not_a_rise(self):
        self.assertEqual(decide(30, None, []), [])


if __name__ == "__main__":
    unittest.main()
