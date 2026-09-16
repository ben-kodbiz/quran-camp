import os, sys, subprocess, shutil
sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign"
PRODUCTS_DIR = os.path.join(BASE_DIR, "12_PRODUCTS")
os.makedirs(PRODUCTS_DIR, exist_ok=True)
previews_dir = os.path.join(PRODUCTS_DIR, "previews")
os.makedirs(previews_dir, exist_ok=True)

brain_dir = "/home/ben/.gemini/antigravity/brain/1d535f8c-0b01-42ad-8e78-fc566134377c"

INTRO_PDF = "/tmp/baqarah_intro.pdf"
MASTER_COMPENDIUM_PDF = os.path.join(PRODUCTS_DIR, "SURAH_AL_BAQARAH_MASTER_COMPENDIUM.pdf")

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
pdf.text("SURAH AL-BAQARAH", w/2 - 185, 345, font="F2", size=32, rgb=GOLD)
pdf.text("THE MASTER CARTOGRAPHY COMPENDIUM", w/2 - 195, 318, font="F2", size=16, rgb=WHITE)
pdf.line(120, 305, w - 120, 305, stroke_rgb=GOLD_LIGHT, line_width=1.0)

# Subtitle
pdf.text("A Complete 16:9 Landscape Widescreen Knowledge Architecture Across All 19 Canonical Parts", w/2 - 240, 288, font="F1", size=10.5, rgb=TEXT_MUTED)

