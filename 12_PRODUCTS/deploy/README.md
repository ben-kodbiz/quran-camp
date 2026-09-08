# Huurs Studio Public Web Portal Deployment Guide

This directory contains production-ready static assets ready for 100% free hosting:
- **`index.html`**: The 114-Surah Interactive Study Reader with smart search, bookmarks, ambient rain, and 3-way theme toggle.
- **`guide.html`**: The high-converting ethical landing page for the Free 7-Day Guided Contemplation Journal.

## Free Deployment Options ($0.00 / month)

### 1. Cloudflare Pages (Recommended - Fastest Global CDN)
1. In Cloudflare Dashboard, go to **Workers & Pages** -> **Create application** -> **Pages**.
2. Connect your GitHub repository or use direct drag-and-drop of the `12_PRODUCTS/deploy/` folder.
3. Build command: *(None required)*
4. Build output directory: `12_PRODUCTS/deploy`

### 2. GitHub Pages (Zero Config)
1. Go to your GitHub repository Settings -> **Pages**.
2. Set Source to **Deploy from a branch**.
3. Select `main` branch and folder `/12_PRODUCTS/deploy` (or push `deploy/` to a `gh-pages` branch).
4. Your site will immediately be live at `https://<username>.github.io/<repo>/`.

### 3. Vercel (Instant Preview)
Run:
```bash
npx vercel 12_PRODUCTS/deploy --prod
```
