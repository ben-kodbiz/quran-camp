import os, sys, subprocess, shutil
sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign"
PRODUCTS_DIR = os.path.join(BASE_DIR, "12_PRODUCTS")
PREVIEWS_DIR = os.path.join(PRODUCTS_DIR, "previews")
os.makedirs(PREVIEWS_DIR, exist_ok=True)
brain_dir = "/home/ben/.gemini/antigravity/brain/1d535f8c-0b01-42ad-8e78-fc566134377c"

INTRO_PDF = "/tmp/fatihah_intro.pdf"
CONTENT_PDF = os.path.join(BASE_DIR, "07_MINDMAP/FATIHAH_MASTER_MINDMAP.pdf")
MASTER_COMPENDIUM_PDF = os.path.join(PRODUCTS_DIR, "SURAH_AL_FATIHAH_MASTER_COMPENDIUM.pdf")

# Palette
NAVY_DEEP = (0.024, 0.039, 0.071)
NAVY_CARD = (0.051, 0.078, 0.133)
NAVY_ELEVATED = (0.078, 0.118, 0.196)
GOLD = (0.831, 0.686, 0.353)
GOLD_LIGHT = (0.910, 0.820, 0.580)
CYAN = (0.220, 0.740, 0.970)
PURPLE = (0.659, 0.333, 0.969)
EMERALD = (0.063, 0.725, 0.506)
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
pdf.text("SURAH AL-FATIHAH", w/2 - 180, 345, font="F2", size=32, rgb=GOLD)
pdf.text("THE MASTER CARTOGRAPHY COMPENDIUM", w/2 - 195, 318, font="F2", size=16, rgb=WHITE)
pdf.line(120, 305, w - 120, 305, stroke_rgb=GOLD_LIGHT, line_width=1.0)

# Subtitle
pdf.text("The Definitive Visual Knowledge Architecture of the Mother of the Book (Umm al-Kitab)", w/2 - 255, 288, font="F1", size=10.5, rgb=TEXT_MUTED)

