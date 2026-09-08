# Artifact Schema

## Huurs Studio — Universal Artifact Data Contract

**Version:** 1.0
**Status:** Foundation Specification
**Owner:** Huurs Studio
**Scope:** Research → Verification → Knowledge → Content → Visual → Audio → Video → Product → Marketing → Evaluation

---

# 1. Purpose

The Artifact Schema defines the universal structure used by Huurs Studio to store, identify, validate, transform, connect, review, and publish every generated or imported artifact.

The central principle is:

> **Every useful piece of work becomes an artifact. Every artifact has provenance. Every derivative knows its parent.**

Huurs Studio must never depend on a conversation history as its primary source of truth.

Instead:

```text
INPUT
  ↓
ARTIFACT
  ↓
VALIDATION
  ↓
DERIVATION
  ↓
QA
  ↓
APPROVAL
  ↓
PUBLISH
  ↓
EVALUATION
  ↓
NEW KNOWLEDGE
```

This makes Huurs Studio a **persistent knowledge and production system**, rather than a collection of AI conversations.

---

# 2. Design Principles

## 2.1 Vendor Independence

Artifacts belong to Huurs Studio, not to Gemini, Google AI Studio, OpenAI, local LLMs, or any other model provider.

```text
Huurs Artifact
      │
      ├── Gemini
      ├── Local Qwen
      ├── Gemma
      ├── Ling
      ├── OpenAI
      └── Future Models
```

AI models are replaceable execution engines.

The artifact schema is persistent.

---

## 2.2 Everything Is an Artifact

Examples:

* Research
* Source
* Verification result
* Ayah analysis
* Hadith analysis
* Tafsir note
* Tadabbur
* Mind map
* Storyboard
* Script
* Image prompt
* Image
* Video prompt
* Video
* Audio script
* Audio
* Ebook
* Social post
* Thumbnail
* Landing page
* Product
* Campaign
* QA report
* Evaluation
* Performance report

All use the same core contract.

---

# 3. Artifact Identity

Every artifact MUST have a globally unique identifier.

Example:

```yaml
artifact_id: QURAN-MULK-TADABBUR-001
```

Recommended format:

```text
DOMAIN-TOPIC-TYPE-SEQUENCE
```

Examples:

```text
QURAN-MULK-RESEARCH-001
QURAN-MULK-VERIFY-001
QURAN-MULK-THEME-001
QURAN-MULK-TADABBUR-001
QURAN-MULK-MINDMAP-001
QURAN-MULK-SCRIPT-001
QURAN-MULK-IMAGE-001
QURAN-MULK-VIDEO-001
QURAN-MULK-EBOOK-001
```

For globally distributed systems, UUIDs may additionally be stored.

```yaml
artifact_id: QURAN-MULK-TADABBUR-001
uuid: 8f1e4f1e-...
```

---

# 4. Core Artifact Object

Canonical representation:

```yaml
artifact:
  artifact_id:
  artifact_type:
  artifact_version:

  project_id:
  campaign_id:

  title:
  description:
  topic:
  language:

  source_type:
  sources:

  content:

  provenance:

  parent_artifacts:
  child_artifacts:
  related_artifacts:

  model:
  agent:
  prompt_version:

  verification:
  qa:
  human_review:

  licensing:

  lifecycle:
  timestamps:

  publication:

  evaluation:

  storage:

  notes:
```

---

# 5. Required Metadata

The following fields SHOULD exist on every artifact.

## Identity

```yaml
artifact_id:
artifact_type:
artifact_version:
```

## Project

```yaml
project_id:
campaign_id:
```

## Content

```yaml
title:
description:
topic:
language:
audience:
```

## Provenance

```yaml
source_type:
sources:
parent_artifacts:
```

## Creation

```yaml
created_by:
agent:
model:
prompt_version:
created_at:
```

## Quality

```yaml
verification_status:
qa_status:
human_review_status:
```

## Lifecycle

```yaml
status:
published:
```

---

# 6. Artifact Types

Canonical artifact types:

