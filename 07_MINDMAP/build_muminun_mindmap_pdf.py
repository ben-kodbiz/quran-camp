#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Mu'minun Master Mindmap Vector PDF Generator
16:9 Landscape Widescreen (792 x 480 pt) • 8 Plates • 16 Pillars • 64 Cards
"""

import os
import sys
import subprocess
import shutil

sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
OUTPUT_PDF = os.path.join(BASE_DIR, "MUMINUN_MASTER_MINDMAP.pdf")
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

def build_muminun_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH AL-MU'MINUN", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
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
    # PLATE 01: THE OPENING DECALOGUE & FALAH
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 8,
        "THE OPENING DECALOGUE & THE ARCHITECTURE OF FALAH",
        "Pillars 1 & 2: Divine Guarantee of Success, Khushu' in Prayer, Shunning Laghw & The Heirs of Firdaus",
        "PLATE 01 : FALAH & HALLMARKS"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 01: THE HALLMARKS OF AUTHENTIC FAITH", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Qad Aflaha, Khushu', I'radh 'an al-Laghw & Active Zakah Purification", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 1, "The Divine Declaration of Falah",
              "The categorical assurance of ultimate cosmic flourishing and deliverance from all dread for true believers.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 2, "Reverent Presence in Prayer (Khushu')",
              "Stillness of physical limbs and deep internal awe of the heart, standing fully present before the Almighty.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 3, "Shunning Vain Distraction (Laghw)",
              "Actively disdaining corrupt talk, frivolous arguments, and soul-draining digital distractions that extinguish reflection.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 4, "Active Purification and Zakah",
              "Systematically cleansing material wealth through charity while purifying the soul continuously from greed.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 02: MORAL INTEGRITY & HEIRS OF FIRDAUS", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Hifdh al-Furuj, Custody of Trusts, Honoring Pledges & Eternal Inheritance", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 5, "The Fortress of Sexual Chastity",
              "Maintaining strict moral restraint, protecting modesty and channeling desires exclusively within lawful marriage.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 6, "Custodianship of Sacred Trusts",
              "Meticulous honesty and integrity across spiritual trusts with Allah and commercial dealings with fellow human beings.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 7, "Unbroken Fidelity to Covenants",
              "Absolute adherence to solemn agreements and social contracts, completely abhorring hypocrisy and betrayal.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 8, "The Heirs of Firdaus (Al-Warithun)",
              "Inheriting the highest, central plateau of Paradise beneath the Throne of the Merciful for all eternity.")

    # ==========================================
    # PLATE 02: EMBRYOLOGY & RESURRECTION
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 8,
        "EMBRYOLOGICAL MORPHOGENESIS & RESURRECTION",
        "Pillars 3 & 4: From Clay to Ensoulment, Ahsanul-Khaliqeen, Mortal Demise & The Second Birth",
        "PLATE 02 : MORPHOGENESIS & REBIRTH"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 03: SEVEN STAGES OF HUMAN GENESIS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Sulalah min Teen, Qararin Makeen, 'Alaqah, Mudghah & Bone Cladding", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 9, "Extract of Earth's Clay (Sulalah)",
              "Human origins rooted in the essential nutrients of soil, establishing primordial humility and kinship with earth.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 10, "The Secure Uterine Lodging",
              "Depositing the reproductive drop into the anatomically fortified fortress of the maternal womb, shielded from trauma.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 11, "The Clinging Clot & Tissue (Mudghah)",
              "Cellular differentiation into a clinging form and a compact somite-rich chewed mass under divine guidance.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 12, "Osteogenesis & Muscular Clothing",
              "Mineralizing skeletal architecture and enveloping bone structures with resilient, functional muscle fibers.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 04: ENSOULMENT & THE PROMISED REBIRTH", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Khalqan Akhar, Ahsanul-Khaliqeen, Mortal Threshold & Bodily Reconstitution", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 13, "Ensoulment into Another Creation",
              "Breathing the spirit into biological tissue, transforming organic matter into a conscious, moral, and sentient soul.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 14, "The Doxology of Design (Fa-Tabarakallah)",
              "Exalting the supreme artistry, wisdom, and aesthetic perfection of Allah, the finest and peerless Creator.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 15, "The Inevitable Mortal Transition",
              "The inescapable decree that every breathing human being will cross the biological frontier of physical death.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 16, "Bodily Resurrection on That Day",
              "Effortlessly reconstituting decomposed human bodies from the dust, demonstrating the certainty of resurrection.")

    # ==========================================
    # PLATE 03: COSMIC CANOPY & PROVISIONS
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 8,
        "THE COSMIC CANOPY & SUSTAINING PROVISIONS",
        "Pillars 5 & 6: Seven Layered Paths, Measured Rain, Subterranean Aquifers, Olive Tree & Livestock",
        "PLATE 03 : CANOPY & SUSTENANCE"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 05: CELESTIAL TRACKS & MEASURED WATER", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Sab'a Tara'iq, Measured Rainfall, Subterranean Aquifers & Power of Deprivation", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 17, "Seven Layered Celestial Tracks",
              "Majestic cosmic pathways and orbital vaults suspended above earth under uninterrupted divine protection.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 18, "Measured Descent of Rain (Bi-Qadar)",
              "Sending atmospheric rain in precise calculations, providing vital irrigation without destructive inundation.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 19, "The Subterranean Aquifer Matrix",
              "Storing vast freshwater reserves within subterranean geological vaults to sustain life across seasons.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 20, "The Divine Power of Deprivation",
              "The sobering reminder that Allah possesses absolute sovereign power to withdraw and drain all moisture away.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 06: BLESSED FLORA, LIVESTOCK & SHIPS", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Date Orchards, Sinai Olive Tree, Cattle's Wholesome Milk & Ocean Vessels", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 21, "Gardens of Palms and Vineyards",
              "Generating rich date-palm groves and fertile vines producing delectable sustenance and aesthetic tranquility.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 22, "The Sinai Olive Tree of Blessed Relish",
              "The blessed olive tree emerging from Mount Sinai, yielding soothing culinary oil and nutritious condiment for meals.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 23, "Pure Milk from Within Bellies",
              "Extracting clean, wholesome nourishment from between digestive waste and blood in domestic livestock.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 24, "Conveyance Upon Beasts and Ships",
              "Traversing arid wilderness upon sturdy camels and cutting across stormy oceans aboard buoyant vessels.")

    # ==========================================
    # PLATE 04: THE PROPHETIC CARAVAN
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 8,
        "THE PROPHETIC CARAVAN ACROSS AGES",
        "Pillars 7 & 8: The Ark of Nuh, The Overthrown Generations, Musa vs Pharaoh & Maryam's Sanctuary",
        "PLATE 04 : PROPHETS & SANCTUARY"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 07: NUH'S ARK & RUINED GENERATIONS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Monotheistic Call, Bi-A'yunina, Deluge Salvation & Arrogant Turned to Debris", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 25, "Nuh's Monotheistic Call",
              "Summoning his people to pure worship, facing false accusations of seeking personal supremacy and ambition.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 26, "Constructing the Ark (Bi-A'yunina)",
              "Building the vessel of salvation under divine inspection and inspiration amidst mockery from his community.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 27, "Boarding with Pairs & Praising Relief",
              "Boarding with animal pairs and believers, thanking Allah who rescued them from the drowning oppressors.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 28, "Arrogant Generations Turned to Flotsam",
              "Post-deluge deniers dismissing the resurrection, struck down by the Blast and reduced to dried flotsam (Ghutha').")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 08: MUSA, HARUN & MARYAM'S HAVEN", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Musa Before Pharaoh, Enslaved Kin, Drowned Despots & The Elevated Hill", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 29, "Musa and Harun Before Pharaoh",
              "Sent with clear miracles to the Egyptian court, rejected haughtily because their brethren were enslaved.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 30, "The Annihilation of the Despots",
              "Drowning Pharaoh and his ministers in their obstinacy, establishing an enduring sign of tyrant overthrows.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 31, "Maryam and 'Isa as an Eternal Sign",
              "Making the mother and her virgin-born son an enduring monument of divine power and immaculate piety.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 32, "The Elevated Tranquil Haven (Rabwah)",
              "Sheltering mother and child upon a fertile, elevated terrace blessed with flowing springs and serenity.")

    # ==========================================
    # PLATE 05: COMMISSION OF PURITY & SINCERITY
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        5, 8,
        "COMMISSION OF PURITY & SINCERE HEARTS",
        "Pillars 9 & 10: Wholesome Sustenance, The One Ummah, Sectarian Factionalism & Trembling Hearts",
        "PLATE 05 : PURITY & SINCERITY"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 09: PURE DIET & THE UNITED UMMAH", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Kulu Min al-Tayyibat, Righteous Action, Ummatan Wahidah & Sectarian Hubris", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 33, "Mandate of Wholesome Diet (Tayyibat)",
              "Commanding all messengers to consume pure, halal sustenance as the essential foundation for accepted righteous deeds.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 34, "The Link of Halal and Action",
              "Unlawful earnings poisoning the spiritual heart, blunting prayers and nullifying good works in the divine sight.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 35, "The Primordial Single Ummah",
              "Affirming that the prophetic mission constitutes one unified spiritual fraternity worshipping the one Lord.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 36, "Sectarian Fragmentation (Zuburan)",
              "Condemning those who splintered religion into competing factions, each sect arrogantly exulting in its narrow views.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 10: THE TREMBLING HEARTS (WAJILAH)", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Wealth Delusions, Reverent Awe, Qulubuhum Wajilah & Racing to Good Deeds", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 37, "The Delusion of Material Wealth",
              "Arrogant tycoons falsely assuming children and wealth indicate divine pleasure, blind to their spiritual peril.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 38, "Reverent Awe of the Awake Heart",
              "Believers who tremble before the majesty of Allah, maintaining pristine monotheism free from subtle partnership.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 39, "Giving with Trembling Hearts (Wajilah)",
              "Performing prayer, fasting, and charity while trembling with fear that their offerings fall short of acceptance.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 40, "Racing to Forefront Excellence",
              "Transforming humble reverence into urgent action, racing eagerly to capture every opportunity for righteousness.")

    # ==========================================
    # PLATE 06: PRIDE & THE THRESHOLD OF DEATH
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        6, 8,
        "THE ANATOMY OF PRIDE & THE BARZAXH",
        "Pillars 11 & 12: Opulence Induced Deafness, Rabbi Irji'oon, The Chilling Kalla & The Impenetrable Barrier",
        "PLATE 06 : PRIDE & THE BARZAKH"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 11: HAUGHTINESS & THE HARDENED HEART", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Turning on Heels, Unpaid Truth, Hardening Under Trial & The Sudden Gate", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 41, "Turning on Heels in Disdain",
              "The affluent elite fleeing from divine reminders, deafened by self-admiration and intoxicating worldly power.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 42, "The Messenger Free from Greed",
              "Recognizing that the Prophet demands no financial compensation, guiding humanity solely to the upright path.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 43, "Hardening Under Adversity",
              "Defiant souls refusing to humble themselves or pray when afflicted with trials, entrenching their stubborn rebellion.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 44, "The Sudden Gate of Retribution",
              "Opening unexpected gates of severe chastisement upon unrepentant rebels, leaving them in frozen bewilderment.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 12: THE MOMENT OF DEATH & THE BARZAKH", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Rabbi Irji'oon, The Chilling Kalla, The Impenetrable Barrier & Finality", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 45, "The Panic at Death (Rabbi Irji'oon)",
              "The dying sinner weeping in terror when the veil lifts, begging desperately to be returned to earth to do good.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 46, "The Chilling Divine Rejection (Kalla!)",
              "Dismissing the panicked plea as an empty word uttered in terror, permanently sealing the earthly testing ground.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 47, "The Impenetrable Barzakh Barrier",
              "The metaphysical boundary separating deceased souls from the material world until the Day of Resurrection.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 48, "The Irreversible Finality of Life",
              "The stark realization that earthly mortality is the solitary, non-repeatable chance to build an eternal destiny.")

    # ==========================================
    # PLATE 07: THE SOUNDING HORN & SCALES
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        7, 8,
        "THE SOUNDING HORN & THE COSMIC SCALES",
        "Pillars 13 & 14: Dissolution of Lineages, Heavy vs Light Scales, Kalihun Agony & The Terrifying Rebuke",
        "PLATE 07 : HORN & SCALES"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 13: DISSOLVED LINEAGES & THE SCALES", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Fala Ansaba Baynahum, The Cosmic Balance, Heavy Scales & Forfeited Souls", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 49, "The Trumpet and Dissolved Lineages",
              "The cosmic blast rendering all earthly ancestry, family status, and tribal nepotism completely void and meaningless.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 50, "The Silent Gathering of Souls",
              "Humanity standing naked and humbled before the Creator, stripped of all worldly defenses and unable to question kin.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 51, "The Heavy Scales of Realized Falah",
              "Sincere prayers, charity, and ethical deeds tilting the cosmic scales to unlock eternal triumph and delight.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 52, "The Barren Scales of Lost Souls",
              "Light scales resulting from hypocrisy and denial, culminating in the irreversible loss of one's own eternal soul.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 14: THE AGONY & THE GREAT REBUKE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Kalihun Grimace, Admitted Misguidance, Ikhsa'u Fiha & Triumphant Believers", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 53, "Scorched Faces and Grimaces (Kalihun)",
              "Inmates of the fire suffering scorched expressions, lips retracted and teeth bared in unending agony.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 54, "Confession of Wretchedness",
              "Admitting that divine messengers recited truth, but personal rebellion and spiritual misfortune prevailed.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 55, "The Terrifying Rebuke (Ikhsa'u Fiha)",
              "The devastating divine decree: 'Remain despised therein and speak not to Me!', shattering every hope of rescue.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 56, "Vindication of the Mocked Believers",
              "The patient believers who endured ridicule on earth crowned as the supreme, joyful victors of eternity.")

    # ==========================================
    # PLATE 08: THE PURPOSEFUL COSMOS & MERCY
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        8, 8,
        "THE PURPOSEFUL UNIVERSE & THE FINAL LITURGY",
        "Pillars 15 & 16: The Ephemeral Day, Refuting Nihilism ('Abathan), The True Sovereign & Khayrur-Rahimeen",
        "PLATE 08 : PURPOSE & MERCY"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 15: THE EPHEMERAL DAY & TELEOLOGY", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Labithna Yawman, Wasted Millennia, Refuting 'Abathan & Al-Malik al-Haqq", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 57, "The Fleeting Illusion of Lifespan",
              "Humanity looking back upon decades of earthly living and seeing it shrink to a single day or a fleeting afternoon.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 58, "The Tragic Folly of Wasted Years",
              "The crushing sorrow of discovering that earthly centuries were squandered on vanity instead of eternal preparation.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 59, "Refutation of Nihilism ('Abathan)",
              "Dismantling atheistic meaninglessness: the cosmos and human consciousness were not created for purposeless play.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 60, "The Exalted Sovereign (Al-Malik al-Haqq)",
              "Exalting Allah, the Supreme King and Ultimate Reality, Sovereign of the magnificent Throne of Glory.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 16: THE REFUGE OF ULTIMATE MERCY", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Baseless Invocations, Defeated Disbelief, Rabbi Ighfir Warham & Khayrur-Rahimeen", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 61, "The Void of False Deities",
              "Invoking created powers alongside Allah without proof, leading to inescapable accounting and spiritual defeat.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 62, "The Certain Defeat of Disbelief",
              "The immutable spiritual axiom that those who reject divine reality shall never attain lasting success.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 63, "The Sublime Closing Liturgy",
              "The Prophet commanded to utter the eternal plea: 'My Lord, forgive and have mercy upon us.'")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 64, "The Best of the Merciful (Khayrur-Rahimeen)",
              "Sealing the surah with unconditional reliance upon Allah, the supreme source of boundless grace and mercy.")

    pdf.save(OUTPUT_PDF)
    print(f"Master Mindmap PDF successfully compiled at: {OUTPUT_PDF}")

    # Generate Previews
    cmd = f"pdftoppm -png -r 150 {OUTPUT_PDF} {PREVIEWS_DIR}/muminun_page"
    subprocess.run(cmd, shell=True, check=True)
    print("PNG Previews rendered in previews directory.")

    # Copy to brain dir
    for i in range(1, 9):
        src = f"{PREVIEWS_DIR}/muminun_page-{i}.png"
        dst = os.path.join(brain_dir, f"muminun_page-{i}.png")
        if os.path.exists(src):
            shutil.copyfile(src, dst)
            print(f"  Copied {src} -> {dst} ({os.path.getsize(dst):,} bytes)")

if __name__ == "__main__":
    build_muminun_pdf()
