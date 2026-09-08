#!/usr/bin/env python3
"""
Upgrade reader.html with:
- Smart multi-field search (English, Arabic, number, theme, classification)
- Bookmarks & favorites saved to localStorage
- Font size adjustment (A-, A, A+)
- 3-Way theme switcher (Dark Slate, Classical Parchment, Midnight OLED)
- Restores last read position upon return
"""

import re

file_path = "/mnt/AI/ag/Campaign/12_PRODUCTS/reader.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add Midnight theme and font size CSS variable
css_addon = """
    [data-theme="midnight"] {
      --bg-main: #000000;
      --bg-card: #0A0F18;
      --bg-sidebar: #05080E;
      --accent-gold: #D4AF37;
      --accent-gold-light: #F3E5AB;
      --text-main: #F8FAFC;
      --text-muted: #64748B;
      --border-color: #1E293B;
    }

    body {
      --content-scale: 1rem;
    }
    body.font-sm { --content-scale: 0.88rem; }
    body.font-lg { --content-scale: 1.15rem; }
    body.font-xl { --content-scale: 1.3rem; }

    .section-card p, .section-card div pre {
      font-size: var(--content-scale);
    }
"""

if '[data-theme="midnight"]' not in html:
    html = html.replace('[data-theme="parchment"] {', css_addon + '\n    [data-theme="parchment"] {')

# 2. Add Bookmarks filter pill to HTML
old_pills = """      <div class="filter-pills">
        <button class="filter-btn active" data-filter="all">All (114)</button>
        <button class="filter-btn" data-filter="Makki">Makki</button>
        <button class="filter-btn" data-filter="Madani">Madani</button>
      </div>"""

new_pills = """      <div class="filter-pills">
        <button class="filter-btn active" data-filter="all">All (114)</button>
        <button class="filter-btn" data-filter="Makki">Makki</button>
        <button class="filter-btn" data-filter="Madani">Madani</button>
        <button class="filter-btn" data-filter="bookmarks" id="bookmarkFilterBtn">★ Saved (<span id="bookmarkCount">0</span>)</button>
      </div>"""

html = html.replace(old_pills, new_pills)

# 3. Add Bookmark & Font controls to top bar
old_actions = """      <div class="nav-actions">
        <button id="audioAmbienceBtn" class="btn">
          <span>🌧️</span> Ambient Rain
        </button>
        <button id="themeToggleBtn" class="btn">
          <span>🌓</span> Theme
        </button>
      </div>"""

new_actions = """      <div class="nav-actions" style="display: flex; gap: 8px; align-items: center;">
        <button id="bookmarkToggleBtn" class="btn" title="Save or bookmark this Surah">
          <span id="bookmarkIcon">☆</span> <span id="bookmarkText">Save</span>
        </button>
        <div style="display: inline-flex; border: 1px solid var(--border-color); border-radius: 6px; overflow: hidden;">
          <button id="fontDecBtn" class="btn" style="padding: 6px 10px; font-size: 0.8rem; border-radius: 0;" title="Smaller text">A-</button>
          <button id="fontResetBtn" class="btn" style="padding: 6px 10px; font-size: 0.8rem; border-radius: 0;" title="Default text">A</button>
          <button id="fontIncBtn" class="btn" style="padding: 6px 10px; font-size: 0.8rem; border-radius: 0;" title="Larger text">A+</button>
        </div>
        <button id="audioAmbienceBtn" class="btn">
          <span>🌧️</span> Ambient Rain
        </button>
        <button id="themeToggleBtn" class="btn">
          <span>🌓</span> <span id="themeName">Dark</span>
        </button>
      </div>"""

html = html.replace(old_actions, new_actions)

