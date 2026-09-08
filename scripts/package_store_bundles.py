#!/usr/bin/env python3
"""
HUURS STUDIO - Commercial Store Bundle Packaging Engine
========================================================
Compiles and verifies the 4 standard customer delivery packages
for Gumroad and Lemon Squeezy digital storefronts with SHA-256
cryptographic checksums. Includes both printable HTML and PDF editions.

Packages:
1. PACKAGE 0: Free Lead Magnet (Tier 0)
2. PACKAGE 1: 30-Day Guided Journal Workbook (Tier 1)
3. PACKAGE 2: Master Digital Book Edition (Tier 2)
4. PACKAGE 3: Complete Master Ecosystem VIP (Tier 3)
"""

import os
import sys
import zipfile
import hashlib
import json
from datetime import datetime, timezone

ROOT_DIR = "/mnt/AI/ag/Campaign"
PRODUCTS_DIR = os.path.join(ROOT_DIR, "12_PRODUCTS")
BUNDLES_DIR = os.path.join(PRODUCTS_DIR, "bundles")
STORE_DIR = os.path.join(PRODUCTS_DIR, "store")

os.makedirs(BUNDLES_DIR, exist_ok=True)

PACKAGES = {
    "PACKAGE_0_FREE_LEAD_MAGNET": {
        "tier": "Tier 0 (Free Lead Magnet)",
        "price_usd": 0.0,
        "description": "7-Day Guided Contemplation Journal (PDF & HTML) & Onboarding Setup",
        "files": [
            ("12_PRODUCTS/QURAN-COMEBACK-GUIDE-001.md", "7_Days_Back_To_The_Quran_Guide.md"),
            ("12_PRODUCTS/print/7day_guided_journal_print.pdf", "7_Days_Back_To_The_Quran_Printable.pdf"),
            ("12_PRODUCTS/print/7day_guided_journal_print.html", "7_Days_Back_To_The_Quran_Printable.html"),
            ("12_PRODUCTS/store/CUSTOMER_ONBOARDING_WORKFLOW.md", "Getting_Started_Guide.md"),
            ("12_PRODUCTS/store/COMMERCIAL_LICENSE_AND_TERMS.md", "License_And_Terms.md")
        ]
    },
    "PACKAGE_1_30DAY_JOURNAL": {
        "tier": "Tier 1 (Guided Workbook Edition)",
        "price_usd": 9.0,
        "description": "30-Day Guided Workbook, Daily Habit Tracker, & Printable PDF/HTML Edition",
        "files": [
            ("12_PRODUCTS/QURAN-COMEBACK-JOURNAL-30DAYS.md", "30_Day_Quran_Journal_Workbook.md"),
            ("12_PRODUCTS/print/30day_journal_workbook_print.pdf", "30_Day_Quran_Journal_Printable.pdf"),
            ("12_PRODUCTS/print/30day_journal_workbook_print.html", "30_Day_Quran_Journal_Printable.html"),
            ("12_PRODUCTS/store/CUSTOMER_ONBOARDING_WORKFLOW.md", "Getting_Started_Guide.md"),
            ("12_PRODUCTS/store/COMMERCIAL_LICENSE_AND_TERMS.md", "License_And_Terms.md")
        ]
    },
    "PACKAGE_2_MASTER_EBOOK": {
        "tier": "Tier 2 (Core Digital Book)",
        "price_usd": 19.0,
        "description": "Official EPUB 3 Edition & Full Obsidian/Notion Markdown Manuscript",
        "files": [
            ("12_PRODUCTS/COME_BACK_TO_QURAN_114_SURAHS.epub", "Come_Back_To_The_Quran_114_Surahs.epub"),
            ("12_PRODUCTS/COME_BACK_TO_QURAN_114_SURAHS_MASTER.md", "Come_Back_To_The_Quran_Master_Manuscript.md"),
            ("12_PRODUCTS/store/CUSTOMER_ONBOARDING_WORKFLOW.md", "Send_To_Kindle_And_Reading_Guide.md"),
            ("12_PRODUCTS/store/COMMERCIAL_LICENSE_AND_TERMS.md", "License_And_Terms.md")
        ]
    },
    "PACKAGE_3_MASTER_ECOSYSTEM_VIP": {
        "tier": "Tier 3 (Complete Study Ecosystem VIP)",
        "price_usd": 47.0,
        "description": "The Complete Digital Suite: EPUB 3, Full Manuscript, Both PDF Journals, Standalone Web Reader, & Audio Guides",
        "files": [
            ("12_PRODUCTS/COME_BACK_TO_QURAN_114_SURAHS.epub", "Come_Back_To_The_Quran_114_Surahs.epub"),
            ("12_PRODUCTS/COME_BACK_TO_QURAN_114_SURAHS_MASTER.md", "Come_Back_To_The_Quran_Master_Manuscript.md"),
            ("12_PRODUCTS/QURAN-COMEBACK-JOURNAL-30DAYS.md", "30_Day_Quran_Journal_Workbook.md"),
            ("12_PRODUCTS/print/30day_journal_workbook_print.pdf", "30_Day_Quran_Journal_Printable.pdf"),
            ("12_PRODUCTS/print/30day_journal_workbook_print.html", "30_Day_Quran_Journal_Printable.html"),
            ("12_PRODUCTS/QURAN-COMEBACK-GUIDE-001.md", "7_Days_Back_To_The_Quran_Guide.md"),
            ("12_PRODUCTS/print/7day_guided_journal_print.pdf", "7_Days_Back_To_The_Quran_Printable.pdf"),
            ("12_PRODUCTS/print/7day_guided_journal_print.html", "7_Days_Back_To_The_Quran_Printable.html"),
            ("12_PRODUCTS/reader.html", "Interactive_Study_Portal_Offline_Reader.html"),
            ("12_PRODUCTS/store/CUSTOMER_ONBOARDING_WORKFLOW.md", "VIP_Ecosystem_Onboarding_Guide.md"),
            ("12_PRODUCTS/store/COMMERCIAL_LICENSE_AND_TERMS.md", "Commercial_License_And_Terms.md")
        ]
    }
}

