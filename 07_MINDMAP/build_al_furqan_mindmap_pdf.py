#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Furqan Master Mindmap Vector PDF Generator
16:9 Landscape Widescreen (792 x 480 pt) • 8 Plates • 16 Pillars • 64 Cards
"""

import os
import sys
import subprocess
import shutil

sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
OUTPUT_PDF = os.path.join(BASE_DIR, "AL_FURQAN_MASTER_MINDMAP.pdf")
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

def build_al_furqan_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH AL-FURQAN", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
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
    # PLATE 01: THE DIVINE CRITERION & SOVEREIGNTY
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 8,
        "THE DIVINE CRITERION & COSMIC SOVEREIGNTY",
        "Pillars 1 & 2: Tabaraka, Universal Warning, Absolute Monotheism & Ontological Impotence of Idols",
        "PLATE 01 : THE CRITERION"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 01: THE DESCENT OF AL-FURQAN", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Tabaraka, The Criterion, The Perfect Servant & Universal Warning", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 1, "The Blessed Exaltation (Tabaraka)",
              "Derived from perpetual, inexhaustible abundance, affirming Allah's infinite perfection, majesty, and absolute transcendence.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 2, "The Criterion of Truth & Falsehood",
              "Al-Furqan: the decisive instrument cleaving guidance from error, halal from haram, and enduring reality from fleeting delusion.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 3, "The Apex of Servitude ('Abdihi)",
              "Honoring the Prophet with the title of servitude, confirming that total submission to Allah is the highest human nobility.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 4, "Universal Herald (Nadhiran lil-'Alamin)",
              "A global mission extending across temporal eras and geographical boundaries to warn all conscious creation.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 02: THE NEGATION OF FABRICATED DEITIES", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Cosmic Dominion, Absolute Measure, Ontological Impotence & Slander", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 5, "Absolute Singularity of Kingship",
              "Possessing unbroken sovereignty over the heavens and earth, having taken neither offspring nor partner in cosmic command.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 6, "Creation by Precise Measure (Taqdira)",
              "Designing every physical atom, biological organism, and planetary orbit with mathematical precision and intended purpose.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 7, "Ontological Impotence of False Gods",
              "Deities that cannot create a speck of dust, possess no power over death, life, or resurrection, and control no benefit or harm.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 8, "Refutation of Plagiarism Allegations",
              "Exposing the cynics' claim that the Qur'an is ancient myths dictated at dawn, affirming it descends from the Knower of Secrets.")

    # ==========================================
    # PLATE 02: THE PROPHET'S HUMANITY & SKEPTICISM
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 8,
        "PROPHETIC HUMANITY & THE SKEPTICS' FALLACY",
        "Pillars 3 & 4: Biological Reality, Marketplaces, Demand for Angels & The Cosmic Fitnah",
        "PLATE 02 : PROPHETIC TRIAL"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 03: THE ACCESSIBLE MESSENGER", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Eating Food, Walking in Markets, Angelic Escorts & Lost Treasure", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 9, "The Biological Reality of Prophecy",
              "The skeptics mocked his eating of food, failing to understand that moral guidance requires a mortal exemplar experiencing hunger.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 10, "Engagement in Public Marketplaces",
              "Walking in commercial avenues as a relatable human being, demonstrating ethical trade, honesty, and grounded humility.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 11, "The Demand for Supernatural Apparitions",
              "Superficial demands for visible angelic bodyguards or descended heavenly treasuries, misunderstanding the nature of faith.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 12, "The Mirage of Material Prestige",
              "Equating spiritual leadership with palatial orchards and endless wealth, deconstructed by divine sovereign wisdom.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 04: THE ARCHITECTURE OF TRIAL & PATIENCE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Mutual Testing, Allegations of Sorcery, Unyielding Sabr & Divine Sight", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 13, "The Accusation of Enchantment",
              "Dismissing the Prophet as a bewitched man, demonstrating the psychological blindness of those trapped in cynicism.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 14, "The Divine Promise of Gardens Above",
              "Allah can grant earthly palaces and rivers, yet preserved the Prophet's ascetic station to keep the reward pure in Akhirah.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 15, "Mutual Existential Trial (Fitnah)",
              "Making humanity a mutual test: wealth tests poverty, health tests illness, and prophetic meekness tests oligarchic pride.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 16, "The Call to Unyielding Sabr",
              "Asking the soul: 'Will you have patience?'—reminding believers that their steadfast endurance is witnessed by the All-Seeing.")

    # ==========================================
    # PLATE 03: ESCHATOLOGICAL REVERSALS
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 8,
        "ESCHATOLOGICAL REVERSALS & THE DAY OF REGRET",
        "Pillars 5 & 6: Terrifying Angelic Sight, Scattered Dust, Rending Skies & The Hands of Remorse",
        "PLATE 03 : ESCHATOLOGY"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 05: DISSOLUTION OF OSTENTATIOUS DEEDS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Denial of the Meeting, The Dark Encounter, Scattered Dust & Pure Abode", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 17, "Denial of the Divine Encounter",
              "Those who expect no meeting with Allah arrogantly demand visible angels, unaware of the terror accompanying such a sight.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 18, "The Day Angels Bring No Glad Tidings",
              "Seeing angelic hosts as instruments of inescapable justice, hearing the dread proclamation: 'A barrier completely forbidden!'")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 19, "Good Deeds as Scattered Dust (Haba')",
              "Worldly charities and achievements performed without Ikhlas and Tawheed reduced to weightless, sunlit particles of dust.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 20, "The Serene Abode of the Righteous",
              "Contrasting the ruin of falsehood with the companions of Paradise, resting in honorable dwelling places and tranquil midday ease.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 06: THE AGONY OF CORRUPT COMPANIONSHIP", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Skies Torn with Clouds, The Biting of Hands, The Fatal Friend & Betrayal", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 21, "The Cleaving of the Heavens",
              "Skies split open with white luminous clouds as celestial ranks descend, confirming that ultimate sovereignty belongs to Ar-Rahman.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 22, "The Tyrant Biting His Hands",
              "Gnawing upon flesh in unspeakable psychological torment, lamenting: 'If only I had taken with the Messenger a righteous path!'")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 23, "The Ruin of the Corrupt Friend (Khalil)",
              "Crying in eternal agony over a charming friend who mocked faith, drew the soul away from remembrance, and led it to destruction.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 24, "Satan's Treacherous Abandonment",
              "Exposing the demonic strategy: whispering delusions into human vanity, then abandoning the victim to face eternal shame alone.")

    # ==========================================
    # PLATE 04: THE ABANDONED QUR'AN & TARTEEL
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 8,
        "THE ABANDONED REVELATION & GRADUAL DESCENT",
        "Pillars 7 & 8: The Prophetic Complaint, Five Levels of Hajr, Tarteel & Heart-Anchoring",
        "PLATE 04 : THE LIVING BOOK"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 07: THE PROPHETIC GRIEVANCE & OPPOSITION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Hajr al-Qur'an, Five Diagnostic Levels, Criminal Adversaries & Divine Sufficiency", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 25, "The Solemn Cry of the Messenger",
              "'O my Lord, indeed my people have taken this Qur'an as an abandoned thing'—the most harrowing indictment against negligence.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 26, "The Taxonomy of Hajr (Ibn al-Qayyim)",
              "Diagnosing five fatal abandonments: neglecting listening, practical action, legal arbitration, deep reflection, and spiritual healing.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 27, "Criminal Enemies of the Prophets",
              "Establishing the historical law that every messenger faces hardened antagonists from the corrupt elites of their society.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 28, "Allah as Sufficient Guide and Helper",
              "Comforting the believer's heart: despite cultural hostility, divine guidance (*Hadiya*) and divine aid (*Nasira*) are absolute.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 08: THE PEDAGOGY OF MEASURED DESCENT", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Objections of Single Descent, Anchoring the Heart, Tarteel & Real-Time Answers", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 29, "The Demand for a Single Descent",
              "Skeptics questioned why the Qur'an was not delivered all at once like former scriptures, missing its living pedagogical nature.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 30, "Anchoring the Prophetic Heart (Fu'ad)",
              "Descending in response to trials, constantly reassuring the Prophet, infusing courage, and nurturing communal spiritual maturity.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 31, "The Cadence of Tarteel",
              "Recited with distinct pauses, deliberate beauty, and measured contemplation, training the listener to absorb divine meanings.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 32, "Decisive Answers to Intellectual Queries",
              "No objection is raised by skeptics except that the Qur'an brings the definitive truth and the most profound explanation.")

    # ==========================================
    # PLATE 05: HISTORICAL WARNINGS & EGO-IDOLATRY
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        5, 8,
        "HISTORICAL PRECEDENTS & THE DEIFICATION OF DESIRE",
        "Pillars 9 & 10: Ancient Civilizational Demise, The Rain of Ruin, Mockery & The Idolatry of Hawa",
        "PLATE 05 : HISTORICAL SIGNS"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 09: THE RUINS OF TYRANNICAL NATIONS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Musa & Pharaoh, The Deluge of Nuh, 'Ad, Thamud, Ar-Rass & Extinction", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 33, "Musa & Harun Against Imperial Tyranny",
              "Sent with divine signs to Pharaoh's regime, culminating in the destruction of those who defied the Criterion of justice.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 34, "The Drowning of the People of Nuh",
              "When they rejected their messenger, their civilization was drowned in the deluge and made an everlasting warning for humanity.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 35, "The Obliteration of 'Ad & Thamud",
              "Mighty ancient empires possessing physical prowess and stone architecture, reduced to ruins when they defied monotheism.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 36, "The Companions of Ar-Rass",
              "Dwelling by ancient watercourses, annihilated along with numerous generations whose arrogance erased them from the earth.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 10: THE IDOLATRY OF BASE PASSIONS (HAWA)", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("The Shower of Stones, Cynical Ridicule, Worship of Whim & Sub-Bovine Degradation", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 37, "Passing by the Ruined Sodom",
              "Trading caravans passed by the city struck by the rain of stones, yet walked past without drawing moral or spiritual awakening.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 38, "The Arrogance of Public Mockery",
              "Scoffing: 'Is this the one whom Allah has sent as a messenger?'—masking their internal moral insecurity behind cynicism.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 39, "Deifying Personal Desires (Hawa)",
              "Diagnosing the ultimate root of polytheism: elevating personal lust, social pride, and ego above divine truth, creating an internal idol.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 40, "Degradation Below Grazing Cattle",
              "Beasts fulfill their instinctual purpose, while heedless humans who silence their intellect become more lost than grazing herds.")

    # ==========================================
    # PLATE 06: COSMIC SHADOWS & HYDROLOGICAL ORDER
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        6, 8,
        "THE COSMIC CANVAS: SHADOWS, NIGHT & HYDROLOGICAL MERCY",
        "Pillars 11 & 12: Extension of the Shadow, The Garment of Night, Purifying Rain & Revived Earth",
        "PLATE 06 : NATURAL ORDER"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 11: PLANETARY SHADOWS & CIRCADIAN HARMONY", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Madda az-Zill, The Solar Pointer, Gradual Retraction, Night as Garment & Sleep", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 41, "The Calibration of the Shadow (Madda)",
              "Extending the morning shadow upon earth: if Allah willed, it would be static, but the sun is made its dynamic astronomical pointer.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 42, "The Gentle Retraction (Qabdan Yasira)",
              "Drawing the shadow back with imperceptible smoothness, revealing the mathematical elegance of planetary rotation.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 43, "The Vestment of Night (Libasa)",
              "Designing darkness as an enveloping garment that grants sensory shelter, cooling, and emotional tranquility to weary creatures.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 44, "Sleep as Subat & Day as Resurrection",
              "Sleep as temporary biological cessation and the waking morning (*Nushura*) as a daily empirical demonstration of resurrection.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 12: HYDROLOGICAL MERCY & DIVINE PROVISION", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Harbinger Winds, Pure Celestial Water (Tahur), Reviving Soil & Quenching Creation", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 45, "Winds as Harbingers of Mercy",
              "Sending atmospheric currents carrying moist vapor as joyful glad tidings preceding the descent of divine rain.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 46, "Pure and Purifying Water (Ma'an Tahura)",
              "Rain descending from clouds intrinsically pristine, cleansing physical impurity and establishing the legal foundation for ritual purity.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 47, "Revival of Dead Earth (Baldatan Maytan)",
              "Restoring barren cracked deserts to green agricultural abundance, demonstrating the effortless reality of bodily resurrection.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 48, "Quenching Multitudes of Creatures",
              "Supplying vast populations of livestock and humanity with drink, inviting hearts to ponder with gratitude (*Shukr*).")

    # ==========================================
    # PLATE 07: THE MARITIME BARRIER & HUMAN LINEAGE
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        7, 8,
        "THE MARITIME BARRIER & BIOLOGICAL ANTHROPOLOGY",
        "Pillars 13 & 14: The Confluence of Waters, The Invisible Partition, Genesis from Water & Lineage",
        "PLATE 07 : WATERS & KIN"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 13: THE SANCTUARY OF TWO SEAS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Sweet Palatable River, Salty Bitter Sea, The Barzakh & Inviolable Partition", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 49, "The Convergence of Vast Waters",
              "Releasing the sweet palatable river waters alongside dense, salty, bitter ocean waters in perpetual dynamic contact.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 50, "The Unseen Barrier (Barzakh)",
              "A physical interface of differing salinity and water density that prevents one body from obliterating the other's ecology.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 51, "The Inviolable Partition (Hijran Mahjura)",
              "A natural quarantine maintaining the life-supporting properties of fresh river estuaries and maritime oceanic ecosystems.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 52, "Cosmic Harmony in Hydrological Law",
              "Demonstrating that the Lord who governs vast oceanic balances also governs the delicate spiritual balances of the human heart.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 14: BIOLOGICAL ORIGINS & SOCIAL COVENANTS", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Creation from Water, Blood Lineage (Nasab), Marital Alliance (Sihr) & Cosmic Constellations", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 53, "Creation of Man from Fluid",
              "Fashioning complex conscious humanity from a drop of humble fluid, manifesting divine architectural omnipotence.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 54, "The Bond of Blood Lineage (Nasab)",
              "Organizing human society into biological families, parents, and offspring, securing social stability and inheritance.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 55, "The Alliance of Marriage (Sihr)",
              "Binding unrelated families through legal, loving marital covenants, weaving diverse tribes into a cohesive human tapestry.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 56, "Celestial Mansions & Radiant Lamps",
              "Placing constellations (*Buruj*) in the sky, lighting the sun as a radiant lamp (*Siraj*), and the moon as reflecting light.")

    # ==========================================
    # PLATE 08: 'IBAD AR-RAHMAN - SPIRITUAL NOBILITY
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        8, 8,
        "'IBAD AR-RAHMAN : THE TAXONOMY OF SPIRITUAL ROYALTY",
        "Pillars 15 & 16: Serenity, Night Vigils, Balance, Chastity, Transmuted Sins & The Chambers of Al-Ghurfah",
        "PLATE 08 : 'IBAD AR-RAHMAN"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 15: PERSONAL HUMILITY & DEVOTIONAL EXCELLENCE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Walking with Serenity (Hawn), Peaceful Words (Salama), Night Sujood & Fear of Hell", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 57, "Walking Upon Earth with Serenity (Hawn)",
              "Treading upon the earth with grounded dignity and calm humility, free from swagger, arrogance, or anxious status-seeking.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 58, "Responding to Ignorance with Peace (Salama)",
              "When accosted by foolish provocations or toxic rhetoric, responding with composed words that guard the soul from degradation.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 59, "Nocturnal Vigils (Sujjadan wa Qiyama)",
              "Spending the private watches of the night prostrating and standing before their Lord while heedless eyes are closed in slumber.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 60, "Trembling Supplication from Hellfire",
              "Begging: 'Our Lord, avert from us the torment of Hell'—combining supreme worship with deep vulnerability before divine justice.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 16: ETHICAL PURITY, SUBLIME DU'A & AL-GHURFAH", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Economic Balance, Absolute Purity, Transmuted Sins, Noble Silence & Leaders of Taqwa", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 61, "Economic Equilibrium (Qawama)",
              "Navigating finances with wisdom: neither squandering in vain luxury (*Israf*) nor constricting in paralyzing greed (*Iqtar*).")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 62, "Sanctity of Life, Chastity & Monotheism",
              "Shunning polytheism, murder, and fornication, guarding the soul and community from the three cardinal spiritual destructions.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 63, "The Transmutation of Past Sins (Yubaddilu)",
              "Sincere tawbah that wipes out evil deeds and divinely transforms former transgressions into shining mountains of rewards.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 64, "Visionary Du'a & The Elevated Chambers",
              "Praying for families as 'coolness of eyes' and leadership in Taqwa, rewarded with the lofty palaces of Al-Ghurfah in eternal peace.")

    # Save PDF
    pdf.save(OUTPUT_PDF)
    print(f"Generated Vector Mindmap PDF: {OUTPUT_PDF}")

    # Generate PNG Previews
    cmd = f"pdftoppm -png -r 150 {OUTPUT_PDF} {os.path.join(PREVIEWS_DIR, 'al_furqan_mindmap_page')}"
    subprocess.run(cmd, shell=True, check=True)
    print(f"Rendered PNG previews in {PREVIEWS_DIR}")

    # Copy to Brain Directory for Visual Verification
    for i in range(1, 9):
        src_png = os.path.join(PREVIEWS_DIR, f"al_furqan_mindmap_page-{i}.png")
        dst_png = os.path.join(brain_dir, f"al_furqan_mindmap_page_{i}.png")
        if os.path.exists(src_png):
            shutil.copy2(src_png, dst_png)
    print(f"Copied mindmap preview plates to {brain_dir}")

if __name__ == '__main__':
    build_al_furqan_pdf()
