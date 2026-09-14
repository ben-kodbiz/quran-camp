#!/usr/bin/env python3
"""
Huurs Studio - Surah Yunus Master Mindmap Vector PDF Generator
16:9 Landscape Widescreen (792 x 480 pt) • 8 Plates • 16 Pillars • 64 Cards
"""

import os
import sys
import subprocess
import shutil

sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
OUTPUT_PDF = os.path.join(BASE_DIR, "YUNUS_MASTER_MINDMAP.pdf")
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

def build_yunus_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH YUNUS", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
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
    # PAGE 1: COSMIC WISDOM, CREATION & THE SIGNS OF TIME
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 8,
        "COSMIC WISDOM, CREATION & THE SIGNS OF TIME",
        "Pillars 1 & 2: The Wise Book, The Throne Administration, Solar Radiance & Lunar Chronometry",
        "PLATE 01 : CREATION & CHRONOMETRY"
    )

    # Column 1: Pillar 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 1: THE BOOK OF WISDOM & SOVEREIGN GOVERNANCE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Kitabin Hakeem, Six Epochs of Creation & The Throne Administration", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. Alif-Lam-Ra: The Book of Supreme Wisdom", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Verses of the Wise Scripture revealed to awaken humanity from slumber.\n"
        "- Addressing human bewilderment that a mortal man was chosen to convey revelation.\n"
        "- Establishing that divine guidance is the highest cosmic mercy bestowed on creation."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("2. The Cosmic Hexaemeron & Sovereign Throne", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Allah created the heavens and earth in six epochs, then established His Throne.\n"
        "- Yudabbirul-Amr: Sovereignly directing and administering all celestial and earthly affairs.\n"
        "- No particle in existence moves outside His flawless knowledge and sovereign decree."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("3. No Intercessor Except by Divine Leave", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Demolishing polytheistic fantasies of independent, automatic intercessors.\n"
        "- No mediation occurs in the divine court except after His explicit permission.\n"
        "- That is Allah your Lord; therefore worship Him alone; will you not reflect?"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("4. The Return of All Souls & Justice of Creation", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Unto Him is the return of all humanity; a promise of Allah binding in truth.\n"
        "- He originates creation then restores it to reward the believers with absolute equity.\n"
        "- Deniers face excruciating consequences for rejecting objective cosmic reality."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 2
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 2: CELESTIAL CHRONOMETRY & THE DAY OF ACCOUNTING", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Sun as Radiance, Moon as Luminescence & The Reckoning of Years", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("5. The Radiant Sun & The Luminescent Moon", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Precise lexical demarcation: Sun made Diya' (radiant heat/light); Moon made Noor.\n"
        "- Distinguishing active solar radiance from cool, serene reflected lunar illumination.\n"
        "- Allah created not all of this except in profound, purposeful cosmic truth (Bil-Haqq)."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("6. Orbital Precision & The Calculation of Eras", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Calibrating the lunar trajectory into 28 distinct astronomical stations (Manazil).\n"
        "- Enabling human civilization to reckon the count of years and calculate time.\n"
        "- Detailing celestial signs for a people possessing deep intellectual discernment."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("7. Alternation of Night & Day as Divine Signs", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- In the cyclic rotation of nocturnal dark and diurnal light are magnificent signs.\n"
        "- Manifesting divine wisdom in all that Allah created throughout the heavens and earth.\n"
        "- A continuous living testament reserved for those who cultivate God-consciousness (Taqwa)."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("8. The Tragedy of Worldly Satisfaction", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Those who anticipate no encounter with their Lord, satisfied with mortal life.\n"
        "- Finding false tranquility in transient adornments while heedless of eternal signs.\n"
        "- Their ultimate refuge is the Fire for what their own hands consistently earned."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 2: THE HUMAN PSYCHOLOGICAL PARADOX & THE FLEETING WORLD
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 8,
        "THE HUMAN PSYCHOLOGICAL PARADOX & THE FLEETING WORLD",
        "Pillars 3 & 4: Man in Distress vs Relief, The Maritime Storm & Earthly Meadows Pulverized",
        "PLATE 02 : HUMAN PARADOX & PARABLES"
    )

    # Column 1: Pillar 3
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 3: THE UNGRATEFUL SOUL IN DISTRESS & RELIEF", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Calling Upon God Reclining/Sitting/Standing & Walking Away in Ingratitude", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("9. Supplication in Agony & Immediate Forgetfulness", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- When harm touches man, he calls upon Us in every posture: on his side, sitting, or standing.\n"
        "- Yet when relief is granted, he passes on indifferently as if he had never prayed.\n"
        "- Exposing the shallow spiritual opportunism of the heedless human ego."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("10. Generations Destroyed for Injustice", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- We destroyed generations before you when they committed sustained systemic tyranny.\n"
        "- Their Messengers brought clear proofs, yet they obstinately refused to believe.\n"
        "- Thus does divine retribution inevitably recompense stubborn criminal communities."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("11. Successors Upon the Earth (Khala'if)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Then We established you as terrestrial stewards after them to see how you behave.\n"
        "- Power, resources, and longevity are an active moral examination, not an entitlement.\n"
        "- Accountability awaits every community regarding its stewardship of the earth."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("12. Rejecting Demands to Alter Revelation", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Deniers demand: 'Bring a Quran other than this, or alter its unbending truth!'\n"
        "- Proclaim: 'It is not for me to change it of my own accord; I follow only revelation.'\n"
        "- The Messenger transmits divine truth purely, fearing the chastisement of a Great Day."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 4
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 4: PARABLES OF THE TRANSIENT WORLD (AL-HAYAT AD-DUNYA)", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("The Sudden Storm, Earthly Splendor as Stubble & Inviting to Dar as-Salam", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("13. The Maritime Parable: The Violent Sea Storm", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Ships gliding smoothly through the ocean with joyous, favorable winds.\n"
        "- Suddenly, a tempest strikes; waves surge from every direction; mortals feel encircled.\n"
        "- Stripping all pretense: Pleading with Allah in pure, unadulterated monotheistic sincerity."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("14. Desperate Vows on the Waves & Insolvent Return", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Crying out: 'If You rescue us from this peril, we will surely be of the grateful!'\n"
        "- Yet when brought safely to dry shore, they immediately resume rebellion and injustice.\n"
        "- O humanity, your injustice is only against yourselves; brief worldly pleasure, then return."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("15. The Blooming Meadow Pulverized Overnight", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Rain falls; earth adorns itself in lush splendor; humans think they master it.\n"
        "- Our command strikes by night or day, rendering it reaped stubble overnight.\n"
        "- Ka'an lam taghna bil-ams: As if it had never flourished yesterday; reflect, O thinkers!"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("16. The Invitation to the Abode of Peace (Dar as-Salam)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- While the world decays into stubble, Allah invites humanity to the Abode of Peace.\n"
        "- Guiding whom He wills to an unswerving, luminous Straight Path (Sirat Mustaqeem).\n"
        "- Trading fleeting mortal vanity for eternal, unshakeable sanctuary in the presence of God."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 3: ESCHATOLOGICAL CERTAINTY & THE SUPREME VISION
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 8,
        "ESCHATOLOGICAL CERTAINTY & THE SUPREME VISION",
        "Pillars 5 & 6: Az-Ziyadah (The Divine Countenance), Radiant Faces vs Darkness & Idols Disavowed",
        "PLATE 03 : AZ-ZIYADAH & ESCHATOLOGY"
    )

    # Column 1: Pillar 5
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 5: AZ-ZIYADAH: GAZING UPON THE DIVINE COUNTENANCE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Lilladhina Ahsanoo al-Husna wa Ziyadah & The Radiance of the Redeemed", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("17. Al-Husna: The Ultimate Reward of Paradise", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- For those who practiced spiritual excellence (Ihsan) is the ultimate good: Jannah.\n"
        "- An abode of pristine beauty, unblemished joy, and eternal physical felicity.\n"
        "- The magnificent fruition of patient faith, righteous conduct, and moral struggle."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("18. Az-Ziyadah: Gazing Upon the Lord's Countenance", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Verified in Sahih Muslim: The veil is lifted; dwellers of Jannah behold their Lord.\n"
        "- The supreme climax of existence: Gazing upon the transcendent Beauty of Allah.\n"
        "- Eclipsing all sensory delights of Paradise; the ultimate increase of the redeemed."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("19. Faces Free from Humiliation & Dust", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Neither darkness, gloom, nor disgrace shall touch the radiant countenances of believers.\n"
        "- Illuminated by divine light, reflecting the peace of eternal divine acceptance.\n"
        "- These are the true companions of Paradise; therein they will dwell forever."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("20. Faces Shrouded in Blackness (Ka'annama Ughshiyat)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Those who earned evil: Recompense of evil is its like, covered in suffocating disgrace.\n"
        "- Faces shrouded in black gloom as if draped in fragments of pitch-black night.\n"
        "- They have no protector against Allah; they are the eternal companions of the Fire."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 6
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 6: THE INTERROGATION OF FALSE DEITIES", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Severed Polytheistic Claims, Idols Disavowing Worship & The Sovereign Provider", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("21. Gathering the Nations & Severing False Alliances", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- On the Day We gather all creation, We say to the polytheists: 'Stay in your places!'\n"
        "- We separate them from their fabricated partners, dissolving all pagan illusions.\n"
        "- The terrifying moment when all worldly crutches and false deities vanish into nothingness."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("22. The Disavowal of the Idols", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Their fabricated deities speak out: 'You were never truly worshipping us!'\n"
        "- 'Allah is sufficient as witness between us; we were utterly unaware of your worship.'\n"
        "- Polytheists betrayed by the very entities they traded away their souls to venerate."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("23. Who Provides from the Heavens and the Earth?", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Challenge them: Who provides your sustenance? Who controls hearing and sight?\n"
        "- Who brings forth the living from the dead, and rules all affairs? They say: 'Allah!'\n"
        "- Say: 'Will you then not fear Him and abandon your illogical idolatrous associations?'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("24. Beyond Truth, What Remains Except Error?", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Fa-dhalikumullahu Rabbukumul-Haqq: That is Allah, your true Sovereign Lord.\n"
        "- What can exist after the manifest truth except catastrophic delusion and error?\n"
        "- How then can you be turned away from cosmic reality into irrational falsehood?"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 4: THE MIRACLE OF THE QUR'AN & THE HEALING OF HEARTS
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 8,
        "THE MIRACLE OF THE QUR'AN & THE HEALING OF HEARTS",
        "Pillars 7 & 8: Inimitability Challenge, The Fourfold Medicine of Revelation & Rejoicing in Divine Grace",
        "PLATE 04 : INIMITABILITY & HEALING"
    )

    # Column 1: Pillar 7
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 7: INIMITABILITY & THE DIVINE PROVENANCE OF REVELATION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Could Never Be Produced by Other Than Allah & The Challenge of a Single Surah", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("25. The Impossibility of Human Authorship", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- This Quran could never have been authored or produced by other than Almighty Allah.\n"
        "- Confirming the authentic scriptures revealed before it and detailing divine law.\n"
        "- An uncorrupted, infallible revelation sent from the Lord of all the Worlds."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("26. The Ultimate Challenge: Produce a Single Surah", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- If you claim: 'He forged it!' then produce a single Surah like it in eloquence and truth.\n"
        "- Call upon whomsoever you can muster besides Allah, if you are indeed truthful.\n"
        "- The permanent, unanswerable challenge that broke the literary pride of Arabia."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("27. Denying What Lies Beyond Their Comprehension", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Rather, they denied that which their intellect could not encompass in knowledge.\n"
        "- Rejecting the unseen reality before its undeniable fulfillment has arrived.\n"
        "- Thus did earlier deniers belie their prophets; look at the final end of wrongdoers!"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("28. Apostles to Every Nation with Absolute Justice", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- For every community of humanity there is a divine Messenger sent to warn them.\n"
        "- When their Messenger arrives, they are judged with absolute, immaculate justice.\n"
        "- Never is any human soul wronged in the divine court; truth is established fairly."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 8
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 8: THE FOURFOLD TRANSFIGURATION OF REVELATION", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Maw'idhah, Shifa', Huda & Rahmah: Rejoicing in Divine Bounty", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("29. The Admonition from Your Lord (Maw'idhah)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- O humanity, there has arrived to you a transformative admonition from your Lord.\n"
        "- Penetrating moral counsel shaking the human conscience free from worldly intoxication.\n"
        "- Awaking the slumbering soul before the irreversible gates of eternity close."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("30. The Healing for the Breasts (Shifa'un lima fis-Sudoor)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- A profound clinical medicine healing spiritual pathology within the human chest.\n"
        "- Eradicating arrogance, envy, hypocrisy, paralyzing anxiety, and existential doubt.\n"
        "- Restoring pristine fitrah and radiating healthy spiritual life throughout the soul."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("31. Guidance & Mercy for the Believers (Hudan wa Rahmah)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- An infallible intellectual and legal compass navigating complex ethical dilemmas.\n"
        "- Coupled with divine Rahmah: Showering the faithful in peace, comfort, and forgiveness.\n"
        "- Transforming broken mortal lives into monuments of righteous, purposeful living."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("32. Rejoicing Exclusively in Divine Grace", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Qul bi-fadlillahi wa bi-rahmatihi fa-bidhalika fal-yafrahoo: Rejoice in His grace!\n"
        "- Holding divine revelation in your heart is infinitely superior to all mortal wealth.\n"
        "- Elevating human ambition above transient bank balances into eternal divine treasure."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 5: THE ALLIES OF ALLAH & DIVINE OMNISCIENCE
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        5, 8,
        "THE ALLIES OF ALLAH & DIVINE OMNISCIENCE",
        "Pillars 9 & 10: The Sanctuary of Awliya'ullah, Glad Tidings in Both Worlds & The Weight of an Atom",
        "PLATE 05 : AWLIYA'ULLAH & OMNISCIENCE"
    )

    # Column 1: Pillar 9
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 9: THE SANCTUARY OF AWLIYA'ULLAH", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("No Fear nor Grief, Faith Combined with Taqwa & Glad Tidings in Both Worlds", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("33. The Allies of Allah: Free from Fear and Grief", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Ala inna awliya'allahi la khawfun 'alayhim wa la hum yahzanoon.\n"
        "- Protected from fear of what lies ahead in the grave and grief over worldly loss.\n"
        "- Resting within an impenetrable psychological and spiritual fortress of serenity."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("34. The Two Keys: Authentic Faith & Continual Taqwa", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Defined precisely: Alladheena amanoo wa kanoo yattaqoon.\n"
        "- True sainthood in Islam requires no esoteric pedigree; it demands Iman and Taqwa.\n"
        "- Every pious, God-conscious believer is an honored, beloved ally of Almighty Allah."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("35. Glad Tidings in This World & the Next (Al-Bushra)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- For them are joyous tidings in worldly life: Righteous dreams, praise, and inner peace.\n"
        "- And in the Hereafter: Angelic greetings upon death, expansive graves, and Jannah.\n"
        "- Unbroken divine companionship accompanying the righteous soul through all realms."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("36. No Alteration in the Words of Allah", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- La tabdeela li-kalimatillah: The promises and laws of Allah are immutable.\n"
        "- That is indeed the magnificent, ultimate attainment (Al-Fawz al-'Azeem).\n"
        "- Let not the arrogant speech or slander of deniers cause your heart sorrow."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 10
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 10: OMNIPRESENT WITNESS & THE WEIGHT OF AN ATOM", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Ma Takoonu fee Sha'n, Cosmic Ledger & Rebuking Fabricated Prohibitions", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("37. Divine Presence in Every Moment", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- In whatever matter you are engaged, or reciting scripture, We are Witnesses over you.\n"
        "- Total existential surveillance: No action is performed in isolation from divine sight.\n"
        "- Instilling acute awareness (Muraqabah) that sanctifies work, worship, and speech."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("38. Not the Weight of an Atom Escapes Him (Mithqala Dharrah)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Not an atom's weight in the earth or the heavens escapes your Sovereign Lord.\n"
        "- Nothing smaller than that nor larger exists except recorded in a Clear Book.\n"
        "- Absolute cosmic data integrity preserving every good intention and hidden tear."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("39. Rebuking Invented Religious Prohibitions", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Denouncing those who declare lawful provisions unlawful based on cultural whims.\n"
        "- 'Has Allah permitted you this, or do you invent fabrications against Allah?'\n"
        "- Protecting the purity of Shari'ah from arbitrary human tampering and false asceticism."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("40. What Do Fabricators Expect on the Last Day?", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- What will those who invent lies against Allah think on the Day of Resurrection?\n"
        "- Allah is indeed full of boundless bounty to humanity, yet most mortals are ungrateful.\n"
        "- Calling humanity back to humble gratitude before the Day of ultimate accounting."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 6: THE PROPHETIC CYCLE: NUH & THE CRUCIBLE OF MUSA
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        6, 8,
        "THE PROPHETIC CYCLE: NUH & THE CRUCIBLE OF MUSA",
        "Pillars 11 & 12: Nuh's Unshakable Reliance, The Ark of Survival & Musa Confronting Sorcery",
        "PLATE 06 : NUH & MUSA'S CRUCIBLE"
    )

    # Column 1: Pillar 11
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 11: THE DEFIANCE OF NUH & THE ARK OF SURVIVAL", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Confronting Polytheist Conspiracies, No Recompense Demanded & Drowning Oppressors", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("41. Nuh's Challenge to His Hostile Nation", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Nuh said to his people: 'If my station and reminders of Allah's signs offend you...'\n"
        "- 'Then upon Allah alone I rely; gather your associates and execute your plot without delay!'\n"
        "- The supreme fearlessness of a solitary prophet armored only in absolute Tawakkul."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("42. I Ask of You No Recompense (In Ajriya illa 'alallah)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'And if you turn away, I have never asked you for any material wage or wealth.'\n"
        "- 'My recompense is only with Allah, and I am commanded to be of those who submit.'\n"
        "- Complete purity of prophetic purpose: Liberated from all worldly dependency."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("43. The Ark of Salvation & The Inundation", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- They denied him, so We saved Nuh and those aboard the Ark, making them successors.\n"
        "- While We drowned those who rejected Our signs in the cataclysmic deluge.\n"
        "- Illustrating that moral rectitude survives while tyrannical civilizations drown."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("44. The Consequence of the Warned Nations", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Gaze upon the final end of those who were warned yet persisted in arrogance.\n"
        "- After Nuh, Messengers arrived with clear proofs, yet communities refused to believe.\n"
        "- Thus does Allah seal the hearts of those who transgress beyond all moral boundaries."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 12
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 12: MUSA & HARUN CONFRONTING PHARAOH'S SORCERY", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Magic Dismissed as Truth, Staff Swallowing Illusions & Pharaoh's Tyranny", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("45. Commissioning Musa & Harun with Clear Signs", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Dispatched to Pharaoh and his ruling elite with unmistakable divine miracles.\n"
        "- Yet they behaved with haughty pride and were an entrenched criminal people.\n"
        "- Power blinded to truth, scorning prophetic warnings as subversive threats."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("46. Denouncing Truth as Sorcery (Asihrun Hadha?)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- When divine truth arrived, the regime proclaimed: 'This is manifest sorcery!'\n"
        "- Musa said: 'Do you say this of the truth when it has come to you? Can this be magic?'\n"
        "- Proclaiming with divine certainty: 'Sorcerers and deceivers will never triumph!'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("47. Summoning the Magicians of the Empire", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Pharaoh commanded: 'Bring before me every master sorcerer in the empire!'\n"
        "- A public spectacle designed to preserve imperial hegemony through optical illusion.\n"
        "- Musa said to the assembled magicians: 'Cast down whatever you are going to cast!'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("48. The Staff Annihilating Imperial Illusion", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Musa proclaimed: 'What you brought is sorcery; Allah will surely nullify it!'\n"
        "- 'Indeed, Allah does not prosper the corrupt work of those who spread mischief.'\n"
        "- Allah establishes truth by His words, even though hardened criminals detest it."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 7: THE SEA CRUCIBLE, PHARAOH'S DROWNING & HIS PRESERVED BODY
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        7, 8,
        "THE SEA CRUCIBLE, PHARAOH'S DROWNING & HIS PRESERVED BODY",
        "Pillars 13 & 14: Homes as Sanctuaries (Buyootakum Qiblah), Parting the Sea & The Preserved Corpse",
        "PLATE 07 : EXODUS & PHARAOH PRESERVED"
    )

    # Column 1: Pillar 13
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 13: THE EXODUS & SPLITTING OF THE RED SEA", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Turning Domestic Homes into Sanctuaries, Establishing Prayer & The Parted Sea", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("49. Turning Domestic Homes into Sanctuaries", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Commanded Musa and Harun: 'Settle your people in homes and make them places of prayer!'\n"
        "- When public congregational worship was suppressed, homes became spiritual citadels.\n"
        "- Establish Salah with diligence and give joyous glad tidings to the faithful believers."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("50. Musa's Imprecation Against Pharaoh's Wealth", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Our Lord, You granted Pharaoh and his chiefs splendor and wealth in this life...'\n"
        "- 'Obliterate their wealth and harden their hearts so they believe not until painful doom!'\n"
        "- An imprecation against systemic oppressors who weaponize resources against truth."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("51. The Answered Supplication: Be Steadfast!", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Allah declared: 'Your prayer has been answered; so remain steadfast and straight!'\n"
        "- 'And follow not the reckless path of those who know not cosmic truth and law.'\n"
        "- The divine promise fulfilled through unshakeable prophetic persistence."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("52. The Red Sea Parting & Pharaoh's Pursuit", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- We led the Children of Israel across the sea through miraculous parted dry beds.\n"
        "- Pharaoh and his legions pursued them in insolent tyranny and aggressive hatred.\n"
        "- Setting the stage for the definitive historical demise of the ancient superpower."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 14
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 14: THE DEATHBED CONFESSION & THE PRESERVED CORPSE", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Pharaoh Drowning, 'Al-Aana', The Sign for Generations & Bani Israel Delivered", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("53. Surging Waves & The Deathbed Surrender", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- When drowning waters overwhelmed him, Pharaoh cried: 'I believe in Israel's God!'\n"
        "- 'I testify that there is no deity except Him, and I am of those who submit (Muslimoon)!'\n"
        "- The terrifying collapse of imperial arrogance in the face of inevitable mortality."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("54. The Divine Rejection: 'Al-Aana?' (Now?)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Now you believe? When you rebelled previously and were of the corrupters?'\n"
        "- Repentance in the agony of death (Hadd al-Ya's) is universally rejected by God.\n"
        "- Free will terminates when the veil of the unseen is ripped aside by doom."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("55. Preservation of the Tyrant's Body (Bi-Badanika)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Fa-l-yawma nunajjeeka bi-badanika: Today We rescue your physical corpse from the sea.\n"
        "- Cast upon the shores so that you become an enduring sign for all future generations.\n"
        "- An astonishing archaeological prophecy preserved in history down to the modern era."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("56. Deliverance of Bani Israel & Warning Against Doubt", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- We settled the Children of Israel in an honorable settlement and provided good sustenance.\n"
        "- Yet they differed only after verified knowledge arrived; your Lord will judge between them.\n"
        "- Warning the Ummah against following the sectarian pitfalls of past delivered nations."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 8: THE MIRACLE OF YUNUS'S PEOPLE & THE SUFFICIENCY OF ALLAH
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        8, 8,
        "THE MIRACLE OF YUNUS'S PEOPLE & THE SUFFICIENCY OF ALLAH",
        "Pillars 15 & 16: The Unique Repentance of Yunus's Nation, Free Will & The Fortress of Tawhid",
        "PLATE 08 : YUNUS'S NATION & TAWHID"
    )

    # Column 1: Pillar 15
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 15: THE UNIQUE EXEMPTION OF THE PEOPLE OF YUNUS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Collective Repentance, Lifting Worldly Torment & The Bounds of Free Will", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("57. The Unprecedented Repentance of Yunus's Nation", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Why was there not a single city that believed and benefited except Yunus's people?\n"
        "- When signs of retribution loomed, the entire population of Nineveh wept in contrition.\n"
        "- Casting off pride, they prostrated collectively before the storm of doom descended."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("58. The Removal of Worldly Degradation", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Lamma amanoo kashafna 'anhum: When they believed, We lifted shameful worldly torment.\n"
        "- Granted them wholesome enjoyment of life for an appointed season.\n"
        "- Proving that sincere, collective societal repentance has power to alter history."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("59. The Inviolability of Moral Free Will", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Had your Lord willed, all on earth would have believed together; will you compel them?\n"
        "- Faith cannot be coerced by sword or state force; it is an act of free moral choice.\n"
        "- The prophetic duty is immaculate conveyance; guidance belongs exclusively to Allah."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("60. No Soul Believes Except by Divine Leave", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- No soul can believe except by the permission and decree of Almighty Allah.\n"
        "- And He places disgraceful filth (Rijs) upon those who obstinately refuse to reason.\n"
        "- Look at what is in the heavens and earth! Yet signs and warnings avail not the deniers."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 16
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 16: THE ULTIMATE PROTECTION & PROPHETIC PROCLAMATION", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Fa in Kunta fee Shakkin, If Allah Touches with Harm & Follow Revelation", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("61. Consulting Prior Scriptures: Absolute Certainty", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- If you are in doubt, ask those who have been reading the Scripture before you.\n"
        "- The truth has arrived from your Lord, so be not of those who waver in uncertainty.\n"
        "- Corroborating the eternal monotheistic chain connecting all authentic prophets."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("62. If Allah Touches You with Harm (Bi-Durrin)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- If Allah touches you with affliction, none can remove or relieve it except Him.\n"
        "- And if He intends good for you, none can turn back or repel His boundless bounty.\n"
        "- He causes it to reach whom He wills of His servants; He is Forgiving, Merciful."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("63. O Humanity, The Truth Has Arrived from Your Lord", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Proclaim: 'O people, the truth has come to you from your Sovereign Lord!'\n"
        "- Whoever is guided is guided only for the eternal benefit of his own soul.\n"
        "- And whoever strays strays only against himself; I am not a warden over you."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("64. Follow Revelation & Patiently Await Allah's Judgment", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Follow what is revealed to you, and be patient until Allah issues His judgment.\n"
        "- For He is the absolute Best of Judges (Khayrul-Hakimeen), ruling with flawless equity.\n"
        "- The eternal conclusion: Anchor the heart in patient endurance and divine trust."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Save PDF
    pdf.save(OUTPUT_PDF)
    print(f"Master Mindmap PDF generated: {OUTPUT_PDF}")

    # Generate PNG Previews
    cmd = f"pdftoppm -png -r 150 {OUTPUT_PDF} {PREVIEWS_DIR}/yunus_page"
    subprocess.run(cmd, shell=True, check=True)
    print("Previews generated in previews dir.")

    # Copy to brain dir
    for i in range(1, 9):
        src = f"{PREVIEWS_DIR}/yunus_page-{i}.png"
        dst = os.path.join(brain_dir, f"yunus_page-{i}.png")
        shutil.copyfile(src, dst)
    print("Previews copied to brain dir successfully.")

if __name__ == "__main__":
    build_yunus_pdf()
