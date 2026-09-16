#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Baqarah Part 6 Master Landscape Mindmap PDF Compiler
Foundation Media: Part 6 Audio Lecture (Duration: 01:53:08)
Strict Standardization:
- Title: Surah Al-Baqarah — Part 6
- Zero Ayah Numbers in titles/headers/cards
- Zero mention of external speaker names; 100% Huurs Studio & Sunni source discipline
- ZERO AUDIO TIMESTAMPS anywhere on the mindmap (as mandated)
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
OUTPUT_PDF = os.path.join(BASE_DIR, "BAQARAH_PART_06_MINDMAP.pdf")

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

def build_part06_pdf():
    w, h = 792, 480 # Landscape ratio (1.65:1)
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        # Background
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH AL-BAQARAH", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
        # Foundation Media Badge (NO Timestamps)
        pdf.rect(w - 235, h - 32, 130, 20, fill_rgb=NAVY_ELEVATED, stroke_rgb=BORDER_MUTED, line_width=0.8)
        pdf.text("FOUNDATION MEDIA: PART 6", w - 225, h - 20, font="F2", size=7, rgb=EMERALD)
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
    # PAGE 1: LINGUISTIC HYGIENE, AMBUSH WORDS & DIVINE FAVOR
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 4,
        "LINGUISTIC HYGIENE, AMBUSH WORDS & DIVINE FAVOR",
        "Pillars 1 & 2: Eradicating covert mockery, the ethics of Unzurna, sectarian envy, and boundless grace",
        "PART 6 : SECTION 1"
    )

    # Column 1: Pillar 1 (Linguistic Ambush & Prophetic Veneration)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 1: LINGUISTIC AMBUSH & PROPHETIC ADAB", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.5, rgb=CYAN)
    pdf.text("Root R-'-Y, Phonetic Subterfuge & The Sacred Mandate of Unzurna", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    # Card 1A: The Ambush of Ra'ina
    y_c = c1_y + c1_h - 50
    pdf.text("1. The Ambush of Ra'ina (La Taqooloo Ra'ina)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Believers innocently said 'Ra'ina' meaning 'Consider our pace and grant us your attention.'\n"
        "- Opponents weaponized phonetic overlap with Hebrew 'Ra'' (evil) or 'Ru'oonah' (foolishness).\n"
        "- Feigning polite conversation while covertly insulting the Prophet (peace be upon him)."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 1B: The Mandate of Unzurna
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. The Mandate of Unzurna: Transparent Speech", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Replaced ambiguous phrasing with 'Unzurna' ('Look upon us with regard and patience').\n"
        "- Foundational legal rule of Sadd al-Dhara'i': Eliminating words enemies can distort.\n"
        "- Cultivating supreme linguistic hygiene and reverence in the presence of prophetic authority."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 1C: Attentive Listening
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Attentive Listening as Adab: 'Wasma'oo'", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Wasma'oo': Listen attentively; true reverence is active obedience rather than debate.\n"
        "- Shifting focus from interrupting discussions to absorbing divine guidance with humility.\n"
        "- Spiritual maturity begins when the ego ceases argumentative chatter and submits to truth."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 1D: Agonizing Penalty
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Penalty for Cynical Mockery: ''Adhabun Aleem'", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Wa lil-kafireena 'adhabun aleem': Severe torment awaits those who mock revelation.\n"
        "- Cloaking disrespect in linguistic ambiguity does not deceive the Knower of hidden secrets.\n"
        "- Cynical sarcasm directed at sacred guidance corrodes the heart and brings ruin."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Center Gap Connector Bridge
    pdf.line(c1_x + c1_w, bridge_y, c2_x, bridge_y, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(w/2 - 12, bridge_y - 8, 24, 16, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=0.8)
    pdf.text_centered("->", w/2, bridge_y + 3, font="F2", size=7, rgb=GOLD_LIGHT)

    # Column 2: Pillar 2 (Sectarian Envy & Divine Selection)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 2: SECTARIAN ENVY & DIVINE SELECTION", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.5, rgb=EMERALD)
    pdf.text("The Pathology of Hasad, Tribal Resentment & The Boundless Bounty", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    # Card 2A: The Pathology of Envy
    y_c = c1_y + c1_h - 50
    pdf.text("1. The Malice of Envy (Ma Yawaddul-Ladheena Kafaroo)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Hostile factions detested seeing any spiritual or communal blessing descend upon Muslims.\n"
        "- Root H-S-D (Hasad): Toxic craving that an unearned favor given to another be stripped away.\n"
        "- Tribal prejudice: Bitter that final prophethood emerged outside their ancestral clan."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 2B: Divine Selection
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Sovereign Selection: 'Yakhtassu Bi-Rahmatih'", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Wallahu yakhtassu bi-rahmatihi man yasha'': Allah grants His mercy to whomever He wills.\n"
        "- Divine revelation is an unmerited sovereign gift, never a hereditary family entitlement.\n"
        "- Human arrogance possesses zero power to restrict, dictate, or cancel divine appointments."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 2C: Boundless Bounty
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Boundless Bounty: 'Wallahu Dhul-Fadlil-'Azeem'", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Dhul-Fadlil-'Azeem': God's grace is infinite; enriching others depletes nothing from Him.\n"
        "- Resenting another's gift is an implicit protest against the supreme wisdom of the Provider.\n"
        "- Healing jealousy requires faith that Allah's celestial storehouses are eternally limitless."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 2D: Community Immunity
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Immunizing Believers: Serenity in Divine Will", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Believers must remain undaunted by external malice, smear campaigns, or online hostility.\n"
        "- When Allah decrees honor and guidance, no earthly plot or human envy can revoke it.\n"
        "- Spiritual security is achieved through grateful worship, personal piety, and total trust in God."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 2: PROGRESSIVE REVELATION & THE DANGER OF SKEPTICISM
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 4,
        "PROGRESSIVE REVELATION & THE DANGER OF SKEPTICISM",
        "Pillars 3 & 4: The pedagogy of Naskh, divine cosmic dominion, and the hazard of cynical demands",
        "PART 6 : SECTION 2"
    )

    # Column 1: Pillar 3 (The Pedagogy of Progressive Abrogation)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 3: THE PEDAGOGY OF PROGRESSIVE ABROGATION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.5, rgb=CYAN)
    pdf.text("Wisdom of Naskh, Legislative Maturation & Universal Sovereignty", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    # Card 3A: Divine Rationale of Naskh
    y_c = c1_y + c1_h - 50
    pdf.text("1. Divine Pedagogy of Naskh (Ma Nansakh Min Aayah)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Whatever verse We abrogate or cause to be forgotten, We bring what is better or like it.'\n"
        "- Naskh is not divine indecision; it is planned pedagogy adjusting laws to human capacity.\n"
        "- Just as a physician alters treatment during healing, divine law progresses toward perfection."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 3B: Sublime Replacement
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Sublime Replacement: 'Na'ti Bi-Khayrin Minha'", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Replacement brings greater legal ease, higher spiritual rewards, or communal resilience.\n"
        "- Demonstrates divine mercy: raising moral expectations as community faith strengthens.\n"
        "- The shifting of the Qiblah from Jerusalem to Makkah serves as the master test of obedience."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 3C: Absolute Omnipotence
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Absolute Omnipotence: ''Ala Kulli Shay'in Qadeer'", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Sceptics challenged changes in commands; Allah points to His unlimited cosmic authority.\n"
        "- 'Alam ta'lam annallaha 'ala kulli shay'in qadeer': God has absolute dominion over all affairs.\n"
        "- The Creator who commands celestial movements possesses total authority to govern statutes."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 3D: Universal Guardianship
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Cosmic Dominion & True Protector: 'Mulkus-Samawat'", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Lahoo mulkus-samawati wal-ard': To Him belongs the absolute kingdom of the universe.\n"
        "- 'Wa ma lakum min doonillahi min waliyyin': None can protect or aid outside of Allah.\n"
        "- Total reliance on the sovereign Lord liberates the soul from fear of hostile worldly powers."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Center Gap Connector Bridge
    pdf.line(c1_x + c1_w, bridge_y, c2_x, bridge_y, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(w/2 - 12, bridge_y - 8, 24, 16, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=0.8)
    pdf.text_centered("->", w/2, bridge_y + 3, font="F2", size=7, rgb=GOLD_LIGHT)

    # Column 2: Pillar 4 (The Danger of Cynical Inquiries)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 4: CYNICAL QUESTIONS & SKEPTICISM", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.5, rgb=EMERALD)
    pdf.text("Parallels with Israelite Demands, Bad-Faith Doubts & Sawa'as-Sabeel", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    # Card 4A: Rebuking Obstinate Inquiries
    y_c = c1_y + c1_h - 50
    pdf.text("1. Rebuking Bad-Faith Demands (Kama Su'ila Moosa)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Do you wish to interrogate your Messenger as Moses was interrogated before?'\n"
        "- Condemning pedantic, frivolous questions designed to delay obedience rather than seek clarity.\n"
        "- Demanding miraculous sensory shows reflects inner arrogance rather than genuine search for truth."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 4B: Trading Faith for Skepticism
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Trading Faith for Doubt: 'Yatabaddalil-Kufra'", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Wa man yatabaddalil-kufra bil-eeman': Exchanging faith for persistent cynical skepticism.\n"
        "- Chronic doubt is not intellectual courage; it is a spiritual paralysis that chokes conviction.\n"
        "- Constantly looking for excuses and theological loopholes slowly erodes faith from the heart."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 4C: Losing the Level Highway
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Straying from the Highway: 'Sawa'as-Sabeel'", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Faqad dalla sawa'as-sabeel': Strayed completely from the smooth, balanced middle highway.\n"
        "- True intellect inquires in order to implement, not to mock, procrastinate, or evade duties.\n"
        "- The straight path unites reverent inquiry with swift moral compliance upon recognizing truth."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 4D: Sincere Seeking vs Cynicism
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Sincere Inquiry vs Destructive Cynicism", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Islam warmly welcomes questions for learning ('Ask the people of knowledge if you know not').\n"
        "- The divide lies between the sincere seeker desiring light and the arrogant critic evading duty.\n"
        "- Theory without moral action only deepens spiritual confusion and cognitive dissonance."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 3: SECTARIAN SLOGANS, FORGIVENESS & THE SALVATION MATRIX
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 4,
        "SECTARIAN SLOGANS, FORGIVENESS & THE SALVATION MATRIX",
        "Pillars 5 & 6: Strategic forbearance, the myth of tribal salvation, and surrender with excellence",
        "PART 6 : SECTION 3"
    )

    # Column 1: Pillar 5 (Strategic Forbearance & Internal Resilience)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 5: STRATEGIC PATIENCE & RESILIENCE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.5, rgb=CYAN)
    pdf.text("Root H-S-D Unveiled, The Mandate of Fa'foo Wasfahoo & Community Pillars", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    # Card 5A: The Urge to Subvert Faith
    y_c = c1_y + c1_h - 50
    pdf.text("1. Malice to Subvert Faith: 'Law Yaruddoonakum'", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Factions actively plotted to revert Muslims to disbelief after experiencing illumination.\n"
        "- Driven purely by inner malice ('Hasadan min 'indi anfusihim') rather than theological logic.\n"
        "- Persisting in subversion even 'after the truth had become blindingly evident to them.'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 5B: Strategic Forbearance
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Strategic Forbearance: 'Fa'foo Wasfahoo'", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Fa'foo wasfahoo': Pardon provocations and overlook insults with dignified emotional mastery.\n"
        "- 'Hatta ya'tiyallahu bi-amrih': Endure with patience until Allah brings forth His decisive command.\n"
        "- Restraint is strategic strength: avoiding reactive squabbles while conserving communal energy."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 5C: Spiritual Infrastructure
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Institutional Anchors: Salah & Zakah", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Responding to external pressure through inner piety: 'Wa aqeemus-Salata wa atoowaz-Zakah.'\n"
        "- Salah deepens vertical connection with God; Zakah cements horizontal social solidarity.\n"
        "- The ultimate defense against cultural hostility is cultivating an ethically exemplary society."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 5D: Good Preserved with Allah
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Eternal Ledger: 'Tajidoohu 'Indallah'", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Whatever good you send forward for your souls, you will find it preserved with Allah.'\n"
        "- 'Innallaha bima ta'maloona baseer': God is intimately watchful of every sacrifice and tear.\n"
        "- No act of patient restraint, charity, or steadfast endurance is ever forgotten or wasted."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Center Gap Connector Bridge
    pdf.line(c1_x + c1_w, bridge_y, c2_x, bridge_y, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(w/2 - 12, bridge_y - 8, 24, 16, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=0.8)
    pdf.text_centered("->", w/2, bridge_y + 3, font="F2", size=7, rgb=GOLD_LIGHT)

    # Column 2: Pillar 6 (Dismantling Sectarian Monopolies)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 6: DISMANTLING SECTARIAN MONOPOLIES", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.5, rgb=EMERALD)
    pdf.text("The Exclusivist Slogan, Tilka Amaniyy & The Universal Matrix of Aslama", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    # Card 6A: Exclusive Slogans
    y_c = c1_y + c1_h - 50
    pdf.text("1. Slogans of Salvation Monopoly: 'Illa Man Kana'", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'None will enter Paradise unless they are a Jew or a Christian': Tribal claims on grace.\n"
        "- Reducing the boundless mercy of the Creator to a narrow hereditary club or political brand.\n"
        "- Assuming salvation is inherited by birth pedigree rather than earned through moral surrender."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 6B: Empty Wishful Thinking
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Delusions of Privilege: 'Tilka Amaniyyuhum'", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Tilka amaniyyuhum': Those claims are merely empty daydreams, wishful fantasies, and myths.\n"
        "- 'Qul hatoo burhanakum': 'Bring forward your verifiable proof if you are truthful!'\n"
        "- Theological assertions without scriptural or rational evidence possess zero standing with God."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 6C: The True Salvation Matrix
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. The Universal Salvation Matrix: 'Aslama Wajhahu'", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Bala man aslama wajhahoo lillahi wa huwa muhsin': The immutable criterion of salvation.\n"
        "- Criterion 1: 'Aslama wajhahu' — Total inward capitulation of intent, ego, and will to God alone.\n"
        "- Criterion 2: 'Wa huwa muhsin' — Outward excellence in righteous conduct and prophetic ethics."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 6D: Mutual Nullification
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Mutual Nullification & Serenity Guarantee", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Sectarian comedy: Jews claim Christians have no basis; Christians claim Jews have no basis!\n"
        "- Both recite scripture yet descend into mutual invalidation out of tribal chauvinism.\n"
        "- The reward of genuine surrender: 'No fear shall come upon them, nor shall they grieve.'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 4: SACRED SPACES, THE UNIVERSAL COUNTENANCE & COSMIC ORIGINATOR
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 4,
        "SACRED SPACES, THE UNIVERSAL COUNTENANCE & COSMIC ORIGINATOR",
        "Pillars 7 & 8: Barring places of worship, omnipresence of God, refuting paternity, and prophetic limits",
        "PART 6 : SECTION 4"
    )

    # Column 1: Pillar 7 (Sanctity of Mosques & Universal Sanctuary)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 7: SANCTITY OF MOSQUES & OMNIPRESENCE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.5, rgb=CYAN)
    pdf.text("The Crime of Desecration, Worldly Disgrace & The Universal Wajhullah", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    # Card 7A: Desecration of Mosques
    y_c = c1_y + c1_h - 50
    pdf.text("1. Supreme Tyranny: Barring Mosques (Wa Man Azlamu)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Who does greater wrong than one who prevents God's name from being mentioned in His mosques?'\n"
        "- 'Wa sa'a fee kharabiha': Striving actively for their physical destruction or spiritual ruin.\n"
        "- Blocking believers from prayer or vandalizing sacred sanctuaries is an unpardonable crime."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 7B: Worldly Disgrace & Great Torment
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Worldly Disgrace & Fierce Punishment: 'Khizyun'", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Desecrators forfeit peace: they should enter sanctuaries only in trembling trepidation.\n"
        "- Penalty 1: 'Lahum fid-dunya khizyun' — Public disgrace and humiliation in this worldly life.\n"
        "- Penalty 2: 'Wa lahum fil-akhirati 'adhabun 'azeem' — Immense judgment torment in the Hereafter."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 7C: East & West Belong to Allah
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Universal Sacred Space: 'Lillahil-Mashriq'", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Wa lillahil-mashriqu wal-maghrib': The entirety of celestial space belongs to Allah.\n"
        "- God is not confined to human walls; the whole earth was made a pure masjid for the Ummah.\n"
        "- Theological anchor preparing believers for the historical reorientation of the Qiblah."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 7D: The Ever-Present Countenance
    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Ever-Present Countenance: 'Fa-Thamma Wajhullah'", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Wherever you turn, there is the Countenance of Allah. Indeed, Allah is All-Encompassing.'\n"
        "- When tyrants bar physical buildings, the sincere heart connects with Allah anywhere on earth.\n"
        "- Spiritual sanctuary cannot be conquered: God is immediately present with every humble soul."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Center Gap Connector Bridge
    pdf.line(c1_x + c1_w, bridge_y, c2_x, bridge_y, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(w/2 - 12, bridge_y - 8, 24, 16, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=0.8)
    pdf.text_centered("->", w/2, bridge_y + 3, font="F2", size=7, rgb=GOLD_LIGHT)

    # Column 2: Pillar 8 (The Transcendent Originator & Prophetic Boundaries)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 8: TRANSCENDENT ORIGINATOR & PROPHETIC DUTY", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.5, rgb=EMERALD)
    pdf.text("Refuting Divine Paternity, Badee' Ex Nihilo, Kun Fa-yakoon & Basheer", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    # Card 8A: Refuting Divine Offspring
    y_c = c1_y + c1_h - 50
    pdf.text("1. Refuting Divine Offspring: 'Subhanahu'", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Rebutting anthropomorphic dogma: 'Allah has taken a son' — 'Subhanahu' (Transcendently pure!).\n"
        "- A child implies mortality, physical biology, and need; Allah is the Self-Sufficient Creator.\n"
        "- 'Bal lahoo ma fis-samawati wal-ard': Everything in heaven and earth is His created servant."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 8B: Cosmic Devotion
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Cosmic Devotion: 'Kullun Lahoo Qanitoon'", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Kullun lahoo qanitoon': All creation stands in devout, humble submission to His design.\n"
        "- Galaxies, atomic particles, and living cells obey the precise laws decreed by their Lord.\n"
        "- Arrogant humans who fabricate partners rebel against the unanimous cosmic consensus."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 8C: The Incomparable Originator
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Originator Ex Nihilo: 'Badee' & Kun Fa-Yakoon'", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Badee'us-samawati wal-ard': The Originator who creates from nothing without prior model.\n"
        "- 'Idha qada amran fa-innama yaqoolu lahoo Kun Fa-yakoon': Creation via effortless command.\n"
        "- God requires no tools, time, or assistance; reality manifests instantly at His sovereign word."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Card 8D: Prophetic Mission & Boundaries
    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Relieving the Prophet: 'Basheeran Wa Nadheera'", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'We sent you with the truth as a bearer of glad tidings and a warner (Basheeran wa nadheera).'\n"
        "- 'Wa la tus'alu 'an ashabil-jaheem': You are not accountable for those who choose perdition.\n"
        "- The Messenger conveys guidance with perfection; acceptance is the individual's choice."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Save Master PDF
    os.makedirs(BASE_DIR, exist_ok=True)
    pdf.save(OUTPUT_PDF)
    print(f"[OK] Master Landscape PDF compiled successfully: {OUTPUT_PDF}")

if __name__ == "__main__":
    build_part06_pdf()
