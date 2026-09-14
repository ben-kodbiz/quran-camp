#!/usr/bin/env python3
"""
Huurs Studio - Surah As-Sajdah Master Mindmap Vector PDF Generator
16:9 Landscape Widescreen (792 x 480 pt) • 10 Plates • 20 Pillars • 80 Cards
Strict Brand_Visual_System.md & Absolute Copyright Insulation
EXPANDED EDITION: Prophetic Friday Fajr Sunnah, Cosmic Creation & The Nocturnal Vigil
"""

import os
import sys
import subprocess
import shutil

sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
OUTPUT_PDF = os.path.join(BASE_DIR, "AS_SAJDAH_MASTER_MINDMAP.pdf")
PREVIEWS_DIR = os.path.join(BASE_DIR, "previews_as_sajdah")
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

def build_as_sajdah_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH AS-SAJDAH (EXPANDED JUMU'AH EDITION)", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
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
        pdf.text("EXPANDED PROPHETIC FRIDAY EDITION  *  80 ANALYTICAL CARDS  *  READ. REFLECT. RETURN.", w - 465, 16, font="F2", size=7.0, rgb=GOLD_LIGHT)

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
    # PLATE 01: THE LITURGICAL DAWN & DIVINE DESCENT
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 10,
        "THE FRIDAY FAJR SUNNAH & THE BOOK OF TRUTH",
        "Pillars 1 & 2: Weekly Prophetic Recitation, Alif-Lam-Meem & Tanzil al-Kitab",
        "PLATE 01 : FRIDAY DAWN"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 01: THE PROPHETIC FRIDAY FAJR SUNNAH", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Canonical Recitation, Sayyid al-Ayyam & The Bedtime Shield", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 1, "The Canonical Friday Dawn Recitation",
              "Sahih al-Bukhari 891 & Muslim 880: The Prophet ﷺ consistently recited Surah As-Sajdah in full in Friday Fajr's first rak'ah.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 2, "Cosmic Rationale: Master of Days",
              "Ibn al-Qayyim in Zad al-Ma'ad: Friday contains Adam's creation, paradise entry, earth descent, death, and ultimate resurrection.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 3, "The Nightly Bedtime Safeguard",
              "Jami' at-Tirmidhi 2892: The Prophet ﷺ never retired to sleep at night until reciting Surah As-Sajdah and Surah Al-Mulk.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 4, "Weekly Re-awakening of the Ummah",
              "Standing in dawn twilight to hear the complete saga of human origin, earthly duty, appointed death, and eternal reckoning.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 02: DESCENT OF THE INIMITABLE BOOK", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Alif-Lam-Meem, La Rayba Feeh & Refuting Slander of Fabrication", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 5, "Alif-Lam-Meem: Linguistic Inimitability",
              "Opening with detached letters challenging human rhetoric, asserting that divine revelation transcends all mortal composition.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 6, "Tanzil al-Kitab La Rayba Feeh",
              "The descent of the Book, entirely free of doubt, originates from the Lord of the worlds, carrying absolute ontological truth.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 7, "Dismantling Claims of Fabrication",
              "Am yaqooloona iftarah: refuting pagan slanders; Muhammad ﷺ did not invent it; it is transcendent revelation from your Lord.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 8, "Warning the Unwarned Civilization",
              "Sent as unadulterated truth to awaken a people to whom no warner had previously come, guiding them to eternal salvation.")

    # ==========================================
    # PLATE 02: THE COSMIC HEXAD & THE THOUSAND-YEAR DAY
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 10,
        "COSMIC ARCHITECTURE & DIVINE GOVERNANCE",
        "Pillars 3 & 4: Sittati Ayyam, Istiwa' over the Throne & Yudabbiru al-Amr",
        "PLATE 02 : COSMIC GOVERNANCE"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 03: THE HEXAD & THRONE ASCENT", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Creation in Six Epochs, Istiwa' & The Absence of Intercessors", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 9, "Creation in Six Divine Epochs",
              "Created the heavens, earth, and cosmic expanse in six days (Sittati Ayyam), demonstrating sequential harmony and order.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 10, "Istiwa' 'ala al-'Arsh Without Modality",
              "Ascended over the Supreme Throne in a manner befitting transcendent majesty, without bodily modality (Bila Kayf).")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 11, "Sole Sovereignty: No Wali or Shafee'",
              "Creation possesses no autonomous guardian or intercessor apart from Allah; all false deities are impotent illusions.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 12, "The Exhortation to Reflection",
              "Afa-la tatadhakkaroon: will you not awaken your cognitive faculties to recognize the singular Lord of cosmic dominion?")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 04: THE THOUSAND-YEAR GOVERNING DAY", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Yudabbiru al-Amr, Angelic Velocity & Escaping Human Myopia", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 13, "Yudabbiru al-Amr: Directing All Affairs",
              "From highest heaven to terrestrial earth, every planetary orbit, rain droplet, and human breath is divinely steered.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 14, "Ascension of the Cosmic Ledger",
              "Then the decree and reports of human actions ascend to Him across celestial distances governed by divine commands.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 15, "A Single Day of 1,000 Human Years",
              "Miqdaruhu alfa sanah: angelic velocities traversing cosmic distances in one day equivalent to ten centuries of human transit.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 16, "Curing Anthropocentric Panic",
              "Human anxiety operates on micro-seconds; the Sovereign manages the universe across vast scales where divine justice matures.")

    # ==========================================
    # PLATE 03: THE DUAL GENESIS: CLAY & DESPISED FLUID
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 10,
        "THE DUAL MORPHOGENESIS OF HUMANITY",
        "Pillars 5 & 6: Bada'a Khalqa al-Insan min Teen & Sulalah min Ma'in Maheen",
        "PLATE 03 : HUMAN GENESIS"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 05: ADAM'S PRIMORDIAL CLAY GENESIS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Ahsana Kulla Shay'in, Soil Mixture & The Antidote to Arrogance", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 17, "Ahsana Kulla Shay'in Khalaqah",
              "He perfected everything He created: all biological forms and physical laws reflect flawless wisdom, utility, and elegance.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 18, "Commenced Creation from Clay (Teen)",
              "Bada'a khalqa al-insani min teen: Adam was molded directly from earthly mud, grounding human origin in terrestrial soil.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 19, "The Soil Antidote to Human Pride",
              "Regardless of empire or pedigree, human physical architecture is common dirt; strutting across the earth contradicts one's substance.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 20, "Universal Biological Baseline",
              "All human races and nations share identical soil origins; nobility before Allah is earned strictly through Taqwa.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 06: OFFSPRING FROM DESPISED FLUID", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Sulalah Extraction, Ma'in Maheen & Embryonic Frailty", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 21, "Sulalah: The Refined Biological Extract",
              "Thumma ja'ala naslahu min sulalah: progeny is reproduced from a delicate extract drawn from vast volumes of seminal fluid.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 22, "Ma'in Maheen: The Base Despised Fluid",
              "A base, fragile droplet of liquid that must be washed from garments; an undeniable reminder of human physical dependency.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 23, "Embryonic Gestation in Sanctuary",
              "Concealed within maternal darkness, the microscopic extract is miraculously preserved, cell by cell, into living tissue.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 24, "From Weak Fluid to Decaying Dust",
              "A creature starting as despised fluid and ending as a subterranean corpse has zero justification for philosophical arrogance.")

    # ==========================================
    # PLATE 04: ENSOULMENT & THE TRIAL OF SKEPTICISM
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 10,
        "THE INBREATHING OF THE SOUL & SKEPTICAL DISINTEGRATION",
        "Pillars 7 & 8: Nafkh ar-Ruh, As-Sam' wal-Absar & Dalalna fil-Ard",
        "PLATE 04 : THE SOUL & SKEPTICISM"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 07: PROPORTIONING & SENSORY ENDOWMENT", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Taswiyah, Inbreathing of Spirit & The Triad of Consciousness", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 25, "Taswiyah: Proportioned Morphology",
              "Thumma sawwahu: balancing the limbs, neural faculties, and physiological systems into a harmonious, upright biological vessel.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 26, "Nafkh ar-Ruh: The Created Spirit",
              "Nafakha feehi min roohihi: breathing the honored spirit into the vessel, elevating animal biology into a conscious moral agent.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 27, "The Sensory Triad: Hearing, Sights, Hearts",
              "As-Sam' (singular for revelation), Absar, and Af'idah: granting sensory and cognitive receptors to perceive divine truth.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 28, "The Tragic Ingratitude (Qaleelan)",
              "Qaleelan ma tashkuroon: despite these transcendent faculties, man rarely utilizes them in gratitude and obedience to the Giver.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 08: DISINTEGRATION & DENIED MEETING", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Dalalna fil-Ard, The Lost Milk Analogy & Root of Disbelief", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 29, "The Skeptic's Materialist Query",
              "A-idha dalalna fil-ardi a-inna la-fee khalqin jadeed: when we dissolve into subterranean earth, shall we indeed be recreated?")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 30, "The Analogy of Dissolution (Dalalna)",
              "Like milk vanished into vast water or dust dispersed across earth leaving no visible trace; doubting reassembly.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 31, "Unmasking the True Psychological Root",
              "Bal hum bi-liqa'i rabbihim kafiroon: their skepticism is not scientific inquiry; it is desperate denial of moral accountability.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 32, "Materialism as an Ethical Escape",
              "Denying the afterlife to indulge hedonistic desires without the terror of divine reckoning; an intellectual smoke-screen.")

    # ==========================================
    # PLATE 05: THE ANGEL OF DEATH & THE DAY OF REGRET
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        5, 10,
        "THE CUSTODIAL EXTRACTION & THE SHAME OF CRIMINALS",
        "Pillars 9 & 10: Malak al-Mawt, Nakkisoo Ru'oosihim & Inna Naseenakum",
        "PLATE 05 : DEATH & SHAME"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 09: CUSTODY OF THE ANGEL OF DEATH", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Yatawaffakum, Assigned Precision & The Immediate Sovereign Return", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 33, "Yatawaffakum: The Complete Extraction",
              "Tawaffa signifies claiming something fully down to the last penny; death is an official, exhaustive custodial departure.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 34, "Malak al-Mawt Assigned by Name",
              "Alladhi wukkila bikum: specifically appointed to every soul; no individual escapes, no coordinate is lost or confused.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 35, "The Host of Assisting Angels",
              "Angels drawing the soul systematically through veins and limbs to the throat, where the Angel of Death performs extraction.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 36, "The Direct Return to Allah",
              "Thumma ila rabbikum turja'oon: no intermediate wandering; the soul stands immediately before its Creator for judgment.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 10: THE PARALYZING SHAME OF CRIMINALS", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Nakkisoo Ru'oosihim, Futile Pleas & The Absolute Abandonment", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 37, "Downcast Heads in Deep Humiliation",
              "Nakkisoo ru'oosihim: arrogant tyrants who strutted on earth standing with chins collapsed on chests in utter disgrace.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 38, "Belated Vision: Absarna wa Sami'na",
              "Our Lord, now we see and hear! The veil is shredded, angels and Hell are visible, but late visual conviction is useless.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 39, "The Futile Begging for a Second Chance",
              "Farji'na na'mal salihan inna mooqinoon: begging to be sent back to mortal earth to perform deeds; rejected unconditionally.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 40, "Inna Naseenakum: Divine Abandonment",
              "Taste the torment for forgetting the meeting of this Day; as you abandoned divine truth, you are abandoned in the flames.")

    # ==========================================
    # PLATE 06: THE PROSTRATION OF THE UNARROGANT
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        6, 10,
        "THE HALLMARK OF BELIEF & RECITATION PROSTRATION",
        "Pillars 11 & 12: Kharroo Sujjadan, Sabbahoo bi-Hamdi Rabbihim & Sajdat al-Tilawah",
        "PLATE 06 : PROSTRATION"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 11: PHYSICAL SURRENDER TO REVELATION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Innama Yu'minu, Kharroo Sujjadan & Dismantling Pride", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 41, "Innama Yu'minu: Exclusive Hallmark",
              "Only those truly believe in Our signs who, upon hearing them, respond with spontaneous, total physical and spiritual surrender.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 42, "Kharroo Sujjadan: Gravitational Collapse",
              "Kharra denotes collapsing downward instantly, as if pulled by divine gravity; no hesitation, intellectual bargaining, or delay.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 43, "Forehead Placed in Common Soil",
              "Placing the highest anatomical dignity—the forehead—upon dirt, acknowledging absolute servanthood before the Creator.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 44, "Wa Hum La Yastakbiroon: Purging Arrogance",
              "The root of all rebellion is Kibr (pride); prostration physically and psychologically extracts pride from the human soul.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 12: DOXOLOGY & SAJDAT AL-TILAWAH", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Tasbeeh, Tahmeed, Sunni Consensus & Friday Fajr Climax", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 45, "Conjoined Tasbeeh and Tahmeed",
              "Sabbahoo bi-hamdi rabbihim: affirming Allah's absolute freedom from flaws while praising His limitless majesty and grace.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 46, "Sunni Consensus on Sajdat al-Tilawah",
              "All four Sunni madhhabs confirm the prostration of recitation upon reciting or hearing Verse 15; a verified liturgical act.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 47, "The Friday Fajr Congregational Prostration",
              "Imam and congregation falling simultaneously in dawn silence at this verse, exemplifying the living sunnah of the Messenger ﷺ.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 48, "Subhana Rabbiy al-A'la Proclaimed",
              "Glory to my Lord the Most High: proclaiming divine supremacy while the human body is at its lowest physical elevation.")

    # ==========================================
    # PLATE 07: THE NIGHT VIGIL & CONCEALED DELIGHTS
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        7, 10,
        "THE NOCTURNAL TEAR & ETERNAL RECOMPENSE",
        "Pillars 13 & 14: Tatajafa Junubuhum, Khawfan wa Tama'an & Qurratu A'yun",
        "PLATE 07 : NIGHT VIGIL"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 13: SIDES FORSAKING SLUMBER", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Tatajafa, Tahajjud Vigil, Dual Wings of Fear/Hope & Secret Infaq", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 49, "Tatajafa: The Sacred Restlessness",
              "Their sides find no ease upon comfortable mattresses; a divine ache pulls them out of warm beds into the silent night vigil.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 50, "Tahajjud: The Sanctuary of Saints",
              "Performing cold wudu while humanity sleeps, standing alone before the Lord in intimate, tearful communion and prayer.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 51, "Dual Wings: Khawfan wa Tama'an",
              "Invoking Him in balanced reverence: fearing shortcomings and divine justice while eagerly longing for His boundless mercy.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 52, "Nocturnal Prayer Coupled with Charity",
              "Wa mimma razaqnahum yunfiqoon: pairing hidden spiritual devotion by night with generous social charity by day.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 14: QURRATU A'YUN: CONCEALED DELIGHTS", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Ukhfiya Symmetrical Reward, Cool Radiant Eyes & Hadith Qudsi", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 53, "Ukhfiya: Symmetrical Concealment",
              "Because they concealed their night prayers from human eyes, Allah concealed their eternal reward from all creation.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 54, "Qurratu A'yun: Radiant Joy of Eyes",
              "In Arabic, tears of joy cool the eye; the rewards of Jannah quench all earthly grief with eternal delight and ecstasy.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 55, "The Supreme Hadith Qudsi of Paradise",
              "Sahih al-Bukhari 3244: 'What no eye has seen, no ear has heard, and has never crossed the heart of any human being.'")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 56, "Incomparability to Mortal Dunya",
              "All worldly luxuries fade and disappoint; the hidden banquets of eternity provide infinite, unfading satisfaction.")

    # ==========================================
    # PLATE 08: RADICAL DIVERGENCE & LESSER PUNISHMENT
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        8, 10,
        "THE TWO DESTINIES & WORLDLY WAKE-UP CALLS",
        "Pillars 15 & 16: La Yastawoon, Jannatu al-Ma'wa & Al-'Adhab al-Adna",
        "PLATE 08 : TWO DESTINIES"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 15: THE RADICAL ONTOLOGICAL INEQUALITY", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("La Yastawoon, Gardens of Refuge & The Inescapable Fire", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 57, "Afa-man Kana Mu'minan: Radical Inequality",
              "Is the believer equal to the corrupt transgressor (Fasiq)? La yastawoon! They are fundamentally unequal in character and fate.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 58, "Jannatu al-Ma'wa: The Eternal Sanctuary",
              "Believers dwell in the Gardens of Refuge, received with divine hospitality (Nuzulan) for their righteous earthly struggle.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 59, "Ma'wahumu an-Nar: The Flaming Prison",
              "The transgressors have their abode in the Fire; every time they attempt to crawl out of its agony, they are driven back.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 60, "Taste What You Used to Deny",
              "Endless confrontation with the truth they mocked: 'Taste the punishment of the Fire which you used to deny in arrogance.'")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 16: AL-'ADHAB AL-ADNA: MERCIFUL TRIALS", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Lesser Worldly Calamities, La'allahum Yarji'oon & Retribution", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 61, "The Lesser Punishment Before the Greater",
              "Wa la-nudheeqannahum mina al-'adhabi al-adna: tasting earthly trials before the catastrophic greater torment of Hell.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 62, "Worldly Calamities as Merciful Alarms",
              "Droughts, illnesses, economic crises, and defeats (like Badr) designed to shatter self-sufficiency and awaken repentance.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 63, "La'allahum Yarji'oon: The Sole Divine Goal",
              "Trials are not gratuitous malice; their ultimate pedagogical purpose is that wandering souls may repent and return to God.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 64, "Retribution from the Willfully Blind",
              "Who is more unjust than one reminded of Allah's verses who turns away in pride? From the criminals We will exact retribution.")

    # ==========================================
    # PLATE 09: MUSA'S TORAH & THE PILLARS OF LEADERSHIP
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        9, 10,
        "PROPHETIC CONTINUITY & SPIRITUAL LEADERSHIP",
        "Pillars 17 & 18: Musa's Scripture & Leadership Through Sabr and Yaqeen",
        "PLATE 09 : LEADERSHIP"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 17: PROPHETIC REVELATION & PRECEDENT", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Musa's Scripture, Guidance for Bani Isra'il & Fraternity", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 65, "The Torah Granted to Musa",
              "We gave Moses the Book, confirming that divine revelation is an unbroken chain of guidance delivered across history.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 66, "Be in No Doubt of Meeting Him",
              "Fa-la takun fee miryatin min liqa'ih: confirming the reality of revelation and prophetic fraternity across the ages.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 67, "Guidance for the Children of Israel",
              "Revealing a divine law to liberate a subjugated people and structure their society in moral justice and righteousness.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 68, "The Single Lineage of Monotheism",
              "The message of Muhammad ﷺ confirms and culminates the exact message of Musa; pure monotheism without distortion.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 18: THE TWIN PILLARS OF LEADERSHIP", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("A'immah Yahdoon, Sabr Against Desires & Yaqeen Against Doubts", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 69, "A'immatan Yahdoona bi-Amrina",
              "We appointed leaders from among them guiding by Our command; true leadership serves divine truth rather than human ego.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 70, "Lamma Sabaroo: The Pillar of Sabr",
              "Appointed when they exercised patient endurance: resisting base desires, persevering through persecution, and holding the line.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 71, "Kanoo bi-Ayatina Yooqinoon: Yaqeen",
              "Held unwavering certainty in Our signs: possessing deep intellectual and spiritual certitude that destroys every doubt.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 72, "The Golden Axiom of Ibn Taymiyyah",
              "'Bi-Sabri wal-Yaqeeni tunalu al-imamatun fid-deen': through patience and certainty alone is spiritual leadership achieved.")

    # ==========================================
    # PLATE 10: PAST RUINS, RAIN REVIVAL & DAY OF DECISION
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        10, 10,
        "PETRIFIED RUINS, REBIRTH & THE FINAL ULTIMATUM",
        "Pillars 19 & 20: Yamshoona fee Masakinihim, Ard Jurooz & Yawm al-Fath",
        "PLATE 10 : FINAL DECISION"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 19: SILENT RUINS & RAIN RESURRECTION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Walking in Vanished Homes, Ard Jurooz & Hydrologic Rebirth", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 73, "Walking Among Destroyed Civilizations",
              "Yamshoona fee masakinihim: caravans walking among petrified ruins of fallen empires; why do you think you are immune?")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 74, "Al-Ard al-Jurooz: Barren Concrete Earth",
              "Land baked hard and stripped bare of all vegetation under scorching sun, resembling total biological death.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 75, "Nasooqu al-Ma'a: Herding Cloud Oceans",
              "Driving celestial water to dead soil, erupting into green crops providing sustenance for cattle and human survival.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 76, "Empirical Proof of Bodily Resurrection",
              "He who effortlessly revitalizes barren dirt with descending rain will resurrect decayed human bones from graves.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 20: SKEPTIC MOCKERY & YAWM AL-FATH", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Mata Hadha al-Fath, Futile Late Faith & The Prophetic Stance", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 77, "The Mocking Sneer: Mata Hadha al-Fath?",
              "When is this victory and decisive judgment, if you are truthful? Impatient arrogance demanding immediate doom.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 78, "Yawm al-Fath: The Day of Decision",
              "The Day of Final Judgment when truth is manifest, the cosmos dissolves, and divine justice is irrevocably executed.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 79, "The Futility of Belated Profession",
              "La yanfa'u alladhina kafaroo eemanuhum: belief upon witnessing punishment is utterly rejected; no respite is granted.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 80, "Fa-A'rid 'Anhum Wantazir: Calm Certainty",
              "Turn away from their insolence and wait with serene dignity; the believers await Paradise, while the deniers await judgment.")

    pdf.save(OUTPUT_PDF)
    print(f"[OK] Generated {OUTPUT_PDF}")

    # Generate preview PNGs
    cmd = f"pdftoppm -png -r 150 {OUTPUT_PDF} {PREVIEWS_DIR}/page"
    subprocess.run(cmd, shell=True, check=True)
    print(f"[OK] Generated preview images in {PREVIEWS_DIR}")

    # Copy to brain dir
    for i in range(1, 11):
        src = f"{PREVIEWS_DIR}/page-{i:02d}.png" if os.path.exists(f"{PREVIEWS_DIR}/page-{i:02d}.png") else f"{PREVIEWS_DIR}/page-{i}.png"
        dst = f"{brain_dir}/as_sajdah_mindmap_page_{i}.png"
        if os.path.exists(src):
            shutil.copyfile(src, dst)
            print(f"[OK] Copied preview to {dst}")
        else:
            print(f"Warning: preview file {src} not found")

if __name__ == "__main__":
    build_as_sajdah_pdf()