# Showcase Badges
box_w = 320
pdf.rect(w/2 - box_w - 15, 185, box_w, 75, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
pdf.text("THE DIVINE DIALOGUE (HADITH QUDSI)", w/2 - box_w - 5, 243, font="F2", size=9.5, rgb=CYAN)
pdf.text("THE HALVED PRAYER : SAHIH MUSLIM", w/2 - box_w - 5, 227, font="F2", size=11, rgb=WHITE)
pdf.text("Real-Time Divine Response to Every Recited Verse", w/2 - box_w - 5, 212, font="F1", size=8, rgb=TEXT_MUTED)
pdf.text("Transforming Monologue into Living Divine Encounter", w/2 - box_w - 5, 198, font="F3", size=7.5, rgb=GOLD_LIGHT)

pdf.rect(w/2 + 15, 185, box_w, 75, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
pdf.text("THE SEED OF ALL REVELATION", w/2 + 25, 243, font="F2", size=9.5, rgb=PURPLE)
pdf.text("CONCENTRIC RING COMPOSITION", w/2 + 25, 227, font="F2", size=11, rgb=WHITE)
pdf.text("7 Symmetrical Verses * 3 Praise * 1 Fulcrum * 3 Petition", w/2 + 25, 212, font="F1", size=8, rgb=TEXT_MUTED)
pdf.text("The Microcosm Answering the Call of Al-Baqarah", w/2 + 25, 198, font="F3", size=7.5, rgb=GOLD_LIGHT)

# Bottom Stats Ribbon
pdf.rect(48, 135, w - 96, 32, fill_rgb=NAVY_ELEVATED, stroke_rgb=BORDER_MUTED, line_width=0.8)
pdf.text("6 MASTER WIDESCREEN PLATES   *   8 THEMATIC PILLARS   *   32 VISUAL CARDS   *   100% VERIFIED", w/2 - 265, 149, font="F2", size=9.5, rgb=EMERALD)

# Footnote Metadata
pdf.text("ORTHODOX SUNNI ISLAMIC SOURCE DISCIPLINE", w/2 - 130, 85, font="F2", size=9, rgb=GOLD)
pdf.text("Tafsir Ibn Kathir  *  Jami' al-Bayan (Al-Tabari)  *  Al-Jami' li-Ahkam al-Qur'an (Al-Qurtubi)  *  Mafatih al-Ghayb (Al-Razi)", w/2 - 270, 70, font="F1", size=8, rgb=TEXT_MUTED)
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
pdf.text(" |  SURAH AL-FATIHAH MASTER COMPENDIUM", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
pdf.text("MASTER ARCHITECTURE & NAVIGATION", w - 240, h - 26, font="F2", size=9, rgb=GOLD)

pdf.text("TABLE OF CONTENTS & THEMATIC NAVIGATION", 32, h - 66, font="F2", size=12, rgb=WHITE)
pdf.text("A Structural Architectural Roadmap Across the Four Foundation Movements of Surah Al-Fatihah", 32, h - 79, font="F1", size=7.8, rgb=TEXT_MUTED)
pdf.text("[6 MASTER PLATES]", w - 140, h - 68, font="F2", size=10, rgb=GOLD)
pdf.line(32, h - 86, w - 32, h - 86, stroke_rgb=BORDER_MUTED, line_width=0.8)

# 2 Columns for TOC / Architecture Overview
c1_x, c2_x, c_w = 32, 412, 348

# Col 1: Plate Overview
pdf.rect(c1_x, 35, c_w, 345, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.0)
pdf.rect(c1_x, 345, c_w, 35, fill_rgb=NAVY_ELEVATED)
pdf.text("CONTENT PLATES & THEMATIC BREAKDOWN", c1_x + 12, 365, font="F2", size=9, rgb=CYAN)
pdf.text("Four Symmetrical Landscape Plates Across the Revelation", c1_x + 12, 352, font="F3", size=7.2, rgb=TEXT_MUTED)
pdf.line(c1_x, 345, c1_x + c_w, 345, stroke_rgb=CYAN, line_width=0.8)

toc_items = [
    ("Plate 01 : Master Compendium Cover Plate", "Plate 01"),
    ("Plate 02 : Table of Contents & Architecture Map", "Plate 02"),
    ("Plate 03 : The Celestial Prologue & Absolute Praise", "Plate 03"),
    ("Plate 04 : Oceans of Mercy & Sovereign Recompense", "Plate 04"),
    ("Plate 05 : The Central Covenant & Highway of Guidance", "Plate 05"),
    ("Plate 06 : The Three Destinies & Cosmic Ring Balance", "Plate 06"),
]

y_pos = 320
for title, plates in toc_items:
    pdf.text(title, c1_x + 12, y_pos, font="F2", size=8, rgb=WHITE)
    pdf.text(plates, c1_x + c_w - 65, y_pos, font="F2", size=8, rgb=GOLD_LIGHT)
    pdf.line(c1_x + 12, y_pos - 6, c1_x + c_w - 12, y_pos - 6, stroke_rgb=BORDER_MUTED, line_width=0.4)
    y_pos -= 42

# Col 2: Thematic Core & Ring Chiasmus
pdf.rect(c2_x, 35, c_w, 345, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.0)
pdf.rect(c2_x, 345, c_w, 35, fill_rgb=NAVY_ELEVATED)
pdf.text("THE CONCENTRIC RING ARCHITECTURE", c2_x + 12, 365, font="F2", size=9, rgb=PURPLE)
pdf.text("Symmetrical Balance Around the Central Covenant", c2_x + 12, 352, font="F3", size=7.2, rgb=TEXT_MUTED)
pdf.line(c2_x, 345, c2_x + c_w, 345, stroke_rgb=PURPLE, line_width=0.8)

chiasmus_items = [
    ("A. Transcendent Name & Dual Mercy", "Verse 1 (Basmalah)"),
    ("  B. Cosmic Lordship & Praise", "Verse 2 (Al-Hamd)"),
    ("    C. Maternal Compassion Re-iterated", "Verse 3 (Ar-Rahman)"),
    ("      D. Sovereign Accountability Court", "Verse 4 (Yawm ad-Deen)"),
    ("★ E. THE CENTER PIVOT: DUAL COVENANT", "Verse 5 (Iyyaka Na'budu)"),
    ("      D'. Sovereign Direction Requested", "Verse 6 (Ihdinas-Sirat)"),
    ("    C'. The Bestowed Grace of Favor", "Verse 7a (An'amta)"),
    ("  B'. Shielding from Earned Wrath", "Verse 7b (Maghdub)"),
    ("A'. Shielding from Lost Direction", "Verse 7c (Dallin)"),
]

y_pos = 325
for clause, verse_ref in chiasmus_items:
    is_pivot = "★" in clause
    c_rgb = GOLD if is_pivot else (WHITE if not clause.startswith(" ") else TEXT_MUTED)
    f_type = "F2" if is_pivot else "F1"
    pdf.text(clause, c2_x + 12, y_pos, font=f_type, size=7.2, rgb=c_rgb)
    pdf.text(verse_ref, c2_x + c_w - 95, y_pos, font="F2", size=6.8, rgb=GOLD_LIGHT if is_pivot else CYAN)
    pdf.line(c2_x + 12, y_pos - 4, c2_x + c_w - 12, y_pos - 4, stroke_rgb=BORDER_MUTED, line_width=0.4)
    y_pos -= 30

# Bottom Footer
pdf.line(32, 25, w - 32, 25, stroke_rgb=BORDER_MUTED, line_width=0.8)
pdf.text("HUURS KNOWLEDGE SYSTEMS  *  AUTHENTIC SUNNI SOURCE DISCIPLINE  *  READ. REFLECT. RETURN.", 32, 13, font="F1", size=7.2, rgb=TEXT_MUTED)
pdf.text("SURAH AL-FATIHAH FOUNDATION ARCHITECTURE", w - 245, 13, font="F2", size=7.2, rgb=GOLD)

# Save Intro PDF
pdf.save(INTRO_PDF)
print(f"Intro PDF generated at {INTRO_PDF}")

# Merge Intro + Content
cmd = f"pdfunite {INTRO_PDF} {CONTENT_PDF} {MASTER_COMPENDIUM_PDF}"
subprocess.run(cmd, shell=True, check=True)
print(f"Master Compendium PDF compiled successfully: {MASTER_COMPENDIUM_PDF}")

# Generate Previews
cmd_prev = f"pdftoppm -png -r 150 -f 1 -l 2 {MASTER_COMPENDIUM_PDF} {PREVIEWS_DIR}/fatihah_compendium_page"
subprocess.run(cmd_prev, shell=True, check=True)

# Copy to brain dir
cov_src = f"{PREVIEWS_DIR}/fatihah_compendium_page-1.png" if os.path.exists(f"{PREVIEWS_DIR}/fatihah_compendium_page-1.png") else f"{PREVIEWS_DIR}/fatihah_compendium_page-01.png"
toc_src = f"{PREVIEWS_DIR}/fatihah_compendium_page-2.png" if os.path.exists(f"{PREVIEWS_DIR}/fatihah_compendium_page-2.png") else f"{PREVIEWS_DIR}/fatihah_compendium_page-02.png"
shutil.copyfile(cov_src, os.path.join(brain_dir, "fatihah_compendium_cover.png"))
shutil.copyfile(toc_src, os.path.join(brain_dir, "fatihah_compendium_toc.png"))
shutil.copyfile(cov_src, f"{PREVIEWS_DIR}/fatihah_compendium_cover.png")
shutil.copyfile(toc_src, f"{PREVIEWS_DIR}/fatihah_compendium_toc.png")
print("Previews copied successfully.")
