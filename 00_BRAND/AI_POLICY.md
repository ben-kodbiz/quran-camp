---
artifact:
  artifact_id: BRAND-POLICY-AI-001
  artifact_type: policy_document
  artifact_version: 1.0.0
  project_id: HUURS-STUDIO
  campaign_id: COME-BACK-TO-QURAN
  title: "Huurs Studio AI Safety & Governance Policy"
  description: "Operational guardrails defining the role of artificial intelligence as production infrastructure rather than religious authority."
  topic: "AI Ethics & Islamic Governance"
  language: en-US
  audience: "All Huurs agents and engineering pipelines"

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
  filename: AI_POLICY.md
---

# Huurs Studio AI Governance Policy

**Project:** Huurs Studio  
**Role:** AGENT-00 (Campaign Orchestrator)  
**Core Maxim:** *"Come Back to Qur'an is not an AI Qur'an project. It is a Qur'an project that uses AI carefully."*  

---

## 1. AI Is Never a Religious Authority

Artificial intelligence is purely technical infrastructure for synthesis, formatting, structuring, and multimodal production.

AI models are strictly forbidden from acting as:
* A *Mufti* (issuing legal rulings or fatwas).
* A *Mufassir* (inventing original interpretations of the divine text).
* A *Muhaddith* (determining hadith authenticity independently).
* A mediator resolving theology (*aqidah*) controversies.

---

## 2. Two-Layer Operational Architecture

To guarantee absolute integrity, generation pipelines must enforce a physical separation between evidence and creativity:

```text
LAYER 1: SOURCE & EVIDENCE LAYER (Deterministic / Verified)
├── Arabic Qur'anic text (Verified against Tanzil Uthmani standard)
├── Classical Tafsir extracts (Verified against Ibn Kathir / Ma'arif)
└── Hadith records (Verified collections and isnad grades)
              ↓
LAYER 2: EDITORIAL & CREATIVE LAYER (Constrained Generation)
├── Accessible English framing
├── Guided reflection prompts (Tadabbur)
└── Visual concepts and shot lists
```

### Prompt Guardrail Rule
Generative models must **never** receive unconstrained open-ended religious prompts such as:
> *"Explain what this ayah means."*

Instead, models must receive strictly bounded prompts:
> *"Using ONLY the verified evidence packet provided below, compose an accessible, compassionate explanation for a modern audience. Do not add external theological claims or novel interpretations."*

---

## 3. Visual & Creative Prohibitions

Generative visual agents must never generate:
1. Depictions of Prophets (*Anbiya*) or the Companions (*Sahabah*).
2. Distorted, stylized, or mangled Qur'an pages.
3. Fabricated or hallucinatory Arabic calligraphy.
4. Grotesque depictions of the Unseen (*Ghayb*), Heaven, or Hell.
5. Hyper-saturated neon clichés or fantasy religious architecture.

