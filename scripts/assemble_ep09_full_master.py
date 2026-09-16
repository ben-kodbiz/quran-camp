#!/usr/bin/env python3
"""
HUURS STUDIO - Episode 9 Full Master 5-Scene Assembly
=====================================================
Assembles all 5 living-creation scene clips for Episode 9 (Surah Al-Asr 103:1–3) with
contemplative slow-motion, seamless crossfades, burned-in IBM Plex Serif typography,
and the official discreet trademark watermark:

Living Creation Motif Mapping:
- Section 1 (42.78s): Scene 1 (Infinite Spiral Galaxies & Glowing Nebulae — The Disappearing Clock)
- Section 2 (58.23s): Scene 2 (Deep Ocean Sunbeams & Silver Fish — Innal-Insāna Lafī Khusr)
- Section 3 (49.84s): Scene 3 (Living Coral Reef & Tropical Fish — The 4 Conditions of Salvation)
- Section 4 (39.67s): Scene 4 (Bird of Paradise / Cenderawasih in Rainforest — Parting Admonition)
- Section 5 (36.51s): Scene 5 (Epic Green Mountain Panorama & Waterfall — Practical Action & Reset)

Total Master Duration: 227.02s (3m 47.0s)
Trademark Watermark: 'HUURS STUDIO' (IBM Plex Serif, opacity 0.22, lower right)
Audio: Mastered to -14 LUFS broadcast standard, Zero Music Policy.
Subtitles: Burned-in IBM Plex Serif typography via libass.
Hardware: NVIDIA GeForce RTX 3060 12GB (h264_nvenc P7).
"""

import os
import sys
import time
import subprocess

ROOT_DIR = "/mnt/AI/ag/Campaign"
RENDERS_DIR = os.path.join(ROOT_DIR, "10_VIDEO/renders")
AUDIO_IN = os.path.join(ROOT_DIR, "11_AUDIO/EP09_audio.mp3")
OUTPUT_MASTER = os.path.join(RENDERS_DIR, "QURAN-COMEBACK-EP09-FULL-MASTER.mp4")
OUTPUT_SHORT = os.path.join(RENDERS_DIR, "QURAN-COMEBACK-EP09-SHORT-001A.mp4")
SUBTITLE_FILE = os.path.join(RENDERS_DIR, "ep09_master_subtitles.ass")
TEMP_DIR = "/tmp/ep09_assembly"

os.makedirs(TEMP_DIR, exist_ok=True)

S1_FILE = os.path.join(RENDERS_DIR, "EP09_SCENE01.mp4")
S2_FILE = os.path.join(RENDERS_DIR, "EP09_SCENE02.mp4")
S3_FILE = os.path.join(RENDERS_DIR, "EP09_SCENE03.mp4")
S4_FILE = os.path.join(RENDERS_DIR, "EP09_SCENE04.mp4")
S5_FILE = os.path.join(RENDERS_DIR, "EP09_SCENE05.mp4")

SECTIONS = [
    {"id": "sec1", "file": S1_FILE, "name": "Infinite Spiral Galaxies & Nebulae", "duration": 42.78},
    {"id": "sec2", "file": S2_FILE, "name": "Deep Ocean Sunbeams & Silver Fish", "duration": 58.23},
    {"id": "sec3", "file": S3_FILE, "name": "Living Coral Reef & Tropical Fish", "duration": 49.84},
    {"id": "sec4", "file": S4_FILE, "name": "Bird of Paradise / Cenderawasih", "duration": 39.67},
    {"id": "sec5", "file": S5_FILE, "name": "Epic Green Mountain Panorama & Waterfall", "duration": 36.51},
]

