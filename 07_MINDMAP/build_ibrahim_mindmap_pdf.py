#!/usr/bin/env python3
"""
Huurs Studio - Surah Ibrahim Master Mindmap Vector PDF Generator
16:9 Landscape Widescreen (792 x 480 pt) • 8 Plates • 16 Pillars • 64 Cards
"""

import os
import sys
import subprocess
import shutil

sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
OUTPUT_PDF = os.path.join(BASE_DIR, "IBRAHIM_MASTER_MINDMAP.pdf")
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

def build_ibrahim_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH IBRAHIM", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
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
    # PAGE 1: FROM DARKNESS TO LIGHT & THE VERNACULAR OF PROPHETHOOD
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 8,
        "FROM DARKNESS TO LIGHT & THE VERNACULAR OF PROPHETHOOD",
        "Pillars 1 & 2: Scriptural Teleology, The Language of Messengers & The Days of Allah",
        "PLATE 01 : LIGHT & HISTORY"
    )

    # Column 1: Pillar 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 1: SCRIPTURAL PURPOSE & THE VERNACULAR OF MESSENGERS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Mina az-Zulumat ila an-Noor, Al-'Azeez al-Hameed & Mother Tongues", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. Delivering Humanity from Plural Darknesses", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Opening with Alif-Lam-Ra: A Book revealed to deliver from darknesses to Light.\n"
        "- The plural Zulumat represents manifold errors; singular Noor is unified truth.\n"
        "- Directing mankind to the sovereign path of the Almighty, the Praiseworthy."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("2. The Path of the Exalted, the Praiseworthy", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The divine path belongs to Al-'Azeez (Invincible) and Al-Hameed (Self-Praised).\n"
        "- Sovereign ownership of everything within the heavens and across the earth.\n"
        "- Establishing monotheistic devotion as the sole foundation of spiritual security."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("3. Peril of Loving the World Over the Hereafter", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Severe doom for those preferring transient worldly life over the eternal.\n"
        "- Actively obstructing seekers from the straight path of divine guidance.\n"
        "- Seeking deviousness in truth; wandering in profound, self-inflicted delusion."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("4. The Mother Tongue of Every Divine Messenger", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Universal rule: Every messenger sent in the native tongue of his own people.\n"
        "- Eliminating linguistic ambiguity; truth expounded with crystalline clarity.\n"
        "- Establishing absolute moral responsibility before divine judgment is rendered."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 2
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 2: THE DAYS OF ALLAH (AYYAM ALLAH) & MUSA'S DELIVERANCE", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Historical Deliverance, Pharaonic Trauma & The Grateful Heart", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("5. Musa Dispatched With Clear Signs of Deliverance", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Prophet Musa commissioned to extract Banu Isra'il from darkness to light.\n"
        "- Armed with clear signs of divine majesty to shatter institutional bondage.\n"
        "- Reorienting an enslaved nation toward the worship of the Living God."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("6. The Sacred Mandate to Recall the Days of Allah", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Command: 'Remind them of the Days of Allah (Ayyam Allah).'\n"
        "- Commemorating moments of divine intervention and historical deliverance.\n"
        "- Containing signs for every soul that is immensely patient and grateful."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("7. The Historical Trauma of Pharaonic Oppression", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Recalling Pharaoh's brutal genocide: slaughtering infant sons, enslaving women.\n"
        "- Inflicting humiliating, agonizing torment upon a defenseless populace.\n"
        "- A tremendous trial (Bala'un 'Azeem) testing communal faith to its limits."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("8. The Sea Parted & Unmerited Sovereign Grace", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The miraculous parting of the sea and destruction of the Pharaonic host.\n"
        "- Historical liberation is an unearned divine gift demanding eternal gratitude.\n"
        "- The warning: Forgetting past deliverance breeds spiritual entitlement and rot."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 2: THE EQUATION OF GRATITUDE & THE ASH OF FALSE DEEDS
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 8,
        "THE EQUATION OF GRATITUDE & THE ASH OF FALSE DEEDS",
        "Pillars 3 & 4: The Law of Increase, Absolute Self-Sufficiency & Deeds Blown in Storms",
        "PLATE 02 : GRATITUDE & DEEDS"
    )

    # Column 1: Pillar 3
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 3: GRATITUDE PROCLAIMED (LA'IN SHAKARTUM) & SELF-SUFFICIENCY", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("The Immutable Law of Increase, Ingratitude & The Independence of God", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("9. The Universal Proclamation: La'in Shakartum", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Divine proclamation: 'If you are grateful, I will surely grant you increase.'\n"
        "- Gratitude (Shukr) as an ontological law preserving and expanding blessings.\n"
        "- Stern warning: Ingratitude (Kufr an-Ni'mah) triggers severe divine punishment."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("10. The Tripartite Anatomy of True Gratitude", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Acknowledging in the heart that all blessings originate solely from God.\n"
        "- Expressing continuous, humble verbal praise upon the tongue without boast.\n"
        "- Deploying physical faculties and wealth strictly in divine obedience."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("11. The Absolute Independence of the Creator", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Musa declaring: If all humanity disbelieves, God's kingdom is undiminished.\n"
        "- Allah is intrinsically Self-Sufficient (Ghaniyyun) and Praiseworthy (Hameed).\n"
        "- Human worship benefits only the worshiper; God has no need of creation."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("12. The Forgotten Ruins of Past Civilizations", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Historical warnings: The chronicles of Nuh, 'Ad, Thamud, and vanished races.\n"
        "- Generations known only to Allah, who dismissed their messengers with arrogance.\n"
        "- Imperial glory dissolves into dust when communities defy moral law."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 4
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 4: PROPHETIC DOUBTS & DEEDS BLOWN LIKE STORMY ASHES", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Biting Fingers in Defiance, Cosmic Originator & Stormy Wind Parable", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("13. Biting Hands in Mockery & Suspicious Skepticism", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Deniers placing hands over mouths in cynical mockery of divine messages.\n"
        "- Proclaiming obstinate doubt: 'We disbelieve in that with which you were sent.'\n"
        "- Cynicism masking deep internal terror of moral accountability before God."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("14. Is There Any Doubt Concerning the Originator?", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Prophetic retort: 'Afee Allahi shakkun Fatiri as-samawati wal-ard?'\n"
        "- The existence of the Originator is self-evident across the entire cosmos.\n"
        "- Calling creation to divine forgiveness and postponing until an appointed term."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("15. Prophetic Reliance in the Face of Persecution", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Why should we not rely upon Allah when He has guided us to our ways?'\n"
        "- Unshakable prophetic patience under threats of exile, torture, and murder.\n"
        "- Anchoring the soul in divine providence against hostile worldly majorities."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("16. Deeds Blown Away Like Stormy Ashes", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The deeds of disbelievers are like ashes on a rock during a hurricane (Reeh 'Asif).\n"
        "- Works severed from Tawhid lack ontological weight, scattered into nothingness.\n"
        "- Complete spiritual bankruptcy on the Day of Judgment; zero trace recovered."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 3: TYRANTS' ULTIMATUMS & THE BITTER DRAUGHT OF SEDEED
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 8,
        "TYRANTS' ULTIMATUMS & THE BITTER DRAUGHT OF SEDEED",
        "Pillars 5 & 6: Totalitarian Threats, Divine Promise & The Horrors of Jahannam",
        "PLATE 03 : TYRANTS & SADEED"
    )

    # Column 1: Pillar 5
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 5: EXILING THE PROPHETS & DIVINE REASSURANCE TO MESSENGERS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Coercive Ultimatums, Destruction of Oppressors & Inheriting the Land", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("17. The Tyrants' Binary Ultimatum of Exile", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Totalitarian demand: 'We will expel you from our land, or you must return!'\n"
        "- Authoritarian regimes cannot tolerate incorruptible moral independence.\n"
        "- The perpetual clash between secular coercion and sacred conviction."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("18. Divine Reassurance: Oppressors Will Be Destroyed", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Revelation inspiring prophets: 'We will surely destroy the wrongdoers.'\n"
        "- Worldly oppression has an unalterable expiration date calibrated by God.\n"
        "- The promise of divine vindication comforting the persecuted minority."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("19. Inheriting the Earth After the Oppressors", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'And We will surely settle you in the land after them' (Lanuskinannakum).\n"
        "- Earthly stewardship is the heritage of those who revere standing before God.\n"
        "- Reverence of the Divine Court (Khafa Maqamee) as the qualification to lead."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("20. Divine Victory Sought & Every Tyrant Decimated", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Messengers seeking divine victory (Wastaftahoo) when human options closed.\n"
        "- Every stubborn, haughty tyrant (Jabbarin 'Aneed) brought to catastrophic ruin.\n"
        "- Breaking the illusion of worldly invincibility built on weapons and arrogance."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 6
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 6: THE BITTER DRAUGHT OF FESTERING WATER (MA'IN SADEED)", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("The Crucible of Hell, Putrid Drinks & The Lingering Death", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("21. Hellfire Awaiting the Arrogant Tyrant", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Beyond worldly collapse lies Jahannam, confronting the tyrant with truth.\n"
        "- The reversal of status: worldly masters reduced to wretched prisoners.\n"
        "- Total exposure to the horrifying consequences of their earthly cruelties."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("22. The Putrid Draught of Festering Purulence", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Forced to drink boiling, putrid festering liquid (Ma'in Sadeed) in the Fire.\n"
        "- The gruesome embodiment of the foul, toxic corruption they spread on earth.\n"
        "- Repulsive to every sense, yet consumed out of unquenchable, desperate thirst."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("23. The Agony of Swallowing & The Lingering Death", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Gulping down the boiling liquid in agonizing sips (Yatajarra'uh) scarcely swallowed.\n"
        "- Death assaulting the condemned from every physical direction, yet they cannot die.\n"
        "- Suspended in perpetual torment; stripped of the mercy of cessation or relief."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("24. The Relentless Horizon of Heavy Punishment", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Beyond the torment of putrid drinks lies an intensifying chastisement ('Adhab Ghaleez).\n"
        "- Exacting cosmic justice for every cry of the oppressed they ignored on earth.\n"
        "- The terrifying end of pride that refused to bow to the Lord of the worlds."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 4: THE KHUTBAH OF IBLIS & THE METAPHOR OF THE PURE TREE
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 8,
        "THE KHUTBAH OF IBLIS & THE METAPHOR OF THE PURE TREE",
        "Pillars 7 & 8: Satan's Confession in the Fire & Kalimah Tayyibah Like a Noble Tree",
        "PLATE 04 : IBLIS & PURE TREE"
    )

    # Column 1: Pillar 7
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 7: SATAN'S CONFESSION IN THE FIRE: BLAME YOURSELVES", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("All Exposed, Impotence of Leaders & The Master Betrayer Speaks", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("25. All Humanity Emerging Exposed Before Allah", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- All created beings emerging together before Allah (Barazoo lillahi jamee'an).\n"
        "- Weak followers turning in fury upon arrogant masters who led them astray.\n"
        "- Desperate demands: 'Can you avert from us any fraction of Allah's punishment?'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("26. The Helpless Admission of Arrogant Leaders", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Worldly elites confessing total impotence: 'If God guided us, we would guide you.'\n"
        "- Panic and stoic patience are identical in the Fire; there is zero escape (Mahis).\n"
        "- Shattering the delusion that following popular culture or corrupt leaders shields."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("27. Satan's Sermon When Judgment is Concluded", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Iblis speaking from his pulpit of fire: 'Indeed, Allah promised you the truth.'\n"
        "- 'And I promised you, but I betrayed you' (Wa wa'adtukum fa-akhlaftukum).\n"
        "- The ultimate admission: God's warnings were real; secular seductions were lies."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("28. 'Do Not Blame Me; Blame Your Own Souls!'", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'I possessed no authority over you except that I called, and you responded.'\n"
        "- Stripping humanity of victimhood: Satan had no coercive power, only invitation.\n"
        "- The bitter realization of self-inflicted damnation: 'Do not blame me; blame yourselves.'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 8
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 8: KALIMAH TAYYIBAH: THE PURE TREE ROOTED TO THE SKY", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("The Good Word, Immovable Roots & Continuous Celestial Fruit", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("29. The Divine Parable of the Good Word", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Have you not considered how Allah strikes the parable of Kalimah Tayyibah?\n"
        "- The Good Word is the pure testimony of Tawhid and words of truth and virtue.\n"
        "- The ultimate standard of enduring speech, character, and spiritual reality."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("30. Like a Noble, Radiant Tree (Kashajaratin Tayyibah)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Resembling a magnificent date palm or celestial tree of radiant vitality.\n"
        "- Green, lush, and unwithering; impervious to harsh climates and scorching heat.\n"
        "- Embodying the living heart of the believer whose faith never decays."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("31. Roots Immovable in Bedrock (Asluha Thabit)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Roots anchored deeply into the bedrock of fitrah and divine conviction.\n"
        "- Immune to the violent winds of intellectual doubt, social fashion, and fear.\n"
        "- A stable center that remains unshakeable when worldly systems collapse."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("32. Canopy Piercing the Sky with Perpetual Fruit", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Branches soaring high into the heavens (Far'uha fis-samaa') bearing righteous deeds.\n"
        "- Yielding sweet, nourishing fruit in every single season (Tu'tee ukulaha kulla heen).\n"
        "- Bringing continuous benefit, wisdom, and moral shade to all of humanity."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 5: THE EVIL TREE, DIVINE ANCHORING & DENIERS OF GRACE
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        5, 8,
        "THE EVIL TREE, DIVINE ANCHORING & DENIERS OF GRACE",
        "Pillars 9 & 10: The Uprooted Weed, Al-Qawl ath-Thabit & Trading Blessings for Ruin",
        "PLATE 05 : ANCHORING & RUIN"
    )

    # Column 1: Pillar 9
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 9: THE UPROOTED WEED & FIRM ANCHOR OF THE BELIEVER", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Kalimah Khabeethah, Questioning in the Grave & Firm Conviction", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("33. The Parable of the Evil Word (Kalimah Khabeethah)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The foul word of polytheism, cynicism, and slander like an evil thorn weed.\n"
        "- Uprooted from the surface of the earth (Ijtuth-that), possessing zero root depth.\n"
        "- Hollow, prickly, and unstable; producing only bitterness, poison, and ruin."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("34. Devoid of Any Stability (Ma Laha min Qarar)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Lacking ontological stability; easily toppled and scattered by the slightest breeze.\n"
        "- Ideologies of falsehood make loud, prickly noise but vanish into irrelevance.\n"
        "- Those anchored in falsehood find no peace or enduring foundation in life."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("35. Establishing Believers with the Firm Word", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Allah establishes those who believe with the firm word (Bil-Qawlith-Thabit).\n"
        "- Unwavering spiritual certitude in worldly trials, sickness, and agony of death.\n"
        "- Authenticated in Sahih: Anchored upon the interrogation of Munkar and Nakir."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("36. The Confusion of Oppressors & Sovereign Divine Will", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Allah leaves to stray the oppressors who rejected truth out of stubborn pride.\n"
        "- Divine justice leaving the arrogant to wander blindly in their own confusion.\n"
        "- Allah accomplishes whatever He wills with absolute authority and wisdom."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 10
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 10: TRADING GRACE FOR INGRATITUDE & SETTLING IN THE RUIN", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Dar al-Bawar, Invented Rivals & The Command to Spend Secretly", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("37. Exchanging Divine Blessings for Ingratitude", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Do you not observe those who traded Allah's favors for bitter denial?\n"
        "- Taking the gift of prophetic guidance and weaponizing it into war and pride.\n"
        "- Historical application to the Quraysh elite who led their followers to ruin."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("38. Settling Communities in the Abode of Perdition", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Leading their societies directly into the wretched dwelling of ruin (Dar al-Bawar).\n"
        "- Plunging into Hellfire to burn eternally—a catastrophic, miserable destination.\n"
        "- The terrible consequence when corrupt leaders manipulate vulnerable masses."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("39. Inventing False Rivals to Mislead from the Path", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Fabricating equals and rivals to Allah (Andadan) to justify secular autonomy.\n"
        "- Divine dismissal: 'Enjoy your fleeting worldly pleasures; your return is the Fire!'\n"
        "- Exposing the transience of all systems built in defiance of monotheism."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("40. The Command of Prayer & Secret/Open Generosity", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Instruct My believing servants to establish regular prayer with conscious focus.\n"
        "- Spending from divine provision covertly to guard sincerity and openly to inspire.\n"
        "- Preparing before the arrival of a Day devoid of commerce, bargaining, or friendship."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 6: COSMIC SUBJUGATION & FOUNDATIONS AT THE SACRED VALLEY
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        6, 8,
        "COSMIC SUBJUGATION & FOUNDATIONS AT THE SACRED VALLEY",
        "Pillars 11 & 12: Heavens, Sun & Moon, Innumerable Favors & Ibrahim at Makkah",
        "PLATE 06 : COSMOS & MAKKAH"
    )

    # Column 1: Pillar 11
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 11: CELESTIAL ARCHITECTURE, SOLAR CHARIOTS & BARREN VALLEY", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Creation of Heavens, Rain, Ships, Sun & Moon in Tireless Motion", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("41. The Architecture of Heavens, Earth & Rains", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Allah who created the heavens and earth, sending down life-reviving rains.\n"
        "- Extracting vibrant fruits as sustenance; subjugating ships to traverse oceans.\n"
        "- The seamless integration of cosmological, hydrological, and maritime systems."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("42. Sun and Moon in Continuous Tireless Orbits", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Subjugating the sun and moon in perpetual, tireless motion (Da'ibayn).\n"
        "- Calibrating day and night to sustain biological rhythms, agriculture, and sleep.\n"
        "- Unbroken cosmic service orchestrated solely for the benefit of human life."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("43. Innumerable Blessings Beyond Human Computation", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- He gave you of everything you petitioned or required for life and growth.\n"
        "- 'And if you were to count the blessings of Allah, never could you enumerate them.'\n"
        "- The tragedy of human nature: deeply prone to injustice and ungrateful denial."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("44. The Arrival at the Waterless Desert Canyon", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Prophet Ibrahim settling his infant Isma'il and Hajar in the barren wilderness.\n"
        "- An uncultivated valley without crops (Bi-wadin ghayri dhee zar'in).\n"
        "- Placing his family beside the Sacred House (Baytika al-Muharram) in supreme trust."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 12
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 12: YEARNING HEARTS & THE GIFT OF SONS IN OLD AGE", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Li-Yuqeemu as-Salah, Yearning Hearts (Tahwee) & Sons in Old Age", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("45. The Singular Purpose: Establishing Prayer", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The purpose of Makkah's foundation: 'In order that they establish prayer.'\n"
        "- Subordinating economics, commerce, and settlement to pure worship of God.\n"
        "- Sanctifying geographical space to become the global focal point of prayer."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("46. Hearts of Humanity Yearning Toward Makkah", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Visionary prayer: 'Make hearts among mankind yearn toward them' (Tahwee ilayhim).\n"
        "- Not mere physical travel, but deep spiritual yearning drawing millions of souls.\n"
        "- Providing bountiful fruits to a desert valley as proof of answered prayer."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("47. Divine Omniscience Over the Yearning Heart", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Ibrahim's intimate prayer: 'Our Lord, You know what we hide and what we declare.'\n"
        "- Nothing in the earth or heavens is hidden from the All-Seeing Creator.\n"
        "- Pouring out silent vulnerability before the One who understands without words."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("48. Exultant Gratitude for Isma'il and Ishaq", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Praise be to Allah who granted me in old age Isma'il and Ishaq!'\n"
        "- Overcoming human despair: Offspring granted past 80/90 years to barren parents.\n"
        "- Sealing his praise with certitude: 'Indeed, my Lord is the Hearer of Prayer.'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 7: THE ABRAHAMIC DU'A & THE DELAYED RECKONING
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        7, 8,
        "THE ABRAHAMIC DU'A & THE DELAYED RECKONING",
        "Pillars 13 & 14: The Model Intergenerational Prayer & The Delay of Oppressors",
        "PLATE 07 : DU'A & RECKONING"
    )

    # Column 1: Pillar 13
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 13: THE MODEL PRAYER: ESTABLISHERS OF SALAH & PARENTAL PARDON", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Muqeema as-Salah, Upright Progeny, Filial Pardon & The Final Account", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("49. Pleading for Upright Descendants", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'My Lord, make me an establisher of prayer, and from my descendants.'\n"
        "- The visionary patriarch looking across millennia to protect future generations.\n"
        "- Recognizing prayer as the spiritual anchor preserving family from degradation."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("50. Humility in Pleading: Rabbana wa Taqabbal Du'a", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Sealing the prayer with deep humility: 'Our Lord, and accept my supplication.'\n"
        "- Never feeling entitled to divine favor; approaching the King with reverence.\n"
        "- The model of prophetic supplication combining passionate desire with humility."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("51. The Universal Filial & Communal Supplication", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Our Lord, forgive me and my parents and the believers on the Day of Account.'\n"
        "- Honoring biological parents and uniting the global family of faith in one plea.\n"
        "- The immortal formula recited in the final sitting of every Muslim's prayer."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("52. Solidarity Across Historical Generations", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Connecting the modern believer directly to the heart and tongue of Ibrahim.\n"
        "- Living with an eschatological horizon: Everything oriented toward Yawm al-Hisab.\n"
        "- The triumph of faith uniting generations in a shared covenant of divine mercy."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 14
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 14: DIVINE VIGILANCE: STARING EYES & HURRYING IN PANIC", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Wa La Tahsabanna, Staring Eyes, Outstretched Necks & Hollow Hearts", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("53. Never Think Allah Unaware of the Oppressors", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Thunderous reassurance: 'Never think Allah is unaware of what wrongdoers do.'\n"
        "- Divine patience is never divine neglect; every injustice is logged and measured.\n"
        "- Consolation to the oppressed: No tyrant escapes the sovereign ledger of God."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("54. Postponed Until the Day Eyes Stare in Terror", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- He merely delays them for a Day when eyes freeze in terror (Tashkhasu al-absar).\n"
        "- The unblinking, horrified stare of those who realized their worldly hubris was vanity.\n"
        "- The sudden, irreversible arrival of the ultimate cosmic reckoning."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("55. Rushing Forward with Outstretched Necks & Hollow Hearts", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Resurrected oppressors rushing forward in sheer panic, heads rigidly lifted high.\n"
        "- Gazes frozen, unable to return to themselves; hearts drained and hollow (Hawaa').\n"
        "- The horrifying psychological disintegration of worldly masters before God."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("56. Desperate Pleas for Delay Met with Scorn", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Sinners begging in terror: 'Our Lord, delay us for a short term so we may answer!'\n"
        "- The scathing divine retort: 'Did you not swear before you would face no end?'\n"
        "- The absolute finality of earthly testing: No second chances after the veil parts."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 8: THE TRANSMUTED EARTH & THE FINAL MANIFESTATION
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        8, 8,
        "THE TRANSMUTED EARTH & THE FINAL MANIFESTATION",
        "Pillars 15 & 16: Mountain Conspiracies, The Transmuted Cosmos & Balaghun lin-Nas",
        "PLATE 08 : TRANSMUTED COSMOS"
    )

    # Column 1: Pillar 15
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 15: CONSPIRACIES MOVING MOUNTAINS & SOLEMN RETRIBUTION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Ruins of Antiquity, Mountainous Plots & Allah Never Fails His Promise", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("57. Inhabiting the Ruins of Extinguished Tyrannies", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'You inhabited the dwellings of those who wronged themselves before you.'\n"
        "- Witnessing the archaeological graveyards of past empires, yet failing to learn.\n"
        "- Willful historical blindness: repeating the exact vices that destroyed predecessors."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("58. Conspiracies Engineered to Move Mountains", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- They schemed their plots, but their plotting is audited completely by Allah.\n"
        "- Even if their geopolitical conspiracies were capable of moving mountains.\n"
        "- Human conspiracies are infinitely subordinate to the transcendent decree of God."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("59. Allah Never Fails His Covenant to Messengers", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Never think that Allah will fail in His promise to His messengers.'\n"
        "- Divine attribution: Allah is Almighty (Al-'Azeez), Possessor of Retribution.\n"
        "- The guarantee that truth will triumph and tyranny will face cosmic reckoning."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("60. The Precise Compensation for Every Soul", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Every soul recompensed exactly for what it earned, without fraction of injustice.\n"
        "- Allah is swift in reckoning (Saree'ul-Hisab); the cosmic audit leaves nothing out.\n"
        "- Absolute balance restored across all realms of human history."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 16
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 16: TRANSMUTED EARTH, PITCH GARMENTS & UNIVERSAL MESSAGE", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Yawma Tubaddalu al-Ard, Al-Wahid al-Qahhar, Shackles & Final Balagh", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("61. The Day the Earth and Heavens Are Transmuted", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'On the Day the earth will be replaced by another earth, and the heavens.'\n"
        "- Physical cosmic reconstitution: A pure, level plain stripped of all landmarks.\n"
        "- The dissolution of all earthly geography and temporal political boundaries."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("62. Standing Exposed Before the One, the Subduer", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Humanity emerging from graves, standing bare before Al-Wahid al-Qahhar.\n"
        "- The One, the All-Subduing Lord holding absolute, uncontested dominion.\n"
        "- Total silence across the assembly; all worldly arrogance wiped from existence."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("63. Criminals Bound in Shackles with Garments of Pitch", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- You will see the guilty bound in iron shackles (Muqarraneena fil-asfad).\n"
        "- Garments made of flammable black pitch (Qatiran), faces veiled in fire.\n"
        "- The terrifying physical manifestation of their dark worldly transgressions."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("64. A Decisive Proclamation for All Humanity", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'This Qur'an is a decisive proclamation for mankind' (Hadha balaghun lin-nas).\n"
        "- Revealed to warn humanity, establish pure monotheism, and enlighten intellect.\n"
        "- Sealing Surah Ibrahim with the eternal call to the people of intellect (Ulul-Albab)."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    pdf.save(OUTPUT_PDF)
    print(f"Master Mindmap PDF successfully written to: {OUTPUT_PDF}")

    # Generate preview images for each plate
    print("Generating preview PNGs via pdftoppm...")
    cmd = [
        "pdftoppm",
        "-png",
        "-r", "150",
        OUTPUT_PDF,
        os.path.join(PREVIEWS_DIR, "ibrahim_page")
    ]
    subprocess.run(cmd, check=True)

    # Copy to brain dir
    for i in range(1, 9):
        src_pattern = os.path.join(PREVIEWS_DIR, f"ibrahim_page-{i}.png")
        if not os.path.exists(src_pattern):
            src_pattern = os.path.join(PREVIEWS_DIR, f"ibrahim_page-0{i}.png")
        if os.path.exists(src_pattern):
            dst = os.path.join(brain_dir, f"ibrahim_page-{i}.png")
            shutil.copyfile(src_pattern, dst)
            print(f"Copied {src_pattern} -> {dst}")

if __name__ == "__main__":
    build_ibrahim_pdf()
