#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Baqarah 10-Page Master Landscape Mindmap PDF Compiler
Generates an 8-to-10 page high-definition landscape vector PDF (792 x 446 pts, 16:9 ratio)
embodying Ustadh Nouman Ali Khan's structural and linguistic analysis:
- Page 1: Global Macro Ring Composition (Ayat 1-286)
- Page 2: Act I: Genesis, The 3 Hearts & Prototype (Ayat 1-39)
- Page 3: Act II: Banu Isra'il: Covenant Failure & The Cow (Ayat 40-123)
- Page 4: Act III: Ibrahimic Standard & Qiblah Shift (Ayat 124-177)
- Page 5: Act IV: Legal Matrix & Community Architecture (Ayat 178-242)
- Page 6: SPECIAL DEDICATION 1: Ayat al-Kursi (2:255) 9-Sentence Internal Ring
- Page 7: SPECIAL DEDICATION 2: Triad of Sovereignty & 3 Proofs (Ayat 256-260)
- Page 8: Act V: Financial Jihad, Infaq vs. Riba, Contracts (Ayat 261-284)
- Page 9: SPECIAL DEDICATION 3: Ayah 285 - Universal Creed & Submission (Sami'na wa Ata'na)
- Page 10: SPECIAL DEDICATION 4: Ayah 286 - The 7 Master Climax Petitions (Wus'aha)
"""

import os
import sys

# Import our verified PDF engine
sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
ASSETS_DIR = "/mnt/AI/ag/Campaign/Portfolio/assets"

# Colors
NAVY_DEEP = (0.027, 0.047, 0.082) # #070C15
NAVY_CARD = (0.055, 0.086, 0.141) # #0E1624
NAVY_LIGHT = (0.090, 0.137, 0.220)
GOLD = (0.831, 0.686, 0.353)      # #D4AF59
GOLD_LIGHT = (0.910, 0.820, 0.580)
WHITE = (0.98, 0.98, 0.98)
TEXT_MUTED = (0.72, 0.76, 0.82)
TEXT_DARK = (0.12, 0.14, 0.18)
BORDER_GOLD = (0.70, 0.56, 0.28)
BORDER_MUTED = (0.18, 0.24, 0.32)
EMERALD = (0.15, 0.65, 0.45)
CYAN = (0.20, 0.65, 0.85)

def build_baqarah_landscape_mindmap():
    w, h = 792, 446 # 16:9 widescreen landscape
    pdf = PDFDocument(page_width=w, page_height=h)

    # Register assets
    pdf.register_jpeg("night_galaxy", os.path.join(ASSETS_DIR, "night_galaxy.jpg"))
    pdf.register_jpeg("masjid_nabawi", os.path.join(ASSETS_DIR, "masjid_nabawi.jpg"))
    pdf.register_jpeg("hero_oasis", os.path.join(ASSETS_DIR, "hero_oasis.jpg"))
    pdf.register_jpeg("stream_source", os.path.join(ASSETS_DIR, "stream_source.jpg"))
    pdf.register_jpeg("two_seas", os.path.join(ASSETS_DIR, "two_seas.jpg"))

    def draw_mindmap_chrome(pnum, title, ayah_range, badge_text="THEMATIC & RING COMPOSITION CARTOGRAPHY"):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)
        # Header banner
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 35, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT: SURAH AL-BAQARAH  -  " + badge_text, 125, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        pdf.text(f"PAGE {pnum:02d} / 10", w - 85, h - 26, font="F2", size=9, rgb=GOLD)
        
        # Sub-title bar
        pdf.text(title, 35, h - 68, font="F2", size=13, rgb=WHITE)
        pdf.text(f"[{ayah_range}]", w - 120, h - 68, font="F2", size=11, rgb=GOLD)
        pdf.line(35, h - 75, w - 35, h - 75, stroke_rgb=BORDER_MUTED, line_width=0.8)

        # Footer
        pdf.line(35, 26, w - 35, 26, stroke_rgb=BORDER_MUTED, line_width=0.8)
        pdf.text("HUURS KNOWLEDGE SYSTEMS  *  NAZM RING COMPOSITION ARCHITECTURE  *  READ. REFLECT. RETURN.", 35, 14, font="F1", size=7.5, rgb=TEXT_MUTED)
        pdf.text("SOURCE: USTADH NOUMAN ALI KHAN IN-DEPTH LECTURES", w - 265, 14, font="F2", size=7.5, rgb=GOLD)

    # -------------------------------------------------------------
    # PAGE 1: GLOBAL MACRO RING COMPOSITION (AYAT 1-286)
    # -------------------------------------------------------------
    pdf.new_page(w, h)
    draw_mindmap_chrome(1, "GLOBAL MACRO RING COMPOSITION: THE 9-PART SYMMETRY", "AYAT 1 - 286")

    # Center Pivot Highlight Box (Ayah 143)
    piv_x, piv_y, piv_w, piv_h = w/2 - 130, h - 145, 260, 58
    pdf.rect(piv_x, piv_y, piv_w, piv_h, fill_rgb=NAVY_LIGHT, stroke_rgb=GOLD, line_width=1.5)
    pdf.text_centered("[E] THE CENTER PIVOT: THE MIDDLE NATION", w/2, piv_y + 40, font="F2", size=9.5, rgb=GOLD)
    pdf.text_centered("Ayat 142 - 152: Shift of Qiblah (Jerusalem -> Makkah)", w/2, piv_y + 26, font="F1", size=8, rgb=WHITE)
    pdf.text_centered('"Wa kadhalika ja\'alnakum Ummatan Wasatan" (2:143)', w/2, piv_y + 12, font="F3", size=7.5, rgb=GOLD_LIGHT)

    # 4 Outer Symmetrical Columns (Left: Opening Halves A-D | Right: Mirrored Halves D'-A')
    # Row 1: A vs A'
    pdf.rect(35, h - 145, 220, 58, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1)
    pdf.text("[A] FAITH & GUIDANCE (1-20)", 45, h - 105, font="F2", size=8.5, rgb=CYAN)
    pdf.text("3 Hearts: Muttaqin, Kafirun, Munafiqun", 45, h - 120, font="F1", size=7.5, rgb=WHITE)
    pdf.text("Two Parables: The Desert Fire & Rainstorm", 45, h - 134, font="F1", size=7, rgb=TEXT_MUTED)

    pdf.rect(w - 255, h - 145, 220, 58, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1)
    pdf.text("[A'] CLIMAX: FAITH & DUA (284-286)", w - 245, h - 105, font="F2", size=8.5, rgb=CYAN)
    pdf.text("The Apostles' Creed (Amana ar-Rasul)", w - 245, h - 120, font="F1", size=7.5, rgb=WHITE)
    pdf.text("Submission (Sami'na) & 7 Master Petitions", w - 245, h - 134, font="F1", size=7, rgb=TEXT_MUTED)

    # Connector line A <-> A'
    pdf.line(255, h - 116, piv_x, h - 116, stroke_rgb=BORDER_MUTED, line_width=0.8)
    pdf.line(piv_x + piv_w, h - 116, w - 255, h - 116, stroke_rgb=BORDER_MUTED, line_width=0.8)

    # Row 2: B vs B'
    pdf.rect(35, h - 220, 220, 60, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1)
    pdf.text("[B] CREATION & COVENANT (21-39)", 45, h - 180, font="F2", size=8.5, rgb=EMERALD)
    pdf.text("Universal Call to Worship; Inimitability", 45, h - 194, font="F1", size=7.5, rgb=WHITE)
    pdf.text("Adam's Caliphate, Iblis's Pride, Tawbah", 45, h - 208, font="F1", size=7, rgb=TEXT_MUTED)

    pdf.rect(w - 255, h - 220, 220, 60, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1)
    pdf.text("[B'] SACRIFICE & SOVEREIGNTY (243-283)", w - 245, h - 180, font="F2", size=8.5, rgb=EMERALD)
    pdf.text("Talut/Dawud; Ayatul Kursi (255)", w - 245, h - 194, font="F1", size=7.5, rgb=WHITE)
    pdf.text("Infaq Multiplier, War on Riba, Debt Law (282)", w - 245, h - 208, font="F1", size=7, rgb=TEXT_MUTED)

    # Row 3: C vs C'
    pdf.rect(35, h - 295, 220, 60, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1)
    pdf.text("[C] BANU ISRA'IL DECAY (40-123)", 45, h - 255, font="F2", size=8.5, rgb=GOLD)
    pdf.text("Covenants, Pharaoh, Golden Calf, The Cow", 45, h - 269, font="F1", size=7.5, rgb=WHITE)
    pdf.text("Tahrif, Harut/Marut, Hardened Hearts", 45, h - 283, font="F1", size=7, rgb=TEXT_MUTED)

    pdf.rect(w - 255, h - 295, 220, 60, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1)
    pdf.text("[C'] NEW UMMAH'S LEGAL MATRIX (178-242)", w - 245, h - 255, font="F2", size=8.5, rgb=GOLD)
    pdf.text("Qisas, Ramadan Fasting, Du'a (186), Hajj", w - 245, h - 269, font="F1", size=7.5, rgb=WHITE)
    pdf.text("Combat Ethics, Family & Divorce Protection", w - 245, h - 283, font="F1", size=7, rgb=TEXT_MUTED)

    # Row 4: D vs D'
    pdf.rect(35, h - 370, 220, 60, fill_rgb=NAVY_CARD, stroke_rgb=(0.85, 0.50, 0.30), line_width=1)
    pdf.text("[D] IBRAHIM'S LEGACY (124-141)", 45, h - 330, font="F2", size=8.5, rgb=(0.85, 0.50, 0.30))
    pdf.text("Ibrahim passes trials; Ka'bah built with Ismail", 45, h - 344, font="F1", size=7.5, rgb=WHITE)
    pdf.text("Du'a for the Ummah & Unlettered Messenger", 45, h - 358, font="F1", size=7, rgb=TEXT_MUTED)

    pdf.rect(w - 255, h - 370, 220, 60, fill_rgb=NAVY_CARD, stroke_rgb=(0.85, 0.50, 0.30), line_width=1)
    pdf.text("[D'] NEW UMMAH'S TRIALS (153-177)", w - 245, h - 330, font="F2", size=8.5, rgb=(0.85, 0.50, 0.30))
    pdf.text("Sabr & Salah, Martyrs Alive, Fear/Loss Tests", w - 245, h - 344, font="F1", size=7.5, rgb=WHITE)
    pdf.text("Safa & Marwa, Halal/Tayyib, True Birr (177)", w - 245, h - 358, font="F1", size=7, rgb=TEXT_MUTED)

    # Center Flow Box (Summary of Symmetry)
    pdf.rect(piv_x, 40, piv_w, 150, fill_rgb=NAVY_CARD, stroke_rgb=BORDER_MUTED, line_width=1)
    pdf.text_centered("CORE THEMATIC ARCHITECTURE", w/2, 175, font="F2", size=8.5, rgb=GOLD)
    summary_txt = (
        "Surah Al-Baqarah transitions leadership of the world from Banu Isra'il to the Ummah of Muhammad (peace be upon him).\n"
        "1. Establishes the standard of faith (A, A').\n"
        "2. Contrasts the failure of Banu Isra'il (C) with the new legal safeguard of the Muslims (C').\n"
        "3. Anchors leadership in Ibrahim (D) and tests the new followers (D').\n"
        "4. Pivots at Verse 143: The Middle Nation."
    )
    pdf.paragraph(summary_txt, piv_x + 10, 160, piv_w - 20, line_height=12, font="F1", size=7, rgb=WHITE)

    # -------------------------------------------------------------
    # PAGE 2: ACT I — GENESIS & THE THREE HEARTS (AYAT 1-39)
    # -------------------------------------------------------------
    pdf.new_page(w, h)
    draw_mindmap_chrome(2, "ACT I: THE HUMAN CONDITION, THREE HEARTS & THE PROTOTYPE", "AYAT 1 - 39")

    # 3 Horizontal Section Blocks
    # Block 1: Prologue & The Three Dispositions
    b1_x, b1_y, b1_w, b1_h = 35, 42, 230, h - 128
    pdf.rect(b1_x, b1_y, b1_w, b1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1)
    pdf.text("1. THE THREE HEARTS (1-20)", b1_x + 10, b1_y + b1_h - 18, font="F2", size=9.5, rgb=GOLD)
    pdf.line(b1_x + 10, b1_y + b1_h - 24, b1_x + b1_w - 10, b1_y + b1_h - 24, stroke_rgb=BORDER_MUTED, line_width=0.8)

    t1 = (
        "- Alif-Lam-Meem (1): Letters prove divine teacher; student orientation: humility ('You know nothing').\n\n"
        "- Dhalikal-Kitab (2): Etched in stone, unchangeable order. La Rayba Feeh: zero agitating doubt. Hudan lil-Muttaqin: active living guidance (Hal).\n\n"
        "- Muttaqin (3-5): Belief in Ghayb, Salah, Infaq, past books, Akhirah certainty.\n\n"
        "- Kafirun (6-7): Sealed hearts, hearing, and vision.\n\n"
        "- Munafiqun (8-16): Heart disease, claim reform while corrupting, mock believers as fools."
    )
    pdf.paragraph(t1, b1_x + 10, b1_y + b1_h - 40, b1_w - 20, line_height=11.5, font="F1", size=7.2, rgb=WHITE)

    # Block 2: The Two Parables of Hypocrisy
    b2_x = b1_x + b1_w + 16
    pdf.rect(b2_x, b1_y, b1_w, b1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1)
    pdf.text("2. TWO PARABLES (17-20)", b2_x + 10, b1_y + b1_h - 18, font="F2", size=9.5, rgb=CYAN)
    pdf.line(b2_x + 10, b1_y + b1_h - 24, b2_x + b1_w - 10, b1_y + b1_h - 24, stroke_rgb=BORDER_MUTED, line_width=0.8)

    t2 = (
        "- Parable 1: The Kindled Fire (17-18)\n"
        "  A man sparks fire in pitch darkness. When light surrounds him, Allah takes their light, leaving them in deep darkness: deaf, dumb, blind.\n"
        "  -> Represents intellectual hypocrisy (loss of light).\n\n"
        "- Parable 2: The Thunderous Storm (19-20)\n"
        "  Dark cloud with thunder and lightning. They thrust fingers in ears from fear of death. Lightning briefly guides step; darkness freezes them.\n"
        "  -> Represents psychological cowardice in hardship.\n\n"
        "- Universal Call (21-29):\n"
        "  Worship your Lord; challenge to produce 1 Surah; metaphor of the gnat; cosmic design."
    )
    pdf.paragraph(t2, b2_x + 10, b1_y + b1_h - 40, b1_w - 20, line_height=11.5, font="F1", size=7.2, rgb=WHITE)

    # Block 3: The Prototype of Responsibility (Adam & Iblis)
    b3_x = b2_x + b1_w + 16
    pdf.rect(b3_x, b1_y, b1_w, b1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1)
    pdf.text("3. PROTOTYPE: ADAM & IBLIS (30-39)", b3_x + 10, b1_y + b1_h - 18, font="F2", size=9.5, rgb=EMERALD)
    pdf.line(b3_x + 10, b1_y + b1_h - 24, b3_x + b1_w - 10, b1_y + b1_h - 24, stroke_rgb=BORDER_MUTED, line_width=0.8)

    t3 = (
        "- Khalifah Announcement (30):\n"
        "  Angels ask: 'Will You place one who sheds blood?' Allah: 'I know what you know not.'\n\n"
        "- Teaching of Names (31-33):\n"
        "  Adam demonstrates conceptual language (Asma'); angels submit in humility.\n\n"
        "- The Refusal of Iblis (34):\n"
        "  Pride and arrogance ('Aba wastakbara') - the root of Kufr.\n\n"
        "- The Forbidden Tree & Fall (35-36):\n"
        "  Shaytan slips them; descended to earth.\n\n"
        "- The Antidote: Words of Repentance (37-39):\n"
        "  Adam receives Kalimat; tawbah accepted. Promise: 'Whoever follows My guidance shall have no fear nor grieve.'"
    )
    pdf.paragraph(t3, b3_x + 10, b1_y + b1_h - 40, b1_w - 20, line_height=11.5, font="F1", size=7.2, rgb=WHITE)

    # -------------------------------------------------------------
    # PAGE 3: ACT II — BANU ISRA'IL & THE COW (AYAT 40-123)
    # -------------------------------------------------------------
    pdf.new_page(w, h)
    draw_mindmap_chrome(3, "ACT II: BANU ISRA'IL: THE CASE STUDY OF COVENANT DECAY", "AYAT 40 - 123")

    # 3 Columns
    col_w = (w - 70 - 32) / 3
    # Col 1: Favors & Deliverance
    c1_x = 35
    pdf.rect(c1_x, 42, col_w, h - 128, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1)
    pdf.text("1. FAVORS & BETRAYALS (40-66)", c1_x + 10, h - 95, font="F2", size=9.5, rgb=GOLD)
    pdf.line(c1_x + 10, h - 101, c1_x + col_w - 10, h - 101, stroke_rgb=BORDER_MUTED, line_width=0.8)

    p3_t1 = (
        "- The Warning (40-48):\n"
        "  Remember My favors; do not sell My verses for a cheap price; fear the Day no soul avails another.\n\n"
        "- Historical Deliverances:\n"
        "  * Rescued from Pharaoh's slaughter.\n"
        "  * Sea parted before their eyes.\n"
        "  * Golden Calf worshipped during Musa's 40 nights at Mount Sinai.\n"
        "  * Thunderclap strikes them after demanding: 'Show us Allah openly.'\n"
        "  * Manna & Quail provided; yet they complain demanding onions, garlic, lentils.\n"
        "  * Raised the Mount above them."
    )
    pdf.paragraph(p3_t1, c1_x + 10, h - 115, col_w - 20, line_height=11.5, font="F1", size=7.2, rgb=WHITE)

    # Col 2: Narrative of the Cow
    c2_x = c1_x + col_w + 16
    pdf.rect(c2_x, 42, col_w, h - 128, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1)
    pdf.text("2. THE SACRED COW (67-74)", c2_x + 10, h - 95, font="F2", size=9.5, rgb=CYAN)
    pdf.line(c2_x + 10, h - 101, c2_x + col_w - 10, h - 101, stroke_rgb=BORDER_MUTED, line_width=0.8)

    p3_t2 = (
        "- The Simple Command (67):\n"
        "  'Allah commands you to slaughter a cow.'\n"
        "  Response: 'Do you make a mockery of us?'\n\n"
        "- Procrastination & Questioning:\n"
        "  * What age? (Neither old nor virgin).\n"
        "  * What color? (Bright yellow, pleasing).\n"
        "  * What work? (Unblemished, free of labor).\n\n"
        "- The Reluctant Sacrifice (71):\n"
        "  'They slaughtered it, though they nearly did not.'\n\n"
        "- The Murder Solved (72-73):\n"
        "  Struck victim with part of cow; brought to life.\n\n"
        "- The Hardening of Hearts (74):\n"
        "  Hearts turned like stones or even harder."
    )
    pdf.paragraph(p3_t2, c2_x + 10, h - 115, col_w - 20, line_height=11.5, font="F1", size=7.2, rgb=WHITE)

    # Col 3: Spiritual Pathology & Envy
    c3_x = c2_x + col_w + 16
    pdf.rect(c3_x, 42, col_w, h - 128, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1)
    pdf.text("3. THEOLOGICAL DECAY (75-123)", c3_x + 10, h - 95, font="F2", size=9.5, rgb=EMERALD)
    pdf.line(c3_x + 10, h - 101, c3_x + col_w - 10, h - 101, stroke_rgb=BORDER_MUTED, line_width=0.8)

    p3_t3 = (
        "- Tahrif (Scripture Alteration) (75-79):\n"
        "  Woe to those who write scripture with their hands and say: 'This is from Allah' to earn wealth.\n\n"
        "- False Salvation Entitlement (80-82):\n"
        "  'Fire will not touch us but for counted days.'\n\n"
        "- Selective Faith (85):\n"
        "  Believing in part of the book and rejecting part.\n\n"
        "- Occult Distraction (102-103):\n"
        "  Trading divine book for Babylon black magic (Harut & Marut).\n\n"
        "- Theological Jealousy (109):\n"
        "  Envy that the final Messenger was chosen from the Arabs rather than Banu Isra'il."
    )
    pdf.paragraph(p3_t3, c3_x + 10, h - 115, col_w - 20, line_height=11.5, font="F1", size=7.2, rgb=WHITE)

    # -------------------------------------------------------------
    # PAGE 4: ACT III — IBRAHIM & THE PIVOT (AYAT 124-177)
    # -------------------------------------------------------------
    pdf.new_page(w, h)
    draw_mindmap_chrome(4, "ACT III: IBRAHIMIC SUCCESSION & THE QIBLAH PIVOT", "AYAT 124 - 177")

    # 3 Columns
    pdf.rect(c1_x, 42, col_w, h - 128, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1)
    pdf.text("1. IBRAHIM'S IMAMAH (124-141)", c1_x + 10, h - 95, font="F2", size=9.5, rgb=GOLD)
    pdf.line(c1_x + 10, h - 101, c1_x + col_w - 10, h - 101, stroke_rgb=BORDER_MUTED, line_width=0.8)

    p4_t1 = (
        "- The Test of Leadership (124):\n"
        "  Tested with Kalimat; passed all.\n"
        "  'I will make you a leader for mankind.'\n"
        "  'My covenant does not include oppressors.'\n\n"
        "- Raising the Ka'bah Foundations (127):\n"
        "  Ibrahim & Ismail: 'Rabbana taqabbal minna.'\n\n"
        "- The Prophetic Invocation (129):\n"
        "  Prayer for the Ummi Messenger:\n"
        "  To recite verses, teach Book & Wisdom, and purify them.\n\n"
        "- Pure Submission (131):\n"
        "  'Aslim! Qala: Aslamtu li-Rabbil-'Alamin.'"
    )
    pdf.paragraph(p4_t1, c1_x + 10, h - 115, col_w - 20, line_height=11.5, font="F1", size=7.2, rgb=WHITE)

    pdf.rect(c2_x, 42, col_w, h - 128, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1)
    pdf.text("2. THE CENTER PIVOT (142-152)", c2_x + 10, h - 95, font="F2", size=9.5, rgb=CYAN)
    pdf.line(c2_x + 10, h - 101, c2_x + col_w - 10, h - 101, stroke_rgb=BORDER_MUTED, line_width=0.8)

    p4_t2 = (
        "- Shift of Qiblah (142-144):\n"
        "  Fools ask: 'What turned them from their Qiblah?'\n"
        "  Turning face toward Masjid al-Haram.\n\n"
        "- The Middle Nation (143):\n"
        "  'Ummatan Wasatan' - Just, Balanced.\n"
        "  Witnesses over mankind; Messenger witness over you.\n\n"
        "- Testing True Followers:\n"
        "  Qiblah shift exposed hypocrites from sincere followers.\n\n"
        "- Climax of Gratitude (152):\n"
        "  'Fadhkuruni adhkurkum, washkuru li wa la takfurun.'"
    )
    pdf.paragraph(p4_t2, c2_x + 10, h - 115, col_w - 20, line_height=11.5, font="F1", size=7.2, rgb=WHITE)

    pdf.rect(c3_x, 42, col_w, h - 128, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1)
    pdf.text("3. TRIALS & TRUE BIRR (153-177)", c3_x + 10, h - 95, font="F2", size=9.5, rgb=EMERALD)
    pdf.line(c3_x + 10, h - 101, c3_x + col_w - 10, h - 101, stroke_rgb=BORDER_MUTED, line_width=0.8)

    p4_t3 = (
        "- Weapons of Endurance (153):\n"
        "  Seek help through Sabr & Salah.\n\n"
        "- Living Martyrs (154):\n"
        "  Not dead, but alive with Allah.\n\n"
        "- Inevitable Trials (155-157):\n"
        "  Tested with fear, hunger, loss of wealth/lives. Glad tidings to those who say 'Inna lillah...'\n\n"
        "- Safa & Marwa (158): Sacred symbols.\n\n"
        "- Ayat al-Birr (177):\n"
        "  Righteousness is not merely facing East or West; it is faith, spending beloved wealth, keeping promises, patience in war."
    )
    pdf.paragraph(p4_t3, c3_x + 10, h - 115, col_w - 20, line_height=11.5, font="F1", size=7.2, rgb=WHITE)

    # -------------------------------------------------------------
    # PAGE 5: ACT IV — LEGAL MATRIX & SOCIETY (AYAT 178-242)
    # -------------------------------------------------------------
    pdf.new_page(w, h)
    draw_mindmap_chrome(5, "ACT IV: COMMUNITY BLUEPRINT, LAWS & SOCIAL SANITY", "AYAT 178 - 242")

    pdf.rect(c1_x, 42, col_w, h - 128, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1)
    pdf.text("1. LIFE, FASTING & DUA (178-188)", c1_x + 10, h - 95, font="F2", size=9.5, rgb=GOLD)
    pdf.line(c1_x + 10, h - 101, c1_x + col_w - 10, h - 101, stroke_rgb=BORDER_MUTED, line_width=0.8)

    p5_t1 = (
        "- Qisas / Retribution (178-179):\n"
        "  Preserving human sanctity ('In retribution is saving of life, O people of understanding').\n\n"
        "- Wills & Bequests (180-182): Just distribution.\n\n"
        "- Ramadan Fasting (183-185):\n"
        "  Fasting prescribed for Taqwa; the month Qur'an was revealed; ease intended, not hardship.\n\n"
        "- The Climax of Du'a (186):\n"
        "  'When My servants ask about Me, I am near. I answer the caller when he calls.'\n\n"
        "- Anti-Bribery (188): No embezzlement."
    )
    pdf.paragraph(p5_t1, c1_x + 10, h - 115, col_w - 20, line_height=11.5, font="F1", size=7.2, rgb=WHITE)

    pdf.rect(c2_x, 42, col_w, h - 128, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1)
    pdf.text("2. COMBAT & HAJJ (189-214)", c2_x + 10, h - 95, font="F2", size=9.5, rgb=CYAN)
    pdf.line(c2_x + 10, h - 101, c2_x + col_w - 10, h - 101, stroke_rgb=BORDER_MUTED, line_width=0.8)

    p5_t2 = (
        "- Combat Ethics (190-195):\n"
        "  Fight those who fight you; do not transgress. Fitnah is worse than killing. Spend in Allah's way; do not throw yourself into destruction.\n\n"
        "- Hajj Pilgrimage (196-203):\n"
        "  Complete Hajj & Umrah for Allah. No obscenity or quarreling. Master Du'a (201): 'Rabbana atina fid-dunya hasanah...'\n\n"
        "- Hypocrite vs. Sincere Believer (204-207):\n"
        "  Smooth talker who destroys crops vs. soul sold completely for Allah's pleasure."
    )
    pdf.paragraph(p5_t2, c2_x + 10, h - 115, col_w - 20, line_height=11.5, font="F1", size=7.2, rgb=WHITE)

    pdf.rect(c3_x, 42, col_w, h - 128, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1)
    pdf.text("3. FAMILY LAW MATRIX (215-242)", c3_x + 10, h - 95, font="F2", size=9.5, rgb=EMERALD)
    pdf.line(c3_x + 10, h - 101, c3_x + col_w - 10, h - 101, stroke_rgb=BORDER_MUTED, line_width=0.8)

    p5_t3 = (
        "- Social Welfare (215-220):\n"
        "  Orphans, alcohol & gambling prohibition.\n\n"
        "- Marriage & Oaths (221-225):\n"
        "  Faithful believer better than polytheist.\n\n"
        "- Ethics of Divorce (226-237):\n"
        "  * Retain in honor or release with grace ('Imsakun bi-ma'rufin aw tasrihun bi-ihsan').\n"
        "  * Do not take back bridal gifts (Mahr).\n"
        "  * Nursing rights for 2 full years (233).\n"
        "  * Widows' protection (234).\n\n"
        "- Guarding Prayers in Danger (238-239):\n"
        "  Guard the middle prayer (Salat al-Wusta)."
    )
    pdf.paragraph(p5_t3, c3_x + 10, h - 115, col_w - 20, line_height=11.5, font="F1", size=7.2, rgb=WHITE)

    # -------------------------------------------------------------
    # PAGE 6: SPECIAL DEDICATION 1 — AYAT AL-KURSI (2:255)
    # -------------------------------------------------------------
    pdf.new_page(w, h)
    draw_mindmap_chrome(6, "SPECIAL DEDICATION 1: AYAT AL-KURSI (2:255) - 9-SENTENCE INTERNAL RING", "AYAH 2:255", "THE GREATEST AYAH IN THE QUR'AN")

    # Center Axis Box (Clause 5)
    c5_w, c5_h = 420, 52
    c5_x, c5_y = w/2 - c5_w/2, h/2 - c5_h/2 - 5
    pdf.rect(c5_x, c5_y, c5_w, c5_h, fill_rgb=NAVY_LIGHT, stroke_rgb=GOLD, line_width=1.5)
    pdf.text_centered("CLAUSE 5: THE CENTER FULCRUM - ABSOLUTE ALL-KNOWLEDGE", w/2, c5_y + 36, font="F2", size=9, rgb=GOLD)
    pdf.text_centered('"Ya\'lamu ma bayna aydeehim wa ma khalfahum"', w/2, c5_y + 22, font="F5", size=10, rgb=WHITE)
    pdf.text_centered("(He knows what is before them and what will be after them)", w/2, c5_y + 10, font="F1", size=7.5, rgb=GOLD_LIGHT)

    # 4 Symmetrical Pairs
    box_w = 340
    box_h = 42
    left_x = 40
    right_x = w - 40 - box_w

    # Pair 1: Clause 1 <-> Clause 9 (Top)
    y1 = h - 130
    pdf.rect(left_x, y1, box_w, box_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1)
    pdf.text("1. DIVINE SELF-EXISTENCE", left_x + 10, y1 + 28, font="F2", size=8, rgb=GOLD)
    pdf.text('"Allahu la ilaha illa Huwa, Al-Hayyul Qayyum"', left_x + 10, y1 + 15, font="F5", size=8.5, rgb=WHITE)
    pdf.text("Ever-Living, Self-Sustaining upon whom all relies", left_x + 10, y1 + 4, font="F1", size=7, rgb=TEXT_MUTED)

    pdf.rect(right_x, y1, box_w, box_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1)
    pdf.text("9. SUPREME TRANSCENDENT MAJESTY", right_x + 10, y1 + 28, font="F2", size=8, rgb=GOLD)
    pdf.text('"Wa Huwal \'Aliyyul \'Adheem"', right_x + 10, y1 + 15, font="F5", size=8.5, rgb=WHITE)
    pdf.text("The Most High, The Infinite in Absolute Greatness", right_x + 10, y1 + 4, font="F1", size=7, rgb=TEXT_MUTED)
    pdf.line(left_x + box_w, y1 + 21, right_x, y1 + 21, stroke_rgb=BORDER_MUTED, line_width=0.8)

    # Pair 2: Clause 2 <-> Clause 8
    y2 = y1 - 50
    pdf.rect(left_x, y2, box_w, box_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1)
    pdf.text("2. UNTOUCHED BY FATIGUE", left_x + 10, y2 + 28, font="F2", size=8, rgb=CYAN)
    pdf.text('"La ta\'khudhuhu sinatun wa la nawm"', left_x + 10, y2 + 15, font="F5", size=8.5, rgb=WHITE)
    pdf.text("Neither drowsiness (sinah) nor deep sleep overtakes Him", left_x + 10, y2 + 4, font="F1", size=7, rgb=TEXT_MUTED)

    pdf.rect(right_x, y2, box_w, box_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1)
    pdf.text("8. UNTOUCHED BY PRESERVATION BURDEN", right_x + 10, y2 + 28, font="F2", size=8, rgb=CYAN)
    pdf.text('"Wa la ya\'uduhu hifdhuhuma"', right_x + 10, y2 + 15, font="F5", size=8.5, rgb=WHITE)
    pdf.text("Preserving heavens and earth causes Him zero fatigue", right_x + 10, y2 + 4, font="F1", size=7, rgb=TEXT_MUTED)
    pdf.line(left_x + box_w, y2 + 21, right_x, y2 + 21, stroke_rgb=BORDER_MUTED, line_width=0.8)

    # Pair 3: Clause 3 <-> Clause 7
    y3 = c5_y - 48
    pdf.rect(left_x, y3, box_w, box_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1)
    pdf.text("3. UNIVERSAL OWNERSHIP", left_x + 10, y3 + 28, font="F2", size=8, rgb=EMERALD)
    pdf.text('"Lahu ma fis-samawati wa ma fil-ard"', left_x + 10, y3 + 15, font="F5", size=8.5, rgb=WHITE)
    pdf.text("To Him belongs everything in heavens and on earth", left_x + 10, y3 + 4, font="F1", size=7, rgb=TEXT_MUTED)

    pdf.rect(right_x, y3, box_w, box_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1)
    pdf.text("7. THE COSMIC KURSI", right_x + 10, y3 + 28, font="F2", size=8, rgb=EMERALD)
    pdf.text('"Wasi\'a kursiyyuhus-samawati wal-ard"', right_x + 10, y3 + 15, font="F5", size=8.5, rgb=WHITE)
    pdf.text("His Kursi (Seat of Authority) extends over heavens/earth", right_x + 10, y3 + 4, font="F1", size=7, rgb=TEXT_MUTED)
    pdf.line(left_x + box_w, y3 + 21, right_x, y3 + 21, stroke_rgb=BORDER_MUTED, line_width=0.8)

    # Pair 4: Clause 4 <-> Clause 6 (Bottom)
    y4 = y3 - 50
    pdf.rect(left_x, y4, box_w, box_h, fill_rgb=NAVY_CARD, stroke_rgb=(0.85, 0.50, 0.30), line_width=1)
    pdf.text("4. INTERCESSION SUBORDINATED", left_x + 10, y4 + 28, font="F2", size=8, rgb=(0.85, 0.50, 0.30))
    pdf.text('"Man dhal-ladhi yashfa\'u \'indahu illa bi-idhnih"', left_x + 10, y4 + 15, font="F5", size=8.5, rgb=WHITE)
    pdf.text("Who can intercede with Him except by His prior permission?", left_x + 10, y4 + 4, font="F1", size=7, rgb=TEXT_MUTED)

    pdf.rect(right_x, y4, box_w, box_h, fill_rgb=NAVY_CARD, stroke_rgb=(0.85, 0.50, 0.30), line_width=1)
    pdf.text("6. KNOWLEDGE SUBORDINATED", right_x + 10, y4 + 28, font="F2", size=8, rgb=(0.85, 0.50, 0.30))
    pdf.text('"Wa la yuheetoona bi-shay\'im-min \'ilmihi illa bima sha\'"', right_x + 10, y4 + 15, font="F5", size=8.5, rgb=WHITE)
    pdf.text("Humans encompass nothing of His knowledge except as He wills", right_x + 10, y4 + 4, font="F1", size=7, rgb=TEXT_MUTED)
    pdf.line(left_x + box_w, y4 + 21, right_x, y4 + 21, stroke_rgb=BORDER_MUTED, line_width=0.8)

    # -------------------------------------------------------------
    # PAGE 7: SPECIAL DEDICATION 2 — TRIAD OF SOVEREIGNTY & 3 PROOFS
    # -------------------------------------------------------------
    pdf.new_page(w, h)
    draw_mindmap_chrome(7, "SPECIAL DEDICATION 2: TRIAD OF SOVEREIGNTY & THREE PROOFS OF LIFE", "AYAT 256 - 260")

    # Left Column: The Triad of Liberation (255-257)
    t_w = 340
    pdf.rect(35, 42, t_w, h - 128, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1)
    pdf.text("PART A: TRIAD OF LIBERATION (255-257)", 45, h - 95, font="F2", size=9.5, rgb=GOLD)
    pdf.line(45, h - 101, 35 + t_w - 10, h - 101, stroke_rgb=BORDER_MUTED, line_width=0.8)

    triad_txt = (
        "1. Ayah 255 (Ayatul Kursi): Absolute Sovereignty\n"
        "   Allah is the supreme owner, master, and sustainer of the cosmos.\n\n"
        "2. Ayah 256: Intellectual Freedom ('La Ikraha fid-Deen')\n"
        "   * There is no compulsion in religion.\n"
        "   * Truth stands distinct from falsehood.\n"
        "   * Al-Urwatul Wuthqa: The unbreakable handhold of faith.\n\n"
        "3. Ayah 257: Cosmic Guardianship (The Two Allies)\n"
        "   * Allah is the Wali of believers: Brings them from multi-layered darkness into the singular Light (Min az-Zulumat ilan-Nur).\n"
        "   * The Taghut (tyrant-idols) are allies of disbelievers: Drag them from light into multiple darknesses."
    )
    pdf.paragraph(triad_txt, 45, h - 115, t_w - 20, line_height=12.5, font="F1", size=7.5, rgb=WHITE)

    # Right Column: The Three Historical Proofs of Life/Death (258-260)
    p_w = w - 70 - t_w - 20
    p_x = 35 + t_w + 20
    pdf.rect(p_x, 42, p_w, h - 128, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1)
    pdf.text("PART B: THREE PROOFS OF RESURRECTION (258-260)", p_x + 10, h - 95, font="F2", size=9.5, rgb=CYAN)
    pdf.line(p_x + 10, h - 101, p_x + p_w - 10, h - 101, stroke_rgb=BORDER_MUTED, line_width=0.8)

    proofs_txt = (
        "1. Proof 1: Ibrahim vs. King Nimrod (258)\n"
        "   Nimrod claims: 'I give life and cause death.'\n"
        "   Ibrahim's checkmate: 'Allah brings the sun from the East; bring it from the West.' The tyrant was dumbfounded.\n\n"
        "2. Proof 2: Sleeper in the Ruined City (Uzayr) (259)\n"
        "   Passed a ruined town: 'How will Allah bring this to life?'\n"
        "   Died 100 years. Revived: food fresh, donkey revived from bones before his eyes. 'Allah is competent over all.'\n\n"
        "3. Proof 3: Ibrahim & The Four Birds (260)\n"
        "   'Show me how You revive the dead.'\n"
        "   'Do you not believe?' 'Yes, but to reassure my heart.'\n"
        "   Birds called; fly to him in haste. Absolute proof of resurrection."
    )
    pdf.paragraph(proofs_txt, p_x + 10, h - 115, p_w - 20, line_height=12.5, font="F1", size=7.5, rgb=WHITE)

    # -------------------------------------------------------------
    # PAGE 8: ACT V — FINANCIAL JIHAD, INFAQ & CONTRACTS (AYAT 261-284)
    # -------------------------------------------------------------
    pdf.new_page(w, h)
    draw_mindmap_chrome(8, "ACT V: STRUGGLE, INFAQ MULTIPLIER & COMMERCIAL INTEGRITY", "AYAT 261 - 284")

    pdf.rect(c1_x, 42, col_w, h - 128, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1)
    pdf.text("1. THE INFAQ MULTIPLIER (261-274)", c1_x + 10, h - 95, font="F2", size=9.5, rgb=GOLD)
    pdf.line(c1_x + 10, h - 101, c1_x + col_w - 10, h - 101, stroke_rgb=BORDER_MUTED, line_width=0.8)

    p8_t1 = (
        "- 700-Fold Multiplier (261):\n"
        "  Like a grain sprouting 7 ears, 100 grains in each ear. Allah multiplies for whom He wills.\n\n"
        "- Pure Charity Etiquette (262-264):\n"
        "  * No reminders of generosity (Mann).\n"
        "  * No hurtful injury (Adha).\n"
        "  * A kind word is better than charity followed by injury.\n"
        "  * The barren rock metaphor.\n\n"
        "- Psychological Battle (268):\n"
        "  Shaytan promises poverty; Allah promises forgiveness and abundance."
    )
    pdf.paragraph(p8_t1, c1_x + 10, h - 115, col_w - 20, line_height=11.5, font="F1", size=7.2, rgb=WHITE)

    pdf.rect(c2_x, 42, col_w, h - 128, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1)
    pdf.text("2. WAR ON RIBA / USURY (275-281)", c2_x + 10, h - 95, font="F2", size=9.5, rgb=CYAN)
    pdf.line(c2_x + 10, h - 101, c2_x + col_w - 10, h - 101, stroke_rgb=BORDER_MUTED, line_width=0.8)

    p8_t2 = (
        "- The Madness of Usury (275):\n"
        "  They rise like one beaten by Shaytan into insanity.\n"
        "  'Trade is like usury.' False! Allah permitted trade, forbade usury.\n\n"
        "- Eradication of Usury (276):\n"
        "  Allah destroys usury and increases charity.\n\n"
        "- Declaration of War (278-279):\n"
        "  Notice of war from Allah and His Messenger if usury is not abandoned.\n\n"
        "- Final Verse Revealed (281):\n"
        "  'Fear a Day you will be returned to Allah; every soul will be compensated.'"
    )
    pdf.paragraph(p8_t2, c2_x + 10, h - 115, col_w - 20, line_height=11.5, font="F1", size=7.2, rgb=WHITE)

    pdf.rect(c3_x, 42, col_w, h - 128, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1)
    pdf.text("3. DEBT CONTRACTS (282-284)", c3_x + 10, h - 95, font="F2", size=9.5, rgb=EMERALD)
    pdf.line(c3_x + 10, h - 101, c3_x + col_w - 10, h - 101, stroke_rgb=BORDER_MUTED, line_width=0.8)

    p8_t3 = (
        "- Ayat ad-Dayn (282 - Longest Verse):\n"
        "  * Write down debt contracts with specified terms.\n"
        "  * Scribe must write in justice as Allah taught.\n"
        "  * Debtor dictates terms.\n"
        "  * Two male witnesses, or 1 man and 2 women.\n"
        "  * Protects society from suspicion and fraud.\n\n"
        "- Collateral on Journey (283):\n"
        "  Pledges in hand; fulfill trusts; do not conceal testimony.\n\n"
        "- Final Audit (284):\n"
        "  To Allah belongs all in heavens and earth; He will hold you accountable for what is in your souls."
    )
    pdf.paragraph(p8_t3, c3_x + 10, h - 115, col_w - 20, line_height=11.5, font="F1", size=7.2, rgb=WHITE)

    # -------------------------------------------------------------
    # PAGE 9: SPECIAL DEDICATION 3 — AYAH 285: THE UNIVERSAL CREED
    # -------------------------------------------------------------
    pdf.new_page(w, h)
    draw_mindmap_chrome(9, "SPECIAL DEDICATION 3: AYAH 285 - THE APOSTLES' CREED & SUBMISSION PLEDGE", "AYAH 2:285", "RECEIVED DIRECTLY IN MI'RAJ FROM BENEATH THE THRONE")

    # Layout: 2 Master Cards + Center Formula
    p9_w = (w - 70 - 20) / 2
    
    # Left Card: 4 Pillars of Conviction
    pdf.rect(35, 42, p9_w, h - 128, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.text("PART A: THE 4 PILLARS OF FAITH", 45, h - 95, font="F2", size=10, rgb=GOLD)
    pdf.line(45, h - 101, 35 + p9_w - 10, h - 101, stroke_rgb=BORDER_MUTED, line_width=0.8)

    p9_t1 = (
        "1. The Shared Horizon of Faith:\n"
        "   'Amana ar-rasulu bima unzila ilayhi min rabbihi wal-mu'minun.'\n"
        "   The Messenger is joined with the believers as the first and purest adherent.\n\n"
        "2. The Four Indivisible Pillars:\n"
        "   * Belief in Allah (Kullun amana billah)\n"
        "   * Belief in His Angels (Wa mala'ikatih)\n"
        "   * Belief in His Scriptures (Wa kutubih)\n"
        "   * Belief in His Messengers (Wa rusulih)\n\n"
        "3. Rejection of Sectarian Discrimination:\n"
        "   'La nufarriqu bayna ahadim-min rusulih.'\n"
        "   Believers do not commit Banu Isra'il's fatal error of accepting Musa while rejecting Isa or Muhammad (peace be upon them all)."
    )
    pdf.paragraph(p9_t1, 45, h - 118, p9_w - 20, line_height=13, font="F1", size=7.8, rgb=WHITE)

    # Right Card: The Submission Pledge & Cry for Forgiveness
    r_x = 35 + p9_w + 20
    pdf.rect(r_x, 42, p9_w, h - 128, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.text("PART B: THE SUBMISSION FORMULA & HUMILITY", r_x + 10, h - 95, font="F2", size=10, rgb=CYAN)
    pdf.line(r_x + 10, h - 101, r_x + p9_w - 10, h - 101, stroke_rgb=BORDER_MUTED, line_width=0.8)

    p9_t2 = (
        "1. The Golden Covenant: 'Sami'na wa Ata'na'\n"
        "   * 'We hear and we obey!'\n"
        "   * The moral antidote to Banu Isra'il's declaration: 'Sami'na wa 'Asayna' (We hear and disobey).\n"
        "   * True Islam is the immediate surrender of intellect, will, and action to Allah's decree.\n\n"
        "2. The Immediate Reflex of Humility:\n"
        "   'Ghufranaka Rabbana wa ilaykal-masir.'\n"
        "   * After pledging total obedience, the believer does not boast or claim perfection.\n"
        "   * Human obedience is always deficient before Divine Majesty.\n"
        "   * We immediately plead: 'Your forgiveness, our Lord!'\n"
        "   * To You alone is the final homecoming."
    )
    pdf.paragraph(p9_t2, r_x + 10, h - 118, p9_w - 20, line_height=13, font="F1", size=7.8, rgb=WHITE)

    # -------------------------------------------------------------
    # PAGE 10: SPECIAL DEDICATION 4 — AYAH 286: THE 7 MASTER PETITIONS
    # -------------------------------------------------------------
    pdf.new_page(w, h)
    draw_mindmap_chrome(10, "SPECIAL DEDICATION 4: AYAH 286 - THE CHARTER OF MERCY & 7 MASTER PETITIONS", "AYAH 2:286", "DIVINE GRACE & THE COSMIC PRAYER OF VICTORY")

    # Layout: Top Charter Box + 7 Petitions Grid Below
    # Top Charter Box: Wus'aha
    c_w = w - 70
    c_h = 55
    pdf.rect(35, h - 138, c_w, c_h, fill_rgb=NAVY_LIGHT, stroke_rgb=GOLD, line_width=1.2)
    pdf.text("THE DIVINE CHARTER OF FAIRNESS & CAPACITY (AL-WUS')", 45, h - 95, font="F2", size=9.5, rgb=GOLD)
    pdf.text('"La yukallifullahu nafsan illa wus\'aha, laha ma kasabat wa \'alayha maktasabat"', 45, h - 110, font="F5", size=9.5, rgb=WHITE)
    pdf.text("Allah never burdens a soul beyond capacity. Good is earned naturally (kasabat); evil requires strained labor (iktasabat).", 45, h - 124, font="F1", size=7.5, rgb=GOLD_LIGHT)

    # 7 Petitions Grid: 2 Columns Below
    pet_y = 42
    pet_h = h - 138 - 50
    pet_col_w = (c_w - 16) / 2

    # Left Column: Petitions 1 to 3
    pdf.rect(35, pet_y, pet_col_w, pet_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1)
    pdf.text("PETITIONS 1 - 3: BURDEN-LIFTING DU'AS", 45, pet_y + pet_h - 18, font="F2", size=9, rgb=EMERALD)
    pdf.line(45, pet_y + pet_h - 24, 35 + pet_col_w - 10, pet_y + pet_h - 24, stroke_rgb=BORDER_MUTED, line_width=0.8)

    p10_t1 = (
        "1. Pardon of Inadvertence:\n"
        "   'Rabbana la tu'akhidhna in naseena aw akhta'na.'\n"
        "   Do not hold us accountable if we forget or make unintentional slips.\n\n"
        "2. Relief from Crushing Burdens (Al-Isr):\n"
        "   'Rabbana wa la tahmil \'alayna isran kama hamaltahu \'alalladhina min qablina.'\n"
        "   Do not lay upon us a shackling burden like that placed on Banu Isra'il due to their rebellion.\n\n"
        "3. Protection from Breaking-Point Tribulations:\n"
        "   'Rabbana wa la tuhammilna ma la taqata lana bih.'\n"
        "   Do not burden us with calamities exceeding our endurance."
    )
    pdf.paragraph(p10_t1, 45, pet_y + pet_h - 40, pet_col_w - 20, line_height=12, font="F1", size=7.5, rgb=WHITE)

    # Right Column: Petitions 4 to 7 (Grace & Victory)
    r2_x = 35 + pet_col_w + 16
    pdf.rect(r2_x, pet_y, pet_col_w, pet_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1)
    pdf.text("PETITIONS 4 - 7: TRIPLE SHIELD & VICTORY", r2_x + 10, pet_y + pet_h - 18, font="F2", size=9, rgb=CYAN)
    pdf.line(r2_x + 10, pet_y + pet_h - 24, r2_x + pet_col_w - 10, pet_y + pet_h - 24, stroke_rgb=BORDER_MUTED, line_width=0.8)

    p10_t2 = (
        "4. 'Wa'fu 'anna' (Erase our sins):\n"
        "   Complete wiping away of past sins like footprints in sand.\n\n"
        "5. 'Waghfir lana' (Shield & protect us):\n"
        "   Armor (Mighfar) protecting from future recurrence and public shame.\n\n"
        "6. 'Warhamna' (Shower us in maternal mercy):\n"
        "   Unmerited divine grace and entry into Paradise.\n\n"
        "7. 'Anta Mawlana fansurna \'alal-qawmil-kafirin':\n"
        "   Cosmic Allegiance: You alone are our Supreme Guardian, so grant us victory over falsehood."
    )
    pdf.paragraph(p10_t2, r2_x + 10, pet_y + pet_h - 40, pet_col_w - 20, line_height=12, font="F1", size=7.5, rgb=WHITE)

    # Save Master PDF
    out_file = os.path.join(BASE_DIR, "Surah_Al_Baqarah_Landscape_Mindmap.pdf")
    pdf.save(out_file)

if __name__ == "__main__":
    print("--- COMPILING 10-PAGE SURAH AL-BAQARAH LANDSCAPE MINDMAP PDF ---")
    build_baqarah_landscape_mindmap()
    print("--- 10-PAGE LANDSCAPE MINDMAP PDF COMPILATION COMPLETE ---")
