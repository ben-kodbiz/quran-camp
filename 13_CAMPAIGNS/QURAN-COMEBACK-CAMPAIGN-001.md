---
artifact:
  artifact_id: QURAN-COMEBACK-CAMPAIGN-001
  artifact_type: campaign_manifest
  artifact_version: 1.0.0
  project_id: HUURS-QURAN
  campaign_id: COME-BACK-TO-QURAN
  title: "Come Back to the Qur'an — Master Campaign Architecture & DAG Manifest"
  description: "Master campaign architecture, execution DAG, 30-day calendar, 10 flagship episodes, repurposing matrix, and 114-surah digital book roadmap."
  topic: "Qur'an Re-engagement & Tadabbur"
  language: en-US
  audience: "English-speaking Muslims, especially those seeking to reconnect with the Qur'an through contemplation and authentic understanding."

source_layer:
  source_type: original_synthesis
  primary_sources:
    - "Holy Qur'an (Uthmani text)"
    - "Tafsir Ibn Kathir (Abridged)"
    - "Ma'arif-ul-Qur'an (Mufti Muhammad Shafi)"
    - "Sahih al-Bukhari & Sahih Muslim"
  translation_reference: "The Clear Quran (Dr. Mustafa Khattab)"

lifecycle:
  status: active
  created_by: AGENT-00
  created_at: 2026-09-07T16:08:00Z
  updated_at: 2026-09-07T16:08:00Z

provenance:
  parent_artifacts:
    - "file:///mnt/AI/ag/Campaign/13_CAMPAIGNS/Learn_quran.md"
    - "file:///mnt/AI/ag/Campaign/Brand_Campaign.md"
    - "file:///mnt/AI/ag/Campaign/Antigravity_Agent_Routing.md"
    - "file:///mnt/AI/ag/Campaign/Artifact_Schema.md"

verification:
  verification_status: verified
  verified_by: AGENT-03
  qa_status: passed
  human_review_status: approved_gate_01_and_gate_02

storage:
  repository: huurs-studio
  path: 13_CAMPAIGNS/
  filename: QURAN-COMEBACK-CAMPAIGN-001.md
---

# Come Back to the Qur'an (`QURAN-COMEBACK-CAMPAIGN-001`)

**Project:** Huurs / Huur Studio  
**Tagline:** *Read it. Understand it. Live it.*  
**North Star:** **READ. REFLECT. RETURN.**  
**Status:** In Execution (Sprint 1 Active)  

---

## 1. Executive Directive & Mission

The mission of *Come Back to the Qur'an* is **not** to produce generic motivational media, nor to compete with audio recitation channels, nor to offer ungrounded personal interpretations.

The mission is:
> **To help believers return to the Book of Allah, understand its verses with authentic Sunni scholarship, reflect upon them with sincerity (tadabbur), and live them through concrete daily practice.**

### The Core Content Equation
```text
QUR'AN (Arabic)
      ↓
ACCURATE TRANSLATION
      ↓
CLASSICAL TAFSIR (Ibn Kathir / Ma'arif-ul-Qur'an)
      ↓
AUTHENTIC HADITH CHECK
      ↓
TADABBUR (Guided Contemplation)
      ↓
PRACTICAL ACTION (Living the Ayah)
      ↓
RETURN (Daily Reconnection)
```

---

## 2. Active Task DAG Ledger

| Task ID | Stage | Assigned Agent | Capability Tier | Status | Output Artifact ID | Human Review Gate |
|---|---|---|---|---|---|---|
| **T-01** | Campaign Manifest & DAG Registration | `AGENT-01` | Deep Reasoning | **COMPLETED** | `QURAN-COMEBACK-CAMPAIGN-001` | N/A |
| **T-02** | Policy Suite Initialization | `AGENT-19` | System Orchestration | **COMPLETED** | Policy Docs (`00_BRAND/`) | Passed |
| **T-03** | SQLite Provenance Store Init | `AGENT-19` | Code / SQLite | **COMPLETED** | `database/quran_campaign.db` | Passed |
| **T-04** | Episode 1 Primary Research Pull | `AGENT-02` | Deep Reasoning + Search | **COMPLETED** | `QURAN-COMEBACK-RESEARCH-001` | Passed |
| **T-05** | Claim-Level Source Verification | `AGENT-03` | Deep Reasoning + Fact-check | **COMPLETED** | `QURAN-COMEBACK-VERIFY-001` | **GATE 01 (APPROVED)** |
| **T-06** | Thematic & Metaphor Map | `AGENT-04` | Reasoning | **COMPLETED** | `QURAN-COMEBACK-THEMES-001` | Passed |
| **T-07** | Tadabbur Reflection Framework | `AGENT-05` | Reflective Reasoning | **COMPLETED** | `QURAN-COMEBACK-TADABBUR-001` | Passed (`AGENT-15`) |
| **T-08** | Knowledge Mind Map Structure | `AGENT-06` | Canvas / Visual Reasoning | **COMPLETED** | `QURAN-COMEBACK-MINDMAP-001` | Passed (`AGENT-16`) |
| **T-09** | Visual Direction & Shot List | `AGENT-08` | Multimodal Visual Reasoning | **COMPLETED** | `QURAN-COMEBACK-VISUAL-001` | Passed (`AGENT-16`) |
| **T-10** | Flagship YouTube Script (Ep 1) | `AGENT-07` | Editorial Writing | **COMPLETED** | `QURAN-COMEBACK-SCRIPT-001` | Passed (`AGENT-17`) |
| **T-11** | Shorts Repurposing Pack (5 Shorts) | `AGENT-13` | Social Strategy | **COMPLETED** | `QURAN-COMEBACK-SHORTS-001` | Passed |
| **T-12** | Free Lead Magnet (Day 1 Guide) | `AGENT-12` | Product Structuring | **COMPLETED** | `QURAN-COMEBACK-GUIDE-001` | Passed |
| **T-13** | Ebook Prototype Chapter (114-Surah) | `AGENT-12` | Long-form Editorial | **COMPLETED** | `QURAN-COMEBACK-EBOOK-001` | Passed |
| **T-14** | Multi-Layer QA Audit | `AGENT-15/16/17`| Strict Audit | **COMPLETED** | `QURAN-COMEBACK-QA-001` | **GATE 02 (APPROVED)** |