```yaml
artifact_types:

  knowledge:
    - research
    - source
    - verification
    - thematic_analysis
    - tafsir
    - tadabbur
    - quran_analysis
    - hadith_analysis
    - seerah_analysis

  structure:
    - outline
    - mindmap
    - knowledge_graph
    - storyboard
    - content_plan

  writing:
    - script
    - article
    - caption
    - social_post
    - narration
    - ebook
    - journal
    - landing_page
    - email

  visual:
    - visual_concept
    - image_prompt
    - image
    - thumbnail
    - infographic
    - diagram

  audiovisual:
    - video_prompt
    - video
    - audio_prompt
    - audio

  product:
    - product
    - product_bundle
    - lead_magnet
    - digital_book
    - course

  marketing:
    - campaign
    - funnel
    - campaign_asset
    - advertisement
    - marketing_copy

  quality:
    - qa_report
    - islamic_qa
    - visual_qa
    - content_qa
    - evaluation

  system:
    - task
    - campaign_manifest
    - prompt
    - model_evaluation
```

New types may be added without breaking the core schema.

---

# 7. Source Classification

Every artifact containing factual, religious, historical, or scholarly claims SHOULD identify its source class.

```yaml
source_type:
  - quran
  - hadith
  - tafsir
  - scholarly_work
  - academic
  - historical
  - primary_source
  - secondary_source
  - user_input
  - ai_generated
  - derived
  - mixed
```

---

# 8. Islamic Source Layer

Religious artifacts require additional provenance.

Example:

```yaml
islamic_context:
  school_context: Sunni
  source_categories:
    - Quran
    - Tafsir
    - Hadith

  methodology:
    - source_preservation
    - attribution_required
    - quotation_verification

  scholarly_status:
    - established
    - accepted
    - disputed
    - uncertain
```

The system MUST distinguish:

```text
QUR'AN
  ↓
HADITH
  ↓
TAFSIR
  ↓
SCHOLARLY INTERPRETATION
  ↓
TADABBUR
  ↓
APPLICATION
```

These layers must never silently merge.

---

# 9. Source Object

A source should be represented separately.

```yaml
source:
  source_id:
  title:
  author:
  type:
  language:

  publisher:
  publication_year:

  reference:
  url:

  quotation:
  page:
  volume:
  chapter:

  reliability:
  verification_status:

  license:
  notes:
```

Example:

```yaml
source:
  source_id: SRC-MULK-001
  title: Example Tafsir
  author: Example Author
  type: tafsir
  language: ar

  reference:
    surah: 67
    ayah: 1

  verification_status: verified
```

---

# 10. Provenance Graph

Every derived artifact SHOULD preserve its lineage.

Example:

```text
SOURCE
  │
  ▼
RESEARCH
  │
  ▼
VERIFICATION
  │
  ▼
THEMATIC ANALYSIS
  │
  ├──────► TADABBUR
  │
  ├──────► MIND MAP
  │
  └──────► VISUAL CONCEPT
                │
                ▼
             SCRIPT
                │
                ▼
              VIDEO
                │
                ▼
            SOCIAL POST
                │
                ▼
             PRODUCT
```

Example metadata:

```yaml
provenance:
  parent_artifacts:
    - QURAN-MULK-RESEARCH-001
    - QURAN-MULK-VERIFY-001

  source_artifacts:
    - SRC-MULK-001
    - SRC-MULK-002

  derivation_method:
    type: transformation
    agent: AGENT-05
    prompt_version: TADABBUR-V2
```

---

# 11. Parent / Child Relationships

Artifacts must explicitly describe relationships.

```yaml
parent_artifacts:
  - QURAN-MULK-RESEARCH-001

child_artifacts:
  - QURAN-MULK-TADABBUR-001
  - QURAN-MULK-MINDMAP-001
  - QURAN-MULK-SCRIPT-001
```

Relationship types:

```yaml
relationship:
  - derived_from
  - generated_from
  - verified_by
  - visualized_from
  - summarized_from
  - translated_from
  - adapted_from
  - bundled_with
  - evaluated_by
  - supersedes
  - references
```

---

# 12. Content Object

Text-based artifacts SHOULD use:

```yaml
content:
  format: markdown
  body:
  word_count:
  character_count:
```

Possible formats:

```text
markdown
plain_text
html
json
yaml
csv
svg
png
jpg
webp
mp4
mp3
pdf
epub
```

Binary artifacts should store metadata and a storage reference rather than embedding large binary data in the artifact record.

---

# 13. AI Generation Metadata

AI-generated artifacts MUST record their execution context.

