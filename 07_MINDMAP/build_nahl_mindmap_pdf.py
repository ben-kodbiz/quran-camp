#!/usr/bin/env python3
"""
Huurs Studio - Surah An-Nahl Master Mindmap Vector PDF Generator
16:9 Landscape Widescreen (792 x 480 pt) • 8 Plates • 16 Pillars • 64 Cards
"""

import os
import sys
import subprocess
import shutil

sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
OUTPUT_PDF = os.path.join(BASE_DIR, "NAHL_MASTER_MINDMAP.pdf")
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

def build_nahl_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH AN-NAHL", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
        # Badges
        pdf.rect(w - 280, h - 32, 175, 20, fill_rgb=NAVY_ELEVATED, stroke_rgb=BORDER_MUTED, line_width=0.8)
        pdf.text(f"PAGE {pnum:02d} / {total_pages:02d}", w - 85, h - 26, font="F2", size=9, rgb=GOLD)

        # Sub-header Title Area
        pdf.text(title, 32, h - 66, font="F2", size=12.5, rgb=WHITE)
        pdf.text(subtitle, 32, h - 79, font="F1", size=7.8, rgb=TEXT_MUTED)

        # Right Section Badge
        badge_str = f"[{section_badge}]"
        badge_w = len(badge_str) * 6.1
        pdf.text(badge_str, (w - 32) - badge_w, h - 68, font="F2", size=10.5, rgb=GOLD)

        pdf.line(32, h - 86, w - 32, h - 86, stroke_rgb=BORDER_MUTED, line_width=0.8)

        # Footer Bar
        pdf.line(32, 36, w - 32, 36, stroke_rgb=BORDER_MUTED, line_width=0.8)
        pdf.text("HUURS STUDIO  *  READ. REFLECT. RETURN.  *  SUNNI SOURCE DISCIPLINE (TABARI, IBN KATHIR, QURTUBI, RAZI, BAGHAWI)", 32, 22, font="F1", size=7.2, rgb=TEXT_MUTED)
        pdf.text("PROPRIETARY CARTOGRAPHY  *  STRICTLY VERIFIED TIER-1", w - 275, 22, font="F2", size=7.2, rgb=GOLD)

    c1_x = 32
    c2_x = 412
    c1_w = 348
    c2_w = 348
    c1_y = 48
    c1_h = 332

    # =========================================================================
    # PAGE 1: THE INEVITABLE DECREE & THE REALM OF LIVESTOCK
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 8,
        "THE INEVITABLE DECREE & THE REALM OF LIVESTOCK",
        "Pillars 1 & 2: Cosmic Sovereignty, Bil-Haqq & The Aesthetic Splendor of Herds (Jamal)",
        "PLATE 01 : DECREE & LIVESTOCK"
    )

    # Column 1: Pillar 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 1: THE SOVEREIGN DECREE & COSMIC CREATION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Ata Amru Allah, Warning Angels, Bil-Haqq & Human Disputation", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. The Inevitable Decree: Ata Amru Allah", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Opening with thunderous finality: 'The decree of Allah has arrived, so do not hasten it.'\n"
        "- Using past tense (Ata) to denote the absolute certainty of the eschatological reckoning.\n"
        "- Exalting the Creator far above the petty partners and false gods ascribed to Him."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("2. Angels Descending with the Spirit of Warning", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Allah dispatches the angels carrying the Spirit of revelation by His sovereign decree.\n"
        "- Entrusted to chosen prophetic vessels with a singular core message: 'No deity but Me.'\n"
        "- Establishing God-consciousness (Taqwa) as the sole rational response to divine majesty."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("3. Creation of the Heavens & Earth in Truth (Bil-Haqq)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The cosmos brought into existence not by accident or whim, but in transcendent Truth.\n"
        "- Exquisite mathematical order, purpose, and physical laws governing all celestial bodies.\n"
        "- Transcending all polytheistic pantheons: God has no associates in cosmic architecture."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("4. From Humble Sperm-Drop to Argumentative Adversary", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Biological origin: fashioned from a microscopically humble fluid drop (Nutfah).\n"
        "- The astonishing arrogance of human nature: evolving into a blatant, contentious debater.\n"
        "- Challenging the Creator with insolent skepticism regarding resurrection."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 2: GRAZING LIVESTOCK & AESTHETIC MAJESTY", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Thermal Warmth, Visual Beauty (Jamal) & Travel Beyond Strength", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("5. Livestock Created for Warmth, Nourishment & Utility", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Cattle, sheep, and camels created specifically to sustain human physiological life.\n"
        "- Providing natural thermal protection through wool, hair, and leather, alongside sustenance.\n"
        "- Tangible biological infrastructure demonstrating divine mercy woven into animal creation."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("6. Aesthetic Beauty in Departure & Return (Jamal)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'And for you in them is aesthetic beauty (Jamal) when you bring them in and lead them out.'\n"
        "- Validating human aesthetic joy: witnessing flourishing herds returning at golden twilight.\n"
        "- Connecting economic prosperity with deep visual tranquility and gratitude to the Giver."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("7. Carrying Burdens to Distant Lands Beyond Strength", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Subjugating heavy beasts to carry cargo across vast, inhospitable desert distances.\n"
        "- Journeys that human bodies could never accomplish except through extreme personal anguish.\n"
        "- Proof of a Lord who is inherently Kind (Ra'oof) and Boundlessly Merciful (Raheem)."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("8. Mounts of Splendor & Divine Creations Yet Unknown", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Horses, mules, and donkeys engineered for rapid travel and dignified splendor (Zeenah).\n"
        "- Prophetic foresight: 'And He creates that which you do not yet know.'\n"
        "- Encompassing all future technological modes of transit—automotive, aviation, and space."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 2: HYDROLOGIC BOUNTIES & THE OCEANIC HIGHWAYS
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 8,
        "HYDROLOGIC BOUNTIES & THE OCEANIC HIGHWAYS",
        "Pillars 3 & 4: Agrarian Flora, Marine Harvest, Mountain Pegs & Innumerable Favors",
        "PLATE 02 : RAIN & OCEANS"
    )

    # Column 1: Pillar 3
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 3: DOWNPOUR FROM SKIES & MULTI-COLORED EARTH", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Rain, Olives, Palms, Vineyards & Terrestrial Diversity", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("9. Rain Producing Refreshing Drink & Lush Pastures", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- He sends down life-giving water from the clouds for human consumption and hydration.\n"
        "- Awakening fertile pasturelands where domestic herds graze in safety and nourishment.\n"
        "- The continuous atmospheric cycle operating as an unearned, vital gift to human civilization."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("10. Agrarian Abundance: Olives, Palms, Grapes & Fruits", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Sprouting diverse crops from single soil: olive groves, date palms, and vineyards.\n"
        "- Yielding endless varieties of fruits, tastes, and chemical compositions for human health.\n"
        "- An undeniable, living sign for individuals who engage in deep, reflective contemplation."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("11. Celestial Synchronization: Day, Night, Sun & Stars", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Subjugating the rotational alternation of night for rest and day for economic endeavor.\n"
        "- Sun and moon bound to rhythmic orbits, with stellar constellations obedient to command.\n"
        "- Cosmic chronometry engineered specifically to anchor human agriculture and time."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("12. Earth's Multi-Colored Splendor: Mukhtalifan Alwanuh", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Dispersing across the earthly landscape minerals, soils, flora, and fauna in varied colors.\n"
        "- The staggering diversity of biodiversity and geology reflecting limitless creative power.\n"
        "- A resonant, profound reminder for a people who actively cultivate conscious remembrance."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 4
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 4: OCEANIC TREASURES & INNUMERABLE FAVORS", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Tender Meat, Pearls, Mountain Pegs & La Tuhsooha", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("13. The Subjugated Sea: Fresh Tender Meat & Pearls", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Subjugating the maritime expanse so humans may harvest succulent, tender seafood.\n"
        "- Extracting brilliant pearls, corals, and jewelry to adorn human culture and beauty.\n"
        "- The oceans functioning as an inexhaustible, self-replenishing pantry and treasure house."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("14. Ships Plowing Through Swelling Waves (Mawakhiroo)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Giant naval vessels carving through churning deep waters by divine buoyancy laws.\n"
        "- Facilitating global commerce, maritime exchange, and the pursuit of divine economic bounty.\n"
        "- Human navigation across violent ocean swells functioning as a school for gratitude."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("15. Stabilizing Mountain Pegs, River Highways & Stars", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Casting deep, stabilizing mountain roots into the earth lest it wobble beneath humanity.\n"
        "- Carving freshwater rivers, valley pathways, and celestial star-maps for desert guidance.\n"
        "- Terrestrial and astronomical wayfinding systems ensuring safe passage across the planet."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("16. Incalculable Ocean of Divine Favors (La Tuhsooha)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The supreme mathematical reality: 'If you count Allah's favors, never could you enumerate them.'\n"
        "- Divine gifts surpass human cognitive, linguistic, and computational capacity to record.\n"
        "- Balancing human failure with divine grace: 'Indeed, Allah is All-Forgiving, Most Merciful.'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 3: THE SKEPTIC'S ARROGANCE & TRAGEDY OF INFANTICIDE
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 8,
        "THE SKEPTIC'S ARROGANCE & TRAGEDY OF INFANTICIDE",
        "Pillars 5 & 6: Cognitive Blindness of Shirk, The Darkened Face & Divine Forbearance",
        "PLATE 03 : SHIRK & INFANTICIDE"
    )

    # Column 1: Pillar 5
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 5: IMPOTENCE OF FALSE IDOLS & ARROGANCE UNVEILED", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Lifeless Deities, Arrogant Hearts & Bearing Full Burdens", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("17. Dead, Lifeless Idols Devoid of Resurrective Knowledge", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Fabricated gods create nothing; they are themselves inanimate objects manufactured by hands.\n"
        "- Deceased, lifeless entities lacking all sensory awareness, hearing, or consciousness.\n"
        "- Completely ignorant of the timing of resurrection, unable to aid themselves or devotees."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("18. Monotheistic Truth & Arrogant Rejection of the Heart", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Your God is One indivisible God; pure monotheism is the sole coherent worldview.\n"
        "- Those who deny the Hereafter suffer from psychological denial: their hearts reject truth.\n"
        "- Arrogance (Mustakbiroon) as the foundational spiritual sickness blinding human intellect."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("19. Omniscience of What is Secret and Declared", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Without doubt, Allah possesses absolute awareness of what human souls conceal and declare.\n"
        "- No whisper of conspiracy, private vice, or hidden motive escapes divine surveillance.\n"
        "- The solemn declaration: Allah possesses zero love for the haughty and the arrogant."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("20. Cynical Dismissal: Tales of Antiquity & Full Burdens", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- When asked what their Lord revealed, cynics dismissively scoff: 'Fables of ancient peoples!'\n"
        "- Attempting to trivialize transcendent moral truth into primitive cultural myth.\n"
        "- Bearing the crushing weight of their own sins on Judgment Day, alongside those they misled."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 6
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 6: SHAME OF DARKENED FACES & FORBEARANCE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Buried Daughters, Suppressed Rage & Divine Postponement", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("21. Hypocrisy of Attributing Daughters to Allah", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The shocking theological inconsistency: pagans ascribing angelic daughters to God.\n"
        "- Claiming for the Sovereign of the universe what they themselves despise in their culture.\n"
        "- Exposing the moral bankruptcy and irrational prejudice of polytheistic belief systems."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("22. Grief and Rage of Pagan Infanticide (Muswaddan)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- When informed of the birth of a female infant, the father's face turns black with shame.\n"
        "- Consumed with suppressed fury and toxic social embarrassment before his tribal peers.\n"
        "- The psychological anatomy of misogynistic pride rejecting the sacred gift of female life."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("23. Contemplating Dust: Humiliation vs. Burial Alive", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The horrific dilemma: whether to raise her in disgrace or bury her alive in dust (Yadussuhu).\n"
        "- 'Evil indeed is the judgment they make!'—Divine condemnation of female infanticide.\n"
        "- The Qur'an acting as the revolutionary defender and sanctifier of female infant rights."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("24. Divine Forbearance: Why Retribution is Delayed", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'If Allah held mankind accountable for injustice, not a creature would remain alive.'\n"
        "- Divine patience (Hilm) granting humanity an appointed term rather than swift destruction.\n"
        "- When their decreed expiration arrives, neither delay nor advancement is possible."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 4: THE BIOLOGICAL MIRACLE OF MILK & THE BEE'S HONEY
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 8,
        "THE BIOLOGICAL MIRACLE OF MILK & THE BEE'S HONEY",
        "Pillars 7 & 8: Mammalian Lactation, Human Senescence & Divine Inspiration to the Bee",
        "PLATE 04 : MILK & THE BEE"
    )

    # Column 1: Pillar 7
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 7: PURE MILK FROM INTESTINAL CHYME & THE VINE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Farth & Dam, Palatable Lactation & Decrepit Senility", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("25. Living Sign: Pure Milk Between Chyme and Blood", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'And indeed, for you in grazing livestock is a profound, instructive lesson.'\n"
        "- Extracting wholesome, nourishing milk from between digestive chyme and blood.\n"
        "- A staggering biological filter converting digestion into pristine nutrition without taint."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("26. Palatable to Drinkers (Khalisan Sa'ighan)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Milk emerging pure white, completely free of the odor of chyme or color of blood.\n"
        "- Smooth, palatable, and nutritious, designed perfectly for human physiological health.\n"
        "- An everyday biological miracle demonstrating divine precision operating within mammals."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("27. Dates and Grapes: Wholesome Life-Sustaining Provision", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Harvesting from date palms and grapevines both intoxicating drink and pure sustenance.\n"
        "- Contrasting destructive intoxicants with wholesome, life-sustaining foods (Rizqan hasana).\n"
        "- A profound sign for communities endowed with critical thinking and moral discernment."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("28. Human Senescence: Decrepit Infancy (Ardhal al-'Umr)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Allah creates human beings, causes them to grow, and eventually takes them in death.\n"
        "- Some individuals relegated to the most decrepit stage of extreme old age (Ardhal al-'Umr).\n"
        "- Losing memory and cognitive faculties after possessing knowledge; humbling human pride."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 8
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 8: ARCHITECTURE OF THE BEE (AL-NAHL) & HEALING", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Inspiration of the Hive, Subdued Paths & Medicinal Honey", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("29. Divine Inspiration (Wahy) to the Sovereign Bee", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'And your Lord revealed and inspired to the bee (Al-Nahl)...'\n"
        "- Bestowing biological instinct, structural intelligence, and navigational programming.\n"
        "- Nature guided directly by divine software to perform complex social and architectural feats."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("30. Geometric Architectural Homes in Mountains & Trees", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Instructing the bee to construct its hives in mountain crevices, trees, and structures.\n"
        "- The hexagonal comb geometry maximizing volume, structural integrity, and efficiency.\n"
        "- Marvel of bio-engineering executed without formal schooling by divine calibration."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("31. Subdued Pathways & Feeding on Diverse Nectars", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Commanding the bee to feed upon the sweet nectars of diverse flowers and fruits.\n"
        "- Traversing complex navigational flight paths made smooth and accessible by its Creator.\n"
        "- Flawless spatial memory and communication dances returning safely to the central hive."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("32. The Golden Liquid: Varied Hues & Healing for Humanity", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Secreting from their bellies a rich, concentrated liquid of varied colors.\n"
        "- 'In it is healing and medicine for humanity' (Feehi shifa'un lin-nas).\n"
        "- A medical, biological, and contemplative testament for a society that ponders signs."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 5: TWO PARABLES OF INEQUALITY & DOMESTIC SANCTUARIES
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        5, 8,
        "TWO PARABLES OF INEQUALITY & DOMESTIC SANCTUARIES",
        "Pillars 9 & 10: The Helpless Slave vs. Free Benefactor, Sensory Emergence & Homes",
        "PLATE 05 : PARABLES & HOMES"
    )

    # Column 1: Pillar 9
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 9: BOUND SLAVE VS. FREE BENEFACTOR & BURDEN", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Unequal Provision, The Mute Burden & The Twinkling Hour", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("33. Hierarchy of Worldly Provision & Ungrateful Disavowal", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Allah has favored some over others in the distribution of economic provision.\n"
        "- Wealthy elites refuse to share their fortunes equally with subordinates, guarding wealth.\n"
        "- The biting paradox: humans protect property, yet ascribe partners to God's dominion!"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("34. Parable of Helpless Bonded Slave vs. Free Master", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The first master parable: A slave possessed by another, completely powerless.\n"
        "- Juxtaposed against a free man richly endowed, spending generously in secret and open.\n"
        "- 'Are they equal? Praise belongs to Allah! But most of humanity does not comprehend.'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("35. Parable of the Mute Burden vs. Champion of Justice", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The second parable: A man dumb, mute, completely incapable of any productive endeavor.\n"
        "- A heavy, useless burden (Kallun) on his guardian; wherever directed, he brings zero good.\n"
        "- Can he be compared to an enlightened leader who commands justice and walks straight?"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("36. Unseen Realms of Heavens & Twinkling of the Hour", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- To Allah alone belongs the absolute unseen realm (Ghayb) of the heavens and earth.\n"
        "- The arrival of the Final Hour is as instantaneous as the twinkling of an eye, or swifter.\n"
        "- Reaffirming that divine omnipotence encompasses every physical and metaphysical domain."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 10
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 10: EMERGENCE FROM WOMB & DOMESTIC SANCTUARY", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Sensory Infrastructure, Birds in Flight & Shelters of Rest", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("37. Born from Wombs in Zero Knowledge: Endowed Faculties", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'And Allah extracted you from the wombs of your mothers knowing nothing at all.'\n"
        "- Born into this world completely devoid of knowledge, culture, language, or skills.\n"
        "- Stripping the intellectual of arrogance: all wisdom is an acquired, unearned gift."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("38. Hearing, Vision & Hearts Given for Thanksgiving", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Bestowing the auditory faculties, optical systems, and reflective hearts (Af'idah).\n"
        "- Cognitive infrastructure provided for a singular objective: that you might give thanks.\n"
        "- Using faculties to ignore divine truth is a catastrophic misuse of biological machinery."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("39. Birds Suspended in Vault of the Sky (Taskheer)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Do they not observe the birds held suspended in the atmospheric currents of the sky?\n"
        "- Nothing holds them aloft against gravity except the precise physical laws of God.\n"
        "- Signs of sublime aerodynamic calibration for individuals who anchor hearts in faith."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("40. Dwellings of Peace, Portable Leather Tents & Shade", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Providing settled houses as tranquil sanctuaries of privacy, security, and peace.\n"
        "- Engineering portable tents from animal hides, effortless to transport on travel days.\n"
        "- Furnishing wool, fur, and hair into garments, household goods, and protective shade."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 6: THE GOLDEN TRIAD OF ETHICS & THE UNRAVELING WEAVER
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        6, 8,
        "THE GOLDEN TRIAD OF ETHICS & THE UNRAVELING WEAVER",
        "Pillars 11 & 12: Justice, Ihsan, Kinship, The Unspooling Yarn & Hayatan Tayyibah",
        "PLATE 06 : ETHICS & TAYYIBAH"
    )

    # Column 1: Pillar 11
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 11: UNIVERSAL MORAL CHARTER: JUSTICE & IHSAN", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("'Adl, Ihsan, Kinship, Prohibitions of Fahsha' & Oaths", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("41. The Friday Mandate: Absolute Justice ('Adl)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Indeed, Allah orders justice (Al-'Adl)'—the non-negotiable foundation of human society.\n"
        "- Demanding fair weights, equitable legal administration, and the defense of human rights.\n"
        "- Prohibiting favoritism, corruption, and systemic oppression across all civic institutions."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("42. Transcendent Excellence (Ihsan) & Generosity to Kin", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Elevating society beyond mere bare justice to Ihsan—grace, beauty, charity, and generosity.\n"
        "- Commanded to support and honor relatives and vulnerable kinfolk (Ita'i dhi al-qurba).\n"
        "- Cultivating communal solidarity and compassionate welfare networks across generations."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("43. Universal Prohibition: Shamelessness, Evil & Tyranny", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Strictly forbidding Al-Fahsha' (sexual indecency and vulgarity in private and public).\n"
        "- Prohibiting Al-Munkar (all universally recognized evil, corruption, and moral decay).\n"
        "- Banning Al-Baghy (tyrannical overreach, political brutality, and arrogance over fellow humans)."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("44. Inviolable Sanctity of Oaths & Solemn Covenants", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Fulfill the covenant of Allah whenever you take a solemn pledge; never break oaths.\n"
        "- Invoking Allah as your guarantor makes contract violation a direct assault on divine honor.\n"
        "- Business ethics, diplomatic treaties, and personal promises must remain unbreakable."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 12
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 12: PARABLE OF THE UNRAVELING WEAVER & TAYYIBAH", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Naqadat Ghazlaha, Opportunism & Wholesome Life for Both Genders", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("45. Folly of the Weaver: Untwisting Spun Yarn (Naqadat)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The unforgettable metaphor: Do not be like the woman who spins strong thread,\n"
        "- Only to systematically unravel her own woven fabric into loose, useless fibers.\n"
        "- Warning against spiritual self-sabotage: building discipline only to dismantle it."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("46. Exploiting Treaties for Geopolitical Advantage", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Forbidding the cynical practice of weaponizing oaths to manipulate weaker tribes.\n"
        "- Breaking treaties because one faction becomes larger, richer, or more powerful.\n"
        "- International law grounded in absolute moral integrity rather than opportunism."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("47. Universal Golden Guarantee: Hayatan Tayyibah", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Whoever performs righteous deeds, whether male or female, while being a believer...'\n"
        "- 'We will surely grant them to live a pure, beautiful, wholesome life (Hayatan Tayyibah).'\n"
        "- Wholesome life is internal peace, content sufficiency, and serenity, distinct from wealth."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("48. Equal Spiritual Rank & Reward for Men and Women", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Absolute equality of moral and spiritual accountability: male and female rewarded identically.\n"
        "- Recompensed in the Hereafter according to the finest and highest of their earthly actions.\n"
        "- Eradicating all pre-Islamic tribal sexism; establishing universal spiritual dignity."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 7: RECITING UNDER SANCTUARY & THE REFUGE OF THE COERCED
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        7, 8,
        "RECITING UNDER SANCTUARY & THE REFUGE OF THE COERCED",
        "Pillars 13 & 14: Isti'adhah Protocol, Jibril's Descent & The Jurisprudence of Duress",
        "PLATE 07 : ISTI'ADHAH & IKRAH"
    )

    # Column 1: Pillar 13
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 13: SEEKING DIVINE REFUGE & ROOH AL-QUDUS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Isti'adhah Protocol, Satanic Impotence & Revelation in Truth", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("49. Protocol of Recitation: Seeking Refuge (Isti'adhah)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'When you recite the Qur'an, seek refuge in Allah from the outcast devil.'\n"
        "- Pre-recitation purification: shielding the heart from satanic distraction and doubt.\n"
        "- Approaching sacred scripture with conscious spiritual vigilance and pure humility."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("50. Absolute Impotence of Satan Over Sincere Believers", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Indeed, he possesses no authority whatsoever over those who believe and rely on God.'\n"
        "- Tawakkul (complete reliance on God) serves as an impenetrable metaphysical firewall.\n"
        "- Demonic whispers lose all efficacy against a heart fortified by monotheistic conviction."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("51. Realm of Demonic Sway: Voluntarily Chosen Allies", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Satanic dominion is confined strictly to those who willingly elect him as guide.\n"
        "- Seducing those who commit polytheism and surrender moral agency to demonic fashion.\n"
        "- Human culpability remains total: the damned freely chose their allegiance."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("52. Rooh al-Qudus (Jibril) Delivering Revelation in Truth", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Say: The Holy Spirit (Rooh al-Qudus / Jibril) has brought it down from your Lord in Truth.\n"
        "- Revealed to firmly anchor and stabilize the hearts of those who have attained faith.\n"
        "- Providing divine guidance, clarity, and glad tidings to all who submit to their Creator."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 14
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 14: ACCUSATIONS OF TUTELAGE & DURESS (IKRAH)", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Lisanun 'Arabiyy, Exonerating 'Ammar & The Peril of Apostasy", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("53. Absurd Accusation of Foreign Human Authorship", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Quraysh conspirators claiming: 'It is only a foreign human slave who teaches Muhammad!'\n"
        "- Attempting to explain away the incomparable literary and theological miracle.\n"
        "- The desperate rationalization of polytheistic elites confronting prophetic genius."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("54. Crystalline Arabic Tongue vs. Foreign Speech", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Devastating refutation: The language of the person they slander is foreign and crude.\n"
        "- 'While this Qur'an is in clear, crystalline, eloquent Arabic!' (Lisanun 'Arabiyyun mubeen).\n"
        "- The linguistic perfection impossible to originate from a non-native speaker."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("55. Sacred Exception: Coerced Soul at Peace in Faith", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Except one who is forced while his heart is content in faith (Mutma'innun bil-Eeman).'\n"
        "- Historical milestone: Exonerating companion 'Ammar ibn Yasir tortured by pagans.\n"
        "- Establishing the foundational jurisprudence of duress (Rukhsat al-Ikrah): protecting life."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("56. Wrath of God Upon Apostasy Driven by Worldly Love", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Those who freely open chests to disbelief out of preference for fleeting worldly luxury.\n"
        "- Sealing their hearing, vision, and hearts; descending into irreversible heedlessness.\n"
        "- The terrifying end of those who trade eternal salvation for temporary social approval."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 8: THE UNGRATEFUL CITY, MODEL IBRAHIM & THE CALL WITH WISDOM
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        8, 8,
        "THE UNGRATEFUL CITY, MODEL IBRAHIM & THE CALL WITH WISDOM",
        "Pillars 15 & 16: The Starved Metropolis, The Nation of Ibrahim & The Charter of Dawah",
        "PLATE 08 : WISDOM & MUHSINOON"
    )

    # Column 1: Pillar 15
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 15: PARABLE OF THE STARVED CITY & MODEL IBRAHIM", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Libas al-Joo'i wal-Khawf, Halal Diet & Ummatan Qanitan", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("57. Secure City Stricken with Hunger and Fear", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The allegorical city: initially peaceful, secure, with provision flowing from all sides.\n"
        "- It showed ingratitude for Allah's blessings, sinking into pride and transgression.\n"
        "- Retribution: Allah enveloped its people in the garments of famine and terror."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("58. Lawful, Wholesome Food (Halalan Tayyiba) & Gratitude", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'So eat of that which Allah has provided for you, lawful and good (Halalan Tayyiba).'\n"
        "- Giving continuous, practical thanks for divine sustenance; avoiding unlawful corruptions.\n"
        "- Forbidding the pagan practice of inventing arbitrary dietary taboos without authority."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("59. Ibrahim as an Ummah (Ummatan Qanitan): The Champion", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Indeed, Ibrahim was an Ummah (a whole nation)—devoutly obedient, inclining to truth.'\n"
        "- A single individual embodying the virtues, monotheistic courage, and conviction of a race.\n"
        "- Pure in his monotheism (Haneefan), refusing every form of polytheistic compromise."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("60. Ever Grateful for Divine Favors (Shakiran Li-An'umih)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The defining hallmark of Patriarch Ibrahim: deeply grateful for every divine favor.\n"
        "- Chosen and guided by Allah to the straight, unswerving path of righteousness.\n"
        "- Bestowed good in this world, and ranked among the highest righteous in the Hereafter."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 16
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 16: THE ART OF DAWAH: WISDOM, SPEECH & PATIENCE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Hikmah, Maw'izhah, Proportional Justice & Divine Company", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("61. Universal Charter of Dawah: Wisdom & Admonition", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Call to the way of your Lord with wisdom (Hikmah) and beautiful admonition.'\n"
        "- Adapting speech to audience capacity; addressing the intellect with proof and heart with beauty.\n"
        "- The eternal pedagogical charter for every Muslim educator, scholar, and communicator."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("62. Debating Opponents with Grace (Billatee Hiya Ahsan)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'And debate with them in the manner that is finest, gentlest, and most noble.'\n"
        "- Refusing insults, emotional aggression, and cheap rhetorical tricks in religious discourse.\n"
        "- Recognizing that guidance belongs solely to Allah; human duty is dignified presentation."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("63. Strict Proportional Justice & Superiority of Sabr", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'And if you punish, then punish with an equivalent of that with which you were harmed.'\n"
        "- Outlawing vindictive excess and blood feuds; setting strict boundaries of justice.\n"
        "- The higher spiritual summit: 'But if you endure with patience, it is surely better.'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("64. Divine Accompaniment with the Mindful (Al-Muhsinoon)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'And endure with patience, and your patience is not except through Allah.'\n"
        "- Do not grieve over detractors, nor be in distress on account of their conspiracies.\n"
        "- Sealing Surah An-Nahl: 'Indeed, Allah is with those who have Taqwa and Muhsinoon!'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    pdf.save(OUTPUT_PDF)
    print(f"[OK] Generated {OUTPUT_PDF}")

    # Generate previews
    cmd = ["pdftoppm", "-png", "-r", "150", OUTPUT_PDF, os.path.join(PREVIEWS_DIR, "nahl_page")]
    subprocess.run(cmd, check=True)
    print(f"[OK] Rendered preview images to {PREVIEWS_DIR}")

    # Copy to brain dir
    for i in range(1, 9):
        src_name = f"nahl_page-{i}.png" if os.path.exists(os.path.join(PREVIEWS_DIR, f"nahl_page-{i}.png")) else f"nahl_page-0{i}.png"
        src_path = os.path.join(PREVIEWS_DIR, src_name)
        dst_path = os.path.join(brain_dir, f"nahl_page-{i}.png")
        if os.path.exists(src_path):
            shutil.copyfile(src_path, dst_path)
            print(f"[OK] Copied {src_name} -> {dst_path}")

if __name__ == "__main__":
    build_nahl_pdf()
