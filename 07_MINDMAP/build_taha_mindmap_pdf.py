#!/usr/bin/env python3
"""
Huurs Studio - Surah Ta-Ha Master Mindmap Vector PDF Generator
16:9 Landscape Widescreen (792 x 480 pt) • 8 Plates • 16 Pillars • 64 Cards
"""

import os
import sys
import subprocess
import shutil

sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
OUTPUT_PDF = os.path.join(BASE_DIR, "TAHA_MASTER_MINDMAP.pdf")
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

def build_taha_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH TA-HA", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
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
    # PLATE 01: REVELATION & TUWA
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 8,
        "THE SOLACE OF REVELATION & THE SACRED FIRE OF TUWA",
        "Pillars 1 & 2: The Antidote to Distress, Ar-Rahman's Throne, Sinai Wilderness & Removal of Sandals",
        "PLATE 01 : REVELATION & TUWA"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 01: THE SOLACE OF REVELATION & MAJESTY", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Ma Anzalna 'Alayka al-Qur'ana Li-Tashqa, Tadhkirah & Istawa", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 1, "The Refutation of Misery (Li-Tashqa)",
              "Divine declaration that revelation was never sent to induce crushing distress, but to bring solace, spiritual equilibrium, and peace.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 2, "Reminder for the God-Fearing (Tadhkirah)",
              "Revelation operates as an awakening reminder for hearts open to reverence, illuminating the primordial covenant imprinted upon the fitrah.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 3, "Sovereign Ascension (Istawa)",
              "Ar-Rahman's majestic ascension upon the Throne, governing all realms between the heavens, the earth, and the depths of the soil.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 4, "Knowledge of the Whispered Secret",
              "Divine omniscience encompassing spoken words, hidden thoughts, and innermost secrets, revealing that nothing escapes the Creator.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 02: THE EPIPHANY AT SACRED TUWA", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("The Desert Fire, Voice of the Lord, Removing Sandals & Prayer", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 5, "The Desert Fire (Anastu Naran)",
              "Musa perceiving fire in the freezing Sinai wilderness, seeking an ember for his family or wayfaring guidance, leading to prophethood.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 6, "The Call in the Holy Valley (Tuwa)",
              "The voice of the Lord addressing Musa directly in the sanctified valley, inaugurating his prophetic covenant with the Almighty.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 7, "Removing the Sandals (Ikhla' Na'layk)",
              "Commandment to shed footwear in deep humility and tactile reverence before stepping upon sanctified prophetic soil.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 8, "Prayer for Remembrance (Li-Dhikri)",
              "The prime directive of worship: establishing ritual prayer as the definitive cognitive anchor of divine mindfulness amidst mortality.")

    # ==========================================
    # PLATE 02: SIGNS & EXPANSIVENESS
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 8,
        "THE CELESTIAL SIGNS & THE DU'A OF EXPANSIVENESS",
        "Pillars 3 & 4: Staff Serpent, Radiant White Hand, Sharh as-Sadr & Harun's Prophetic Partnership",
        "PLATE 02 : SIGNS & EXPANSIVENESS"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 03: THE TWO CELESTIAL PROPHETIC SIGNS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Transformation of the Staff, Living Serpent & The Luminous Hand", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 9, "The Shepherd's Staff Transformed",
              "Musa's ordinary shepherd's tool transformed into an active slithering serpent, demonstrating sovereign divine mastery over physical matter.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 10, "Seizing Without Fear (Khudh-ha)",
              "Divine command to seize the serpent with bare hands without terror, instantly restoring the staff to its original wooden form.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 11, "The Radiant White Hand (Bayda')",
              "Drawing the hand from the armpit radiating dazzling white light without illness or blemish, a second celestial credential.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 12, "Commission to Face Tyranny (Tagha)",
              "Divine charge to march directly to Pharaoh, the imperial oppressor who crossed all moral bounds, armed with celestial signs.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 04: THE DU'A OF PSYCHOLOGICAL EXPANSIVENESS", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Sharh as-Sadr, Eased Mission, Untied Tongue & Fraternal Alliance", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 13, "Expansion of the Chest (Sharh as-Sadr)",
              "Musa praying for an expanded emotional vessel capable of absorbing mockery, hostility, and tyrannical threats without malice.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 14, "Facilitation of the Task (Yassir Li Amri)",
              "Acknowledging that the most intimidating geopolitical missions require transcendent ease bestowed directly by the Creator.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 15, "Untying the Tongue (Uqdatan min Lisani)",
              "Praying for functional communicative clarity so adversaries can truly understand the message, devoid of rhetorical vanity.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 16, "Fraternal Alliance with Harun",
              "Requesting Harun as co-prophet and partner to share prophetic weight, multiplying communal glorification and collective remembrance.")

    # ==========================================
    # PLATE 03: PROVIDENCE & DESTINY
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 8,
        "DIVINE PROVIDENCE & THE TAPESTRY OF DESTINY",
        "Pillars 5 & 6: The River Chest, Sister's Vigil, Madyan Exile & Arriving upon Divine Schedule",
        "PLATE 03 : PROVIDENCE & DESTINY"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 05: INFANT SURVIVAL & PALACE EMBRACE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("The Floating Taboot, Divine Love & The Watchful Sister", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 17, "The Floating River Chest (At-Taboot)",
              "Casting newborn Musa into the Nile, shielded under divine surveillance and guided into the palace of his murderous enemy.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 18, "The Endowment of Divine Love (Mahabbah)",
              "Allah casting His personal love upon Musa, making him an irresistible infant whom even Pharaoh's wife could not bear to harm.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 19, "The Sister's Stealth Vigil",
              "Musa's sister shadowing the floating chest from afar, stepping forward to recommend his biological mother as wet nurse.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 20, "The Maternal Reunion",
              "Fulfilling the divine promise to return the baby to his mother's arms, comforting her grieving heart and banishing sorrow.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 06: EXILE, REFINEMENT & DECREED ARRIVAL", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Trial of Slaying Egyptian, Years in Madyan & Ji'ta 'Ala Qadarin", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 21, "The Crucible of Testing (Futoon)",
              "Musa tested through unintentional manslaughter, fear, and exile, purifying his character for future leadership.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 22, "Shepherding in Madyan",
              "Ten years of quiet labor as a shepherd in Madyan, learning patience, humility, and crisis management in solitude.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 23, "Arriving on Decreed Schedule (Qadar)",
              "Sinai arrival orchestrated with cosmic precision; every preceding tribulation served as an intentional preparatory curriculum.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 24, "Fashioned for Divine Service (Wastana'tuka)",
              "The sublime declaration: 'I have fashioned you for Myself,' establishing prophetic election as total dedication to God.")

    # ==========================================
    # PLATE 04: DIALECTIC & MILDNESS
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 8,
        "THE DIALECTIC BEFORE PHARAOH & GENTLE SPEECH",
        "Pillars 7 & 8: Qawlan Layyina, Divine Accompaniment, Teleological Definition & Historical Record",
        "PLATE 04 : DIALECTIC & MILDNESS"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 07: THE ETHICS OF GENTLE ADVOCACY", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Qawlan Layyina, Divine Accompaniment & Dispelling Fear", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 25, "The Mandate of Mild Speech (Qawlan Layyina)",
              "Commanded to address an arrogant child-killer with gentle words, illustrating that dawah must always prioritize dignity.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 26, "Transcendent Accompaniment (Asma'u wa Ara)",
              "Divine reassurance to trembling prophets: 'I am with you both; I hear and I see,' shattering the illusion of human power.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 27, "Confronting the Imperial Court",
              "Standing unarmed before the Egyptian throne, demanding the liberation of the Children of Israel from systemic enslavement.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 28, "Peace upon the Guided",
              "Proclaiming that true peace rests upon those who follow guidance, while ruin awaits those who deny truth and turn away.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 08: THE TELEOLOGICAL DEFINITION OF GOD", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("A'ta Kulla Shay'in Khalqahu, Guidance & The Infallible Record", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 29, "The Supreme Definition of God",
              "Our Lord is He who gave every single entity its created form and then guided it, articulating universal design and purpose.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 30, "Pharaoh's Deflection: Former Nations",
              "Pharaoh evading theological debate by questioning the fate of ancient ancestors; Musa grounding judgment in divine knowledge.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 31, "The Infallible Record (La Yadillu)",
              "Musa declaring that knowledge of past generations is preserved in an unerring book; my Lord neither errs nor forgets.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 32, "The Earth as a Cradle (Mahda)",
              "Reminding humanity of the terrestrial cradle, sky-sent rain, diverse botanical species, and the cyclical return to dust.")

    # ==========================================
    # PLATE 05: CONTEST & PROSTRATION
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        5, 8,
        "THE CONTEST OF ILLUSION & TRIUMPH OF TRUTH",
        "Pillars 9 & 10: Yawm al-Zeenah, Ropes and Staffs, Staff Swallowing & The Sorcerers' Martyrdom",
        "PLATE 05 : CONTEST & PROSTRATION"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 09: THE FESTIVAL DAY & SENSORY ILLUSION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Yawm al-Zeenah, Slithering Ropes & Musa's Inner Tremor", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 33, "The Midday Festival (Yawm al-Zeenah)",
              "Choosing public confrontation at broad daylight on the annual holiday, ensuring thousands of independent eyewitnesses.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 34, "Warning Against Fabrication",
              "Musa cautioning the gathered sorcerers not to invent lies against God lest a sudden divine punishment eradicate them.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 35, "The Optical Illusion of Magic",
              "Sorcerers casting ropes and staffs with mercury, deceiving human eyes into perceiving terrifying slithering serpents.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 36, "Inner Apprehension & Reassurance",
              "Musa experiencing a fleeting tremor of human hesitation; Allah commanding: 'Fear not, indeed you are the superior.'")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 10: THE SWALLOWING STAFF & MARTYR'S DEFIANCE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Talqaf Ma Sana'oo, Prostration in Faith & Defying Crucifixion", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 37, "The Devouring Staff (Talqaf)",
              "Musa casting his staff which physically devours all fraudulent illusions, proving that divine truth destroys artifice.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 38, "Instantaneous Prostration (Sujjadan)",
              "Recognizing divine reality, the elite magicians immediately fall in prostration, professing faith in the Lord of Aaron and Moses.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 39, "Pharaoh's Raging Tyranny",
              "Pharaoh accusing them of conspiracy, threatening cross-amputation and public crucifixion upon the trunks of palm trees.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 40, "The Victory of Transcendent Faith",
              "The converted sorcerers defying the emperor: 'You can only decree for this worldly life; we seek the forgiveness of our Lord.'")

    # ==========================================
    # PLATE 06: EXODUS & GOLDEN CALF
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        6, 8,
        "THE RED SEA HIGHWAY & THE GOLDEN CALF",
        "Pillars 11 & 12: Dry Sea Highway, Pharaoh's Drowning, Samiri's Golden Calf & Harun's Plea",
        "PLATE 06 : EXODUS & GOLDEN CALF"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 11: THE DRY HIGHWAY THROUGH THE SEA", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Nocturnal Exodus, Tariqan fil-Bahri Yabasa & Engulfing Sea", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 41, "The Nocturnal Exodus",
              "Commanded to lead the Children of Israel out of Egypt by night, relying entirely upon divine navigational protection.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 42, "The Dry Path (Tariqan Yabasa)",
              "Striking the ocean to forge a firm, dry highway through the sea without fear of capture or drowning.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 43, "Engulfed by the Ocean (Fa-Ghashiyahum)",
              "Pharaoh and his arrogant hosts surging into the divided waters, engulfed completely by the returning sea.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 44, "Delivering Israel from Bondage",
              "Fulfilling the historic liberation of an enslaved nation, providing manna and quails across the wilderness.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 12: SAMIRI'S BETRAYAL & THE GOLDEN IDOL", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("The Lowing Calf, Stolen Jewelry, Exploited Weakness & Calf Worship", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 45, "Musa Hurrying to Sinai",
              "Musa rushing to the mountain appointment ahead of his people: 'I hastened to You, my Lord, that You might be pleased.'")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 46, "Samiri's Counterfeit Calf (Khuwar)",
              "As-Samiri casting melted jewelry into a hollow golden bovine, producing an eerie lowing whistle in the desert wind.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 47, "The Trap of Regressive Idolatry",
              "Exploiting newly liberated slaves' lingering affinity for Egyptian cattle-worship, deifying the lifeless metal statue.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 48, "Harun's Restraint & Community Unity",
              "Harun warning against the idolatrous trap, exercising political patience to prevent bloody civil war before Musa's return.")

    # ==========================================
    # PLATE 07: INDIGNATION & ANNIHILATION
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        7, 8,
        "INDIGNATION, ANNIHILATION & SAMIRI'S EXILE",
        "Pillars 13 & 14: Musa's Burning Wrath, Ya Ibna Umma, Pulverizing the Idol & La Misas",
        "PLATE 07 : INDIGNATION & ANNIHILATION"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 13: THE BURNING INDIGNATION OF MUSA", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Dropping the Tablets, Seizing the Beard & Fraternal Reconciliation", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 49, "Returning in Grief and Anger",
              "Musa descending from Sinai in profound sorrow and holy rage, shattering the stone tablets upon witnessing the apostasy.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 50, "Confronting Harun (Ya Ibna Umma)",
              "Seizing Harun's beard and hair; Harun de-escalating with filial affection: 'O son of my mother, do not seize my beard.'")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 51, "Preserving Communal Cohesion",
              "Harun explaining his agonizing decision: avoiding premature tribal slaughter that would irrevocably fracture Israel.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 52, "Fraternal Forgiveness & Prayer",
              "Musa recognizing his brother's innocence, releasing his anger, and praying for divine forgiveness for them both.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 14: SAMIRI'S CONDEMNATION & IDOL ANNIHILATION", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("The Handful of Dust, Burning the Idol, Scattering at Sea & La Misas", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 53, "Samiri's Arrogant Confession",
              "Samiri admitting grabbing a handful of dust from the messenger's footprint, seduced by his own distorted ego.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 54, "The Sentence of Isolation (La Misas)",
              "Musa exiling Samiri with a lifelong physical and psychological affliction: crying 'Touch me not' in total ostracization.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 55, "Pulverizing the Golden Calf",
              "Incinerating the golden idol, grinding it into fine particulate dust, and scattering it into the ocean currents.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 56, "Absolute Monotheism Reclaimed",
              "Proclaiming that true divinity belongs solely to Allah, whose infinite knowledge encompasses all created things.")

    # ==========================================
    # PLATE 08: RESURRECTION & ADAM
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        8, 8,
        "THE BLIND RESURRECTION & ADAM'S COVENANT",
        "Pillars 15 & 16: Flattened Earth, Ma'eeshatan Danka, Adam's Forgetfulness & Universal Guarantee",
        "PLATE 08 : RESURRECTION & ADAM"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 15: THE LEVELED EARTH & THE BLIND RETURN", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Qa'an Safsafa, Constricted Living & Resurrected in Blindness", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 57, "The Leveling of the Mountains",
              "Cosmic shattering on the Last Day, pulverizing mountains into smooth, level plains without hills or depressions.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 58, "Voices Humbled Before Ar-Rahman",
              "Absolute silence enveloping the assembly of resurrected humanity; no sound heard except the faint rustling of footsteps.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 59, "The Constricted Life (Ma'eeshatan Danka)",
              "Whoever turns away from divine remembrance suffocates in anxiety, fear, and internal existential misery.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 60, "The Blind Resurrection (A'ma)",
              "Waking on Judgment Day physically blind; divine retribution for having lived spiritually blind to God's signs.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 16: ADAM'S COVENANT & THE DIVINE GUARANTEE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Lapse of Vigilance, Satanic Whispers, Repentance & Fa-La Tashqa", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 61, "Adam's Forgetfulness (Fa-Nasiya)",
              "Human vulnerability contextualized: Adam forgot the covenant without malice, succumbing to a temporary lapse of resolve.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 62, "The Deception of False Eternity",
              "Satan enticing humanity with the illusion of unending worldly power through the forbidden tree.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 63, "Repentance & Divine Election",
              "Adam weeping in contrition; Allah choosing him, forgiving his lapse, and guiding his posterity.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 64, "The Universal Divine Shield",
              "Whoever follows divine guidance will never go astray in this world nor suffer misery in the next: Fa-la yadillu wa la yashqa.")

    pdf.save(OUTPUT_PDF)
    print(f"Master Mindmap PDF successfully compiled at: {OUTPUT_PDF}")

    # Generate Previews
    cmd = f"pdftoppm -png -r 150 {OUTPUT_PDF} {PREVIEWS_DIR}/taha_page"
    subprocess.run(cmd, shell=True, check=True)
    print("PNG Previews rendered in previews directory.")

    # Copy to brain dir
    for i in range(1, 9):
        src = f"{PREVIEWS_DIR}/taha_page-{i}.png"
        dst = os.path.join(brain_dir, f"taha_page-{i}.png")
        if os.path.exists(src):
            shutil.copyfile(src, dst)
    print("PNG Previews successfully copied to brain directory.")

if __name__ == "__main__":
    build_taha_pdf()
