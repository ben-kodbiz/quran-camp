#!/usr/bin/env python3
"""
Huurs Studio - Surah Maryam Master Mindmap Vector PDF Generator
16:9 Landscape Widescreen (792 x 480 pt) • 8 Plates • 16 Pillars • 64 Cards
"""

import os
import sys
import subprocess
import shutil

sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
OUTPUT_PDF = os.path.join(BASE_DIR, "MARYAM_MASTER_MINDMAP.pdf")
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

def build_maryam_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH MARYAM", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
        # Badges
        pdf.rect(w - 280, h - 32, 175, 20, fill_rgb=NAVY_ELEVATED, stroke_rgb=BORDER_MUTED, line_width=0.8)
        pdf.text(f"PAGE {pnum:02d} / {total_pages:02d}", w - 85, h - 26, font="F2", size=9, rgb=GOLD)

        # Sub-header Title Area
        pdf.text(title, 32, h - 66, font="F2", size=12.5, rgb=WHITE)
        pdf.text(subtitle, 32, h - 79, font="F1", size=7.8, rgb=TEXT_MUTED)

        # Right Section Badge
        badge_str = f"[{section_badge}]"
        badge_w = len(badge_str) * 6.1
        pdf.text(badge_str, (w - 32) - badge_w, h - 68, font="F2", size=9.5, rgb=GOLD)

        # Divider Rule
        pdf.line(32, h - 86, w - 32, h - 86, stroke_rgb=BORDER_MUTED, line_width=0.8)

        # Bottom Footer
        pdf.line(32, 30, w - 32, 30, stroke_rgb=BORDER_MUTED, line_width=0.8)
        pdf.text("HUURS KNOWLEDGE SYSTEMS  *  AUTHENTIC SUNNI SOURCE DISCIPLINE  *  READ. REFLECT. RETURN.", 32, 16, font="F1", size=7.2, rgb=TEXT_MUTED)
        pdf.text("AUTHENTIC SUNNI SOURCE DISCIPLINE  *  THEMATIC SEQUENCE PURITY  *  READ. REFLECT. RETURN.", w - 465, 16, font="F2", size=7.0, rgb=GOLD_LIGHT)

    def draw_card(c_x, y_c, c_w, card_num, title, text):
        pdf.rect(c_x + 6, y_c - 52, c_w - 12, 62, fill_rgb=NAVY_CARD, stroke_rgb=BORDER_MUTED, line_width=0.6)
        pdf.rect(c_x + 12, y_c - 6, 22, 12, fill_rgb=NAVY_ELEVATED, stroke_rgb=BORDER_MUTED, line_width=0.5)
        pdf.text(f"{card_num:02d}", c_x + 16, y_c + 2, font="F2", size=6.8, rgb=GOLD)
        pdf.text(title, c_x + 38, y_c + 2, font="F2", size=7.8, rgb=WHITE)
        pdf.paragraph(text, c_x + 12, y_c - 10, c_w - 24, line_height=10.2, font="F1", size=6.8, rgb=TEXT_MUTED)

    c1_w, c2_w = 348, 348
    c1_x, c2_x = 32, 412
    c1_y, c1_h = 48, 332

    # ==========================================
    # PLATE 01: INTIMACY & YAHYA
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 8,
        "THE SUPPLICATION OF INTIMACY & THE SIGN OF YAHYA",
        "Pillars 1 & 2: Zakariyya's Whisper, Old Age Vulnerability, Spiritual Heir & The Three-Day Silence",
        "PLATE 01 : INTIMACY & YAHYA"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 01: THE INTIMATE WHISPER OF ZAKARIYYA", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Nida'an Khafiyya, Weakened Bones, Gray Hair & Unbroken Hope", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 1, "The Secret Whisper (Nida'an Khafiyya)",
              "Zakariyya invoking his Lord in private intimacy, establishing silent supplication as the purest vehicle of sincerity and humility before the All-Hearing.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 2, "Somatic Frailty of Old Age",
              "Weakened bones and head flaring with gray hair like fire consuming brushwood, articulating total biological vulnerability before God.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 3, "Unbroken Spiritual Hope",
              "'Never have I been in supplication to You, my Lord, unblessed'; past divine mercies serving as the spiritual collateral for present impossible prayers.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 4, "The Spiritual Inheritance (Yarithunee)",
              "Seeking an heir to inherit monotheistic guidance and knowledge of the House of Ya'qub, not ephemeral coins or physical worldly estates.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 02: THE MIRACULOUS BIRTH & SACRED SILENCE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("The Name Yahya, Barren Matriarch & The Three-Day Sign of Silence", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 5, "The Unique Name (Yahya)",
              "Bestowing a divine name never before borne by any human, signifying perpetual spiritual, moral, and physical vitality through faith.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 6, "Creation Beyond Causality (Hayyin)",
              "Divine reply to human astonishment: 'It is easy for Me; I created you before when you were nothing at all,' shattering causal limits.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 7, "The Three-Day Silence (Sawiyya)",
              "Physical restraint of speech for three days while remaining physically sound, dedicating speech solely to morning and evening Tasbih.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 8, "Gesturing Praise (Fa-Awha)",
              "Emerging from the sanctuary to instruct his community through symbolic gesture to glorify God constantly in the dawn and dusk.")

    # ==========================================
    # PLATE 02: SANCTUARY & ANNUNCIATION
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 8,
        "THE SANCTUARY OF MARYAM & THE ANNUNCIATION",
        "Pillars 3 & 4: Yahya's Childhood Wisdom, Maryam's Eastern Seclusion & Jibril's Pure Boy",
        "PLATE 02 : SANCTUARY & ANNUNCIATION"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 03: THE PROPHETIC ENDOWMENTS OF YAHYA", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Scripture with Strength, Childhood Wisdom, Tenderness & Pure Devotion", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 9, "Holding Scripture with Strength",
              "Commanded to seize the divine scripture with resolute firmness, intellectual depth, and unwavering moral dedication from early life.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 10, "Judicial Discernment in Childhood",
              "Bestowed with prophetic wisdom and deep spiritual understanding while still a youth, elevated above childish trivialities and pursuits.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 11, "Divine Tenderness & Purity (Hananan)",
              "Endowed with exceptional divine compassion, immaculate purity of character, and deep empathy for vulnerable human beings.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 12, "Filial Dutifulness Devoid of Pride",
              "Exhibiting tender devotion to his elderly parents, completely free of tyrannical arrogance, insolence, or stubborn disobedience.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 04: THE SANCTUARY OF MARYAM & THE VISITATION", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("The Eastern Screen, Manifestation of Jibril & The Pure Conception", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 13, "The Eastern Seclusion (Sharqiyya)",
              "Maryam retreating to an eastern sanctuary of the Temple, erecting a veil to devote herself entirely to contemplative worship.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 14, "The Manifestation of Jibril (Sawiyya)",
              "The archangel appearing before her in the form of a flawlessly proportioned human being, testing her spiritual chastity and resolve.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 15, "The Fortress of Ar-Rahman",
              "Instantly seeking refuge in the Most Merciful: 'I seek refuge in Ar-Rahman from you, if you should be fearing of Allah!'")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 16, "The Bestowal of a Pure Boy (Zaki)",
              "Jibril clarifying his mission: dispatched solely by the Lord to grant an immaculate, righteous boy as a cosmic sign and mercy.")

    # ==========================================
    # PLATE 03: NATIVITY & TESTIMONY
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 8,
        "NATIVITY UNDER THE PALM & CRADLE TESTIMONY",
        "Pillars 5 & 6: Maternal Labor Agony, The Stream and Dates, Slander Refuted & 'Abdullah",
        "PLATE 03 : NATIVITY & TESTIMONY"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 05: MATERNAL ANGUISH & THE DIVINE CONSOLATION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("The Palm Trunk, Cry of Despair, Postpartum Dates & The Brook of Peace", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 17, "The Agony of Labor Pains (Ajā'aha)",
              "Intense biological labor contractions driving Maryam across the wilderness to the dry trunk of a solitary date palm tree.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 18, "The Cry of Anguish (Ya Laytanee Mittu)",
              "Weeping: 'Oh, I wish I had died before this and was in oblivion, forgotten!'—validating acute maternal and social grief.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 19, "The Subterranean Brook (Sariyya)",
              "Divine consolation breaking forth at her feet: a fresh flowing rivulet to cleanse, hydrate, and soothe her exhausted body.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 20, "Fresh Succulent Dates (Rutaban)",
              "Shaking the rigid palm trunk to drop fresh dates, providing optimal nutritional and hormonal support for maternal recovery.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 06: THE FAST OF SILENCE & CRADLE SPEECH", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Vow of Silence, Societal Slander, Infant Eloquence & Proclamation of Servitude", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 21, "The Fast of Silence (Sawman)",
              "Vowing silence unto Ar-Rahman; divine wisdom sparing her the indignity of debating cynics and leaving her defense to God.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 22, "The Brutal Slander (Ukhta Haroon)",
              "Her tribe leveling vicious accusations: 'You have brought an unprecedented evil! Your parents were never unchaste!'")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 23, "Speech from the Cradle (Innee 'Abdullah)",
              "The infant speaking with majestic eloquence: 'Indeed, I am the servant of Allah; He has given me the Book and made me a prophet.'")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 24, "The Prophetic Charter of Jesus",
              "Proclaiming blessing wherever he is, prayer, zakah, tender duty to his mother, and total freedom from tyrannical arrogance.")

    # ==========================================
    # PLATE 04: ISA'S TRUTH & IBRAHIM
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 8,
        "THE TRUTH OF ISA & IBRAHIM'S FILIAL COMPASSION",
        "Pillars 7 & 8: Qawlul-Haqq, Kun Fayakoon, The Four 'Ya Abati' & The Peaceful Farewell",
        "PLATE 04 : ISA'S TRUTH & IBRAHIM"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 07: THE DOGMATIC TRUTH OF ISA (QAWLUL-HAQQ)", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Statement of Truth, Denial of Divine Sonship & Creation by Kun", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 25, "The Word of Truth (Qawlul-Haqq)",
              "That is Jesus, son of Mary—the definitive statement of truth about which contentious sectarian factions endlessly dispute.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 26, "Impossibility of Divine Sonship",
              "'It is not befitting for Allah to take a son; Exalted is He!' Absolute monotheistic transcendence above anthropomorphic myths.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 27, "The Imperative of Kun Fayakoon",
              "When He decrees an affair, He merely says to it: 'Be,' and it is; biological virgin conception is effortless for the Sovereign Creator.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 28, "The Straight Monotheistic Path",
              "Jesus confirming: 'Indeed, Allah is my Lord and your Lord, so worship Him alone; this is the straight path of truth.'")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 08: IBRAHIM'S COMPASSIONATE DAWAH (YA ABATI)", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Four Gentle Appeals, Warning of Satan, Threat of Stoning & The Peaceful Prayer", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 29, "The Four Filial Appeals (Ya Abati)",
              "Addressing his idolater father with tender reverence four times, modeling the pinnacle of loving, patient family dawah.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 30, "Rational & Spiritual Warning",
              "Appealing against inanimate idols that cannot see or hear, and warning against falling into spiritual bondage to Satan.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 31, "The Threat of Violent Stoning",
              "Azar threatening his son with violent execution and exile: 'Do you turn away from my gods? I will surely stone you!'")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 32, "The Response of Peace (Salamun 'Alayk)",
              "Absorbing threats with prophetic grace: 'Peace be upon you; I will ask my Lord to forgive you; He is ever gracious to me.'")

    # ==========================================
    # PLATE 05: PROPHETS & SUJOOD
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        5, 8,
        "PROPHETIC LINEAGE & TEARS IN SUJOOD",
        "Pillars 9 & 10: Musa at Tuwa, Isma'il's Fidelity, Idris Elevated & Weeping Prostration",
        "PLATE 05 : PROPHETS & SUJOOD"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 09: THE GOLDEN ILLUMINATION OF PROPHETS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Musa's Intimacy, Isma'il's Truthfulness & Idris's High Elevation", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 33, "Musa's Intimate Call (Najiyya)",
              "Called from the right side of Mount Tur and brought near for intimate divine speech, granted his brother Haroon as a supportive prophet.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 34, "Isma'il True to His Word (Sadiq al-Wa'd)",
              "Celebrated for unyielding fidelity to covenants and commanding his household to establish prayer and zakah with devotion.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 35, "Idris Elevated on High (Makanan 'Aliyya)",
              "An intensely truthful prophet elevated by Allah to a sublime celestial and spiritual station of supreme honor and dignity.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 36, "The Genealogies of Mercy",
              "The blessed monotheistic lineage descending from Adam, Nuh, Ibrahim, and Isra'il, chosen and guided by transcendent divine grace.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 10: TEARS OF AWE & ABANDONMENT OF PRAYER", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Weeping in Sujood (Sajdat at-Tilawah), Degenerate Posterity & Ghayya Ruin", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 37, "Weeping in Prostration (Kharroo Sujjada)",
              "When the verses of Ar-Rahman are recited, true believers collapse in physical prostration, tears streaming down their faces in awe.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 38, "Degenerate Posterity (Khalf)",
              "Succeeded by unworthy generations who neglected the prayer and pursued base lusts, heading toward catastrophic ruin (Ghayya).")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 39, "Anatomy of Neglected Prayer",
              "Disregarding prayer times and spiritual presence directly unleashes unchecked animalistic passions and social moral decay.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 40, "The Open Door of Tawbah",
              "Except those who repent, believe, and perform righteous deeds; they will enter Paradise without their reward diminished in the least.")

    # ==========================================
    # PLATE 06: EDEN & ANGELS
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        6, 8,
        "THE ABODE OF EDEN & CELESTIAL DECREES",
        "Pillars 11 & 12: Jannatu 'Adn, The Realm of Salam, Angelic Descent by Decree & The Timeless Master",
        "PLATE 06 : EDEN & ANGELS"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 11: THE SANCTUARY OF ETERNAL PEACE (SALAM)", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Gardens of Eden, Absence of Idle Speech & Morning/Evening Provisions", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 41, "Gardens of Eden in the Unseen",
              "Promised by Ar-Rahman to His servants in the unseen realm; divine promises are ever certain, immutable, and fulfilled in full.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 42, "Absence of Idle Talk (La Laghwa)",
              "Purged of vanity, gossip, slander, and noise; hearing only pure words of greeting, harmony, and celestial peace (Salam).")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 43, "Continuous Celestial Provisions",
              "Sustained with exquisite morning and evening provisions, reflecting the eternal rhythm of divine contentment and joy.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 44, "Inheritance of the God-Fearing",
              "That is the Paradise which We give as an inheritance to those among Our servants who were deeply conscious of God (Taqiyya).")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 12: ANGELIC DESCENT & TIMELESS SOVEREIGNTY", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Angelic Inability to Act Independently, Past/Present/Future & Endless Patience", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 45, "Descent Solely by Divine Command",
              "Jibril clarifying: 'We descend not except by the command of your Lord,' dispelling notions of independent angelic agency.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 46, "Total Temporal Ownership",
              "'To Him belongs what is before us, what is behind us, and what is between that,' ruling past, present, and future unconditionally.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 47, "Infallible Divine Memory (Ma Nasiyya)",
              "'And your Lord is never forgetful'; not a single prayer, secret tear, or silent righteous deed is ever forgotten by God.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 48, "Patience in His Servitude (Wa-Stabir)",
              "Lord of heavens and earth and all between; worship Him alone and remain resolutely steadfast and patient in His servitude.")

    # ==========================================
    # PLATE 07: RESURRECTION & HUBRIS
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        7, 8,
        "RESURRECTION REBUTTAL & DISMANTLING HUMAN HUBRIS",
        "Pillars 13 & 14: Skeptic Mockery of Bones, Kneeling Crowds (Jithiyya), Pride of Status & Vanished Empires",
        "PLATE 07 : RESURRECTION & HUBRIS"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 13: SKEPTICISM OF RESURRECTION REFUTED", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Man's Cynical Question, The Primordial Creation & Gathering Upon Knees", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 49, "The Skeptic's Mockery of Death",
              "Man cynically asks: 'When I am dead, shall I truly be brought forth alive?' doubting the reality of the second creation.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 50, "Rebuttal of Primordial Genesis",
              "'Does man not remember that We created him before, when he was nothing at all?' The first creation proves the second.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 51, "Gathered Upon Knees (Jithiyya)",
              "Swearing by your Lord: We will assemble mankind and devils, then bring them around the fire of Hell kneeling in helpless terror.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 52, "Plucking the Arrogant Rebels",
              "Extracting from every faction those who were most violently insolent against the Most Merciful to face prime retribution.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 14: THE VAIN BOASTING OF MATERIAL CLOUT", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Elite Arrogance of Station, Swept Empires, Misleading Wealth & True Guidance", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 53, "The Boast of Superior Status",
              "Skeptics boast against humble believers: 'Which of our two factions is superior in social position and finer in council?'")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 54, "The Dust of Extinct Civilizations",
              "How many generations before them have We destroyed who were vastly superior in luxury, assets, and outward prestige!")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 55, "The Trap of Extended Delusion",
              "Whoever persists in error, the Most Merciful extends his rope until they witness what was promised: punishment or the Hour.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 56, "Enduring Righteous Strivings",
              "Allah increases those who are guided in guidance; and the enduring righteous deeds are superior in reward and ultimate return.")

    # ==========================================
    # PLATE 08: SHIRK HORROR & WUDD
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        8, 8,
        "THE COSMIC HORROR OF SHIRK & THE GIFT OF WUDD",
        "Pillars 15 & 16: Cosmic Tremors at Divine Offspring, Universal Servitude ('Abda), The Gift of Love & Ease",
        "PLATE 08 : SHIRK HORROR & WUDD"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 15: COSMIC REVOLT AGAINST POLYTHEISM", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("The Monstrous Claim (Idda), Celestial Tremors & Inanimate Creation's Outrage", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 57, "The Monstrous Assertion (Shay'an Idda)",
              "Rebuking those who claim Ar-Rahman has taken a son: 'You have indeed brought forth a monstrous, reality-rupturing falsehood!'")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 58, "Violent Revolt of Creation",
              "The heavens almost tear apart, the earth cleaves open, and mountains collapse into pulverized dust at attributing a son to God.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 59, "Universal Servitude ('Abda)",
              "Every entity in the heavens and earth comes to the Most Merciful strictly as a humble, obedient worshipper and servant.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 60, "Standing Entirely Alone (Farda)",
              "God has numbered them with precise enumeration; each human being will stand before Him on Judgment Day completely alone.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 16: THE CELESTIAL GIFT OF LOVE (WUDD)", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Divine Affection Planted, Qur'anic Linguistic Ease & The Vanished Murmurs", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 61, "The Endowment of Divine Love (Wudd)",
              "Those who believe and perform righteous deeds: the Most Merciful will appoint for them enduring celestial love across the earth.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 62, "Angelic Proclamation of Affection",
              "When Allah loves a servant, Jibril and the heavens love him, and widespread acceptance is placed for him among human hearts.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 63, "Qur'anic Linguistic Facilitation",
              "'We have only made it easy in your tongue that you may give glad tidings to the righteous and warn contentious people.'")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 64, "Vanished Murmurs of Extinct Tyrants",
              "'How many generations before them have We destroyed! Do you perceive of them a single one or hear of them a whisper?'")

    pdf.save(OUTPUT_PDF)
    print(f"Generated Vector PDF at: {OUTPUT_PDF}")

    # Generate PNG Previews
    cmd = f"pdftoppm -png -r 150 {OUTPUT_PDF} {PREVIEWS_DIR}/maryam_page"
    subprocess.run(cmd, shell=True, check=True)
    print(f"Rendered PNG previews in: {PREVIEWS_DIR}")

    # Copy to brain dir
    for i in range(1, 9):
        src_prev = f"{PREVIEWS_DIR}/maryam_page-{i}.png"
        dst_brain = os.path.join(brain_dir, f"maryam_page-{i}.png")
        if os.path.exists(src_prev):
            shutil.copyfile(src_prev, dst_brain)
            print(f"Copied {src_prev} to {dst_brain}")

if __name__ == "__main__":
    build_maryam_pdf()
