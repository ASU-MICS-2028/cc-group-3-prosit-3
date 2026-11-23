import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from devices import BRIDGE, acl_text  # noqa: E402


def rules(text):
    """ACL text -> {user: [rule, ...]}."""
    out, user = {}, None
    for line in text.splitlines():
        if line.startswith("user "):
            user = line.split(" ", 1)[1]
            out[user] = []
        elif line.startswith("topic "):
            out[user].append(line)
    return out


class AclTest(unittest.TestCase):
    def test_device_writes_only_its_own_topic(self):
        r = rules(acl_text([BRIDGE, "aq-nima-001", "wb-makola-002"]))
        self.assertEqual(r["aq-nima-001"], ["topic write accra/nima/air_quality/aq-nima-001"])
        self.assertEqual(r["wb-makola-002"], ["topic write accra/makola/waste/wb-makola-002"])

    def test_openaq_feeder_gets_its_own_topic(self):
        self.assertEqual(rules(acl_text(["aq-madina-001"]))["aq-madina-001"],
                         ["topic write accra/madina/air_quality/aq-madina-001"])

    def test_bridge_only_reads(self):
        self.assertEqual(rules(acl_text([BRIDGE]))[BRIDGE], ["topic read accra/#"])

    def test_revoked_or_unknown_users_get_nothing(self):
        r = rules(acl_text([BRIDGE, "aq-makola-001", "not-a-device"]))
        self.assertEqual(set(r), {BRIDGE, "aq-makola-001"})


if __name__ == "__main__":
    unittest.main()
