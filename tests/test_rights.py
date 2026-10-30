"""
Unit tests for UGC Rights Auditor
"""
import unittest
from src.audit_rights import audit_ugc_licenses

class TestUGCRights(unittest.TestCase):
    def test_critical_expired_violation(self):
        assets = [
            {"asset_id": "A1", "creator_handle": "@user", "expiration_date": "2026-08-01", "in_active_ad_campaign": True}
        ]
        res = audit_ugc_licenses(assets, "2026-10-01")
        self.assertEqual(res["critical_violations_count"], 1)

if __name__ == "__main__":
    unittest.main()
