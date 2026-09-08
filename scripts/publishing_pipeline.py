#!/usr/bin/env python3
"""
Autonomous Publishing & Media Alignment Pipeline for Huurs Studio
==================================================================
Manages 70-day social media publishing, verifies on-disk media artifacts,
tracks publication state in SQLite database, stages rolling batches for
Buffer/Metricool Free tiers, and provides optional direct Buffer API pushing.

Usage:
  python3 scripts/publishing_pipeline.py --sync
  python3 scripts/publishing_pipeline.py --verify
  python3 scripts/publishing_pipeline.py --status
  python3 scripts/publishing_pipeline.py --stage-week 1
  python3 scripts/publishing_pipeline.py --mark-published BATCH-W01
  python3 scripts/publishing_pipeline.py --push-buffer [--dry-run]
"""

import os
import sys
import csv
import sqlite3
import argparse
import json
import urllib.request
import urllib.parse
from datetime import datetime, timezone

ROOT_DIR = "/mnt/AI/ag/Campaign"
DB_PATH = os.path.join(ROOT_DIR, "database/quran_campaign.db")
SCHEDULE_CSV = os.path.join(ROOT_DIR, "13_CAMPAIGNS/publishing_schedule_import.csv")
BATCH_DIR = os.path.join(ROOT_DIR, "13_CAMPAIGNS/batches")

