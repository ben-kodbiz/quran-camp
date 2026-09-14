#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Baqarah Part 2 Master Landscape Mindmap PDF Compiler
Foundation Media: Part 2 Audio Lecture (Duration: 01:59:44)
Strict Standardization:
- Title: Surah Al-Baqarah — Part 2
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
OUTPUT_PDF = os.path.join(BASE_DIR, "BAQARAH_PART_02_MINDMAP.pdf")

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

def build_part02_pdf():
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
        pdf.text(f"FOUNDATION MEDIA: PART 2 ({time_badge})", w - 282, h - 20, font="F2", size=6.8, rgb=EMERALD)
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
    # PAGE 1: THE PRIMORDIAL GENESIS & THE TRIAL OF KNOWLEDGE
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 4,
        "THE PRIMORDIAL GENESIS & THE TRIAL OF KNOWLEDGE",
        "Pillars 1 & 2: Earthly purpose, refutation of original sin, cognitive nouns, and the hubris of Iblis",
        "PART 2 : SECTION 1",
        "00:00 - 26:38"
    )

    # Column 1: Pillar 1 (The Earthly Decree & Stewardship)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 1: THE EARTHLY STEWARDSHIP", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Earthly Decree, Refutation of Original Sin & Angels' Query", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c1_x + c1_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=0.6)
    pdf.text("00:00 - 12:38", c1_x + c1_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    # Card 1A: Earthly Purpose & Negation of Original Sin
    y_c = c1_y + c1_h - 48
    pdf.text("1. Purpose from Day 1: Earthly Stewardship (Khalifah)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Inni ja'ilun fil-ardi khalifah': Decreed for earth before the tree, temptation, or slip.\n"
        "- Completely negates Christian Original Sin: earth is NOT a punitive prison or curse.\n"
        "- Humans are born upon pristine Fitrah; children dying before maturity enter Paradise directly."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 1B: Lexical Root of Khalifah
    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Lexical Definition: Generational Succession (Ibn Kathir)", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Yakhlufu ba'duhum ba'da': Successive generations reproducing across time.\n"
        "- Unlike static angelic beings, humans propagate lineage and inherit moral stewardship.\n"
        "- Rejects 'vicegerent of God' dogma: Allah rules directly without deputies."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 1C: Angels' Query
    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. The Angels' Incomprehension: Corruption & Bloodshed", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'A-taj'alu feeha man yufsidu feeha wa yasfikud-dima'': Anticipated violence and greed.\n"
        "- Humans with free will, desire, and rage will inevitably cause civil discord (Fasad).\n"
        "- Angels contrast this with their ceaseless Tasbih and Hamd."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 1D: Justification of Creation
    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Divine Mystery: 'I Know What You Do Not Know'", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Inni a'lamu ma la ta'lamun': The angels were right about the masses, but wrong about the elite.\n"
        "- A chosen minority—prophets, martyrs, and sincere believers who freely choose virtue over vice—justify the entire magnificent creation of humanity."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Center Gap Connector Bridge
    pdf.line(c1_x + c1_w, bridge_y, c2_x, bridge_y, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(w/2 - 12, bridge_y - 8, 24, 16, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=0.8)
    pdf.text_centered("->", w/2, bridge_y + 3, font="F2", size=7, rgb=GOLD_LIGHT)

    # Column 2: Pillar 2 (Conceptual Language & Iblis's Hubris)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 2: COGNITIVE NOUNS & IBLIS'S PRIDE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Terminology Gift, Angelic Submission & Hidden Arrogance", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c2_x + c2_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=0.6)
    pdf.text("12:39 - 26:38", c2_x + c2_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    # Card 2A: Cognitive Endowment
    y_c = c1_y + c1_h - 48
    pdf.text("1. The Cognitive Endowment: All Language Built on Nouns", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Wa 'allama Adama al-asma'a kullaha': Taught Adam vocabulary and conceptual taxonomy.\n"
        "- In linguistic science, every discipline (medicine, physics, agriculture) reduces to terminology.\n"
        "- Modern skyscrapers and technology are manifestations of this divine cognitive spark."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 2B: Angelic Submission
    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Angelic Submission: Subhanaka La 'Ilma Lana", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Challenged to name concepts, angels surrender: 'Glory be to You! We have no knowledge except what You taught us; You are the All-Knowing, All-Wise.'\n"
        "- They acknowledge there is divine wisdom in humanity's creation beyond their grasp."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 2C: Concealed Arrogance
    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Concealed Infiltration: 'What You Were Hiding'", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Wa a'lamu ma tubduna wa ma kuntum taktumun': Angels have no secrets or deceit.\n"
        "- What was hidden? Iblis was embedded in the angelic ranks, secretly harboring jealousy, entitlement, and latent hubris against Adam (Al-Alusi, Ruh al-Ma'ani)."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 2D: Aba Wastakbara
    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Defiance & The Trap of Religious Hubris (Aba Wastakbara)", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Aba': Defied rightful divine authority; 'Istakbara': Actively sought greatness.\n"
        "- Religious Hubris: Arrogance is not just for secular kings; it strikes devout worshippers who feel entitled to rank. Iblis's latent disbelief was exposed (Wa kana minal-kafireen)."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 2: DOMESTIC SANCTUARY, THE SLIP & CHARTER OF PEACE
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 4,
        "DOMESTIC SANCTUARY, THE SLIP & THE CHARTER OF PEACE",
        "Pillars 3 & 4: Domestic stewardship, the tree perimeter, grace of taught words, and the guarantee against fear",
        "PART 2 : SECTION 2",
        "26:39 - 67:15"
    )

    # Column 1: Pillar 3 (Domestic Sanctuary & Utilitarian World)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 3: DOMESTIC SANCTUARY & THE SLIP", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Stewardship, Tree Perimeter, Equal Slip & Worldly Mata'", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c1_x + c1_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=0.6)
    pdf.text("26:39 - 39:18", c1_x + c1_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=CYAN)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    # Card 3A: Domestic Stewardship
    y_c = c1_y + c1_h - 48
    pdf.text("1. Domestic Leadership: 'Uskun Anta wa Zawjuk'", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Addressed directly to Adam: establishes domestic stewardship and spiritual protection.\n"
        "- The Tree Boundary: 'Wa la taqraba' (Do not even come near)—setting moral perimeters.\n"
        "- Boundless abundance: Feasting freely anywhere except one designated test boundary."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 3B: Symmetrical Slip
    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. The Equal Slip: Refuting the Eve Fallacy", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Fa-azallahumash-shaytan' (Satan caused BOTH of them to slip).\n"
        "- Islam completely rejects the misogynistic biblical dogma blaming Eve for humanity's fall.\n"
        "- Plural descent 'Ihbitu': Animosity between mankind and Satan, and gender frictions."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 3C: Earth as Temporary Toolkit
    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Earth as Temporary Toolkit: The Etymology of Mata'", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Al-Asma'i Bedouin Discovery: A desert girl whose cleaning scrub-brush was taken cried 'Akhadha mata'i!'\n"
        "- Mata' is a tool you utilize (sponge, shovel) but never emotionally fall in love with.\n"
        "- Dunya is a utilitarian toolkit to build Jannah; keep it in your hand, never in your heart."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 3D: Catholic vs. Protestant Dual Extremes
    y_c -= 60
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Avoiding Dual Extremes: Asceticism vs. Prosperity Gospel", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Monasticism equates worldliness with curse; Prosperity Gospel equates wealth with God's love.\n"
        "- Islamic Balance: Wealth is merely a test; beloved prophets had nothing, evil tyrants had everything.\n"
        "- Business success is never proof of divine favor."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Center Gap Connector Bridge
    pdf.line(c1_x + c1_w, bridge_y, c2_x, bridge_y, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(w/2 - 12, bridge_y - 8, 24, 16, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=0.8)
    pdf.text_centered("->", w/2, bridge_y + 3, font="F2", size=7, rgb=GOLD_LIGHT)

    # Column 2: Pillar 4 (Divine Repentance & Freedom from Fear)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 4: DIVINE TAWBAH & FREEDOM FROM FEAR", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Taught Words of Mercy, Future Fear vs Past Grief", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c2_x + c2_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=0.6)
    pdf.text("39:19 - 67:15", c2_x + c2_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    # Card 4A: Grace of Taught Words
    y_c = c1_y + c1_h - 48
    pdf.text("1. Grace of Taught Words: 'Fa-talaqqa Adamu Kalimat'", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Allah Himself revealed the words of reconciliation: 'Rabbana zalamna anfusana...'\n"
        "- Tawbah converts a debt of sins into a credit of good deeds (Yubaddilullahu sayyi'atihina hasanat).\n"
        "- If Adam could be instantly forgiven, no sinner may ever despair of Allah's mercy."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 4B: Emphatic Guidance Verification
    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Emphatic Guidance: 'Fa-imma Ya'tiyannakum'", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Emphatic Nun guarantees that authentic revelation will definitely descend.\n"
        "- Obligation to verify: Islam rejects blind cultural inheritance; believers follow with eyes wide open (Ad'u ilallahi 'ala baseerah)."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 4C: Fear vs Grief
    y_c -= 54
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Linguistic Anatomy: Fear (Future) vs. Grief (Past)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Khawf: Pertains to future dread (sickness, financial insecurity, death).\n"
        "- Huzn: Pertains to past trauma and regret. Khawf is framed as noun (constant state), Huzn as verb (temporary wave).\n"
        "- 'La khawfun 'alayhim': There is no objective destruction threatening them."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 4D: Sickness as Purifier
    y_c -= 62
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. The Believer's Win-Win: Sickness as Spiritual Cleanser", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Prophetic comfort: 'La ba's, tahoorun insha'Allah' (No harm, a purifier).\n"
        "- Afflictions wipe out sins; in the Akhirah believers will thank Allah for worldly sickness.\n"
        "- Two great tests: Calamity (patience) and Luxury (gratitude/preventing complacency)."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 3: THE COVENANT WITH BANU ISRA'IL & ETHICS OF SCRIPTURE
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 4,
        "THE COVENANT WITH BANU ISRA'IL & SCRIPTURAL ETHICS",
        "Pillars 5 & 6: Awakening favors, primacy of Risalah, selling out for petty gain, and cloaking truth",
        "PART 2 : SECTION 3",
        "67:16 - 89:33"
    )

    # Column 1: Pillar 5 (Awakening Favors & Primacy of Risalah)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 5: AWAKENING FAVOR & RISALAH", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Collective Memory, Symmetrical Covenant & Forefront Denial", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c1_x + c1_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=0.6)
    pdf.text("67:16 - 78:40", c1_x + c1_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    # Card 5A: Awakening Favors
    y_c = c1_y + c1_h - 48
    pdf.text("1. Awakening Collective Favor: 'Udkuru Ni'mati'", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Connects to Surah Al-Fatihah: 'Siratal-ladhina an'amta 'alayhim'.\n"
        "- Banu Isra'il was once favored with prophethood and divine book; they are reminded of this grace to soften their hearts rather than leading with harsh condemnation."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 5B: Symmetrical Covenant
    y_c -= 56
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. The Symmetrical Covenant: 'Awfu Bi-'Ahdi Ufi'", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Fulfill My covenant, I will fulfill yours': If you uphold the Torah, you will eat from above and below in Dunya, and gain Paradise in Akhirah.\n"
        "- Fear of Allah alone: 'Wa iyyaya farhabun'—breaking sectarian fears."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 5C: Primacy of Faith in the Messenger
    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Primacy of Faith in the Final Messenger (Risalah)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Wa aminu bima anzaltu musaddiqal-lima ma'akum': Demands faith in the Prophet Muhammad.\n"
        "- Refutes modern pluralist distortions: Banu Isra'il already believed in God and the Last Day; what damned them was rejecting the Final Messenger out of racial arrogance."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 5D: Front-Row Leaders in Denial
    y_c -= 60
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Forefront Leaders in Denial: 'Awwala Kafirin Bih'", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Not chronologically first (Quraish rejected first), but first in priority and leadership.\n"
        "- Expected to be the first to believe due to scriptural literacy, they instead led the opposition."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Center Gap Connector Bridge
    pdf.line(c1_x + c1_w, bridge_y, c2_x, bridge_y, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(w/2 - 12, bridge_y - 8, 24, 16, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=0.8)
    pdf.text_centered("->", w/2, bridge_y + 3, font="F2", size=7, rgb=GOLD_LIGHT)

    # Column 2: Pillar 6 (Selling Out & Cloaking Truth)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 6: THE ECONOMICS OF BETRAYAL", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Selling Out, Cloaking Truth with Falsehood & Watered Down Religion", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c2_x + c2_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=0.6)
    pdf.text("78:41 - 89:33", c2_x + c2_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    # Card 6A: Selling Out for Petty Gain
    y_c = c1_y + c1_h - 48
    pdf.text("1. Selling Out for Petty Status: 'Thamanan Qaleela'", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Wa la tashtaru bi-ayati thamanan qaleela': Sacrificing divine truth for salaries and prestige.\n"
        "- Feared losing communal monopoly if they acknowledged a non-Jewish Prophet."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 6B: Cloaking Truth
    y_c -= 52
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Cloaking Truth with Falsehood: 'Talbis al-Haqq'", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Mixing 90% truth with 10% distortion so falsehood appears respectable.\n"
        "- 'Wa taktumul-haqq': Concurrently hiding clear scriptural prophecies confirming the Prophet."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 6C: Two Modern Extremes
    y_c -= 54
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Two Modern Distortions: Liberal Water-Down vs. Rage", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 1. Liberal Extreme (driven by Khawf): Diluting scripture to appease critics and secular approval.\n"
        "- 2. Extremist Reaction (driven by Huzn/Anger): Weaponizing isolated texts out of political rage.\n"
        "- Pure Islamic scholarship operates with level-headed Taqwa, immune to fear and rage."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 6D: Integrity of Fitrah
    y_c -= 64
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Divine Confidence: The Qur'an Speaks to Human Fitrah", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- When presented authentically without apologetic compromise, the Qur'an resonates with human decency.\n"
        "- We must never alter revelation out of fear of public reaction."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 4: INSTITUTIONAL REFORMATION & PHARAOH'S TYRANNY
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 4,
        "INSTITUTIONAL REFORM, THE SOUL'S TETHER & PHARAOH'S TYRANNY",
        "Pillars 7 & 8: Joining the bowing, self-forgetful preachers, 'Aql as restraint, and the deliverance from infanticide",
        "PART 2 : SECTION 4",
        "89:34 - 119:44"
    )

    # Column 1: Pillar 7 (Institutional Reform & The Tethered Mind)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 7: INSTITUTIONAL REFORM & 'AQL", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Salah, Zakat, Joining the Bowing & Self-Forgetful Scholars", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c1_x + c1_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=0.6)
    pdf.text("89:34 - 103:15", c1_x + c1_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=GOLD)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    # Card 7A: Joining the Bowing
    y_c = c1_y + c1_h - 48
    pdf.text("1. Joining the Islamic Congregation: 'Warka'u Ma'ar-Raki'een'", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Ancient Jewish liturgy practiced Sujud before Ruku'.\n"
        "- 'Bow with those who bow': Leave sectarian isolation and join the congregation of Muhammad.\n"
        "- Salah and Zakat cure spiritual stagnation: Dhikr tethers the heart, Zakat cleanses greed."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 7B: Self-Forgetful Preachers
    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Indictment of Religious Preachers: 'Tansawna Anfusakum'", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Do you command people to virtue and forget your own souls while reciting Scripture?'\n"
        "- Religious Hypocrisy: Preaching ethics publicly while cheating, abusing families, or hoarding privately. Those who teach the book face the gravest accountability."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 7C: Etymology of 'Aql
    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Etymology of 'Aql: The Camel's Hobble ('Iqal)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Aql in Arabic literally means to tie down (the rope used to hobble a camel).\n"
        "- Intellect is NOT theoretical IQ; it is emotional self-restraint and moral impulse control.\n"
        "- An intellectual without self-restraint is functionally irrational (Ghayr 'Aqil)."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 7D: Anchor of Sabr & Salah
    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Seeking Strength: 'Wasta'inu Bis-Sabri Was-Salah'", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Isti'anah: Calling for assistance when working at the limit of human capacity.\n"
        "- Enormously heavy except upon the Khashi'een (those viscerally convinced they will meet Allah)."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Center Gap Connector Bridge
    pdf.line(c1_x + c1_w, bridge_y, c2_x, bridge_y, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(w/2 - 12, bridge_y - 8, 24, 16, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=0.8)
    pdf.text_centered("->", w/2, bridge_y + 3, font="F2", size=7, rgb=GOLD_LIGHT)

    # Column 2: Pillar 8 (Day of No Ransom & Deliverance from Tyranny)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 8: DAY OF NO BAIL & PHARAOH'S CRIME", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Judgment Day, Infanticide, Parted Sea & Golden Calf Relapse", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.rect(c2_x + c2_w - 95, c1_y + c1_h - 26, 85, 16, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=0.6)
    pdf.text("103:16 - 119:44", c2_x + c2_w - 82, c1_y + c1_h - 16, font="F2", size=7, rgb=CYAN)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    # Card 8A: Day of No Ransom
    y_c = c1_y + c1_h - 48
    pdf.text("1. The Day of Zero Bail: 'La Tajzi Nafsun 'An Nafsin'", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- No proxy benefit, no unapproved intercession (Shafa'ah), no ransom or bail ('Adl).\n"
        "- Lineage, clerical pedigree, and ethnic status evaporate; each soul stands isolated."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 8B: Pharaoh's Brutal Tyranny
    y_c -= 52
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Pharaoh's Tyranny: Infanticide & Abuse of Women", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Yudhabbi-huna abna'akum wa yastah-yuna nisa'akum': Slaughtering newborn sons.\n"
        "- Violating women as a weapon of systemic humiliation. A supreme trial from their Lord (Bala'um-mir-rabbikum 'azeem)."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 8C: Miraculous Deliverance
    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. The Parted Sea: 'Wa Idh Faraqna Bikumul-Bahr'", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Trapped between water and Pharaoh's army, the sea parted miraculously.\n"
        "- Anjaynakum (completed rescue); watching Pharaoh's elite drown while staring in shock (Antum tanzurun)."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Card 8D: The Golden Calf Relapse
    y_c -= 56
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Relapse into Materialism: The Golden Calf ('Ijl)", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Musa called for 40 nights to receive the tablets.\n"
        "- In his brief absence, after seeing the sea part, they fashioned and worshipped a golden calf!\n"
        "- Lessons for all nations: Materialism and idolatry easily creep back without constant spiritual vigilance."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Save Output
    pdf.save(OUTPUT_PDF)
    print(f"[OK] Master Landscape Mindmap PDF compiled successfully: {OUTPUT_PDF} (4 Pages)")

if __name__ == "__main__":
    build_part02_pdf()
