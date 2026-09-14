#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Baqarah Session 01 Landscape Mindmap PDF Compiler (Perfected)Covers Ayat 1-2 across 4 Core Pillars:
- Pillar 1: Socio-Historical Setting & Demographic Shift of Madinah (00:00 - 11:10)
- Pillar 2: Ayah 1: Alif-Lam-Meem & The Student Orientation (11:10 - 24:35)
- Pillar 3: Ayah 2: Al-Kitab & La Rayba Feeh - The Celestial Canon (24:35 - 43:35)
- Pillar 4: Ayah 2: Hudan Lil-Muttaqin - The Real-Time Guidance Engine (43:35 - 54:37)
"""

import os
import sys

# Import verified PDF engine
sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
OUTPUT_PDF = os.path.join(BASE_DIR, "SESSION_01_BAQARAH_AYAT_1_2_MINDMAP.pdf")

# Palette
NAVY_DEEP = (0.024, 0.039, 0.071)      # #060A12
NAVY_CARD = (0.051, 0.078, 0.133)      # #0D1422
NAVY_ELEVATED = (0.078, 0.118, 0.196)  # #141E32
NAVY_QUOTE = (0.040, 0.065, 0.110)
GOLD = (0.831, 0.686, 0.353)           # #D4AF59
GOLD_LIGHT = (0.910, 0.820, 0.580)
CYAN = (0.220, 0.740, 0.970)           # #38BDF8
PURPLE = (0.659, 0.333, 0.969)         # #A855F7
EMERALD = (0.063, 0.725, 0.506)        # #10B981
WHITE = (0.973, 0.980, 0.988)
TEXT_MUTED = (0.680, 0.730, 0.800)
BORDER_MUTED = (0.160, 0.220, 0.310)
BORDER_GOLD = (0.700, 0.560, 0.280)

def build_session01_pdf():
    w, h = 792, 480 # Landscape ratio (1.65:1)
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, ayah_badge, timestamp_badge):
        # Background
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH AL-BAQARAH FOUNDATION", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
        # Audio & Page Badges
        pdf.rect(w - 285, h - 32, 180, 20, fill_rgb=NAVY_ELEVATED, stroke_rgb=BORDER_MUTED, line_width=0.8)
        pdf.text(f"AUDIO FOUNDATION: NIGHT 01 ({timestamp_badge})", w - 277, h - 20, font="F2", size=6.8, rgb=EMERALD)
        pdf.text(f"PAGE {pnum:02d} / {total_pages:02d}", w - 85, h - 26, font="F2", size=9, rgb=GOLD)

        # Sub-title Bar
        pdf.text(title, 32, h - 66, font="F2", size=12, rgb=WHITE)
        pdf.text(subtitle, 32, h - 79, font="F1", size=7.8, rgb=TEXT_MUTED)
        pdf.text(f"[{ayah_badge}]", w - 120, h - 68, font="F2", size=10.5, rgb=GOLD)
        pdf.line(32, h - 86, w - 32, h - 86, stroke_rgb=BORDER_MUTED, line_width=0.8)

        # Bottom Footer
        pdf.line(32, 25, w - 32, 25, stroke_rgb=BORDER_MUTED, line_width=0.8)
        pdf.text("HUURS KNOWLEDGE SYSTEMS  *  AUTHENTIC SUNNI SOURCE DISCIPLINE  *  READ. REFLECT. RETURN.", 32, 13, font="F1", size=7.2, rgb=TEXT_MUTED)
        pdf.text("
    # Balanced Symmetrical Geometry
    # Left margin 32, Col 1 = 348, Gap = 32, Col 2 = 348, Right margin 32
    c1_x, c1_y, c1_w, c1_h = 32, 35, 348, h - 130
    c2_x = c1_x + c1_w + 32
    c2_w = 348

    # -------------------------------------------------------------------------
    # PAGE 1: SOCIO-HISTORICAL MATRIX & AYAH 1 (ALIF-LAM-MEEM)
    # -------------------------------------------------------------------------
    pdf.new_page(w, h)
    draw_chrome(
        1, 2,
        "PROLOGUE & ORIENTATION: MADANI DEMOGRAPHICS & THE STUDENT DISPOSITION",
        "Pillars 1 & 2: Historical context of sovereignty, ink-stained scholars, and the epistemological humility of Huruf Muqatta'at",
        "AYAT 1 - 2 (PART I)",
        "00:00 - 24:35"
    )

    # Pillar 1 Container (Left)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    
    # Pillar 1 Header
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 1: SOCIO-HISTORICAL SETTING", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Madani Demographics, Sovereignty & Scholar Caste", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c1_x + c1_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=0.6)
    pdf.text("00:00 - 11:10", c1_x + c1_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    # Card 1A: Sovereign Transition & Address Shift
    y_cursor = c1_y + c1_h - 48
    pdf.text("1. The Sovereign Transition & Address Shift", c1_x + 12, y_cursor, font="F2", size=8, rgb=WHITE)
    t1a = (
        "- Shift from persecuted Makkan minority to sovereign, self-governing Ummah in Madinah.\n"
        "- Madani revelation forms ~30%-35% of the Qur'an, focusing on community law & governance.\n"
        "- Discourse shifts from universal address ('Ya ayyuhan-nas' - O mankind) to the intimate covenant address: 'Ya ayyuhalladhina amanu' (O you who have believed)."
    )
    pdf.paragraph(t1a, c1_x + 12, y_cursor - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 1B: Al-Ahbar vs An-Nabiyy Al-Ummi
    y_cursor -= 58
    pdf.line(c1_x + 12, y_cursor + 6, c1_x + c1_w - 12, y_cursor + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. The Contrast: Al-Ahbar vs. An-Nabiyy Al-Ummi", c1_x + 12, y_cursor, font="F2", size=8, rgb=GOLD_LIGHT)
    t1b = (
        "- Al-Ahbar (Root H-B-R = ink): Rabbi caste whose hands & robes were stained with ink across generations of transcribing and studying Torah & Talmud.\n"
        "- An-Nabiyy Al-Ummi (Root U-M-M = mother): Unlettered Prophet, formal education as untouched as the day he emerged from his mother's womb.\n"
        "- Polemic: Elites mocked: 'How can an unlettered man without credentials teach us?'"
    )
    pdf.paragraph(t1b, c1_x + 12, y_cursor - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 1C: The 4 Madinan Demographics
    y_cursor -= 66
    pdf.line(c1_x + 12, y_cursor + 6, c1_x + c1_w - 12, y_cursor + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. The Four Distinct Demographics of Madinah", c1_x + 12, y_cursor, font="F2", size=8, rgb=WHITE)
    t1c = (
        "- 1. The Core Believers: Muhajirun (emigrants) and Ansar (native helpers).\n"
        "- 2. Ahl al-Kitab: Established Jewish & Christian communities with deep scriptural literacy.\n"
        "- 3. New Converts from Ahl al-Kitab: Believers whose families remained Jewish/Christian.\n"
        "- 4. The Munafiqun (Hypocrites): Feigning faith while conspiring against the state."
    )
    pdf.paragraph(t1c, c1_x + 12, y_cursor - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 1D: The 10-Year Revelation Span
    y_cursor -= 62
    pdf.line(c1_x + 12, y_cursor + 6, c1_x + c1_w - 12, y_cursor + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Revelation Timeline & Celestial Climax", c1_x + 12, y_cursor, font="F2", size=8, rgb=GOLD_LIGHT)
    t1d = (
        "- Spans the full 10-year Madani period: from pre-Badr (2 AH) down to the very final verse revealed before the Prophet's death (2:281 - 'Wattaqu yawman turja'una feehi ilallah').\n"
        "- The concluding verses (285-286) were not revealed on earth, but gifted directly during the celestial ascension (Al-Mi'raj) in the Heavens (Sahih Muslim 173)."
    )
    pdf.paragraph(t1d, c1_x + 12, y_cursor - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Center Gap Connector Bridge
    bridge_y = c1_y + c1_h / 2
    pdf.line(c1_x + c1_w, bridge_y, c2_x, bridge_y, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(w/2 - 12, bridge_y - 8, 24, 16, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=0.8)
    pdf.text_centered("->", w/2, bridge_y + 3, font="F2", size=7, rgb=GOLD_LIGHT)

    # Pillar 2 Container (Right)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    
    # Pillar 2 Header
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 2: AYAH 1 (ALIF-LAM-MEEM)", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("The Student Orientation & Epistemological Humility", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c2_x + c2_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=0.6)
    pdf.text("11:10 - 24:35", c2_x + c2_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    # Card 2A: Oral Culture Proof
    y_cursor = c1_y + c1_h - 48
    pdf.text("1. Oral Culture vs. Spelling: Proof of Divine Teacher", c2_x + 12, y_cursor, font="F2", size=8, rgb=WHITE)
    t2a = (
        "- In oral cultures, words are known by sounds; letter names require formal reading education.\n"
        "- An illiterate person reading the letters would naturally say 'Alam' (as in Surah Al-Fil).\n"
        "- Reciting the isolated letters 'Alif-Lam-Meem' with 6-count elongation (Madd Lazim) conclusively proves the Prophet is repeating dictation from a Divine Teacher ('Allamal-Qur'an)."
    )
    pdf.paragraph(t2a, c2_x + 12, y_cursor - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 2B: Epistemological Humility
    y_cursor -= 58
    pdf.line(c2_x + 12, y_cursor + 6, c2_x + c2_w - 12, y_cursor + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Syllabus Day: Humility Over Human Arrogance", c2_x + 12, y_cursor, font="F2", size=8, rgb=GOLD_LIGHT)
    t2b = (
        "- Absolute Consensus (Ijma' of the Salaf): The definitive meaning is known only to Allah.\n"
        "- Pedagogical Function: The first lesson of Qur'an study is shattering intellectual ego: 'You know nothing; Allah knows everything' (Wallahu ya'lamu wa antum la ta'lamun).\n"
        "- Stunned the Arabs who called non-Arabs 'Ajam' (stammerers) by leading with alien fragmented letters."
    )
    pdf.paragraph(t2b, c2_x + 12, y_cursor - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 2C: Destruction of Consumer Mindset (with callout styling)
    y_cursor -= 66
    pdf.line(c2_x + 12, y_cursor + 6, c2_x + c2_w - 12, y_cursor + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Demolishing the Modern Consumer Mindset", c2_x + 12, y_cursor, font="F2", size=8, rgb=WHITE)
    t2c = (
        "- Modern consumer mindset: 'The customer is king; I will rate this 1-5 stars; satisfy me.'\n"
        "- Approaching scripture as a consumer produces arrogance, skepticism, and spiritual blindness.\n"
        "- The Student Attitude: Approach as a dying, destitute wanderer in the desert receiving water. You do not critique the water; you drink to survive."
    )
    pdf.paragraph(t2c, c2_x + 12, y_cursor - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 2D: Warning Against Futile Codes
    y_cursor -= 62
    pdf.line(c2_x + 12, y_cursor + 6, c2_x + c2_w - 12, y_cursor + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Condemnation of Trivia & Structural Invariant", c2_x + 12, y_cursor, font="F2", size=8, rgb=GOLD_LIGHT)
    t2d = (
        "- Condemns sick hearts who obsess over obscure codes (Ibtigha'al-fitnah) while evading moral commands. Spending 10 years decoding numbers is an evasion of practical guidance.\n"
        "- Structural Invariant: In every instance where Huruf Muqatta'at occur, the immediate succeeding clause is ALWAYS a declaration concerning the Scripture (Al-Kitab)."
    )
    pdf.paragraph(t2d, c2_x + 12, y_cursor - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # -------------------------------------------------------------------------
    # PAGE 2: THE IMMUTABLE CANON & LIVING GUIDANCE (AYAH 2)
    # -------------------------------------------------------------------------
    pdf.new_page(w, h)
    draw_chrome(
        2, 2,
        "THE IMMUTABLE CANON & THE LIVING ENGINE: AYAH 2 LINGUISTIC ARCHITECTURE",
        "Pillars 3 & 4: Deep lexical analysis of Al-Kitab, Dhalika, Rayb, Tadabbur, and Taqwa as active vigilance",
        "AYAH 2 (PART II)",
        "24:35 - 54:37"
    )

    # Pillar 3 Container (Left)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    
    # Pillar 3 Header
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 3: AYAH 2 (AL-KITAB & LA RAYB)", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("The Immutable Celestial Archetype & Intellectual Miracle", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c1_x + c1_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=0.6)
    pdf.text("24:35 - 43:35", c1_x + c1_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=CYAN)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    # Card 3A: Root Ka-Ta-Ba
    y_cursor = c1_y + c1_h - 48
    pdf.text("1. Linguistic Archaeology of Al-Kitab (Ka-Ta-Ba)", c1_x + 12, y_cursor, font="F2", size=8, rgb=WHITE)
    t3a = (
        "- Classical Origin: 'Kataba' originally meant carving into stone, wood, or stitching leather.\n"
        "- Represents unalterable permanence: once carved in stone, text cannot be erased or reordered.\n"
        "- Although revealed piecemeal (Tanjim) over 23 years, Allah designated it 'Al-Kitab' from early Madinah because its symmetry was already etched in Al-Lawh Al-Mahfuz (Preserved Tablet)."
    )
    pdf.paragraph(t3a, c1_x + 12, y_cursor - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 3B: Dhalika vs Hadha
    y_cursor -= 58
    pdf.line(c1_x + 12, y_cursor + 6, c1_x + c1_w - 12, y_cursor + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Rhetorical Purpose of Dhalika ('That') vs. Hadha", c1_x + 12, y_cursor, font="F2", size=8, rgb=GOLD_LIGHT)
    t3b = (
        "- Hadha denotes proximity (this book here); Dhalika denotes distance and exalted status.\n"
        "- 1. Exalted Altitude: Physical sounds on earth, but uncreated reality is in 7th Heaven (Fi Kitabin Maknun).\n"
        "- 2. The Promised Scripture (Al-Kitab Al-Maw'ud): Tells Ahl al-Kitab: 'That is the very Book promised in your scriptures that you have been waiting for.'"
    )
    pdf.paragraph(t3b, c1_x + 12, y_cursor - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 3C: Rayb vs Shakk
    y_cursor -= 66
    pdf.line(c1_x + 12, y_cursor + 6, c1_x + c1_w - 12, y_cursor + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Rayb (Agitating Doubt) vs. Shakk (Doubt)", c1_x + 12, y_cursor, font="F2", size=8, rgb=WHITE)
    t3c = (
        "- Zamakhshari (Al-Kashshaf): Haqiqat ar-Rayb: Qalaqun-nafs wa-dtirabuha (The reality of Rayb is internal agitation, unrest, and anxiety that robs sleep).\n"
        "- 'La rayba feeh' promises that for the sincere seeker, this Book contains zero agitating uncertainty or moral confusion.\n"
        "- Punctuation (Mu'anaqah): Pause at 'La rayb' OR 'Feeh' - both recitations valid in Qira'at."
    )
    pdf.paragraph(t3c, c1_x + 12, y_cursor - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 3D: Miracle of Ears vs Eyes
    y_cursor -= 66
    pdf.line(c1_x + 12, y_cursor + 6, c1_x + c1_w - 12, y_cursor + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Sensory Eyes Miracles vs. Living Intellect Miracle", c1_x + 12, y_cursor, font="F2", size=8, rgb=GOLD_LIGHT)
    t3d = (
        "- Past miracles (Musa's staff, Isa's healing) were visual spectacles for the eyes. They eliminated doubt for eyewitnesses, but died as living proofs with that generation.\n"
        "- The Qur'an is an intellectual and auditory miracle for the ears that lives forever.\n"
        "- Requires Tadabbur (deep contemplation): superficial reading produces perceived doubt; deep reflection dissolves all contradictions. (Anecdote: Philosophy student pinned down after 2 yrs)."
    )
    pdf.paragraph(t3d, c1_x + 12, y_cursor - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Center Gap Connector Bridge
    bridge_y = c1_y + c1_h / 2
    pdf.line(c1_x + c1_w, bridge_y, c2_x, bridge_y, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(w/2 - 12, bridge_y - 8, 24, 16, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=0.8)
    pdf.text_centered("->", w/2, bridge_y + 3, font="F2", size=7, rgb=GOLD_LIGHT)

    # Pillar 4 Container (Right)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    
    # Pillar 4 Header
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 4: AYAH 2 (HUDAN LIL-MUTTAQIN)", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("The Real-Time Guidance Engine & Vigilant Warhorse", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c2_x + c2_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=0.6)
    pdf.text("43:35 - 54:37", c2_x + c2_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    # Card 4A: Hudan & Hadiyah
    y_cursor = c1_y + c1_h - 48
    pdf.text("1. Hudan & Hadiyah: The Supreme Desert Gift", c2_x + 12, y_cursor, font="F2", size=8, rgb=WHITE)
    t4a = (
        "- Etymological connection to 'Hadiyah' (gift). To a traveler dying of thirst and lost in a trackless desert, the greatest gift is not gold, but clear direction to water and life.\n"
        "- The Qur'an is Allah's ultimate gift of life to spiritually disoriented humanity."
    )
    pdf.paragraph(t4a, c2_x + 12, y_cursor - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 4B: The Spiritual Water Cycle
    y_cursor -= 58
    pdf.line(c2_x + 12, y_cursor + 6, c2_x + c2_w - 12, y_cursor + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. The Water Analogy: Continuous Rehydration", c2_x + 12, y_cursor, font="F2", size=8, rgb=GOLD_LIGHT)
    t4b = (
        "- The biological body cannot survive on yesterday's water; cells deplete and die.\n"
        "- The human soul similarly requires continuous spiritual rehydration to survive moral toxicity.\n"
        "- This is why the believer asks for guidance ('Ihdinas-Sirat al-Mustaqim') in every single rak'ah of daily prayer (17+ times a day)."
    )
    pdf.paragraph(t4b, c2_x + 12, y_cursor - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 4C: Farasun Waq (The Warhorse)
    y_cursor -= 66
    pdf.line(c2_x + 12, y_cursor + 6, c2_x + c2_w - 12, y_cursor + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Taqwa & Farasun Waq (The Barefoot Warhorse)", c2_x + 12, y_cursor, font="F2", size=8, rgb=WHITE)
    t4c = (
        "- Classical philology (Root W-Q-Y): Extreme protective vigilance (Fartus-Siyanah).\n"
        "- Origin: 'Farasun Waq' is a battle horse that lost its shoes traversing volcanic rock. It steps with hyper-alert, delicate caution to avoid injury.\n"
        "- Taqwa is not perfection or absence of rocks; it is navigating life's moral minefield with deliberate, vigilant care of heart, eyes, and tongue."
    )
    pdf.paragraph(t4c, c2_x + 12, y_cursor - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 4D: Hudan as Hal
    y_cursor -= 66
    pdf.line(c2_x + 12, y_cursor + 6, c2_x + c2_w - 12, y_cursor + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Grammatical State of Hal: The Running Engine", c2_x + 12, y_cursor, font="F2", size=8, rgb=GOLD_LIGHT)
    t4d = (
        "- 'Hudan' is grammatically parsed as a Hal (circumstantial state of active execution).\n"
        "- The Qur'an does not merely possess dormant potential to guide; it is actively, dynamically executing guidance in real-time.\n"
        "- When a sincere seeker turns to it in personal or societal crisis, the verse speaks directly to their immediate predicament—the engine is running."
    )
    pdf.paragraph(t4d, c2_x + 12, y_cursor - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Output document
    pdf.save(OUTPUT_PDF)
    print(f"[OK] Session 01 Landscape Mindmap PDF compiled successfully: {OUTPUT_PDF}")

if __name__ == "__main__":
    build_session01_pdf()
