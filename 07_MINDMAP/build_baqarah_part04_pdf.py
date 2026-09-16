#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Baqarah Part 4 Master Landscape Mindmap PDF Compiler
Foundation Media: Part 4 Audio Lecture (Duration: 01:46:49)
Strict Standardization:
- Title: Surah Al-Baqarah — Part 4
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
OUTPUT_PDF = os.path.join(BASE_DIR, "BAQARAH_PART_04_MINDMAP.pdf")

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

def build_part04_pdf():
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
        pdf.text(f"FOUNDATION MEDIA: PART 4 ({time_badge})", w - 282, h - 20, font="F2", size=6.8, rgb=EMERALD)
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
    # PAGE 1: THE PETRIFICATION OF HEARTS & NATURE'S SUBLIME HUMILITY
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 4,
        "THE PETRIFICATION OF HEARTS & NATURE'S SUBLIME HUMILITY",
        "Pillars 1 & 2: Witnessing miracles yet hardening, the anatomy of Qaswah, and three classes of stone",
        "PART 4 : SECTION 1",
        "00:00 - 24:30"
    )

    # Column 1: Pillar 1 (The Anatomy of Spiritual Petrification)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 1: ANATOMY OF SPIRITUAL PETRIFICATION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.2, rgb=CYAN)
    pdf.text("Hardening After Miracles, Root Q-S-W & Inorganic Rigidity", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c1_x + c1_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=0.6)
    pdf.text("00:00 - 12:15", c1_x + c1_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    # Card 1A: Hardening After Clear Miracles
    y_c = c1_y + c1_h - 50
    pdf.text("1. Hardening After Miracles (Thumma Qasat Quloobukum)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Witnessed the parted sea, the hoisted mountain, and the dead revived by the heifer's flesh.\n"
        "- Miracles alone cannot create faith without humility; when pride persists, the heart calcifies.\n"
        "- Time-distance and routine familiarity with sacred texts breed dangerous spiritual complacency."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 1B: Lexical Root Q-S-W
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Lexical Anatomy of Qaswah: Desiccated Rigidity", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Root Q-S-W: Physical petrification, drying up of all moisture, and total loss of elasticity.\n"
        "- Applied to the soul: Inability to be moved by divine admonition, grief of others, or fear of God.\n"
        "- The spiritual heart hardens like untreated leather left under scorching desert sun."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 1C: Harder Than Rock
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Harder Than Mineral Bedrock (Fa-hiya Kal-Hijarah)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Inanimate stones lack free will yet remain responsive to the universal laws of their Creator.\n"
        "- Corrupted human hearts possess intellect, conscience, and revelation yet actively rebel.\n"
        "- Willful moral obstinacy sinks human consciousness lower than inorganic minerals."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 1D: Divine Watchfulness
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Divine Watchfulness: 'Wa Mallahu Bi-Ghafilin'", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Wa mallahu bi-ghafilin 'amma ta'maloon': Divine justice never slumbers or overlooks crimes.\n"
        "- Delays in worldly retribution are divine respite, not evidence of divine indifference.\n"
        "- Taqwa requires active, vigilant awareness that the heart's secret petrification is audited."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Center Gap Connector Bridge
    pdf.line(c1_x + c1_w, bridge_y, c2_x, bridge_y, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(w/2 - 12, bridge_y - 8, 24, 16, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=0.8)
    pdf.text_centered("->", w/2, bridge_y + 3, font="F2", size=7, rgb=GOLD_LIGHT)

    # Column 2: Pillar 2 (Nature's Three Stones & Cosmic Humility)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 2: THREE STONES & COSMIC SUBMISSION", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.2, rgb=EMERALD)
    pdf.text("Gushing Rivers, Trickling Fissures & Mountain Cliffs Trembling", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c2_x + c2_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=0.6)
    pdf.text("12:16 - 24:30", c2_x + c2_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    # Card 2A: Gushing Rivers
    y_c = c1_y + c1_h - 50
    pdf.text("1. First Class: Gushing Rivers (Yatafajjaru Minhul-Anhar)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Massive boulders fracturing wide to unleash surging, abundant rivers of fresh water.\n"
        "- Metaphor for grand public benefit: souls that pour forth continuous knowledge and mercy.\n"
        "- Inanimate matter yielding life-giving sustenance, shaming human hearts that withhold charity."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 2B: Fissures of Mercy
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Second Class: Splitting Fissures (Yash-shaqqaqu)", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Rocks cracking under pressure, allowing humble trickles of moisture to emerge quietly.\n"
        "- Reflects modest internal softening: even small sincerity eventually breaks through rigidity.\n"
        "- The quiet tear shed in solitary repentance mirrors the hidden stream seeping from stone."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 2C: Plunging in Awe
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Third Class: Tumbling in Awe (Min Khashyatillah)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Gigantic boulders hurtling down mountain cliffs in literal, humble submission to Allah.\n"
        "- Classical tafsir affirms true cosmic consciousness: all physical nature reveres its Creator.\n"
        "- Creation prostrates while arrogant humans proudly resist divine guidance."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 2D: Curing Cynicism
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Curing Cynicism: Transforming the Rocky Heart", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- The disease of scholarly desensitization: analyzing scripture intellectually without being moved.\n"
        "- Stones shatter in awe of Allah; believers must soften hearts through constant Quranic reflection.\n"
        "- Consistent Tadabbur, secret tears of Tawbah, and serving the vulnerable melt callousness."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 2: EPISTEMOLOGICAL TREACHERY & MEDINAN DUPLICITY
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 4,
        "EPISTEMOLOGICAL TREACHERY & MEDINAN DUPLICITY",
        "Pillars 3 & 4: The eagerness of believers, calculated Tahreef, bifurcated discourse, and divine omniscience",
        "PART 4 : SECTION 2",
        "24:31 - 49:15"
    )

    # Column 1: Pillar 3 (The Reality of Calculated Distortion)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 3: CALCULATED SCRIPTURAL DISTORTION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.2, rgb=CYAN)
    pdf.text("Reorienting Eager Faith, Root H-R-F & Treason After Comprehension", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c1_x + c1_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=0.6)
    pdf.text("24:31 - 36:50", c1_x + c1_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    # Card 1A: Reorienting the Longing of Believers
    y_c = c1_y + c1_h - 50
    pdf.text("1. Reorienting Eager Faith (A-fatatma'oona An Yu'minoo)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Eager Sahabah in Medina hoped Jewish scholars would readily embrace Islam due to shared legacy.\n"
        "- Allah consoles the Prophet and believers: sincere faith cannot be forced upon political rivals.\n"
        "- Monotheistic heritage is no guarantee of humility; vested interests often blind the learned."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 1B: The Corrupt Clerical Faction
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. The Scholarly Faction (Fareequn Minhum)", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Fareequn minhum': Qur'anic fairness specifies an intellectual clique, not every single adherent.\n"
        "- Islam prohibits blanket communal demonization; righteous, truth-seeking individuals exist.\n"
        "- The critique targets the rabbinic leadership that weaponized religious authority for power."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 1C: The Anatomy of Tahreef
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. The Anatomy of Tahreef: 'Min Ba'di Ma 'Aqalooh'", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Root H-R-F: Dislocating phrases from their rightful contexts and corrupting original statutes.\n"
        "- Committed *min ba'di ma 'aqalooh*: After comprehensive cognitive grasp and grammatical mastery.\n"
        "- *Wa hum ya'lamoon*: Full moral and legal awareness; calculated treason rather than innocent error."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 1D: Trading Revelation for Hegemony
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Weaponizing Sacred Trusts for Secular Dominance", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Revelation is an eternal criterion; corrupt hierarchies treated it as transactional currency.\n"
        "- Twisting divine texts to please ruling patrons and safeguard prestigious institutional stipends.\n"
        "- Modern warning: Twisting Islamic edicts to legitimize oppression or flatter cultural fads."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Center Gap Connector Bridge
    pdf.line(c1_x + c1_w, bridge_y, c2_x, bridge_y, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(w/2 - 12, bridge_y - 8, 24, 16, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=0.8)
    pdf.text_centered("->", w/2, bridge_y + 3, font="F2", size=7, rgb=GOLD_LIGHT)

    # Column 2: Pillar 4 (Dual Faces & Behind Closed Doors)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 4: MEDINAN DUPLICITY & DIVINE AUDIT", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.2, rgb=EMERALD)
    pdf.text("Public Flattery, Secret Caucuses & Divine Omniscience", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c2_x + c2_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=0.6)
    pdf.text("36:51 - 49:15", c2_x + c2_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    # Card 2A: Public Flattery
    y_c = c1_y + c1_h - 50
    pdf.text("1. Public Flattery: 'Idha Laqul-Ladheena Amano'", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Facing believers in public, they feigned agreement: 'We believe your prophet matches our books.'\n"
        "- Political expediency: Maintaining peaceful trade alliances while concealing theological truth.\n"
        "- The cowardice of double-dealing: smiling before allies while planning subversion in private."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 2B: The Secret Caucus
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. The Secret Caucus: 'Li-Yuhajjookum Bihee'", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Behind closed doors, senior clerics scolded: 'Why tell them what God revealed to you?'\n"
        "- Terrified that Muslims would cite Torah prophecies of the Prophet as evidence before Allah!\n"
        "- Absurd theology: Imagining that withholding facts from humans prevents God from judging them."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 2C: Inversion of Intellect
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Inversion of Intellect: 'A-fa-la Ta'qiloon?'", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Clerics reprimanded peers: 'Have you no intellect (A-fa-la ta'qiloon) to leak our secrets?'\n"
        "- Corrupted definition of 'wisdom': equating intelligence with cynical cover-ups and deception.\n"
        "- When spiritual orientation decays, speaking truth is mocked as naive and treasonous."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 2D: Divine Omniscience
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Divine Omniscience: 'Ya'lamu Ma Yusirroon'", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Awala ya'lamoona annallaha ya'lamu ma yusirroona wa ma yu'linoon': Complete divine surveillance.\n"
        "- Whispers plotted in subterranean council chambers are as loud to Allah as public declarations.\n"
        "- Hypocrisy is grounded in atheistic forgetfulness that Allah is the omniscient Lord of existence."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 3: LAY ILLITERACY, FORGERY CARTELS & ENCIRCLING SIN
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 4,
        "LAY ILLITERACY, FORGERY CARTELS & ENCIRCLING SIN",
        "Pillars 5 & 6: Scriptural illiteracy, fabricated scrolls for profit, the 40-day myth, and encircling sin",
        "PART 4 : SECTION 3",
        "49:16 - 78:40"
    )

    # Column 1: Pillar 5 (Lay Illiteracy & The Scribe Forgery Cartel)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 5: ILLITERACY & FORGERY CARTELS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.2, rgb=CYAN)
    pdf.text("The Curse of Amaniyy, Fabricating Texts & The Triple Curse of Wayl", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c1_x + c1_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=0.6)
    pdf.text("49:16 - 63:55", c1_x + c1_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    # Card 1A: Scriptural Illiteracy
    y_c = c1_y + c1_h - 50
    pdf.text("1. Scriptural Illiteracy: 'Wa Minhum Ummiyyoona'", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Ummiyyoona': Lay masses completely cut off from direct comprehension or study of the Book.\n"
        "- Incapable of evaluating religious claims independently; utterly dependent on clerical gatekeepers.\n"
        "- Religious illiteracy leaves communities helpless against theological exploitation and folklore."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 1B: The Tyranny of Amaniyy
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. The Delusion of Amaniyy: Wishful Folklore", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Illa amaniyya': Knowing scripture only as soothing myths, fairy tales, and wishful superstitions.\n"
        "- Also denotes mechanical rote recitation: chanting sacred words without understanding moral law.\n"
        "- 'Wa in hum illa yazunnoon': Living in a fog of unfounded conjecture and imaginary entitlement."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 1C: Forging Sacred Scrolls
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. The Scribe Forgery Cartel (Yaktuboonal-Kitaba)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Corrupt scribes authored treatises with their own hands, stamping them: 'Hadha min 'indillah.'\n"
        "- Inventing religious loopholes to justify illicit interests and absolve powerful benefactors.\n"
        "- Motivation: Selling divine revelation for 'Thamanan Qaleela' — fleeting material and political perks."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 1D: The Triple Curse of Wayl
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. The Triple Curse of Wayl (Doom Upon Commercializers)", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Curse 1: 'Fa-waylul-lilladheen' — Absolute doom upon the perpetrators who commercialize truth.\n"
        "- Curse 2: 'Fa-waylul-lahum mimma katabat aydihim' — Doom for the poisonous doctrines authored.\n"
        "- Curse 3: 'Wa waylul-lahum mimma yaksiboon' — Doom for every single dirham amassed through fraud."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Center Gap Connector Bridge
    pdf.line(c1_x + c1_w, bridge_y, c2_x, bridge_y, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(w/2 - 12, bridge_y - 8, 24, 16, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=0.8)
    pdf.text_centered("->", w/2, bridge_y + 3, font="F2", size=7, rgb=GOLD_LIGHT)

    # Column 2: Pillar 6 (The Exemption Fallacy & Soul-Encircling Sin)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 6: EXEMPTION MYTH & ENCIRCLING SIN", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.2, rgb=EMERALD)
    pdf.text("The 40-Day Delusion, Divine Cross-Examination & Ihatah Matrix", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c2_x + c2_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=0.6)
    pdf.text("63:56 - 78:40", c2_x + c2_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    # Card 2A: The 40-Day Hellfire Myth
    y_c = c1_y + c1_h - 50
    pdf.text("1. The Myth of Ethnic Immunity: 'Ayyaman Ma'doodah'", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Slogan: 'The Fire will never touch us except for a few numbered days' (claiming 40 or 7 days).\n"
        "- Tribal presumption that ancestry or denominational branding grants automatic salvation.\n"
        "- Trusting genealogical superiority while openly trampling the moral statutes of the covenant."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 2B: The Divine Cross-Examination
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. The Divine Interrogation: 'Attakhadhtum 'Ahdan'", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Qul attakhadhtum 'indallahi 'ahdan': Has Allah signed a binding exemption contract with you?\n"
        "- 'Am taqooloona 'alallahi ma la ta'lamoon': Or are you recklessly forging claims against God?\n"
        "- Divine justice is immutable; no nation holds an exclusive hereditary monopoly over salvation."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 2C: The Law of Encircling Sin
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. The Universal Law: 'Ahatat Bihee Khatee'atuh'", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Bala man kasaba sayyi'atan': The universal rule: active earning of deliberate, unrepented sin.\n"
        "- Root H-W-T (Ihatah): Sin completely surrounds and besieges the soul like an impenetrable wall.\n"
        "- When conscience is suffocated and light is extinguished, the unrepented soul enters eternal doom."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 2D: The Salvation Matrix
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. The Salvation Matrix: True Faith & Righteous Deeds", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Wal-ladheena amanoo wa 'amilus-salihati': The true companions of Paradise (Ashabul-Jannah).\n"
        "- Salvation is tied strictly to inward Tawhid and outward moral action, never tribal slogans.\n"
        "- Humility and repentance dismantle the fortress of sin before death seals the soul's account."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 4: THE UNIVERSAL MORAL COVENANT & SANCTITY OF LIFE
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 4,
        "THE UNIVERSAL MORAL COVENANT & SANCTITY OF LIFE",
        "Pillars 7 & 8: The moral decalogue of Banu Isra'il, universal gracious speech, and outlawing fratricide",
        "PART 4 : SECTION 4",
        "78:41 - 106:49"
    )

    # Column 1: Pillar 7 (The Master Ethical Covenant)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 7: THE PRIMORDIAL MORAL COVENANT", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.2, rgb=CYAN)
    pdf.text("Monotheism, Filial Excellence, Shielding Orphans & Community Pillars", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c1_x + c1_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=0.6)
    pdf.text("78:41 - 92:45", c1_x + c1_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    # Card 1A: Pure Monotheism
    y_c = c1_y + c1_h - 50
    pdf.text("1. Monotheism as Root: 'La Ta'budoona Illallah'", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Master covenant begins with pure Tawhid: absolute devotion and submission to the Creator alone.\n"
        "- Syntactically framed as a factual imperative: worshipping Allah is existence's supreme reality.\n"
        "- Without pure monotheism, subsequent ethical and social duties lose their eternal anchor."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 1B: Filial Excellence
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Filial Excellence: 'Wa Bil-Walidayni Ihsana'", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Directly following Tawhid: commanding proactive *Ihsan* (devotion, beauty, dignity) to parents.\n"
        "- Transcends cold legal duty; requires gentle speech, financial support, and compassionate care.\n"
        "- Honoring mother and father is the foundational bedrock of all societal health and continuity."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 1C: Protecting the Vulnerable
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Concentric Duty: Kin, Orphans & Destitute", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Concentric circles of care: near kin (*Dhil-qurba*), fatherless orphans (*Al-yatama*).\n"
        "- *Al-Masakeen*: The economically broken whose income cannot meet essential basic human needs.\n"
        "- A civilization's spiritual legitimacy is measured by how it protects its most vulnerable tiers."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 1D: Salah & Zakah Community
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Institutional Anchors: Salah & Zakah", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Aqimus-Salata wa atoowaz-Zakah': Vertical communion with God paired with wealth distribution.\n"
        "- Prayer restrains inner indecency; Zakah cleanses communal greed, poverty, and social resentment.\n"
        "- Historical failure: 'Thumma tawallaytum' — Turning away in arrogance, except a steadfast few."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Center Gap Connector Bridge
    pdf.line(c1_x + c1_w, bridge_y, c2_x, bridge_y, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(w/2 - 12, bridge_y - 8, 24, 16, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=0.8)
    pdf.text_centered("->", w/2, bridge_y + 3, font="F2", size=7, rgb=GOLD_LIGHT)

    # Column 2: Pillar 8 (Universal Gracious Speech & The Sanctity of Life)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 8: UNIVERSAL CIVILITY & SANCTITY OF LIFE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.2, rgb=EMERALD)
    pdf.text("Gracious Speech to All Mankind, Outlawing Fratricide & Exile", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c2_x + c2_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=0.6)
    pdf.text("92:46 - 106:49", c2_x + c2_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    # Card 2A: Universal Civility in Speech
    y_c = c1_y + c1_h - 50
    pdf.text("1. Universal Gracious Speech: 'Qooloo Lin-Nasi Husna'", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Lin-nas': Universal scope commanding courtesy, gentleness, and beauty in speech to ALL people.\n"
        "- Forbids sectarian vitriol, caustic insults, condescension, or bigotry toward any human being.\n"
        "- Classical tafsir: Speaking good includes enjoining justice, smiling, and respecting human dignity."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 2B: The Sanctity of Human Blood
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Sanctity of Blood: 'La Tasfikoona Dima'akum'", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Do not shed your own blood': The Qur'an equates killing a brother with slaying oneself.\n"
        "- Human beings share a single ontological origin; violating life strikes at all humanity.\n"
        "- Shedding innocent blood for tribal glory or territory is a fatal breach of the sacred covenant."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 2C: Outlawing Eviction
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Outlawing Eviction: 'La Tukhrijoona Anfusakum'", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Do not evict yourselves from your homes': Forcible displacement is condemned alongside murder.\n"
        "- Expelling families and rendering brethren homeless creates intergenerational trauma and ruin.\n"
        "- Uprooting human beings from their land violates divine law and dissolves societal cohesion."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 2D: The Ratified Witness
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. The Ratified Witness: 'Thumma Aqrartum'", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Thumma aqrartum wa antum tash-hadoon': Solemnly ratified and witnessed by generations.\n"
        "- Breaching ratified moral duties while claiming religious pedigree is deliberate hypocrisy.\n"
        "- True religion requires living integrity: uniting worship of God with universal mercy to humanity."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Write output
    pdf.save(OUTPUT_PDF)
    print(f"[OK] Generated: {OUTPUT_PDF} ({len(pdf.pages)} pages, {os.path.getsize(OUTPUT_PDF)} bytes)")

if __name__ == "__main__":
    build_part04_pdf()