HERO_IMAGE_MAP = {
    1: "09_IMAGE/QURAN-COMEBACK-HERO-001.jpg",
    2: "09_IMAGE/QURAN-COMEBACK-GUIDANCE-002.jpg",
    3: "09_IMAGE/QURAN-COMEBACK-NEARNESS-003.jpg",
    4: "09_IMAGE/QURAN-COMEBACK-RAIN-004.jpg",
    5: "09_IMAGE/QURAN-COMEBACK-EASE-005.jpg",
    6: "09_IMAGE/QURAN-COMEBACK-PATH-006.jpg",
    7: "09_IMAGE/QURAN-COMEBACK-TARTIL-007.jpg",
    8: "09_IMAGE/QURAN-COMEBACK-ROUTINE-008.jpg",
    9: "09_IMAGE/QURAN-COMEBACK-TIME-009.jpg",
    10: "09_IMAGE/QURAN-COMEBACK-TREE-010.jpg"
}

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db(conn):
    """Ensure publishing_queue table exists."""
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS publishing_queue (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            post_uid TEXT UNIQUE NOT NULL,
            scheduled_date TEXT NOT NULL,
            day_of_week TEXT NOT NULL,
            time_utc TEXT NOT NULL,
            platform TEXT NOT NULL,
            content_type TEXT NOT NULL,
            episode_num INTEGER,
            title TEXT NOT NULL,
            caption TEXT NOT NULL,
            hashtags TEXT,
            media_path TEXT,
            resolved_media_path TEXT,
            media_type TEXT,
            media_status TEXT DEFAULT 'PENDING',
            publish_status TEXT DEFAULT 'PENDING', -- PENDING, STAGED, QUEUED, PUBLISHED, SKIPPED, FAILED
            batch_id TEXT,
            buffer_profile_id TEXT,
            buffer_update_id TEXT,
            staged_at TEXT,
            queued_at TEXT,
            published_at TEXT,
            error_message TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()

def sync_from_csv(conn):
    """Load or update publishing_queue from 13_CAMPAIGNS/publishing_schedule_import.csv."""
    init_db(conn)
    if not os.path.exists(SCHEDULE_CSV):
        print(f"Error: {SCHEDULE_CSV} not found.")
        return

    with open(SCHEDULE_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    c = conn.cursor()
    inserted = 0
    updated = 0

    for idx, r in enumerate(rows, 1):
        date_str = r["Scheduled_Date"]
        day_str = r["Day"]
        time_str = r["Time_UTC"]
        platform = r["Platform"]
        c_type = r["Content_Type"]
        ep_str = r["Episode"]
        title = r["Title"]
        copy_text = r["Copy"]
        tags = r.get("Tags", "")
        media_path = r.get("Media_Path", "")

        # Extract episode number
        ep_num = None
        ep_match = re_search = None
        import re
        m = re.search(r'Episode\s+(\d+)', ep_str)
        if m:
            ep_num = int(m.group(1))

        # Generate deterministic UID
        plat_slug = platform.split()[0].replace('/', '-').upper()
        type_slug = c_type.split()[0].upper()
        post_uid = f"EP{ep_num:02d}-{day_str[:3].upper()}-{plat_slug}-{type_slug}-{idx:03d}"

        # Resolve media type
        media_type = "document"
        if "Carousel" in c_type:
            media_type = "carousel_png"
        elif "Card" in c_type or "WhatsApp" in platform:
            media_type = "card_png"
        elif "Video" in c_type or "Short" in c_type:
            media_type = "video_720p"
        elif "Thread" in c_type:
            media_type = "thread_text"
        elif "Email" in platform or "Newsletter" in c_type:
            media_type = "email_markdown"
        elif "Podcast" in c_type:
            media_type = "audio_narration"

        # Check if exists
        c.execute("SELECT id, publish_status FROM publishing_queue WHERE post_uid = ?", (post_uid,))
        existing = c.fetchone()

        if existing:
            # Update fields but preserve publish_status, batch_id, etc.
            c.execute("""
                UPDATE publishing_queue SET
                    scheduled_date = ?, day_of_week = ?, time_utc = ?, platform = ?,
                    content_type = ?, episode_num = ?, title = ?, caption = ?,
                    hashtags = ?, media_path = ?, media_type = ?, updated_at = CURRENT_TIMESTAMP
                WHERE post_uid = ?
            """, (date_str, day_str, time_str, platform, c_type, ep_num, title, copy_text, tags, media_path, media_type, post_uid))
            updated += 1
        else:
            c.execute("""
                INSERT INTO publishing_queue (
                    post_uid, scheduled_date, day_of_week, time_utc, platform,
                    content_type, episode_num, title, caption, hashtags,
                    media_path, media_type, publish_status
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'PENDING')
            """, (post_uid, date_str, day_str, time_str, platform, c_type, ep_num, title, copy_text, tags, media_path, media_type))
            inserted += 1

    conn.commit()
    print(f"Sync complete. Total CSV rows: {len(rows)} | Inserted: {inserted} | Updated: {updated}")

def resolve_and_verify_media(conn):
    """Scan all posts and verify that their referenced media artifacts exist on disk."""
    c = conn.cursor()
    c.execute("SELECT id, episode_num, media_path, media_type, content_type, platform FROM publishing_queue")
    posts = c.fetchall()

    verified = 0
    missing = 0

    for p in posts:
        p_id = p["id"]
        ep_num = p["episode_num"]
        m_path = p["media_path"] or ""
        m_type = p["media_type"] or ""
        c_type = p["content_type"] or ""
        platform = p["platform"] or ""
        resolved_path = None
        is_valid = False

        # First, strip anchor fragments like #Scene-1, #WhatsApp, #Twitter
        clean_rel_path = m_path.split('#')[0].strip()
        full_path = os.path.join(ROOT_DIR, clean_rel_path) if clean_rel_path else None

        if "Carousel" in c_type:
            # Check for 10 slides in 14_SOCIAL/renders/carousel_00X/
            carousel_dir = os.path.join(ROOT_DIR, f"14_SOCIAL/renders/carousel_{ep_num:03d}")
            if os.path.isdir(carousel_dir):
                slides = [os.path.join(carousel_dir, f"slide_{s:02d}.png") for s in range(1, 11)]
                if all(os.path.exists(s) for s in slides):
                    is_valid = True
                    resolved_path = carousel_dir
            elif full_path and (os.path.isdir(full_path) or os.path.exists(full_path)):
                is_valid = True
                resolved_path = full_path

        elif "Card" in c_type or "WhatsApp" in platform or "WhatsApp" in m_path:
            card_path = os.path.join(ROOT_DIR, f"14_SOCIAL/renders/whatsapp_card_{ep_num:03d}.png")
            if os.path.exists(card_path):
                is_valid = True
                resolved_path = card_path
            elif full_path and os.path.exists(full_path):
                is_valid = True
                resolved_path = full_path

        elif "Long-Form" in c_type or "Horizontal" in c_type:
            sb_path = os.path.join(ROOT_DIR, f"10_VIDEO/QURAN-COMEBACK-VIDEO-{ep_num:03d}.md")
            hero_rel = HERO_IMAGE_MAP.get(ep_num, "")
            hero_path = os.path.join(ROOT_DIR, hero_rel)
            if os.path.exists(sb_path):
                is_valid = True
                resolved_path = f"{sb_path} | {hero_path}" if os.path.exists(hero_path) else sb_path

        elif "Vertical Video" in c_type or "Short" in c_type or "Shorts" in c_type:
            shorts_path = os.path.join(ROOT_DIR, f"08_SCRIPTS/QURAN-COMEBACK-SHORTS-{ep_num:03d}.md")
            if os.path.exists(shorts_path):
                is_valid = True
                resolved_path = shorts_path
            elif full_path and os.path.exists(full_path):
                is_valid = True
                resolved_path = full_path

        elif "Podcast" in c_type or "Audio" in c_type:
            audio_path = os.path.join(ROOT_DIR, f"11_AUDIO/QURAN-COMEBACK-AUDIO-{ep_num:03d}.md")
            if os.path.exists(audio_path):
                is_valid = True
                resolved_path = audio_path
            elif full_path and os.path.exists(full_path):
                is_valid = True
                resolved_path = full_path

        elif "Thread" in c_type or "Twitter" in platform or "X" in platform:
            soc_path = os.path.join(ROOT_DIR, f"14_SOCIAL/QURAN-COMEBACK-SOCIAL-{ep_num:03d}.md")
            if os.path.exists(soc_path):
                is_valid = True
                resolved_path = soc_path
            elif full_path and os.path.exists(full_path):
                is_valid = True
                resolved_path = full_path

        elif "Email" in platform or "Newsletter" in c_type or "Contemplation Essay" in c_type:
            email_path = os.path.join(ROOT_DIR, "15_MARKETING/QURAN-COMEBACK-EMAIL-SERIES-001.md")
            if os.path.exists(email_path):
                is_valid = True
                resolved_path = email_path
            elif full_path and os.path.exists(full_path):
                is_valid = True
                resolved_path = full_path
        else:
            # Fallback direct path check
            if full_path and (os.path.exists(full_path) or os.path.isdir(full_path)):
                is_valid = True
                resolved_path = full_path

        status_str = "VERIFIED" if is_valid else "MISSING"
        if is_valid:
            verified += 1
        else:
            missing += 1

        c.execute("""
            UPDATE publishing_queue SET
                resolved_media_path = ?,
                media_status = ?,
                updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (resolved_path, status_str, p_id))

    conn.commit()
    print(f"Media verification complete: {verified} VERIFIED | {missing} MISSING (Total: {len(posts)})")

def show_status(conn):
    """Print comprehensive status dashboard of publishing pipeline."""
    c = conn.cursor()
    c.execute("SELECT count(*) FROM publishing_queue")
    total = c.fetchone()[0]

    if total == 0:
        print("Publishing queue is empty. Run: python3 scripts/publishing_pipeline.py --sync")
        return

    print("\n" + "="*75)
    print("        HUURS STUDIO AUTONOMOUS PUBLISHING PIPELINE STATUS")
    print("="*75)
    print(f"Total Scheduled Drops: {total} (20 Weeks / Season 1 & Season 2)")

    # Status breakdown
    c.execute("SELECT publish_status, count(*) FROM publishing_queue GROUP BY publish_status ORDER BY count(*) DESC")
    print("\n--- Publication Lifecycle Status ---")
    for r in c.fetchall():
        print(f"  • {r[0]:<12}: {r[1]} drops")

    # Media verification breakdown
    c.execute("SELECT media_status, count(*) FROM publishing_queue GROUP BY media_status")
    print("\n--- Media Artifact Alignment ---")
    for r in c.fetchall():
        print(f"  • {r[0]:<12}: {r[1]} assets")

    # Platform breakdown
    c.execute("SELECT platform, count(*) FROM publishing_queue GROUP BY platform ORDER BY count(*) DESC")
    print("\n--- Distribution Channels ---")
    for r in c.fetchall():
        print(f"  • {r[0]:<30}: {r[1]} drops")

    # Next 5 upcoming pending drops
    c.execute("""
        SELECT post_uid, scheduled_date, day_of_week, time_utc, platform, content_type, title, media_status, publish_status
        FROM publishing_queue
        WHERE publish_status IN ('PENDING', 'STAGED')
        ORDER BY scheduled_date, time_utc
        LIMIT 6
    """)
    upcoming = c.fetchall()

    if upcoming:
        print("\n--- Next Upcoming Drops in Queue ---")
        print(f"{'UID':<30} | {'Date & Time':<18} | {'Platform':<15} | {'Media':<8} | {'Status'}")
        print("-" * 88)
        for u in upcoming:
            dt_str = f"{u['scheduled_date']} {u['time_utc']}"
            plat_short = u['platform'].split('/')[0].strip()[:14]
            print(f"{u['post_uid']:<30} | {dt_str:<18} | {plat_short:<15} | {u['media_status']:<8} | {u['publish_status']}")
    else:
        print("\nAll scheduled drops have been queued or published!")

    print("="*75 + "\n")

def stage_batch(conn, week_num=1):
    """
    Export the scheduled drops for Week N into a clean batch CSV
    formatted for Buffer / Metricool free bulk import.
    Marks items as STAGED in database.
    """
    c = conn.cursor()
    c.execute("""
        SELECT * FROM publishing_queue
        WHERE episode_num = ? AND publish_status = 'PENDING'
        ORDER BY scheduled_date, time_utc
    """, (week_num,))
    posts = c.fetchall()

    if not posts:
        print(f"No PENDING posts found for Week {week_num} (Episode {week_num}).")
        return

    os.makedirs(BATCH_DIR, exist_ok=True)
    batch_id = f"BATCH-W{week_num:02d}"
    out_csv = os.path.join(BATCH_DIR, f"batch_week_{week_num:02d}_buffer.csv")

    headers = ["Date", "Time", "Platform", "Post_UID", "Text", "Media_Path"]
    out_rows = []

    for p in posts:
        out_rows.append({
            "Date": p["scheduled_date"],
            "Time": p["time_utc"],
            "Platform": p["platform"],
            "Post_UID": p["post_uid"],
            "Text": f"{p['caption']}\n\n{p['hashtags'] or ''}",
            "Media_Path": p["resolved_media_path"] or p["media_path"]
        })

    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(out_rows)

    # Mark as STAGED in database
    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    c.execute("""
        UPDATE publishing_queue SET
            publish_status = 'STAGED',
            batch_id = ?,
            staged_at = ?,
            updated_at = CURRENT_TIMESTAMP
        WHERE episode_num = ? AND publish_status = 'PENDING'
    """, (batch_id, now_str, week_num))
    conn.commit()

    print(f"Staged {len(posts)} drops for Week {week_num} into:")
    print(f"  -> {out_csv}")
    print(f"Batch ID: {batch_id} (All marked as STAGED in database)")
    print("\nHow to deploy:")
    print("1. Open Buffer (Free) or Metricool (Free).")
    print(f"2. Upload this CSV file to your calendar queue.")
    print(f"3. Run: python3 scripts/publishing_pipeline.py --mark-queued {batch_id}")

def mark_status(conn, identifier, new_status):
    """Update status of a specific post_uid or all posts in a batch_id."""
    c = conn.cursor()
    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # Check if identifier is batch_id
    c.execute("SELECT count(*) FROM publishing_queue WHERE batch_id = ?", (identifier,))
    batch_count = c.fetchone()[0]

    if batch_count > 0:
        if new_status == 'PUBLISHED':
            c.execute("""
                UPDATE publishing_queue SET
                    publish_status = ?, published_at = ?, updated_at = CURRENT_TIMESTAMP
                WHERE batch_id = ?
            """, (new_status, now_str, identifier))
        elif new_status == 'QUEUED':
            c.execute("""
                UPDATE publishing_queue SET
                    publish_status = ?, queued_at = ?, updated_at = CURRENT_TIMESTAMP
                WHERE batch_id = ?
            """, (new_status, now_str, identifier))
        else:
            c.execute("""
                UPDATE publishing_queue SET
                    publish_status = ?, updated_at = CURRENT_TIMESTAMP
                WHERE batch_id = ?
            """, (new_status, identifier))
        conn.commit()
        print(f"Updated {batch_count} posts in batch '{identifier}' to status: {new_status}")
    else:
        # Check if single post_uid
        c.execute("SELECT id FROM publishing_queue WHERE post_uid = ?", (identifier,))
        row = c.fetchone()
        if row:
            col_time = "published_at" if new_status == 'PUBLISHED' else "queued_at"
            c.execute(f"""
                UPDATE publishing_queue SET
                    publish_status = ?, {col_time} = ?, updated_at = CURRENT_TIMESTAMP
                WHERE post_uid = ?
            """, (new_status, now_str, identifier))
            conn.commit()
            print(f"Updated post '{identifier}' to status: {new_status}")
        else:
            print(f"Error: No post or batch found with identifier: {identifier}")

def push_to_buffer(conn, dry_run=False):
    """
    Direct integration with Buffer Free API.
    Reads BUFFER_ACCESS_TOKEN. Checks queue depth per profile.
    Pushes next pending items respecting the 10-slot free queue limit.
    """
    token = os.environ.get("BUFFER_ACCESS_TOKEN")
    if not token:
        env_file = os.path.join(ROOT_DIR, ".env")
        if os.path.exists(env_file):
            with open(env_file) as f:
                for line in f:
                    if line.startswith("BUFFER_ACCESS_TOKEN="):
                        token = line.strip().split("=", 1)[1].strip("\"'")

    if not token:
        print("BUFFER_ACCESS_TOKEN is not set.")
        print("You can get a free personal access token from: https://buffer.com/manage/apps")
        print("Or continue using the 100% free offline batch mode: python3 scripts/publishing_pipeline.py --stage-week 1")
        return

    print("Authenticating with Buffer API...")
    url = f"https://api.bufferapp.com/1/profiles.json?access_token={token}"
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as resp:
            profiles = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"Buffer API Authentication Error: {e}")
        return

    print(f"Connected to {len(profiles)} Buffer profiles:")
    for prof in profiles:
        service = prof.get("service", "unknown")
        user_name = prof.get("formatted_username", "unknown")
        pending_count = prof.get("counts", {}).get("pending", 0)
        prof_id = prof.get("id")
        print(f"  • [{service.upper()}] {user_name} (ID: {prof_id}) — {pending_count}/10 in queue")

        # Calculate free slots (max 10 on free plan)
        available_slots = max(0, 10 - pending_count)
        if available_slots == 0:
            print(f"    Queue full for {service}. Waiting for next post to publish.")
            continue

        # Find next pending posts matching this platform
        c = conn.cursor()
        c.execute("""
            SELECT * FROM publishing_queue
            WHERE lower(platform) LIKE ? AND publish_status IN ('PENDING', 'STAGED')
            ORDER BY scheduled_date, time_utc
            LIMIT ?
        """, (f"%{service.lower()}%", available_slots))
        posts_to_push = c.fetchall()

        if not posts_to_push:
            print(f"    No pending posts in local database for {service}.")
            continue

        print(f"    Pushing {len(posts_to_push)} posts to {service}...")
        for post in posts_to_push:
            post_uid = post["post_uid"]
            text_body = f"{post['title']}\n\n{post['caption']}\n\n{post['hashtags'] or ''}"

            if dry_run:
                print(f"      [DRY-RUN] Would push {post_uid} ({post['scheduled_date']})")
                continue

            # API Call: POST /1/updates/create.json
            push_url = "https://api.bufferapp.com/1/updates/create.json"
            post_data = urllib.parse.urlencode({
                "access_token": token,
                "profile_ids[]": prof_id,
                "text": text_body,
                "now": False,
                "top": False
            }).encode("utf-8")

            try:
                push_req = urllib.request.Request(push_url, data=post_data, method="POST")
                with urllib.request.urlopen(push_req) as p_resp:
                    res = json.loads(p_resp.read().decode("utf-8"))
                    if res.get("success"):
                        up_id = res.get("updates", [{}])[0].get("id")
                        now_str = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
                        c.execute("""
                            UPDATE publishing_queue SET
                                publish_status = 'QUEUED',
                                buffer_profile_id = ?,
                                buffer_update_id = ?,
                                queued_at = ?,
                                updated_at = CURRENT_TIMESTAMP
                            WHERE id = ?
                        """, (prof_id, up_id, now_str, post["id"]))
                        conn.commit()
                        print(f"      Queued: {post_uid} (Buffer ID: {up_id})")
                    else:
                        print(f"      Buffer Error on {post_uid}: {res.get('message')}")
            except Exception as pe:
                print(f"      Failed to push {post_uid}: {pe}")

def main():
    parser = argparse.ArgumentParser(description="Huurs Studio Autonomous Publishing & Media Tracking Pipeline")
    parser.add_argument("--sync", action="store_true", help="Sync schedule from 13_CAMPAIGNS/publishing_schedule_import.csv into SQLite")
    parser.add_argument("--verify", action="store_true", help="Verify all referenced media assets on disk")
    parser.add_argument("--status", action="store_true", help="Display full dashboard of publishing queue")
    parser.add_argument("--stage-week", type=int, help="Stage Week N into a clean batch CSV for Buffer/Metricool")
    parser.add_argument("--push-buffer", action="store_true", help="Directly push pending posts into Buffer API (requires BUFFER_ACCESS_TOKEN)")
    parser.add_argument("--dry-run", action="store_true", help="Simulate actions without modifying remote platforms")
    parser.add_argument("--mark-queued", type=str, help="Mark post_uid or batch_id as QUEUED")
    parser.add_argument("--mark-published", type=str, help="Mark post_uid or batch_id as PUBLISHED")
    parser.add_argument("--reset-batch", type=str, help="Reset batch_id back to PENDING")

    args = parser.parse_args()
    conn = get_db()

    if args.sync:
        sync_from_csv(conn)
        resolve_and_verify_media(conn)
    elif args.verify:
        resolve_and_verify_media(conn)
    elif args.status:
        show_status(conn)
    elif args.stage_week:
        stage_batch(conn, args.stage_week)
    elif args.push_buffer:
        push_to_buffer(conn, dry_run=args.dry_run)
    elif args.mark_queued:
        mark_status(conn, args.mark_queued, "QUEUED")
    elif args.mark_published:
        mark_status(conn, args.mark_published, "PUBLISHED")
    elif args.reset_batch:
        mark_status(conn, args.reset_batch, "PENDING")
    else:
        # Default behavior: run status
        show_status(conn)

    conn.close()

if __name__ == "__main__":
    main()