# 4. Enhance JavaScript logic
js_new_logic = """let currentFilter = 'all';

    // Bookmarks and preferences from localStorage
    let bookmarks = [];
    try {
      bookmarks = JSON.parse(localStorage.getItem('huurs_bookmarks') || '[]');
    } catch(e) { bookmarks = []; }

    let currentScale = localStorage.getItem('huurs_font_scale') || 'normal';
    if (currentScale !== 'normal') {
      document.body.classList.add('font-' + currentScale);
    }

    let savedTheme = localStorage.getItem('huurs_theme') || 'slate';
    if (savedTheme === 'parchment' || savedTheme === 'midnight') {
      document.body.setAttribute('data-theme', savedTheme);
      const themeLabel = document.getElementById('themeName');
      if (themeLabel) themeLabel.textContent = savedTheme.charAt(0).toUpperCase() + savedTheme.slice(1);
    }

    // Elements
    const surahListEl = document.getElementById('surahList');
    const contentScrollEl = document.getElementById('contentScroll');
    const searchInput = document.getElementById('searchInput');
    const topSurahInfo = document.getElementById('topSurahInfo');
    const themeToggleBtn = document.getElementById('themeToggleBtn');
    const audioAmbienceBtn = document.getElementById('audioAmbienceBtn');
    const filterBtns = document.querySelectorAll('.filter-btn');
    const bookmarkCountEl = document.getElementById('bookmarkCount');
    const bookmarkToggleBtn = document.getElementById('bookmarkToggleBtn');
    const bookmarkIconEl = document.getElementById('bookmarkIcon');
    const bookmarkTextEl = document.getElementById('bookmarkText');
    const fontDecBtn = document.getElementById('fontDecBtn');
    const fontResetBtn = document.getElementById('fontResetBtn');
    const fontIncBtn = document.getElementById('fontIncBtn');

    function updateBookmarkUI() {
      if (bookmarkCountEl) bookmarkCountEl.textContent = bookmarks.length;
      const s = surahs[currentSurahIndex];
      const isSaved = s && bookmarks.includes(s.num);
      if (bookmarkIconEl) bookmarkIconEl.textContent = isSaved ? '★' : '☆';
      if (bookmarkTextEl) bookmarkTextEl.textContent = isSaved ? 'Saved' : 'Save';
      if (bookmarkToggleBtn) {
        if (isSaved) {
          bookmarkToggleBtn.classList.add('active-audio');
        } else {
          bookmarkToggleBtn.classList.remove('active-audio');
        }
      }
    }

    // Render Surah List with Smart Multi-Field Search
    function renderSurahList() {
      const query = searchInput.value.toLowerCase().trim();
      surahListEl.innerHTML = '';

      let displayedCount = 0;
      surahs.forEach((s, idx) => {
        let matchesFilter = true;
        if (currentFilter === 'bookmarks') {
          matchesFilter = bookmarks.includes(s.num);
        } else if (currentFilter !== 'all') {
          matchesFilter = s.classification.includes(currentFilter);
        }

        const matchesQuery = !query ||
                             s.name.toLowerCase().includes(query) ||
                             s.arabic.includes(query) ||
                             s.num.toString() === query ||
                             s.num.toString() === query.replace('surah', '').trim() ||
                             s.theme.toLowerCase().includes(query) ||
                             s.classification.toLowerCase().includes(query);

        if (matchesFilter && matchesQuery) {
          displayedCount++;
          const isBookmarked = bookmarks.includes(s.num);
          const item = document.createElement('div');
          item.className = `surah-item ${idx === currentSurahIndex ? 'active' : ''}`;
          item.innerHTML = `
            <div class="surah-left">
              <div class="surah-num">${s.num}</div>
              <div>
                <div class="surah-name">${s.name} ${isBookmarked ? '<span style="color:var(--accent-gold);font-size:0.8rem;">★</span>' : ''}</div>
                <div class="surah-meta">${s.classification} • ${s.verses} verses</div>
              </div>
            </div>
            <div class="surah-ar">${s.arabic}</div>
          `;
          item.addEventListener('click', () => selectSurah(idx));
          surahListEl.appendChild(item);
        }
      });

      if (displayedCount === 0) {
        surahListEl.innerHTML = '<div style="padding:24px;text-align:center;color:var(--text-muted);font-size:0.9rem;">No matching Surahs found.</div>';
      }
      updateBookmarkUI();
    }
"""

