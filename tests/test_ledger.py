import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from consent_ledger_validator import validate_ledger

class TestLedger(unittest.TestCase):
    def test_val(self):
        c = Path(__file__).resolve().parent.parent / "templates" / "consent-tracking-sheet.csv"
        self.assertGreaterEqual(validate_ledger(str(c)), 1)

if __name__ == "__main__":
    unittest.main()