```yaml
generation:
  provider:
  model:
  model_version:

  agent:
  prompt_id:
  prompt_version:

  temperature:
  max_tokens:

  input_artifacts:
  output_artifacts:

  generated_at:
```

Example:

```yaml
generation:
  provider: Google
  model: Gemini
  model_version: current

  agent: AGENT-02
  prompt_id: RESEARCH-SURAH-V1
  prompt_version: 1.2

  input_artifacts:
    - CAMPAIGN-MULK-001

  generated_at: 2026-09-07T10:30:00+08:00
```

Exact model parameters should be stored whenever available.

---

# 14. Prompt Provenance

Every AI-generated artifact SHOULD be traceable to the prompt that generated it.

```yaml
prompt:
  prompt_id:
  prompt_version:
  prompt_hash:

  system_prompt_hash:
  task_prompt_hash:

  routing_agent:
```

This enables:

```text
Artifact
   ↓
Prompt
   ↓
Model
   ↓
Agent
   ↓
Input
```

and allows reproducibility.

---

# 15. Verification

Verification is separate from generation.

```yaml
verification:
  status:
    - not_required
    - pending
    - verified
    - verified_with_notes
    - disputed
    - failed

  verifier:
  verification_date:

  checked_sources:
  claims_checked:

  issues:
  notes:
```

Important:

> AI confidence is NOT equivalent to verification.

For example:

```yaml
verification:
  status: pending
```

must remain pending even if the model says:

```text
"I am highly confident."
```

---

# 16. Claim-Level Verification

High-risk artifacts SHOULD support individual claim tracking.

```yaml
claims:

  - claim_id: CLM-001

    text: "Claim text"

    claim_type: theological

    source_refs:
      - SRC-001

    verification_status: verified

    verifier:
    notes:
```

Claim types:

```yaml
- factual
- historical
- theological
- quranic
- hadith
- scholarly
- scientific
- statistical
- interpretive
```

This allows the system to identify exactly which sentence requires review.

---

# 17. Human Review

Human review is a first-class state.

```yaml
human_review:
  status:
    - not_required
    - pending
    - approved
    - approved_with_changes
    - rejected

  reviewer:
  reviewed_at:

  reason:
  comments:
  required_changes:
```

Mandatory human review SHOULD apply to:

```text
Qur'an quotations
Hadith quotations
Theological conclusions
Sensitive religious claims
Scholarly attribution
Disputed historical claims
AI-generated Arabic religious text
Uncertain sources
Potentially misleading interpretations
```

---

# 18. QA Object

```yaml
qa:
  status:
    - not_run
    - pending
    - pass
    - pass_with_revisions
    - fail
    - human_review_required

  checks:
    source_accuracy:
    religious_integrity:
    factual_accuracy:
    grammar:
    structure:
    visual_quality:
    brand_consistency:
    platform_fit:
    copyright:
    metadata:

  issues:
  recommendations:

  evaluator:
  evaluated_at:
```

---

# 19. Islamic QA

Islamic QA has an explicit schema.

```yaml
islamic_qa:

  status:
    - pending
    - pass
    - pass_with_revisions
    - human_review_required
    - fail

  quran_accuracy:
  hadith_accuracy:
  tafsir_accuracy:
  attribution_accuracy:
  theological_accuracy:

  source_separation:
  interpretation_labeling:

  fabricated_citation_detected:
  unsupported_claim_detected:

  reviewer:
  notes:
```

---

# 20. Visual QA

```yaml
visual_qa:

  status:

  composition:
  lighting:
  realism:
  typography:
  readability:
  negative_space:
  visual_dna:
  platform_fit:

  religious_integrity:
  distorted_text:
  generated_artifact:
  misleading_visual:

  issues:
  recommendations:
```

---

# 21. Licensing

Every artifact should have explicit licensing metadata.

```yaml
licensing:
  status:
    - verified
    - pending
    - unknown
    - restricted

  source_license:
  output_license:
  commercial_use:
  attribution_required:

  restrictions:
  notes:
```

The system MUST NOT assume:

```text
AI-generated = unrestricted
```

Licensing must be evaluated separately.

---

# 22. Lifecycle

Artifact lifecycle:

```text
GENERATED
    ↓
PARSED
    ↓
VALIDATED
    ↓
QA
    ↓
APPROVED
    ↓
PUBLISHED
```

