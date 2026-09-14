#!/usr/bin/env python3
"""
Huurs Studio - Surah Saba Master Mindmap Vector PDF Generator
16:9 Landscape Widescreen (792 x 480 pt) • 8 Plates • 16 Pillars • 64 Cards
Strict Brand_Visual_System.md & Absolute Copyright Insulation
The Cosmic Hamd, Dawud's Iron, Sulayman's Staff, The Flood of 'Arim & The Solitary Reflection
"""

import os
import sys
import subprocess
import shutil

sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
OUTPUT_PDF = os.path.join(BASE_DIR, "SABA_MASTER_MINDMAP.pdf")
PREVIEWS_DIR = os.path.join(BASE_DIR, "previews_saba")
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

def build_saba_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH SABA", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
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
    # PLATE 01: THE COSMIC HAMD & THE ATOM'S WEIGHT
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 8,
        "THE COSMIC HAMD & THE OMNISCIENCE OF THE ATOM'S WEIGHT",
        "Pillars 1 & 2: Universal Doxology in Creation & Eternity, The Subatomic Scale & Infallible Register",
        "PLATE 01 : COSMIC OMNISCIENCE"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 01: UNIVERSAL PRAISE IN TWO REALMS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Cosmic Ownership, Hereafter Hamd & Four Vectors of Transit", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 1, "Universal Hamd in Two Realms",
              "Al-Hamdu lillahi alladhi lahu ma fis-samawati wa ma fil-ard: praise in primordial creation conjoined with eternal praise in the Hereafter.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 2, "Entering the Terrestrial Depths",
              "Ma yaliju fil-ard: rainwater penetrating deep aquifers, buried seeds germinating in darkness, and decomposing bodies awaiting rebirth.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 3, "Emerging into Living Reality",
              "Ma yakhruju minha: flora bursting into blossom, subterranean springs gushing, and resurrected souls emerging from graves.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 4, "Vertical Axis of Transit",
              "Ma yanzilu min as-sama' wa ma ya'ruju feeha: revelation and angels descending while deeds, supplications, and pure souls ascend.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 02: THE SUBATOMIC SCALE & INFALLIBLE REGISTER", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Skepticism Over the Hour, Solemn Divine Oath & Mithqala Dharrah", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 5, "Cynical Denial of the Hour",
              "La ta'teena as-sa'ah: polytheists scoffing at eschatological judgment, assuming death is total oblivion without moral consequence.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 6, "The Solemn Divine Oath",
              "Qul bala wa Rabbi lata'tiyannakum: an unyielding oath by the Knower of the Unseen swearing the Hour will strike with absolute certainty.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 7, "The Weight of an Atom",
              "La ya'zubu 'anhu mithqalu dharrah: not an atom's weight escapes His divine knowledge in heavens or earth, refuting all materialist doubt.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 8, "The Infallible Cosmic Register",
              "Wa la asgharu min dhalika wa la akbaru illa fee Kitabin Mubeen: nothing smaller or larger exists except inscribed in a clear book.")

    # ==========================================
    # PLATE 02: SLANDER OF DELIRIUM & COSMIC VULNERABILITY
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 8,
        "THE SLANDER OF DELIRIUM & CELESTIAL VULNERABILITY",
        "Pillars 3 & 4: The Psychology of Disintegration Skepticism & Ground-Fissures Beneath Arrogance",
        "PLATE 02 : COSMIC VULNERABILITY"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 03: DISINTEGRATION SKEPTICISM & SLANDER", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("The Mocking Banter of Quraysh & The False Dilemma of Madness", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 9, "The Mocking Query of Quraysh",
              "Hal nadullukum 'ala rajul: the tribal elite pointing at the Prophet with derision, turning divine warnings into theatrical mockery.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 10, "The Riddle of Disintegration",
              "Idha muzziqtum kulla mumazzaq: asserting that reassembling scattered bodily molecules across vast deserts is biologically impossible.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 11, "The False Dilemma of Madness",
              "Aftara 'ala Allahi kadhiban am bihi jinnah: falsely claiming the Messenger is either a calculating fraud or afflicted with delirium.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 12, "Unmasking the Moral Escape",
              "Balilladheena la yu'minoona bil-akhirati fil-'adhab: exposing skepticism as an excuse to indulge in injustice without accountability.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 04: THE FRAGILE TERRESTRIAL FLOOR", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Enveloping Cosmic Canopies, Fissuring Mantle & Signs for the Penitent", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 13, "Enveloping Cosmic Canopy",
              "Afa-lam yaraw ila ma bayna aydeehim wa ma khalfahum: humans are enclosed above and below by cosmic architecture held by divine command.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 14, "The Latent Ground-Fissure",
              "In nasha' nakhsif bihim al-ard: the fragile geological crust can rupture instantly, swallowing cities that walk upon it with arrogance.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 15, "Falling Celestial Fragments",
              "Aw nusqit 'alayhim kisafan min as-sama': the celestial dome is capable of releasing crushing fragments upon ungrateful empires.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 16, "Signs for the Penitent Servant",
              "Inna fee dhalika la-ayatan li-kulli 'abdin muneeb: cosmic vulnerability is a compassionate sign for every soul turning back to Allah.")

    # ==========================================
    # PLATE 03: THE DYNASTY OF GRATITUDE (DAWUD'S IRON)
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 8,
        "THE DYNASTY OF GRATITUDE: DAWUD'S MOLTEN IRON",
        "Pillars 5 & 6: Cosmic Echoes of Mountains and Birds, Pliable Iron & Defensive Metallurgy",
        "PLATE 03 : DAWUD'S IRON"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 05: SYMPHONIC PRAISE OF NATURE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Divine Grace Bestowed, Singing Granite Peaks & Airborne Flocks", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 17, "Divine Favor Upon Dawud",
              "Wa laqad atayna Dawooda minna fadla: electing David with unique spiritual, political, and acoustic blessings unmatched in history.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 18, "Symphonic Mountain Echoes",
              "Ya jibalu awwibee ma'ahu: commanding towering stone peaks to resonate with and repeat his rhythmic psalms of glorification.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 19, "Flocks of Attuned Birds",
              "Wat-tayr: airborne flocks halting in flight and descending to synchronize their songs with David's melodious praise of the Creator.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 20, "Cosmic Sympathy of Matter",
              "The physical universe is intrinsically conscious and worshipping, joining the voice of the human servant whose heart is pure.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 06: PLIABLE IRON & SACRED METALLURGY", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Malleable Iron, Defensive Interlocking Armor & Balanced Engineering", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 21, "Iron Malleable in Bare Hands",
              "Wa alanna lahu al-hadeed: solid iron rendered soft as wax or clay without forge fire, demonstrating divine mastery over materials.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 22, "Defensive Interlocking Armor",
              "An i'mal sabighat: weaving protective chain mail coats to shield human lives rather than forging cruel weapons of imperial conquest.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 23, "Precision Engineering of Links",
              "Wa qaddir fis-sard: calibrating the weight and thickness of ring links with balanced precision so defense does not exhaust the bearer.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 24, "Sanctity of Manual Labor",
              "Dawud sustained his regal household entirely through manual labor, establishing the supreme spiritual dignity of honest craft.")

    # ==========================================
    # PLATE 04: THE KINGDOM OF SULAYMAN (WINDS & COPPER)
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 8,
        "THE KINGDOM OF SULAYMAN: SUBJUGATED WINDS & COPPER",
        "Pillars 7 & 8: The Monthly Wind, Fluid Brass Spring, Jinn Architecture & Active Gratitude",
        "PLATE 04 : SULAYMAN'S EMPIRE"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 07: SUBJUGATED WINDS & FLUID BRASS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("The Monthly Atmospheric Journey, 'Ayn al-Qitr & Conscripted Jinn", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 25, "The Subjugated Atmospheric Wind",
              "Ghuduwwuha shahrun wa rawahuha shahr: wind harnessed to traverse a one-month caravan journey between dawn and midday across his realm.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 26, "The Spring of Molten Copper",
              "Asalna lahu 'ayn al-qitr: a subterranean fountain of liquid copper flowing like water for three days, supplying metal for construction.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 27, "Conscripted Jinn Under Mandate",
              "Wa min al-jinni man ya'malu bayna yadayh: Jinn subjugated to his authority not by occult sorcery, but by the direct permission of his Lord.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 28, "Angelic Enforcement of Order",
              "Man yazigh minhum 'an amrina nudhiqhu min 'adhabi as-sa'eer: angels instantly chastising any rebellious spirit deviating from duty.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 08: JINN CRAFT & THE AXIOM OF WORK", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Palaces, Feeding Reservoirs, I'maloo Shukra & The Rarity of the Grateful", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 29, "Sanctuaries & Monumental Forts",
              "Ya'maloona lahu ma yashaa'u min mahareeb wa tamatheel: constructing soaring fortresses, prayer sanctuaries, and architectural marvels.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 30, "Reservoirs & Anchored Cauldrons",
              "Jifan kal-jawab wa qudoor rasiyat: banquet basins broad as cisterns and immovable cauldrons deployed to feed armies and the poor.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 31, "The Golden Axiom of Gratitude",
              "I'maloo ala Dawooda shukra: gratitude in Islam is an active imperative verb; deploying every bestowed power in devotional service.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 32, "Rarity of the Truly Grateful",
              "Wa qaleelun min 'ibadiya ash-shakoor: divine testimony that while many thank with the tongue, few embody active, systemic gratitude.")

    # ==========================================
    # PLATE 05: SULAYMAN'S STAFF & OCCULT DEMOLITION
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        5, 8,
        "SULAYMAN'S STAFF & OCCULT DEMOLITION",
        "Pillars 9 & 10: Silent Departure in Prayer, The Wood-Boring Insect & Shattering Jinn Omniscience",
        "PLATE 05 : OCCULT DEMOLITION"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 09: THE SILENT DEMISE IN PRAYER", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Decree of Mortality, Leaning Sentinel & Months of Veiled Transition", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 33, "The Universal Decree of Mortality",
              "Falamma qadayna 'alayhi al-mawt: even Solomon, the master of kings and winds, passes away by the unyielding divine decree of death.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 34, "Standing Leaned Upon the Staff",
              "His noble soul departs while standing in his prayer chamber, his physical frame supported upright by his wooden staff (Minsa'ah).")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 35, "The Agonizing Toil of the Jinn",
              "The Jinn continue sweating in grueling, humiliating labor, terrified by the motionless silhouette of the king watching over them.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 36, "Months of Veiled Transition",
              "An extended period transpires wherein the ruler is dead yet his posture of command keeps thousands under strict discipline.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 10: DEMOLITION OF OCCULT SUPERSTITION", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("The Termite at the Core, The Collapse & Exposing Jinn Blindness", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 37, "The Minute Wood-Boring Insect",
              "Dabbat al-ard ta'kulu minsa'atah: an infinitesimal termite chewing through the wooden fibers of the staff, grain by tiny grain.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 38, "The Collapse to the Earth",
              "Falamma kharra: when the hollowed staff snaps, the king's body falls to the floor, instantly dissolving the illusion of presence.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 39, "Exposing Jinn Ignorance",
              "Law kanoo ya'lamoona al-ghayb: had the Jinn known the unseen, they would not have remained in humiliating torment serving a corpse.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 40, "Demolition of Astrology & Sorcery",
              "A decisive theological blow freeing humanity from fear of the occult; knowledge of the Unseen belongs exclusively to Allah.")

    # ==========================================
    # PLATE 06: THE CIVILIZATION OF SABA & BURST DAM
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        6, 8,
        "THE CIVILIZATION OF SABA: THE TWO GARDENS & BURST DAM",
        "Pillars 11 & 12: Hydraulic Paradise of Ma'rib, Baldatun Tayyibah, Sayl al-'Arim & Bitter Scrubland",
        "PLATE 06 : COLLAPSE OF SABA"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 11: BALDATUN TAYYIBAH (PARADISE)", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("The Dam of Ma'rib, Twin Garden Valleys & Effortless Abundance", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 41, "The Divine Sign in Ma'rib",
              "Laqad kana li-Saba'in fee maskanihim ayah: a monumental stone dam channeling mountain monsoons into agricultural wonder.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 42, "Twin Terraced Garden Valleys",
              "Jannatani 'an yameenin wa shimal: twin flourishing garden valleys flanking the city, producing endless sweet fruits and vines.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 43, "A Pure, Disease-Free Realm",
              "Baldatun tayyibah: wholesome soil and pure air so devoid of pests that fruit dropped into baskets carried effortlessly by strollers.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 44, "The Simple Mandate of Faith",
              "Kuloo min rizqi Rabbikum washkuroo lah: eat from divine provision, live with modesty, and thank an All-Forgiving Lord.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 12: SAYL AL-'ARIM (CATACLYSM)", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Ingratitude, The Bursting Dam, Ecological Ruin & Recompense", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 45, "Civilizational Ingratitude",
              "Fa-a'radoo: turning away from prophets, becoming bored of continuous ease, and attributing hydraulic triumph to human genius.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 46, "The Cataclysmic Burst Dam",
              "Fa-arsalna 'alayhim sayla al-'arim: subterranean burrowing undermining the stone masonry; monsoons bursting the dam in a tidal wave.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 47, "Desolate Scrubland Replacement",
              "Dhawatay ukulin khamt wa athl wa sidrin qaleel: sweet fruit replaced by bitter desert shrubs, barren tamarisk, and sparse thorns.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 48, "The Immutable Penalty of Ingratitude",
              "Dhalika jazaynahum bima kafaroo: divine justice penalizing pride; transforming an agricultural Eden into an arid wilderness.")

    # ==========================================
    # PLATE 07: PROXIMITY FATIGUE & SCATTERING OF SABA
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        7, 8,
        "PROXIMITY FATIGUE & THE SCATTERING OF NATIONS",
        "Pillars 13 & 14: Connected Highways, The Arrogant Prayer for Distance, Folklore & Iblis's Bet",
        "PLATE 07 : DISPERSAL OF SABA"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 13: THE SIN OF PROXIMITY FATIGUE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Visible Road Settlements, Seamless Security & Demanding Hardship", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 49, "Connected Visible Settlements",
              "Quran zahirah: an unbroken chain of flourishing towns linking Yemen to Syria, allowing merchants to travel without rations.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 50, "Measured Security by Night and Day",
              "Qaddarna feeha as-sayr seeroo feeha layaliya wa ayyaman amineen: seamless safety where no traveler feared bandits or thirst.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 51, "Arrogant Prayer for Desert Distance",
              "Rabbana ba'id bayna asfarina: merchant oligarchs tired of egalitarian safety, begging for arduous deserts to monopolize trade.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 52, "Self-Inflicted Oppression",
              "Wa zalamoo anfusahum: despising widespread comfort and demanding artificial scarcity, sealing their own civilizational doom.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 14: DISSOLUTION & IBLIS'S BET", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Scattered into Folklore Tales, Mazzaqnahum, Sabbar-Shakoor & Satan's Guess", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 53, "Reduced to Cautionary Tales",
              "Fa-ja'alnahum ahadeeth: the mighty empire collapsing into campfire folklore and oral proverbs across the Arabian peninsula.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 54, "Utter Tribal Dispersal",
              "Wa mazzaqnahum kulla mumazzaq: tribes scattered to the winds; Ghassan to Syria, Aws and Khazraj to Yathrib, Khuza'ah to Mecca.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 55, "The Twin Virtues of Reflection",
              "Inna fee dhalika la-ayatin li-kulli sabbarin shakoor: historical rise and fall understood only by those uniting Sabr and Shukr.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 56, "The Confirmation of Iblis's Guess",
              "Wa laqad saddaqa 'alayhim Ibleesu zannahu: Satan's cynical bet that mankind would prove ungrateful verified in the ruin of Saba.")

    # ==========================================
    # PLATE 08: ANGELIC AWE, SOLITUDE & FINAL PARTITION
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        8, 8,
        "ANGELIC AWE, SOLITARY REFLECTION & FINAL PARTITION",
        "Pillars 15 & 16: Quadruple Demolition of Idols, Angelic Terror at Divine Speech & The Solitary Awakening",
        "PLATE 08 : FINAL AWAKENING"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 15: DEMOLITION OF SHIRK & ANGELIC AWE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Severing the 4 Roots of Idolatry & Archangels Prostrating in Dread", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 57, "Severing False Ownership & Partnership",
              "La yamlikoona mithqala dharrah: idols possess zero atomic ownership in heaven or earth, and share zero percentage of creation.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 58, "Zero Divine Need for Assistance",
              "Wa ma lahu minhum min dhaheer: the Sovereign Lord requires no minister, cabinet, or helper among created entities.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 59, "The True Boundary of Intercession",
              "Wa la tanfa'u ash-shafa'atu 'indahu illa liman adhina lah: autonomous mediation abolished; intercession operates solely by divine license.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 60, "Angelic Dread at Divine Speech",
              "Hatta idha fuzzi'a 'an quloobihim: archangels falling trembling like chains on stone when Allah speaks, declaring His Word Al-Haqq.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 16: SOLITARY AWAKENING & THE PARTITION", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Universal Mission, Standing Alone Before Allah & The Irreversible Chasm", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 61, "Universal Prophetic Mission",
              "Wa ma arsalnaka illa kaffatan lin-nasi: the Messenger sent comprehensively to all humanity as bringer of glad tidings and warner.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 62, "The Solitary Intellectual Mandate",
              "An taqoomoo lillahi mathna wa furada: step outside the noise of the mob; contemplate alone before Allah and recognize prophetic truth.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 63, "Impossibility of Belated Reaching",
              "Wa anna lahumu at-tanawooshu min makanin ba'eed: reaching for faith after judgment has begun is as impossible as grasping across a void.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 64, "The Irreversible Final Partition",
              "Wa heela baynahum wa bayna ma yashtahoon: an impenetrable barrier descends between them and what they desire, sealing doubt forever.")

    # Save PDF
    pdf.save(OUTPUT_PDF)
    print(f"[OK] Successfully built Surah Saba Master Mindmap PDF: {OUTPUT_PDF}")

    # Render Previews
    cmd = ["pdftoppm", "-png", "-r", "150", OUTPUT_PDF, os.path.join(PREVIEWS_DIR, "page")]
    subprocess.run(cmd, check=True)
    print(f"[OK] Rendered preview images in {PREVIEWS_DIR}")

    # Copy to brain dir
    for i in range(1, 9):
        src = os.path.join(PREVIEWS_DIR, f"page-{i}.png")
        dst = os.path.join(brain_dir, f"saba_mindmap_page_{i}.png")
        if os.path.exists(src):
            shutil.copyfile(src, dst)
            print(f"[OK] Copied plate {i} preview to {dst}")

if __name__ == "__main__":
    build_saba_pdf()
