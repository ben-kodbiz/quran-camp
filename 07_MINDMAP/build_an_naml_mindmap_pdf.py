#!/usr/bin/env python3
"""
Huurs Studio - Surah An-Naml Master Mindmap Vector PDF Generator
16:9 Landscape Widescreen (792 x 480 pt) • 8 Plates • 16 Pillars • 64 Cards
"""

import os
import sys
import subprocess
import shutil

sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
OUTPUT_PDF = os.path.join(BASE_DIR, "AN_NAML_MASTER_MINDMAP.pdf")
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

def build_an_naml_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH AN-NAML", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
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
    # PLATE 01: ILLUMINATION & MUSA AT THE BUSH
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 8,
        "SACRED ILLUMINATION & MUSA AT THE FIRE",
        "Pillars 1 & 2: Ta-Seen, Book of Light, The Voice at the Bush, Agile Serpent & Pharaoh's Arrogance",
        "PLATE 01 : THE ILLUMINATION"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 01: THE MANIFEST SCRIPTURE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Ta-Seen, Glad Tidings for Believers, Certainty in Akhirah & Moral Blindness", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 1, "The Illuminated Openings (Ta-Seen)",
              "Signs of the Qur'an and a Manifest Book providing clear, unadulterated guidance and glad tidings to the righteous believers.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 2, "Hallmarks of Certainty (Yooqinoon)",
              "Those who establish regular prayer, give zakah in purification, and possess absolute certainty in the reality of the Hereafter.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 3, "The Blindness of the Deniers",
              "Those who deny the Akhirah have their evil deeds beautified in their sight, causing them to wander aimlessly in confusion.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 4, "Direct Transmission from the Wise",
              "Confirming that the Prophet Muhammad receives the Qur'an directly from the All-Wise, the All-Knowing (*Hakeem 'Aleem*).")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 02: THE THEOPHANY AT THE SACRED BUSH", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Seeking the Fire, The Celestial Voice, The Darting Serpent & Arrogant Rejection", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 5, "Musa Seeking the Desert Fire",
              "Seeking a burning ember to warm his freezing family in the Sinai darkness, led by divine decree toward sacred revelation.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 6, "Blessed is He at the Fire (Buriqa)",
              "A celestial proclamation from the burning bush: 'Blessed is whoever is at the fire and around it, and exalted is Allah!'")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 7, "The Darting Serpent & Radiant Hand",
              "The staff writhing like an agile serpent (*Jann*) and his hand emerging luminously white without disease, reassuring Musa's heart.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 8, "Pharaoh's Wilful Denial (Zulman wa 'Uluwwa)",
              "Rejecting the nine signs out of haughty political pride, despite their internal souls being completely convinced of their truth.")

    # ==========================================
    # PLATE 02: DAWUD, SULAYMAN & CREATION
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 8,
        "DAWUD, SULAYMAN & THE LANGUAGE OF CREATION",
        "Pillars 3 & 4: Gift of Sacred 'Ilm, Mantiq at-Tayr, Disciplined Hosts & The Ant's Excusing Voice",
        "PLATE 02 : WISDOM & CREATION"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 03: THE SOVEREIGNTY OF KNOWLEDGE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Gift of 'Ilm, Dawud's Inheritance, The Language of Birds & Disciplined Ranks", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 9, "The Elevation Through Knowledge ('Ilm)",
              "Dawud and Sulayman gifted specialized knowledge, praising Allah for favoring them above many believing servants.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 10, "Inheritance of Prophetic Stewardship",
              "Sulayman inheriting Dawud's wisdom, spiritual authority, and leadership of faith—not perishable material gold.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 11, "The Language of Birds (Mantiq at-Tayr)",
              "Taught the communicative faculties of winged creatures and granted abundance, demonstrating divine harmony across creation.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 12, "Disciplined Marshaling of Armies",
              "Assembling divisions of jinn, men, and birds in rigorous formation (*Yooza'oon*), exercising power with absolute ethical restraint.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 04: THE VALLEY OF THE ANTS & AWZI'NI", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("The Ant's Warning, Pastoral Compassion, Grateful Smile & The Sublime Supplication", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 13, "The Warning of the Female Ant",
              "Calling her colony to enter their subterranean dwellings: 'Lest Sulayman and his armies crush you while they perceive not!'")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 14, "The Ant's Supreme Husn al-Dhann",
              "Exonerating the mighty army from intentional cruelty with 'Wa hum la yash'uroon,' teaching humanity the ethics of excusing others.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 15, "The Joyful Smile of Wonder",
              "Sulayman smiling with joyful wonder at her speech, perceiving the delicate tapestry of consciousness woven by the Creator.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 16, "The Sublime Du'a of Gratitude (Awzi'ni)",
              "Begging: 'My Lord, inspire me to be grateful for Your favors upon me and my parents, and admit me among Your righteous servants.'")

    # ==========================================
    # PLATE 03: THE HOOPOE & SHEBA'S THRONE
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 8,
        "THE STRATEGIC HOOPOE & THE KINGDOM OF SHEBA",
        "Pillars 5 & 6: Inspection of Flocks, Certain News from Saba, Solar Idolatry & The Royal Missive",
        "PLATE 03 : THE DISPATCH"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 05: STRATEGIC RECONNAISSANCE OF THE HOOPOE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Inspection of Birds, Missing Scout, News from Saba & Solar Prostration", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 17, "Inspection of the Airborne Hosts",
              "Sulayman inspecting his birds with military precision, discovering the Hoopoe's absence and demanding an authenticated reason.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 18, "Certain Intelligence from Sheba (Saba)",
              "The Hoopoe returning with strategic news: 'I have grasped that which you have not grasped, and bring you from Saba certain truth.'")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 19, "A Prosperous Queen & A Great Throne",
              "Describing Queen Bilqis endowed with abundant civilizational wealth and possessing a magnificent, jewel-encrusted royal throne.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 20, "Satanic Deception: Prostrating to the Sun",
              "The Hoopoe expresses moral outrage: a civilized nation worshiping the physical sun instead of Allah, who brings forth what is hidden.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 06: THE DIPLOMATIC MISSIVE & POLITICAL WISDOM", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("The Letter of Sulayman, Innahu Min Sulaymana, Bilqis's Council & Imperial Wars", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 21, "Testing Truthfulness with the Letter",
              "Sulayman delivers a test of verification: 'We will see whether you were truthful or whether you were of the liars.'")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 22, "The Noble Letter: Innahu Min Sulaymana",
              "An official missive: 'In the name of Allah, Most Merciful, Most Compassionate: Be not haughty against me, but come in surrender.'")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 23, "Consultation of the Parliamentary Council",
              "Bilqis consulting her chieftains: they offer martial strength, but leave ultimate strategic decision-making to her political wisdom.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 24, "The Geopolitical Insight on Imperial Conquest",
              "Bilqis warns: 'Kings, when they enter a city, ruin it and make the noble humiliated'—initiating diplomatic gifts instead of war.")

    # ==========================================
    # PLATE 04: TRANSLOCATION & THE GLASS PALACE
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 8,
        "THE TRANSLOCATION OF THE THRONE & THE CRYSTAL PALACE",
        "Pillars 7 & 8: Rejecting Bribery, Twinkling of an Eye, Hadha Min Fadli Rabbi & Paved Glass",
        "PLATE 04 : THE SURRENDER"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 07: THE TRANSLOCATION OF THE THRONE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Refusing Gifts, The 'Ifrit's Offer, The Scholar of the Book & Instant Arrival", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 25, "Categorical Rejection of Material Bribery",
              "Sulayman rebuffs her gifts of silver and gold: 'What Allah has given me is far better than what He gave you; you rejoice in gifts!'")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 26, "The Challenge of Translocation",
              "Demanding her royal throne before her retinue arrives: a demonstration of miraculous divine power superseding imperial prestige.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 27, "The Powerful Jinn vs. Sacred Knowledge",
              "The 'Ifrit offers delivery before the council rises; but the one with Book Knowledge delivers it in the twinkling of an eye.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 28, "Hadha Min Fadli Rabbi (Blessings as Trial)",
              "Upon the throne's instant materialization, Sulayman proclaims: 'This is from my Lord's grace to test if I will be grateful or ungrateful!'")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 08: THE ILLUMINATING CRYSTAL PAVILION", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Disguising the Throne, Ka'annahu Huwa, The Glass Pavement & Bilqis's Conversion", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 29, "The Epistemological Test of the Throne",
              "Disguising the throne to test her discernment: she answers with brilliant balance: 'It is as if it were it,' avoiding rash errors.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 30, "The Paved Crystal Glass (Sarh Mumarrad)",
              "Invited into the pavilion, she mistakes the crystal floor over flowing water for a deep pool and uncovers her shins in caution.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 31, "The Dissolution of Optical Illusion",
              "Sulayman clarifies: 'It is a palace paved with smooth glass.' Realizing the physical sun was merely created glass, her heart awakens.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 32, "Queen Bilqis's Surrender to Allah",
              "Confessing: 'My Lord, indeed I have wronged myself, and I surrender with Sulayman to Allah, Lord of the worlds.'")

    # ==========================================
    # PLATE 05: SALIH & THE NINE CONSPIRATORS
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        5, 8,
        "SALIH'S THAMUD & THE NINE URBAN CONSPIRATORS",
        "Pillars 9 & 10: Calling to Goodness, City Divided, Nine Plotters by Night & Divine Counter-Plan",
        "PLATE 05 : THAMUD'S PLOT"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 09: SALIH & THE POLARIZED POLIS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Worship Allah, Hastening Evil Over Good, Bad Omens & Societal Division", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 33, "Salih's Mission to Thamud",
              "Sent as a brother calling them to worship Allah alone; the city immediately fractured into two disputing factions.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 34, "Hastening Evil Before Good",
              "Salih asks: 'O my people, why do you hasten what is evil before what is good? Why do you not seek forgiveness from Allah?'")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 35, "The Superstition of Evil Omens (Tatayyur)",
              "They accuse Salih: 'We see an evil omen in you and those with you.' Salih responds: 'Your omen is with Allah; you are being tested.'")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 36, "The Moral Cleavage of Society",
              "Exposing the tragic human tendency: choosing cynical obstinacy and tribal polarization over rational repentance.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 10: THE NINE PLOTTERS & THE DIVINE COUNTER-PLAN", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Tis'atu Raht, Night Assassination Conspiracy, The Hidden Plan & Desolate Mansions", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 37, "The Nine Urban Conspirators (Tis'atu Raht)",
              "In the city were nine ringleaders who spread corruption and never reformed, dominating political life with criminal deceit.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 38, "The Nocturnal Assassination Oath",
              "Swearing by Allah to ambush Salih and his household by night, then lie to his protectors: 'We did not witness their destruction!'")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 39, "The Unseen Counter-Plan of Allah",
              "They planned a stealthy plot, but Allah planned a counter-strategy while they perceived not (*Wa hum la yash'uroon*).")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 40, "Desolate Ruins of the Wrongdoers",
              "A sudden cataclysm obliterated the conspirators and their city, leaving their hewn cliff dwellings desolate ruins of remembrance.")

    # ==========================================
    # PLATE 06: THE 5 COSMIC QUESTIONS
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        6, 8,
        "THE FIVE COSMIC INTERROGATIONS: A-ILAHUN MA'ALLAH?",
        "Pillars 11 & 12: Splendid Gardens, Fixed Earth & Rivers, Answering the Desperate & Night Navigation",
        "PLATE 06 : A-ILAHUN MA'ALLAH"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 11: ECOLOGY, GEOLOGY & HYDROLOGY", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Gardens of Delight, The Stable Earth (Qarar), Mountain Anchors & The Marine Barrier", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 41, "Gardens of Splendor (Hada'iq)",
              "Who created the heavens and earth and sent rain, producing magnificent orchards whose trees you could never grow? Is there a god with Allah?")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 42, "The Stable Earth (Qarar)",
              "Who made the planet a balanced resting place for living civilization, channeling rivers through continental arteries? Is there a god with Allah?")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 43, "Mountain Anchors (Rawasiya)",
              "Fixing massive tectonic anchors to stabilize the crust against catastrophic shaking, establishing geological harmony across earth.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 44, "The Barrier Between Two Waters (Hajiz)",
              "Placing an imperceptible physical partition between sweet rivers and saline oceans, preserving vital aquatic habitats.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 12: THE ANSWERER OF THE DESPERATE SOUL", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Am-man Yujeebu al-Mudtarr, Relief of Harm, Terrestrial Succession & Celestial Guidance", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 45, "Answering the Desperate (Al-Mudtarr)",
              "Who responds to the broken, desperate soul when he calls out, and removes his agony? Is there any deity with Allah? Little do you remember!")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 46, "Successors of the Earth (Khulafa')",
              "Establishing generations as civilizational inheritors of the earth, holding power as moral stewards before the Ultimate Judge.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 47, "Guides in Pitch Darkness (Zulumat)",
              "Who guides caravans and ships through the pitch darkness of desert and ocean via the stars, sending winds as harbingers of rain?")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 48, "Origination & Cosmic Sustenance",
              "Who originates life from nothing, recreates it after death, and sustains all biology from sky and soil? Is there a deity with Allah?")

    # ==========================================
    # PLATE 07: ESCHATOLOGY & MOVING MOUNTAINS
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        7, 8,
        "ESCHATOLOGICAL PORTENTS & THE MOVING MOUNTAINS",
        "Pillars 13 & 14: Scepticism of Resurrection, Beast of Earth, Trumpet Blast & Mountains as Clouds",
        "PLATE 07 : SUN'ALLAH"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 13: THE RESURRECTION PORTENTS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Cynical Demands, The Beast of the Earth (Dabbah), Marshalling Factions & Denial", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 49, "The Cynics' Demand for the Promise",
              "Skeptics taunt: 'When is this promise if you are truthful?' The Prophet is told: 'Perhaps some of what you hasten is close behind.'")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 50, "The Emergence of the Beast (Dabbat al-Ard)",
              "When the decree falls against a heedless generation, a creature emerges from the earth to address humanity, marking true belief.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 51, "Marshalling the Deniers of Every Nation",
              "On that Day, factions who rejected divine verses are gathered in disciplined ranks, interrogated: 'Did you deny My signs without knowledge?'")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 52, "The Silence of Guilt",
              "The decree falls upon them for their injustice; they are rendered struck dumb, incapable of formulating excuses before divine justice.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 14: SUN'ALLAH: THE CRAFTSMANSHIP OF CREATION", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("The Trumpet Blast (Soor), Cosmic Terror, Mountains Passing as Clouds & Perfect Order", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 53, "The Universal Tremor of the Trumpet",
              "The blowing of the Horn: all who are in the heavens and earth are struck with terror, except those whom Allah wills to protect.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 54, "The Illusion of Motionless Mountains",
              "You behold the colossal mountains, thinking them rigid and stationary (*Jamidatan*), yet they pass smoothly like the passing of clouds.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 55, "The Sublime Artistry (Sun'allah)",
              "The flawless craftsmanship of Allah, who perfected all things (*Atqana kulla shay'*)—from cosmic orbits to geological dynamics.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 56, "The Final Balancing of Deeds",
              "Whoever brings a good deed receives better than it, safe from all terror; whoever brings an evil deed is cast headlong into the Fire.")

    # ==========================================
    # PLATE 08: PROPHETIC MISSION & DOXOLOGY
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        8, 8,
        "PROPHETIC MISSION, THE LIVING RECITATION & PRAISE",
        "Pillars 15 & 16: Worshiping Lord of Mecca, Reciting the Qur'an, Unveiling Signs & Alhamdulillah",
        "PLATE 08 : AL-HAMD"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 15: THE PROPHETIC CHARTER", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("The Lord of Mecca, Total Surrender (Islam), Reciting the Qur'an & Personal Guidance", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 57, "Worshiping the Lord of the Sanctuary",
              "Proclaiming: 'I have only been commanded to worship the Lord of this sacred city of Mecca, who has sanctified it for all creation.'")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 58, "The Command of Total Surrender",
              "Commanded to be of those who surrender wholly to Allah (*Mina al-muslimeen*), embodying humble servitude before sovereign majesty.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 59, "The Living Mandate: Reciting the Qur'an",
              "Commanded to recite the Holy Qur'an to humanity, letting its uncreated light awaken dormant souls and dismantle intellectual delusions.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 60, "Guidance as an Individual Choice",
              "Whoever chooses guidance benefits his own soul; whoever strays, the Prophet proclaims: 'I am only of the warners.'")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 16: THE UNVEILING OF SIGNS & SUPREME PRAISE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Concealed Chests, Signs on Horizons, Universal Recognition & Divine Watchfulness", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 61, "Divine Omniscience of Hidden Chests",
              "Your Lord knows what their breasts conceal and what they reveal; nothing in the heavens or earth is hidden from the Preserved Tablet.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 62, "The Promise: Sa-yureekum Ayatihi",
              "Proclaiming: 'He will show you His signs, and you will recognize them'—promising ongoing empirical confirmation across horizons.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 63, "The Universal Doxology: Alhamdulillah",
              "Concluding with supreme praise: 'All praise belongs to Allah'—anchoring all creation, knowledge, and history in divine glory.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 64, "The Ever-Watchful Sustainer",
              "A final reassuring seal: 'And your Lord is never unaware of what you do'—comforting the righteous and warning the unjust.")

    # Save PDF
    pdf.save(OUTPUT_PDF)
    print(f"Generated Vector Mindmap PDF: {OUTPUT_PDF}")

    # Generate PNG Previews
    cmd = f"pdftoppm -png -r 150 {OUTPUT_PDF} {os.path.join(PREVIEWS_DIR, 'an_naml_mindmap_page')}"
    subprocess.run(cmd, shell=True, check=True)
    print(f"Rendered PNG previews in {PREVIEWS_DIR}")

    # Copy to Brain Directory for Visual Verification
    for i in range(1, 9):
        src_png = os.path.join(PREVIEWS_DIR, f"an_naml_mindmap_page-{i}.png")
        dst_png = os.path.join(brain_dir, f"an_naml_mindmap_page_{i}.png")
        if os.path.exists(src_png):
            shutil.copy2(src_png, dst_png)
    print(f"Copied mindmap preview plates to {brain_dir}")

if __name__ == '__main__':
    build_an_naml_pdf()
