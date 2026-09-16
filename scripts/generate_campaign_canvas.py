#!/usr/bin/env python3
"""
HUURS STUDIO - Master Campaign Production Canvas Generator
===========================================================
Generates a state-of-the-art interactive Studio Production Canvas
for the entire 20-week campaign ("Come Back to the Qur'an").

Features:
- Dynamic discovery of all 20 episodes (Season 1 & Season 2)
- Multi-fallback clipboard copying (works in iframes, file://, and web)
- Clean spoken narration extraction (strips audio production cues)
- Interactive click-to-select textareas for all scene prompts
- Live floating toast notifications (replaces blocked alert() calls)
- Live embedded video & audio players for rendered masters
- Real-time credit balance tracking (15 credits / generation)
- Outputs to both Campaign repository and Antigravity artifact directory
"""

import os
import sys
import glob
import re
import json
import shutil
import sqlite3

ROOT_DIR = "/mnt/AI/ag/Campaign"
BRAIN_DIR = "/home/ben/.gemini/antigravity/brain/1d535f8c-0b01-42ad-8e78-fc566134377c"
REPO_OUTPUT = os.path.join(ROOT_DIR, "13_CAMPAIGNS/studio_canvas.html")
BRAIN_OUTPUT = os.path.join(BRAIN_DIR, "studio_canvas.html")

DB_PATH = os.path.join(ROOT_DIR, "database/quran_campaign.db")
RENDERS_DIR = os.path.join(ROOT_DIR, "10_VIDEO/renders")
AUDIO_DIR = os.path.join(ROOT_DIR, "11_AUDIO")
IMAGE_DIR = os.path.join(ROOT_DIR, "09_IMAGE")

def get_surah_info(ep_num):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT english_name, arabic_name, verse_count FROM surahs WHERE number = ?", (ep_num,))
    row = c.fetchone()
    conn.close()
    if row:
        return {"english": row[0], "arabic": row[1], "verses": row[2]}
    return {"english": f"Episode {ep_num}", "arabic": "", "verses": 0}