# Showcase Badges
box_w = 320
pdf.rect(w/2 - box_w - 15, 185, box_w, 75, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
pdf.text("SPECIAL SHOWCASE I (PART 17)", w/2 - box_w - 5, 243, font="F2", size=9.5, rgb=CYAN)
pdf.text("AYAT AL-KURSI : THE THRONE VERSE", w/2 - box_w - 5, 227, font="F2", size=11, rgb=WHITE)
pdf.text("2 Dedicated Landscape Plates * 9 Concentric Clauses", w/2 - box_w - 5, 212, font="F1", size=8, rgb=TEXT_MUTED)
pdf.text("Authentic Desert Ring Metric & Asma' wa Sifat Theology", w/2 - box_w - 5, 198, font="F3", size=7.5, rgb=GOLD_LIGHT)

pdf.rect(w/2 + 15, 185, box_w, 75, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
pdf.text("SPECIAL SHOWCASE II (PART 19)", w/2 + 25, 243, font="F2", size=9.5, rgb=PURPLE)
pdf.text("THE LAST TWO VERSES : AMANAR-RASOOL", w/2 + 25, 227, font="F2", size=11, rgb=WHITE)
pdf.text("2 Dedicated Landscape Plates * The Nightly Sufficiency", w/2 + 25, 212, font="F1", size=8, rgb=TEXT_MUTED)
pdf.text("Direct Gift Beneath the Throne & Answered Petitions", w/2 + 25, 198, font="F3", size=7.5, rgb=GOLD_LIGHT)

# Metrics Ribbon
pdf.rect(80, 135, w - 160, 34, fill_rgb=NAVY_DEEP, stroke_rgb=BORDER_MUTED, line_width=0.8)
pdf.text("78 MASTER WIDESCREEN PLATES   *   152 THEMATIC PILLARS   *   608 VISUAL CARDS   *   100% VERIFIED", w/2 - 275, 149, font="F2", size=9.5, rgb=EMERALD)

# Bottom Accreditation
pdf.text("ORTHODOX SUNNI ISLAMIC SOURCE DISCIPLINE", w/2 - 130, 85, font="F2", size=9, rgb=GOLD)
pdf.text("Tafsir Ibn Kathir  *  Jami' al-Bayan (Al-Tabari)  *  Al-Jami' li-Ahkam al-Qur'an (Al-Qurtubi)  *  Mafatih al-Ghayb (Al-Razi)", w/2 - 270, 70, font="F1", size=8, rgb=TEXT_MUTED)
pdf.text("READ. REFLECT. RETURN.", w/2 - 68, 45, font="F2", size=10.5, rgb=GOLD_LIGHT)


# ==========================================
# PAGE 2: TABLE OF CONTENTS & ARCHITECTURE
# ==========================================
pdf.new_page(w, h)

# Chrome
pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)
pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
pdf.text(" |  SURAH AL-BAQARAH MASTER COMPENDIUM", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
pdf.text("MASTER ARCHITECTURE & NAVIGATION", w - 240, h - 26, font="F2", size=9, rgb=GOLD)

pdf.text("TABLE OF CONTENTS & THEMATIC NAVIGATION", 32, h - 66, font="F2", size=12, rgb=WHITE)
pdf.text("A Navigational Roadmap across the Three Grand Cycles of Surah Al-Baqarah", 32, h - 79, font="F1", size=7.8, rgb=TEXT_MUTED)
pdf.text("[78 MASTER PLATES]", w - 140, h - 68, font="F2", size=10, rgb=GOLD)
pdf.line(32, h - 86, w - 32, h - 86, stroke_rgb=BORDER_MUTED, line_width=0.8)

# Columns for TOC
c_w = 348
c1_x = 32
c2_x = 412
y_start = h - 102

# Col 1: Cycle 1 & Cycle 2 Part 1
pdf.rect(c1_x, 35, c_w, 345, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.0)
pdf.rect(c1_x, 345, c_w, 35, fill_rgb=NAVY_ELEVATED)
pdf.text("CYCLE 1 : THE CREED & ANCIENT NATIONS", c1_x + 12, 365, font="F2", size=9, rgb=CYAN)
pdf.text("Epistemology, Primordial Genesis, Sinai & Abrahamic Legacy", c1_x + 12, 352, font="F3", size=7.2, rgb=TEXT_MUTED)
pdf.line(c1_x, 345, c1_x + c_w, 345, stroke_rgb=CYAN, line_width=0.8)

toc_col1 = [
    ("Part 01 : Epistemology of Revelation & Three Archetypes", "Plates 03 - 06"),
    ("Part 02 : Adam, Knowledge & The Primordial Trial", "Plates 07 - 10"),
    ("Part 03 : Sinai Covenant, Wilderness & The Heifer", "Plates 11 - 14"),
    ("Part 04 : Hardened Hearts, Tahreef & Moral Decalogue", "Plates 15 - 18"),
    ("Part 05 : Tribal Sedition, Solomon & Babylonian Occult", "Plates 19 - 22"),
    ("Part 06 : Linguistic Hygiene, Naskh & Universal Creed", "Plates 23 - 26"),
    ("Part 07 : Trial of Ibrahim & Foundation of the Ka'bah", "Plates 27 - 30"),
    ("Part 08 : Legacy of Ya'qub, Millat Ibrahim & Sibghatullah", "Plates 31 - 34"),
    ("Part 09 : Qiblah Reorientation & Sacred Martyrdom", "Plates 35 - 38"),
    ("Part 10 : Safa & Marwah, Concealing Truth & Pure Halal", "Plates 39 - 42"),
]

y_pos = 325
for title, plates in toc_col1:
    pdf.text(title, c1_x + 12, y_pos, font="F2", size=7.4, rgb=WHITE)
    pdf.text(plates, c1_x + c_w - 65, y_pos, font="F2", size=7.4, rgb=GOLD_LIGHT)
    pdf.line(c1_x + 12, y_pos - 4, c1_x + c_w - 12, y_pos - 4, stroke_rgb=BORDER_MUTED, line_width=0.4)
    y_pos -= 28

# Col 2: Cycle 2 Part 2 & Cycle 3 Finale
pdf.rect(c2_x, 35, c_w, 345, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.0)
pdf.rect(c2_x, 345, c_w, 35, fill_rgb=NAVY_ELEVATED)
pdf.text("CYCLES 2 & 3 : SACRED LAW & DIVINE SOVEREIGNTY", c2_x + 12, 365, font="F2", size=9, rgb=PURPLE)
pdf.text("Statutory Governance, Infaq Economy & The Crowning Showcases", c2_x + 12, 352, font="F3", size=7.2, rgb=TEXT_MUTED)
pdf.line(c2_x, 345, c2_x + c_w, 345, stroke_rgb=PURPLE, line_width=0.8)

toc_col2 = [
    ("Part 11 : Dietary Boundaries & The Constitution of Birr", "Plates 43 - 46"),
    ("Part 12 : Retribution, Wills & Ramadan Fasting", "Plates 47 - 50"),
    ("Part 13 : Sacred Defense & Just Warfare Ethics", "Plates 51 - 54"),
    ("Part 14 : Pilgrimage Ordinances & Wholehearted Islam", "Plates 55 - 58"),
    ("Part 15 : Adversity, Infaq Categories & Social Governance", "Plates 59 - 62"),
    ("Part 16 : Family Sanctity, Marriage & Talaq Charters", "Plates 63 - 66"),
    ("★ Part 17 : Talut, Goliath & AYAT AL-KURSI (🌟 Showcase)", "Plates 67 - 70"),
    ("Part 18 : Conscience, Resurrection & Infaq Economy", "Plates 71 - 74"),
    ("★ Part 19 : Usury War, Debt Charter & LAST 2 VERSES (🌟)", "Plates 75 - 78"),
]

y_pos = 325
for title, plates in toc_col2:
    is_star = "★" in title
    c_rgb = GOLD if is_star else WHITE
    pdf.text(title, c2_x + 12, y_pos, font="F2", size=7.4, rgb=c_rgb)
    pdf.text(plates, c2_x + c_w - 65, y_pos, font="F2", size=7.4, rgb=GOLD_LIGHT)
    pdf.line(c2_x + 12, y_pos - 4, c2_x + c_w - 12, y_pos - 4, stroke_rgb=BORDER_MUTED, line_width=0.4)
    y_pos -= 28

# Footer
pdf.line(32, 25, w - 32, 25, stroke_rgb=BORDER_MUTED, line_width=0.8)
pdf.text("HUURS KNOWLEDGE SYSTEMS  *  AUTHENTIC SUNNI SOURCE DISCIPLINE  *  READ. REFLECT. RETURN.", 32, 13, font="F1", size=7.2, rgb=TEXT_MUTED)
pdf.text("SURAH AL-BAQARAH FOUNDATION ARCHITECTURE", w - 235, 13, font="F2", size=7.2, rgb=GOLD)

pdf.save(INTRO_PDF)
print(f"[OK] Generated Intro/Cover PDF: {INTRO_PDF}")

# ==========================================
# MERGE WITH ALL 19 PARTS
# ==========================================
pdf_list = [INTRO_PDF]
for i in range(1, 20):
    part_pdf = f"/mnt/AI/ag/Campaign/07_MINDMAP/BAQARAH_PART_{i:02d}_MINDMAP.pdf"
    if os.path.exists(part_pdf):
        pdf_list.append(part_pdf)
    else:
        print(f"[WARNING] Missing: {part_pdf}")

print(f"Merging {len(pdf_list)} PDF documents into {MASTER_COMPENDIUM_PDF}...")
merge_cmd = f"pdfunite {' '.join(pdf_list)} {MASTER_COMPENDIUM_PDF}"
subprocess.run(merge_cmd, shell=True, check=True)
print(f"[SUCCESS] Merged Master Compendium PDF created: {MASTER_COMPENDIUM_PDF}")

# Render Cover and TOC previews
cmd_prev = f"pdftoppm -png -r 150 -f 1 -l 2 {MASTER_COMPENDIUM_PDF} {previews_dir}/compendium_page"
subprocess.run(cmd_prev, shell=True, check=True)

shutil.copyfile(f"{previews_dir}/compendium_page-01.png", f"{brain_dir}/compendium_cover.png")
shutil.copyfile(f"{previews_dir}/compendium_page-02.png", f"{brain_dir}/compendium_toc.png")
print(f"[OK] Previews copied to brain directory.")