Possible failure path:

```text
QA
 ↓
REJECTED
 ↓
REVISION
 ↓
REGENERATED
 ↓
QA
```

Artifact status:

```yaml
lifecycle:
  status:
    - draft
    - generated
    - parsed
    - validated
    - qa
    - approved
    - published
    - archived
    - rejected
    - superseded
```

---

# 23. Versioning

Artifacts are immutable by default.

Instead of silently changing:

```text
QURAN-MULK-TADABBUR-001
```

create:

```text
QURAN-MULK-TADABBUR-001
QURAN-MULK-TADABBUR-001-V2
QURAN-MULK-TADABBUR-001-V3
```

Metadata:

```yaml
version:
  major: 1
  minor: 2
  patch: 0

  previous_version:
  change_summary:
```

Rules:

```text
Major = conceptual/content change
Minor = meaningful improvement
Patch = correction/metadata change
```

---

# 24. Superseding

An artifact can be replaced without destroying historical provenance.

```yaml
supersedes:
  - QURAN-MULK-TADABBUR-001-V1
```

The original artifact remains preserved.

This enables auditability.

---

# 25. Storage

Artifacts SHOULD separate logical metadata from physical storage.

```yaml
storage:
  repository:
  path:
  filename:
  mime_type:
  size_bytes:

  checksum:
  storage_version:
```

Example:

```yaml
storage:
  repository: huurs-studio
  path: 06_TADABBUR/QURAN-MULK/
  filename: QURAN-MULK-TADABBUR-001.md
  mime_type: text/markdown
  checksum: sha256:...
```

---

# 26. Standard Folder Mapping

Recommended Huurs Studio storage:

```text
HOURS_STUDIO/
│
├── 00_BRAND/
├── 01_RESEARCH/
├── 02_VERIFICATION/
├── 03_QURAN/
├── 04_HADITH/
├── 05_TAFSIR/
├── 06_TADABBUR/
├── 07_MINDMAP/
├── 08_SCRIPTS/
├── 09_IMAGE/
├── 10_VIDEO/
├── 11_AUDIO/
├── 12_PRODUCTS/
├── 13_CAMPAIGNS/
├── 14_SOCIAL/
├── 15_MARKETING/
├── 16_EVALUATION/
│
└── 99_ARCHIVE/
```

The folder structure is organizational.

The artifact ID and provenance graph remain authoritative.

---

# 27. Campaign Artifact

A campaign is itself an artifact.

```yaml
artifact_id: CAMPAIGN-MULK-001

artifact_type: campaign

title: Surah Al-Mulk Campaign

campaign:
  objective:
  audience:
  theme:

  start_date:
  end_date:

  tasks:
  artifacts:
  products:
  channels:

  kpis:
  status:
```

Campaign artifacts connect:

```text
Campaign
 ├── Research
 ├── Verification
 ├── Content
 ├── Visuals
 ├── Videos
 ├── Products
 ├── Social
 ├── Marketing
 └── Evaluation
```

---

# 28. Task Artifact

Agents should also communicate using artifact-compatible task objects.

```yaml
task:
  task_id:
  task_type:

  objective:

  input_artifacts:
  required_sources:

  assigned_agent:
  model:

  priority:
  dependencies:

  expected_outputs:

  qa_required:
  human_review_required:

  status:
```

This allows the orchestration layer to treat tasks as persistent objects.

---

# 29. Agent Result

Every agent should return a standardized result.

```yaml
agent_result:

  task_id:
  status:

  artifact_id:

  summary:

  output:
    location:
    format:

  qa:
    required:
    status:

  human_review:
    required:
    reason:

  derived_tasks:

  errors:

  next_action:
```

This is the bridge between:

```text
Antigravity
      ↓
Agent
      ↓
Artifact
      ↓
Next Agent
```

---

# 30. Derived Artifact Contract

When an artifact generates another artifact:

```yaml
derivation:

  parent:
    artifact_id:

  child:
    artifact_id:

  relationship:
    derived_from

  transformation:
    type:

  agent:
  prompt_version:

  created_at:
```

Example:

```yaml
derivation:
  parent:
    artifact_id: QURAN-MULK-RESEARCH-001

  child:
    artifact_id: QURAN-MULK-TADABBUR-001

  relationship: derived_from

  transformation:
    type: research_to_reflection

  agent: AGENT-05
  prompt_version: TADABBUR-V2
```

