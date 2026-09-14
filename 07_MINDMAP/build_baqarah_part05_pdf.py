#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Baqarah Part 5 Master Landscape Mindmap PDF Compiler
Foundation Media: Part 5 Audio Lecture (Duration: 01:30:35)
Strict Standardization:
- Title: Surah Al-Baqarah — Part 5
- Zero Ayah Numbers in titles/headers/cards
- Zero mention of external speaker names; 100% Huurs Studio & Sunni source discipline
- 4 Landscape Widescreen Pages (792 x 480 pts, 1.65:1 ratio)
- Symmetrical 2-column layout with center connector bridges
- Perfect vertical card distribution (71pt intervals) with zero collisions
"""

import os
import sys

# Import verified PDF engine
sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
OUTPUT_PDF = os.path.join(BASE_DIR, "BAQARAH_PART_05_MINDMAP.pdf")

# Palette
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
BORDER_GOLD = (0.700, 0.560, 0.280)

def build_part05_pdf():
    w, h = 792, 480 # Landscape ratio (1.65:1)
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge, time_badge):
        # Background
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH AL-BAQARAH", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
        # Audio & Page Badges
        pdf.rect(w - 290, h - 32, 185, 20, fill_rgb=NAVY_ELEVATED, stroke_rgb=BORDER_MUTED, line_width=0.8)
        pdf.text(f"FOUNDATION MEDIA: PART 5 ({time_badge})", w - 282, h - 20, font="F2", size=6.8, rgb=EMERALD)
        pdf.text(f"PAGE {pnum:02d} / {total_pages:02d}", w - 85, h - 26, font="F2", size=9, rgb=GOLD)

        # Sub-title Bar
        pdf.text(title, 32, h - 66, font="F2", size=12, rgb=WHITE)
        pdf.text(subtitle, 32, h - 79, font="F1", size=7.8, rgb=TEXT_MUTED)
        pdf.text(f"[{section_badge}]", w - 140, h - 68, font="F2", size=10.5, rgb=GOLD)
        pdf.line(32, h - 86, w - 32, h - 86, stroke_rgb=BORDER_MUTED, line_width=0.8)

        # Bottom Footer
        pdf.line(32, 25, w - 32, 25, stroke_rgb=BORDER_MUTED, line_width=0.8)
        pdf.text("HUURS KNOWLEDGE SYSTEMS  *  AUTHENTIC SUNNI SOURCE DISCIPLINE  *  READ. REFLECT. RETURN.", 32, 13, font="F1", size=7.2, rgb=TEXT_MUTED)
        pdf.text("SURAH AL-BAQARAH FOUNDATION ARCHITECTURE", w - 235, 13, font="F2", size=7.2, rgb=GOLD)

    # Column Coordinates
    c1_x, c1_y, c1_w, c1_h = 32, 35, 348, h - 130
    c2_x = c1_x + c1_w + 32
    c2_w = 348
    bridge_y = c1_y + c1_h / 2

    CARD_STEP = 71 # Vertical spacing between cards

    # =========================================================================
    # PAGE 1: TRIBAL SEDITION, CIVIL WARFARE & SELECTIVE SCRIPTURE
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 4,
        "TRIBAL SEDITION, CIVIL WARFARE & SELECTIVE SCRIPTURE",
        "Pillars 1 & 2: Medinan tribal alliances, brethren slaughter, the ransom hypocrisy, and double penalty",
        "PART 5 : SECTION 1",
        "00:00 - 20:25"
    )

    # Column 1: Pillar 1 (Medinan Tribal Sedition & Hypocrisy of Ransoming)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 1: CIVIL WARFARE & CAPTIVE RANSOMING", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Banu Isra'il Alliances, Expulsion of Brethren & Fidyah Hypocrisy", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c1_x + c1_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=0.6)
    pdf.text("00:00 - 10:15", c1_x + c1_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    # Card 1A: Geopolitical Sedition in Medina
    y_c = c1_y + c1_h - 50
    pdf.text("1. Medinan Tribal Alliances (Thumma Antum Ha'ula')", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Jewish tribes in Medina divided: Qaynuqa/Nadir allied with Khazraj, Qurayzah with Aws.\n"
        "- When civil war erupted, they sided with pagan allies to slaughter and evict their own brethren.\n"
        "- Explicit violation of the Torah prohibition against shedding brethren blood or expelling them."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 1B: The Ransom Hypocrisy
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. The Ransoming Hypocrisy: 'Wa In Ya'tookum Usara'", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- When Jewish combatants were captured, they pooled community funds to redeem them (Tufadoohum).\n"
        "- Piety theater: Claimed Torah commanded ransoming, while ignoring that they caused the war.\n"
        "- Willing to kill them in battle, but eager to fundraise to free them when captured."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 1C: Fractional Scripture
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. The Indictment of Selective Faith (Bi-Ba'dil-Kitab)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'A-fatu'minoona bi-ba'dil-Kitabi wa takfuroona bi-ba'd?': Believing part, rejecting part.\n"
        "- Obeying the law only when convenient, while violating its fundamental pillars for political gain.\n"
        "- Selective adherence to divine revelation is legally and spiritually equivalent to total disbelief."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 1D: The Double Penalty
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Worldly Disgrace & Fiercest Torment (Khizyun & Ashadd)", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Penalty 1: 'Khizyun fil-hayatid-dunya' — Complete sociopolitical disgrace and humiliation.\n"
        "- Penalty 2: 'Ila ashaddil-'adhab' — Consigned to the fiercest torment on the Day of Resurrection.\n"
        "- 'Wa mallahu bi-ghafilin': Divine justice never sleeps; heedlessness (Ghaflah) is a fatal delusion."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Center Gap Connector Bridge
    pdf.line(c1_x + c1_w, bridge_y, c2_x, bridge_y, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(w/2 - 12, bridge_y - 8, 24, 16, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=0.8)
    pdf.text_centered("->", w/2, bridge_y + 3, font="F2", size=7, rgb=GOLD_LIGHT)

    # Column 2: Pillar 2 (The Pathology of Selective Religion)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 2: THE PATHOLOGY OF SELECTIVE DIN", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Self-Serving Religion, Legalistic Crutches & Moral Dissociation", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c2_x + c2_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=0.6)
    pdf.text("10:16 - 20:25", c2_x + c2_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    # Card 2A: The Din Serving the Self
    y_c = c1_y + c1_h - 50
    pdf.text("1. Inversion of Din: Demanding Religion Serve the Self", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Din was revealed for humans to surrender to God; spiritual rot occurs when humans use Din for self-gain.\n"
        "- Picking ritual aspects that make one feel accomplished while neglecting basic ethical duties.\n"
        "- When scholars and believers act hypocritically, they make the Din itself look repulsive to outsiders."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 2B: Modern Ummah Parallels
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Compartmentalized Piety: Modern Ummah Parallels", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Strictness in prayer or halal food, while neglecting family obligations or earning haram income.\n"
        "- A saint in the mosque, but oppressive and cruel at home or in business transactions.\n"
        "- This is the modern manifestation of believing in part of the Scripture and rejecting the rest."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 2C: Internal Muslim Conflict
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Slandering Brethren & Tribal Lawsuits", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Historic tragedy: Muslim factions warring, declaring Takfir on each other until external enemies strike.\n"
        "- Turning to secular courts to wage bitter lawsuits against fellow believers and mosques.\n"
        "- The sanctity, blood, and dignity of a believer are inviolable in the sight of God."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 2D: Consciousness of Divine Sight
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Curing Ghaflah: The Living Watchfulness of Allah", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Wa mallahu bi-ghafilin 'amma ta'maloon': A direct spiritual cure for moral compromise.\n"
        "- If consciousness of Allah's sight was present, humans would restrain their tongues and actions.\n"
        "- Taqwa is the active awareness that every action, contract, and evasion is audited in real-time."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 2: WORLDLY TRANSACTION & THE SUCCESSION OF PROPHETS
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 4,
        "WORLDLY INVESTMENTS & THE SUCCESSION OF PROPHETS",
        "Pillars 3 & 4: Purchasing Dunya, unmitigated torment, prophetic continuum from Moses to Jesus, and Hawa",
        "PART 5 : SECTION 2",
        "20:26 - 34:09"
    )

    # Column 1: Pillar 3 (Purchasing Dunya & Unmitigated Torment)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 3: THE WORLDLY TRANSACTION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Buying Dunya for Akhirah, False Entitlement & Unlightened Torment", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c1_x + c1_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=0.6)
    pdf.text("20:26 - 27:15", c1_x + c1_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    # Card 3A: Purchasing Dunya
    y_c = c1_y + c1_h - 50
    pdf.text("1. The Ruinous Trade: 'Ishtarawul-Hayatad-Dunya'", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Ula'ikalladhinash-tarawul-hayatad-dunya bil-akhirah': Exchanging eternity for fleeting comforts.\n"
        "- Usually used for disbelievers, but here addressed to those claiming scriptural faith.\n"
        "- They preferred political alliances, worldly power, and wealth over divine integrity."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 3B: No Lightening of Punishment
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Unmitigated Torment: 'Fa-la Yukhaffafu 'Anhum'", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- God's law intended to lighten burdens in life: 'Yureedullahu an yukhaffifa 'ankum' (Nisa 4:28).\n"
        "- Rejecting divine law results in punishment that will never be lightened in the Hereafter.\n"
        "- 'Wa la hum yunsaroon': Stripped of all intercession, allies, or tribal confederates."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 3C: Self-Serving Good Deeds
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Delusion of Minimum Compliance", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The hypocrite believes fulfilling a single convenient ritual grants total immunity from judgment.\n"
        "- God shatters this delusion: selectively obeying minor rules while committing major sins is worthless.\n"
        "- Salvation requires sincere, comprehensive submission (Silm) to divine authority."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 3D: The Spiritual Balance Sheet
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. The Spiritual Economy: Dunya vs. Akhirah Accounts", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Spending in Allah's cause is a transfer from the earthly account to the eternal account.\n"
        "- Investing entirely in Dunya leaves the Akhirah account bankrupt, breeding terror of death.\n"
        "- Where a person's treasure is invested, there their heart and anticipation will remain."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Center Gap Connector Bridge
    pdf.line(c1_x + c1_w, bridge_y, c2_x, bridge_y, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(w/2 - 12, bridge_y - 8, 24, 16, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=0.8)
    pdf.text_centered("->", w/2, bridge_y + 3, font="F2", size=7, rgb=GOLD_LIGHT)

    # Column 2: Pillar 4 (The Prophetic Continuum from Moses to Jesus)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 4: THE PROPHETIC CONTINUUM", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Succession of Messengers, Jesus Son of Mary, Hawa & Hubris", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c2_x + c2_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=0.6)
    pdf.text("27:16 - 34:09", c2_x + c2_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    # Card 4A: Prophetic Succession (Qaffayna)
    y_c = c1_y + c1_h - 50
    pdf.text("1. Pearls on a String: 'Wa Qaffayna Min Ba'dihi'", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Qaffayna' (Root Q-F-W): Continuous succession of prophets sent one after another.\n"
        "- From Moses onward, countless prophets preserved, explained, and revived the Torah.\n"
        "- Divine mercy provided unbroken guidance so no generation was left without a warner."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 4B: Jesus Son of Mary
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Jesus Fortified with Signs & Rooh al-Qudus", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Wa aatayna 'Isabna Maryamal-Bayyinat': Jesus was sent as the final prophet to Banu Isra'il.\n"
        "- Given clear signs (raising dead, healing lepers) and fortified by the Holy Spirit (Archangel Jibril).\n"
        "- Moses opened the Israelite era; Jesus concluded it before the final universal Prophet."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 4C: The Tyranny of Desire (Hawa)
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Rebellion Against Divine Law: 'Bima La Tahwa'", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Afa-kullama ja'akum rasoolum-bima la tahwa anfusukumus-takbartum': Hawa vs. Wahy.\n"
        "- Whenever a prophet brought divine commands contradicting personal appetites, they rebelled.\n"
        "- True faith requires desires to be subordinated to prophetic revelation, not vice versa."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 4D: Falsifying & Slaying Prophets
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Falsifying & Slaying Prophets (Fareeqan Kadhdhabtum)", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Some prophets they slandered as liars (Isa, Muhammad); others they murdered (Zechariah, Yahya).\n"
        "- Prophet's hadith: 'Ulama'u ummati ka-anbiya'i bani Isra'il' (Scholars inherit prophetic role).\n"
        "- Persecuting, imprisoning, and silencing righteous scholars replicates this historic treason."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 3: THE SEALED HEARTS FALLACY & THE CRITERION OF DEATH
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 4,
        "THE SEALED HEARTS FALLACY & THE CRITERION OF DEATH",
        "Pillars 5 & 6: Arrogant claims of sealed hearts, the prophecy trump card, and the sincerity test of death",
        "PART 5 : SECTION 3",
        "34:10 - 48:24"
    )

    # Column 1: Pillar 5 (Sealed Hearts Myth & Exploiting Prophecy)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 5: SEALED HEARTS & PROPHETIC BETRAYAL", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Quloobuna Ghulf, Cursed for Disbelief & The Betrayal of Prophecy", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c1_x + c1_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=0.6)
    pdf.text("34:10 - 41:15", c1_x + c1_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    # Card 5A: Slogan of Sealed Hearts
    y_c = c1_y + c1_h - 50
    pdf.text("1. The Slogan of Intellectual Hubris: 'Quloobuna Ghulf'", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Claimed: 'Our hearts are wrapped / encased' — meaning fully stocked with knowledge.\n"
        "- Arrogant dismissal: We have no need for outside revelation or a Gentile Arab messenger.\n"
        "- God's rebuttal: 'Bal la'anahumullahu bi-kufrihim' — They are cursed and exiled from mercy."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 5B: The Prophecy Trump Card
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Exploiting Prophecy as a Threat (Yastaftihoon)", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Prior to Islam, whenever defeated by pagan Arabs, they boasted: 'A prophet is coming!'\n"
        "- 'Wa kanoo min qablu yastaftihoona 'alal-ladhina kafaroo': Seeking victory through his name.\n"
        "- Used scriptural prophecies as a geopolitical trump card to threaten rivals."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 5C: Rejection Out of Racial Envy
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Rejection Out of Racial Envy (Baghyan)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Fa-lamma ja'ahum ma 'arafoo kafaroo bih': When the recognized truth arrived, they denied it.\n"
        "- Rejected purely out of envy (Baghyan) because the Prophet was an Arab from Isma'il.\n"
        "- Racial nationalism superseded submission to truth, sealing their condemnation."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 5D: Wrath Upon Wrath
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Wrath Upon Wrath (Ghadaban 'Ala Ghadab)", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Bi'sa mash-taraw bihi anfusahum': Vile is the price for which they sold their souls.\n"
        "- Compounded anger: First for rejecting Isa and the Torah; second for denying Muhammad.\n"
        "- 'Wa lil-kafireena 'adhabun muheen': For the arrogant deniers is an utterly humiliating penalty."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Center Gap Connector Bridge
    pdf.line(c1_x + c1_w, bridge_y, c2_x, bridge_y, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(w/2 - 12, bridge_y - 8, 24, 16, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=0.8)
    pdf.text_centered("->", w/2, bridge_y + 3, font="F2", size=7, rgb=GOLD_LIGHT)

    # Column 2: Pillar 6 (The Wish for Death & Clinging to Life)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 6: THE LITMUS TEST OF DEATH", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Fatamannawul-Mawt, Worldly Clinging & 1000-Year Delusion", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c2_x + c2_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=0.6)
    pdf.text("41:16 - 48:24", c2_x + c2_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    # Card 6A: The Death Challenge
    y_c = c1_y + c1_h - 50
    pdf.text("1. The Sincerity Challenge: 'Fatamannawul-Mawt'", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Decisive challenge: If Paradise is exclusively yours to the exclusion of all humanity, wish for death!\n"
        "- If you are guaranteed paradise with zero reckoning, death is an immediate ticket to eternal bliss.\n"
        "- Unmasks false religious confidence: their deeds prove they dread facing God."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 6B: Guilt Drives Fear
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. The Hand's Investments: 'Bima Qaddamat Aydihim'", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Wa lan yatamannawhu abadan': They will never, ever wish for death in sincerity.\n"
        "- Why? 'Bima qaddamat aydihim' — Because of the corrupt deeds and sins their hands sent forward.\n"
        "- Deep inside, every corrupt soul knows its record is black and terrifies at the final reckoning."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 6C: Desperate Attachment to Life
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Desperate Attachment to Life (Ahrasan-Nasi)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Wa la-tajidannahum ahrasan-nasi 'ala hayah': The most greedy of people in clinging to mere life.\n"
        "- More desperate than pagan idolaters, who had warrior honor codes accepting heroic death.\n"
        "- When hearts have no hope in the Akhirah, they obsessively cling to any worldly existence."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 6D: The 1,000-Year Delusion
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. The Futile 1,000-Year Wish (Alfa Sanah)", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Yawaddu ahaduhum law yu'ammaru alfa sanah': Each wishes to live for a thousand years.\n"
        "- 'Wa ma huwa bi-muzahzihihi minal-'adhab': Longevity does not avert divine justice.\n"
        "- Whether one lives 50 or 1,000 years, every soul will stand naked before the All-Seeing (Baseer)."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 4: THE ANGELIC FEUD, SOLOMON'S VINDICATION & BABYLONIAN OCCULT
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 4,
        "THE ANGELIC FEUD, SOLOMON'S VINDICATION & BABYLONIAN OCCULT",
        "Pillars 7 & 8: Pretext against Jibril, tossing scripture, exonerating Solomon, and Harut/Marut magic",
        "PART 5 : SECTION 4",
        "48:25 - 90:35"
    )

    # Column 1: Pillar 7 (The Feud with Jibril & Tossing Scripture Behind Backs)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 7: FEUD WITH JIBRIL & REJECTION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Absurd Enmity to Jibril, Divine War, Aayatin Bayyinat & Nabatha", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c1_x + c1_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=0.6)
    pdf.text("48:25 - 67:30", c1_x + c1_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    # Card 7A: Enmity to Jibril
    y_c = c1_y + c1_h - 50
    pdf.text("1. Pretext of Enmity: 'Qul Man Kana 'Aduwwal-li-Jibreel'", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Claimed Jibril brings warfare/hardship, while Mika'il brings rain, so they rejected Jibril.\n"
        "- God's rebuttal: Jibril brought revelation upon the Prophet's heart solely by Allah's permission.\n"
        "- The Qur'an confirms past scriptures and brings guidance and glad tidings to true believers."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 7B: God is the Enemy of Deniers
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Unity of Heavenly Assembly: Enmity with Jibril is Kufr", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Man kana 'aduwwal-lillahi wa mala'ikatihi... fa-innallaha 'aduwwul-lil-kafireen'.\n"
        "- Enmity toward one angel or messenger severs connection with the entire divine order.\n"
        "- Refutes pagan and sectarian mythologies portraying angels in cosmic rivalry against each other."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 7C: Clear Proofs (Bayyinat)
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Flawless Text & Messenger Character (Aayatin Bayyinat)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Wa laqad anzalna ilayka aayatin bayyinat': Undeniable signs combining message and messenger.\n"
        "- Flawless Quranic wisdom united with the unblemished character of the Prophet (peace be upon him).\n"
        "- 'Wa ma yakfuru biha illal-fasiqoon': Only the inherently corrupt and defiant reject it."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 7D: Tossing Scripture Like Trash
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Tossing Scripture Behind Backs (Nabadha)", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Nabadha' (Root N-B-Dh): Discarding something precious with contempt, treating it as trash.\n"
        "- 'Wara'a zuhoorihim ka'annahum la ya'lamoon': Threw God's Book behind their backs, playing dumb.\n"
        "- Abandoning scripture left a spiritual vacuum that was quickly filled by occult deception."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Center Gap Connector Bridge
    pdf.line(c1_x + c1_w, bridge_y, c2_x, bridge_y, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(w/2 - 12, bridge_y - 8, 24, 16, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=0.8)
    pdf.text_centered("->", w/2, bridge_y + 3, font="F2", size=7, rgb=GOLD_LIGHT)

    # Column 2: Pillar 8 (Solomon's Vindication & Babylonian Magic)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 8: SOLOMON & BABYLONIAN OCCULT", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Exonerating Solomon, Devils' Sorcery, Harut & Marut Trial", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c2_x + c2_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=0.6)
    pdf.text("67:31 - 90:35", c2_x + c2_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    # Card 8A: Vindication of Solomon
    y_c = c1_y + c1_h - 50
    pdf.text("1. Exonerating Solomon: 'Wa Ma Kafara Sulayman'", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Replaced abandoned scripture with occult lore devils recited during Solomon's reign.\n"
        "- Vindicating Solomon: 'Wa ma kafara Sulaymanu wa lakinnash-shayateena kafaroo'.\n"
        "- Refutes biblical slanders that Solomon fell into witchcraft; the devils committed disbelief."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 8B: Harut & Marut Trial
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. The Trial of Harut & Marut in Babylon (Babil)", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Two angels sent to Babylon as an overt trial (Fitnah) for human free will.\n"
        "- Warned every applicant: 'Innama nahnu fitnatun fa-la takfur' (We are only a test; do not disbelieve!).\n"
        "- Learning and practicing black magic constitutes an explicit act of Kufr."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 8C: Severing Spouses & Zero Inherent Harm
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Dividing Spouses & Divine Sovereignty (Illa bi-Idhnillah)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Learned spells to sever the bond between husband and wife (Baynal-mar'i wa zawjih).\n"
        "- 'Wa ma hum bi-daarrina bihi min ahadin illa bi-idhnillah': Zero independent harm.\n"
        "- Magic and talismans possess no autonomous power; harm occurs only if permitted by Allah."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 8D: Forfeiting the Hereafter
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Total Forfeiture of the Akhirah (Ma Lahoo Min Khalaq)", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Wa yata'allamoona ma yadurruhum wa la yanfa'uhum': Learning what destroys their own souls.\n"
        "- 'Wa laqad 'alimoo la-manish-tarahu ma lahoo fil-akhirati min khalaq': Zero share in the Hereafter.\n"
        "- Warning against amulets, fortune-telling, and dark arts: reliance belongs solely to Allah."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Save Master PDF
    os.makedirs(BASE_DIR, exist_ok=True)
    pdf.save(OUTPUT_PDF)
    print(f"[OK] Master Landscape PDF compiled successfully: {OUTPUT_PDF}")

if __name__ == "__main__":
    build_part05_pdf()
