# Customer UGC Rights Management & Consent Ledger System

> Safely turn customer social posts into high-converting paid ads. Standardized UGC consent request templates and license tracking ledger.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Format: TEMPLATE_FRAMEWORK](https://img.shields.io/badge/Format-TEMPLATE--FRAMEWORK-green.svg)](#)
[![Tier: 1](https://img.shields.io/badge/Tier-1-orange.svg)](#)
[![Region: MENA](https://img.shields.io/badge/Region-Egypt%20%7C%20GCC%20%7C%20Saudi-purple.svg)](#)
[![Tests: Passing](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](#)
[![Owner: mahmoudabdelnaby1](https://img.shields.io/badge/Owner-mahmoudabdelnaby1-blue.svg)](https://github.com/mahmoudabdelnaby1)

---

## 📌 Problem Statement & Target Persona

### Target Persona
**PRO** operating in high-growth e-commerce, digital publishing, and direct-response marketing across Saudi Arabia, UAE, and Egypt.

### Core Problem
Build an open-source customer UGC rights clearance system: 1) Standardized bilingual consent request copy for Instagram/TikTok comments and DMs, 2) CSV/Markdown rights tracking ledger schema (Asset URL, Creator Handle, Consent Timestamp, Usage Scope, Expiration Date), 3) Python audit script (`audit_rights.py`) warning of expiring usage licenses, 4) Takedown response protocol.

---

## 🛠️ Repository Architecture & Deliverables

This repository provides self-contained, documented implementations and specifications:

- `docs/gcc-privacy-ugc-law.md`
- `LICENSE`
- `playbooks/rights-clearance-sop.md`
- `README.md`
- `schemas/ugc_rights_ledger.csv`
- `src/audit_rights.py`
- `src/consent_ledger_validator.py`
- `templates/consent-request-copy-bilingual.md`
- `templates/consent-tracking-sheet.csv`
- `templates/ugc-rights-request-dms.md`
- `tests/test_audit.py`
- `tests/test_ledger.py`
- `tests/test_rights.py`


---

## 🚀 Quick Start & How to Run Locally

### Run Test Suite Locally
```bash
# Ensure no bytecode generation
export PYTHONDONTWRITEBYTECODE=1  # Linux / macOS
$env:PYTHONDONTWRITEBYTECODE="1"  # Windows PowerShell

# Run Python unittest discovery
python -m unittest discover -s tests
```

### Run CLI Script
```bash
python src/audit_rights.py --help
```

---

## 📊 Sample Input & Output Fixtures

> **Data Disclosure:** Any included sample data is illustrative and may be synthetic; it is not a measured customer result or market benchmark unless a source and collection method are stated alongside it. These files run offline with standard libraries and require no paid third-party API credentials.

```json
{
  "domain": "social",
  "repository": "customer-ugc-rights-consent-ledger",
  "status": "READY_FOR_LOCAL_REVIEW",
  "license": "MIT"
}
```

---

## ⚠️ Known Technical & Domain Constraints

- **Verifiable Consent Audit Trail:** Stores timestamped digital consent records connecting specific social media post URLs to marketing usage permissions.
- **Scope of Commercial Rights:** Documents exact permitted channels (Organic Social, Paid Ads, Website Hero, Email Newsletters) and license duration.
- **Saudi PDPL & GDPR Alignment:** Ensures user right-to-revoke consent is implemented with automated asset retirement workflows.

---

## 📚 Primary Documentation & Verifiable References

- [W3C Decentralized Identifiers (DIDs) & Verifiable Credentials](https://www.w3.org/TR/did-core/) - Standards for creating verifiable digital consent records.
- [Saudi Personal Data Protection Law (PDPL) - SDAIA](https://sdaia.gov.sa/) - Statutory rules governing the collection and commercial use of personal customer imagery.
- [GDPR Article 7: Conditions for Lawful Consent](https://gdpr-info.eu/art-7-gdpr/) - International legal standard for demonstrable and freely given marketing consent.

---


## 👤 Maintainer & License

- **Author & Maintainer:** [Mahmoud Abdelnaby](https://github.com/mahmoudabdelnaby1) (`@mahmoudabdelnaby1`)
- **License:** [MIT License](LICENSE) - Open-source, auditable, and freely adaptable for internal enterprise or commercial use.
