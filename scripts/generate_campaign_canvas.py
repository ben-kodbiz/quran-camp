#!/usr/bin/env python3
"""
HUURS STUDIO - Master Campaign Production Canvas Generator
===========================================================
Generates a state-of-the-art interactive Studio Production Canvas
for the entire 20-week campaign ("Come Back to the Qur'an").

Features:
- Dynamic discovery of all 20 episodes (Season 1 & Season 2)
- One-click copy for Google Flow prompts (individual & batch)
- One-click copy for Google AI Studio narration scripts
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

    if os.path.exists(a_file):
        with open(a_file, "r", encoding="utf-8") as f:
            a_text = f.read()
        m_code = re.findall(r"```text\s*([\s\S]*?)\s*```", a_text)
        if m_code:
            narration = "\n\n".join(m_code)
        else:
            narration = a_text[:1200]

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

    scene_renders = []
    for s in range(1, 6):
        sc_file = f"QURAN-COMEBACK-VEO-{ep_num:03d}-SCENE0{s}.mp4"
        if os.path.exists(os.path.join(RENDERS_DIR, sc_file)):
            scene_renders.append(sc_file)

    surah = get_surah_info(ep_num)

    return {
        "ep_num": ep_num,
        "title": title,
        "surah": surah,
        "prompts": prompts,
        "narration": narration,
        "has_master": has_master,
        "has_short": has_short,
        "has_pilot": has_pilot,
        "has_audio": has_audio,
        "has_hero": has_hero,
        "master_file": master_vid if has_master else None,
        "short_file": short_vid if has_short else None,
        "audio_file": audio_boosted if has_audio else None,
        "hero_file": hero_img if has_hero else None,
        "scene_renders": scene_renders
    }

def generate_canvas():
    print("Gathering data across all 20 episodes...")
    episodes = [parse_episode(i) for i in range(1, 21)]

    total_scenes_rendered = sum(len(ep["scene_renders"]) for ep in episodes)
    credits_spent = total_scenes_rendered * 15
    total_credits = 1000
    credits_remaining = total_credits - credits_spent

    print(f"Metrics: {total_scenes_rendered} scenes rendered, {credits_spent} credits spent, {credits_remaining} remaining.")

    os.makedirs(BRAIN_DIR, exist_ok=True)
    for ep in episodes:
        if ep["has_master"]:
            shutil.copy2(os.path.join(RENDERS_DIR, ep["master_file"]), os.path.join(BRAIN_DIR, ep["master_file"]))
        if ep["has_short"]:
            shutil.copy2(os.path.join(RENDERS_DIR, ep["short_file"]), os.path.join(BRAIN_DIR, ep["short_file"]))
        if ep["has_audio"]:
            shutil.copy2(os.path.join(AUDIO_DIR, ep["audio_file"]), os.path.join(BRAIN_DIR, ep["audio_file"]))
        if ep["has_hero"]:
            shutil.copy2(os.path.join(IMAGE_DIR, ep["hero_file"]), os.path.join(BRAIN_DIR, ep["hero_file"]))

    ep_json = json.dumps(episodes)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Huurs Studio - Campaign Production Canvas</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    ::-webkit-scrollbar {{ width: 6px; height: 6px; }}
    ::-webkit-scrollbar-track {{ background: transparent; }}
    ::-webkit-scrollbar-thumb {{ background: rgba(150, 150, 150, 0.3); border-radius: 3px; }}
    .active-ep-pill {{ background: var(--primary); color: var(--primary-foreground); font-weight: 600; }}
  </style>
</head>
<body class="bg-[var(--background)] text-[var(--foreground)] antialiased p-6 min-h-screen">

  <!-- MASTER HEADER -->
  <header class="max-w-7xl mx-auto mb-8 border-b border-[var(--border)] pb-6 flex flex-col md:flex-row md:items-center md:justify-between gap-4">
    <div>
      <div class="flex items-center gap-2 mb-1">
        <span class="px-2.5 py-0.5 rounded-full text-xs font-mono bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-500/20 font-medium">HUURS STUDIO MASTER CANVAS</span>
        <span class="text-xs text-[var(--muted-foreground)] font-mono">AGENT-00 • FULL CAMPAIGN CONSOLE</span>
      </div>
      <h1 class="text-2xl font-bold tracking-tight">"Come Back to the Qur'an" — Production Canvas</h1>
      <p class="text-sm text-[var(--muted-foreground)]">Integrated Visual Control Plane • All 20 Episodes (Season 1 & 2) • 720p HD Master Standard</p>
    </div>
    
    <div class="flex items-center gap-3">
      <div class="bg-[var(--card)] border border-[var(--border)] rounded-xl px-4 py-2.5 text-center shadow-sm">
        <div class="text-xs text-[var(--muted-foreground)] uppercase tracking-wider font-semibold">Google Flow Credits</div>
        <div class="text-lg font-bold text-emerald-600 dark:text-emerald-400 font-mono">{credits_remaining} / {total_credits} <span class="text-xs font-normal text-[var(--muted-foreground)]">(~{credits_remaining//15} clips)</span></div>
      </div>
      <div class="bg-[var(--card)] border border-[var(--border)] rounded-xl px-4 py-2.5 text-center shadow-sm">
        <div class="text-xs text-[var(--muted-foreground)] uppercase tracking-wider font-semibold">Campaign Progress</div>
        <div class="text-lg font-bold text-[var(--foreground)] font-mono">{total_scenes_rendered} / 100 Scenes <span class="text-xs font-normal text-emerald-500">({total_scenes_rendered}%)</span></div>
      </div>
    </div>
  </header>

  <!-- MAIN INTERACTIVE STUDIO -->
  <main class="max-w-7xl mx-auto space-y-6">

    <!-- SEASON SELECTOR & EPISODE HORIZONTAL SCROLLER -->
    <div class="space-y-3">
      <div class="flex items-center justify-between">
        <span class="text-xs font-bold uppercase tracking-wider text-[var(--muted-foreground)] font-mono">Select Episode:</span>
        <div class="flex items-center gap-2 text-xs font-mono">
          <span class="flex items-center gap-1"><span class="w-2 h-2 rounded-full bg-emerald-500"></span> Completed</span>
          <span class="flex items-center gap-1"><span class="w-2 h-2 rounded-full bg-amber-500"></span> Next Up</span>
          <span class="flex items-center gap-1"><span class="w-2 h-2 rounded-full bg-slate-400"></span> Planned</span>
        </div>
      </div>

      <div id="episode-pills" class="flex items-center gap-2 overflow-x-auto pb-2 text-xs font-mono">
        <!-- Injected via JS -->
      </div>
    </div>

    <!-- ACTIVE EPISODE DETAIL VIEW -->
    <div id="episode-detail" class="space-y-6">
      <!-- Injected via JS -->
    </div>

  </main>

  <script>
    const episodes = {ep_json};
    let currentEpNum = 1;

    function renderPills() {{
      const container = document.getElementById('episode-pills');
      container.innerHTML = episodes.map(ep => {{
        const isCurrent = ep.ep_num === currentEpNum;
        const isDone = ep.scene_renders.length === 5;
        const isNext = ep.ep_num === 2;
        let dotColor = 'bg-slate-400';
        if (isDone) dotColor = 'bg-emerald-500';
        else if (isNext) dotColor = 'bg-amber-500';

        const cls = isCurrent 
          ? 'px-3 py-2 rounded-lg active-ep-pill shadow-sm transition-all flex items-center gap-1.5 whitespace-nowrap cursor-pointer'
          : 'px-3 py-2 rounded-lg bg-[var(--card)] border border-[var(--border)] text-[var(--muted-foreground)] hover:text-[var(--foreground)] transition-all flex items-center gap-1.5 whitespace-nowrap cursor-pointer';

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

      const isEp1 = ep.ep_num === 1;

      let mediaSection = '';
      if (isEp1 && ep.has_master) {{
        mediaSection = `
        <div class="bg-[var(--card)] border border-[var(--border)] rounded-2xl p-6 shadow-sm">
          <div class="flex flex-col lg:flex-row gap-6 items-start">
            
            <!-- 16:9 Master Player -->
            <div class="w-full lg:w-3/5 space-y-3">
              <div class="flex items-center justify-between">
                <div>
                  <span class="text-xs font-mono text-emerald-500 uppercase font-semibold">16:9 WIDESCREEN MASTER DELIVERABLE</span>
                  <h3 class="text-base font-bold">${{ep.title}}</h3>
                </div>
                <span class="text-xs text-[var(--muted-foreground)] font-mono">38.5s • 1280x720 • 24fps</span>
              </div>
              
              <div class="relative rounded-xl overflow-hidden bg-black aspect-video border border-[var(--border)] shadow-md">
                <video controls preload="metadata" class="w-full h-full object-cover">
                  <source src="${{ep.master_file}}" type="video/mp4">
                  Your browser does not support HTML5 video preview.
                </video>
              </div>
              <div class="p-3 rounded-lg bg-[var(--background)] border border-[var(--border)] text-xs text-[var(--muted-foreground)]">
                ✅ <strong>5-Scene Progression:</strong> Desk (0-8s) ➔ Courtyard (8-16s) ➔ Olive Grove (16-24s) ➔ Mountain Stream (24-32s) ➔ Mountain Sunrise (32-38s). Audio: -14 LUFS Broadcast Master.
              </div>
            </div>

            <!-- 9:16 Short & Audio Column -->
            <div class="w-full lg:w-2/5 space-y-4">
              
              <!-- 9:16 Short Player -->
              <div class="bg-[var(--background)] border border-[var(--border)] rounded-xl p-4 space-y-2">
                <div class="flex items-center justify-between">
                  <span class="text-xs font-semibold uppercase text-emerald-500 font-mono">9:16 Vertical Short 1A</span>
                  <span class="text-xs text-[var(--muted-foreground)] font-mono">30.0s • 720x1280</span>
                </div>
                <div class="relative rounded-lg overflow-hidden bg-black aspect-[9/16] border border-[var(--border)] max-h-56 mx-auto">
                  <video controls preload="metadata" class="w-full h-full object-cover">
                    <source src="${{ep.short_file}}" type="video/mp4">
                  </video>
                </div>
              </div>

              <!-- Audio Player -->
              <div class="bg-[var(--background)] border border-[var(--border)] rounded-xl p-4 space-y-2">
                <div class="flex items-center justify-between">
                  <span class="text-xs font-semibold text-[var(--foreground)] uppercase tracking-wider">Master Voiceover</span>
                  <span class="text-xs text-emerald-500 font-mono">-14 LUFS</span>
                </div>
                <audio controls class="w-full h-8">
                  <source src="${{ep.audio_file}}" type="audio/mpeg">
                </audio>
              </div>

            </div>

          </div>
        </div>
        `;
      }}

      // Build 5 Prompts Cards
      const promptCards = ep.prompts.map((p, idx) => `
        <div class="bg-[var(--background)] border border-[var(--border)] rounded-xl p-4 space-y-2">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-amber-500 font-mono">SCENE ${{idx + 1}}</span>
            <button onclick="copyPromptText(this, ${{idx}})" class="text-xs text-[var(--muted-foreground)] hover:text-[var(--foreground)] border border-[var(--border)] px-2 py-0.5 rounded cursor-pointer">Copy</button>
          </div>
          <p id="prompt-p-${{idx}}" class="text-xs text-[var(--muted-foreground)] font-mono leading-relaxed bg-[var(--card)] p-2.5 rounded border border-[var(--border)] select-all">
            ${{p}}
          </p>
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
                <span class="text-xs text-[var(--muted-foreground)] font-mono">Surah ${{ep.surah.english}} (${{ep.surah.arabic}})</span>
              </div>
              <h2 class="text-xl font-bold mt-1">Episode ${{ep.ep_num}}: ${{ep.title}}</h2>
            </div>
            <div class="flex items-center gap-2">
              <button onclick="copyAllPrompts(${{ep.ep_num}})" class="px-3.5 py-2 bg-[var(--primary)] text-[var(--primary-foreground)] rounded-lg text-xs font-semibold shadow-sm hover:opacity-90 transition-opacity flex items-center gap-1.5 cursor-pointer">
                📋 Copy All 5 Prompts for Flow
              </button>
              <button onclick="copyNarration(${{ep.ep_num}})" class="px-3.5 py-2 bg-[var(--card)] border border-[var(--border)] hover:bg-[var(--background)] rounded-lg text-xs font-semibold transition-colors flex items-center gap-1.5 cursor-pointer">
                🎙️ Copy Voiceover Script
              </button>
            </div>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            ${{promptCards || '<div class="text-xs text-[var(--muted-foreground)] col-span-2">Prompts are currently compiling for this episode.</div>'}}
          </div>

          <!-- ASSEMBLY INSTRUCTION BAR -->
          <div class="p-4 rounded-xl bg-[var(--background)] border border-[var(--border)] flex flex-col sm:flex-row items-center justify-between gap-3 text-xs">
            <div>
              <span class="font-bold text-[var(--foreground)]">Automated RTX 3060 Assembly:</span>
              <span class="text-[var(--muted-foreground)]">Once clips are in <code>10_VIDEO/renders/</code>, run:</span>
              <code class="ml-2 px-2 py-0.5 rounded bg-[var(--card)] border border-[var(--border)] font-mono">python3 scripts/assemble_ep01_full_master.py</code>
            </div>
            <span class="text-emerald-500 font-mono font-semibold">⚡ ~5s Render Time</span>
          </div>

        </div>
      `;
    }}

    function copyPromptText(btn, idx) {{
      const el = document.getElementById('prompt-p-' + idx);
      if (!el) return;
      navigator.clipboard.writeText(el.innerText.trim()).then(() => {{
        const orig = btn.innerText;
        btn.innerText = 'Copied!';
        btn.classList.add('bg-emerald-500', 'text-white');
        setTimeout(() => {{
          btn.innerText = orig;
          btn.classList.remove('bg-emerald-500', 'text-white');
        }}, 1800);
      }});
    }}

    function copyAllPrompts(epNum) {{
      const ep = episodes.find(e => e.ep_num === epNum);
      if (!ep) return;
      const fullText = ep.prompts.map((p, idx) => `[SCENE ${{idx+1}}]\\n${{p}}`).join('\\n\\n');
      navigator.clipboard.writeText(fullText).then(() => alert(`All 5 Prompts for Episode ${{epNum}} copied to clipboard!`));
    }}

    function copyNarration(epNum) {{
      const ep = episodes.find(e => e.ep_num === epNum);
      if (!ep) return;
      navigator.clipboard.writeText(ep.narration).then(() => alert(`Voiceover Script for Episode ${{epNum}} copied to clipboard!`));
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
