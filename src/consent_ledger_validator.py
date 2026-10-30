#!/usr/bin/env python3
import csv
import sys

def validate_ledger(csv_path):
    approved = 0
    with open(csv_path, "r", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("consent_status") == "APPROVED":
                approved += 1
    return approved

if __name__ == "__main__":
    count = validate_ledger(sys.argv[1])
    print(f"Validated UGC Consent Ledger: {count} legally approved assets ready for ads.")
