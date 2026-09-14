#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Qasas Master Mindmap Vector PDF Generator
16:9 Landscape Widescreen (792 x 480 pt) • 8 Plates • 16 Pillars • 64 Cards
Strict Brand_Visual_System.md & Absolute Copyright Insulation
"""

import os
import sys
import subprocess
import shutil

sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
OUTPUT_PDF = os.path.join(BASE_DIR, "AL_QASAS_MASTER_MINDMAP.pdf")
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

def build_al_qasas_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH AL-QASAS", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
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
    # PLATE 01: THE DIVINE DECREE & THE NILE BASKET
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 8,
        "THE DIVINE DECREE & THE NILE BASKET",
        "Pillars 1 & 2: Subversion of Imperial Tyranny, The Oppressed Vanguard & Asiyah's Sanctuary",
        "PLATE 01 : THE RIVER OF FAITH"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 01: THE OPPRESSED VANGUARD", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Ta-Seen-Meem, Caste Fracturing & The Sovereign Decree", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 1, "The Clear Book (Ta-Seen-Meem)",
              "The illuminated verses of the manifest Book reciting the epic chronicle of Musa and Pharaoh in pristine truth for believers.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 2, "Imperial Caste Division (Shiya'an)",
              "Pharaoh exalted himself in the land, fracturing society into disenfranchised factions, slaughtering newborn sons and subjugating women.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 3, "The Sovereign Will (Wa Nureedu)",
              "Divine determination to confer favor upon the oppressed, subverting worldly tyrannies and turning the marginalized into leaders.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 4, "Inheritors of the Earth (Al-Waritheen)",
              "Establishing the humble upon the earth while confronting Pharaoh, Haman, and their armies with the very destruction they feared.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 02: THE RIVER & THE PALACE SANCTUARY", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Divine Inspiration, The Nile Ark & The Queen's Intercession", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c2_y if 'c2_y' in locals() else c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 5, "Inspiration to the Mother (Ilham)",
              "Commanded to nurse her infant, then cast him into the rushing river without fear or sorrow, armed with the divine covenant of return.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 6, "The Floating Ark of Deliverance",
              "Surrendering maternal anxiety to divine providence; the chest drifts safely past imperial patrols into Pharaoh's private garden moat.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 7, "Asiyah's Sanctuary (Qurratu 'Ayn)",
              "Pharaoh's noble queen pleads for the defenseless child: 'A comfort of the eye for me and you; do not slay him, perhaps he will benefit us.'")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 8, "Nurtured in the Tyrant's Lair",
              "Divine irony perfected: Pharaoh funds, guards, and clothes the very prophet ordained by Allah to dismantle his imperial throne.")

    # ==========================================
    # PLATE 02: MATERNAL AGONY & THE RESTORATION
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 8,
        "MATERNAL AGONY & THE DIVINE RESTORATION",
        "Pillars 3 & 4: The Emptied Heart Bound by God, The Oblique Observer & The Milk of Home",
        "PLATE 02 : THE BINDING OF HEARTS"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 03: THE EMPTIED HEART BOUND", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Maternal Trauma, Evacuated Heart & The Gift of Serenity", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 9, "The Evacuated Heart (Farighan)",
              "The heart of Musa's mother became completely emptied of all worldly awareness, drained by acute grief and agonizing separation.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 10, "Divine Binding of the Heart (Rabatna)",
              "On the verge of crying aloud, Allah tied firm bonds of faith and tranquility upon her heart to keep her among the steadfast believers.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 11, "The Anatomy of Divine Serenity",
              "Demonstrating that psychological fortitude in moments of sudden disruption is a supernatural gift granted through divine remembrance.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 12, "Faith Above Paralyzing Fear",
              "Her anchored heart trusts the unseen decree, overcoming raw instinctual terror to allow the sovereign plan of Allah to unfold.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 04: THE SISTER'S MISSION & RETURN", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Oblique Tracking, Wet-Nurse Aversion & The Fulfilled Vow", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 13, "The Oblique Scout (Qusseeh)",
              "The sister follows the basket from an oblique distance ('An Junubin), blending seamlessly into the public while guarding the secret.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 14, "Rejection of Wet-Nurses (Harramna)",
              "Allah instills an instinctual aversion in the infant's palate against all royal wet-nurses, rendering palace physicians helpless.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 15, "Diplomatic Discretion at Court",
              "The sister steps forward proposing a noble household to nurture the weeping child, speaking with masterly tactical reserve.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 16, "The Restored Bosom & True Promise",
              "Restored to his mother that her eyes find solace and know that Allah's promise is inviolable truth, though most humans perceive not.")

    # ==========================================
    # PLATE 03: CRISIS IN EGYPT & DESERT FLIGHT
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 8,
        "THE CRISIS IN EGYPT & THE DESERT FLIGHT",
        "Pillars 5 & 6: Attaining Maturity, The Accidental Blow, Conscience of Tawbah & The Sincere Warner",
        "PLATE 03 : THE FUGITIVE'S EXILE"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 05: MATURITY & THE MORAL VOW", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Equilibrium, The Fatal Strike & Instant Repentance", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 17, "Full Stature & Wisdom (Istawa)",
              "Reaching physical zenith and intellectual equilibrium, Musa is endowed with divine judgment, knowledge, and prophetic virtue.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 18, "The Unintended Fatal Blow (Wakaza)",
              "Intervening during midday rest to protect an oppressed Israelite, Musa strikes an abusive Egyptian overseer, killing him accidentally.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 19, "Instant Repentance Without Excuses",
              "Recognizing demonic anger, Musa offers no tribal rationalization, weeping: 'My Lord, I have wronged myself, so forgive me!'")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 20, "Vow Against Oppression (Zaheeran)",
              "Musa makes an eternal ethical oath: 'My Lord, for the favor You bestowed upon me, never will I be an ally to the criminals!'")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 06: CONSPIRACY & DESERT ESCAPE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Watchful Fear, The Council's Warrant & The Sincere Ally", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 21, "Watchful Apprehension in the City",
              "Walking cautiously, Musa discovers the same Israelite instigating another brawl, rebuking him as an unguided troublemaker.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 22, "The Fatal Secret Exposed",
              "Thinking Musa intends to strike him, the quarreler exposes the prior killing, crying out: 'Do you intend to slay me like yesterday?'")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 23, "The Running Believer (Rajulun Yas'a)",
              "A courageous nobleman rushes from the city's outskirts, warning Musa that the high council is signing an execution warrant.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 24, "Unarmed Flight Into the Wilderness",
              "Musa flees toward Madyan without bread or beast, crying: 'My Lord, save me from the unjust; guide me upon the straight path!'")

    # ==========================================
    # PLATE 04: THE WELL OF MADYAN & COVENANT
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 8,
        "THE WELL OF MADYAN & THE SACRED COVENANT",
        "Pillars 7 & 8: Chivalry in the Shade, The Universal Beggar's Du'a & The Hiring Standard",
        "PLATE 04 : THE SHADE OF MADYAN"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 07: CHIVALRY & THE ACACIA SHADE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Restrained Maidens, Unprompted Service & Absolute Need", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 25, "The Restrained Flock (Tadhudaan)",
              "Reaching Madyan's well, Musa sees aggressive male shepherds jostling, while two women keep back their sheep with reserved dignity.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 26, "Pure Chivalric Relief (Fa-Saqa)",
              "Though starving and exhausted, Musa lifts the massive stone unassisted, waters their flock, and demands neither wage nor gratitude.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 27, "Retreat to the Acacia Shade (Az-Zill)",
              "Withdrawing immediately to avoid unnecessary interaction, Musa seeks refuge under an acacia tree, looking only to the heavens.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 28, "The Beggar's Du'a (Rabbi Inni Lima)",
              "Musa pours his soul out: 'My Lord, indeed I am in absolute, destitute need of whatever goodness You send down upon me!'")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 08: MODESTY & THE IDEAL HIRE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Sacred Haya', Character Assessment & The Ten-Year Term", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 29, "Walking with Modesty (Istihya')",
              "One maiden approaches walking with radiant modesty, conveying her father's invitation to honor Musa's chivalric labor.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 30, "Sanctuary with the Patriarch",
              "Recounting his trials, the elder reassures Musa: 'Do not fear; you have escaped from the wrongdoing, tyrannical people.'")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 31, "The Hiring Standard (Al-Qawiyyu Al-Ameen)",
              "The daughter outlines the timeless formula of public governance and employment: hire the one who is Strong and Trustworthy.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 32, "The Covenant of Prophetic Honor",
              "Musa contracts an eight-year marital covenant of pastoral work, freely choosing to complete the full ten years in noble generosity.")

    # ==========================================
    # PLATE 05: MOUNT TUR & THE IMPERIAL TOWER
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        5, 8,
        "MOUNT TUR & THE IMPERIAL TOWER",
        "Pillars 9 & 10: The Sacred Bush, Staff and Radiant Hand, Pharaoh's Hubris & Haman's Ziggurat",
        "PLATE 05 : THE SACRED MOUNT"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 09: THE FIRE AT MOUNT TUR", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("The Blessed Valley, Theophany & The Prophetic Commission", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 33, "The Fire in the Desert Night",
              "Traveling across Sinai with his family, Musa perceives a fire upon Mount Tur, seeking warmth and navigational guidance.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 34, "The Celestial Call (Inni Ana Allah)",
              "Called from the right bank of the blessed valley from the tree: 'O Musa, indeed I am Allah, Lord of the Worlds!'")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 35, "The Serpent & The Radiant Hand",
              "The staff wriggles like an agile serpent; drawing his hand from his garment, it shines brilliant white without blemish or harm.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 36, "Harun Appointed Ministerial Partner",
              "Acknowledging his fear of retaliation, Musa requests his brother Harun as an eloquent ministerial partner to confirm the message.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 10: PHARAOH'S HUBRIS & RETRIBUTION", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("False Divinity, Baked Clay Tower & Submersion in the Sea", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 37, "Pharaoh's Cosmic Arrogance",
              "Pharaoh proclaims to his council: 'O nobles, I have known no god for you other than me!'—the zenith of totalitarian narcissism.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 38, "Haman's Baked Clay Tower (Sarh)",
              "Ordering Haman to bake mud bricks and erect a towering ziggurat to inspect Musa's God, mocking the unseen Lord of creation.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 39, "Seized & Cast Into the Sea",
              "Allah seizes Pharaoh and his elite legions, hurling them into the roaring waves like worthless flotsam, ending the dynasty.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 40, "Leaders Inviting to the Fire (A'immah)",
              "The tyrants are branded leaders inviting humanity to the Fire, abandoned and disgraced on the Day of Resurrection.")

    # ==========================================
    # PLATE 06: SCRIPTURE & THE LAW OF GUIDANCE
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        6, 8,
        "SCRIPTURE & THE SOVEREIGN LAW OF GUIDANCE",
        "Pillars 11 & 12: The Illuminating Torah, Meccan Skepticism, The Passing of Abu Talib & Divine Selection",
        "PLATE 06 : THE LAW OF GUIDANCE"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 11: SCRIPTURE AS MERCY & LIGHT", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Torah as Insight, Historical Continuity & Human Caprice", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 41, "The Gift of the First Scripture",
              "After annihilating ancient tyrants, Allah gives Musa the Book as discernment, enlightenment, and mercy that people might reflect.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 42, "Witness of the Unseen History",
              "The Prophet was not on the western slopes of Sinai nor present at Madyan; the pristine Quranic account is unadulterated revelation.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 43, "Meccan Objections & Demands",
              "Skeptics protest: 'Why was he not given like Musa?' Yet they previously rejected Musa, declaring: 'Two works of magic aiding each other!'")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 44, "The Blindness of Vested Passions",
              "If they fail to produce a better scripture, know that they merely follow base desires; none is more astray than one led by whims.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 12: THE LAW OF DIVINE GUIDANCE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Innaka La Tahdi, Hearts in Divine Hands & Sincere Converts", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 45, "The Passing of Abu Talib",
              "Revealed when the Prophet grieved over his uncle's death: emotional longing cannot manufacture faith in an obstinate heart.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 46, "Guidance is a Sovereign Gift",
              "Allah alone guides whom He wills; human messengers are conveyors of truth, while spiritual opening belongs to the Creator.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 47, "Receptive Christian Believers",
              "Sincere scholars of earlier scriptures who weep upon hearing the Qur'an, proclaiming: 'We were Muslims even before this!'")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 48, "Turning Away from Vanity (Laghy)",
              "The righteous respond to ignorance with noble detachment: 'To us our deeds, and to you yours; peace upon you, we seek not the foolish.'")

    # ==========================================
    # PLATE 07: HUBRIS OF QARUN & SINKING EARTH
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        7, 8,
        "THE HUBRIS OF QARUN & THE SINKING EARTH",
        "Pillars 13 & 14: The Heavy Keys, The Scholars' Fivefold Charter, Meritocratic Hubris & Liquefaction",
        "PLATE 07 : THE COLLAPSE OF WEALTH"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 13: QARUN'S HOARD & ADMONITION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Heavy Vault Keys, The Scholar's Admonition & Fatal Arrogance", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 49, "The Keys Burdening Strong Men",
              "Qarun accumulated treasures so massive that the iron keys to his vaults overburdened a whole cohort of vigorous, muscular men.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 50, "The Fivefold Economic Charter",
              "Scholars advised: Do not exult; seek the Hereafter; remember your worldly share; do good as Allah did to you; do not corrupt the earth.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 51, "Meritocratic Hubris ('Ala 'Ilmin 'Indi)",
              "Qarun sneers: 'I was only given this due to knowledge I possess!'—the quintessential delusion of self-made intellectual arrogance.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 52, "The Delusion of Worldly Observers",
              "Parading in opulence, worldly men sighed: 'Would that we had what Qarun has!' But men of knowledge warned: 'Allah's reward is superior!'")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 14: LIQUEFACTION & THE AWAKENING", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("The Swallowing Ground, Complete Abandonment & Awakened Sight", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 53, "The Swallowing Earth (Khasafna)",
              "The solid earth cracks open and swallows Qarun, his towering palace, and his vaults into subterranean depths in terrifying seconds.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 54, "Total Absence of Partisans",
              "Neither his hired mercenaries, his gold, nor his political connections can offer a shred of defense against the decree of Allah.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 55, "The Morning Awakening of Envy",
              "Those who envied him yesterday shudder in horror, recognizing that wealth is an existential trial, not a proof of divine favor.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 56, "Sovereignty Over Provision (Rizq)",
              "Allah expands and restricts provision through transcendent wisdom; the deniers of truth will never achieve ultimate victory.")

    # ==========================================
    # PLATE 08: ETERNAL ABODE & PROMISE OF RETURN
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        8, 8,
        "THE ETERNAL ABODE & THE PROMISE OF RETURN",
        "Pillars 15 & 16: Tilka Ad-Daru Al-Akhirah, Freedom from Arrogance, The Sacred Return & The Perishing Cosmos",
        "PLATE 08 : THE FINAL RETURN"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 15: THE CONSTITUTION OF SALVATION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Tilka Ad-Daru Al-Akhirah, Rejection of 'Uluww & Fasad", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 57, "The Eternal Abode (Ad-Daru Al-Akhirah)",
              "That transcendent Home of the Hereafter is reserved exclusively for those who harbored no lust for tyranny or corruption on earth.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 58, "Freedom from High-Handed Pride ('Uluww)",
              "Entry requires a heart purified from narcissism, superior haughtiness, and desires to subjugate fellow humans beneath one's will.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 59, "Rejection of Corruption (Fasad)",
              "True faith is incompatible with exploiting society, plundering public wealth, or spreading moral and environmental decay.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 60, "The Ultimate Victory for the Muttaqeen",
              "The everlasting ending belongs to the God-conscious who anchored their lives in devotion, equity, and sincere humility.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 16: THE RETURN & THE FACE OF ALLAH", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("La-Raadduka Ila Ma'ad, Divine Protection & The Eternal King", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 61, "Comfort in Forced Displacement",
              "Departing Mecca in exile, the Prophet is consoled: the One who ordained the Qur'an will surely return you to your ultimate home.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 62, "The Triumphant Return (Ma'ad)",
              "Foretelling the triumphant return to Mecca and the ultimate gathering on the Day of Resurrection under divine vindication.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 63, "Absolute Prohibition of Shirk",
              "Never call upon another deity alongside Allah; worship Him alone in pure unadulterated monotheism without partner or intermediary.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 64, "Everything Perishes Except His Face",
              "Every mortal entity, empire, and mountain will dissolve into dust except His Noble Face. His is judgment, and to Him is the return.")

    pdf.save(OUTPUT_PDF)
    print(f"[OK] Generated {OUTPUT_PDF}")

    # Generate preview PNGs
    cmd = f"pdftoppm -png -r 150 {OUTPUT_PDF} {PREVIEWS_DIR}/page"
    subprocess.run(cmd, shell=True, check=True)
    print(f"[OK] Generated preview images in {PREVIEWS_DIR}")

    # Copy to brain dir
    for i in range(1, 9):
        src = f"{PREVIEWS_DIR}/page-{i}.png"
        dst = f"{brain_dir}/al_qasas_mindmap_page_{i}.png"
        if os.path.exists(src):
            shutil.copyfile(src, dst)
            print(f"[OK] Copied preview to {dst}")

if __name__ == "__main__":
    build_al_qasas_pdf()
