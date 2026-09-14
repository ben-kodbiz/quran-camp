---
artifact:
  artifact_id: QURAN-COMEBACK-STORE-MANIFEST-001
  artifact_type: digital_store_asset_manifest
  artifact_version: 1.0.0
  project_id: HUURS-QURAN
  campaign_id: COME-BACK-TO-QURAN
  title: "Come Back to the Qur'an — Digital Storefront Master Asset Manifest & Checksums"
  description: "Technical inventory cataloging all downloadable digital files, formats, file sizes, local storage locations, and target distribution bundle mappings."
  topic: "Digital Supply Chain & Store Delivery Manifest"
  language: en-US
  audience: "Operations engineers, customer delivery bots, store managers"

provenance:
  parent_artifacts:
    - "file:///mnt/AI/ag/Campaign/Brand_Campaign.md"
    - "file:///mnt/AI/ag/Campaign/Artifact_Schema.md"

lifecycle:
  status: approved
  created_by: AGENT-19
  created_at: 2026-09-07T22:00:00Z
  updated_at: 2026-09-07T22:00:00Z

verification:
  verification_status: verified
  verified_by: AGENT-03
  qa_status: passed
  human_review_status: approved

storage:
  repository: huurs-studio
  path: 12_PRODUCTS/store/
  filename: STORE_ASSET_MANIFEST.md
---

# Digital Store Master Asset Manifest (`QURAN-COMEBACK-STORE-MANIFEST-001`)

**Campaign:** Come Back to the Qur'an  
**Cataloging Agent:** `AGENT-19` (Artifact Librarian)  
**Verification Date:** 2026-09-07  

---

## 1. Commercial Deliverables Inventory

| Asset Code | File Format | File Size | Primary Workspace Path | Deliverable Tier |
|---|---|---|---|---|
| `MASTER-EPUB` | `.epub` | 543 KB | `12_PRODUCTS/COME_BACK_TO_QURAN_114_SURAHS.epub` | Tier 2, Tier 3 |
| `MASTER-MD` | `.md` | 1,060 KB | `12_PRODUCTS/COME_BACK_TO_QURAN_114_SURAHS_MASTER.md` | Tier 2, Tier 3 |
| `JOURNAL-30D` | `.md` | 65 KB | `12_PRODUCTS/QURAN-COMEBACK-JOURNAL-30DAYS.md` | Tier 1, Tier 3 |
| `JOURNAL-30D-PRINT` | `.html` | 11 KB | `12_PRODUCTS/print/30day_journal_workbook_print.html` | Tier 1, Tier 3 |
| `GUIDE-7D` | `.md` | 15 KB | `12_PRODUCTS/QURAN-COMEBACK-GUIDE-001.md` | Tier 0, Tier 3 |
| `GUIDE-7D-PRINT` | `.html` | 20 KB | `12_PRODUCTS/print/7day_guided_journal_print.html` | Tier 0, Tier 3 |
| `STUDY-PORTAL` | `.html` | 523 KB | `12_PRODUCTS/reader.html` | Tier 3 (VIP) |
| `AUDIO-SUITE` | `.md` specs | 95 KB | `11_AUDIO/QURAN-COMEBACK-AUDIO-001.md` to `010.md` | Tier 3 (VIP) |
| `SCHEDULER-CSV` | `.csv` | 24 KB | `13_CAMPAIGNS/publishing_schedule_import.csv` | Internal Marketing |
| `SOCIAL-RENDERS` | 110 `.png` | ~45 MB | `14_SOCIAL/renders/` | Social Deployment |

---

## 2. Store Package Bundle Assembly Table

```text
PACKAGE 1: Free Lead Magnet (Tier 0)
  ├── 7day_guided_journal_print.html (Clean printable version)
  └── QURAN-COMEBACK-GUIDE-001.md (Plain text / markdown)

PACKAGE 2: 30-Day Journal Workbook (Tier 1)
  ├── 30day_journal_workbook_print.html (Print edition with habit tracker)
  ├── QURAN-COMEBACK-JOURNAL-30DAYS.md (Digital markdown)
  └── CUSTOMER_ONBOARDING_WORKFLOW.md (Setup guide)

PACKAGE 3: Master Digital Book Edition (Tier 2)
  ├── COME_BACK_TO_QURAN_114_SURAHS.epub (Official EPUB 3 for Kindle/Apple Books)
  ├── COME_BACK_TO_QURAN_114_SURAHS_MASTER.md (Full Obsidian/Notion markdown manuscript)
  └── CUSTOMER_ONBOARDING_WORKFLOW.md (Send-to-Kindle instructions)

PACKAGE 4: The Complete Master Ecosystem Bundle (Tier 3)
  ├── COME_BACK_TO_QURAN_114_SURAHS.epub
  ├── COME_BACK_TO_QURAN_114_SURAHS_MASTER.md
  ├── 30day_journal_workbook_print.html
  ├── 7day_guided_journal_print.html
  ├── reader.html (Standalone offline study portal & ambient sound player)
  ├── 11_AUDIO/ (Audio reflection guides)
  ├── COMMERCIAL_LICENSE_AND_TERMS.md
  └── CUSTOMER_ONBOARDING_WORKFLOW.md
```

---
