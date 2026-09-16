#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Kahf Master Mindmap Vector PDF Generator
16:9 Landscape Widescreen (792 x 480 pt) • 8 Plates • 16 Pillars • 64 Cards
"""

import os
import sys
import subprocess
import shutil

sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
OUTPUT_PDF = os.path.join(BASE_DIR, "KAHF_MASTER_MINDMAP.pdf")
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

def build_kahf_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH AL-KAHF", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
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
    # PLATE 01: SCRIPTURE & REFUGE
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 8,
        "THE UNWARPED SCRIPTURE & THE REFUGE OF YOUTH",
        "Pillars 1 & 2: Incorruptible Revelation, Dajjal Defense, Pagan Tyranny & The Cave Sanctuary",
        "PLATE 01 : SCRIPTURE & REFUGE"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 01: THE INCORRUPTIBLE SCRIPTURE (AL-KITAB)", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Uncrooked Revelation, Dajjal Shield & The Adornment of Earth", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 1, "The Upright Revelation (Qayyiman)",
              "Negating all internal crookedness ('Iwaj) and affirming sovereign rectifying authority (Qayyim) to guide, balance, and reform human civilizations across all eras.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 2, "The Shield Against the Dajjal",
              "Memorizing the opening and closing verses grants spiritual and intellectual immunity against the supreme tribulations, illusions, and deceptions of the end times.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 3, "Terrestrial Adornment as a Trial",
              "Worldly luxuries, flora, architecture, and technology are temporary ornaments designed solely to test which human beings remain most morally upright in conduct.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 4, "The Barren Dust Destination (Juruza)",
              "Reminding human ambition that earth's lush greenery and magnificent monuments will ultimately be leveled into sterile, dry dust before the eternal Reckoning.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 02: THE YOUTH OF FAITH IN SANCTUARY", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Standing Before Tyrants, The Bound Hearts & The Prayer for Mercy", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 5, "The Young Believers (Fityatun Amanoo)",
              "Sincere youth rising against Roman imperial polytheism, illustrating that pure, uncompromised hearts embrace truth long before socially entrenched elders.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 6, "Binding the Heart (Rabatna 'ala Quloob)",
              "Divine grace fortifying emotional resolve, empowering youth to boldly declare pure Tawhid before sovereign state tyranny without terror or hesitation.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 7, "The Supplication of Exile (Min Ladunka)",
              "Fleeing with zero material backups, begging Allah for all-encompassing mercy and righteous guidance to rectify their desperate circumstances in exile.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 8, "The Sanctuary of the Cave (Fa'woo)",
              "Choosing cold stone cavern over gilded royal courts, trusting that God's expansive mercy will spread within physical constriction to shield their faith.")

    # ==========================================
    # PLATE 02: SLUMBER & AWAKENING
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 8,
        "CELESTIAL SLUMBER & THE AWAKENING IN TIME",
        "Pillars 3 & 4: 309-Year Solar Mechanics, Somatic Turning, The Pure Meal & The Rule of In Sha' Allah",
        "PLATE 02 : SLUMBER & AWAKENING"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 03: CELESTIAL MECHANICS OF PRESERVATION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Astronomical Sunlight, Biological Turning & The Faithful Dog", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 9, "Trajectory of Sunlight (Tazawaru)",
              "The northern cave opening shielding them from direct solar ultraviolet rays, preserving their biological tissues and garments across three centuries.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 10, "Somatic Turning (Nuqallibuhum)",
              "Alternating physical posture between right and left sides to prevent circulatory thrombosis, pressure ulcers, and tissue necrosis over 309 years.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 11, "The Guard Dog at the Threshold (Waseed)",
              "The faithful dog stretching its paws at the cave entrance; keeping company with the righteous elevates even an animal to immortal mention in scripture.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 12, "The Shield of Terrifying Awe",
              "An intimidating divine aura enveloping their slumbering forms, preventing discovery or desecration by turning away intruders in terror.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 04: THE AWAKENING & DIVINE ETIQUETTES", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("The Coin Transaction, Halal Sustenance & The Mandatory In Sha' Allah", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 13, "The Disputed Duration (Kam Labithtum)",
              "Awakening after three centuries perceiving only a single day or part of a day, illustrating the psychological relativity of human temporal perception.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 14, "Seeking Pure Sustenance (Azka Ta'ama)",
              "Prioritizing food that is lawful and uncontaminated by pagan rituals, maintaining acute spiritual and dietary vigilance even in displacement.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 15, "Prudent Subtlety (Wa L-Yatalattaf)",
              "Directing the envoy to exercise extreme tactical caution, prudence, and diplomacy to safeguard the vulnerable community from detection.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 16, "The Etiquette of In Sha' Allah",
              "Forbidding absolute assertions about future actions without adding 'If Allah wills'; human agency is entirely subordinate to transcendent decree.")

    # ==========================================
    # PLATE 03: TWO GARDENS & WEALTH
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 8,
        "THE PARABLE OF TWO GARDENS & VANITY OF WEALTH",
        "Pillars 5 & 6: The Hubris of Capital, The Faithful Dialectic, Hand-Wringing Regret & Al-Baqiyat",
        "PLATE 03 : TWO GARDENS & WEALTH"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 05: THE ARROGANCE OF ABUNDANCE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Lush Vineyards, Delusion of Permanence & The Believing Counter", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 17, "The Opulent Agricultural Estate",
              "Two thriving vineyards ringed by date palms, interspersed with green crops and bisected by a flowing river, yielding full harvests without defect.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 18, "Capitalistic Arrogance (Ana Aktharu)",
              "Boasting over his poorer companion: 'I am greater than you in wealth and more eminent in followers,' deifying material assets as status weapons.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 19, "The Delusion of Permanence",
              "Entering his orchard wronging his soul, claiming: 'I do not think this will ever perish, nor that the Day of Resurrection will ever occur.'")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 20, "The Believing Admonition",
              "The impoverished companion challenging his hubris: 'Do you disbelieve in Him who created you from dust, then fashioned you into a man?'")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 06: RUIN OF TRELLISES & ENDURING DEEDS", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("The Spiritual Vaccine (Ma Sha' Allah), Tempest Ruin & Al-Baqiyat as-Salihat", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 21, "The Vaccine of Gratitude (Ma Sha' Allah)",
              "Directing the wealthy to utter: 'What Allah wills; there is no power except through Allah,' neutralizing vanity and attributing equity to the Provider.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 22, "The Sudden Cosmic Tempest (Husban)",
              "A nocturnal disaster devastating the orchards, collapsing vine trellises into ruins and sinking groundwater beyond human retrieval.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 23, "Hand-Wringing Regret (Yuqallibu Kaffayhi)",
              "Waking to wring empty hands in bitter agony over spent investments, crying: 'I wish I had not associated anyone with my Lord!'")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 24, "The Enduring Equity (Al-Baqiyat as-Salihat)",
              "Worldly wealth and offspring are temporary ornaments; enduring righteous deeds yield everlasting reward and superior hope before your Lord.")

    # ==========================================
    # PLATE 04: RECORD & IBLIS
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 8,
        "THE BARREN EARTH, UNVEILED RECORD & REBELLIOUS JINN",
        "Pillars 7 & 8: Leveling of Mountains, Photographic Ledger, Iblis's Transgression & Human Argument",
        "PLATE 04 : RECORD & IBLIS"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 07: COSMIC RECKONING & THE OPEN RECORD", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("The Exposed Earth, Universal Ranks & The Infallible Ledger", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 25, "The Barren Earth (Bareezah)",
              "The Day mountains are uprooted into dust and the earth is exposed flat, stripped of all human monuments and civilizational fortresses.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 26, "Mankind Arrayed in Ranks (Saffa)",
              "All humanity assembled before the Divine Throne: 'You have come to Us just as We created you the first time, without wealth or allies.'")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 27, "The Photographic Ledger (Ma Li-Hadhal-Kitab)",
              "Sinners terrified as the scroll unfolds, crying: 'Woe to us! What a book this is, omitting neither small nor great deed without registering it!'")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 28, "Absolute Equity (La Yazlimu Ahada)",
              "Every choice, transaction, and secret deed presented with flawless precision; your Lord wrongs no single soul in the supreme court of judgment.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 08: THE HOSTILITY OF IBLIS & INTELLECTUAL HUBRIS", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Jinn Origin, Refusal of Sujood, The Enemy as Ally & Chronic Argument", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 29, "The Jinn Origin (Kana Minal-Jinn)",
              "Clarifying that Iblis was from the jinn and openly rebelled against the divine command, refusing to prostrate to Adam out of fiery pride.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 30, "The Absurdity of Befriending the Foe",
              "Divine rebuke: 'Will you take him and his progeny as allies instead of Me, while they are your sworn enemies? Evil is the exchange for oppressors!'")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 31, "Exclusion from Cosmic Creation",
              "Satan possessed zero role in creating heavens, earth, or human souls; God never takes deceivers or misleaders as assistants in dominion.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 32, "Human Contentiousness (Jadala)",
              "God has varied every parable in the Qur'an for reflection, yet human pride remains the most contentious, argumentative entity in existence.")

    # ==========================================
    # PLATE 05: MUSA & AL-KHIDR
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        5, 8,
        "THE QUEST FOR KNOWLEDGE & THE PROPHETIC ENCOUNTER",
        "Pillars 9 & 10: Musa's Resolution, The Revived Fish, The Ladunni Servant & The Covenant of Patience",
        "PLATE 05 : MUSA & AL-KHIDR"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 09: THE EXPEDITION TO THE CONFLUENCE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Prophetic Resolve, Confluence of Seas & The Escaping Salted Fish", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 33, "Musa's Boundless Resolve (La Abrahu)",
              "Declaring he will march unceasingly until reaching the confluence of two seas, even if journeying for decades to acquire higher illumination.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 34, "The Confluence of the Seas (Majma' al-Bahrayn)",
              "The geographic and metaphysical junction where marine currents meet, divinely appointed as the station of instruction for the arch-prophet.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 35, "The Sign of the Revived Fish (Sarabah)",
              "The salted travel fish miraculously regaining life at the rock, tunneling through the sea as the divinely appointed marker of meeting.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 36, "Retracing Footsteps (Irtadda)",
              "Overcoming physical fatigue and hunger, turning back upon their exact footsteps to locate the forgotten station of divine grace and knowledge.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 10: THE LADUNNI SERVANT & COVENANT OF PATIENCE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Endowment of Mercy, Transcendent Knowledge & The Strict Pact", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 37, "The Ladunni Servant (Rahmatan & 'Ilma)",
              "Meeting Al-Khidr: an illuminated worshipper endowed with special divine mercy and knowledge operating beyond mortal causal horizons.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 38, "Musa's Student Humility (Hal Attabi'uka)",
              "Despite being Kalimullah, Musa asks permission to follow as a humble student to learn righteous conduct with total deference.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 39, "The Challenge of Patience (Lan Tastatee'a)",
              "Khidr's warning: 'You will never be able to maintain patience with me; how can you endure that which you do not encompass in knowledge?'")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 40, "The Strict Pedagogical Condition",
              "Khidr's terms: 'If you follow me, ask me nothing about any occurrence until I initiate explanation to you,' testing impulse control.")

    # ==========================================
    # PLATE 06: THREE PARADOXES
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        6, 8,
        "THE THREE EPISTEMOLOGICAL PARADOXES UNVEILED",
        "Pillars 11 & 12: The Damaged Vessel, Slaying the Boy, Rebuilding the Wall & Transcendent Wisdom",
        "PLATE 06 : THREE PARADOXES"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 11: THE DAMAGED SHIP & THE SLAIN YOUTH", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Pulling the Plank, Slaying the Boy & Musa's Immediate Protests", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 41, "The Deliberate Flaw (Kharaqaha)",
              "Khidr breaches the hull of a vessel that offered free passage, provoking Musa's immediate outrage at apparent catastrophic ingratitude.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 42, "The Tyrant King of Confiscation (Ghasba)",
              "Hidden reality unveiled: impoverished fishermen protected from an encroaching tyrant king who seized every sound vessel by force.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 43, "Slaying of the Youth (Qatala Ghulam)",
              "Slaying an innocent boy without legal provocation, inciting Musa's horror at taking an unretaliated soul without judicial due process.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 44, "Mercy for Pious Parents",
              "Hidden reality unveiled: the youth destined to torment his devout parents with rebellion and disbelief; replaced with a purer child.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 12: THE COLLAPSING WALL & ULTIMATE HUMILITY", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("The Inhospitable Village, The Righteous Father & Disavowal of Egotism", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 45, "The Rebuilt Wall (Aqamahu)",
              "Repairing a crumbling wall in an inhospitable town that denied them food, prompting Musa to suggest taking wages to buy sustenance.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 46, "Treasure of the Two Orphans",
              "Hidden reality unveiled: beneath the wall lay gold for two orphan boys, safeguarded by God because their late father was a righteous man.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 47, "The Canopy of Parental Righteousness",
              "Demonstrating that a parent's private devotion to God establishes an enduring protective spiritual canopy over descendants across generations.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 48, "Disavowal of Autonomous Will (Ma Fa'altuhu)",
              "Khidr concludes with consummate humility: 'I did not do it of my own accord; this is the explanation of what you could not bear.'")

    # ==========================================
    # PLATE 07: DHUL-QARNAYN & IRON
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        7, 8,
        "SOVEREIGNTY OF DHUL-QARNAYN & THE IRON RAMPART",
        "Pillars 13 & 14: Expeditions East and West, Refusing Tribute, Collaborative Metallurgy & Gog/Magog",
        "PLATE 07 : DHUL-QARNAYN & IRON"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 13: THE EXPEDITIONS OF THE JUST MONARCH", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Universal Dominion, Setting Sun Spring & Nomads of the Rising Sun", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 49, "Empowerment with Means (Sababa)",
              "Granted legitimate imperial authority, advanced engineering logistics, and material means to traverse continents with equity.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 50, "The Setting Sun Expedition (Maghrib)",
              "Journeying to the western oceanic horizon, observing the sun setting in a dark spring, governing diverse peoples with justice and mercy.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 51, "The Rising Sun Expedition (Matli')",
              "Encountering vulnerable populations with no technological sheltering from the sun, treating them with civil dignity without cultural erasure.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 52, "The Mountain Pass (Bayna as-Saddayn)",
              "Arriving between two natural mountain ramparts, meeting an isolated people terrorized by the rapacious marauders of Gog and Magog.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 14: THE METALLURGICAL BARRIER & TOTAL HUMILITY", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Rejecting Tribute, Stacking Iron Blocks, Molten Copper & Dissolution in the Hour", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 53, "Rejecting Financial Tribute (Kharjan)",
              "Refusing monetary bribery: 'That in which my Lord has established me is superior,' rejecting imperial extortion of impoverished peoples.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 54, "Organizing Human Labor (Fa-A'eenoonee)",
              "Mobilizing the populace: 'Help me with strength/labor,' fostering collective societal agency rather than passive welfare dependency.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 55, "The Iron & Molten Copper Rampart (Qitr)",
              "Stacking iron blocks between cliffs, blowing bellows until glowing, and pouring molten copper to create an unscalable alloy wall.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 56, "Sovereign Humility (Rahmatun Min Rabbi)",
              "Standing before the monumental rampart: 'This is a mercy from my Lord; when His promise comes, it will be leveled to dust.'")

    # ==========================================
    # PLATE 08: ULTIMATE LOSERS & TAWHID
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        8, 8,
        "THE GREATEST LOSERS, OCEAN OF WORDS & TAWHID",
        "Pillars 15 & 16: The Delusion of Sincerity, Hospitality of Firdaus, Ocean of Ink & The Pure Manifesto",
        "PLATE 08 : ULTIMATE LOSERS & TAWHID"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 15: THE SUPREME LOSERS & THE GARDENS OF FIRDAUS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Tragic Delusion of Sincerity, Zero Weight in Scales & Eternal Hospitality", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 57, "The Ultimate Losers (Al-Akhsareen)",
              "Warning of those whose worldly efforts are completely wasted, yet live under the tragic delusion that they are doing exemplary work.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 58, "Zero Weight in Scales (Fala Nuqeemu)",
              "Having rejected divine signs and the Meeting, their accumulated worldly titles and assets carry zero gravitational mass in the divine scales.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 59, "Lodging of Firdaus (Jannatul-Firdaws)",
              "Believers who act righteously inherit the highest gardens of Paradise as an eternal hospitality lodging prepared by the King of kings.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 60, "Perpetual Contentment (La Yabghoona)",
              "Dwelling eternally within sublime divine bliss, possessing zero desire for relocation, change, or alternative station forever.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 16: THE INEXHAUSTIBLE WORDS & THE FINAL MANIFESTO", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("The Ocean of Ink, Prophetic Humanity & The Dual Pillars of Salvation", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 61, "The Ocean as Ink (Law Kanal-Bahru)",
              "Were the oceans ink to transcribe the sciences and decrees of God, the oceans would deplete before His words run dry.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 62, "Boundless Transcendent Knowledge",
              "Even if reinforced with an ocean of equal magnitude, human and created comprehension can never exhaust transcendent divine wisdom.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 63, "Prophetic Humanity (Innama Ana Bashar)",
              "Prophet Muhammad declares his mortal humanity: a human messenger chosen to receive singular divine revelation of pure Tawhid.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 64, "The Final Equation of Salvation",
              "'Whoever hopes to meet his Lord: let him perform righteous deeds according to the Sunnah, and associate none in worship with his Lord.'")

    pdf.save(OUTPUT_PDF)
    print(f"Generated Vector PDF at: {OUTPUT_PDF}")

    # Generate PNG Previews
    cmd = f"pdftoppm -png -r 150 {OUTPUT_PDF} {PREVIEWS_DIR}/kahf_page"
    subprocess.run(cmd, shell=True, check=True)
    print(f"Rendered PNG previews in: {PREVIEWS_DIR}")

    # Copy to brain dir
    for i in range(1, 9):
        src_prev = f"{PREVIEWS_DIR}/kahf_page-{i}.png"
        dst_brain = os.path.join(brain_dir, f"kahf_page-{i}.png")
        if os.path.exists(src_prev):
            shutil.copyfile(src_prev, dst_brain)
            print(f"Copied {src_prev} to {dst_brain}")

if __name__ == "__main__":
    build_kahf_pdf()