pattern = re.compile(r"let currentFilter = 'all';[\s\S]*?function selectSurah\(idx\) {")
html = pattern.sub(js_new_logic + "\n    // Select & Render Surah\n    function selectSurah(idx) {", html)

select_extra = """      currentSurahIndex = idx;
      try { localStorage.setItem('huurs_last_read', idx); } catch(e) {}
"""
html = html.replace("currentSurahIndex = idx;\n      const s = surahs[idx];", select_extra + "      const s = surahs[idx];")

listener_addon = """
    // Bookmark Toggle Listener
    bookmarkToggleBtn.addEventListener('click', () => {
      const s = surahs[currentSurahIndex];
      if (!s) return;
      const idxInBM = bookmarks.indexOf(s.num);
      if (idxInBM >= 0) {
        bookmarks.splice(idxInBM, 1);
      } else {
        bookmarks.push(s.num);
      }
      try { localStorage.setItem('huurs_bookmarks', JSON.stringify(bookmarks)); } catch(e) {}
      renderSurahList();
      updateBookmarkUI();
    });

    // Font Size Listeners
    fontDecBtn.addEventListener('click', () => {
      document.body.classList.remove('font-sm', 'font-lg', 'font-xl');
      document.body.classList.add('font-sm');
      try { localStorage.setItem('huurs_font_scale', 'sm'); } catch(e) {}
    });
    fontResetBtn.addEventListener('click', () => {
      document.body.classList.remove('font-sm', 'font-lg', 'font-xl');
      try { localStorage.setItem('huurs_font_scale', 'normal'); } catch(e) {}
    });
    fontIncBtn.addEventListener('click', () => {
      document.body.classList.remove('font-sm', 'font-lg', 'font-xl');
      document.body.classList.add('font-lg');
      try { localStorage.setItem('huurs_font_scale', 'lg'); } catch(e) {}
    });

    // 3-Way Theme Toggle (Slate -> Parchment -> Midnight -> Slate)
    themeToggleBtn.addEventListener('click', () => {
      const current = document.body.getAttribute('data-theme');
      const themeLabel = document.getElementById('themeName');
      if (!current) {
        document.body.setAttribute('data-theme', 'parchment');
        if (themeLabel) themeLabel.textContent = 'Parchment';
        try { localStorage.setItem('huurs_theme', 'parchment'); } catch(e) {}
      } else if (current === 'parchment') {
        document.body.setAttribute('data-theme', 'midnight');
        if (themeLabel) themeLabel.textContent = 'Midnight';
        try { localStorage.setItem('huurs_theme', 'midnight'); } catch(e) {}
      } else {
        document.body.removeAttribute('data-theme');
        if (themeLabel) themeLabel.textContent = 'Dark';
        try { localStorage.setItem('huurs_theme', 'slate'); } catch(e) {}
      }
    });
"""

old_theme_listener = re.compile(r"// Theme Toggle\s*themeToggleBtn\.addEventListener[\s\S]*?\}\);")
html = old_theme_listener.sub(listener_addon, html)

init_old = "renderSurahList();\n    selectSurah(0);"
init_new = """let initialIdx = 0;
    try {
      const saved = parseInt(localStorage.getItem('huurs_last_read') || '0', 10);
      if (!isNaN(saved) && saved >= 0 && saved < surahs.length) initialIdx = saved;
    } catch(e) { initialIdx = 0; }
    renderSurahList();
    selectSurah(initialIdx);
    updateBookmarkUI();"""
html = html.replace(init_old, init_new)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Successfully updated reader.html with bookmarks, search, font sizing, and 3-way theme toggle!")
