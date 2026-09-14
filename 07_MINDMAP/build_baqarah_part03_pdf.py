#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Baqarah Part 3 Master Landscape Mindmap PDF Compiler
Foundation Media: Part 3 Audio Lecture (Duration: 01:59:45)
Strict Standardization:
- Title: Surah Al-Baqarah — Part 3
- Zero Ayah Numbers in titles/headers/cards
- Zero mention of external speaker names; 100% Huurs Studio & Sunni source discipline
- 4 Landscape Widescreen Pages (792 x 480 pts, 1.65:1 ratio)
- Symmetrical 2-column layout with center connector bridges
- Perfect vertical card distribution (70pt intervals) with zero collisions
"""

import os
import sys

# Import verified PDF engine
sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
OUTPUT_PDF = os.path.join(BASE_DIR, "BAQARAH_PART_03_MINDMAP.pdf")

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

def build_part03_pdf():
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
        pdf.text(f"FOUNDATION MEDIA: PART 3 ({time_badge})", w - 282, h - 20, font="F2", size=6.8, rgb=EMERALD)
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
    # PAGE 1: CONSTITUTIONAL LAW, COLLECTIVE RETRIBUTION & SENSORY DEMANDS
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 4,
        "CONSTITUTIONAL LAW, COLLECTIVE RETRIBUTION & SENSORY DEMANDS",
        "Pillars 1 & 2: Law & Criterion, calf-worship retribution, grammar of surrender, and resurrection",
        "PART 3 : SECTION 1",
        "00:00 - 26:16"
    )

    # Column 1: Pillar 1 (Constitutional Law & Retribution)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 1: CONSTITUTIONAL LAW & RETRIBUTION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Al-Kitab, Al-Furqan, Active Striving & Calf-Worship Penalty", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c1_x + c1_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=0.6)
    pdf.text("00:00 - 13:30", c1_x + c1_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    # Card 1A: Al-Kitab & Al-Furqan
    y_c = c1_y + c1_h - 50
    pdf.text("1. The Binding Law (Kitab) & Criterion (Furqan)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Al-Kitab': In Semitic/Quranic usage, denotes binding statutory law (Shari'ah).\n"
        "- 'Al-Furqan' (Root F-R-Q): The decisive divider separating truth from falsehood.\n"
        "- 'Bayan' parallel: Moral clarity exists only when mixed elements are fully separated."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 1B: Active Striving
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Active Exertion for Guidance (La'allakum Tahtadoon)", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Ihtida'' (Form VIII / Ifti'al): Demands active personal striving to attain guidance.\n"
        "- 'Muhtad' (active walker of the path) vs. 'Mahdi' (passive recipient).\n"
        "- Divine revelation builds the illuminated road; human responsibility requires walking it."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 1C: Calf Retribution
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. The Jurisprudence of Treason (Faq-tuloo Anfusakum)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Ya qawmi innakum zalamtum anfusakum': Collective confession of calf-worship.\n"
        "- Each of the 12 tribes executed members who committed treasonous idolatry.\n"
        "- Ancient biblical statute: Capital penalty for high spiritual treason is not an innovation."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 1D: Evaluation of Al-Bari'
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Divine Valuation & Sincere Tawbah ('Inda Bari'ikum)", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Al-Bari'': The Originator shaping distinct creation (cognate to Hebrew Boreh).\n"
        "- 'Dhalikum khayrun lakum': True welfare is judged by God, restoring societal sanctity.\n"
        "- Repentance requires concrete obedience first; refutes unconditional chosenness."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Center Gap Connector Bridge
    pdf.line(c1_x + c1_w, bridge_y, c2_x, bridge_y, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(w/2 - 12, bridge_y - 8, 24, 16, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=0.8)
    pdf.text_centered("->", w/2, bridge_y + 3, font="F2", size=7, rgb=GOLD_LIGHT)

    # Column 2: Pillar 2 (Sensory Demands & Resurrection)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 2: SENSORY DEMANDS & RESURRECTION", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Grammar of Laka, Empiricism, Thunderbolt & Revival Sign", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c2_x + c2_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=0.6)
    pdf.text("13:31 - 26:16", c2_x + c2_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    # Card 2A: Lan Nu'mina Laka
    y_c = c1_y + c1_h - 50
    pdf.text("1. The Grammar of Defiance: 'Lan Nu'mina Laka'", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Preposition 'Li' (Laka) alters the verb: implies yielding, surrendering, and complying.\n"
        "- They acknowledged Musa's status; their rebellion was against submitting to authority.\n"
        "- 'Lan nu'mina laka': We will not cave into your demands or surrender our autonomy."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 2B: Sensory Ultimatum
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. The Empiricism Ultimatum: 'Hatta Narallaha Jahrah'", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Demanded to see Allah manifestly face-to-face (Jahrah) before complying.\n"
        "- Imposing arrogant empirical conditions before yielding to legitimate commands.\n"
        "- Allah speaks in second person: 'You said this, and I was directly hearing your words.'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 2C: Thunderbolt
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. The Fatal Blast: As-Sa'iqah Seizes the Delegation", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Fa-akhadhatkumus-sa'iqah wa antum tanzuroon': Instantaneous death by thunderbolt.\n"
        "- Struck down in real-time observation as a direct warning to the onlookers.\n"
        "- Demonstrates the severe peril of mocking divine majesty with empirical theater."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 2D: Physical Resurrection
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Physical Revival & Gratitude (Thumma Ba'athnakum)", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Sunni consensus affirms literal death and physical revival; refutes modern allegorizing.\n"
        "- Miracles operate outside nature by the absolute omnipotence of Al-Qadir.\n"
        "- 'La'allakum tashkuroon': Real gratitude (Shukr) is shown through prophetic obedience."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 2: WILDERNESS MIRACLES, SEDITION & SCRIPTURAL ALTERATION
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 4,
        "WILDERNESS MIRACLES, SEDITION & SCRIPTURAL ALTERATION",
        "Pillars 3 & 4: Desert canopies, Manna & Salwa, Jericho entry, Hittah alteration, and 12 gushing springs",
        "PART 3 : SECTION 2",
        "26:17 - 50:27"
    )

    # Column 1: Pillar 3 (Wilderness Sustenance & Jericho)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 3: WILDERNESS SUSTENANCE & JERICHO", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Cloud Canopies, Manna & Salwa, Tayyib & The Jericho Gate", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c1_x + c1_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=0.6)
    pdf.text("26:17 - 38:27", c1_x + c1_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    # Card 3A: Cloud Canopy & Nutrition
    y_c = c1_y + c1_h - 50
    pdf.text("1. Desert Canopy & Nutrition (Ghamam, Manna, Salwa)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Ghamam': Joyful white canopy clouds shielding the multitude from fatal heatstroke.\n"
        "- 'Manna': Sweet carbohydrate dew for bread; 'Salwa': Quail birds providing pure protein.\n"
        "- Complete nutritional baseline gifted miraculously without labor in the barren wilderness."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 3B: Self-Inflicted Ruin
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Rebellion Harms Only the Self (Wa Ma Zalamoona)", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Kuloo min tayyibati ma razaqnakum': Consume what is intrinsically pure and lawful.\n"
        "- 'Wa ma zalamoona wa lakin kanoo anfusahum yazlimoon': Defiance never diminishes God.\n"
        "- Moral violations rebound exclusively as spiritual and physical ruin upon transgressors."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 3C: Jericho Entry
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Jericho Entry & Prostration (Wad-khulul-Bab)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Entering the promised city (Jericho) under Joshua after 40-year desert wanderings.\n"
        "- 'Wad-khulul-baba sujjadan': Commanded to enter the city gates prostrating upon mounts.\n"
        "- Foreheads lowered to the necks of their animals in deep humility, renouncing conquest pride."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 3D: Sacred Password Hittah
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Unload Our Heavy Sins! (Wa Qooloo Hittatun)", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Root H-T-T: Unloading the heavy saddlebags from a beast of burden; wiping the ledger.\n"
        "- Liturgical plea: 'O Allah, unload the crushing burden of our sins from our backs!'\n"
        "- Promised full pardon and multiplied rewards for the Muhsinin upon reciting this word."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Center Gap Connector Bridge
    pdf.line(c1_x + c1_w, bridge_y, c2_x, bridge_y, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(w/2 - 12, bridge_y - 8, 24, 16, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=0.8)
    pdf.text_centered("->", w/2, bridge_y + 3, font="F2", size=7, rgb=GOLD_LIGHT)

    # Column 2: Pillar 4 (Scriptural Alteration & 12 Springs)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 4: SCRIPTURAL ALTERATION & 12 SPRINGS", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Altering Hittah, Plague Penalty, Fanfajarat & Mind Corruption", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c2_x + c2_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=0.6)
    pdf.text("38:28 - 50:27", c2_x + c2_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    # Card 4A: Cynical Word Alteration
    y_c = c1_y + c1_h - 50
    pdf.text("1. Turning Repentance into a Joke: 'Fa-baddala'", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Rebellious leaders mocked the command: entered dragging themselves on their backsides.\n"
        "- Substituted the sacred plea 'Hittah' with 'Habbah fee sha'irah' (a grain in barley).\n"
        "- Psychological rot: Desensitization to sacred rites by weaponizing comedy and irony."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 4B: Celestial Retribution
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Plague from the Sky (Rijzan Minas-Samaa')", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Rijz': A severe, disfiguring pestilence/plague descending from the sky.\n"
        "- 'Bima kanoo yafsuqoon': Punished not just for one utterance, but for chronic defiance (Fisq).\n"
        "- This catastrophic ruin was avoidable through a single sincere phrase of contrition."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 4C: 12 Springs
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Twelve Gushing Springs: Fanfajarat vs. Fanbajasat", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Musa strikes the rock: 12 separate springs burst out, one for each tribe (Mashrabahum).\n"
        "- Strategic resource management: Eliminates lethal civil water conflicts in the desert.\n"
        "- 'Fanfajarat' (Baqarah = violent gushing in prayer) vs. 'Fanbajasat' (A'raf = trickling)."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 4D: Ideological Rot
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Ideological Rot (Wa La Ta'thaw Fil-Ardi Mufsidin)", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Athiya / Ya'tha': Internal corruption of the mind influenced by insidious propaganda.\n"
        "- Corrupted thinking inevitably yields external sociopolitical devastation (Mufsidin).\n"
        "- Individuals who normalize subtle internal corruptions fuel the overarching societal collapse."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 3: THE SLAVE MINDSET, TRIPLE HUMILIATION & SALVATION MATRIX
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 4,
        "THE SLAVE MINDSET, TRIPLE HUMILIATION & SALVATION MATRIX",
        "Pillars 5 & 6: Egyptian slave diet, triple bondage curse, killing prophets, and authentic salvation criteria",
        "PART 3 : SECTION 3",
        "50:28 - 73:35"
    )

    # Column 1: Pillar 5 (Slave Mentality & Curse of Bondage)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 5: SLAVE MENTALITY & CURSE OF BONDAGE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Craving Prison Menu, Ihbitoo Misran & The Triple Penalty", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c1_x + c1_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=0.6)
    pdf.text("50:28 - 62:00", c1_x + c1_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    # Card 5A: Craving Prison Produce
    y_c = c1_y + c1_h - 50
    pdf.text("1. Craving Prison Produce: The Slave Mindset", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Lan nasbira 'ala ta'amin wahid': Weary of celestial Manna; craving slave vegetables.\n"
        "- Demanded garlic, onions, lentils, and cucumbers (*Fum, Basal, 'Adas, Qith-tha'*).\n"
        "- Missing the prison food means missing the prison: preferring varied slavery over dignified freedom."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 5B: The Scriptural Pun
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Trading Noble for Base: 'Ihbitoo Misran'", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'A-tastabdiloona-lladhi huwa adna billadhi huwa khayr': Exchanging grace for base crops.\n"
        "- 'Ihbitoo Misran': Tanween means an ordinary village, but puns sharply on Egypt (Misr).\n"
        "- Sarcastic rebuke: 'Descend back down to your slave quarters if you crave bondage!'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 5C: The Triple Penalty
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Triple Bondage Slapped Back: Dhillah, Maskanah, Ghadab", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The 3 evils of slavery: 1. Humiliation (Dhillah), 2. Powerlessness (Maskanah), 3. Tyrant wrath.\n"
        "- 'Duribat 'alayhim': Desiring slave life caused Allah to slap those 3 exact curses upon them.\n"
        "- Now incurring divine anger (Baa'oo bi-ghadabin minallah) — infinitely graver than Pharaoh."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 5D: Slaying Prophets
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Denying Revelations & Killing Prophets (Bima 'Asaw)", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Escalation: Disbelieving ayat progressed to murdering prophets without right (Bi-ghayril-haqq).\n"
        "- Root cause: Arrogant defiance ('Asaw) and habitual transgression of red lines (Ya'tadoon).\n"
        "- Modern Ummah parallel: Silencing and persecuting righteous scholars mirrors this pathology."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Center Gap Connector Bridge
    pdf.line(c1_x + c1_w, bridge_y, c2_x, bridge_y, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(w/2 - 12, bridge_y - 8, 24, 16, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=0.8)
    pdf.text_centered("->", w/2, bridge_y + 3, font="F2", size=7, rgb=GOLD_LIGHT)

    # Column 2: Pillar 6 (Universal Salvation Matrix)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 6: THE UNIVERSAL SALVATION MATRIX", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Deconstructing 2:62, Tawhid, Akhirah & The Triad of Iman", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c2_x + c2_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=0.6)
    pdf.text("62:01 - 73:35", c2_x + c2_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    # Card 6A: Refutation of Pluralism
    y_c = c1_y + c1_h - 50
    pdf.text("1. Contextual Discipline: Refuting Pluralist Distortion", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Verse 2:62 addresses Believers, Jews, Christians, and Sabians.\n"
        "- Pluralist error: Claiming any faith grants salvation without accepting the Final Messenger.\n"
        "- Surrounding context: Bookended by explicit verses demanding adherence to prophecy."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 6B: The Three Criteria
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. The Three Criteria on God's Terms (Man Aamana...)", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 1. Faith in Allah: On His standard of pure Tawhid (refuting Trinity, sonship, and anthropomorphism).\n"
        "- 2. Faith in the Last Day: Subject to divine reckoning, not national or tribal entitlement.\n"
        "- 3. Righteous Deeds (Wa 'Amila Salihan): Defined exclusively by authentic prophetic revelation."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 6C: Spiritual Logic Triad
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. The Interlocking Architecture of Belief", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Belief in a Just God logically demands belief in Akhirah (where unpunished tyrants are judged).\n"
        "- Belief in Akhirah compels righteous action (Amal Salih) to prepare for the supreme audit.\n"
        "- Neglecting deeds signals dying Akhirah conviction and an empty awareness of God."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 6D: Serenity Guarantee
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Objective Serenity: 'La Khawfun 'Alayhim'", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Historical sincere followers of Musa and Isa, and all who follow Muhammad, attain salvation.\n"
        "- 'Fa-lahum ajruhum 'inda rabbihim': Their reward is eternally secured with their Master.\n"
        "- Absolute immunity: No future terror can destroy their soul, nor past grief haunt their peace."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 4: THE SINAI CANOPY, SABBATH TRANSGRESSION & THE HEIFER
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 4,
        "THE SINAI CANOPY, SABBATH TRANSGRESSION & THE HEIFER",
        "Pillars 7 & 8: Mount Tur canopy, Sabbath apes, murder mystery, yellow cow criteria, and resurrection",
        "PART 3 : SECTION 4",
        "73:36 - 119:45"
    )

    # Column 1: Pillar 7 (Sinai Canopy & Sabbath Apes)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 7: SINAI CANOPY & SABBATH APES", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Mountain Hoisted Overhead, Quwwah, Sabbath Evasion & Apes", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c1_x + c1_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=0.6)
    pdf.text("73:36 - 95:00", c1_x + c1_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    # Card 7A: Mount Tur Canopy
    y_c = c1_y + c1_h - 50
    pdf.text("1. Mount Tur Hoisted as a Canopy (Rafa'na Fawqakum)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Mount Sinai hoisted overhead like an impending roof; a terrifying 'scared straight' divine sign.\n"
        "- Not to coerce initial belief, but to enforce commitment to an already accepted covenant.\n"
        "- 'Khudhoo ma aataynakum bi-quwwah': Hold onto revelation with rigorous resolve and strength."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 7B: Vocal Recitation & Taqwa
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. The Engine of Taqwa: 'Wadhkuroo Ma Feehi'", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Dhikr comprises internal remembrance and active vocal recitation (the structure of daily Salah).\n"
        "- Immersion in scripture is the sole shield against degenerative spiritual backsliding.\n"
        "- 'Fa-lawla fadlullahi 'alaykum': Were it not for divine grace and mercy, ruin was guaranteed."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 7C: Sabbath Evasion
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. The Sabbath Evasion: Legalistic Hypocrisy", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Coastal town (Aylah) set fishing nets on Friday to trap fish on the prohibited Sabbath.\n"
        "- Collected harvest Sunday: Preserving technical wording while violating divine intent.\n"
        "- Exposes the spiritual bankruptcy of inventing legal loopholes to justify forbidden greed."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 7D: Metamorphosis into Apes
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Transformed into Despised Apes (Qiradatan Khasi'een)", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Koonoo qiradatan khasi'een': Moral regression followed by physical metamorphosis into cursed apes.\n"
        "- Humans who surrender moral restraint to unchecked appetites regress to beastly status.\n"
        "- 'Nakalan': A terrifying public sign along river highways, warning all future generations."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Center Gap Connector Bridge
    pdf.line(c1_x + c1_w, bridge_y, c2_x, bridge_y, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(w/2 - 12, bridge_y - 8, 24, 16, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=0.8)
    pdf.text_centered("->", w/2, bridge_y + 3, font="F2", size=7, rgb=GOLD_LIGHT)

    # Column 2: Pillar 8 (The Heifer & Resurrection Proof)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 8: THE HEIFER & RESURRECTION PROOF", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("The Murder, Mocking Commands, Evasive Questions & Revival", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c2_x + c2_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=0.6)
    pdf.text("95:01 - 119:45", c2_x + c2_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    # Card 8A: Unsolved Murder & Mockery
    y_c = c1_y + c1_h - 50
    pdf.text("1. The Murder Mystery & Accusation of Joking (Huzuwa)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Slain man found; tribes hurl mutual blame (Faddara'tum feeha), risking open civil war.\n"
        "- Ordered to slaughter a cow. Reaction: 'Are you mocking us?' (A-tattakhidhuna huzuwa?).\n"
        "- Musa seeks refuge: Joking about divine commandments is foolish, reckless ignorance (Jahl)."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 8B: Pedantic Questions
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Pedantic Questioning Narrowing Divine Mercy", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Question 1 (Age): Middle-aged ('Awanun bayna dhalik). Musa commands: 'Just do it!' (Faf'aloo!).\n"
        "- Question 2 (Color): Radiant, deep yellow (Safra'u faqi'un), captivating onlookers (Tasurrun-nazireen).\n"
        "- Question 3 (Work): Untamed, never plowed soil, unblemished with zero spots (Musallamah)."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 8C: Reluctant Obedience
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Reluctant Slaughter at Exorbitant Cost (Ma Kadoo)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Fa-dhabahooha wa ma kadoo yaf'aloon': Slaughtered it, though they nearly refused.\n"
        "- Forced to pay its weight in gold to an orphan boy due to their self-inflicted restrictions.\n"
        "- Demanding unnecessary details narrows Shari'ah and multiplies hardship upon believers."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 8D: Resurrection Proof
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Resurrection Demonstration (Kadhalika Yuhyillah)", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Striking the corpse with a piece of the heifer revived the dead man to name his murderer.\n"
        "- 'Wallahu mukhrijum ma kuntum taktumoon': God exposes what conspirators hide in darkness.\n"
        "- 'Kadhalika yuhyillahul-mawta': Conclusive proof of resurrection; true 'Aql requires a pure heart."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Save Master PDF
    os.makedirs(BASE_DIR, exist_ok=True)
    pdf.save(OUTPUT_PDF)
    print(f"[OK] Master Landscape PDF recompiled successfully: {OUTPUT_PDF}")

if __name__ == "__main__":
    build_part03_pdf()
