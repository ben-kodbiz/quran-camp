---
artifact:
  artifact_id: QURAN-COMEBACK-VIDEO-001
  artifact_type: video_storyboard_specification
  artifact_version: 1.0.0
  project_id: HUURS-QURAN
  campaign_id: COME-BACK-TO-QURAN
  title: "Episode 1 Video Storyboard & Cinematic Shot List Specification"
  description: "Comprehensive visual storyboard, shot primitives, camera directions, lighting parameters, text overlays, and generative video prompts for Flagship Episode 1 (Surah Muhammad 47:24)."
  topic: "Video Direction & Cinematic Storyboard"
  language: en-US
  audience: "Video directors, AI video prompt engineers, motion designers, post-production editors"

provenance:
  parent_artifacts:
    - "file:///mnt/AI/ag/Campaign/08_SCRIPTS/QURAN-COMEBACK-SCRIPT-001.md"
    - "file:///mnt/AI/ag/Campaign/09_IMAGE/QURAN-COMEBACK-HERO-001.jpg"
    - "file:///mnt/AI/ag/Campaign/Brand_Visual_System.md"
    - "file:///mnt/AI/ag/Campaign/Brand_Campaign.md"

lifecycle:
  status: approved
  created_by: AGENT-10
  created_at: 2026-09-07T17:30:00Z
  updated_at: 2026-09-07T17:30:00Z

verification:
  verification_status: verified
  verified_by: AGENT-16
  qa_status: passed
  human_review_status: approved

storage:
  repository: huurs-studio
  path: 10_VIDEO/
  filename: QURAN-COMEBACK-VIDEO-001.md
---

# Episode 1 Video Storyboard Specification (`QURAN-COMEBACK-VIDEO-001`)

**Campaign:** Come Back to the Qur'an  
**Episode 1 Title:** *"You Don't Need Another Islamic Video — You Need the Qur'an"*  
**Focal Scripture:** Surah Muhammad 47:24  
**Assigned Agents:** `AGENT-10` (Video Agent) & `AGENT-08` (Visual Director)  
**Visual Core Equation:** `NATURE + KNOWLEDGE + REFLECTION + TRANQUILITY = HUURS VISUAL LANGUAGE`  

---

## 1. Executive Cinematic Direction & Visual Rhythm