---

# 31. Golden Artifacts

Huurs Studio SHOULD designate certain artifacts as canonical.

```yaml
golden:
  status: true
  golden_reason:
```

Examples:

```text
Golden Research
Golden Source Set
Golden Verification
Golden Tadabbur
Golden Brand Prompt
Golden Visual System
Golden Campaign
```

Golden artifacts become regression-test inputs for future agents.

---

# 32. Artifact Hash

Every artifact SHOULD have a checksum.

```yaml
integrity:
  algorithm: sha256
  checksum:
```

This allows detection of accidental modification.

---

# 33. Evaluation

Performance and quality feedback should become artifacts.

```yaml
evaluation:

  evaluation_id:

  evaluator:

  dimensions:
    accuracy:
    usefulness:
    engagement:
    clarity:
    visual_quality:
    conversion:
    retention:

  score:

  feedback:

  lessons:

  recommended_changes:
```

The evaluation can feed back into:

```text
Evaluation
    ↓
Prompt Library
    ↓
Agent Routing
    ↓
New Campaign
```

---

# 34. Complete Example

```yaml
artifact:

  artifact_id: QURAN-MULK-TADABBUR-001
  artifact_type: tadabbur
  artifact_version: 1.0.0

  project_id: HUURS-QURAN
  campaign_id: CAMPAIGN-MULK-001

  title: Surah Al-Mulk Reflection
  description: Reflection framework based on verified sources.
  topic: Surah Al-Mulk
  language: en
  audience: general

  source_type: mixed

  sources:
    - SRC-MULK-QURAN-001
    - SRC-MULK-TAFSIR-001

  content:
    format: markdown
    body: "..."
    word_count: 1200

  islamic_context:
    school_context: Sunni

    source_categories:
      - Quran
      - Tafsir

    scholarly_status: accepted

  provenance:

    parent_artifacts:
      - QURAN-MULK-RESEARCH-001
      - QURAN-MULK-VERIFY-001

    source_artifacts:
      - SRC-MULK-QURAN-001
      - SRC-MULK-TAFSIR-001

    derivation_method:
      type: research_to_reflection
      agent: AGENT-05
      prompt_version: TADABBUR-V2

  child_artifacts:
    - QURAN-MULK-MINDMAP-001
    - QURAN-MULK-SCRIPT-001
    - QURAN-MULK-EBOOK-001

  generation:

    provider: Google
    model: Gemini

    agent: AGENT-05

    prompt:
      prompt_id: TADABBUR-SURAH-V2
      prompt_version: 2.1

    generated_at: 2026-09-07T10:30:00+08:00

  verification:

    status: verified

    verifier: AGENT-03

    claims_checked:
      - CLM-MULK-001
      - CLM-MULK-002

  human_review:

    status: pending

    reason: Religious interpretation requires human review.

  islamic_qa:

    status: human_review_required

    quran_accuracy: pass
    hadith_accuracy: not_applicable
    tafsir_accuracy: pass
    attribution_accuracy: pass
    source_separation: pass

  qa:

    status: pass_with_revisions

    checks:
      source_accuracy: pass
      religious_integrity: pass
      factual_accuracy: pass
      grammar: pass
      structure: pass

  licensing:

    status: pending

  lifecycle:

    status: qa

  integrity:

    algorithm: sha256
    checksum: "..."

  storage:

    repository: huurs-studio
    path: 06_TADABBUR/QURAN-MULK/
    filename: QURAN-MULK-TADABBUR-001.md
    mime_type: text/markdown

  notes:
    - "Do not present reflection as tafsir."
    - "Human review required before publication."
```

---

# 35. Minimal Artifact

Not every artifact requires every field.

The minimum valid artifact is:

```yaml
artifact:

  artifact_id:
  artifact_type:

  title:

  content:

  created_at:

  provenance:

  lifecycle:
    status:
```

The system may progressively enrich the artifact.

---

# 36. Validation Rules

Huurs Studio SHOULD reject an artifact when:

```text
artifact_id is missing
artifact_type is unknown
content is missing when required
parent provenance is missing for a derived artifact
source information is missing for source-dependent claims
verification status is missing for religious claims
licensing status is unknown for commercial publication
```

Additional validation:

