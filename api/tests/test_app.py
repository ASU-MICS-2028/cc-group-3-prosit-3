import json
import sys
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app import HttpError, check_report, forecast  # noqa: E402

T0 = datetime(2026, 11, 23, tzinfo=timezone.utc)


class ForecastTest(unittest.TestCase):
    def test_repeats_the_same_hour_a_day_earlier(self):
        hourly = {T0 + timedelta(hours=h): float(h) for h in range(48)}  # last hour is T0+47h
        points = forecast(hourly, 24)
        self.assertEqual(len(points), 24)
        self.assertEqual(points[0], (T0 + timedelta(hours=48), 24.0))  # same hour yesterday
        self.assertEqual(points[-1], (T0 + timedelta(hours=71), 47.0))

    def test_48h_uses_two_days_back_then_falls_back_to_latest(self):
        hourly = {T0 + timedelta(hours=h): float(h) for h in range(30)}  # 30 h of history, last T0+29h
        points = dict(forecast(hourly, 48))
        self.assertEqual(points[T0 + timedelta(hours=30)], 6.0)    # 1 day back
        self.assertEqual(points[T0 + timedelta(hours=60)], 12.0)   # 2 days back
        self.assertEqual(points[T0 + timedelta(hours=77)], 29.0)   # nothing that far back: latest


class ReportTest(unittest.TestCase):
    good = {"category": "flooding", "description": "Drain blocked", "lat": 5.55, "lon": -0.21}

    def test_valid_report_passes(self):
        self.assertEqual(check_report(json.dumps(self.good)), self.good)

    def test_rejects_bad_reports(self):
        for bad in ["not json", {**self.good, "lat": 200}, {**self.good, "phone": "024..."},
                    {k: v for k, v in self.good.items() if k != "category"}]:
            with self.subTest(bad=bad), self.assertRaises(HttpError) as e:
                check_report(bad if isinstance(bad, str) else json.dumps(bad))
            self.assertEqual(e.exception.status, 400)


if __name__ == "__main__":
    unittest.main()
