---
artifact:
  artifact_id: BRAND-POLICY-HADITH-001
  artifact_type: policy_document
  artifact_version: 1.0.0
  project_id: HUURS-STUDIO
  campaign_id: COME-BACK-TO-QURAN
  title: "Huurs Studio Hadith Verification & Authentication Policy"
  description: "Stringent standards governing the selection, citation, isnad verification, and scholarly grading of hadith literature."
  topic: "Hadith Authentication Standards"
  language: en-US
  audience: "All Huurs researchers, writers, and verification agents"

lifecycle:
  status: active
  created_by: AGENT-00
  created_at: 2026-09-07T16:08:00Z

provenance:
  parent_artifacts:
    - "file:///mnt/AI/ag/Campaign/Brand_Campaign.md"
    - "file:///mnt/AI/ag/Campaign/AGENTS.md"
    - "file:///mnt/AI/ag/Campaign/13_CAMPAIGNS/Learn_quran.md"

verification:
  verification_status: verified
  qa_status: passed
  human_review_status: approved

storage:
  repository: huurs-studio
  path: 00_BRAND/
  filename: HADITH_POLICY.md
---

# Huurs Studio Hadith Verification Policy

**Project:** Huurs Studio  
**Role:** AGENT-03 (Source Verification) & AGENT-15 (Islamic QA)  
**Standard:** Rigorous Sunni Hadith Discipline  

---

## 1. Zero Tolerance for Unauthenticated Traditions

1. **No hadith may be cited merely because an AI model outputs it.**
2. Viral internet quotes, pious anecdotes (*qisas*), and weak/fabricated traditions (*mawdu'* / *da'if jiddan*) are strictly forbidden.
3. If a hadith's grading cannot be verified through recognized muhaddithin (scholars of hadith), it must **not** be included.

---

## 2. Mandatory Citation Coordinates

Every cited hadith must include the following five attributes in its metadata and provenance record:

| Attribute | Description | Example |
|---|---|---|
| **Primary Collection** | Specific canonical collection | *Sahih al-Bukhari*, *Sahih Muslim*, *Sunan Abi Dawud* |
| **Book / Chapter** | Book name & chapter title | *Kitab Fada'il al-Qur'an* (Virtues of the Qur'an) |
| **Hadith Number** | Stable reference number | Hadith 5050 (Bukhari) / Hadith 800 (Muslim) |
| **Narrator** | Companion who received the tradition | Abdullah ibn Mas'ud, Abu Hurairah, Aisha (رضي الله عنهم) |
| **Scholarly Grading** | Authenticated grade | *Sahih* (sound), *Hasan* (good) per classical consensus |

---

## 3. Preferred Source Hierarchy

1. **Sahihayn First:** Traditions recorded in *Sahih al-Bukhari* and *Sahih Muslim* carry primary priority.
2. **Four Sunan:** (*Abu Dawud*, *At-Tirmidhi*, *An-Nasa'i*, *Ibn Majah*) accompanied by explicit authentication from recognized classical and contemporary authorities (e.g., Ibn Hajar al-Asqalani, An-Nawawi, Al-Albani).
3. **Muwatta Imam Malik** and **Musnad Ahmad** where authenticated.

---

## 4. Quoting vs. Paraphrasing

* Direct quotations must be faithfully translated without omitting qualifying clauses.
* Where a narration is summarized for brevity, it must be explicitly noted: *"In an authentic narration summarized from Sahih Muslim..."*

