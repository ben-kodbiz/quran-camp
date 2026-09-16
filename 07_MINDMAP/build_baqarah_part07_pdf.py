#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Baqarah Part 7 Master Landscape Mindmap PDF Compiler
Foundation Media: Part 7 Audio Lecture
Strict Standardization:
- Title: Surah Al-Baqarah — Part 7
- Zero Ayah Numbers in titles/headers/cards
- Zero mention of external speaker names; 100% Huurs Studio & Sunni source discipline
- ZERO AUDIO TIMESTAMPS anywhere on the mindmap
- 4 Landscape Widescreen Pages (792 x 480 pts, 1.65:1 ratio)
- Symmetrical 2-column layout with center connector bridges
- Perfect vertical card distribution (71pt intervals) with zero collisions
"""

import os
import sys

sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
OUTPUT_PDF = os.path.join(BASE_DIR, "BAQARAH_PART_07_MINDMAP.pdf")

# Palette
NAVY_DEEP = (0.024, 0.039, 0.071)
NAVY_CARD = (0.051, 0.078, 0.133)
NAVY_ELEVATED = (0.078, 0.118, 0.196)
GOLD = (0.831, 0.686, 0.353)
GOLD_LIGHT = (0.910, 0.820, 0.580)
CYAN = (0.220, 0.740, 0.970)
PURPLE = (0.659, 0.333, 0.969)
EMERALD = (0.063, 0.725, 0.506)
WHITE = (0.973, 0.980, 0.988)
TEXT_MUTED = (0.680, 0.730, 0.800)
BORDER_MUTED = (0.160, 0.220, 0.310)

def build_part07_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH AL-BAQARAH", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
        pdf.rect(w - 235, h - 32, 130, 20, fill_rgb=NAVY_ELEVATED, stroke_rgb=BORDER_MUTED, line_width=0.8)
        pdf.text("FOUNDATION MEDIA: PART 7", w - 225, h - 20, font="F2", size=7, rgb=EMERALD)
        pdf.text(f"PAGE {pnum:02d} / {total_pages:02d}", w - 85, h - 26, font="F2", size=9, rgb=GOLD)

        pdf.text(title, 32, h - 66, font="F2", size=12, rgb=WHITE)
        pdf.text(subtitle, 32, h - 79, font="F1", size=7.8, rgb=TEXT_MUTED)
        pdf.text(f"[{section_badge}]", w - 140, h - 68, font="F2", size=10.5, rgb=GOLD)
        pdf.line(32, h - 86, w - 32, h - 86, stroke_rgb=BORDER_MUTED, line_width=0.8)

        pdf.line(32, 25, w - 32, 25, stroke_rgb=BORDER_MUTED, line_width=0.8)
        pdf.text("HUURS KNOWLEDGE SYSTEMS  *  AUTHENTIC SUNNI SOURCE DISCIPLINE  *  READ. REFLECT. RETURN.", 32, 13, font="F1", size=7.2, rgb=TEXT_MUTED)
        pdf.text("SURAH AL-BAQARAH FOUNDATION ARCHITECTURE", w - 235, 13, font="F2", size=7.2, rgb=GOLD)

    c1_x, c1_y, c1_w, c1_h = 32, 35, 348, h - 130
    c2_x = c1_x + c1_w + 32
    c2_w = 348
    bridge_y = c1_y + c1_h / 2
    CARD_STEP = 71

    # PAGE 1: THE LIMITS OF APPEASEMENT & TRUE RECITATION
    pdf.new_page(w, h)
    draw_chrome(1, 4, "THE LIMITS OF APPEASEMENT & TRUE RECITATION",
                "Pillars 1 & 2: The fallacy of pleasing adversaries, authentic divine guidance, and Haqqa Tilawatih", "PART 7 : SECTION 1")

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 1: THE LIMITS OF APPEASEMENT", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.5, rgb=CYAN)
    pdf.text("The Fallacy of Compromise & Inna Hudallahi Huwal-Huda", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 50
    pdf.text("1. The Illusion of Appeasement: 'Wa Lan Tarda 'Anka'", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = ("- Neither Jewish nor Christian factions will ever be pleased until you follow their creed.\n"
         "- Ideological adversaries do not seek mutual respect; they demand total theological surrender.\n"
         "- Compromising core revelation to gain secular or social approval is an exercise in futility.")
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Sovereign Guidance: 'Inna Hudallahi Huwal-Huda'", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = ("- 'Say: Indeed, the guidance of Allah is the only true guidance' — absolute epistemological anchor.\n"
         "- Human philosophical fashions shift constantly; revelation remains the unchanging criterion.\n"
         "- True dignity lies in unapologetic adherence to divine truth rather than apologetic dilution.")
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Warning Against Following Desires: 'Ahwa'ahum'", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = ("- Severe divine warning: Following their sectarian desires after knowledge has come to you.\n"
         "- Compromising after receiving certainty strips a believer of divine protection and alliance.\n"
         "- 'You will have neither protector nor helper against Allah' — the cost of moral betrayal.")
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Intellectual Integrity Over Public Opinion", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = ("- Believers must anchor their self-worth in divine validation rather than external popularity.\n"
         "- Seeking approval from critics who reject God creates spiritual paralysis and hypocrisy.\n"
         "- Courage consists of holding firmly to the rope of Allah amidst cultural storms.")
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Center Bridge
    pdf.line(c1_x + c1_w, bridge_y, c2_x, bridge_y, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(w/2 - 12, bridge_y - 8, 24, 16, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=0.8)
    pdf.text_centered("->", w/2, bridge_y + 3, font="F2", size=7, rgb=GOLD_LIGHT)

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 2: THE ETHIC OF TRUE RECITATION", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.5, rgb=EMERALD)
    pdf.text("Ibn Mas'ud's Classical Canon: Comprehension, Law & Devotion", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 50
    pdf.text("1. True Recitation: 'Yatloonahoo Haqqa Tilawatih'", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = ("- 'Those to whom We gave the Scripture and recite it with its true right of recitation.'\n"
         "- Ibn Mas'ud defined Haqqa Tilawatih: Declaring its halal as halal, its haram as haram.\n"
         "- Moving beyond melodic oral sounds to active intellectual and ethical submission.")
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. The Quadruple Pillars of Tilawah", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = ("- Pillar 1: Precise phonetics and correct linguistic pronunciation without alteration.\n"
         "- Pillar 2: Deep reflective contemplation (Tadabbur) on every divine metaphor and command.\n"
         "- Pillar 3: Immediate moral obedience; Pillar 4: Transformative spiritual character.")
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Authentic Belief vs Cosmetic Piety", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = ("- 'Oola'ika yu'minoona bih': Only those who fulfill its true recitation genuinely believe in it.\n"
         "- Superficial reading without practical life conformity is a symptom of weak conviction.\n"
         "- Sincere souls among past scriptural communities recognized the Qur'an through this standard.")
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. The Fatal Loss of Disbelief: 'Humul-Khasiroon'", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = ("- 'And whoever disbelieves in it, it is they who are the ultimate losers.'\n"
         "- Rejecting revelation after understanding its signs results in profound existential bankruptcies.\n"
         "- The Qur'an is either an argument for the soul or an unassailable argument against it.")
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # PAGE 2: THE FINAL ADDRESS & THE ABRAHAMIC PIVOT
    pdf.new_page(w, h)
    draw_chrome(2, 4, "THE FINAL ADDRESS & THE ABRAHAMIC PIVOT",
                "Pillars 3 & 4: Closing the Israelite discourse, Day of Zero Leverage, and testing of Ibrahim", "PART 7 : SECTION 2")

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 3: THE FINAL CLOSING REMINDER", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.5, rgb=CYAN)
    pdf.text("Closing the Israelite Discourse & The Day of Zero Leverage", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 50
    pdf.text("1. The Ring Composition: 'Ya Banee Isra'eel'", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = ("- Symmetrical recapitulation of the opening call from early in the Surah.\n"
         "- Final urgent appeal to Banu Isra'il before the thematic transition to Prophet Ibrahim.\n"
         "- Reminding them of historical divine favors and their election above contemporary nations.")
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. The Day of Absolute Independence", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = ("- 'Wattaqoo yawman la tajzee nafsun 'an nafsin shay'a': Fear a Day when no soul avails another.\n"
         "- Genetic lineage, ancestral sainthood, and tribal status count for zero in the divine court.\n"
         "- Every individual stands solitary and accountable for their personal moral choices.")
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Shattering Illusions of Leverage", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = ("- 'No compensation will be accepted, no intercession will benefit, nor will they be helped.'\n"
         "- Total refutation of the delusion that holy ancestors will shield corrupt descendants.\n"
         "- Faith requires personal accountability today; delayed repentance brings total forfeiture.")
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. The Shift to Universal Patriarchal Legacy", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = ("- Transitioning from ethnic sectarian disputes to the universal founder of pure monotheism.\n"
         "- Ibrahim is claimed by Jews, Christians, and pagan Quraysh; the Qur'an reclaims his true legacy.\n"
         "- True Abrahamic succession is defined by absolute Hanifiyyah (monotheism), not genetic claims.")
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Center Bridge
    pdf.line(c1_x + c1_w, bridge_y, c2_x, bridge_y, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(w/2 - 12, bridge_y - 8, 24, 16, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=0.8)
    pdf.text_centered("->", w/2, bridge_y + 3, font="F2", size=7, rgb=GOLD_LIGHT)

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 4: THE PRIMORDIAL TESTING OF IBRAHIM", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.5, rgb=EMERALD)
    pdf.text("Trials of Kalimat, Flawless Completion & Universal Imamah", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 50
    pdf.text("1. Divine Trials: 'Ibtala Ibraheema Rabbuhoo'", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = ("- 'And remember when his Lord tested Ibrahim with commands (Kalimat).'\n"
         "- Tests included confronting idolaters, exile from Ur, surviving fire, and sacrificing his son.\n"
         "- Spiritual elevation is forged in crucible trials; true faith is tested through severe sacrifice.")
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Flawless Completion: 'Fa-Atammahunn'", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = ("- 'Fa-atammahunn': Ibrahim fulfilled every single command with absolute perfection and beauty.\n"
         "- He hesitated not in the fire, questioned not the desert abandonment, resisted not the sacrifice.\n"
         "- The Qur'an praises him: 'Wa Ibraheema-lladhee waffa' (And Ibrahim who fulfilled his trust).")
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Appointment to Leadership: 'Innee Ja'iluka Imama'", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = ("- Divine decree: 'Indeed, I will make you an Imam (leader/exemplar) for all mankind.'\n"
         "- Imamah is not political conquest; it is universal moral authority and righteous guidance.\n"
         "- Granted only after proven submission; moral authority must be earned through lived integrity.")
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. The Abrahamic Exemplar for All Generations", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = ("- Ibrahim stood alone as an entire Ummah ('Inna Ibraheema kana Ummatan qanitan lillah').\n"
         "- Demonstrates that a single steadfast believer can reorient the spiritual trajectory of history.\n"
         "- The foundation upon which the Final Messenger and the Muslim Ummah are directly built.")
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # PAGE 3: THE COVENANT OF LEADERSHIP & THE SANCTUARY
    pdf.new_page(w, h)
    draw_chrome(3, 4, "THE COVENANT OF LEADERSHIP & THE SANCTUARY",
                "Pillars 5 & 6: Barring oppressors from the covenant, Mathabah, and the sacred station of Ibrahim", "PART 7 : SECTION 3")

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 5: DISQUALIFYING OPPRESSION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.5, rgb=CYAN)
    pdf.text("Moral Merit vs Hereditary Entitlement: 'La Yanalu 'Ahdiz-Zalimeen'", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 50
    pdf.text("1. Ibrahim's Paternal Petition: 'Wa Min Dhurriyyati?'", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = ("- Upon receiving Imamah, Ibrahim immediately pleaded: 'And from my descendants as well?'\n"
         "- Paternal yearning to pass divine light and prophetic guidance down generational lines.\n"
         "- Shows the righteous father's chief concern is the spiritual preservation of his offspring.")
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. The Decisive Divine Boundary: 'La Yanalu 'Ahdi'", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = ("- Allah's instant answer: 'My covenant does not encompass the wrongdoers/oppressors.'\n"
         "- The foundational refutation of genetic entitlement, dynastic privilege, and racism.\n"
         "- Divine election is tied strictly to ethical righteousness, never DNA or biological descent.")
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. The Definition of Zulm (Injustice & Tyranny)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = ("- Classical tafsir: Zulm encompasses Shirk (associating partners with God) and oppression.\n"
         "- Any leader who oppresses people or perverts justice is disqualified from the divine covenant.\n"
         "- Authority in Islam is a sacred moral trust (Amanah), never an unconditional license to rule.")
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Dismantling Tribal Supremacy", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = ("- Direct indictment of Banu Isra'il and pagan Quraysh who claimed automatic nobility via Ibrahim.\n"
         "- If a descendant acts unjust, the ancestral bond with Ibrahim is shattered in the eyes of God.\n"
         "- The true heirs of Ibrahim are those who follow his unblemished path of pure monotheism.")
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Center Bridge
    pdf.line(c1_x + c1_w, bridge_y, c2_x, bridge_y, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(w/2 - 12, bridge_y - 8, 24, 16, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=0.8)
    pdf.text_centered("->", w/2, bridge_y + 3, font="F2", size=7, rgb=GOLD_LIGHT)

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 6: THE CHARTER OF THE SANCTUARY", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.5, rgb=EMERALD)
    pdf.text("Mathabah for Mankind, Perpetual Sanctuary & Maqam Ibrahim", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 50
    pdf.text("1. The House as Mathabah: Perpetual Return", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = ("- 'And remember when We made the House a place of return (Mathabah) for mankind.'\n"
         "- Root Th-W-B: A site to which hearts yearn to return again and again without ever tiring.\n"
         "- No pilgrim visits the Ka'bah except that their longing to revisit is doubled upon departure.")
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. A Global Sanctuary of Peace: 'Wa Amna'", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = ("- 'Wa amna': Established as a permanent inviolable sanctuary of physical and spiritual safety.\n"
         "- Even in pre-Islamic Arabia, blood-feuds were frozen inside the Haram; wildlife remained safe.\n"
         "- A living blueprint for world peace: a sacred zone where weapons and aggression are forbidden.")
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Maqam Ibrahim as a Place of Prayer", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = ("- 'Wattakhidhoo min Maqami Ibraheema musalla': Take the Station of Ibrahim as a place of prayer.\n"
         "- The miraculous stone upon which Ibrahim stood while building the walls of the Ka'bah.\n"
         "- Commemorating the footprints of the father of monotheism through two units of post-Tawaf Salah.")
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Unifying the Global Ummah Toward One Center", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = ("- Consecrating Makkah prepares for the divine order to unify the direction of prayer (Qiblah).\n"
         "- The Ka'bah is the spiritual epicenter of humanity, predating sectarian denominational shrines.\n"
         "- The focal point where race, class, and nationality dissolve in uniform white Ihram.")
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # PAGE 4: SANCTIFICATION & THE VALLEY OF PEACE
    pdf.new_page(w, h)
    draw_chrome(4, 4, "SANCTIFICATION & THE VALLEY OF PEACE",
                "Pillars 7 & 8: Consecrating the House for worship, the du'a for peace, and temporary sustenance", "PART 7 : SECTION 4")

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 7: PURIFYING THE SACRED PRECINCTS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.5, rgb=CYAN)
    pdf.text("The Covenant with Ibrahim & Isma'il: Tahhira Baytiya", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 50
    pdf.text("1. The Mandate to Cleanse: 'Tahhira Baytiya'", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = ("- 'And We covenanted with Ibrahim and Isma'il: Purify My House.'\n"
         "- Physical purification: Freeing the grounds from filth, commercial clutter, and distractions.\n"
         "- Spiritual purification: Total eradication of idolatry, theological corruptions, and vanity.")
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Consecrated for the Four Modes of Worship", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = ("- Purified for: 1. Those who perform circumambulation (At-Ta'ifeen);\n"
         "- 2. Those who enter contemplative seclusion (Al-'Akifeen);\n"
         "- 3. Those who bow (Ar-Rukka'); 4. Those who prostrate in deep prayer (As-Sujood).")
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Partnership of Prophet Father & Son", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = ("- Ibrahim and Isma'il labored side by side as humble construction workers for God's House.\n"
         "- Two noble prophets carrying mortar and stones, displaying supreme humility in divine service.\n"
         "- Exemplar for family legacy: uniting father and son in building spiritual institutions.")
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    y_c -= CARD_STEP
    pdf.line(c1_x + 12, y_c + 8, c1_x + c1_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Custodianship as Servant Leadership", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = ("- Custodians of sacred places must view their role as humble servants of worshippers, not lords.\n"
         "- Providing cleanliness, peace, and dignity for the poorest pilgrim entering the sanctuary.\n"
         "- Sincere mosque governance requires selfless stewardship anchored in prophetic humility.")
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    # Center Bridge
    pdf.line(c1_x + c1_w, bridge_y, c2_x, bridge_y, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(w/2 - 12, bridge_y - 8, 24, 16, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=0.8)
    pdf.text_centered("->", w/2, bridge_y + 3, font="F2", size=7, rgb=GOLD_LIGHT)

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 8: PRAYER FOR PEACE & PROVISION", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.5, rgb=EMERALD)
    pdf.text("Ibrahim's Supplication, Security Before Sustenance & Dunya Mata'", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 50
    pdf.text("1. Security Precedes Sustenance: 'Baladan Aminan'", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = ("- Ibrahim prayed: 'My Lord, make this city a place of peace, and provide its people with fruits.'\n"
         "- Security is mentioned before food: without peace and safety, economic prosperity cannot be enjoyed.\n"
         "- Peace is the essential prerequisite for civilized life, intellectual growth, and worship.")
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. The Barren Desert Yielding Abundant Fruits", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = ("- Makkah was an uncultivated valley without agriculture, water, or vegetation ('Ghayri dhee zar'').\n"
         "- Through Ibrahim's du'a, produce from every corner of the earth flows into Makkah effortlessly.\n"
         "- Divine providence turns desolate arid rock into an oasis of perpetual abundance.")
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Dunya Sustenance vs Eternal Recompense", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = ("- Ibrahim restricted his prayer to believers; Allah corrected him: 'And whoever disbelieves...'\n"
         "- 'I will grant him enjoyment for a little, then force him to the torment of the Fire.'\n"
         "- Earthly provision (Rizq) is universal; afterlife bliss (Falah) is reserved strictly for faith.")
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    y_c -= CARD_STEP
    pdf.line(c2_x + 12, y_c + 8, c2_x + c2_w - 12, y_c + 8, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. The Terrible Destination: 'Wa Bi'sal-Maseer'", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = ("- Worldly luxury is fleeting ('Umatti'uhoo qaleelan'); material wealth is never a proof of salvation.\n"
         "- A disbeliever may enjoy feast and palaces in dunya, only to face eternal destitution in Akhirah.\n"
         "- True wisdom measures success by the final destination, never transient earthly comforts.")
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10, font="F1", size=6.7, rgb=TEXT_MUTED)

    os.makedirs(BASE_DIR, exist_ok=True)
    pdf.save(OUTPUT_PDF)
    print(f"[OK] Master Landscape PDF compiled successfully: {OUTPUT_PDF}")

if __name__ == "__main__":
    build_part07_pdf()