---

## 3. 30-Day Launch Campaign Architecture

```text
WEEK 1: RETURN (Reconnect the Heart)
├── Day 01: Why Come Back to the Qur'an? (Manifesto: 47:24)
├── Day 02: The Qur'an Was Sent as Guidance (2:2)
├── Day 03: Allah Is Near — Dua and Presence (2:186)
├── Day 04: When Your Heart Feels Hard (39:23, 57:16)
├── Day 05: Don't Wait Until You Are "Good Enough" (39:53)
├── Day 06: The 5-Minute Qur'an Habit Routine
└── Day 07: Week 1 Reflection & Heart Audit

WEEK 2: UNDERSTAND (Overcoming the Difficulty Barrier)
├── Day 08: Surah Al-Fatihah: What Are You Actually Asking For? (1:1–7)
├── Day 09: Guide Me to the Straight Path (1:6)
├── Day 10: No Soul Burdened Beyond Its Capacity (2:286)
├── Day 11: With Hardship Comes Ease — Realistic Hope (94:5–6)
├── Day 12: When You Feel Abandoned (93:3–11)
├── Day 13: Did Allah Not Expand Your Chest? (94:1–8)
└── Day 14: How to Read One Ayah Slowly (Tadabbur Workshop)

WEEK 3: LIVE IT (Transforming Insight into Character)
├── Day 15: What Makes a Person Honorable? (49:13)
├── Day 16: Guarding the Tongue & Ending Backbiting (49:12)
├── Day 17: Honoring Parents: The Qur'anic Command (17:23–24)
├── Day 18: Righteousness Is Beyond Empty Ritual (2:177)
├── Day 19: Character of the True Believer (23:1–11)
├── Day 20: Running Out of Time (103:1–3)
└── Day 21: Weekly Audit: What is One Ayah You Are Living?

WEEK 4: STAY WITH IT (Endurance & Lifelong Return)
├── Day 22: Guarding Against Whispers (23:97–98)
├── Day 23: Seeking Unbreakable Protection (Surah Al-Falaq & An-Nas)
├── Day 24: What to Do When You Fall into Sin (3:133–136)
├── Day 25: Never Despair of the Mercy of Allah (39:53)
├── Day 26: Preparing for Tomorrow (59:18)
├── Day 27: Signs in Creation: Look at What Surrounds You (67:1–5)
├── Day 28: Human Life Summarized in Three Verses (Surah Al-Asr)
├── Day 29: Building a Lifelong Qur'an Habit
└── Day 30: The Journey Begins Today: Commitment to Return
```

---

## 4. 10 Flagship YouTube Episodes

1. **Episode 1:** *"You Don't Need Another Islamic Video — You Need the Qur'an"* (Campaign Manifesto; 47:24)
2. **Episode 2:** *"What Is the Qur'an Actually For?"* (Guidance; 2:2)
3. **Episode 3:** *"Allah Is Closer Than You Think"* (Dua and Nearness; 2:186)
4. **Episode 4:** *"What If You've Been Away From Allah?"* (Mercy; 39:53)
5. **Episode 5:** *"When Life Becomes Heavy"* (Ease with Hardship; 94:5–6)
6. **Episode 6:** *"The Most Important Dua You Say Every Day"* (Sirat al-Mustaqim; 1:6)
7. **Episode 7:** *"Why Does Allah Ask Us to Read Slowly?"* (Tartil and Tadabbur; 73:4)
8. **Episode 8:** *"A Qur'an Routine for Someone Who Has No Time"* (Practical 10-minute method)
9. **Episode 9:** *"The Surah That Explains Why You're Losing"* (Surah Al-Asr; 103:1–3)
10. **Episode 10:** *"30 Days From Now, You Could Be Different"* (Conversion & Lifelong Journey)

---

## 5. Content Repurposing Matrix (Per Research Package)

Each verified research package produces:
* 1 × YouTube Flagship Episode (4–8 minutes)
* 5 × Platform Shorts (Short A: Hook, Short B: Ayah, Short C: Action, Short D: Question, Short E: Myth Check)
* 3 × Static Reflection Cards & Social Carousels
* 1 × Community / Newsletter Reminder
* 1 × Free Lead Magnet Module
* 1 × Standardized Chapter Entry for the 114-Surah Digital Book

---

## 6. The 114-Surah Product Roadmap

* **Free Lead Magnet:** *7 Days Back to the Qur'an* (PDF / Workbook)
* **Entry Product:** *30 Days Back to the Qur'an: Understand. Reflect. Live.*
* **Core Commercial Product:** *Come Back to Qur'an — 114 Surahs: Understand. Reflect. Live.*
  - Phase 1: Surahs 1–10 (MVP validation)
  - Phase 2: Surahs 11–30
  - Phase 3: Surahs 31–60
  - Phase 4: Surahs 61–90
  - Phase 5: Surahs 91–114
* **Future Companion:** Guided audio reflections & printable reflection journal.