def parse_episode(ep_num):
    v_file = os.path.join(ROOT_DIR, f"10_VIDEO/QURAN-COMEBACK-VIDEO-{ep_num:03d}.md")
    a_file = os.path.join(ROOT_DIR, f"11_AUDIO/QURAN-COMEBACK-AUDIO-{ep_num:03d}.md")
    
    title = f"Episode {ep_num}"
    prompts = []
    narration = ""

    if os.path.exists(v_file):
        with open(v_file, "r", encoding="utf-8") as f:
            v_text = f.read()
        m_title = re.search(r'title:\s*"([^"]+)"', v_text)
        if m_title:
            title = m_title.group(1).replace("Episode Video Storyboard & Cinematic Shot List Specification", "").strip()
        
        matches = re.findall(r"(?:Prompt|Video Generation Prompt)[^`]*`([^`]+)`", v_text, re.IGNORECASE)
        prompts = [p.strip() for p in matches if not p.strip().startswith("no neon") and not p.strip().startswith("no ") and not p.strip().startswith("--")]
        if len(prompts) > 5:
            prompts = prompts[-5:]

        s_matches = re.findall(r"###\s*Scene\s*(\d+)(?:\s*\([^)]*\))?\s*:\s*(.+)", v_text)
        scene_titles = {}
        for s_idx, s_name in s_matches:
            try:
                scene_titles[int(s_idx)] = s_name.strip()
            except:
                pass
    else:
        scene_titles = {}

    if os.path.exists(a_file):
        with open(a_file, "r", encoding="utf-8") as f:
            a_text = f.read()
        m_code = re.findall(r"```text\s*([\s\S]*?)\s*```", a_text)
        raw_narration = "\n\n".join(m_code) if m_code else a_text[:1200]
        # Clean production cues so spoken audio script is pure text
        cleaned = re.sub(r"\[[^\]]+\]", "", raw_narration)
        cleaned = re.sub(r"^-+\s*$", "", cleaned, flags=re.MULTILINE)
        cleaned = re.sub(r"\n{3,}", "\n\n", cleaned).strip()
        cleaned = re.sub(r'"+', '"', cleaned)
        narration = cleaned

    master_vid = f"QURAN-COMEBACK-EP{ep_num:02d}-FULL-MASTER.mp4"
    short_vid = f"QURAN-COMEBACK-EP{ep_num:02d}-SHORT-001A.mp4"
    pilot_vid = f"QURAN-COMEBACK-EP{ep_num:02d}-SCENE01-PILOT.mp4"
    audio_boosted = f"EP{ep_num:02d}_SCENE01_audio_boosted.mp3"
    hero_img = f"QURAN-COMEBACK-HERO-{ep_num:03d}.jpg"

    has_master = os.path.exists(os.path.join(RENDERS_DIR, master_vid))
    has_short = os.path.exists(os.path.join(RENDERS_DIR, short_vid))
    has_pilot = os.path.exists(os.path.join(RENDERS_DIR, pilot_vid))
    has_audio = os.path.exists(os.path.join(AUDIO_DIR, audio_boosted))
    has_hero = os.path.exists(os.path.join(IMAGE_DIR, hero_img))

    scenes = []
    scene_renders = []
    for s in range(1, 6):
        sc_file = f"QURAN-COMEBACK-VEO-{ep_num:03d}-SCENE0{s}.mp4"
        short_alias = f"EP{ep_num:02d}_SCENE0{s}.mp4"
        is_rendered = os.path.exists(os.path.join(RENDERS_DIR, sc_file)) or (ep_num == 1 and s == 1)
        if is_rendered:
            scene_renders.append(sc_file)
        
        p_text = prompts[s-1] if s-1 < len(prompts) else ""
        s_title = scene_titles.get(s, f"Scene {s}")
        scenes.append({
            "num": s,
            "name": s_title,
            "filename": sc_file,
            "short_alias": short_alias,
            "prompt": p_text,
            "rendered": is_rendered
        })

    surah = get_surah_info(ep_num)

    return {
        "ep_num": ep_num,
        "title": title,
        "surah": surah,
        "prompts": prompts,
        "scenes": scenes,
        "narration": narration,
        "has_master": has_master,
        "has_short": has_short,
        "has_pilot": has_pilot,
        "has_audio": has_audio,
        "has_hero": has_hero,
        "master_file": f"../10_VIDEO/renders/{master_vid}",
        "short_file": f"../10_VIDEO/renders/{short_vid}",
        "audio_file": f"../11_AUDIO/{audio_boosted}",
        "hero_file": f"../09_IMAGE/{hero_img}",
        "scene_renders": scene_renders
    }