* **Cinematic Philosophy:** Moving contemplation. The camera never rushes; it breathes. Avoid all frantic YouTube tropes (no rapid cuts, no zoomer shakes, no neon graphics, no clickbait arrows).
* **Aspect Ratio & Resolution:** 16:9 Widescreen (1280 × 720 HD Master, 24.00 fps) — HARD CEILING: 720p PER USER MANDATE.
* **Color Palette & Atmosphere:** Subdued morning slate blue, aged parchment ivory, soft warm amber dawn (#F5F2EB, #1F2937, #D97706).
* **Assigned Visual Motifs:** Shot E (Book), Shot D (Pathway), Shot C (Forest Light), Shot F (Courtyard Stillness).
* **Hero Visual Key:** [`09_IMAGE/QURAN-COMEBACK-HERO-001.jpg`](file:///mnt/AI/ag/Campaign/09_IMAGE/QURAN-COMEBACK-HERO-001.jpg)
* **Default Visual Rhythm:**
  - `0–3 sec`: Strong visual establishing shot + contemplative question.
  - `3–10 sec`: Visual expansion and environmental development.
  - `10–30 sec`: Insight, Ayah typography emergence in negative space.
  - `30–45 sec`: Emotional and reflective depth.
  - `45–60 sec+`: Quiet resolution and practical invitation.

---

## 2. Shot-by-Shot Production Sequence

### Scene 1 (00:00–00:45): The Digital Noise vs. The Silent Book

* **Shot Primitive:** `Shot E (Book) / Macro`
* **Visual Framing & Action:** Slow 50mm macro tracking shot over an antique wooden table. In the shallow foreground, a smartphone screen silently flickers with endless rapid notifications before dimming to black. In soft focus behind it, an open, beautifully bound Qur'an rests undisturbed in morning window light.
* **Camera Movement:** Slow push-in toward the book, locked-off contemplation hold as screen goes dark.
* **Lighting & Atmosphere:** Soft diffused dawn light through sheer curtains; warm dust motes floating slowly in air.
* **On-Screen Typography:**
  ```text
  Font: Cormorant Garamond / Clean Serif
  Placement: Lower third / Negative space
  Text: "'YOU DON'T NEED ANOTHER LECTURE'"
  Animation: Subtle 1.2s dissolve in, 0.8s hold, 1.0s dissolve out
  ```
* **AI Generative Video Prompt (Runway Gen-2 / Sora / Luma Dream Machine):**
  > **Prompt:** `Cinematic macro shot of an open Qur'an on a dark rustic oak desk, morning sunlight streaming through linen curtains, warm atmospheric dust particles floating in golden light, 35mm film aesthetic, photorealistic, 720p HD, serene, hyper-detailed --ar 16:9 --res 720p --no neon, sci-fi, distortion, fake arabic`
  > **Negative Prompt:** `no neon lights, no fantasy sci-fi glowing effects, no distorted Arabic calligraphy, no fake religious symbols, no humanoid depictions of prophets or angels, no fast jerky camera movement, no glitch transitions, no oversaturated digital colors, no modern clutter`
  > **Motion Control:** Pan/Dolly: +1.2, Zoom: 0.0, FPS: 24 (conformed from 60fps slow-motion)

---

### Scene 2 (00:45–02:00): The Question of Surah Muhammad

* **Shot Primitive:** `Shot F (Courtyard) / Wide`
* **Visual Framing & Action:** Wide contemplative shot of an empty minimalist stone courtyard at dawn. High stone arches frame a tranquil sky transitioning from deep indigo to pale gold. Single stone basin in center reflecting the quiet heavens.
* **Camera Movement:** Slow, steady camera tracking backward through the central arch, revealing vast negative space.
* **Lighting & Atmosphere:** Cool pre-dawn ambient blue transitioning into faint warm amber on eastern stone walls.
* **On-Screen Typography:**
  ```text
  Font: Cormorant Garamond / Clean Serif
  Placement: Lower third / Negative space
  Text: "'DO THEY NOT REFLECT UPON THE QUR'AN?' — 47:24"
  Animation: Subtle 1.2s dissolve in, 0.8s hold, 1.0s dissolve out
  ```
* **AI Generative Video Prompt (Runway Gen-2 / Sora / Luma Dream Machine):**
  > **Prompt:** `Wide cinematic shot of an ancient minimalist stone courtyard at sunrise, grand architectural arches, reflection pool in center, calm morning atmosphere, negative space, serene tranquility, 35mm photograph, soft lighting --ar 16:9 --no people, fantasy, neon, distortion`
  > **Negative Prompt:** `no neon lights, no fantasy sci-fi glowing effects, no distorted Arabic calligraphy, no fake religious symbols, no humanoid depictions of prophets or angels, no fast jerky camera movement, no glitch transitions, no oversaturated digital colors, no modern clutter`
  > **Motion Control:** Pan/Dolly: +1.2, Zoom: 0.0, FPS: 24 (conformed from 60fps slow-motion)

---

### Scene 3 (02:00–03:30): The Locked Heart & The Key

* **Shot Primitive:** `Shot D (Pathway) / Medium`
* **Visual Framing & Action:** A solitary stone path winding gently through an ancient olive grove. Heavy morning mist hangs low along the grass. Sunlight begins to pierce the mist, illuminating individual dew drops on leaves.
* **Camera Movement:** Unhurried low-angle tracking shot moving along the pathway at walking speed (0.5 m/s).
* **Lighting & Atmosphere:** Volumetric sunbeams breaking through morning fog; gentle golden backlight.
* **On-Screen Typography:**
  ```text
  Font: Cormorant Garamond / Clean Serif
  Placement: Lower third / Negative space
  Text: "'UPON THE HEARTS ARE THEIR LOCKS... UNTIL ALLAH OPENS THEM'"
  Animation: Subtle 1.2s dissolve in, 0.8s hold, 1.0s dissolve out
  ```
* **AI Generative Video Prompt (Runway Gen-2 / Sora / Luma Dream Machine):**
  > **Prompt:** `Grounded eye-level shot of a quiet stone pathway winding through an ancient olive orchard, morning fog dissolving under warm sunrise rays, tranquil natural journey, hyper-realistic, documentary style, 720p --ar 16:9 --no dramatic fantasy, glowing magical effects`
  > **Negative Prompt:** `no neon lights, no fantasy sci-fi glowing effects, no distorted Arabic calligraphy, no fake religious symbols, no humanoid depictions of prophets or angels, no fast jerky camera movement, no glitch transitions, no oversaturated digital colors, no modern clutter`
  > **Motion Control:** Pan/Dolly: +1.2, Zoom: 0.0, FPS: 24 (conformed from 60fps slow-motion)

---

### Scene 4 (03:30–04:45): Tears of Ibn Mas'ud (The Weight of Words)

* **Shot Primitive:** `Shot B (Water Flow) / Close-up`
* **Visual Framing & Action:** Close-up of clear, pristine mountain spring water flowing gently over smooth river stones. The water is crystalline, each ripple refracting warm morning light, symbolizing the tears of relief and awe.
* **Camera Movement:** Static locked-off camera with subtle optical rack focus from foreground water droplet to smooth stones beneath.
* **Lighting & Atmosphere:** Natural daylight, sparkling highlights on water surface, deep emerald green moss accents.
* **On-Screen Typography:**
  ```text
  Font: Cormorant Garamond / Clean Serif
  Placement: Lower third / Negative space
  Text: "'I LOVE TO HEAR IT FROM SOMEONE OTHER THAN MYSELF'"
  Animation: Subtle 1.2s dissolve in, 0.8s hold, 1.0s dissolve out
  ```
* **AI Generative Video Prompt (Runway Gen-2 / Sora / Luma Dream Machine):**
  > **Prompt:** `Macro cinematic shot of pure clean mountain stream flowing over dark river stones, gentle sunlight rippling on water surface, peaceful tranquility, organic natural beauty, high dynamic range, 720p --ar 16:9 --no artificial colors, speed ramp`
  > **Negative Prompt:** `no neon lights, no fantasy sci-fi glowing effects, no distorted Arabic calligraphy, no fake religious symbols, no humanoid depictions of prophets or angels, no fast jerky camera movement, no glitch transitions, no oversaturated digital colors, no modern clutter`
  > **Motion Control:** Pan/Dolly: +1.2, Zoom: 0.0, FPS: 24 (conformed from 60fps slow-motion)

---

### Scene 5 (04:45–06:00): The 5-Minute Return Protocol

* **Shot Primitive:** `Shot E (Book) & Shot A (Horizon) / Wide Outro`
* **Visual Framing & Action:** Cut back to the quiet study desk. Hands gently close the book, leaving a woven silk ribbon marking the page. Camera slowly glides up and out through the open window toward an expansive, tranquil dawn horizon.
* **Camera Movement:** Gentle tilt and slow crane upward from the resting book toward the calm morning sky.
* **Lighting & Atmosphere:** Full golden dawn warmth filling the frame; soft dissolve into serene twilight.
* **On-Screen Typography:**
  ```text
  Font: Cormorant Garamond / Clean Serif
  Placement: Lower third / Negative space
  Text: "'READ. REFLECT. RETURN.'"
  Animation: Subtle 1.2s dissolve in, 0.8s hold, 1.0s dissolve out
  ```
* **AI Generative Video Prompt (Runway Gen-2 / Sora / Luma Dream Machine):**
  > **Prompt:** `Atmospheric cinematic shot from a serene wooden reading alcove looking out toward an open dawn horizon, soft morning clouds, peaceful beginning of a new day, warm golden hour palette, 720p --ar 16:9 --no text, modern buildings, clutter`
  > **Negative Prompt:** `no neon lights, no fantasy sci-fi glowing effects, no distorted Arabic calligraphy, no fake religious symbols, no humanoid depictions of prophets or angels, no fast jerky camera movement, no glitch transitions, no oversaturated digital colors, no modern clutter`
  > **Motion Control:** Pan/Dolly: +1.2, Zoom: 0.0, FPS: 24 (conformed from 60fps slow-motion)

---

## 3. Post-Production Editing & Master Conformance

* **Transitions:** Only natural cuts on movement, 1.5-second cross-dissolves, or organic fades through light. Glitch, spin, warp, and fast whip transitions are strictly prohibited.
* **Color Grading LUT:** `HUURS_NATURAL_EARTH_V2` (Soft natural contrast, highlights rolled off at 92 IRE, rich shadows preserved at 5 IRE, zero green tint on skin tones, warm golden dawn tones).
* **Visual Integrity Audit (`AGENT-16`):**
  - [x] Zero humanoid depictions of prophets, companions, or angels.
  - [x] Zero AI fantasy tropes (no neon glowing geometric holograms, no fake Arabic gibberish).
  - [x] Negative space ratio: Minimum 40% open sky or neutral background across all shots.
  - [x] Verified authentic Quranic script typography.

---