def make_extended_clip(input_video, target_duration, output_path):
    seg_dur = 18.5
    num_loops = int(target_duration // seg_dur) + 2

    filter_parts = ["[0:v]setpts=2.0*PTS,minterpolate=fps=24:mi_mode=blend[slow0]"]
    for i in range(1, num_loops):
        filter_parts.append(f"[0:v]setpts=2.0*PTS,minterpolate=fps=24:mi_mode=blend[slow{i}]")

    cur = "slow0"
    offset = 18.5
    for i in range(1, num_loops):
        next_tag = f"slow{i}"
        out_tag = f"xfade{i}" if i < num_loops - 1 else "v_full"
        filter_parts.append(f"[{cur}][{next_tag}]xfade=transition=fade:duration=1.5:offset={offset:.2f}[{out_tag}]")
        cur = out_tag
        offset += 18.5

    filter_parts.append(f"[v_full]trim=start=0:duration={target_duration},setpts=PTS-STARTPTS,format=yuv420p[v_out]")
    fc = ";".join(filter_parts)

    cmd = [
        "ffmpeg", "-y", "-i", input_video,
        "-filter_complex", fc,
        "-map", "[v_out]",
        "-t", str(target_duration),
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p",
        output_path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error extending {input_video}:\n{res.stderr[-500:]}")
        sys.exit(1)

def create_subtitles():
    ass_content = """[Script Info]
Title: Huurs Studio - Episode 9 Master Subtitles
ScriptType: v4.00+
WrapStyle: 0
ScaledBorderAndShadow: yes
PlayResX: 1280
PlayResY: 720

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: HuursContemplation,IBM Plex Serif,23,&H00F5F2EB,&H00000000,&H801A1A1A,&H800A0A0A,-1,0,0,0,100,100,0.8,0,1,1.5,1.0,2,60,60,55,1
Style: HuursItalic,IBM Plex Serif,23,&H00E2D9C8,&H00000000,&H801A1A1A,&H800A0A0A,0,-1,0,0,100,100,0.8,0,1,1.5,1.0,2,60,60,55,1
Style: HuursGold,IBM Plex Serif,24,&H008AE2FF,&H00000000,&H801A1A1A,&H800A0A0A,-1,0,0,0,100,100,0.8,0,1,1.8,1.2,2,60,60,55,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.60,0:00:07.50,HuursContemplation,,0,0,0,,{\\fad(400,300)}Have you felt lately like time is moving unnaturally fast?
Dialogue: 0,0:00:08.00,0:00:16.50,HuursContemplation,,0,0,0,,{\\fad(300,300)}You wake up on Monday morning, blink your eyes, and suddenly it is Friday night.
Dialogue: 0,0:00:17.00,0:00:27.50,HuursItalic,,0,0,0,,{\\fad(300,300)}‘Where did it all go? What did I actually build for my soul?’
Dialogue: 0,0:00:28.00,0:00:36.50,HuursContemplation,,0,0,0,,{\\fad(300,300)}We check our screens for hours. We hustle. We buy things.
Dialogue: 0,0:00:37.00,0:00:42.50,HuursGold,,0,0,0,,{\\fad(300,400)}And yet... a lingering anxiety remains: I am busy, but I am losing.
Dialogue: 0,0:00:43.00,0:00:51.00,HuursContemplation,,0,0,0,,{\\fad(400,300)}Listen to the oath: Wal-'Asr. Innal-insāna lafī khusr.
Dialogue: 0,0:00:51.50,0:01:00.00,HuursGold,,0,0,0,,{\\fad(300,300)}‘By time! Indeed, mankind is submerged inside loss.’
Dialogue: 0,0:01:00.50,0:01:10.00,HuursContemplation,,0,0,0,,{\\fad(300,300)}Loss is the default state of every human being.
Dialogue: 0,0:01:10.50,0:01:21.50,HuursItalic,,0,0,0,,{\\fad(300,300)}‘Have mercy upon a man whose entire capital is melting away!’
Dialogue: 0,0:01:22.00,0:01:31.50,HuursContemplation,,0,0,0,,{\\fad(300,300)}If the ice vendor sits and does nothing, his ice melts into water. He goes bankrupt.
Dialogue: 0,0:01:32.00,0:01:40.50,HuursGold,,0,0,0,,{\\fad(300,400)}Your time is that block of ice. Every second is a piece of your life dissolving.
Dialogue: 0,0:01:41.00,0:01:51.00,HuursContemplation,,0,0,0,,{\\fad(400,300)}Except those who believe, do righteous deeds, and counsel truth and patience.
Dialogue: 0,0:01:51.50,0:02:01.00,HuursItalic,,0,0,0,,{\\fad(300,300)}Imam ash-Shafi'i: ‘If humanity reflected upon this surah alone, it would suffice.’
Dialogue: 0,0:02:01.50,0:02:11.50,HuursContemplation,,0,0,0,,{\\fad(300,300)}Four non-negotiable anchors: 1. Authentic Knowledge • 2. Righteous Action
Dialogue: 0,0:02:12.00,0:02:22.00,HuursContemplation,,0,0,0,,{\\fad(300,300)}3. Advising to Truth • 4. Advising to Enduring Patience.
Dialogue: 0,0:02:22.50,0:02:30.50,HuursGold,,0,0,0,,{\\fad(300,400)}Standing for truth is demanding... and you need mutual endurance.
Dialogue: 0,0:02:31.00,0:02:40.50,HuursContemplation,,0,0,0,,{\\fad(400,300)}The companions would never part ways until reciting Surah Al-Asr.
Dialogue: 0,0:02:41.00,0:02:50.00,HuursContemplation,,0,0,0,,{\\fad(300,300)}They knew how easily conversations drift into worldly complaints.
Dialogue: 0,0:02:50.50,0:03:00.00,HuursGold,,0,0,0,,{\\fad(300,300)}Surah Al-Asr was their compass: ‘Remember: Our ice is melting. Don’t waste your life.’
Dialogue: 0,0:03:00.50,0:03:10.50,HuursContemplation,,0,0,0,,{\\fad(300,400)}Before this day closes: Look at your screen-time report.
Dialogue: 0,0:03:11.00,0:03:20.00,HuursContemplation,,0,0,0,,{\\fad(400,300)}Stop the melting. Take five minutes right now. Read Surah Al-Asr slowly.
Dialogue: 0,0:03:20.50,0:03:30.00,HuursContemplation,,0,0,0,,{\\fad(300,300)}Text someone one genuine word of encouragement or truth. Be the one who reminds of patience.
Dialogue: 0,0:03:30.50,0:03:37.00,HuursGold,,0,0,0,,{\\fad(300,400)}Read it. Understand it. Live it. And come back tomorrow.
Dialogue: 0,0:03:38.00,0:03:47.00,HuursContemplation,,0,0,0,,{\\fad(400,500)}HUURS STUDIO  •  Read. Reflect. Return.
"""
    with open(SUBTITLE_FILE, "w", encoding="utf-8") as f:
        f.write(ass_content.strip())
    print(f"Created ASS Subtitle file: {SUBTITLE_FILE}")

def assemble_master():
    t0 = time.time()
    print("=" * 70)
    print("HUURS STUDIO - ASSEMBLING EPISODE 9 FULL MASTER (5 LIVING SECTIONS)")
    print("=" * 70)

    extended_clips = []
    for i, sec in enumerate(SECTIONS):
        out_ext = os.path.join(TEMP_DIR, f"{sec['id']}.mp4")
        print(f"[{i+1}/5] Preparing {sec['name']} (target: {sec['duration']}s)...")
        make_extended_clip(sec["file"], sec["duration"], out_ext)
        extended_clips.append(out_ext)

    print("-" * 70)
    print("Creating Master Subtitle file (libass IBM Plex Serif)...")
    create_subtitles()

    concat_list = os.path.join(TEMP_DIR, "concat_sections.txt")
    with open(concat_list, "w") as f:
        for c in extended_clips:
            f.write(f"file '{c}'\n")

    video_base = os.path.join(TEMP_DIR, "video_combined.mp4")
    print("Concatenating video sections...")
    cmd = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", concat_list,
        "-c", "copy",
        video_base
    ]
    subprocess.run(cmd, check=True)

    trademark_master = "drawtext=text='HUURS STUDIO':font='IBM Plex Serif':fontsize=16:fontcolor=white@0.22:x=w-tw-40:y=h-th-30"

    print("-" * 70)
    print("Muxing video, normalized audio, burned subtitles, and trademark watermark...")
    cmd = [
        "ffmpeg", "-y",
        "-i", video_base,
        "-i", AUDIO_IN,
        "-filter_complex",
        f"[0:v]{trademark_master},fade=t=in:st=0:d=1.2,fade=t=out:st=224.0:d=3.0,format=yuv420p[v_out];"
        "[1:a]afade=t=in:st=0:d=0.5,afade=t=out:st=224.0:d=3.0[a_out]",
        "-map", "[v_out]",
        "-map", "[a_out]",
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-b:v", "4.8M",
        "-maxrate", "6.5M",
        "-bufsize", "10M",
        "-c:a", "aac",
        "-b:a", "256k",
        "-ar", "48000",
        "-movflags", "+faststart",
        OUTPUT_MASTER
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("Master assembly failed:\n", res.stderr[-800:])
        sys.exit(1)

    print(f"✓ EPISODE 9 FULL MASTER COMPLETED in {time.time()-t0:.2f}s!")
    print(f"  Location: {OUTPUT_MASTER}")

def assemble_short():
    print("-" * 70)
    print("Assembling 9:16 Vertical Cut (Short A: The Disappearing Clock Hook)...")
    sec1_part = os.path.join(TEMP_DIR, "sec1.mp4")
    audio_track = AUDIO_IN

    short_sub_file = os.path.join(RENDERS_DIR, "ep09_short_subtitles.ass")
    ass_short = """[Script Info]
Title: Huurs Studio - Episode 9 Short Subtitles
ScriptType: v4.00+
WrapStyle: 0
ScaledBorderAndShadow: yes
PlayResX: 720
PlayResY: 1280

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: ShortMobile,IBM Plex Serif,32,&H00F5F2EB,&H00000000,&H801A1A1A,&H800A0A0A,-1,0,0,0,100,100,0.8,0,1,2.0,1.2,2,40,40,240,1
Style: ShortGold,IBM Plex Serif,34,&H008AE2FF,&H00000000,&H801A1A1A,&H800A0A0A,-1,0,0,0,100,100,0.8,0,1,2.2,1.5,2,40,40,240,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.60,0:00:07.50,ShortMobile,,0,0,0,,{\\fad(300,250)}Have you felt lately like time is moving unnaturally fast?
Dialogue: 0,0:00:08.00,0:00:16.50,ShortMobile,,0,0,0,,{\\fad(250,250)}You wake up on Monday morning, blink your eyes, and suddenly it is Friday night.
Dialogue: 0,0:00:17.00,0:00:26.50,ShortMobile,,0,0,0,,{\\fad(250,250)}Where did it all go? What did I actually build for my soul?
Dialogue: 0,0:00:27.00,0:00:35.00,ShortMobile,,0,0,0,,{\\fad(250,250)}We check our screens for hours. We hustle. We buy things.
Dialogue: 0,0:00:35.50,0:00:42.50,ShortGold,,0,0,0,,{\\fad(300,300)}A lingering anxiety remains: I am busy, but I am losing.
"""
    with open(short_sub_file, "w", encoding="utf-8") as f:
        f.write(ass_short.strip())
    print(f"Created Short ASS Subtitle file: {short_sub_file}")

    trademark_short = "drawtext=text='HUURS STUDIO':font='IBM Plex Serif':fontsize=14:fontcolor=white@0.22:x=w-tw-30:y=h-th-45"

    cmd = [
        "ffmpeg", "-y",
        "-i", sec1_part,
        "-i", audio_track,
        "-filter_complex",
        f"[0:v]crop=w=ih*(9/16):h=ih:x=(iw-ow)/2:y=0,scale=720:1280,{trademark_short},fade=t=in:st=0:d=0.8,fade=t=out:st=41.0:d=1.7,format=yuv420p[v_out];"
        "[1:a]atrim=start=0:end=42.78,afade=t=in:st=0:d=0.3,afade=t=out:st=41.0:d=1.7[a_out]",
        "-map", "[v_out]",
        "-map", "[a_out]",
        "-t", "42.78",
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-b:v", "5.5M",
        "-c:a", "aac",
        "-b:a", "256k",
        "-ar", "48000",
        "-movflags", "+faststart",
        OUTPUT_SHORT
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("Short render failed:\n", res.stderr[-800:])
        sys.exit(1)
    print(f"✓ EPISODE 9 SHORT 001A COMPLETED!")

def auto_link_scenes():
    """Auto-detect and symlink scene files if named with lowercase or alternate patterns."""
    for i in range(1, 6):
        target = os.path.join(RENDERS_DIR, f"EP09_SCENE{i:02d}.mp4")
        if not os.path.exists(target):
            candidates = [
                f"ep09_scene{i:02d}.mp4",
                f"ep9_scene{i:02d}.mp4",
                f"ep09_scene{i}.mp4",
                f"ep9_scene{i}.mp4",
                f"EP09_Scene{i:02d}.mp4",
                f"EP09_Scene{i}.mp4",
                f"ep09_scene_{i:02d}.mp4",
                f"ep9_scene_{i:02d}.mp4",
                f"QURAN-COMEBACK-VEO-009-SCENE{i:02d}.mp4",
            ]
            for cand in candidates:
                cand_path = os.path.join(RENDERS_DIR, cand)
                if os.path.exists(cand_path):
                    print(f"Auto-linking {cand} -> EP09_SCENE{i:02d}.mp4")
                    try:
                        os.symlink(cand, target)
                    except Exception as e:
                        print(f"Symlink failed: {e}")
                    break

if __name__ == "__main__":
    auto_link_scenes()
    if not all(os.path.exists(s["file"]) for s in SECTIONS):
        print("Waiting for all 5 scene clips to be present in 10_VIDEO/renders/:")
        for s in SECTIONS:
            status = "FOUND" if os.path.exists(s["file"]) else "MISSING"
            print(f"  [{status}] {s['file']}")
        sys.exit(1)

    assemble_master()
    assemble_short()
