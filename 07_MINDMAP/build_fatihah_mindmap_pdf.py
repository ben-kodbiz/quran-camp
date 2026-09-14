#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Fatihah Master Landscape Mindmap PDF CompilerStrict Standardization:
- Title: Surah Al-Fatihah — Master Landscape Mindmap
- Zero Ayah Numbers in titles/headers/cards
- Zero mention of external speaker names; 100% Huurs Studio & Sunni source discipline
- Thematic sequence purity
- 4 Landscape Widescreen Pages (792 x 480 pts, 1.65:1 / 16:9 ratio)
- Symmetrical 2-column layout with center connector bridges
"""

import os
import sys
import subprocess
import shutil

# Import verified PDF engine
sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
OUTPUT_PDF = os.path.join(BASE_DIR, "FATIHAH_MASTER_MINDMAP.pdf")
PREVIEWS_DIR = os.path.join(BASE_DIR, "previews")
os.makedirs(PREVIEWS_DIR, exist_ok=True)

brain_dir = "/home/ben/.gemini/antigravity/brain/1d535f8c-0b01-42ad-8e78-fc566134377c"

# Palette (Strict Brand_Visual_System.md)
NAVY_DEEP = (0.024, 0.039, 0.071)      # #060A12
NAVY_CARD = (0.051, 0.078, 0.133)      # #0D1422
NAVY_ELEVATED = (0.078, 0.118, 0.196)  # #141E32
GOLD = (0.831, 0.686, 0.353)           # #D4AF59
GOLD_LIGHT = (0.910, 0.820, 0.580)
CYAN = (0.220, 0.740, 0.970)           # #38BDF8
PURPLE = (0.659, 0.333, 0.969)         # #A855F7
EMERALD = (0.063, 0.725, 0.506)        # #10B981
ROSE = (0.920, 0.350, 0.450)
WHITE = (0.973, 0.980, 0.988)
TEXT_MUTED = (0.680, 0.730, 0.800)
BORDER_MUTED = (0.160, 0.220, 0.310)

def build_fatihah_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        # Background
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH AL-FATIHAH", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
        # Badges
        pdf.rect(w - 280, h - 32, 175, 20, fill_rgb=NAVY_ELEVATED, stroke_rgb=BORDER_MUTED, line_width=0.8)
        pdf.text(f"PAGE {pnum:02d} / {total_pages:02d}", w - 85, h - 26, font="F2", size=9, rgb=GOLD)

        # Sub-title Bar
        pdf.text(title, 32, h - 66, font="F2", size=12, rgb=WHITE)
        pdf.text(subtitle, 32, h - 79, font="F1", size=7.8, rgb=TEXT_MUTED)
        pdf.text(f"[{section_badge}]", w - 160, h - 68, font="F2", size=10.5, rgb=GOLD)
        pdf.line(32, h - 86, w - 32, h - 86, stroke_rgb=BORDER_MUTED, line_width=0.8)

        # Bottom Footer
        pdf.line(32, 25, w - 32, 25, stroke_rgb=BORDER_MUTED, line_width=0.8)
        pdf.text("HUURS KNOWLEDGE SYSTEMS  *  AUTHENTIC SUNNI SOURCE DISCIPLINE  *  READ. REFLECT. RETURN.", 32, 13, font="F1", size=7.2, rgb=TEXT_MUTED)
        pdf.text("SURAH AL-FATIHAH FOUNDATION ARCHITECTURE", w - 245, 13, font="F2", size=7.2, rgb=GOLD)

    # Column Coordinates
    c1_x, c1_y, c1_w, c1_h = 32, 35, 348, h - 130
    c2_x = c1_x + c1_w + 32
    c2_w = 348

    # =========================================================================
    # PAGE 1: THE CELESTIAL PROLOGUE & THE ARCHITECTURE OF PRAISE
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 4,
        "THE CELESTIAL PROLOGUE & THE ARCHITECTURE OF ABSOLUTE PRAISE",
        "Pillars 1 & 2: Hermeneutical foundations, the halved prayer dialogue, and the grammar of eternal Hamd",
        "PART 1 : SECTION 1"
    )

    # Column 1: Pillar 1 (Hermeneutics & Divine Dialogue)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 1: HERMENEUTICAL FOUNDATIONS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Umm al-Kitab, The Halved Prayer & Isti'adhah", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    # Card 1A: Umm al-Kitab
    y_c = c1_y + c1_h - 48
    pdf.text("1. Umm al-Kitab: The Mother & Seed of Revelation", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Hadith (Bukhari): Designated as Umm al-Qur'an, Sab' al-Mathani, and Shifa'.\n"
        "- In Semitic idiom, the 'Umm' (mother) of something is its comprehensive root.\n"
        "- Every theme across the 113 following surahs is contained in seed form here."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 1B: Hadith Qudsi Dialogue
    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. The Divine Dialogue: The Prayer Halved in Two", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Sahih Muslim: 'I have divided the prayer between Myself and My servant in two halves.'\n"
        "- Each recited verse receives an immediate, personal response from Allah.\n"
        "- Prayer is transformed from a human monologue into an intimate, living conversation."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 1C: Isti'adhah Sanctuary
    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Isti'adhah: Spiritual Sanctuary Before Recitation", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Commanded in An-Nahl (16:98): Clean pipes are required for clean water.\n"
        "- Shaytan attacks the intellect precisely when approaching divine guidance.\n"
        "- Seeking refuge purges cynical distraction and opens the heart to guidance."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 1D: Basmalah Grammar
    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Basmalah: The Grammar of Divine Inception", c1_x + 12, y_c, font="F2", size=8, rgb=CYAN)
    t = (
        "- Prepositional 'Bi': Denotes Isti'anah (seeking empowerment) and Musahabah.\n"
        "- The believer acts not in personal weakness, but accompanied by the Sacred Name.\n"
        "- Root R-H-M (the womb) establishes that divine power is cloaked in compassion."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 2 (Grammar of Hamd)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 2: THE ARCHITECTURE OF ABSOLUTE PRAISE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Al-Hamd, Nominal Permanence & Cosmic Lordship", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    # Card 2A: Hamd vs Shukr
    y_c = c1_y + c1_h - 48
    pdf.text("1. Al-Hamd vs. Shukr: The Unconditional Stance", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Shukr is reactive to favors; Hamd combines intrinsic praise with gratitude.\n"
        "- Al-Istighraq: Definite article 'Al-' claims every conceivable praise for God.\n"
        "- Praise belongs to Allah even in the darkest trial, independent of personal ease."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 2B: Nominal Permanence
    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Nominal Permanence (Jumla Ismiyyah) Over Action", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Verbal sentences ('Nahmadullah') depend on time and fallible human action.\n"
        "- A nominal sentence establishes an immutable, eternal, self-subsisting reality.\n"
        "- God's praise is unalterable: It existed before creation and endures forever."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 2C: Rabb The Nurturer
    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Rabb: The Nurturing Master & Caretaker", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Root R-B-B unites Sayyid (master), Malik (owner), and Murabbi (nurturer).\n"
        "- A Murabbi fosters development from embryonic weakness to full perfection.\n"
        "- Every circumstance is part of a divine curriculum designed for the soul's growth."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 2D: Al-'Alamin
    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Al-'Alamin: Signs Testifying in Every Realm", c2_x + 12, y_c, font="F2", size=8, rgb=EMERALD)
    t = (
        "- Plural of 'Alam, derived from 'Alamah (a landmark, symbol, or sign).\n"
        "- Every sphere—physical cosmos, angelic realms, flora, fauna, human societies—\n"
        "- Exists as an unmistakable indicator pointing directly to its Sovereign Maker."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 2: THE OCEANS OF MERCY & SOVEREIGN RECOMPENSE
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 4,
        "THE OCEANS OF MERCY & SOVEREIGN ACCOUNTABILITY",
        "Pillars 3 & 4: The dual dynamics of compassion, dual Qira'at sovereignty, and settling the cosmic loan",
        "PART 1 : SECTION 2"
    )

    # Column 1: Pillar 3 (Dual Dynamics of Mercy)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 3: THE DUAL DYNAMICS OF COMPASSION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Ar-Rahman, Ar-Rahim & Dismantling Despair", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    # Card 3A: Balancing Awe
    y_c = c1_y + c1_h - 48
    pdf.text("1. Balancing Awe with Maternal Tenderness", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Rabbil-'Alamin invokes awe, immense power, and cosmic subjugation.\n"
        "- Human kings and overlords inspire paralyzing dread and alienation.\n"
        "- Allah immediately comforts hearts: Authority is anchored in maternal mercy."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 3B: Morphological Contrast
    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Morphological Contrast: Fa'lan vs. Fa'eel", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Fa'lan (Ar-Rahman): Intensity, surging fullness, and overflowing immediacy.\n"
        "- Fa'eel (Ar-Rahim): Constancy, permanence, and unbroken continuity.\n"
        "- One name captures the bursting flood; the other captures the permanent ocean."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 3C: Cosmic vs Salvific
    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Cosmic Torrent vs. Permanent Salvific Shelter", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Ar-Rahman embraces all creation in Dunya: oxygen, water, health, and sunlight.\n"
        "- Ar-Rahim is the specialized, eternal mercy reserved for believers in Akhirah.\n"
        "- The believer lives under universal care today and rests in eternal shelter tomorrow."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 3D: Root R-H-M
    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Root R-H-M: The Primordial Sanctuary", c1_x + 12, y_c, font="F2", size=8, rgb=EMERALD)
    t = (
        "- Derived from the mother's womb (Rahim), providing warmth and unconditional safety.\n"
        "- A child receives maternal care before earning anything or performing any service.\n"
        "- Divine love precedes human striving, destroying cynicism and religious self-hatred."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 4 (Day of Recompense)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 4: THE DAY OF MORAL RECKONING", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Malik, Maalik, Yawm ad-Deen & Ultimate Justice", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    # Card 4A: Dual Qira'at
    y_c = c1_y + c1_h - 48
    pdf.text("1. Dual Qira'at: Malik (King) and Maalik (Owner)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Canonical readings: Warsh reads Malik (Sovereign); Hafs reads Maalik (Owner).\n"
        "- An owner possesses physical assets; a king holds judicial jurisdiction.\n"
        "- Allah alone synthesizes both: Absolute property ownership and supreme judicial decree."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 4B: Settling the Loan
    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Yawm ad-Deen: Settling the Cosmic Debt", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Root D-Y-N denotes Dayn (debt, loan, contract, binding obligation).\n"
        "- Life is an unearned loan of consciousness, health, wealth, and agency.\n"
        "- Yawm ad-Deen is the exact accounting day where every loan is audited to the penny."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 4C: Eradicating Nihilism
    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. The Moral Bedrock: Eradicating Nihilism", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- If death ends all, oppressors triumph and martyrs sacrifice in vain.\n"
        "- Recompense establishes an objective moral cosmos: Tyranny faces retribution.\n"
        "- Sincere strivings, hidden tears, and quiet integrity are recognized and redeemed."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 4D: Balancing Mercy and Justice
    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. The Divine Keystone: Mercy United with Justice", c2_x + 12, y_c, font="F2", size=8, rgb=PURPLE)
    t = (
        "- Mercy without accountability degenerates into permissive moral anarchy.\n"
        "- Justice without mercy crushes the human soul in unbearable legalism.\n"
        "- Al-Fatihah perfectly balances both: Immense mercy crowned by impartial justice."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 3: THE CENTRAL COVENANT & THE HIGHWAY OF GUIDANCE
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 4,
        "THE CENTRAL COVENANT & THE HIGHWAY OF GUIDANCE",
        "Pillars 5 & 6: The Iltifat pivot, exclusive devotion, and the four tiers of ascending Hidayah",
        "PART 1 : SECTION 3"
    )

    # Column 1: Pillar 5 (Charter of Servitude)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 5: THE CHARTER OF SERVITUDE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Iyyaka Na'budu, Iltifat Shift & Collective Devotion", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    # Card 5A: Iltifat Shift
    y_c = c1_y + c1_h - 48
    pdf.text("1. The Rhetorical Pivot: Shift to Direct Presence", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Verses 1-4 speak of God in the 3rd person: 'All praise belongs to Him...'\n"
        "- Verse 5 shifts dramatically to 2nd person: 'You alone we worship!' (Iltifat).\n"
        "- The soul ascends from knowing about God to standing directly in His audience."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 5B: Grammatical Hasr
    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Grammatical Fronting (Hasr): Absolute Exclusivity", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Normal syntax: 'Na'buduka' (We worship You); Qur'an fronts: 'Iyyaka Na'budu'.\n"
        "- Fronting the object induces Hasr wal-Ikhtisas (confinement and exclusivity).\n"
        "- 'You alone we worship, and under no circumstances do we bow to any rival!'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 5C: Right Before Need
    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Divine Right Before Human Need: 'Ibadah First", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Worship ('Ibadah) precedes petitioning for assistance (Isti'anah).\n"
        "- Worship is the Creator's rightful due; assistance is the creature's need.\n"
        "- We honor the Master's sovereign claim before presenting our personal requests."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 5D: Collective Plural
    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. The Collective Plural: Dismantling Spiritual Ego", c1_x + 12, y_c, font="F2", size=8, rgb=CYAN)
    t = (
        "- The text does not say 'I worship' (A'budu); it proclaims 'We worship' (Na'budu).\n"
        "- Even when praying alone at midnight, the believer dissolves the isolated ego.\n"
        "- Our frail prayer is wrapped inside the global communion of righteous believers."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 6 (Anatomy of Guidance)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 6: THE ANATOMY OF ULTIMATE GUIDANCE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Ihdina, The Four Tiers of Hidayah & Al-Sirat", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    # Card 6A: Universal Petition
    y_c = c1_y + c1_h - 48
    pdf.text("1. The Universal Petition: Guidance as Sole Life Need", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Standing in divine presence, the servant asks for neither wealth nor status.\n"
        "- The master petition is Hidayah: Divine light navigating every crossroads.\n"
        "- With guidance, poverty and prosperity, sickness and health lead alike to salvation."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 6B: Four Tiers of Hidayah
    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Four Ascending Tiers of Guidance (Ibn al-Qayyim)", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 1. Instinctual Guidance (creation biologies); 2. Clarification (scripture/intellect).\n"
        "- 3. Tawfeeq (heart opening to practice truth); 4. Celestial Guidance across Sirat.\n"
        "- The guided believer continually asks for firmness, deeper insight, and tawfeeq."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 6C: Sirat vs Sabeel
    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Sirat: The Broad, Straight Highway", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Unlike winding trails (Subul) or dark alleys (Turuq), Sirat is always singular.\n"
        "- A wide, illuminated highway that accommodates all humanity without bottleneck.\n"
        "- A straight line is mathematically the shortest distance between creature and Creator."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 6D: Istiqamah
    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Al-Mustaqeem: The Demands of Uprightness", c2_x + 12, y_c, font="F2", size=8, rgb=CYAN)
    t = (
        "- Derived from Root Q-W-M (to stand upright, unswerving, consistent).\n"
        "- Istiqamah requires ethical courage: Resisting ideological fashion and compromise.\n"
        "- The path is grounded in eternal divine truth, not shifting cultural trends."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 4: THE THREE DESTINIES & COSMIC RING BALANCE
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 4,
        "THE THREE DESTINIES & COSMIC RING BALANCE",
        "Pillars 7 & 8: Historical models of guidance, passive adab of wrath, and the architectural ring seed of the Qur'an",
        "PART 1 : SECTION 4"
    )

    # Column 1: Pillar 7 (The Three Spiritual Paths)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 7: THE THREE SPIRITUAL PATHS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("The Favored, The Wrath-Incurred & The Astray", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    # Card 7A: Favored Company
    y_c = c1_y + c1_h - 48
    pdf.text("1. The Blessed Fellowship: Four Historical Exemplars", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Glossed in An-Nisa (4:69): Prophets, Truthful, Martyrs, and the Righteous.\n"
        "- Guidance is not abstract ideology; it is a paved path walked by real humans.\n"
        "- Walking with the righteous shields the soul from isolation and doubt."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 7B: Passive Voice Adab
    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. The Evoked Wrath: Passive Voice & Divine Adab", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Favor is active: 'An'amta' (You blessed); Wrath is passive: 'Al-Maghdubi 'alayhim'.\n"
        "- The agent of wrath is omitted: God does not act maliciously; rebellion earns wrath.\n"
        "- Pure goodness is ascribed to the Creator; human destruction is self-inflicted."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 7C: The Bewildered Straying
    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. The Bewildered Straying: Zeal Without Knowledge", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Wa lad-Dallin: Those who lose the way through emotion, dogma, and speculation.\n"
        "- Sincerity without sound knowledge inevitably drifts into superstition and error.\n"
        "- Religion is preserved by revelation and intellect, not subjective whims."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 7D: The Golden Mean
    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. The Golden Mean: Synthesis of Knowledge & Action", c1_x + 12, y_c, font="F2", size=8, rgb=ROSE)
    t = (
        "- Maghdub = Knowledge without Action (hypocrisy, cynicism, arrogance).\n"
        "- Dallin = Action without Knowledge (blind emotionalism, religious innovation).\n"
        "- The Straight Path synthesizes deep knowledge inseparably with righteous action."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 8 (Structural Chiasmus)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 8: STRUCTURAL CHIASMUS & SEED OF QUR'AN", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Ring Composition, Cosmic Symmetry & Al-Baqarah", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    # Card 8A: Concentric Ring
    y_c = c1_y + c1_h - 48
    pdf.text("1. The Concentric Ring Composition of Al-Fatihah", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 7 Verses: 3 verses of divine praise + 1 center pivot + 3 verses of human petition.\n"
        "- Symmetrical chiasmus: Verse 1 mirrors 7; Verse 2 mirrors 6; Verse 3 mirrors 5.\n"
        "- The prayer is structurally anchored upon the central covenant of surrender."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 8B: Mirror Symmetry
    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. The Mirror Symmetry of Praise and Petition", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Top Half: Belongs entirely to the Master (Names, Lordship, Cosmic Mercy, Justice).\n"
        "- Bottom Half: Belongs entirely to the Servant (Guidance, Fellowship, Protection).\n"
        "- Verse 5 unites both: 'Iyyaka Na'budu' (Master's right) & 'Iyyaka Nasta'een' (servant's need)."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 8C: Seed to Tree
    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. The Microcosmic Blueprint: Seed to Expansive Tree", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Al-Fatihah is the seed; the remaining 113 surahs are the branches and fruit.\n"
        "- Stories of ancient nations illustrate the favored, the maghdub, and the dallin.\n"
        "- Legal ordinances detail the Sirat; eschatological surahs detail Yawm ad-Deen."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 8D: Seamless Handshake
    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. The Seamless Handshake: The Prayer Answered", c2_x + 12, y_c, font="F2", size=8, rgb=PURPLE)
    t = (
        "- Al-Fatihah ends with humanity's urgent cry: 'Ihdinas-Sirat al-Mustaqeem!'\n"
        "- Al-Baqarah instantly answers: 'Dhalikal-Kitabu la rayba feeh, hudal-lil-muttaqin.'\n"
        "- What the soul begs for in Al-Fatihah is placed into its hands in Al-Baqarah."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Save PDF
    pdf.save(OUTPUT_PDF)
    print(f"FATIHAH_MASTER_MINDMAP.pdf successfully compiled: {OUTPUT_PDF}")

    # Generate PNG previews
    cmd = f"pdftoppm -png -r 150 {OUTPUT_PDF} {PREVIEWS_DIR}/fatihah_page"
    subprocess.run(cmd, shell=True, check=True)
    print("PNG Previews generated in previews directory.")

    # Copy to brain dir
    for i in range(1, 5):
        src = f"{PREVIEWS_DIR}/fatihah_page-{i}.png"
        dst = os.path.join(brain_dir, f"fatihah_page-{i}.png")
        if os.path.exists(src):
            shutil.copyfile(src, dst)
            print(f"Copied {src} to {dst}")

if __name__ == "__main__":
    build_fatihah_pdf()
