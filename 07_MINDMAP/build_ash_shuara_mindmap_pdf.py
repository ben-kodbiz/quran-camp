#!/usr/bin/env python3
"""
Huurs Studio - Surah Ash-Shu'ara Master Mindmap Vector PDF Generator
16:9 Landscape Widescreen (792 x 480 pt) • 8 Plates • 16 Pillars • 64 Cards
"""

import os
import sys
import subprocess
import shutil

sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
OUTPUT_PDF = os.path.join(BASE_DIR, "ASH_SHUARA_MASTER_MINDMAP.pdf")
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

def build_ash_shuara_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH ASH-SHU'ARA", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
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
    # PLATE 01: PROPHETIC GRIEF & COMMISSION OF MUSA
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 8,
        "PROPHETIC GRIEF & THE COMMISSION OF MUSA",
        "Pillars 1 & 2: Bakhi'un Nafsaka, The Call to Tuwa, Human Fears & Confronting Pharaoh's Palace",
        "PLATE 01 : THE COMMISSION"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 01: THE COMPASSIONATE MESSENGER", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Ta-Seen-Meem, Overwhelming Grief, The Descent of Signs & Celestial Power", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 1, "The Sovereign Prelude (Ta-Seen-Meem)",
              "Inimitable Qur'anic opening letters confirming the divine, uncreated origin and linguistic supremacy of the revelation.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 2, "Consuming Prophetic Grief (Bakhi')",
              "Exhausting oneself with grief over their disbelief—reflecting the Prophet's supreme mercy and pastoral care for humanity.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 3, "The Sovereign Sign from Heaven",
              "If Allah willed, He could send a sign compelling all necks to bow in humiliation, but faith requires voluntary submission.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 4, "The Cycle of Arrogant Mockery",
              "No fresh reminder comes from the All-Merciful except that the heedless turn away, mocking the truth until consequences strike.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 02: THE DISPATCH TO PHARAOH'S REALM", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("The Sacred Commission, Human Vulnerability, Harun's Support & Gaslighting", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 5, "The Call to the Wrongdoing Nation",
              "Commanding Musa to confront Pharaoh's imperial tyranny, demanding freedom and dignity for the enslaved Israelites.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 6, "Musa's Honest Human Apprehensions",
              "Expressing mortal vulnerability: tightness of chest, impediment in speech, fear of rejection, and the blood-claim against him.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 7, "Divine Accompaniment & Harun's Aid",
              "Allah reassures: 'Nay, go both of you with Our signs; indeed We are with you, listening'—granting ministerial strength.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 8, "Deconstructing Imperial Gaslighting",
              "Pharaoh invokes Musa's fosterage and past deeds; Musa reframes his 'favor' as the direct result of enslaving an entire people.")

    # ==========================================
    # PLATE 02: THE SHOWDOWN & PARTING OF THE SEA
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 8,
        "THE TRIUMPH OF TRUTH & THE PARTING OF THE SEA",
        "Pillars 3 & 4: Staff Consuming Illusions, Magicians' Sujood, Trapped at the Shore & Towering Waves",
        "PLATE 02 : THE DELIVERANCE"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 03: THE COLLAPSE OF IMPERIAL ILLUSION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("The Grand Assembly, The Living Serpent, Spontaneous Sujood & Defying Terror", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 9, "The Festival of Sorcery",
              "Assembling the empire's master illusionists under imperial patronage, seeking prestige, silver, and proximity to power.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 10, "The Devouring Staff (Talqafu)",
              "Musa casts his staff, which becomes a living reality consuming their false illusions, proving the ontological supremacy of truth.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 11, "The Instant Prostration of the Sorcerers",
              "Recognizing divine power beyond all human illusion, the sorcerers fall in total Sujood, surrendering to the Lord of Harun and Musa.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 12, "Defying Amputation and Crucifixion",
              "Pharaoh threatens crucifixion on palm trunks; the newly faithful proclaim: 'No harm! Indeed to our Lord we will return!'")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 04: THE MIRACLE AT THE RED SEA", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("The Midnight March, Cries of Despair, Inna Ma'iya Rabbi & The Drowning Host", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 13, "The Midnight Exodus",
              "Leading the enslaved Israelites by night under divine command, pursued by Pharaoh's mobilizing army at sunrise.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 14, "Trapped Between Army and Ocean",
              "With the raging waters ahead and iron chariots behind, the Israelites despair: 'Indeed, we are surely overtaken!'")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 15, "The Unshakable Cry of Yaqeen",
              "Musa roars: 'Kalla! Inna ma'iya rabbi sa-yahdeen' (Nay! Indeed with me is my Lord; He will guide me!), banishing doubt.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 16, "The Cleaving Waters (Kal-Tawd)",
              "Striking the sea, cleaving it into twelve dry paths between mountain-high water walls, drowning Pharaoh and delivering the faithful.")

    # ==========================================
    # PLATE 03: IBRAHIM'S MONOTHEISM & SOUND HEART
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 8,
        "IBRAHIM'S MONOTHEISM & THE SOUND HEART",
        "Pillars 5 & 6: Socratic Deconstruction of Idols, The Manifest Doxology, Qalbin Saleem & The Judgment",
        "PLATE 03 : THE SOUND HEART"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 05: THE RATIONAL DECONSTRUCTION OF IDOLS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Interrogating Stone Deities, The Blindness of Tradition & Ibrahim's Declaration", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 17, "Interrogating Inanimate Deities",
              "Ibrahim asks his people: 'Do they hear you when you call? Or do they benefit you or harm?' exposing their zero agency.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 18, "The Confession of Blind Imitation (Taqlid)",
              "Their sole defense is intellectual surrender: 'Nay, we found our fathers doing so,' clinging to inherited cultural myths.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 19, "Enemies Except the Lord of the Worlds",
              "Ibrahim disassociates from their pantheon: all false deities are enemies to the soul except the Creator and Sustainer.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 20, "Creation, Sustenance & Guidance",
              "Proclaiming: 'He who created me, and He guides me; and He who feeds me and gives me drink,' establishing absolute reliance.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 06: THE ETERNAL CURRENCY: QALBIN SALEEM", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Spiritual Healing, Prayer for Legacy, Sound Heart & Proximity of Paradise", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 21, "Spiritual Adab in Healing (Yashfeen)",
              "Attributing illness to human frailty (*Idha maridtu*) and ultimate cure solely to Allah (*Fa-huwa yashfeen*), modeling sublime adab.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 22, "The Du'a for an Honorable Legacy",
              "Seeking wisdom (*Hukman*), joining the righteous, and asking for *Lisan Sidqin fil-Akhireen*—honorable mention across future ages.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 23, "The Sound Heart (Qalbin Saleem)",
              "On that Day, neither wealth nor sons avail, except one who meets Allah with a heart sound from shirk, doubt, malice, and pride.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 24, "Eschatological Unveiling: Jannah & Jahim",
              "Paradise brought near to the God-conscious, while Hellfire is exposed to the astray, stripping away worldly illusions.")

    # ==========================================
    # PLATE 04: PROPHETIC MISSIONS: NUH & HUD
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 8,
        "PROPHETIC MISSIONS: NUH & HUD ('AD)",
        "Pillars 7 & 8: Sincerity in Dawah, Aristocratic Snobbery, Vain Monuments on High Ridges & Tyranny",
        "PLATE 04 : NUH & HUD"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 07: NUH & THE DEFENSE OF THE HUMBLE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Taqwa, Infallible Sincerity, Defending Poor Believers & The Ark of Deliverance", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 25, "The Trustworthy Messenger (Rasulun Ameen)",
              "Nuh calls his people to fear Allah and obey, declaring that his message is pure guidance untainted by personal ambition.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 26, "The Sincerity Formula (In Ajriya)",
              "Proclaiming: 'I ask of you no reward; my reward is only upon the Lord of the worlds,' dismantling cynical suspicions.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 27, "Rejecting Aristocratic Elitism",
              "Oligarchs objected that only the lowest social class followed him; Nuh refused to drive away believers whose hearts belong to God.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 28, "Deliverance in the Full Ark",
              "When rejection hardened, Allah delivered Nuh and the faithful in the laden ship (*Al-Fulk al-Mashhoon*), drowning the deniers.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 08: HUD & THE MATERIAL ARROGANCE OF 'AD", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Monuments on Ridges, Tyrannical Striking, Illusions of Immortality & Annihilation", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 29, "Vain Monuments on High Ridges (Ree')",
              "Indicting 'Ad for building colossal architectural towers on mountain ridges purely for vanity, sport, and ostentatious display.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 30, "The Illusion of Earthly Permanence",
              "Constructing palatial fortresses (*Masani'*) as though they would live forever, ignoring their inevitable mortal end.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 31, "Tyrannical Violence (Batash-tum Jabbarin)",
              "Governing through unchecked brute force, cruelty, and militaristic oppression, intoxicating themselves with physical strength.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 32, "The Devastating Wind & Extinction",
              "Warning them of divine blessings in livestock, springs, and gardens; their rejection brought the shattering gale of annihilation.")

    # ==========================================
    # PLATE 05: SALIH'S THAMUD & LUT'S SODOM
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        5, 8,
        "SALIH (THAMUD) & LUT (THE PERVERTED CITIES)",
        "Pillars 9 & 10: Mountain Mansions, The She-Camel's Water Right, Moral Inversion & Stone Rain",
        "PLATE 05 : THAMUD & LUT"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 09: SALIH & THE SACRED SHE-CAMEL", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Hewing Mountains, Shared Water Covenants, Fatal Hamstringing & Morning Regret", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 33, "Hewing Mansions Out of Living Rock",
              "Thamud carved elaborate palaces out of mountain cliffs (*Fariheen*), priding themselves on geotechnical invulnerability.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 34, "The Living Miracle: Naqatullah",
              "A miraculous she-camel granted as a test sign, requiring an inviolable shared water schedule: a day for her and a day for the city.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 35, "The Fatal Hamstringing ('Aqaruha)",
              "Rebellious oligarchs conspired and hamstrung the camel, defying the covenant and daring the divine punishment to strike.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 36, "The Morning Regret (Fa-asbahu Nadimeen)",
              "A thunderous seismic blast shattered their rock sanctuaries at dawn, leaving them motionless corpses filled with useless regret.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 10: LUT & THE TRANSGRESSION OF CREATION", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Defying Natural Order, Threats of Expulsion, The Rescued Family & Stone Rain", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 37, "Confronting Moral Inversion",
              "Lut confronted his society for inverting natural desires and violating travelers, establishing the inviolability of divine order.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 38, "Tyrannical Threats of Expulsion",
              "The corrupt citizens threatened: 'If you do not desist, O Lut, you will surely be expelled,' attempting to outlaw moral purity.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 39, "Deliverance of the Righteous Family",
              "Allah delivered Lut and his household, except his treacherous wife who aligned with the corrupt culture and remained behind.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 40, "The Cataclysmic Rain of Clay Stones",
              "Raining upon the inverted cities an evil shower of baked brimstone (*Mataran fa-sa'a mataru al-mundhareen*), obliterating them.")

    # ==========================================
    # PLATE 06: SHU'AYB & ECONOMIC JUSTICE
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        6, 8,
        "SHU'AYB & THE GOSPEL OF ECONOMIC JUSTICE",
        "Pillars 11 & 12: People of the Thicket, Honest Scales, Commercial Ethics & The Day of the Dark Cloud",
        "PLATE 06 : ECONOMIC JUSTICE"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 11: SHU'AYB & HONEST WEIGHTS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Ashab al-Aykah, Full Measure, The Upright Balance & Forbidding Corruption", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 41, "The Mission to the Forest Dwellers",
              "Shu'ayb sent to the commercial hub of Ashab al-Aykah (The Companions of the Thicket), calling them to Taqwa and obedience.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 42, "The Mandate of Full Measure (Awfu)",
              "Commanding: 'Give full measure and do not be of those who cause loss'—elevating fair trade into a direct spiritual obligation.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 43, "The Upright Balance (Al-Qistas)",
              "Weighing with honest, unrigged scales, forbidding economic exploitation, monopolistic price-gouging, and market deceit.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 44, "Do Not Spread Corruption Upon Earth",
              "Warning that systematic commercial cheating destroys communal trust, dissolves social solidarity, and invites civil ruin.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 12: THE DAY OF THE SHADOW (AZ-ZULLAH)", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Accusations of Sorcery, The Daring of Heaven, The Suffocating Cloud & The Refrain", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 45, "Dismissing the Prophet as Bewitched",
              "The merchants mocked Shu'ayb: 'You are only of those affected by magic; you are merely a human being like us, and a liar!'")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 46, "Daring the Sky to Fall",
              "Arrogantly challenging: 'Make fragments of the sky fall upon us if you are truthful!'—daring divine retribution to strike.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 47, "The Agony of the Dark Cloud (Yawm az-Zullah)",
              "A scorching heat drove them outdoors; when a dark cloud offered shade, they gathered beneath it, only to be consumed by flame.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 48, "The Eighth Liturgical Refrain",
              "Concluding the historical cycle with the majestic cadence: 'Indeed your Lord—He is the Exalted in Might, the Merciful.'")

    # ==========================================
    # PLATE 07: THE TRUSTWORTHY SPIRIT & REVELATION
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        7, 8,
        "THE TRUSTWORTHY SPIRIT & THE CLEAR REVELATION",
        "Pillars 13 & 14: Tanzil Rabbi al-'Alameen, Ar-Ruh al-Ameen, The Pure Heart & Demonic Impotence",
        "PLATE 07 : THE REVELATION"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 13: THE CELESTIAL CHAIN OF TRANSMISSION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Tanzil, The Trustworthy Spirit (Jibril), Inscribed Upon the Heart & Arabic Tongue", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 49, "Descent from the Lord of the Worlds",
              "Confirming that the Qur'an is not human poetry or philosophical musing, but direct revelation (*Tanzil*) from the Creator.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 50, "The Trustworthy Emissary (Ar-Ruh al-Ameen)",
              "Delivered by Archangel Jibril, possessing absolute trustworthiness, immunity from alteration, and majestic celestial authority.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 51, "Inscribed Upon the Prophet's Heart",
              "Deposited directly upon the pure heart (*Qalb*) of the Prophet Muhammad ﷺ, transforming internal consciousness into guidance.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 52, "The Lucid Arabic Medium (Lisan 'Arabi)",
              "Revealed in crystal-clear, unadulterated Arabic (*Bi-lisanin 'arabiyyin mubeen*), providing unsurpassed eloquence and clarity.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 14: THE IMPOTENCE OF DEMONIC FORCES", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Ancient Scriptures, Refuting Soothsaying, Demonic Exclusion & Piercing Flame", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 53, "Foretokened in Former Scriptures (Zubur)",
              "The coming of the Prophet and the final book was inscribed in the primordial scriptures of the ancient prophets.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 54, "Testimony of the Scholars of Israel",
              "The learned rabbis and scholars recognized the prophetic descriptions, serving as an empirical historical proof for Mecca.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 55, "Devils Cannot Transmit Revelation",
              "Refuting pagan slanders: devils have neither the moral character, spiritual capacity, nor divine permission to carry revelation.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 56, "Expulsion from Celestial Hearkening",
              "Demonic forces are permanently barred from overhearing heavenly councils, repelled by burning celestial meteors.")

    # ==========================================
    # PLATE 08: PASTORAL CARE, POETS & DESTINY
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        8, 8,
        "PASTORAL ETHICS, THE POETS & ETERNAL REVERSAL",
        "Pillars 15 & 16: Warning Close Kin, Lowering the Wing, Wandering Poets vs. Believing Artists & The Final Reversal",
        "PLATE 08 : THE POETS"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 15: PROPHETIC PASTORAL DECORUM", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Warning Immediate Kin, Lowering the Wing to Believers & Absolute Tawakkul", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 57, "Warning Immediate Kin (Andhir 'Asheerataka)",
              "Commanded to begin public dawah with closest family, proclaiming on Mount Safa that personal faith alone secures salvation.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 58, "Lowering the Wing to the Believers",
              "Embodying profound tenderness, humility, and protective care (*Wakhfid janahaka*) toward all who embrace the path of truth.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 59, "Disavowal of Transgression (Inni Baree')",
              "Declaring innocence from sinful rebellion while maintaining gentle compassion, balancing moral clarity with pastoral warmth.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 60, "Reliance Upon Al-'Azeez Ar-Raheem",
              "Placing total reliance (*Tawakkul*) upon the Mighty, the Merciful, who witnesses the Prophet's standing and movements in Sujood.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 16: THE ETHICS OF ART & THE FINAL REVERSAL", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Wandering in Every Valley, Hypocrisy of Speech, Believing Poets & The Final Turning", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 61, "Wandering in Every Valley (Yaheemoon)",
              "Dissecting unanchored artists who roam aimlessly through shifting emotional valleys, praising or defaming based on impulse.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 62, "The Gap Between Word and Action",
              "Exposing moral hypocrisy: proclaiming grand ideals of chivalry and sacrifice while living in cowardice, indulgence, and conceit.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 63, "The Redemption of Art Through Faith",
              "Honoring believing writers and artists who do good works, remember Allah abundantly, and employ their eloquence to defend justice.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 64, "The Reversal of Destinies (Ayya Munqalab)",
              "A thunderous closing decree: the oppressors and cynics will soon know to what catastrophic reversal their souls will return.")

    # Save PDF
    pdf.save(OUTPUT_PDF)
    print(f"Generated Vector Mindmap PDF: {OUTPUT_PDF}")

    # Generate PNG Previews
    cmd = f"pdftoppm -png -r 150 {OUTPUT_PDF} {os.path.join(PREVIEWS_DIR, 'ash_shuara_mindmap_page')}"
    subprocess.run(cmd, shell=True, check=True)
    print(f"Rendered PNG previews in {PREVIEWS_DIR}")

    # Copy to Brain Directory for Visual Verification
    for i in range(1, 9):
        src_png = os.path.join(PREVIEWS_DIR, f"ash_shuara_mindmap_page-{i}.png")
        dst_png = os.path.join(brain_dir, f"ash_shuara_mindmap_page_{i}.png")
        if os.path.exists(src_png):
            shutil.copy2(src_png, dst_png)
    print(f"Copied mindmap preview plates to {brain_dir}")

if __name__ == '__main__':
    build_ash_shuara_pdf()
