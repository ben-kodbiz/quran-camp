#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-An'am Master Landscape Mindmap PDF CompilerStrict Standardization:
- Title: Surah Al-An'am — Master Landscape Mindmap
- Zero Ayah Numbers in titles/headers/cards
- Zero mention of external speaker names; 100% Huurs Studio & Sunni source discipline
- Thematic sequence purity
- 8 Landscape Widescreen Pages (792 x 480 pts, 1.65:1 / 16:9 ratio)
- Symmetrical 2-column layout (c1_w = 348, c2_w = 348)
- 16 Thematic Pillars & 64 Structured Cards
"""

import os
import sys
import subprocess
import shutil

sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
OUTPUT_PDF = os.path.join(BASE_DIR, "AL_ANAM_MASTER_MINDMAP.pdf")
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

def build_al_anam_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH AL-AN'AM", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
        # Badges
        pdf.rect(w - 280, h - 32, 175, 20, fill_rgb=NAVY_ELEVATED, stroke_rgb=BORDER_MUTED, line_width=0.8)
        pdf.text(f"PAGE {pnum:02d} / {total_pages:02d}", w - 85, h - 26, font="F2", size=9, rgb=GOLD)

        # Title Sub-header
        pdf.text(title, 32, h - 68, font="F2", size=13.5, rgb=GOLD_LIGHT)
        badge_str = f"[{section_badge}]"
        badge_w = len(badge_str) * 6.1
        pdf.text(badge_str, (w - 32) - badge_w, h - 68, font="F2", size=10.5, rgb=GOLD)
        
        pdf.text(subtitle, 32, h - 84, font="F1", size=8.5, rgb=TEXT_MUTED)
        pdf.line(32, h - 92, w - 32, h - 92, stroke_rgb=BORDER_MUTED, line_width=0.7)

        # Bottom Footer Bar
        pdf.rect(0, 0, w, 28, fill_rgb=NAVY_CARD)
        pdf.line(0, 28, w, 28, stroke_rgb=BORDER_MUTED, line_width=0.8)
        pdf.text("READ. REFLECT. RETURN.  *  SUNNI ISLAMIC SOURCE DISCIPLINE  *  MUTAWATIR TRANSMISSION", 32, 11, font="F1", size=7.2, rgb=TEXT_MUTED)
        pdf.text("AUTHENTICATED EXEGESIS (TABARI * IBN KATHIR * QURTUBI * RAZI)", w - 340, 11, font="F2", size=7.0, rgb=GOLD)

    # Column geometry
    c1_x = 32
    c2_x = 412
    c1_w = 348
    c2_w = 348
    c1_y = 48
    c1_h = 332

    # =========================================================================
    # PAGE 1: COSMIC CREATION & THE KEYS OF THE UNSEEN
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 8,
        "COSMIC CREATION & THE KEYS OF THE UNSEEN",
        "Pillars 1 & 2: Primordial Creation, Al-Qahir Transcendence, Mafatih al-Ghayb & The Falling Leaf",
        "PLATE 01 : CREATION & OMNISCIENCE"
    )

    # Column 1: Pillar 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 1: PRIMORDIAL CREATION & SKEPTICISM", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Cosmic Architecture, Clay Genesis & Demand for Miracles", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. Divine Architecture: Darkness & Light", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Praise be to Allah who originated heavens, earth, darkness, and light ex nihilo.\n"
        "- Darkness mentioned in the plural (Zulumat); truth and light always in the singular.\n"
        "- Refuting dualistic philosophies: Setting up equals (Ya'diloon) is cosmic absurdity."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Creation from Clay & The Appointed Term", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Humankind originated from terrestrial clay; life bound to an appointed lifespan (Ajal).\n"
        "- A second term known exclusively to Him: The predetermined hour of resurrection.\n"
        "- Skepticism condemned: Despite manifest mortal boundaries, deniers continue to doubt."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Demand for Sensory Angels & Paper Books", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Even if a physical parchment descended from heaven, skeptics would dismiss it as sorcery.\n"
        "- Demands for visible angels refuted: An angel appearing would seal immediate judgment.\n"
        "- Were an angel sent as an emissary, he would have appeared in mortal human clothing."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Al-Qahir: Sovereign Might Over Creation", c1_x + 12, y_c, font="F2", size=8, rgb=CYAN)
    t = (
        "- He is the Irresistible Subduer (Al-Qahir) established supreme above all His servants.\n"
        "- If Allah touches you with adversity, none can remove it except Him alone.\n"
        "- If He touches you with good, He is over all things competent; the Wise, the Aware."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 2: MAFATIH AL-GHAYB: DIVINE OMNISCIENCE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("The Keys of the Unseen, Falling Leaves & Nocturnal Recall", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("5. The Keys of the Unseen: Known Only to Him", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- With Him are the Keys of the Unseen (Mafatih al-Ghayb); none knows them except He.\n"
        "- Authenticated Sunnah enumerates five: The Hour, rain, womb secrets, morrow, and death.\n"
        "- Sovereign knowledge encompasses everything upon the dry land and in the fathomless ocean."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("6. The Falling Leaf & Hidden Grain in Darkness", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Not a single leaf drops in any forest or mountain without His specific awareness.\n"
        "- Not a seed hidden in subterranean subterranean earth, nor anything moist or dry escapes.\n"
        "- Every microscopic motion is recorded in an infallible Preserved Register (Kitabin Mubeen)."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("7. Nocturnal Recall: Sleep as Temporary Death", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- He takes your souls by night (in sleep) and knows whatever deeds you commit by day.\n"
        "- Awakening humanity each morning until an appointed lifespan is fully realized.\n"
        "- Sleep serves as a daily living demonstration of the ease and reality of resurrection."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("8. Al-Hisab: Swift Reckoner of All Existence", c2_x + 12, y_c, font="F2", size=8, rgb=PURPLE)
    t = (
        "- When death approaches any servant, angelic messengers take his soul without neglect.\n"
        "- Returned unto Allah, their true Sovereign Master; to Him alone belongs all ultimate judgment.\n"
        "- Sovereign finality: He is the swiftest of all reckoners across entire cosmic creation."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 2: PROPHETIC CONSOLATION & THE CRUCIBLE OF DENIAL
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 8,
        "PROPHETIC CONSOLATION & THE CRUCIBLE OF DENIAL",
        "Pillars 3 & 4: Prophetic Solace, Futile Regret at the Fire, The Deception of Plenty & Path of Criminals",
        "PLATE 02 : CRUCIBLE OF DENIAL"
    )

    # Column 1: Pillar 3
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 3: THE CONSOLATION OF TRUTH & HUMILIATION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Denying Signs, Not the Prophet, The Fire's Edge & Dunya's Game", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("9. Consoling the Prophet: They Reject God's Signs", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Divine solace to the Prophet: We know that what they say grieves your tender heart.\n"
        "- In reality, they do not consider you a liar; rather, the unjust reject the signs of God.\n"
        "- Past messengers endured rejection and persecution with patience until divine victory arrived."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("10. The Futile Wish at the Fire: If Only We Returned!", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Standing before the Fire in horror: 'If only we could be returned to worldly life!'\n"
        "- Pleading to become believers, yet exposed as congenital liars driven by acute panic.\n"
        "- Divine diagnosis: Even if returned, they would inevitably revert to what was forbidden."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("11. Dunya as Play and Amusement: The Real Abode", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Worldly existence is nothing but fleeting play (La'ib) and distraction (Lahw).\n"
        "- The home of the Hereafter is incomparably superior for those who possess authentic Taqwa.\n"
        "- Rhetorical piercing: 'Will you not then use your intellect and reason?'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("12. The Trial of Hardship: Why Not Humble Themselves?", c1_x + 12, y_c, font="F2", size=8, rgb=EMERALD)
    t = (
        "- Nations before you were afflicted with poverty and illness so that they might humble themselves.\n"
        "- Tragedy of arrogance: When hardship struck, their hearts hardened instead of softening.\n"
        "- Satan adorned their corrupt deeds, blinding their moral faculties from seeking repentance."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 4
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 4: THE SUDDEN GRIP & SANCTUARY OF HUMBLE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Istidraj Deception, Rooting Out Tyranny & Sabeel al-Mujrimeen", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("13. The Deception of Plenty: Opening All Doors", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- When they forgot what they were reminded of, We opened to them gates of every luxury.\n"
        "- Until, as they rejoiced in their material abundance, We seized them suddenly in despair.\n"
        "- The spiritual law of Istidraj: Ungrateful prosperity precedes catastrophic divine collapse."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("14. Radical Severance: Cutting Roots of Oppressors", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- The remnant of the people who committed tyranny was utterly severed and eradicated.\n"
        "- Concluding cosmic doxology: 'And praise be to Allah, Lord of all the worlds!'\n"
        "- Divine justice cleanses the earth of persistent oppressors who terrorize creation."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("15. Sanctuary of Humble: Repel Not Morning Callers", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Explicit divine order: Never dismiss those who call upon their Lord morning and evening.\n"
        "- Sincere seekers desiring only His Face; worldly elites have no claim to expel them.\n"
        "- Social egalitarianism of Islam: Spiritual sincerity outranks tribal lineage and wealth."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("16. Sabeel al-Mujrimeen: Path of Criminals Distinct", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD)
    t = (
        "- Thus We explain the signs in detail so that the pathway of criminals is made plain.\n"
        "- Epistemic clarity: Righteousness cannot be distinguished without exposing corruption.\n"
        "- Rebuffing compromises: Refusing to follow arbitrary passions that contradict truth."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 3: CELESTIAL EPISTEMOLOGY & IBRAHIM'S DIALECTIC
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 8,
        "CELESTIAL EPISTEMOLOGY & IBRAHIM'S DIALECTIC",
        "Pillars 5 & 6: Ibrahim's Deconstruction of Astral Worship, La Uhibbul-Afileen & The Citadel of Security (Al-Amn)",
        "PLATE 03 : CELESTIAL EPISTEMOLOGY"
    )

    # Column 1: Pillar 5
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 5: IBRAHIM'S DECONSTRUCTION OF ASTRAL DEITIES", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Stars, Moon, Sun & The Golden Principle: La Uhibbul-Afileen", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("17. Turning Away from Cynical Mockery of Truth", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- When you see those who engage in mockery of Our verses, turn away until they change topic.\n"
        "- If Satan causes you to forget, do not sit after remembering with the unjust wrongdoers.\n"
        "- Intellectual and spiritual hygiene: Guarding the heart against cynical sarcasm."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("18. The Star Rises: Can a Setting Body Be Divine?", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- As darkness engulfed him, Ibrahim beheld a glittering celestial planet/star.\n"
        "- Postulating the opponent's premise: 'Is this my Lord?' testing its metaphysical reality.\n"
        "- As the star descended below the horizon, the premise collapsed through visible motion."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("19. The Radiant Moon & Blazing Sun: Contingency", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Beholding the moon rising in radiance; yet when it waned and set, contingency was proved.\n"
        "- Beholding the sun blazing across the horizon: 'This is greater!' Yet it set into night.\n"
        "- Celestial luminaries are bound by physical laws; they are created signs, not gods."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("20. La Uhibbul-Afileen: 'I Love Not That Which Sets!'", c1_x + 12, y_c, font="F2", size=8, rgb=ROSE)
    t = (
        "- The liberating epistemological axiom: The heart cannot anchor upon what disappears.\n"
        "- Setting bodies prove their non-divinity; true devotion belongs to the Permanent Originator.\n"
        "- Total disavowal: 'O my people, indeed I am free from all that you associate with God!'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 6
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 6: CITADEL OF SECURITY & PURE CREED", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Turning to Fatir as-Samawat, Freedom from Fear & Hujjatullah", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("21. Wajjahtu Wajhiya: Total Consecration to Creator", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'I have turned my face toward Him who originated the heavens and earth, purely upright.'\n"
        "- Rejection of all polytheistic compromises: 'And I am not of those who associate partners.'\n"
        "- Complete orientation of heart and soul to the Transcendent Maker of cosmic order."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("22. Confronting Fear: Who Has Greater Right to Peace?", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- His people argued with him; Ibrahim replied: 'Do you argue with me concerning Allah?'\n"
        "- 'How should I fear what you associate, when you fear not associating partners with God?'\n"
        "- Piercing challenge: Which of the two parties possesses greater right to absolute security?"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("23. Tainting Not Faith with Dhulm: Shirk as Injustice", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Those who believe and taint not their faith with Dhulm—for them is absolute security (Al-Amn).\n"
        "- Sahih hadith clarification: Dhulm here is Shirk, as Luqman said: 'Shirk is a monstrous wrong.'\n"
        "- The psychological reward of pure Tawhid: Inner tranquility and infallible divine guidance."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("24. Hujjatullah: Decisive Divine Proof Bestowed", c2_x + 12, y_c, font="F2", size=8, rgb=CYAN)
    t = (
        "- That was Our decisive argument (Hujjatuna) which We gave to Ibrahim against his people.\n"
        "- We raise in degrees whom We will; indeed, your Lord is All-Wise and All-Knowing.\n"
        "- Intellectual and prophetic triumph of monotheism over astrology and pagan superstition."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 4: PROPHETIC GOLDEN CHAIN & THE CRITERION OF TRUTH
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 8,
        "THE PROPHETIC GOLDEN CHAIN & THE CRITERION OF TRUTH",
        "Pillars 7 & 8: The Constellation of 18 Prophets, Fa-bihudahumu-qtadih, Slander on Revelation & Slanderers' Agony",
        "PLATE 04 : THE PROPHETIC CHAIN"
    )

    # Column 1: Pillar 7
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 7: THE PROPHETIC CONSTELLATION & MANDATE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("18 Named Prophets, Unified Lineage & The Duty of Emulation", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("25. The Golden Lineage: Patriarchs & Rulers", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Ibrahim blessed with Ishaq and Ya'qub; Nuh guided previously in ancient generation.\n"
        "- Prophetic leaders and kings: Dawud, Sulayman, Ayyub, Yusuf, Musa, and Harun.\n"
        "- All blessed with wisdom, moral fortitude, and victory: 'Thus do We reward the righteous.'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("26. Ascetic Emissaries: Zakariyya, Yahya, Isa & Ilyas", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Ascetic masters of prayer and purity: Zakariyya, Yahya, Isa, and Ilyas.\n"
        "- All affirmed as belonging to the righteous (As-Salileen), dedicated to unceasing worship.\n"
        "- Global heralds: Isma'il, Al-Yasa' (Elisha), Yunus, and Lut—favored over all nations."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("27. Universal Favor: Chosen Above the Nations", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Chosen from their fathers, descendants, and brothers; guided to the One Straight Path.\n"
        "- Divine protection: That is the guidance of Allah by which He guides whom He wills.\n"
        "- Severe warning: If even they had committed Shirk, all their great deeds would have perished."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("28. Fa-bihudahumu-qtadih: Follow Their United Guidance", c1_x + 12, y_c, font="F2", size=8, rgb=PURPLE)
    t = (
        "- 'Those are the ones whom Allah has guided, so by their guidance be guided!'\n"
        "- The Prophet Muhammad commanded to follow the unified monotheistic standard of all prophets.\n"
        "- Pure mission: 'I ask of you no monetary fee for this; it is but a reminder to the worlds.'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 8
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 8: REVEALING SCRIPTURE & SLANDERERS' AGONY", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Musa's Torah, Blessed Qur'an & The Agony of Death Throes", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("29. Diminishing God: Claiming No Scripture Sent", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- They did not appraise Allah with true appraisal when they said: 'Allah revealed nothing.'\n"
        "- Decisive historical counter-question: 'Who revealed the scripture that Musa brought?'\n"
        "- Bringing light and guidance to humanity, which they put into parchments hiding much."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("30. The Light of Musa: Knowledge Formerly Unknown", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Taught through revelation that which neither you nor your ancestral fathers knew.\n"
        "- Divine dismissal of obstinacy: 'Say: Allah [revealed it]!' then leave them to play in folly.\n"
        "- Revelation is the supreme conduit of objective truth across all human history."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("31. Mubarakun Musaddiq: Blessed Confirming Qur'an", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- And this is a blessed Book We have sent down, confirming that which preceded it.\n"
        "- Revealed to warn the Mother of Cities (Makkah) and all civilization around its periphery.\n"
        "- Those who believe in the Hereafter believe in it and preserve their daily prayers."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("32. Death Throes of Slanderers: Angels Strike", c2_x + 12, y_c, font="F2", size=8, rgb=EMERALD)
    t = (
        "- Who is more unjust than one who invents lies against Allah or falsely claims revelation?\n"
        "- If only you could see when the unjust are in death agonies, angels stretching forth hands:\n"
        "- 'Surrender your souls! Today you are awarded the humiliating punishment for your lies!'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 5: COSMIC SIGNS, VEGETATION & THE SOLITARY RETURN
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        5, 8,
        "COSMIC SIGNS, VEGETATION & THE SOLITARY RETURN",
        "Pillars 9 & 10: Furada Solitary Reckoning, Faliqul-Habbi Seeds, Cleaving Dawn & The Ripening Fruits",
        "PLATE 05 : SIGNS & SOLITARY RETURN"
    )

    # Column 1: Pillar 9
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 9: SOLITARY RECKONING & CLEAVER OF SEEDS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Furada Solitary Arrival, Severed Ties & The Sprouting Grain", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("33. Furada: Returning Solitary as Created", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'And you have returned to Us solitary (Furada), just as We created you the first time.'\n"
        "- All material fortunes, wealth, and status left completely behind your back on earth.\n"
        "- Stripped of earthly illusions, facing absolute eternal accountability before the Creator."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("34. Severed Ties: Vanishing False Intercessors", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'We see not with you your intercessors whom you claimed were partners with Allah.'\n"
        "- All mythological connections severed; all fabricated illusions vanish into nothingness.\n"
        "- The total collapse of polytheistic dependency structures on the Day of Resurrection."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("35. Faliqul-Habbi: Cleaving Grain and Date Seed", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Indeed, Allah is the Cleaver of the grain and date stone (Faliqul-Habbi wan-Nawa).\n"
        "- He brings forth the living from the dead, and brings forth the dead from the living.\n"
        "- That is Allah! How then are you deluded and turned away from His glorious reality?"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("36. Faliqul-Isbah: Slicing the Radiance of Dawn", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD)
    t = (
        "- Cleaver of the daybreak (Faliqul-Isbah), splitting cosmic darkness with morning light.\n"
        "- Appointed the night for rest and tranquility, and the sun and moon for precise calculation.\n"
        "- That is the flawless determination of the Exalted in Might, the All-Knowing."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 10
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 10: COSMIC CALENDARS & MIRACLES OF WATER", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Navigational Stars, Descending Rain & Botanical Ripening", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("37. Celestial Stars: Beacons in Ocean & Desert", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- He placed the stars for you that you may navigate by them through darkness of land and sea.\n"
        "- Infallible cosmic compass: Guiding travelers across trackless wastes and ocean voyages.\n"
        "- We have detailed the signs for a people who possess knowledge and reflective intellect."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("38. Nafsin Wahidah: Single Origin & Repositories", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- It is He who produced you all from a single soul (Nafsin Wahidah); a shared origin.\n"
        "- Designated a place of dwelling on earth (Mustaqarr) and a repository in graves (Mustawda').\n"
        "- We have detailed the signs for a people who understand the deeper purpose of existence."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("39. Descending Rain: Olives, Palms & Pomegranates", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Sending down water from heaven producing lush vegetation and thick-clustered dates.\n"
        "- Orchards of grapes, olives, and pomegranates—botanically resembling yet distinct in taste.\n"
        "- Diversity of chemical synthesis and sweetness springing from identical soil and water."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("40. Look Upon the Fruit: Ripening Signs for Faith", c2_x + 12, y_c, font="F2", size=8, rgb=ROSE)
    t = (
        "- Contemplate its fruit when it bears fruit and when it ripens into rich nourishment.\n"
        "- Biological transition from bitter unformed matter into sweet, life-sustaining sustenance.\n"
        "- Indeed, in that are unmistakable signs for a people who truly believe in the Divine Maker."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 6: TRANSCENDENT ESSENCE & ETHICAL POLEMICS
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        6, 8,
        "TRANSCENDENT ESSENCE & ETHICAL POLEMICS",
        "Pillars 11 & 12: Tanzih Transcendence, La Tudrikuhul-Absar, Civil Propriety & Deceptive Adorned Speech",
        "PLATE 06 : TRANSCENDENCE & ETHICS"
    )

    # Column 1: Pillar 11
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 11: TANZIH: TRANSCENDENCE BEYOND SENSES", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Badi'us-Samawat, Eradicating Partners & La Tudrikuhul-Absar", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("41. Fabricating Partners: Attributing Jinn & Sons", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Rebutting the pagans who attributed the jinn as partners with Allah, though He created them.\n"
        "- Falsely imputing sons and daughters unto Him without any knowledge or scriptural authority.\n"
        "- Sublime exaltation: 'Exalted and Transcendent is He above what they falsely describe!'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("42. Badi'us-Samawat: Originator Without Equal", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Originator of the heavens and the earth (Badi') without preexisting model or material.\n"
        "- 'How could He have a child when He has no mate, and He created everything?'\n"
        "- And He is knowing of all things: Self-sufficient Lord devoid of physical genealogy."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("43. La Tudrikuhul-Absar: Incomprehensible Majesty", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'No vision can encompass Him (La Tudrikuhul-Absar), but He encompasses all vision.'\n"
        "- Negates comprehensive encompassing (Ihatah); does not negate believers gazing in Akhirah.\n"
        "- Absolute transcendence: His Infinite Majesty cannot be circumscribed by created eyes."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("44. Al-Lateef al-Khabeer: The Subtle, The Fully Aware", c1_x + 12, y_c, font="F2", size=8, rgb=CYAN)
    t = (
        "- And He is the Most Subtle (Al-Lateef), discerning the most imperceptible realities.\n"
        "- The All-Aware (Al-Khabeer), fully cognizant of the secret thoughts within human chests.\n"
        "- Enlightenment has come from your Lord; whoever sees benefits himself, whoever blinds bears it."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 12
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 12: ETHICS OF DISCOURSE & ADORNED LIES", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Sadd al-Dhara'i', Ornate Rhetoric of Devils & Supreme Arbiter", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("45. Civil Propriety: Revile Not Their Deities", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Do not insult those whom they invoke besides Allah, lest they insult Allah in enmity.'\n"
        "- Juristic foundation of Sadd al-Dhara'i': Prohibiting permissible acts that cause greater evil.\n"
        "- High civil ethics: Persuasion conducted through reason and evidence, not vulgar mockery."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("46. Retaliatory Blasphemy: Preventing Slander", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Provoking hostile deniers leads to reciprocal blasphemy against the Lord of the worlds.\n"
        "- Thus have We made attractive to every community their deeds; then to Him is their return.\n"
        "- Maintaining the sacred dignity of God's name above the cheap fray of polemical shouting."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("47. Shayateen al-Ins wal-Jinn: Ornate Speech", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Devils among humans and jinn inspiring one another with adorned speech of delusion.\n"
        "- Intellectual seduction: Falsehood packaged in seductive, sophisticated philosophical rhetoric.\n"
        "- So leave them and whatever lies they fabricate; truth stands independent of propaganda."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("48. Seeking None Other Than Allah as Arbiter", c2_x + 12, y_c, font="F2", size=8, rgb=PURPLE)
    t = (
        "- 'Shall I seek other than Allah as judge (Hakaman) when He revealed the Book explained?'\n"
        "- Those to whom We gave the scripture know it is revealed from your Lord in truth.\n"
        "- Concluding resolve: 'So never be among the doubters!'—Divine sovereignty in arbitration."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 7: THE DIVINE CODE, COMPASSION & PURIFIED SUSTENANCE
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        7, 8,
        "THE DIVINE CODE, COMPASSION & PURIFIED SUSTENANCE",
        "Pillars 13 & 14: Tammat Kalimatu Rabbik, Danger of Majorities, Reborn Light & Eradication of Infanticide",
        "PLATE 07 : DIVINE CODE & COMPASSION"
    )

    # Column 1: Pillar 13
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 13: PERFECTION OF THE WORD & PARABLE OF LIGHT", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Sidqan wa 'Adla, The Treachery of Majorities & Spiritual Resurrection", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("49. Tammat Kalimatu Rabbika: Truth & Justice", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'And the word of your Lord has been fulfilled in truth (Sidqan) and in justice ('Adla).'\n"
        "- Complete in historical narrative and truth; equitable in all legal commandments and limits.\n"
        "- Inviolability of revelation: None can alter His eternal words, and He is Hearing and Knowing."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("50. The Treachery of Majority: Crowds Mislead", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'If you obey most of those upon the earth, they will mislead you from the path of Allah.'\n"
        "- Human consensus is no measure of truth; crowds follow nothing except unverified conjecture.\n"
        "- Your Lord knows best who strays from His path, and He knows best who is rightly guided."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("51. From Death to Light: Parable of Reborn Believer", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Is one who was spiritually dead, whom We brought to life and gave a light to walk among men,\n"
        "- Like one who is trapped in multi-layered darkness from which he cannot ever emerge?\n"
        "- Revelation transforms the dead soul into an illuminated, radiant guide for civil society."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("52. The Constricted Chest: Climbing Into the Sky", c1_x + 12, y_c, font="F2", size=8, rgb=EMERALD)
    t = (
        "- Whomever Allah wills to guide, He expands his chest to embrace the peace of Islam.\n"
        "- Whomever He allows to stray, He makes his chest tight and constricted as if climbing the sky.\n"
        "- Profound psychological insight: Rejection of truth creates suffocating existential constriction."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 14
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 14: ABOLISHING PAGAN TABOOS & INFANTICIDE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Dar as-Salam, Abolishing Daughter-Slaughter & Livestock Purity", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("53. Dar as-Salam: The Abode of Inviolate Peace", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- And this is the path of your Lord, leading straight; We have detailed the signs.\n"
        "- For them will be the Abode of Peace (Dar as-Salam) with their Lord in the Hereafter.\n"
        "- And He will be their loving protecting Ally because of the righteous deeds they worked."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("54. The Criminality of Infanticide: Slaying Children", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Condemning pagan fathers whose idols adorned the slaughter of their innocent children.\n"
        "- Sacrificing daughters out of fear of shame or economic poverty; ruined in Dunya and Akhirah.\n"
        "- Lost indeed are those who murdered their children in ignorance, fabricating lies against God."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("55. Fabricated Dedications: Crop & Cattle Superstitions", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Rebutting arbitrary dedications: 'This is for Allah, and this is for our fabricated partners.'\n"
        "- What belongs to partners reaches not Allah, but what belongs to Allah reaches their idols.\n"
        "- Evil is their judgment: Decimating the economic superstitions of pagan priesthoods."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("56. The Eight Pairs of Livestock: Refuting Fake Harams", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD)
    t = (
        "- Eight pairs of livestock: Sheep, goats, camels, and cattle created as divine sustenance.\n"
        "- Sarcastic challenge: 'Did He forbid the two males or two females or what the wombs contain?'\n"
        "- Dietary boundaries simplified: Maytah, running blood, swine, and unslaughtered meat alone."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 8: THE MASTER DECALOGUE & THE SUPREME DECLARATION
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        8, 8,
        "THE MASTER DECALOGUE & THE SUPREME DECLARATION",
        "Pillars 15 & 16: Al-Wasaya al-'Ashr (The Ten Commandments), Siratee Mustaqeema & Inna Salatee wa Nusukee",
        "PLATE 08 : THE MASTER DECALOGUE"
    )

    # Column 1: Pillar 15
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 15: AL-WASAYA AL-'ASHR: QURANIC DECALOGUE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("The Universal Charter of Ethics, Sanctity of Life & Full Weights", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("57. The Universal Covenant: Tawhid & Parents", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Say: Come, I will recite what your Lord has prohibited to you: Join no partners with Him.'\n"
        "- Command of filial devotion: Practice Ihsan toward parents in speech, sustenance, and care.\n"
        "- Foundational bedrock: The moral order begins with pure monotheism and parental reverence."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("58. Economic Sanctity of Children & Purity", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Do not kill your children out of poverty; We provide for you and for them.'\n"
        "- Absolute prohibition of shameful deeds (Fawahish), whether open or secret.\n"
        "- Eliminating the twin poisons of infanticide and sexual exploitation from civilization."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("59. Sanctity of Soul, Orphan Wealth & Justice", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Kill not the soul which Allah has sanctified, except by legal right.'\n"
        "- 'Approach not the orphan's property except to enhance it until maturity.'\n"
        "- 'Give full measure and weight with justice; when you speak, be fair even against relatives.'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("60. Hadha Siratee Mustaqeema: The One Pathway", c1_x + 12, y_c, font="F2", size=8, rgb=ROSE)
    t = (
        "- 'And this is My path, which is straight, so follow it; and follow not divergent pathways.'\n"
        "- The Prophet drew a straight line in the dust, and lines branching off it, warned of devils.\n"
        "- Divergent sect pathways scatter you away from His road: The covenant of unified truth."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 16
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 16: UNIVERSAL SURRENDER & EARTH'S STEWARDS", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Tenfold Grace, Inna Salatee wa Nusukee & Khala'if al-Ard", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("61. The Tenfold Bounty: Divine Mercy Multiplied", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Whoever brings a good deed shall receive ten times the like thereof in divine reward.\n"
        "- Whoever brings an evil deed shall not be recompensed except with its exact equivalent.\n"
        "- Divine justice is untainted: 'And they shall not be wronged in the slightest.'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("62. Inna Salatee wa Nusukee: The Master Declaration", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Say: Indeed, my prayer, my sacrifice, my living, and my dying are all for Allah alone.'\n"
        "- 'Lord of all the worlds; no partner has He; and with this I have been commanded.'\n"
        "- 'And I am the first of those who surrender (Muslims)': The supreme manifesto of monotheism."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("63. Bearing No Other's Burden: Personal Responsibility", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Every soul earns only against itself; no bearer of burdens bears the burden of another.\n"
        "- Rejection of inherited sin and collective guilt: Absolute moral individual accountability.\n"
        "- Then to your Lord is your return, and He will inform you concerning all that you disputed."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("64. Khala'if al-Ard: Divine Test of Successorship", c2_x + 12, y_c, font="F2", size=8, rgb=CYAN)
    t = (
        "- It is He who made you successors upon the earth (Khala'if al-Ard), generation after generation.\n"
        "- Raised some of you above others in ranks that He may test you in what He has given you.\n"
        "- Final balance: Indeed, your Lord is swift in retribution, yet He is Forgiving and Merciful."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    pdf.save(OUTPUT_PDF)
    print(f"Successfully generated Surah Al-An'am Master Mindmap PDF: {OUTPUT_PDF}")

    # Generate PNG page previews using pdftoppm
    print("Generating PNG previews...")
    cmd = ["pdftoppm", "-png", "-r", "150", OUTPUT_PDF, os.path.join(PREVIEWS_DIR, "al_anam_page")]
    subprocess.run(cmd, check=True)
    print("PNG previews generated in:", PREVIEWS_DIR)

    # Copy previews to brain directory
    print("Copying previews to brain directory...")
    for f in os.listdir(PREVIEWS_DIR):
        if f.startswith("al_anam_page") and f.endswith(".png"):
            src = os.path.join(PREVIEWS_DIR, f)
            dst = os.path.join(brain_dir, f)
            shutil.copy2(src, dst)
            print(f"  Copied {f} to brain directory.")

if __name__ == "__main__":
    build_al_anam_pdf()