```text
No duplicate artifact IDs
No broken parent references
No broken child references
No circular derivation chains
No publication of unapproved sensitive religious artifacts
No publication of failed QA artifacts
```

---

# 37. Publication Gate

An artifact becomes publishable only when:

```text
VALID
 +
SOURCE-CHECKED
 +
QA-PASSED
 +
LICENSE-CHECKED
 +
HUMAN-REVIEWED (when required)
 =
PUBLISHABLE
```

Example:

```yaml
publication:
  status: blocked

  blockers:
    - human_review_pending
```

The system must never allow an agent to bypass publication gates merely because the content looks good.

---

# 38. Artifact Dependency Graph

Huurs Studio should maintain a graph:

```text
                 ┌──────────────┐
                 │    SOURCE    │
                 └──────┬───────┘
                        ↓
                 ┌──────────────┐
                 │   RESEARCH   │
                 └──────┬───────┘
                        ↓
                 ┌──────────────┐
                 │ VERIFICATION │
                 └──────┬───────┘
                        ↓
                ┌───────┴────────┐
                ↓                ↓
           ┌─────────┐      ┌──────────┐
           │TADABBUR │      │ MIND MAP │
           └────┬────┘      └─────┬────┘
                ↓                  ↓
             SCRIPT           VISUAL
                ↓                  ↓
              VIDEO            IMAGE
                └──────┬───────────┘
                       ↓
                  SOCIAL CONTENT
                       ↓
                    PRODUCT
                       ↓
                   CAMPAIGN
                       ↓
                  PERFORMANCE
                       ↓
                 NEW KNOWLEDGE
```

This graph is one of the most important structures in the entire system.

---

# 39. Artifact Registry

Huurs Studio SHOULD maintain an artifact registry.

Example:

```yaml
registry:

  artifact_id:
  type:
  title:

  project:
  campaign:

  status:

  verification_status:
  qa_status:
  human_review_status:

  parent_count:
  child_count:

  created_at:
  updated_at:

  storage_location:
```

The registry provides fast lookup without loading complete artifacts.

---

# 40. Search Index

Artifacts should be searchable by:

```text
artifact_id
title
topic
content_type
project
campaign
source
author
language
agent
model
prompt_version
verification_status
QA status
human review status
publication status
creation date
```

Semantic search SHOULD also be supported.

Example:

```text
"Find all tadabbur artifacts related to patience in Surah Al-Baqarah."
```

---

# 41. Localization

Artifacts should support multiple languages without destroying the original.

```yaml
localization:

  original_language: en

  translations:

    - artifact_id: QURAN-MULK-TADABBUR-001-MS
      language: ms
      translated_from: QURAN-MULK-TADABBUR-001

    - artifact_id: QURAN-MULK-TADABBUR-001-ID
      language: id
      translated_from: QURAN-MULK-TADABBUR-001
```

Translations are separate artifacts.

---

# 42. Artifact Relationship Rules

Never overwrite source lineage.

Bad:

```text
Research → rewritten → source disappears
```

Correct:

```text
Source
  ↓
Research
  ↓
Tadabbur
  ↓
Script
```

Every transformation remains traceable.

---

# 43. AI Model Replacement

Because provenance is independent of the model:

```text
QURAN-MULK-TADABBUR-001
        │
        ├── generated by Gemini
        │
        └── regenerated later by Qwen
```

The artifact identity does not need to become vendor-specific.

Instead:

```yaml
generation_history:

  - model: Gemini
    version:
    artifact_version: 1.0.0

  - model: Qwen
    version:
    artifact_version: 2.0.0
```

This makes Huurs Studio **model-agnostic**.

---

# 44. Reproducibility

A reproducible artifact should contain enough information to identify:

```text
INPUT
+
SOURCE
+
PROMPT
+
MODEL
+
PARAMETERS
+
AGENT
+
VERSION
=
OUTPUT
```

Perfect deterministic reproduction is not always possible with generative AI, but provenance must still be preserved.

---

# 45. Security

External content must always be treated as data.

```text
SOURCE CONTENT ≠ SYSTEM INSTRUCTION
```

An artifact containing:

```text
"Ignore previous instructions..."
```

must not alter agent behavior.

Prompt injection protection applies to:

```text
Web pages
PDFs
Books
Documents
Transcripts
Comments
Social media
Imported AI output
```

