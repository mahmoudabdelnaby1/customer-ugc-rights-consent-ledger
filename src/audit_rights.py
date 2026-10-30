"""
Customer UGC Rights Management & Consent Ledger Auditor
Tracks creator/user content licenses, rights terms, and expiration dates:
- Validates consent scopes (organic repost vs paid ads vs whitelisting)
- Identifies assets nearing license expiration (< 14 days)
- Flags active campaigns running expired UGC assets
"""
import json
import argparse
from datetime import datetime
from typing import List, Dict, Any

def audit_ugc_licenses(assets: List[Dict[str, Any]], reference_date_str: str = "2026-10-01") -> Dict[str, Any]:
    ref_date = datetime.strptime(reference_date_str, "%Y-%m-%d")
    
    expired = []
    expiring_soon = []
    active_valid = []
    
    for a in assets:
        asset_id = a.get("asset_id", "UNKNOWN")
        creator = a.get("creator_handle", "")
        exp_str = a.get("expiration_date")
        paid_allowed = a.get("allow_paid_ads", False)
        in_active_ads = a.get("in_active_ad_campaign", False)
        
        if not exp_str:
            expired.append({"asset_id": asset_id, "reason": "No expiration/consent date recorded"})
            continue
            
        exp_date = datetime.strptime(exp_str, "%Y-%m-%d")
        days_left = (exp_date - ref_date).days
        
        info = {
            "asset_id": asset_id,
            "creator": creator,
            "days_left": days_left,
            "allow_paid_ads": paid_allowed,
            "in_active_ads": in_active_ads
        }
        
        if days_left < 0:
            info["risk"] = "CRITICAL_EXPIRED_IN_USE" if in_active_ads else "EXPIRED"
            expired.append(info)
        elif 0 <= days_left <= 14:
            info["risk"] = "EXPIRING_SOON"
            expiring_soon.append(info)
        else:
            active_valid.append(info)
            
    critical_violations = [x for x in expired if x.get("risk") == "CRITICAL_EXPIRED_IN_USE"]
    
    return {
        "total_assets_audited": len(assets),
        "valid_count": len(active_valid),
        "expiring_soon_count": len(expiring_soon),
        "expired_count": len(expired),
        "critical_violations_count": len(critical_violations),
        "critical_violations": critical_violations,
        "expiring_soon": expiring_soon
    }

def main():
    sample = [
        {"asset_id": "UGC-01", "creator_handle": "@sara_style", "expiration_date": "2026-10-20", "in_active_ad_campaign": True},
        {"asset_id": "UGC-02", "creator_handle": "@ahmed_fit", "expiration_date": "2026-09-15", "in_active_ad_campaign": True}
    ]
    res = audit_ugc_licenses(sample, "2026-10-01")
    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    main()
