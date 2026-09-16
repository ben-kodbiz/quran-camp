# HUURS STUDIO — ZERO BURNED-IN SUBTITLE MANDATE
**Series:** Come Back to the Qur'an (Flagship Series)  
**Effective Date:** 2026-09-11  
**Scope:** All Existing Episodes (EP01–EP10) and All Future Episodes (EP11–EP20+)  
**Status:** Authoritative Production Policy  

---

## 1. Background & Rationale
In initial video prototypes and pilot renders, English subtitles were burned directly into video pixels via FFmpeg's `libass` filter. In practice, this introduced two fundamental flaws:
1. **Audio-Visual Drift & Sync Mismatch:** In multi-minute contemplative voiceovers with deliberate pauses, natural breathing cadence, and reverent pacing, hardcoded subtitle timing timestamps frequently drift out of synchronization with the voiceover, causing jarring discordance.
2. **Visual Clutter & Disruption of Tadabbur:** Burned-in text obscures the natural living-creation visuals (ocean waves, birds, trees, horses, raindrops) and disrupts the viewer's tranquil immersion.

---

## 2. Core Mandates

### Mandate 1: Absolute Prohibition of Burned-In Subtitles
- **No video master** (16:9 Full Master or 9:16 Vertical Short) produced for the *Come Back to the Qur'an* series may contain hardcoded or burned-in subtitles in its video stream.
- All FFmpeg assembly scripts and rendering pipelines must strictly exclude `subtitles=...` filters from their filtergraphs.

### Mandate 2: Pure Visual Composition & Trademark Watermark
The video stream must contain **only**:
1. High-fidelity cinematic nature footage (color graded, stabilized, contemplative pacing).
2. Optional subtle film grain (`noise=c0s=1.2:allf=t`) and gentle head/tail fades.
3. The official discrete trademark watermark:
   - Text: `HUURS STUDIO`
   - Font: IBM Plex Serif
   - Size: 16px (16:9 masters) / 14px (9:16 vertical shorts)
   - Color: `white@0.22` (subtle, non-distracting opacity)
   - Position: Lower-right corner (`x=w-tw-40:y=h-th-30` or `x=w-tw-30:y=h-th-45`)

### Mandate 3: Platform Captions via External Sidecars Only
- If text captions are needed for accessibility or platform distribution (YouTube CC, Facebook, TikTok/Instagram auto-captions), they must be generated and distributed exclusively as external sidecar files (`.srt` or `.vtt`).
- Viewers retain the choice to toggle captions on or off on their viewing platform without permanently altering the video frames.

### Mandate 4: Future Template Enforcement
- Any script generator, pipeline automation, or future episode script (EP11 through EP20) must inherit this clean, subtitle-free composition by default.
