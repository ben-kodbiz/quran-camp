#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Hijr Master Mindmap Vector PDF Generator
16:9 Landscape Widescreen (792 x 480 pt) • 8 Plates • 16 Pillars • 64 Cards
"""

import os
import sys
import subprocess
import shutil

sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
OUTPUT_PDF = os.path.join(BASE_DIR, "HIJR_MASTER_MINDMAP.pdf")
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

def build_hijr_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH AL-HIJR", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
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
    # PAGE 1: THE PRESERVATION OF DHIKR & THE VEIL OF COSMIC PROTECTION
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 8,
        "THE PRESERVATION OF DHIKR & THE VEIL OF COSMIC PROTECTION",
        "Pillars 1 & 2: Scriptural Infallibility, Future Regret & Celestial Constellations",
        "PLATE 01 : PRESERVATION & COSMOS"
    )

    # Column 1: Pillar 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 1: SCRIPTURAL INTEGRITY & THE PROMISE OF PRESERVATION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Inna Nahnu Nazzalna, Rubama Yawaddu & Infallible Protection", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. Al-Kitab and the Clarifying Recitation", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Opening with Alif-Lam-Ra: Distinctive symbols asserting transcendent literary majesty.\n"
        "- The verses are described as signs of the written Scripture and a clarifying Recitation.\n"
        "- Removing all ambiguity concerning the origin, purpose, and final destiny of existence."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("2. The Future Regret of Disbelief (Rubama Yawaddu)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- A glimpse into the eschatological future: deniers yearning desperately to have surrendered.\n"
        "- Regret intensified upon witnessing the salvation of the humble, patient believers.\n"
        "- Leaving the heedless to consume food, revel in delusion, and be blinded by false hope."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("3. The Charge of Madness & Angelic Rebuttal", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Opponents cynically mocking: 'O you upon whom the Reminder descended, you are mad!'\n"
        "- Demanding the physical descent of angels as sensational spectacle rather than moral truth.\n"
        "- Divine answer: Angels descend only in ultimate purpose, after which no respite remains."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("4. Inna Nahnu Nazzalna: The Eternal Preservation of Dhikr", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The supreme covenant: 'Indeed, it is We who sent down the Dhikr, and We are its Guardian.'\n"
        "- Textual preservation unique in religious history, shielding against interpolation.\n"
        "- Protecting both the linguistic wording and the theological essence of the Revelation."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 2: CELESTIAL CONSTELLATIONS & THE BARRED HEAVENS", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Burooj, Shihabun Mubeen & The Balanced Earth (Mawzoon)", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("5. Constellations (Burooj) Adorning the Night Sky", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Great cosmic stations, clusters, and constellations positioned with mathematical precision.\n"
        "- Adorning the vast expanse of the cosmos for the contemplation of observant eyes.\n"
        "- Transforming the night sky into an open theater of divine artistry and majesty."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("6. Heavenly Defense Against Eavesdropping Devils", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The celestial realm sealed and guarded against every accursed, outcast devil.\n"
        "- Any rogue entity attempting to steal heavenly secrets is pursued by a piercing flame.\n"
        "- Cosmic order reflecting spiritual inviolability: falsehood cannot penetrate sacred truth."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("7. Outspread Earth, Mountain Pegs & Balanced Growth", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The earth spread wide for human dwelling and cast with massive stabilizing mountains.\n"
        "- Causing vegetation and life to flourish in precise, calibrated equilibrium (Mawzoon).\n"
        "- Ecological harmony reflecting the wisdom and absolute measure of the Creator."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("8. Treasuries of All Things & Measured Descending", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'There is not a single thing except that with Us are its inexhaustible storehouses.'\n"
        "- Divine resources sent down exclusively according to an exact, calibrated measure.\n"
        "- Preventing cosmic chaos by rationing sustenance in harmony with human capacity."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 2: PRIMORDIAL CREATION & THE REBELLION OF PRIDE
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 8,
        "PRIMORDIAL CREATION & THE REBELLION OF PRIDE",
        "Pillars 3 & 4: Biological Genesis, The Divine Spirit & The Arrogance of Iblis",
        "PLATE 02 : CLAY & PRIDE"
    )

    # Column 1: Pillar 3
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 3: THE FERTILIZING WINDS & THE ARCHITECTURE OF FLESH", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Lawaqih, Salsalin Min Hama'in Masnoon & Naris-Samoom", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("9. Fertilizing Winds (Lawaqih) & Unstorable Waters", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Atmospheric winds dispatched as fertilizing agents for clouds, pollination, and rain.\n"
        "- Water poured from the sky for human drink, which mankind has no power to permanently store.\n"
        "- Complete human dependence on the continuous hydrologic cycle orchestrated by God."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("10. Sovereign Sovereignty Over Life, Death & Inheritance", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Indeed, it is We who give life and cause death, and We are the ultimate Inheritors.'\n"
        "- Full omniscience over the earliest generations and those yet to be born until the end.\n"
        "- All temporary earthly ownership eventually reverting back to the Eternal Sovereign."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("11. Humanity Formed from Sounding Clay of Altered Mud", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The primordial biological origin: fashioned from dried clay that rings like pottery.\n"
        "- Clay sourced from altered, dark mud (Hama'in Masnoon), emphasizing humble origins.\n"
        "- Grounding human self-conception in humility: created from dust, destined to return to dust."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("12. The Jinn Created of Scorching Fire (Naris-Samoom)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The creation of the Jinn prior to humanity from the smokeless, piercing fire of pestilence.\n"
        "- Distinct elemental origins establishing differences in constitution and accountability.\n"
        "- Setting the cosmic stage for the testing of moral obedience between distinct creations."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 4
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 4: THE DIVINE BREATH & THE ARROGANT REFUSAL", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Nafakhtu feehi min Roohee, Angelic Prostration & Expulsion", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("13. Fashioned Form & The Infusion of the Divine Ruh", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'When I have fashioned him in proportion and breathed into him of My Spirit...'\n"
        "- The dual nature of humanity: earthen clay elevated by transcendent divine breath.\n"
        "- Commanding the celestial assembly: 'Fall down before him in prostration of honor!'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("14. Angelic Prostration in Universal Obedience", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The entire angelic host prostrating collectively without a single exception or delay.\n"
        "- Absolute submission to divine command, recognizing God's wisdom in Adam's elevation.\n"
        "- Angelic devotion providing the model of unhesitating obedience to the Sovereign."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("15. The Treason of Iblis: Refusing to Bow to Clay", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Iblis obstinately refusing to join the prostrators out of deep-seated pride and jealousy.\n"
        "- The racist rationalization: 'I will not prostrate to a mortal created from altered clay!'\n"
        "- Elevating physical origin over spiritual reality; the origin of intellectual arrogance."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("16. The Expulsion from Sanctity & The Curse", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The divine verdict: 'Depart from here, for indeed you are an outcast, accursed entity!'\n"
        "- Stripped of proximity, honor, and grace for defying the Lord of the worlds.\n"
        "- An unbroken divine curse following him relentlessly until the Day of Retribution."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 3: THE COVENANT OF SEDUCTION & THE GATES OF PERDITION
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 8,
        "THE COVENANT OF SEDUCTION & THE GATES OF PERDITION",
        "Pillars 5 & 6: The Respite of Iblis, Glamorized Vice & The Immunity of Al-Mukhliseen",
        "PLATE 03 : SEDUCTION & GATES"
    )

    # Column 1: Pillar 5
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 5: RESPITE GRANTED & THE STRATEGY OF GLAMOR", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Al-Waqt al-Ma'loom, Tazyeen & The Sanctuary of Sincerity", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("17. Request for Postponement Until Resurrective Dawn", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Iblis petitioning the Almighty: 'My Lord, grant me respite until the day of resurrection.'\n"
        "- Motivated by vengeance rather than repentance; seeking to drag humanity down in ruin.\n"
        "- Acknowledging Allah as Lord (Rabbi) while remaining in absolute spiritual rebellion."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("18. Respite Until the Appointed Hour (Al-Waqt al-Ma'loom)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Divine concession: 'Indeed, you are of those granted respite until the Appointed Day.'\n"
        "- Respite granted not out of favor, but as the cosmic arena for human moral testing.\n"
        "- Establishing a bounded timeline beyond which evil will face absolute cosmic justice."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("19. The Vow of Deception: Glamorizing Evil Upon Earth", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'By Your decree leading me astray, I will surely make evil glamorous to them on earth.'\n"
        "- The psychological warfare of Satan: disguising destructive vices as liberating beauty.\n"
        "- Vowing to assault and mislead humanity across all cultural and historical eras."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("20. The Sanctuary of Devoted Servants (Al-Mukhliseen)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The forced admission: 'Except Your sincere, purified servants among them.'\n"
        "- Those whose hearts are purified exclusively for Allah are impenetrable to demonic deceit.\n"
        "- Sincerity (Ikhlas) as the supreme metaphysical shield against spiritual corruption."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 6
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 6: THE STRAIGHT PATH OF IMMUNITY & JAHANNAM", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Zero Demonic Authority & Seven Tiered Gates (Sab'atu Abwab)", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("21. The Binding Path: Zero Authority Over the Believer", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Allah's sovereign decree: 'This is a straight way binding upon Me.'\n"
        "- 'Indeed, over My servants you possess no authority whatsoever.'\n"
        "- Demonic influence is limited to whispering; it possesses zero power of physical coercion."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("22. The Domain of Satan: Only Those Who Freely Deviate", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Demonic sway applies exclusively to those who willfully choose to follow falsehood.\n"
        "- Human culpability remains total: no sinner can plead victimization before the Court.\n"
        "- Moral agency remains intact; following seduction is an act of free personal betrayal."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("23. The Promised Destination for Every Follower", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Jahannam is the unalterable appointment promised for all who follow Satan's path.\n"
        "- Cosmic justice demanding that the corrupters and the willfully corrupted share destiny.\n"
        "- The tragic end of those who traded divine sanctuary for illusory demonic promises."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("24. Seven Tiered Gates (Sab'atu Abwab) with Shares", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Hellfire engineered with seven distinct, descending gates of punishment.\n"
        "- Each gate allocated a designated, apportioned fraction of the condemned.\n"
        "- Precision in divine reckoning: punishments calibrated to the exact depth of guilt."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 4: THE ABODE OF PEACE & THE BALANCE OF ATTRIBUTES
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 8,
        "THE ABODE OF PEACE & THE BALANCE OF ATTRIBUTES",
        "Pillars 7 & 8: Paradisiacal Serenity, Eradication of Rancor & Nabbi' 'Ibadee",
        "PLATE 04 : PARADISE & MERCY"
    )

    # Column 1: Pillar 7
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 7: TRANSCENDENT GARDENS & RIPPED-OUT RESENTMENT", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Bi-Salamin Amineen, Naza'na ma fee Sudoorihim & Eternal Joy", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("25. Safe and Secure Entry into Gardens of Springs", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The God-conscious entering lush Paradisiacal gardens fed by crystal springs.\n"
        "- The celestial greeting: 'Enter in peace and complete safety!' (Bi-salamin amineen).\n"
        "- Freedom from every earthly anxiety, danger, instability, and existential threat."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("26. Eradication of All Rancor from the Chests", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'And We will remove whatever rancor, malice, or envy is within their breasts.'\n"
        "- Total spiritual purification: no unresolved trauma, resentment, or bitterness enters.\n"
        "- Inner emotional tranquility perfected as the prerequisite for eternal joy."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("27. Reclining Brothers Facing One Another in Love", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Reclining upon raised couches as loving brothers, facing one another directly.\n"
        "- Mutual honor, intimacy, and unblemished communion without jealousy or friction.\n"
        "- Restoring social fellowship to its primordial purity under the gaze of the Merciful."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("28. Stripped of Fatigue (Nasab) & Eternal Dwelling", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- No weariness, exhaustion, or physical depletion touches them in the Gardens.\n"
        "- 'Nor will they ever be removed or expelled therefrom'—eternity guaranteed.\n"
        "- The ultimate fulfillment of the human longing for permanent security and peace."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 8
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 8: EQUILIBRIUM OF MERCY AND RETRIBUTION", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Al-Ghafoor ar-Raheem, Al-'Adhab al-Aleem & Sunni Creed", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("29. Inform My Servants: Al-Ghafoor ar-Raheem", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Inform My servants that I am indeed the All-Forgiving, the Most Merciful.'\n"
        "- Opening with boundless grace, encouraging the remorseful soul to seek restoration.\n"
        "- Divine mercy preceding wrath, welcoming the penitent back into intimacy with God."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("30. Warning of the Painful Chastisement ('Adhab Aleem)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'And that My punishment is indeed the painful, agonizing punishment.'\n"
        "- Shattering false spiritual complacency and antinomian delusions of cheap grace.\n"
        "- Warning that deliberate, unrepentant rebellion meets uncompromising justice."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("31. Balancing Hope (Raja') and Awe (Khawf)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Classical Sunni exegesis: The believer flies to God with the twin wings of hope and fear.\n"
        "- Hope without fear leads to presumption; fear without hope leads to despair.\n"
        "- Achieving perfect psychological and theological equilibrium before the Divine Court."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("32. Transition to Historical Demonstrations of Justice", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Anchoring theological principles in concrete historical chronicles of past nations.\n"
        "- Transitioning from abstract attributes to empirical demonstrations in ancient lands.\n"
        "- Directing the seeker to examine the fates of nations that rejected prophetic warnings."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 5: ANGELIC EMISSARIES & THE DELIVERANCE OF THE RIGHTEOUS
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        5, 8,
        "ANGELIC EMISSARIES & THE DELIVERANCE OF THE RIGHTEOUS",
        "Pillars 9 & 10: Prophetic Glad Tidings, Rebuking Despair & Sodom's Extinction",
        "PLATE 05 : EMISSARIES & LUT"
    )

    # Column 1: Pillar 9
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 9: THE GUESTS OF IBRAHIM & GLAD TIDINGS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Bi-Ghulamin 'Aleem, Divine Power & Wa Man Yaqnatu", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("33. Emissaries Entering with Greetings of Peace (Salam)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Noble angelic emissaries entering upon Prophet Ibrahim with the sacred salutation of peace.\n"
        "- Disguised in human form, displaying celestial dignity and solemn focus.\n"
        "- The prototype of sacred hospitality and courteous spiritual communication."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("34. Prophetic Trepidation & Glad Tidings of a Knower", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Ibrahim expressing instinctual human apprehension: 'Indeed, we are fearful of you.'\n"
        "- Angels comforting him: 'Do not fear! We bring you glad tidings of a knowledgeable son.'\n"
        "- Divine favor breaking through human anxiety to bring miraculous prophetic continuation."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("35. Astonishment in Extreme Senescence & Divine Power", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Ibrahim astonished: 'Do you bring me good news when old age has overtaken me?'\n"
        "- Natural human reasoning confronting the limitless omnipotence of the Creator.\n"
        "- Affirmation: 'We bring you truth in certainty, so be not of those who despair.'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("36. None Despairs of Allah's Mercy Except the Astray", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The golden theological axiom: 'Who despairs of the mercy of his Lord except the astray?'\n"
        "- Despair diagnosed as an intellectual and spiritual disconnection from divine power.\n"
        "- Fortifying the soul with absolute trust in God's capacity to revive dead possibilities."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 10
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 10: THE COMMISSION OF WRATH & SHIELD OF LUT", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Extirpation of Criminals, Night Deliverance & Tragic Wife", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("37. The Inquest of Ibrahim: What is Your Dread Mission?", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Ibrahim inquiring of the emissaries: 'What is your ultimate assignment, O messengers?'\n"
        "- Discerning that celestial visitors carry weightier purposes than domestic glad tidings.\n"
        "- The prophetic heart concerned for the moral condition and survival of neighboring lands."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("38. Dispatched to Extinguish a Defiant Criminal Nation", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The angelic disclosure: 'We have been sent to a people deeply entrenched in crime.'\n"
        "- Depraved societies reaching the tipping point where divine retribution is inevitable.\n"
        "- Extirpating corruption to preserve the moral ecosystem of humanity."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("39. The Household of Lut Delivered in the Shadow of Dawn", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The decree of salvation: 'Except the family of Lut; indeed, we will save them all.'\n"
        "- Righteous individuals shielded from communal punishment through divine intervention.\n"
        "- Commanded to march in the quiet hours of night, with Lut guarding the rear."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("40. The Tragic Exception: The Wife Decreed to Remain", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Except his wife; We have decreed that she is of those who will remain behind.'\n"
        "- Biological proximity and marital ties cannot substitute for personal faith.\n"
        "- The solemn warning: sympathy with transgression aligns one with its catastrophic fate."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 6: THE APOCALYPTIC BLAST & THE RUINS OF FALSE SECURITY
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        6, 8,
        "THE APOCALYPTIC BLAST & THE RUINS OF FALSE SECURITY",
        "Pillars 11 & 12: Overturned Cities, Archaeological Signs & Megalithic Ruins of Thamud",
        "PLATE 06 : RUINS & MEGASYSTEMS"
    )

    # Column 1: Pillar 11
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 11: THE INTOXICATED MOB & OVERTURNED CITY", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("La'amruka Oath, As-Sayhah & Signs for Lil-Mutawassimeen", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("41. The Depraved Siege of Lut's Guests & Grief", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The corrupted citizens rushing exultantly to violate the angelic visitors.\n"
        "- Prophet Lut pleading in anguish: 'Do not disgrace me regarding my guests!'\n"
        "- Presenting lawful, honorable marriage, yet met with insolent, shameless refusal."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("42. The Sovereign Oath: Wandering in Intoxication", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Divine oath by the life of Muhammad: 'By your life, they wandered in intoxication!'\n"
        "- Moral depravity blinding cognitive faculties; sinners drunk on irrational passion.\n"
        "- Incapable of discerning their impending physical and spiritual annihilation."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("43. The Seismic Morning Blast & Sky Overturned", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The cataclysmic sonic blast overtaking the metropolis at sunrise.\n"
        "- Turning the city upside down: 'We made its highest part its lowest' ('Aliyaha safilaha).\n"
        "- Total geological inversion mirroring their inverted moral and spiritual order."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("44. Rain of Baked Clay (Sijjeel) & Signs for Observers", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Raining down upon them marked stones of hard, baked clay (Sijjeel).\n"
        "- The ruins left along an established commercial highway as an enduring witness.\n"
        "- 'Indeed, in that are signs for the discerning observers' (Lil-Mutawassimeen)."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 12
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 12: HEWN MOUNTAIN FORTRESSES OF AL-HIJR", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Ashab al-Aykah, Thamud's Megaliths & The Futility of Wealth", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("45. Ashab al-Aykah: The Injustice of the Thicket", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The companions of the Thicket (Ashab al-Aykah) living in economic exploitation.\n"
        "- Dismissing Prophet Shu'ayb's calls to fair measurement and righteous conduct.\n"
        "- Divine retribution seizing them, leaving their lands an open sign for travelers."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("46. Dwellers of the Rock Hewing Mountain Homes", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The people of Thamud carving elaborate, majestic palaces directly out of stone.\n"
        "- Advanced civil engineering and architectural mastery dominating rugged terrains.\n"
        "- Confident in their structural brilliance, deeming their fortresses impenetrable."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("47. The Illusion of Architectural Immortality (Amineen)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Hewing homes from the mountains, believing themselves permanently secure.\n"
        "- Material prosperity and technological sophistication breeding spiritual pride.\n"
        "- Denying divine signs, rejecting prophetic messengers, and relying on stone."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("48. The Morning Blast Rendering Engineering Worthless", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The morning blast (As-Sayhah) striking them with seismic, atmospheric fury.\n"
        "- 'And nothing availed them of that which they used to earn and construct.'\n"
        "- Megalithic masonry powerless against divine decree; monuments becoming tombs."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 7: THE SEVEN OFT-REPEATED & THE PROPHETIC SOLACE
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        7, 8,
        "THE SEVEN OFT-REPEATED & THE PROPHETIC SOLACE",
        "Pillars 13 & 14: Cosmic Purpose, Gracious Pardon & The Supreme Treasure of Al-Fatihah",
        "PLATE 07 : MATHANI & SOLACE"
    )

    # Column 1: Pillar 13
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 13: COSMIC PURPOSE & THE GRACIOUS PARDON", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Bil-Haqq, The Hour & Al-Khallaq al-'Aleem", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("49. Heavens and Earth Created Strictly in Truth (Bil-Haqq)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'We did not create the heavens and the earth and all between them except in Truth.'\n"
        "- Cosmic existence is purposeful, rational, and bounded by divine moral governance.\n"
        "- Rejecting nihilistic claims that the universe was born of blind chance or sport."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("50. The Certain Arrival of the Final Hour", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'And indeed, the Hour is surely coming without shadow of doubt.'\n"
        "- All temporal injustices and unresolved oppression will face definitive rectification.\n"
        "- Orienting the human conscience toward the cosmic deadline of resurrection."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("51. The Command of Noble Pardon (As-Safhu al-Jameel)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'So overlook their faults with gracious, dignified pardon' (Fasfahi as-safha al-jameel).\n"
        "- Forgiveness devoid of resentment, bitterness, complaints, or passive-aggressive rancor.\n"
        "- Preserving prophetic dignity and spiritual elevation above petty provocations."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("52. Al-Khallaq al-'Aleem: The Omniscient Creator", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Indeed, your Lord is the All-Creator, the All-Knowing' (Al-Khallaq al-'Aleem).\n"
        "- Continuously creating, knowing every intricate psychological and spiritual reality.\n"
        "- Reassuring the heart that the Creator understands the burdens carried by His servants."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 14
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 14: AL-SAB' AL-MATHANI & PROPHETIC COMPASSION", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Surah Al-Fatihah, La Tamuddanna & Lowering the Wing", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("53. The Seven Oft-Repeated (Al-Fatihah) & Grand Qur'an", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'And We have certainly given you seven oft-repeated verses and the grand Qur'an.'\n"
        "- Authenticated in Sahih: Surah Al-Fatihah as the foundational spiritual treasure.\n"
        "- Bestowing eternal spiritual wealth that dwarfs all temporal empires and possessions."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("54. Forbidding Covetous Gaze Toward Transience", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Do not strain your eyes toward what We have bestowed upon categories of deniers.'\n"
        "- Worldly luxuries are fleeting, transient ornaments given to test human hearts.\n"
        "- Guarding the heart from envy, consumerist covetousness, and spiritual distraction."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("55. Lowering the Wing of Tenderness to the Believers", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Do not grieve over them, and lower your wing of humility to the believers.'\n"
        "- Treating the impoverished, vulnerable righteous with profound warmth and shelter.\n"
        "- The hallmark of prophetic leadership: tenderness to the faithful, independence from elites."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("56. Proclaiming the Uncompromising Warning", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'And say: Indeed, I am the clear, unambiguous warner' (An-Nadheeru al-mubeen).\n"
        "- Uncompromising clarity in warning humanity of the consequences of polytheism.\n"
        "- Confronting those who fragmented divine revelation into arbitrary sects (Al-Muqtasimeen)."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 8: PROCLAIMING THE TRUTH & THE MEDICINE FOR THE CONSTRICTED HEART
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        8, 8,
        "PROCLAIMING THE TRUTH & THE MEDICINE FOR THE CONSTRICTED HEART",
        "Pillars 15 & 16: Fasda' Bima Tu'mar, Divine Sufficiency, Tasbih, Sujood & Al-Yaqeen",
        "PLATE 08 : PROCLAMATION & SUJOOD"
    )

    # Column 1: Pillar 15
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 15: SPLITTING THE MESSAGE OPEN & SUFFICIENCY", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Public Proclamation, Inna Kafaynaka & Turning from Mockers", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("57. Splitting Open the Truth: Fasda' Bima Tu'mar", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The revolutionary mandate: 'Proclaim openly and split forth that which you are commanded!'\n"
        "- Breaking the phase of clandestine organization; proclaiming monotheism in the open.\n"
        "- Moral courage confronting hostile cultural and political establishments without fear."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("58. Turning Decisively Away from Polytheist Distractions", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'And turn away from the polytheists and cynical detractors.'\n"
        "- Conserving spiritual energy; refusing to be dragged into circular, bad-faith debates.\n"
        "- Focusing exclusively on delivering the divine trust with unwavering conviction."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("59. We Suffice You Against Mockers (Inna Kafaynaka)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Divine protection: 'Indeed, We are sufficient for you against the arrogant mockers.'\n"
        "- God undertaking the defense of His messenger against vicious satirists and slanderers.\n"
        "- Historical reality: Every mocking chieftain of Quraysh met an ignominious end."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("60. Inevitable Reckoning for Those Setting False Deities", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Those who set up alongside Allah other fabricated partners and idols.\n"
        "- 'They will come to know with absolute certainty the consequence of their fabrication.'\n"
        "- Reassurance that arrogance against truth is self-terminating and ephemeral."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 16
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 16: CONSTRICTED CHEST, SUJOOD & AL-YAQEEN", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Divine Empathy, Tasbih, Sujood & Lifelong Devotion", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("61. Divine Empathy: Knowing the Constriction of Heart", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'And We certainly know that your breast is constricted by what they say.'\n"
        "- Acknowledging the profound emotional toll of slander, mockery, and rejection.\n"
        "- Divine comfort validating human vulnerability without invalidating spiritual strength."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("62. The Primary Antidote: Glorifying with Praise (Tasbih)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'So glorify your Lord with praise' (Fa-sabbih bi-hamdi rabbika).\n"
        "- Reorienting the distressed mind from human insults to transcendent divine majesty.\n"
        "- Tasbih and Hamd transforming acute psychological pain into cosmic serenity."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("63. Physical Posture of Humility: Be Among Prostrators", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'And be of those who prostrate before Him' (Wa kun mina as-sajideen).\n"
        "- Physical prostration as the ultimate therapeutic grounding of the troubled soul.\n"
        "- Nearest to the Lord in Sujood; releasing all worldly constriction into the earth."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 70
    pdf.text("64. Devotion Until the Final Certainty (Al-Yaqeen)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'And worship your Lord until there comes to you the certainty [death].'\n"
        "- Faithfulness as an unbroken lifelong journey, immune to shifting circumstances.\n"
        "- Sealing Surah Al-Hijr with tranquil, steadfast worship until the final veil is lifted."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    pdf.save(OUTPUT_PDF)
    print(f"[OK] Generated {OUTPUT_PDF}")

    # Generate previews
    cmd = ["pdftoppm", "-png", "-r", "150", OUTPUT_PDF, os.path.join(PREVIEWS_DIR, "hijr_page")]
    subprocess.run(cmd, check=True)
    print(f"[OK] Rendered preview images to {PREVIEWS_DIR}")

    # Copy to brain dir
    for i in range(1, 9):
        src_name = f"hijr_page-{i}.png" if os.path.exists(os.path.join(PREVIEWS_DIR, f"hijr_page-{i}.png")) else f"hijr_page-0{i}.png"
        src_path = os.path.join(PREVIEWS_DIR, src_name)
        dst_path = os.path.join(brain_dir, f"hijr_page-{i}.png")
        if os.path.exists(src_path):
            shutil.copyfile(src_path, dst_path)
            print(f"[OK] Copied {src_name} -> {dst_path}")

if __name__ == "__main__":
    build_hijr_pdf()
