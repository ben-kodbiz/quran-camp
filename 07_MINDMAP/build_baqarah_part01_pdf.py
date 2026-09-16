#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Baqarah Part 1 Master Landscape Mindmap PDF Compiler
Foundation Media: Part 1 Audio Lecture (Duration: 02:02:41)
Strict Standardization:
- Title: Surah Al-Baqarah — Part 1
- Zero Ayah Numbers in titles/headers/cards
- Zero mention of external speaker names; 100% Huurs Studio & Sunni source discipline
- 4 Landscape Widescreen Pages (792 x 480 pts, 1.65:1 ratio)
- Symmetrical 2-column layout with center connector bridges
"""

import os
import sys

# Import verified PDF engine
sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
OUTPUT_PDF = os.path.join(BASE_DIR, "BAQARAH_PART_01_MINDMAP.pdf")

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

def build_part01_pdf():
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
        pdf.text(f"FOUNDATION MEDIA: PART 1 ({time_badge})", w - 282, h - 20, font="F2", size=6.8, rgb=EMERALD)
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

    # =========================================================================
    # PAGE 1: EPISTEMOLOGY & THE STANDARD OF TAQWA
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 4,
        "THE EPISTEMOLOGY OF REVELATION & THE FIVE MARKS OF TAQWA",
        "Pillars 1 & 2: Structural flow, disjointed letters as divine proof, and the labor of the spiritual farmer",
        "PART 1 : SECTION 1",
        "00:00 - 22:49"
    )

    # Column 1: Pillar 1 (Epistemology & Huruf Muqatta'at)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 1: EPISTEMOLOGICAL ORIENTATION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Structural Tanasub, Camel Peak & Disjointed Letters", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c1_x + c1_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=0.6)
    pdf.text("00:00 - 11:35", c1_x + c1_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    # Card 1A: Peak of the Qur'an & Flow
    y_c = c1_y + c1_h - 48
    pdf.text("1. Peak of the Qur'an & Speech Continuity (Tanasub)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Hadith: 'Likulli shay'in sanam, wa sanamul-qur'ani al-baqarah' (Peak/camel hump).\n"
        "- Hermeneutics: Exposing the unbroken organic flow across transitions rather than reading as disconnected legal fragments.\n"
        "- Surah Al-Fatihah ends with a petition for guidance; Al-Baqarah instantly answers."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 1B: Razi's Epistemological Humility
    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Alif-Lam-Meem: Putting Intellect in its Place (Al-Razi)", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- You asked for guidance, but Allah opens with letters human reason cannot decode.\n"
        "- Epistemological First Principle: Shatter intellectual ego before entering revelation: 'You know not; Allah knows everything' (Wallahu ya'lamu wa antum la ta'lamun).\n"
        "- Approaching with arrogance yields zero guidance; intellect must submit to divine instruction."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 1C: Sha'rawi's Oral Orthography Proof
    y_c -= 66
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Oral Culture vs. Alphabet Names (Al-Sha'rawi)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Rabbis mocked Makkans as 'Ummi' (unlettered, devoid of academic literacy).\n"
        "- In oral societies, words are spoken; letter names exist only in spelling education.\n"
        "- An illiterate person says 'Alam'; reciting isolated names 'Alif-Lam-Meem' with 6-count tajweed proves recitation from an external Divine Instructor ('Allamal-Qur'an)."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 1D: Zamakhshari's Challenge
    y_c -= 62
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. The Inimitable Alphabet Challenge (Al-Zamakhshari)", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'These are the letters of your own alphabet from which you compose poetry.'\n"
        "- Allah built this inimitable scripture from those identical letters—why are masters of Arabic eloquence entirely unable to compete with it?"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Center Gap Connector Bridge
    pdf.line(c1_x + c1_w, bridge_y, c2_x, bridge_y, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(w/2 - 12, bridge_y - 8, 24, 16, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=0.8)
    pdf.text_centered("->", w/2, bridge_y + 3, font="F2", size=7, rgb=GOLD_LIGHT)

    # Column 2: Pillar 2 (The Celestial Canon & 5 Marks of Muttaqin)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 2: THE CANON & 5 MARKS OF TAQWA", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Celestial Distance, Zero Agitation & Spiritual Farming", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c2_x + c2_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=0.6)
    pdf.text("11:35 - 22:49", c2_x + c2_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    # Card 2A: Dhalikal-Kitab & La Rayb
    y_c = c1_y + c1_h - 48
    pdf.text("1. Celestial Altitude & Zero Agitating Doubt (Rayb)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Dhalika ('That'): Points to celestial reality in 7th Heaven (Al-Lawh Al-Mahfuz).\n"
        "- Rayb vs. Shakk: Rayb denotes psychological disturbance, anxiety, and sleeplessness (Qalaqun-nafs wa-dtirabuha). La Rayba Feeh guarantees pure serenity for sincere seekers.\n"
        "- Taqwa (36+ occurrences): Proactive self-preservation and hyper-vigilance against sin."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 2B: The First 3 Marks: Ghayb, Salah, Infaq
    y_c -= 60
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Primary Marks: Ghayb, Salah & Account Transfer", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 1. Yu'minuna bil-Ghayb: Belief in the Unseen beyond sensory limits.\n"
        "- 2. Yuqimunas-Salah: Establishing prayer firmly and unbrokenly (not casual prayer).\n"
        "- 3. Mimma Razaqnahum Yunfiqun: Spending from divine provision. Wealth is not ours; infaq is merely an account transfer from Dunya account to Akhirah account."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 2C: Revelation Invariant & Conviction
    y_c -= 66
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Finality of Prophethood & Akhirah Conviction (Yaqeen)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 4. Belief in Quran & Prior Books (Bima unzila ilayk wa ma unzila min qablik).\n"
        "- Crucial: Scripture sent 'before' is confirmed; zero scripture sent 'after'—sealing prophethood.\n"
        "- 5. Bil-akhirati hum yuqinun: Visceral certainty of judgment (like knowing you'll be fired if you walk off the job)."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 2D: The Farmer's Labor (Al-Muflihun)
    y_c -= 62
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. The Harvest of Success: The Farmer's Labor (Muflih)", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Success (Falah) originates from 'Fallah' (farmer) who clears land, plants seeds, weeds, waters, and endures storms before reaping harvest.\n"
        "- Spiritual success is not cheap or instantaneous; it requires sustained, disciplined labor."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 2: THE SEALED DENIERS & ANATOMY OF HYPOCRISY
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 4,
        "THE SEALED DISBELIEVER & THE PSYCHOLOGY OF HYPOCRISY",
        "Pillars 3 & 4: Decade of rejected da'wah, grammatical camouflage, conscious vs unconscious hypocrisy",
        "PART 1 : SECTION 2",
        "22:50 - 34:36"
    )

    # Column 1: Pillar 3 (The Incurable Disbelievers)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 3: THE HARDENED DISBELIEVERS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Decade of Animosity, Sealed Faculties & Rhetorical Sequence", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c1_x + c1_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=0.6)
    pdf.text("22:50 - 27:00", c1_x + c1_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    # Card 3A: Decade of Rejection
    y_c = c1_y + c1_h - 48
    pdf.text("1. Context of Incurable Denial (Innal-ladhina kafaru)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Not all non-believers: refers specifically to leaders who endured a full decade of perfect prophetic da'wah and only intensified in hatred.\n"
        "- Past tense 'Kafaru' signifies finalized, locked-in obstinacy; warning makes zero difference."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 3B: Heart Sealed First
    y_c -= 52
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. The Sealing Sequence: Heart -> Hearing -> Sight", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Khatamallahu 'ala qulubihim (Heart sealed first), wa 'ala sam'ihim (hearing), wa 'ala absarihim ghishawah (sight veiled).\n"
        "- When internal receptor (heart) dies, perception dies; external senses become useless."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 3C: Comparison with Jathiyah
    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Structural Comparison: Al-Baqarah vs. Al-Jathiyah", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- In Al-Jathiyah (45:23), Allah seals ears before the heart (Khatama 'ala sam'ihi wa qalbihi).\n"
        "- Why? Jathiyah verse 8 explicitly describes auditory arrogance ('Yasma'u ayatillahi... ka'allam yasma'ha').\n"
        "- Al-Baqarah seals heart first because opening context centers entirely on internal spiritual states: Iman, Taqwa, Yaqeen, and Kufr."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 3D: Great Punishment
    y_c -= 68
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Penalty: Great Punishment ('Adhabun 'Azim)", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Disbelievers who openly declare their hostility receive 'Adhabun 'Azim.\n"
        "- Clear, unambiguous position: they wear their denial openly, with no deceit or camouflage."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Center Gap Connector Bridge
    pdf.line(c1_x + c1_w, bridge_y, c2_x, bridge_y, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(w/2 - 12, bridge_y - 8, 24, 16, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=0.8)
    pdf.text_centered("->", w/2, bridge_y + 3, font="F2", size=7, rgb=GOLD_LIGHT)

    # Column 2: Pillar 4 (The Psychology of Hypocrisy)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 4: THE PSYCHOLOGY OF HYPOCRISY", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Grammatical Infiltration, Sickness of Heart & Acute Pain", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c2_x + c2_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=0.6)
    pdf.text("27:00 - 34:36", c2_x + c2_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    # Card 4A: Grammar of Infiltration
    y_c = c1_y + c1_h - 48
    pdf.text("1. Grammar of Camouflage: Singular Man vs. Plural Amanna", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Wa minan-nasi man yaqulu' (singular subject: the isolated speaker).\n"
        "- But they utter: 'Amanna billahi' (plural verb: 'We have believed').\n"
        "- The hypocrite tries to blend into the collective body of believers; absolute divine verdict: 'Wa ma hum bi-mu'minin' (Zero true faith)."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 4B: Two Kinds of Hypocrites
    y_c -= 60
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Two Categories: Conscious Infiltrators vs. Unconscious", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 1. Conscious Spies/Agents: Malevolent infiltrators posing as Muslims for political espionage.\n"
        "- 2. Unconscious Hypocrites (Wa ma yash'urun): Believers who genuinely consider themselves good Muslims while their hearts harbor deep hypocrisy.\n"
        "- Umar's Terror: Continually asking Hudhayfah if his own name was on the secret list."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 4C: Sickness of Heart & Continual Lying
    y_c -= 66
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Growing Sickness & Habitual Lying (Yakdhibun)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Fi qulubihim maradun fa-zadahumullahu marada': Moral compromise feeds heart disease.\n"
        "- The root cause: 'Bima kanu yakdhibun' (continuous, habitual lying and fabrication).\n"
        "- No lie is small; deceit rots the internal spiritual compass."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 4D: Acute Pain ('Adhabun Aleem)
    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Acute Pain ('Adhabun Aleem) Harsher than for Kuffar", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Kuffar receive 'Azim (great punishment); Hypocrites receive 'Adhabun Aleem.\n"
        "- Aleem denotes acute, unrelenting, constant pain where the body never builds tolerance.\n"
        "- The punishment of hypocrisy is far harsher because they weaponized the sacred trust."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 3: DECEIT, THE DOUBLE-EXIT BURROW & MASTER PARABLES
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 4,
        "THE DOUBLE-EXIT BURROW & THE TWO MASTER PARABLES",
        "Pillars 5 & 6: Slandering believers as fools, the 300-ft leash, the kindled fire, and thunderous rainstorm",
        "PART 1 : SECTION 3",
        "34:37 - 63:46"
    )

    # Column 1: Pillar 5 (Tactics, Nafaqa' & The Leash)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 5: TACTICS OF DECEIT & THE LEASH", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("False Reformers, Mocking Believers & The Double Exit", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c1_x + c1_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=0.6)
    pdf.text("34:37 - 49:25", c1_x + c1_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=CYAN)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    # Card 5A: False Reformers & Fool Accusation
    y_c = c1_y + c1_h - 48
    pdf.text("1. False Peacemakers & Calling Sahabah 'Fools' (Sufaha')", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Innama nahnu muslihun': Claiming neutrality while maintaining backdoors with enemies.\n"
        "- Mock the Muhajirun who sacrificed homes and wealth: 'Shall we believe as the fools believe?'\n"
        "- Allah directly defends the Sahabah: 'Ala innahum humus-sufaha'u wa lakin la ya'lamun' (They are the real fools!)."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 5B: Nafaqa' (The Desert Lizard)
    y_c -= 60
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Etymology of Munafiq: The Double-Exit Burrow (Nafaqa')", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Nafaqa': Underground burrow of the desert lizard engineered with two escape holes.\n"
        "- If Muslims dominate, they claim 'We are with you!'; if enemies threaten, they escape through the backdoor. Allah mocks them: 'Allahu yastahzi'u bihim'."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 5C: The 300-Foot Leash
    y_c -= 56
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. The 300-Foot Leash: Extending Rebellious Freedom", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Yamudduhum fi tughyanihim ya'mahun': Giving a wild dog a 300-foot leash.\n"
        "- The dog sprints at full speed thinking it is free—until the leash reaches the end and violently snaps its neck. Allah lets them dig their own trench to the lowest pit of Hell."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 5D: Bad Trade & Muhtad
    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Bad Trade: Guidance for Misguidance (Muhtad)", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Ishtarawud-dalalata bil-huda': Exchanged invaluable guidance for cheap worldly security.\n"
        "- 'Wa ma kanu muhtadeen': A 'Muhtad' is someone who makes active moral effort to be guided. They entered Islam casually without effort, so they left casually."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Center Gap Connector Bridge
    pdf.line(c1_x + c1_w, bridge_y, c2_x, bridge_y, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(w/2 - 12, bridge_y - 8, 24, 16, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=0.8)
    pdf.text_centered("->", w/2, bridge_y + 3, font="F2", size=7, rgb=GOLD_LIGHT)

    # Column 2: Pillar 6 (The Two Master Parables)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 6: THE TWO MASTER PARABLES", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("The Kindled Fire & The Thunderous Rainstorm", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c2_x + c2_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=0.6)
    pdf.text("49:26 - 63:46", c2_x + c2_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    # Card 6A: Parable 1: Kindled Fire
    y_c = c1_y + c1_h - 48
    pdf.text("1. Parable 1: The Kindled Fire (Istawqada Nara)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Traveler sparks a fire in pitch darkness; surroundings illuminated (Ada'at ma hawlahu).\n"
        "- Dhahaballahu bi-nurihim: Allah extinguishes *their* internal light and visual capacity, abandoning them in layered dark (Zulumat)."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 6B: Summun Bukmun 'Umyun
    y_c -= 52
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Simultaneous Deprivation: Deaf, Mute, Blind (Summ, Bukm, 'Umy)", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- No conjunctions ('and') between words: simultaneous, total impairment.\n"
        "- Cannot hear instructions (deaf), cannot call for help (mute), cannot see the path (blind).\n"
        "- Fahum la yarji'un: Stranded forever, unable to return to the light they had."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 6C: Parable 2: Rainstorm
    y_c -= 60
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Parable 2: The Thunderous Rainstorm (Sayyib)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Dense black storm cloud with thunder and lightning.\n"
        "- Shoving fingers into ears from thunderclaps in terror of death (Hadharal-mawt).\n"
        "- The futility of hypocrisy: Putting fingers in your ears does not make the storm go away!"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 6D: Fair-Weather Walking
    y_c -= 56
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Conditional Walking: When Lightning Flashes They Walk", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Kullama ada'a lahum mashaw feeh, wa idha azlama 'alayhim qamu'.\n"
        "- When Islam brings social status or ease, they advance; when sacrifices or trials hit, they freeze.\n"
        "- Represents fair-weather believers who flee responsibility."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 4: COSMIC SANCTUARY, INIMITABILITY & THE ETERNAL RETURN
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 4,
        "COSMIC SANCTUARY, INIMITABLE CHALLENGE & THE ETERNAL RETURN",
        "Pillars 7 & 8: Furnished earth, prohibition of rivals, Tufayl & Otba, the mosquito parable, and the 4-stage lifecycle",
        "PART 1 : SECTION 4",
        "63:47 - 122:41"
    )

    # Column 1: Pillar 7 (Cosmic Sanctuary & Prohibition of Rivals)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 7: COSMIC SANCTUARY & ANDAD", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Universal Enslavement, Earth as Bed & Competitors", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c1_x + c1_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=0.6)
    pdf.text("63:47 - 72:31", c1_x + c1_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    # Card 7A: Universal Enslavement
    y_c = c1_y + c1_h - 48
    pdf.text("1. Universal Enslavement to the Master (U'budu Rabbakum)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Ya ayyuhan-nas, u'budu rabbakum': Summary of entire Qur'an.\n"
        "- The earth is furnished as a comfortable bed (Firasha) and the sky as a secure ceiling (Bina'an).\n"
        "- The earth is a home/bedroom designed for human peace and worship."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 7B: Luxury of Fruits
    y_c -= 56
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. The Luxury of Fruits (Thamarat) vs. Bare Nutrition", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Water produces Thamarat: not bland survival food, but sweet, beautiful, fragrant fruits.\n"
        "- Hospital drip feed keeps a patient alive; Allah gave us exquisite tastes, aromas, and colors to enjoy.\n"
        "- Joy in eating is a divine blessing proving Allah's boundless love for creation."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 7C: Prohibition of Rivals
    y_c -= 66
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Prohibition of Competitors (Fa la taj'alu lillahi andada)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Nidd: Competitor, equal, raising a voice against God (Tandid).\n"
        "- We set up rivals when we love wealth, status, career, or family more than Allah, disobeying Him for worldly gain.\n"
        "- Prophet's correction to bedouin: 'Have you made me a competitor (Niddan) to Allah?'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 7D: The Challenge
    y_c -= 60
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. The Inimitable Challenge (Fa'tu bi suratim mim-mithlih)", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Issued as the final verdict after a decade of obstinate refusal.\n"
        "- Tufayl al-Dawsi: Unplugged cotton from his ears, conquered by divine eloquence, accepted Islam.\n"
        "- Otba ibn Rabi'a: Quraish's master debater wept at Surah Fussilat: 'This is not poetry or magic.'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Center Gap Connector Bridge
    pdf.line(c1_x + c1_w, bridge_y, c2_x, bridge_y, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(w/2 - 12, bridge_y - 8, 24, 16, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=0.8)
    pdf.text_centered("->", w/2, bridge_y + 3, font="F2", size=7, rgb=GOLD_LIGHT)

    # Column 2: Pillar 8 (Paradise, The Mosquito & The Return)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 8: PARADISE, MOSQUITO & RETURN", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Waterfront Jannah, Primordial Mithaq & Seven Skies", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c2_x + c2_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=0.6)
    pdf.text("82:16 - 122:41", c2_x + c2_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=CYAN)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    # Card 8A: Waterfront Paradise
    y_c = c1_y + c1_h - 48
    pdf.text("1. Waterfront Mansions & Ever-Novel Fruits (Jannat)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Waterfront real estate: Gardens beneath which rivers flow; permanent tenure (Khalidun).\n"
        "- Ever-transcending fruits: 'Hadhalladhi ruziqna min qabl'—familiar look, but every bite explodes with novel flavor.\n"
        "- Azwajun mutahharah: Spouses purified physically, emotionally, and spiritually."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 8B: The Mosquito Parable
    y_c -= 60
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. The Mosquito Parable: Wisdom vs. Cynical Mockery", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Cynics mock small creatures (mosquitoes/flies); modern science reveals microscopic lethal complexity.\n"
        "- 'Yudillu bihi kathiran wa yahdi bihi kathira': Revelation misguides the corrupt and guides the sincere.\n"
        "- The fault is never in the revelation, but in the disease within the reader's heart."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 8C: The Primordial Covenant & Sunnah
    y_c -= 60
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. The Primordial Covenant (Mithaq) & Sunnah Severing", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Al-Fasiqun break the primordial covenant of the soul (Alastu bi-rabbikum).\n"
        "- 'Yaqta'una ma amarallahu bihi an yusala': Severing ties of kinship AND divorcing the Quran from the Messenger's Sunnah ('Quran-only' deception to distort meanings)."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 8D: 4-Stage Lifecycle & Seven Skies
    y_c -= 56
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Four-Stage Lifecycle & The Seven Skies (Sab'a Samawat)", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Lifecycle: Non-existence (Amwat) -> Life -> Death -> Resurrection -> Return (Ilayhi turja'un).\n"
        "- Seven balanced heavens: Umar disciplining the speculative bedouin.\n"
        "- 'Wa huwa bi-kulli shay'in 'aleem': Human intellect humbled before the All-Knowing Master."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Save Output
    pdf.save(OUTPUT_PDF)
    print(f"[OK] Master Landscape Mindmap PDF compiled successfully: {OUTPUT_PDF} (4 Pages)")

if __name__ == "__main__":
    build_part01_pdf()