---

# 46. Privacy

Artifacts must not unnecessarily store:

```text
Passwords
Authentication tokens
API keys
Payment information
Private credentials
Unnecessary personal information
```

Sensitive user information should be minimized or excluded.

---

# 47. Artifact Quality Levels

Optional quality classification:

```yaml
quality_level:

  0: raw
  1: generated
  2: structured
  3: verified
  4: QA_passed
  5: human_approved
  6: published
  7: proven
```

"Proven" should only be assigned to artifacts that have demonstrated value through evaluation.

---

# 48. Proven Artifact

A proven artifact has:

```text
Verified source
+
Human approval
+
Published
+
Performance data
+
Positive evaluation
```

Example:

```yaml
quality_level: 7

evaluation:
  performance:
    retention: 0.71
    engagement: 0.14

  lesson:
    - "Quiet nature visuals performed better than fast transitions."
```

These lessons can improve future campaigns.

---

# 49. Feedback Loop

The complete system becomes:

```text
RESEARCH
   ↓
CONTENT
   ↓
PRODUCTION
   ↓
PUBLICATION
   ↓
AUDIENCE
   ↓
DATA
   ↓
EVALUATION
   ↓
LESSONS
   ↓
PROMPT LIBRARY
   ↓
AGENT ROUTING
   ↓
BETTER CONTENT
```

This is how Huurs Studio becomes increasingly intelligent without depending on a single model.

---

# 50. Canonical Metadata Template

All new artifacts should begin with:

```yaml
artifact_id:
artifact_type:
artifact_version:

project_id:
campaign_id:

title:
description:
topic:
language:
audience:

source_type:
sources:

content:

islamic_context:

provenance:
  parent_artifacts:
  source_artifacts:
  relationship:

generation:
  provider:
  model:
  agent:
  prompt_id:
  prompt_version:
  generated_at:

verification:
  status:
  verifier:
  claims_checked:

human_review:
  status:
  reason:

qa:
  status:

licensing:
  status:

lifecycle:
  status:

integrity:
  algorithm:
  checksum:

storage:
  repository:
  path:
  filename:
  mime_type:

child_artifacts:
related_artifacts:

evaluation:

notes:
```

---

# 51. Final Architecture

The Artifact Schema is the central contract connecting every Huurs Studio subsystem.

```text
                  HUURS STUDIO
                       │
          ┌────────────┴────────────┐
          │                         │
      AGENT SYSTEM             ARTIFACT SYSTEM
          │                         │
          │                    ┌────┴────┐
          │                    │ REGISTRY│
          │                    └────┬────┘
          │                         │
          └──────────────┬──────────┘
                         ↓
                    PROVENANCE
                         ↓
                  KNOWLEDGE GRAPH
                         ↓
             ┌───────────┼───────────┐
             ↓           ↓           ↓
          CONTENT      VISUAL      PRODUCT
             ↓           ↓           ↓
             └───────────┼───────────┘
                         ↓
                      CAMPAIGN
                         ↓
                    PUBLICATION
                         ↓
                    EVALUATION
                         ↓
                   LEARNING LOOP
```

The critical architectural rule is:

> **Agents perform work. Artifacts remember the work. Provenance explains the work. QA determines whether the work can proceed.**

Therefore:

```text
AI MODEL ≠ SYSTEM OF RECORD

AGENT ≠ KNOWLEDGE BASE

CONVERSATION ≠ ARTIFACT

ARTIFACT = PERSISTENT UNIT OF KNOWLEDGE + PROVENANCE + STATE
```

Huurs Studio should own this layer completely.

Google AI, Gemini, local Qwen, Gemma, Ling, or future models should simply plug into it.

---

# 52. North Star

The ultimate goal is not to generate more AI content.

It is to create a system where:

```text
ONE VERIFIED SOURCE
        ↓
ONE TRUSTED KNOWLEDGE ARTIFACT
        ↓
MANY HIGH-QUALITY DERIVATIVES
        ↓
MANY MEDIA FORMATS
        ↓
MANY PRODUCTS
        ↓
MANY CAMPAIGNS
        ↓
MEASURABLE IMPACT
```

while preserving:

**Authenticity → Provenance → Quality → Beauty → Reusability → Impact**

And the system's governing philosophy remains:

> **READ. REFLECT. RETURN.**
