#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-A'raf Master Landscape Mindmap PDF CompilerStrict Standardization:
- Title: Surah Al-A'raf — Master Landscape Mindmap
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
OUTPUT_PDF = os.path.join(BASE_DIR, "AL_ARAF_MASTER_MINDMAP.pdf")
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

def build_al_araf_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH AL-A'RAF", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
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
    # PAGE 1: PRIMORDIAL GENESIS, THE REFUSAL OF IBLIS & THE HEAVENLY FALL
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 8,
        "PRIMORDIAL GENESIS, THE REFUSAL OF IBLIS & THE HEAVENLY FALL",
        "Pillars 1 & 2: Divine Revelation, Weighing in Truth, Pride of Iblis & Ambush on the Straight Path",
        "PLATE 01 : GENESIS & DISOBEDIENCE"
    )

    # Column 1: Pillar 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 1: DIVINE REVELATION & OBJECTIVE ACCOUNTABILITY", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("No Constriction in the Chest, Cosmic Scales & Sovereign Seizure", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. Revelation: No Constriction in the Chest", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Alif-Lam-Mim-Sad: A divine Book revealed to guide, admonish, and awaken hearts.\n"
        "- Divine reassurance: Let there be no constriction (Haraj) in the prophetic chest.\n"
        "- Follow what is revealed from your Lord; follow no patron protectors besides Him."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("2. Obliteration of Tyrannical Civilizations", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- How many cities were annihilated when divine retribution seized them suddenly.\n"
        "- Struck down in nocturnal slumber or while relaxing in the heat of midday.\n"
        "- Their only cry when punishment arrived was confession: 'Indeed, we were wrongdoers!'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("3. Universal Interrogation of Messengers & Nations", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Every community will be questioned regarding their reception of divine revelation.\n"
        "- The Messengers will be questioned regarding the conveyance of their trust.\n"
        "- All deeds recounted with infallible divine knowledge; God was never absent."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("4. The Scales of Absolute Truth (Al-Wazn)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The weighing of deeds on that Day is an objective, physical, undeniable reality.\n"
        "- Those whose scales are heavy with righteous deeds achieve eternal triumph.\n"
        "- Those whose scales are light ruin their souls through injustice against divine signs."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 2
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 2: ADAM, IBLIS & THE ARROGANCE OF FIRE", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Command to Prostrate, Racial Vanity & Seduction of the Tree", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("5. Terrestrial Station & Primordial Prostration", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Humanity established upon the earth and granted means of livelihood (Ma'ayish).\n"
        "- Man created, fashioned, and presented before the assembly of the angelic host.\n"
        "- Command to prostrate in honor: All angels fell down except Iblis in defiance."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("6. Arrogance of Fire: The Genesis of False Analogy", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Demanded reason: 'What prevented you from prostrating when I commanded you?'\n"
        "- Arrogant rationalization: 'I am better than him; You made me of fire and him of clay.'\n"
        "- Cast down in disgrace: 'Descend from here! It is not for you to be arrogant within it.'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("7. The Granted Respite & The Four-Way Ambush", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Iblis petitions respite until Resurrection; granted reprieve by divine decree.\n"
        "- The swore vendetta: 'I will surely sit in ambush on Your straight path.'\n"
        "- Assaulting humanity from front, back, right, and left; seeking to make them ungrateful."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("8. Seduction of the Tree & Exposed Vulnerability", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Dwelling in the Garden with Hawwa; warned never to approach the singular tree.\n"
        "- Satanic whispering: False swearing that the tree grants eternity and angelic power.\n"
        "- Tasting the fruit: Garments stripped away; feverishly stitching leaves in shame."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 2: MORTAL CLOTHING, WARNINGS TO HUMANITY & THE ABODE OF PEACE
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 8,
        "MORTAL CLOTHING, WARNINGS TO HUMANITY & THE ABODE OF PEACE",
        "Pillars 3 & 4: Libas at-Taqwa, Decorum at the Sanctuary, Rebutting False Taboos & The Appointed Term",
        "PLATE 02 : MODESTY & SANCTUARY"
    )

    # Column 1: Pillar 3
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 3: THE THREE GARMENTS & REDEMPTIVE CONTRITION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Rabbana Zalamna, Modesty of Form & The Clothing of Piety", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("9. The Contrite Archetypal Cry: Rabbana Zalamna", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Our Lord, we have wronged ourselves; if You forgive us not, we are of the losers.'\n"
        "- Immediate personal responsibility contrasts with Iblis's fatalistic grievance.\n"
        "- Descending to earth with mutual enmity; life, death, and resurrection terrestrialized."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("10. Libas at-Taqwa: The Supreme Inner Garment", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Divine gift of clothing: Covering baseline nakedness (Satr) and aesthetic beauty (Reesh).\n"
        "- 'And the garment of righteousness (Libas at-Taqwa)—that is best.'\n"
        "- Fine silks without Taqwa leave the human interior exposed in spiritual humiliation."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("11. Satanic Disrobing: Warning to Children of Adam", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Let not Satan deceive you as he expelled your primordial parents from the Garden.\n"
        "- Stripping away modesty to expose vulnerability is an ancient adversarial strategy.\n"
        "- Shayateen made allies of those who do not believe, beautifying shameful acts."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("12. Decisive Rebuttal of Naked Rituals", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Pre-Islamic pagans committed indecency, claiming: 'We found our forefathers doing it.'\n"
        "- Divine declaration: Allah never commands shameful indecency or immoral rites.\n"
        "- Say: 'My Lord has commanded justice and directing devotion solely to Him.'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 4
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 4: SACRED DECORUM & THE FIVE PROHIBITIONS", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Beauty at the Masjid, Wholesome Provisions & The Fixed Lifespan", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("13. Decorum at the Sanctuary: Adornment & Balance", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'O children of Adam, take your adornment (Zeenah) at every place of prayer.'\n"
        "- Eat and drink in wholesome gratitude; do not commit excess (La tusrifoo).\n"
        "- Divine rule: Moderation and aesthetic dignity are foundational religious duties."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("14. Who Has Forbidden Wholesome Provisions?", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Stern rebuke: 'Who has forbidden the adornment of Allah and wholesome food?'\n"
        "- These blessings are for believers in this worldly life and exclusively theirs in Akhirah.\n"
        "- Islam annihilates false asceticism and fabricated taboos on lawful pleasures."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("15. The Five Universal Prohibitions", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Open and secret indecencies (Fawahish), sin, and unprovoked oppression (Baghy).\n"
        "- Associating partners with Allah without revelatory authority (Shirk).\n"
        "- Speaking about Allah without knowledge: The ultimate spiritual transgression."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("16. The Sealed Lifespan of Civilizations (Ajal)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Every civilization has an immutable appointed term; none escapes its historical hour.\n"
        "- When their time arrives, it can neither be delayed nor advanced by a single moment.\n"
        "- Believers who maintain Taqwa and reform have no fear, nor shall they grieve."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 3: THE DIALOGUE OF THE HEIGHTS & THE COSMIC CLEANSING OF HEARTS
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 8,
        "THE DIALOGUE OF THE HEIGHTS & THE COSMIC CLEANSING OF HEARTS",
        "Pillars 5 & 6: Closed Heavenly Gates, Recriminations in the Fire, Ashab al-A'raf & The Vaulted Bridge",
        "PLATE 03 : THE HEIGHTS & ESCHATOLOGY"
    )

    # Column 1: Pillar 5
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 5: CLOSED GATES & MUTUAL RECRIMINATIONS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("The Eye of the Needle, Beds of Fire & Sister Nations Cursing Sister Nations", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("17. The Eye of the Needle: Barred Heavenly Gates", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- For those who deny divine signs with arrogance, heavenly gates never open.\n"
        "- They shall not enter Paradise until a camel passes through the eye of a needle.\n"
        "- Complete metaphysical impossibility for obstinate deniers of transcendent truth."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("18. Beds of Torment & Retribution for Tyranny", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- For them are couches of Hellfire beneath them and coverings of fire above them.\n"
        "- Exact retributive justice: Repaying oppressors according to their arrogant tyranny.\n"
        "- Contrasted with the humble righteous who strive within the limits of their capacity."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("19. Sister Nations Cursing Sisters in Hell", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Every time a rebellious generation enters the Fire, it curses its predecessor.\n"
        "- Followers accuse their leaders: 'Our Lord, these misled us; give them doubled torment!'\n"
        "- Divine response: 'For each there is double, but you do not know.'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("20. Denied Intercession: Forgetting Those Who Forgot", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- On that Day, the reality of revelation is manifest; former deities vanish into thin air.\n"
        "- Deniers plead for intercessors or a second worldly trial to act righteously.\n"
        "- Divine verdict: 'Today We forget them just as they forgot the meeting of this Day.'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 6
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 6: ASHAB AL-A'RAF & PURIFIED HEARTS IN JANNAH", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Cleansing Resentment, The Men on the Ramparts & The Cry for Water", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("21. Cleansing Resentment: The Vaulted Bridge", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'And We will remove whatever malice (Ghill) is in their breasts; rivers flowing beneath.'\n"
        "- Reconciled upon the Qantarah, entering Paradise as loving brothers upon thrones.\n"
        "- Their eternal gratitude: 'Praise be to Allah who guided us to this blessed abode!'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("22. The Great Dialogue Across the Cosmic Divide", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Dwellers of Paradise call out: 'We have found what our Lord promised to be true!'\n"
        "- Dwellers of the Fire respond in anguish: 'Yes, we have found it true.'\n"
        "- The caller proclaims between them: 'The curse of Allah is upon the oppressors.'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("23. Ashab al-A'raf: The Men upon the Ramparts", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Standing upon the high partition, recognizing residents of both realms by their marks.\n"
        "- Greeting Jannah with longing peace; looking at Hell and crying: 'Save us from them!'\n"
        "- Equal deeds balance them in suspense until sovereign grace admits them into bliss."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("24. The Denied Cry for Water & Nourishment", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Dwellers of the Fire plead: 'Pour upon us some water or what Allah provided you!'\n"
        "- Inhabitants of Paradise answer: 'Indeed, Allah has forbidden both to the disbelievers.'\n"
        "- They took religion as distraction and amusement, deceived by worldly illusions."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 4: COSMIC CREATION, HUMBLE SUPPLICATION & THE EARLY MESSENGERS
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 8,
        "COSMIC CREATION, HUMBLE SUPPLICATION & THE EARLY MESSENGERS",
        "Pillars 7 & 8: Hexaemeron Creation, Istawa Transcendent, Adab of Du'a, Nuh & Hud's Struggle",
        "PLATE 04 : COSMIC CREATION & EARLY PROPHETS"
    )

    # Column 1: Pillar 7
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 7: HEXAEMERON CREATION & SACRED SUPPLICATION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Six Cosmic Epochs, Sovereign Istawa, Tadarru'an wa Khufyah & Reviving Rain", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("25. Six Epochs of Creation & The Solar Veil", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Created heavens and earth in six days; night wraps daylight in swift pursuit.\n"
        "- Sun, moon, and stars completely subservient to His unchallengeable command.\n"
        "- 'Unquestionably, His is the creation and the command; blessed is Allah, Lord of Worlds.'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("26. Istawa 'alal-'Arsh: Transcendent Majesty", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Transcendent establishment over the Throne without physical modality or resemblance.\n"
        "- Incomprehensible glory affirming sovereignty above all contingent dimensions.\n"
        "- Sovereign ruler of cosmic order, guiding all creation through purposeful wisdom."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("27. The Adab of Du'a: Humility & Secrecy", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Call upon your Lord in broken humility (Tadarru') and in secrecy (Khufyah).'\n"
        "- Allah does not love transgressors who scream, boast, or demand the impossible.\n"
        "- Sowing no corruption after earth's reformation; calling in awe and aspiration."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("28. The Reviving Winds: Parable of Resurrection", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Merciful winds sent as glad tidings, carrying heavy clouds across arid wastelands.\n"
        "- Rains reviving dead soils to yield produce; exactly thus are the dead resurrected.\n"
        "- The fertile land yields vegetation by God's leave; corrupt land yields only bitter shrubs."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 8
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 8: EARLY PROPHETIC STRUGGLES: NUH & HUD", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Nuh's Compassionate Naseehah, The Deluge & 'Ad's Monolithic Arrogance", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("29. Nuh's Mission: Pure Monotheism & Warning", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'O my people, worship Allah; you have no deity other than Him; I fear for you the Day.'\n"
        "- Tribal chieftains mock: 'Indeed, we see you in manifest, foolish error.'\n"
        "- Sincere reply: 'There is no error in me, but I am a Messenger from the Lord of Worlds.'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("30. Delivering Sincere Advice (Naseehah)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Nuh conveys divine messages, offering sincere counsel and knowing what they know not.\n"
        "- Rebuking wonder: 'Do you marvel that an admonition comes through a man among you?'\n"
        "- Deniers reject the signs; believers saved in the Ark; the mockers drowned in the flood."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("31. Hud to 'Ad: Confronting Giant Monoliths", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Sent to the mighty empire of 'Ad: 'O my people, worship Allah; will you not fear Him?'\n"
        "- Chieftains insult: 'Indeed, we see you in foolishness, and we think you are of the liars.'\n"
        "- Hud answers with prophetic dignity: 'There is no foolishness in me; I am a faithful adviser.'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("32. Remembrance of Blessings & The Gale Retribution", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Reminding them of how God made them successors after Nuh and increased their stature.\n"
        "- They defiantly clung to ancestral idols; retribution arrived as a furious destructive wind.\n"
        "- Believers delivered through divine mercy; roots of arrogant tyrants severed completely."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 5: PROPHETIC CONTESTS: SALIH, LUT & SHU'AYB
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        5, 8,
        "PROPHETIC CONTESTS: SALIH, LUT & SHU'AYB",
        "Pillars 9 & 10: Thamud & The She-Camel, Lut & The Sodomites, Shu'ayb & Economic Justice",
        "PLATE 05 : PROPHETIC CRUCIBLES"
    )

    # Column 1: Pillar 9
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 9: THE TRIALS OF THAMUD & THE SODOMITES", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Palaces in Rock, The Miraculous She-Camel, Unnatural Obscenity & Brimstone Rain", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("33. Salih to Thamud: Dwelling in Rock Palaces", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Settled in lush plains, carving grand homes out of mountain stone cliffs.\n"
        "- Remember God's favors; do not commit abuse upon the earth, spreading corruption.\n"
        "- The arrogant elite mock: 'Do you know that Salih is truly sent from his Lord?'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("34. The Miraculous She-Camel (Naqatullah)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Sent as a manifest sign: 'This is the She-Camel of Allah; leave her to graze freely.'\n"
        "- Do not touch her with harm, lest a painful punishment seize you without warning.\n"
        "- The wickedest conspirators hamstrung the camel and defied their Lord's decree."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("35. The Tremor (Ar-Rajfah) & Salih's Elegy", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Cataclysmic seismic shock struck them; morning found them collapsed lifeless in homes.\n"
        "- Salih turned away in sorrow: 'I conveyed my Lord's message, but you love not advisers.'\n"
        "- The proud civilization wiped from history, their monumental stone dwellings desolate."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("36. Lut's Stand Against Moral Perversion", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Confronting the men of Sodom: 'Do you commit an obscenity none before you committed?'\n"
        "- Approaching men with carnal lust instead of women; exceeding all human boundaries.\n"
        "- Their only answer was expulsion: 'Drive them out! They are people who keep pure!'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 10
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 10: SHU'AYB, MADYAN & ECONOMIC SANCTITY", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Honest Scales, Highway Extortion, Oligarchic Ultimatums & The Snare of Makr Allah", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("37. Shu'ayb to Madyan: The Integrity of Commerce", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Give full measure and weight; do not deprive people of their rightful belongings.'\n"
        "- Do not cause corruption upon the earth after it has been reformed by divine law.\n"
        "- Grounding honest business in faith: Honest trade is a sacred covenant with the Lord."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("38. Rebuking Highway Ambush & Banditry", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Do not sit upon every pathway threatening travelers and hindering from God's way.\n"
        "- Remember when you were few in numbers and He multiplied your wealth and strength.\n"
        "- Observe the sobering end of those who spread corruption across neighboring lands."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("39. The Oligarchic Ultimatum & Firm Faith", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Arrogant chieftains threaten: 'We will expel you and your followers or you must return!'\n"
        "- Shu'ayb replies: 'Even if we hate it? We would fabricate a lie if we returned to your ways.'\n"
        "- 'Our Lord, decide between us and our people in truth; You are the best of deciders.'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("40. The Destruction of Madyan & The Snare of Security", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Struck by the seismic tremor, left prostrate and dead in their luxurious dwellings.\n"
        "- Those who denied Shu'ayb became as though they had never prospered within them.\n"
        "- Do they feel secure against the plan of Allah (Makr Allah)? None feels secure except losers."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 6: THE EPIC OF MUSA: CONFRONTING FIR'AWN & THE FALL OF SORCERERS
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        6, 8,
        "THE EPIC OF MUSA: CONFRONTING FIR'AWN & THE FALL OF SORCERERS",
        "Pillars 11 & 12: Manifest Serpent, Prostration of Sorcerers, The Five Plagues & Deliverance at the Sea",
        "PLATE 06 : MUSA & TYRANNY"
    )

    # Column 1: Pillar 11
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 11: SIGNS BEFORE PHARAOH & DEFIANCE OF FAITH", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Musa's Emissary Mission, Living Python, Illusion Defeated & The Sorcerers' Sujood", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("41. Musa's Declaration: Emissary from Rabb al-'Alameen", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Musa confronts the Pharaoh: 'I am an emissary from the Lord of the worlds.'\n"
        "- Obligated to speak nothing about Allah except the absolute, unblemished truth.\n"
        "- 'Release with me the Children of Israel from generational enslavement and torment.'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("42. The Real Serpent & The Radiant Hand", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Musa casts his staff: It becomes an undeniable, living, devouring python (Thu'ban).\n"
        "- He draws forth his hand: Radiant, gleaming white to all onlookers without blemish.\n"
        "- Pharaoh's counsellors panic: 'Indeed, this is a learned, dangerous sorcerer!'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("43. The Great Tournament of Egyptian Sorcery", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Magicians summoned from all provinces; promises of riches and royal proximity.\n"
        "- They cast ropes and staffs, bewitching human eyes and striking terror with illusions.\n"
        "- God inspires Musa: 'Cast your staff!' It devours every illusory falsehood they fabricated."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("44. The Prostration of Sorcerers (Sujjada)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The master magicians fall instantly in prostration: 'We believe in the Lord of the worlds!'\n"
        "- Unanimous recognition: This was not magic or trickery, but divine omnipotence.\n"
        "- Truth prevailed; Pharaoh's imperial vanity and spiritual prestige collapsed in a moment."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 12
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 12: PHARAOH'S WRATH, PLAGUES & THE SEA DIVIDE", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Threats of Dismemberment, Heroic Patience, Five Inundations & Sea Deliverance", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("45. Pharaoh's Raging Threats of Dismemberment", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Pharaoh rages: 'Did you believe before I granted permission? This is a conspiracy!'\n"
        "- Threats of cross-amputation (hands and feet on opposite sides) and crucifixion.\n"
        "- The new believers answer with sublime defiance: 'Indeed, to our Lord we return!'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("46. The Believers' Prayer for Steadfastness", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'You take vengeance upon us only because we believed in the signs of our Lord.'\n"
        "- 'Rabbana afrigh 'alayna sabran wa tawaffana muslimeen' (Pour upon us patience!).\n"
        "- Musa counsels his trembling people: 'Seek help through Allah and be steadfast.'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("47. The Five Inundations (Ayatin Mufassalat)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Egypt struck systematically: The flood, locusts, lice, frogs, and water turned to blood.\n"
        "- Manifest, distinct signs; yet Pharaoh and his lords persisted in haughty criminality.\n"
        "- Each time relief was granted upon Musa's du'a, they broke their solemn covenants."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("48. The Splitting of the Sea & Drowning of Fir'awn", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Pharaoh and his hosts pursued the believers; plunged into the deep waters of the sea.\n"
        "- The dispossessed and oppressed inherited the blessed eastern and western lands.\n"
        "- Word of divine promise fulfilled for Bani Isra'il because of their enduring patience."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 7: MOUNT SINAI, THE VISION PETITION & THE GOLDEN CALF
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        7, 8,
        "MOUNT SINAI, THE VISION PETITION & THE GOLDEN CALF",
        "Pillars 13 & 14: The 40 Nights, Rabbi Arini, Pulverized Mountain, Inscribed Tablets & The Golden Calf",
        "PLATE 07 : SINAI & THE TABLETS"
    )

    # Column 1: Pillar 13
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 13: THEOPHANY AT SINAI & THE INSCRIBED TABLETS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Forty Nights, Yearning for Divine Sight, Shattered Granite & The Divine Law", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("49. Forty Nights of Sinai & Harun's Deputyship", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Musa appointed thirty nights, completed with ten, culminating in forty holy nights.\n"
        "- Musa counsels Harun: 'Take my place among my people, act righteously, avoid corruption.'\n"
        "- Prepared through spiritual retreat to receive the direct Word of the Sovereign Lord."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("50. The Vision Petition: Rabbi Arini Anzur Ilayk", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Overwhelmed by love after direct speech (Takleem), Musa asks: 'Lord, show me Yourself!'\n"
        "- Divine response: 'You will never see Me in this mortal realm; but look at the mountain.'\n"
        "- 'If it remains firmly in its place, then you shall behold My transcendent glory.'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("51. The Mountain Pulverized & Musa's Swoon", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- When Allah revealed His glory to the mountain, it crumbled into fine, swirling dust.\n"
        "- Musa collapsed in unconscious terror (Kharra Musa sa'iqa) from the awe of the theophany.\n"
        "- Awakening in repentance: 'Glory be to You! I turn to You, first of the believers.'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("52. The Inscribed Tablets of Admonition", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'O Musa, I have chosen you over humankind through My messages and My speech.'\n"
        "- Bestowed the sacred Tablets inscribed with comprehensive admonition and legal detail.\n"
        "- Commanded to hold them with unwavering strength and enjoin his people to the best of it."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 14
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 14: THE GOLDEN CALF, ANGER & THE UMMI PROPHET", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("The Lowing Calf Effigy, Prophetic Indignation, 70 Elders & The Universal Messenger", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("53. Seduction of the Lowing Calf Effigy", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- In Musa's absence, jewelry melted to form the lifeless body of a lowing golden calf.\n"
        "- The people worshipped it in folly: 'Did they not see it speaks not nor guides them?'\n"
        "- Deep spiritual relapse into pagan superstition the moment prophetic leadership paused."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("54. Musa's Righteous Fury & Harun's Plea", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Musa returns grieving and furious, casting down the Tablets and seizing Harun's beard.\n"
        "- Harun pleads: 'Son of my mother, the mob overpowered me and almost killed me.'\n"
        "- Calming, Musa takes up the Tablets: In their inscription was guidance and mercy for the fearful."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("55. The Seventy Elders & The Seismic Tremor", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Musa chose seventy men of stature for the divine appointment; seized by a violent quake.\n"
        "- Musa intercedes: 'Would You destroy us for what foolish men did? You are our protector.'\n"
        "- 'Forgive us and have mercy upon us; You are the best of those who forgive.'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("56. The Prophesied Ummi Messenger in Scripture", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Mercy decreed for those who follow the unlettered Prophet (An-Nabiyy al-Ummiyy).\n"
        "- Inscribed in the Torah and Injeel: Enjoining good, forbidding evil, making pure things halal.\n"
        "- Relieving humanity from crushing burdens and shackles; successful are those who honor him."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 8: THE PRIMORDIAL COVENANT, THE PARABLE OF THE DOG & FINAL PROSTRATION
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        8, 8,
        "THE PRIMORDIAL COVENANT, THE PARABLE OF THE DOG & FINAL PROSTRATION",
        "Pillars 15 & 16: The Twelve Springs, Sabbath-Breakers, Mithaq Adam, Parable of the Dog & Final Sajdah",
        "PLATE 08 : THE PRIMORDIAL COVENANT"
    )

    # Column 1: Pillar 15
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 15: THE PRIMORDIAL MITHAQ & SABBATH METAMORPHOSIS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Twelve Springs, Transgressing the Sabbath, Canopy Mountain & Alastu bi-Rabbikum", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("57. Twelve Springs, Manna, Quails & The Altered Word", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Divided into twelve tribes; rock struck to yield twelve distinct gushing springs.\n"
        "- Manna and quails provided; commanded to enter the city saying 'Hittah' (Forgiveness).\n"
        "- Transgressors altered the word in mockery, inviting plague for their persistent disobedience."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("58. The Sabbath-Breakers & The Three Factions", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Tested with swarming fish on the Sabbath; three factions: sinners, preachers, bystanders.\n"
        "- Bystanders asked: 'Why preach to people Allah will destroy?' Preachers: 'As an excuse to our Lord.'\n"
        "- The righteous preachers saved; the Sabbath-breakers transformed into despised apes."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("59. Mount Sinai Shaken Like a Canopy (Zullah)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Shaking the mountain above them like a dark, towering storm cloud ready to crush them.\n"
        "- 'Hold fast to what We have given you with resolve, and remember what is within it.'\n"
        "- A terrifying physical testament to the absolute seriousness of the divine covenant."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("60. The Primordial Covenant: Alastu bi-Rabbikum?", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Progeny extracted from Adam's loins, made to testify: 'Am I not your Lord?'\n"
        "- Every soul replied: 'Bala, shahidna!' (Yes, we testify!)—inscribing Fitrah in human consciousness.\n"
        "- Eliminating all excuses on Judgment Day: None can claim heedlessness or inherited Shirk."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 16
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 16: DIVINE NAMES, PERPETUAL THIRST & THE UNIVERSAL SAJDAH", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Parable of the Panting Dog, Hearts Without Understanding, Al-Asma al-Husna & The Sajdah", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("61. Parable of the Panting Dog: The Apostate Scholar", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The man granted divine verses who stripped them away (Insalakha), pursuing vile lusts.\n"
        "- His likeness is that of a dog: Drive him away and he pants, leave him and he pants.\n"
        "- Perpetual, insatiable spiritual thirst of those who sell sacred knowledge for worldliness."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("62. Created for Jahannam: Deadened Spiritual Faculties", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Hearts that do not understand, eyes that do not see, ears that do not hear.\n"
        "- 'They are like livestock; rather, they are more astray; it is they who are the heedless.'\n"
        "- Willful rejection of revelatory faculties reduces the human being below the level of animals."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("63. Al-Asma al-Husna: The Ninety-Nine Beautiful Names", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'And to Allah belong the most beautiful names, so invoke Him by them.'\n"
        "- Abandon those who practice deviation (Ilhad) concerning His transcendent names.\n"
        "- Refuge from Satanic whispers: Seek protection in Allah, the All-Hearing, All-Knowing."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("64. The Adab of Qur'an & The Grand Prostration", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- When the Qur'an is recited, listen in silence that you may obtain divine mercy.\n"
        "- Remember your Lord within yourself with humility, fear, and soft voice morning and night.\n"
        "- Angels before the Throne glorify Him without fatigue and prostrate: Fall down in Sajdah!"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Save PDF
    pdf.save(OUTPUT_PDF)
    print(f"Successfully generated Surah Al-A'raf Master Mindmap PDF: {OUTPUT_PDF} ({os.path.getsize(OUTPUT_PDF)} bytes)")

    # Render PNG previews with pdftoppm
    print("Generating page preview renders...")
    cmd = ["pdftoppm", "-png", "-r", "150", OUTPUT_PDF, os.path.join(PREVIEWS_DIR, "al_araf_page")]
    subprocess.run(cmd, check=True)

    # Copy previews to brain directory
    for f in sorted(os.listdir(PREVIEWS_DIR)):
        if f.startswith("al_araf_page") and f.endswith(".png"):
            src = os.path.join(PREVIEWS_DIR, f)
            dst = os.path.join(brain_dir, f)
            shutil.copy2(src, dst)
            print(f"Copied preview to brain: {dst}")

if __name__ == "__main__":
    build_al_araf_pdf()