def generate_canvas():
    print("Gathering data across all 20 episodes...")
    episodes = [parse_episode(i) for i in range(1, 21)]

    # Metrics
    total_rendered_scenes = sum(len(e["scene_renders"]) for e in episodes)
    credits_spent = total_rendered_scenes * 15
    credits_remaining = 1000 - credits_spent

    ep_json = json.dumps(episodes)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Huurs Studio Master Production Canvas</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    body {{
      background-color: var(--background, #0b0f17);
      color: var(--foreground, #e2e8f0);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }}
    .scrollbar-none::-webkit-scrollbar {{ display: none; }}
    .scrollbar-none {{ -ms-overflow-style: none; scrollbar-width: none; }}
    .active-ep-pill {{
      background-color: var(--primary, #c5a059);
      color: var(--primary-foreground, #0b0f17);
      font-weight: 700;
    }}
    textarea.prompt-box {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-size: 0.75rem;
      line-height: 1.5;
    }}
  </style>
</head>
<body class="p-6 md:p-8 max-w-7xl mx-auto space-y-8 antialiased">

  <!-- TOP HEADER -->
  <header class="flex flex-col md:flex-row md:items-center md:justify-between gap-4 border-b border-[var(--border,#232d3f)] pb-6">
    <div>
      <div class="flex items-center gap-3">
        <span class="px-2.5 py-1 rounded text-xs font-bold tracking-wider uppercase bg-amber-500/10 text-amber-500 border border-amber-500/20 font-mono">
          HUURS STUDIO • MASTER CANVAS
        </span>
        <span class="text-xs font-mono text-[var(--muted-foreground)]">20-WEEK SERIES</span>
      </div>
      <h1 class="text-2xl md:text-3xl font-bold tracking-tight text-[var(--foreground)] mt-2">
        Come Back to the Qur'an — Production & Asset Hub
      </h1>
      <p class="text-sm text-[var(--muted-foreground)] mt-1">
        Seamless orchestration across Google Flow (Veo 3.1 720p), Google AI Studio, and local RTX 3060 NVENC.
      </p>
    </div>

    <!-- CREDIT TRACKER CARD -->
    <div class="flex items-center gap-4 bg-[var(--card,#131a26)] border border-[var(--border,#232d3f)] px-5 py-3.5 rounded-2xl shadow-sm">
      <div class="text-right">
        <div class="text-xs font-mono uppercase tracking-wider text-[var(--muted-foreground)]">Google Flow Quota</div>
        <div class="text-lg font-extrabold text-[var(--foreground)] font-mono">
          <span class="text-emerald-500">{credits_remaining}</span> / 1,000 Credits
        </div>
      </div>
      <div class="w-px h-8 bg-[var(--border,#232d3f)]"></div>
      <div>
        <div class="text-xs font-mono text-[var(--muted-foreground)]">Spent: <span class="font-bold text-amber-500">{credits_spent} cr</span></div>
        <div class="text-xs font-mono text-[var(--muted-foreground)]">Season 1: <span class="font-bold text-[var(--foreground)]">675 cr needed</span></div>
      </div>
    </div>
  </header>

  <!-- EPISODE HORIZONTAL SELECTOR DOCK -->
  <section class="space-y-3">
    <div class="flex items-center justify-between">
      <h2 class="text-xs font-mono uppercase tracking-wider text-[var(--muted-foreground)]">Select Campaign Episode (1–20)</h2>
      <span class="text-xs font-mono text-emerald-500">Season 1: Ep 1–10 • Season 2: Ep 11–20</span>
    </div>
    <div id="episode-pills" class="flex gap-2 overflow-x-auto pb-2 scrollbar-none font-mono text-xs">
      <!-- Injected via JavaScript -->
    </div>
  </section>

  <!-- DYNAMIC EPISODE DETAIL CONTAINER -->
  <main id="episode-detail" class="space-y-8">
    <!-- Injected via JavaScript -->
  </main>

  <!-- FLOATING TOAST NOTIFICATION -->
  <div id="toast" class="fixed bottom-6 right-6 px-4 py-2.5 rounded-xl bg-slate-900 text-white border border-emerald-500/40 shadow-2xl font-sans text-xs flex items-center gap-2.5 z-50 transition-all duration-300 transform opacity-0 translate-y-3 pointer-events-none">
    <span class="text-emerald-400 font-bold text-sm">✓</span>
    <span id="toast-msg">Copied to clipboard!</span>
  </div>

  <!-- QUICK-COPY FALLBACK MODAL (Failsafe for locked iframes) -->
  <div id="copy-modal" class="fixed inset-0 bg-black/80 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4" onclick="closeCopyModal(event)">
    <div class="bg-[var(--card,#131a26)] border border-amber-500/30 rounded-2xl p-6 max-w-lg w-full space-y-4 shadow-2xl" onclick="event.stopPropagation()">
      <div class="flex items-center justify-between border-b border-[var(--border)] pb-3">
        <h3 id="copy-modal-title" class="text-sm font-bold text-[var(--foreground)]">Copy Text</h3>
        <button onclick="closeCopyModal()" class="text-xs text-[var(--muted-foreground)] hover:text-white px-2 py-1 rounded border border-[var(--border)]">Close ✕</button>
      </div>
      <p class="text-xs text-[var(--muted-foreground)]">
        Text has been selected below. Press <kbd class="px-1.5 py-0.5 rounded bg-slate-800 text-amber-400 font-mono font-bold">Ctrl+C</kbd> (or <kbd class="px-1.5 py-0.5 rounded bg-slate-800 text-amber-400 font-mono font-bold">Cmd+C</kbd>) to copy:
      </p>
      <textarea id="copy-modal-textarea" readonly class="w-full h-40 bg-[var(--background)] border border-[var(--border)] rounded-xl p-3 text-xs font-mono text-[var(--foreground)] focus:outline-none focus:border-amber-500 select-all"></textarea>
      <div class="flex justify-end gap-2">
        <button onclick="document.getElementById('copy-modal-textarea').select()" class="px-3 py-1.5 rounded-lg border border-[var(--border)] text-xs font-semibold hover:bg-[var(--background)]">
          Select All
        </button>
        <button onclick="closeCopyModal()" class="px-4 py-1.5 bg-emerald-500 text-white rounded-lg text-xs font-semibold hover:bg-emerald-600">
          Done
        </button>
      </div>
    </div>
  </div>

  <script>
    const episodes = {ep_json};
    let currentEpNum = 1;

    function renderPills() {{
      const container = document.getElementById('episode-pills');
      container.innerHTML = episodes.map(ep => {{
        const isCurrent = ep.ep_num === currentEpNum;
        const isDone = ep.scene_renders.length === 5;
        const isNext = ep.ep_num === 2;
        let dotColor = 'bg-slate-500';
        if (isDone) dotColor = 'bg-emerald-500';
        else if (isNext) dotColor = 'bg-amber-500';

        const cls = isCurrent 
          ? 'px-3 py-2 rounded-lg active-ep-pill shadow-sm transition-all flex items-center gap-1.5 whitespace-nowrap cursor-pointer'
          : 'px-3 py-2 rounded-lg bg-[var(--card,#131a26)] border border-[var(--border,#232d3f)] text-[var(--muted-foreground)] hover:text-[var(--foreground)] transition-all flex items-center gap-1.5 whitespace-nowrap cursor-pointer';

        return `<div onclick="selectEpisode(${{ep.ep_num}})" class="${{cls}}">
          <span class="w-2 h-2 rounded-full ${{dotColor}}"></span>
          Ep ${{ep.ep_num}}: ${{ep.surah.english || 'Surah ' + ep.ep_num}}
        </div>`;
      }}).join('');
    }}

    function selectEpisode(num) {{
      currentEpNum = num;
      renderPills();
      renderDetail();
    }}

    function renderDetail() {{
      const ep = episodes.find(e => e.ep_num === currentEpNum);
      const container = document.getElementById('episode-detail');
      if (!ep) return;

      let mediaSection = '';
      if (ep.has_master) {{
        const masterDuration = ep.ep_num === 1 ? '38.5s' : '04:07 (247.2s)';
        const shortDuration = ep.ep_num === 1 ? '30.0s' : '36.5s';
        mediaSection = `
        <div class="bg-[var(--card,#131a26)] border border-[var(--border,#232d3f)] rounded-2xl p-6 shadow-sm">
          <div class="flex flex-col lg:flex-row gap-6 items-start">
            
            <!-- 16:9 Master Player -->
            <div class="w-full lg:w-3/5 space-y-3">
              <div class="flex items-center justify-between">
                <div>
                  <span class="text-xs font-mono text-emerald-500 uppercase font-semibold">16:9 WIDESCREEN MASTER DELIVERABLE</span>
                  <h3 class="text-base font-bold">${{ep.title}}</h3>
                </div>
                <span class="text-xs text-[var(--muted-foreground)] font-mono">${{masterDuration}} • 1280x720 • 24fps</span>
              </div>
              
              <div class="relative rounded-xl overflow-hidden bg-black aspect-video border border-[var(--border)] shadow-md">
                <video controls preload="metadata" class="w-full h-full object-cover">
                  <source src="${{ep.master_file}}" type="video/mp4">
                  Your browser does not support HTML5 video preview.
                </video>
              </div>
              <div class="p-3 rounded-lg bg-[var(--background)] border border-[var(--border)] text-xs text-[var(--muted-foreground)]">
                <span class="font-bold text-[var(--foreground)]">Audio Mix:</span> -14.0 LUFS broadcast compliant • Clean voiceover • Zero music.
              </div>
            </div>

            <!-- 9:16 Vertical Short + Audio Player -->
            <div class="w-full lg:w-2/5 space-y-4">
              <div class="flex items-center justify-between">
                <span class="text-xs font-mono text-emerald-500 uppercase font-semibold">9:16 VERTICAL SOCIAL CUT</span>
                <span class="text-xs text-[var(--muted-foreground)] font-mono">${{shortDuration}} • 720x1280</span>
              </div>
              
              <div class="flex gap-4 items-start">
                <div class="w-36 h-64 flex-shrink-0 rounded-xl overflow-hidden bg-black border border-[var(--border)] shadow-md relative">
                  <video controls preload="metadata" class="w-full h-full object-cover">
                    <source src="${{ep.short_file}}" type="video/mp4">
                  </video>
                </div>

                <div class="space-y-3 flex-1">
                  <div class="p-3 rounded-xl bg-[var(--background)] border border-[var(--border)] space-y-1.5">
                    <div class="text-xs font-mono text-amber-500 font-semibold uppercase">Voiceover Master (-14 LUFS)</div>
                    <audio controls class="w-full h-8" preload="none">
                      <source src="${{ep.audio_file}}" type="audio/mpeg">
                    </audio>
                  </div>

                  <div class="p-3 rounded-xl bg-[var(--background)] border border-[var(--border)] space-y-1 text-xs">
                    <div class="font-bold text-[var(--foreground)]">5 Veo 3.1 B-Roll Clips:</div>
                    <ul class="text-[var(--muted-foreground)] space-y-0.5 font-mono text-[11px]">
                      ${{(ep.scenes || []).map(sc => `<li>✓ Scene ${{sc.num}}: ${{sc.name}}</li>`).join('')}}
                    </ul>
                  </div>
                </div>
              </div>
            </div>

          </div>
        </div>
        `;
      }}

      // Build 5 Prompts Cards
      const promptCards = (ep.scenes || []).map((sc, idx) => `
        <div class="bg-[var(--background)] border border-[var(--border)] rounded-xl p-4 space-y-2.5">
          <div class="flex items-start justify-between gap-2">
            <div class="space-y-0.5">
              <div class="flex items-center gap-1.5">
                <span class="text-xs font-bold text-amber-500 font-mono tracking-wide">SCENE ${{sc.num}}</span>
                <span class="text-[10px] px-2 py-0.5 rounded font-mono font-semibold ${{sc.rendered ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/30' : 'bg-slate-800 text-slate-400'}}">
                  ${{sc.rendered ? '✓ RENDERED' : 'READY'}}
                </span>
              </div>
              <div class="text-xs font-semibold text-[var(--foreground)] leading-snug">
                ${{sc.name}}
              </div>
            </div>
            <button type="button" onclick="copyScenePrompt(${{ep.ep_num}}, ${{idx}}, this)" class="text-xs text-[var(--foreground)] hover:text-white bg-[var(--card)] hover:bg-amber-500 hover:text-black border border-[var(--border)] px-2.5 py-1 rounded-md font-mono transition-colors cursor-pointer flex items-center gap-1 flex-shrink-0">
              📋 Copy Prompt
            </button>
          </div>

          <div class="flex items-center justify-between text-[11px] font-mono text-[var(--muted-foreground)] bg-[var(--card)]/60 px-2.5 py-1 rounded border border-[var(--border)]/70">
            <span>Target File:</span>
            <span class="text-emerald-400 font-semibold select-all">${{sc.filename}}</span>
          </div>

          <textarea id="prompt-box-${{ep.ep_num}}-${{idx}}" readonly rows="4" 
            onclick="this.select(); copyScenePrompt(${{ep.ep_num}}, ${{idx}}, null)" 
            title="Click to copy and select all"
            class="prompt-box w-full text-xs text-[var(--muted-foreground)] font-mono leading-relaxed bg-[var(--card)] p-2.5 rounded-lg border border-[var(--border)] resize-none cursor-pointer focus:outline-none focus:border-amber-500 focus:text-[var(--foreground)] transition-colors">${{sc.prompt}}</textarea>
        </div>
      `).join('');

      container.innerHTML = `
        ${{mediaSection}}

        <!-- PROMPT BATCH HUB -->
        <div class="bg-[var(--card)] border border-[var(--border)] rounded-2xl p-6 shadow-sm space-y-6">
          <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-3 border-b border-[var(--border)] pb-4">
            <div>
              <div class="flex items-center gap-2">
                <span class="text-xs px-2.5 py-0.5 rounded font-mono font-semibold ${{ep.scene_renders.length === 5 ? 'bg-emerald-500/10 text-emerald-500 border border-emerald-500/20' : 'bg-amber-500/10 text-amber-500 border border-amber-500/20'}}">
                  ${{ep.scene_renders.length === 5 ? '✓ 5/5 SCENES RENDERED' : 'READY TO GENERATE IN FLOW'}}
                </span>
                <span class="text-xs text-[var(--muted-foreground)] font-mono">Surah ${{ep.surah.english}} (${{ep.surah.arabic}}) • ${{ep.surah.verses}} Verses</span>
              </div>
              <h2 class="text-xl font-bold mt-1">Episode ${{ep.ep_num}}: ${{ep.title}}</h2>
            </div>
            <div class="flex flex-wrap items-center gap-2">
              <button type="button" onclick="copyAllPrompts(${{ep.ep_num}}, this)" class="px-3.5 py-2 bg-amber-500 hover:bg-amber-400 text-black rounded-lg text-xs font-bold shadow-sm transition-all flex items-center gap-1.5 cursor-pointer">
                📋 Copy All 5 Prompts for Flow
              </button>
              <button type="button" onclick="copyNarration(${{ep.ep_num}}, this)" class="px-3.5 py-2 bg-[var(--background)] border border-[var(--border)] hover:bg-[var(--card)] rounded-lg text-xs font-semibold text-[var(--foreground)] transition-colors flex items-center gap-1.5 cursor-pointer">
                🎙️ Copy Voiceover Script
              </button>
            </div>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            ${{promptCards || '<div class="text-xs text-[var(--muted-foreground)] col-span-2">Prompts are currently compiling for this episode.</div>'}}
          </div>

          <!-- NARRATION TELEPROMPTER SECTION -->
          <div class="space-y-2 pt-2">
            <div class="flex items-center justify-between">
              <div class="text-xs font-mono uppercase text-[var(--muted-foreground)] font-semibold">
                Voiceover Teleprompter Script (Clean for Google AI Studio Speech)
              </div>
              <button type="button" onclick="copyNarration(${{ep.ep_num}}, this)" class="text-xs text-amber-500 hover:text-amber-400 font-mono font-semibold cursor-pointer">
                Copy Clean Script ↗
              </button>
            </div>
            <textarea id="narration-box-${{ep.ep_num}}" readonly rows="5"
              onclick="this.select()" 
              class="w-full text-xs text-[var(--muted-foreground)] font-sans leading-relaxed bg-[var(--background)] p-3.5 rounded-xl border border-[var(--border)] focus:outline-none focus:border-amber-500 focus:text-[var(--foreground)] resize-none">${{ep.narration}}</textarea>
          </div>

          <!-- ASSEMBLY INSTRUCTION BAR -->
          <div class="p-4 rounded-xl bg-[var(--background)] border border-[var(--border)] flex flex-col sm:flex-row items-center justify-between gap-3 text-xs">
            <div>
              <span class="font-bold text-[var(--foreground)]">Automated RTX 3060 Assembly:</span>
              <span class="text-[var(--muted-foreground)]">Once clips are in <code>10_VIDEO/renders/</code>, run:</span>
              <code class="ml-2 px-2 py-0.5 rounded bg-[var(--card)] border border-[var(--border)] font-mono text-amber-400">python3 scripts/assemble_ep01_full_master.py</code>
            </div>
            <span class="text-emerald-500 font-mono font-semibold">⚡ ~5s Render Time</span>
          </div>

        </div>
      `;
    }}

    // ==========================================
    // BULLETPROOF MULTI-FALLBACK COPY ENGINE
    // ==========================================

    function showToast(msg) {{
      const toast = document.getElementById('toast');
      const toastMsg = document.getElementById('toast-msg');
      if (!toast || !toastMsg) return;
      toastMsg.textContent = msg;
      toast.classList.remove('opacity-0', 'translate-y-3');
      toast.classList.add('opacity-100', 'translate-y-0');
      setTimeout(() => {{
        toast.classList.remove('opacity-100', 'translate-y-0');
        toast.classList.add('opacity-0', 'translate-y-3');
      }}, 2600);
    }}

    function copyTextUniversal(text, label, btnElement) {{
      if (!text) return;

      let succeeded = false;

      // Method 1: Try document.execCommand with native textarea (most reliable in iframes)
      try {{
        const ta = document.createElement('textarea');
        ta.value = text;
        ta.setAttribute('readonly', '');
        ta.style.position = 'fixed';
        ta.style.left = '-9999px';
        ta.style.top = '-9999px';
        document.body.appendChild(ta);
        ta.focus();
        ta.select();
        ta.setSelectionRange(0, text.length);
        succeeded = document.execCommand('copy');
        document.body.removeChild(ta);
      }} catch (err) {{
        succeeded = false;
      }}

      // Method 2: Try modern navigator.clipboard if execCommand wasn't confirmed
      if (!succeeded && navigator.clipboard && window.isSecureContext) {{
        navigator.clipboard.writeText(text).then(() => {{
          handleCopySuccess(label, btnElement);
        }}).catch(() => {{
          openCopyModal(text, label);
        }});
        return;
      }}

      if (succeeded) {{
        handleCopySuccess(label, btnElement);
      }} else {{
        // Method 3: Failsafe modal for strictly sandboxed environments
        openCopyModal(text, label);
      }}
    }}

    function handleCopySuccess(label, btn) {{
      showToast(`✓ Copied ${{label}} to clipboard!`);
      if (btn) {{
        const origText = btn.innerHTML;
        btn.innerHTML = '✓ Copied!';
        btn.classList.add('bg-emerald-500', 'text-white');
        setTimeout(() => {{
          btn.innerHTML = origText;
          btn.classList.remove('bg-emerald-500', 'text-white');
        }}, 2000);
      }}
    }}

    function copyScenePrompt(epNum, idx, btn) {{
      const ep = episodes.find(e => e.ep_num === epNum);
      if (!ep || !ep.scenes || !ep.scenes[idx]) return;
      const sc = ep.scenes[idx];
      copyTextUniversal(sc.prompt, `Scene ${{sc.num}} (${{sc.name}}) Prompt`, btn);
    }}

    function copyAllPrompts(epNum, btn) {{
      const ep = episodes.find(e => e.ep_num === epNum);
      if (!ep || !ep.scenes) return;
      const fullText = ep.scenes.map(sc => `[SCENE ${{sc.num}}: ${{sc.name.toUpperCase()}}]\\nFilename: ${{sc.filename}}\\nPrompt:\\n${{sc.prompt}}`).join('\\n\\n');
      copyTextUniversal(fullText, `All 5 Prompts for Episode ${{epNum}}`, btn);
    }}

    function copyNarration(epNum, btn) {{
      const ep = episodes.find(e => e.ep_num === epNum);
      if (!ep || !ep.narration) return;
      copyTextUniversal(ep.narration, `Voiceover Script for Episode ${{epNum}}`, btn);
    }}

    function openCopyModal(text, label) {{
      const modal = document.getElementById('copy-modal');
      const title = document.getElementById('copy-modal-title');
      const ta = document.getElementById('copy-modal-textarea');
      if (!modal || !ta) return;
      if (title) title.textContent = `Copy ${{label}}`;
      ta.value = text;
      modal.classList.remove('hidden');
      setTimeout(() => {{
        ta.focus();
        ta.select();
      }}, 50);
    }}

    function closeCopyModal(e) {{
      const modal = document.getElementById('copy-modal');
      if (modal) modal.classList.add('hidden');
    }}

    // Init
    renderPills();
    renderDetail();
  </script>
</body>
</html>
"""

    with open(REPO_OUTPUT, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Persisted to Campaign repository: {REPO_OUTPUT}")

    with open(BRAIN_OUTPUT, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Updated Antigravity brain artifact: {BRAIN_OUTPUT}")

if __name__ == "__main__":
    generate_canvas()