def compute_sha256(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def package_all():
    manifest_data = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "store_platforms": ["Gumroad", "Lemon Squeezy"],
        "bundles": {}
    }

    print("===========================================================================")
    print("      HUURS STUDIO - PACKAGING COMMERCIAL STORE DELIVERABLE BUNDLES       ")
    print("===========================================================================\n")

    for pkg_name, pkg_info in PACKAGES.items():
        zip_filename = f"{pkg_name}.zip"
        zip_path = os.path.join(BUNDLES_DIR, zip_filename)
        
        print(f"📦 Packaging: {pkg_name} ({pkg_info['tier']})")
        
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
            package_files = []
            for rel_src, arc_name in pkg_info["files"]:
                abs_src = os.path.join(ROOT_DIR, rel_src)
                if not os.path.exists(abs_src):
                    print(f"   ⚠️ WARNING: Source missing: {rel_src}")
                    continue
                zf.write(abs_src, arc_name)
                fsize_kb = os.path.getsize(abs_src) / 1024
                package_files.append({"archive_name": arc_name, "source": rel_src, "size_kb": round(fsize_kb, 1)})
                print(f"   + Included: {arc_name} ({fsize_kb:.1f} KB)")
        
        zip_size_kb = os.path.getsize(zip_path) / 1024
        sha256_hash = compute_sha256(zip_path)
        
        manifest_data["bundles"][pkg_name] = {
            "tier": pkg_info["tier"],
            "price_usd": pkg_info["price_usd"],
            "filename": zip_filename,
            "size_kb": round(zip_size_kb, 1),
            "sha256": sha256_hash,
            "items_count": len(package_files),
            "files": package_files
        }
        
        print(f"   ✅ Saved: {zip_filename} ({zip_size_kb:.1f} KB) | SHA-256: {sha256_hash[:12]}...\n")

    manifest_path = os.path.join(BUNDLES_DIR, "MANIFEST_CHECKSUMS.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest_data, f, indent=2)
    
    print("===========================================================================")
    print(f"All 4 bundles packaged successfully into: {BUNDLES_DIR}")
    print(f"Cryptographic manifest written to: {manifest_path}")
    print("===========================================================================")

if __name__ == "__main__":
    package_all()
