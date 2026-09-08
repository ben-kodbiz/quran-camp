#!/bin/bash
# Huurs Studio - Quick Static Portal Sync Script
set -e

ROOT_DIR="/mnt/AI/ag/Campaign"
DEPLOY_DIR="$ROOT_DIR/12_PRODUCTS/deploy"

echo "Syncing latest Reader and Landing Page into $DEPLOY_DIR..."
cp "$ROOT_DIR/12_PRODUCTS/reader.html" "$DEPLOY_DIR/index.html"
cp "$ROOT_DIR/15_MARKETING/landing_page.html" "$DEPLOY_DIR/guide.html"
echo "✅ Static portal deployment package updated and ready for GitHub Pages / Cloudflare Pages!"
