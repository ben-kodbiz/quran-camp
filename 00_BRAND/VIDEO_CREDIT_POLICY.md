---
artifact:
  artifact_id: BRAND-POLICY-VIDEO-720P
  artifact_type: operational_policy_document
  artifact_version: 1.0.0
  project_id: HUURS-STUDIO
  campaign_id: COME-BACK-TO-QURAN
  title: "Huurs Studio Video Production Resolution & Credit Conservation Policy (720p Mandatory Ceiling)"
  description: "Permanent operational directive establishing a strict 720p resolution ceiling for all AI video generation, rendering pipelines, and media exports to prevent credit exhaustion on Pro subscriptions."
  topic: "Video Engineering & Credit Conservation Policy"
  language: en-US
  audience: "All Huurs agents (AGENT-00, AGENT-08, AGENT-10, AGENT-16), video editors, prompt engineers"

lifecycle:
  status: active
  created_by: AGENT-00
  created_at: 2026-09-07T22:10:00Z
  updated_at: 2026-09-07T22:10:00Z

provenance:
  parent_artifacts:
    - "file:///mnt/AI/ag/Campaign/Brand_Visual_System.md"
    - "file:///mnt/AI/ag/Campaign/AGENTS.md"
    - "file:///mnt/AI/ag/Campaign/00_BRAND/AI_POLICY.md"

verification:
  verification_status: verified
  verified_by: USER_MANDATE
  qa_status: passed
  human_review_status: permanently_enforced

storage:
  repository: huurs-studio
  path: 00_BRAND/
  filename: VIDEO_CREDIT_POLICY.md
---

# Video Resolution & Credit Conservation Policy (`BRAND-POLICY-VIDEO-720P`)

**Status:** **PERMANENT OPERATIONAL LAW (HARD CEILING)**  
**Effective Date:** 2026-09-07  
**Authority:** User Mandate & Orchestrator Enforcement  
**Core Maxim:** *"720p video is good enough. Never go beyond that!"*  

---

## 1. Absolute Resolution Ceiling Mandate

All agents, subagents, prompt pipelines, and rendering scripts operating within the Huurs Studio ecosystem must strictly adhere to this non-negotiable ceiling:

```text
┌───────────────────────────────┬───────────────────────────────┬───────────────────────────────┐
│ Video Format & Aspect Ratio   │ Mandatory Resolution Setting  │ Enforcement Rule              │
├───────────────────────────────┼───────────────────────────────┼───────────────────────────────┤
│ Widescreen Flagship (16:9)    │ 1280 × 720 (720p HD)          │ ABSOLUTE MAXIMUM CEILING      │
│ Vertical Shorts/Reels (9:16)  │ 720 × 1280 (720p Vertical HD) │ ABSOLUTE MAXIMUM CEILING      │
│ Square Social Previews (1:1)  │ 720 × 720                     │ ABSOLUTE MAXIMUM CEILING      │
│ 1080p, 2K, 4K, 8K Video       │ STRICTLY PROHIBITED           │ ZERO TOLERANCE OVERRIDE       │
└───────────────────────────────┴───────────────────────────────┴───────────────────────────────┘
```

---

## 2. Technical & Economic Justification

1. **Credit Exhaustion Prevention:**
   * AI video generation models (Runway Gen-2/Gen-3, Luma Dream Machine, Kling, Sora, Veo) bill credits quadratically or in discrete tier blocks based on pixel count. Generating 1080p or 4K drains 2× to 4× more credits per second than 720p.
   * By locking generation to 720p, the user's Pro subscription quota is preserved, allowing sustainable, month-long production without mid-cycle budget depletion.
2. **Streaming & Mobile Efficiency:**
   * Over 85% of YouTube Shorts, Instagram Reels, TikTok, and WhatsApp video consumption occurs on mobile devices where 720p HD is visually indistinguishable from 1080p due to screen PPI and high mobile compression.
   * 720p video files render significantly faster, export in a fraction of the time, and minimize local storage and network bandwidth overhead.
3. **Contemplative Visual Dignity:**
   * Huurs visual language relies on **composition, lighting, negative space, and typography**, not hyper-detailed CGI gimmicks. 720p provides the ideal soft, organic, filmic texture that matches our tranquil, unhurried brand identity.

---

## 3. Mandatory Agent Pipeline Directives

* **`AGENT-08` (Visual Director):** Must explicitly specify `1280x720` or `720p` in all visual briefs and shot lists. Never include `4K`, `UHD`, `1080p`, or `8K` in video prompts.
* **`AGENT-10` (Video Agent):** Must configure all video generation API calls, command-line runners, and video storyboards to `resolution: 720p` (or `width: 1280, height: 720` / `width: 720, height: 1280`).
* **`AGENT-16` (Visual QA):** Any video storyboard, prompt, or test render that requests or outputs resolution higher than 720p must be **immediately rejected** at Gate 02.
* **Post-Production Upscaling:** Upscaling beyond 720p is strictly disallowed.

---
