#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Ahzab Product Package Compiler
Produces:
1. 10-Plate Master Compendium PDF (Cover + TOC + 8 Content Plates)
2. PNG Previews for Cover & TOC
3. Copies to brain directory for visual verification
"""

import os, sys, subprocess, shutil
sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign"
PRODUCTS_DIR = os.path.join(BASE_DIR, "12_PRODUCTS")
PREVIEWS_DIR = os.path.join(PRODUCTS_DIR, "previews")
os.makedirs(PREVIEWS_DIR, exist_ok=True)
brain_dir = "/home/ben/.gemini/antigravity/brain/1d535f8c-0b01-42ad-8e78-fc566134377c"

INTRO_PDF = "/tmp/al_ahzab_intro.pdf"
CONTENT_PDF = os.path.join(BASE_DIR, "07_MINDMAP/AL_AHZAB_MASTER_MINDMAP.pdf")
MASTER_COMPENDIUM_PDF = os.path.join(PRODUCTS_DIR, "SURAH_AL_AHZAB_MASTER_COMPENDIUM.pdf")

# Palette (Strict Brand_Visual_System.md)
NAVY_DEEP = (0.024, 0.039, 0.071)
NAVY_CARD = (0.051, 0.078, 0.133)
NAVY_ELEVATED = (0.078, 0.118, 0.196)
GOLD = (0.831, 0.686, 0.353)
GOLD_LIGHT = (0.910, 0.820, 0.580)
CYAN = (0.220, 0.740, 0.970)
PURPLE = (0.659, 0.333, 0.969)
EMERALD = (0.063, 0.725, 0.506)
ROSE = (0.920, 0.350, 0.450)
WHITE = (0.973, 0.980, 0.988)
TEXT_MUTED = (0.680, 0.730, 0.800)
BORDER_MUTED = (0.160, 0.220, 0.310)

w, h = 792, 480
pdf = PDFDocument(page_width=w, page_height=h)

# ==========================================
# PAGE 1: MASTER PRODUCT COVER
# ==========================================
pdf.new_page(w, h)

# Background & Frames
pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)
pdf.rect(16, 16, w - 32, h - 32, stroke_rgb=BORDER_MUTED, line_width=1.0)
pdf.rect(20, 20, w - 40, h - 40, stroke_rgb=GOLD, line_width=0.8)

# Top Bar Brand Badge
pdf.rect(w/2 - 140, h - 52, 280, 26, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.0)
pdf.text("HUURS STUDIO", w/2 - 120, h - 35, font="F2", size=11, rgb=GOLD)
pdf.text(" |  DEEPER THOUGHT CAMPAIGN", w/2 - 25, h - 35, font="F1", size=9, rgb=WHITE)

# Central Emblem / Title Box
pdf.rect(48, 115, w - 96, 280, fill_rgb=NAVY_CARD, stroke_rgb=BORDER_MUTED, line_width=1.2)
pdf.rect(52, 119, w - 104, 272, stroke_rgb=GOLD, line_width=0.5)

# Golden Title Header
pdf.text("THE DEEPER THOUGHT SERIES  *  MASTER CARTOGRAPHY", w/2 - 170, 360, font="F2", size=9.5, rgb=GOLD)
pdf.text("SURAH AL-AHZAB", w/2 - 130, 325, font="F2", size=26, rgb=WHITE)
pdf.text("THE SIEGE OF THE TRENCH: THE PROPHETIC PARAGON & THE COSMIC TRUST", w/2 - 280, 305, font="F2", size=9.8, rgb=GOLD_LIGHT)
pdf.text("The Definitive Visual Knowledge Architecture of The Two Hearts Metaphor, The 10,000 Confederate Coalition Siege (Ghazwat al-Khandaq), Uswatun Hasanah, The Freezing Gale, Ayat al-Takhyir, The Spiritual Decalogue (Ayah 35), Khatam an-Nabiyyeen, Ayat al-Jilbab & The Cosmic Amanah", w/2 - 380, 288, font="F1", size=7.1, rgb=TEXT_MUTED)

# Showcase Badges
box_w = 320
pdf.rect(w/2 - box_w - 15, 185, box_w, 75, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
pdf.text("THE CRUCIBLE OF THE TRENCH", w/2 - box_w - 5, 243, font="F2", size=9.5, rgb=CYAN)
pdf.text("USWATUN HASANAH & REEH SARSAR", w/2 - box_w - 5, 227, font="F2", size=10.5, rgb=WHITE)
pdf.text("Hearts at Throats, Anas b. Nadr, Freezing Gale", w/2 - box_w - 5, 212, font="F1", size=8, rgb=TEXT_MUTED)
pdf.text("Invisible Hosts & Routing of the 10,000 Coalition", w/2 - box_w - 5, 198, font="F3", size=7.5, rgb=GOLD_LIGHT)

pdf.rect(w/2 + 15, 185, box_w, 75, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
pdf.text("THE HOUSEHOLD & THE COSMIC TRUST", w/2 + 25, 243, font="F2", size=9.5, rgb=GOLD)
pdf.text("KHATAM AN-NABIYYEEN & AL-AMANAH", w/2 + 25, 227, font="F2", size=10.5, rgb=WHITE)
pdf.text("Ayat al-Takhyir, Tatheer, Spiritual Decalogue", w/2 + 25, 212, font="F1", size=8, rgb=TEXT_MUTED)
pdf.text("Salat 'ala an-Nabi, Jilbab & Shuddering Mountains", w/2 + 25, 198, font="F3", size=7.5, rgb=GOLD_LIGHT)

# Bottom Stats Ribbon
pdf.rect(48, 135, w - 96, 32, fill_rgb=NAVY_ELEVATED, stroke_rgb=BORDER_MUTED, line_width=0.8)
pdf.text("10 MASTER WIDESCREEN PLATES   *   16 THEMATIC PILLARS   *   64 VISUAL CARDS   *   100% VERIFIED", w/2 - 275, 149, font="F2", size=9.5, rgb=EMERALD)

# Footnote Metadata
pdf.text("ORTHODOX SUNNI ISLAMIC SOURCE DISCIPLINE", w/2 - 130, 85, font="F2", size=9, rgb=GOLD)
pdf.text("Tafsir al-Tabari  *  Tafsir Ibn Kathir  *  Tafsir al-Qurtubi  *  Mafatih al-Ghayb (Al-Razi)  *  Al-Baghawi", w/2 - 245, 70, font="F1", size=8, rgb=TEXT_MUTED)
pdf.text("READ. REFLECT. RETURN.", w/2 - 68, 45, font="F2", size=10.5, rgb=GOLD_LIGHT)

# ==========================================
# PAGE 2: TABLE OF CONTENTS & NAVIGATION
# ==========================================
pdf.new_page(w, h)

# Chrome
pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)
pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
pdf.text(" |  SURAH AL-AHZAB MASTER COMPENDIUM", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
pdf.text("MASTER ARCHITECTURE & NAVIGATION", w - 240, h - 26, font="F2", size=9, rgb=GOLD)

pdf.text("TABLE OF CONTENTS & THEMATIC NAVIGATION", 32, h - 66, font="F2", size=12, rgb=WHITE)
pdf.text("The 8 Content Plates Mapped Across 16 Pillars, 64 Structural Cards and 100% Verified Classical Sunni Exegesis", 32, h - 79, font="F1", size=7.8, rgb=TEXT_MUTED)
badge_str = "[10 MASTER PLATES]"
badge_w = len(badge_str) * 6.1
pdf.text(badge_str, (w - 32) - badge_w, h - 68, font="F2", size=10, rgb=GOLD)
pdf.line(32, h - 86, w - 32, h - 86, stroke_rgb=BORDER_MUTED, line_width=0.8)

# 2 Columns for TOC
c1_x, c2_x, c_w = 32, 412, 348

# Col 1: Plates 1 to 4
pdf.rect(c1_x, 35, c_w, 345, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.0)
pdf.rect(c1_x, 345, c_w, 35, fill_rgb=NAVY_ELEVATED)
pdf.text("HEART INTEGRITY, THE SIEGE & PARAGON", c1_x + 12, 365, font="F2", size=8.8, rgb=CYAN)
pdf.text("Plates 01 to 04: Two Hearts, Trench Crucible, Uswah Hasanah & Divine Gale", c1_x + 12, 352, font="F3", size=7.2, rgb=TEXT_MUTED)
pdf.line(c1_x, 345, c1_x + c_w, 345, stroke_rgb=CYAN, line_width=0.8)

col1_items = [
    ("Plate 01 : Master Compendium Cover Plate", "Plate 01", "Deluxe institutional presentation and thematic summary"),
    ("Plate 02 : Table of Contents & Navigation Map", "Plate 02", "Structural architectural roadmap and plate index"),
    ("Plate 03 : Heart Integrity & Adoption Abolition", "Plate 03", "Two Hearts, Zihar, Ud'oohum li-Aba'ihim & Prophetic Primacy"),
    ("Plate 04 : Crucible of the Trench (Siege of 10k)", "Plate 04", "10,000 Coalition, Hearts at Throats & Hypocrisy Unmasked"),
    ("Plate 05 : Uswatun Hasanah & Men of Covenant", "Plate 05", "The Prophetic Paragon, Anas ibn al-Nadr & Unyielding Resolve"),
    ("Plate 06 : The Freezing Gale & Invisible Hosts", "Plate 06", "Reeh Sarsar, Angelic Legions, Overturned Tents & Coalition Rout")
]

y_pos = 320
for title, p_num, sub in col1_items:
    pdf.text(title, c1_x + 12, y_pos, font="F2", size=7.8, rgb=WHITE)
    pdf.text(p_num, c1_x + c_w - 60, y_pos, font="F2", size=7.8, rgb=CYAN)
    pdf.text(sub, c1_x + 12, y_pos - 10, font="F1", size=6.5, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, y_pos - 15, c1_x + c_w - 12, y_pos - 15, stroke_rgb=BORDER_MUTED, line_width=0.4)
    y_pos -= 44

# Col 2: Plates 5 to 8
pdf.rect(c2_x, 35, c_w, 345, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.0)
pdf.rect(c2_x, 345, c_w, 35, fill_rgb=NAVY_ELEVATED)
pdf.text("HOUSEHOLD, KHATAM & THE COSMIC TRUST", c2_x + 12, 365, font="F2", size=8.8, rgb=GOLD)
pdf.text("Plates 05 to 08: Mothers of Believers, Parity Decalogue, Khatam & Amanah", c2_x + 12, 352, font="F3", size=7.2, rgb=TEXT_MUTED)
pdf.line(c2_x, 345, c2_x + c_w, 345, stroke_rgb=GOLD, line_width=0.8)

col2_items = [
    ("Plate 07 : Mothers of Believers & Tatheer", "Plate 07", "Ayat al-Takhyir, Speech Decorum, Wa Qarna & Complete Purification"),
    ("Plate 08 : Decalogue of Parity & Divine Decree", "Plate 08", "Ten Paired Virtues, No Choice Against Decree & Zaynab's Marriage"),
    ("Plate 09 : Seal of Prophets & Radiant Beacon", "Plate 09", "Khatam an-Nabiyyeen, Sirajan Muneera & Abundant Remembrance"),
    ("Plate 10 : Salat upon Prophet & Cosmic Trust", "Plate 10", "Salat 'ala an-Nabi, Ayat al-Jilbab, Shuddering Mountains & Amanah"),
    ("Core Architecture : 16 Thematic Pillars", "64 Cards", "Complete Sunni Exegetical Synthesis • 100% Tier-1 Certified"),
    ("Theological Standard : Mutawatir & Classical Sunni", "Tier-1", "Tafsir al-Tabari, Ibn Kathir, Al-Qurtubi, Al-Razi, Al-Baghawi")
]

y_pos = 320
for title, p_num, sub in col2_items:
    pdf.text(title, c2_x + 12, y_pos, font="F2", size=7.8, rgb=WHITE)
    pdf.text(p_num, c2_x + c_w - 60, y_pos, font="F2", size=7.8, rgb=GOLD_LIGHT)
    pdf.text(sub, c2_x + 12, y_pos - 10, font="F1", size=6.5, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, y_pos - 15, c2_x + c_w - 12, y_pos - 15, stroke_rgb=BORDER_MUTED, line_width=0.4)
    y_pos -= 44

# Bottom Footer
pdf.line(32, 25, w - 32, 25, stroke_rgb=BORDER_MUTED, line_width=0.8)
pdf.text("HUURS KNOWLEDGE SYSTEMS  *  AUTHENTIC SUNNI SOURCE DISCIPLINE  *  READ. REFLECT. RETURN.", 32, 13, font="F1", size=7.2, rgb=TEXT_MUTED)
pdf.text("SURAH AL-AHZAB FOUNDATION ARCHITECTURE", w - 240, 13, font="F2", size=7.2, rgb=GOLD)

# Save Intro PDF
pdf.save(INTRO_PDF)
print(f"Intro PDF generated at {INTRO_PDF}")

# Merge Intro + Content
cmd = f"pdfunite {INTRO_PDF} {CONTENT_PDF} {MASTER_COMPENDIUM_PDF}"
subprocess.run(cmd, shell=True, check=True)
print(f"Master Compendium PDF compiled successfully: {MASTER_COMPENDIUM_PDF}")

# Generate Previews
cmd_prev = f"pdftoppm -png -r 150 -f 1 -l 2 {MASTER_COMPENDIUM_PDF} {PREVIEWS_DIR}/al_ahzab_compendium_page"
subprocess.run(cmd_prev, shell=True, check=True)

# Copy to brain dir
shutil.copyfile(f"{PREVIEWS_DIR}/al_ahzab_compendium_page-01.png", os.path.join(brain_dir, "al_ahzab_compendium_cover.png"))
shutil.copyfile(f"{PREVIEWS_DIR}/al_ahzab_compendium_page-02.png", os.path.join(brain_dir, "al_ahzab_compendium_toc.png"))
print(f"Copied cover and TOC previews to {brain_dir}")
