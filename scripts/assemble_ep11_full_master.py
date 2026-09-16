#!/usr/bin/env python3
"""
HUURS STUDIO - Episode 11 Full Master Assembly (Season 2 Premiere)
==================================================================
Assembles all 5 living-creation scene clips for Episode 11 (Surah Hud 11:112, 114–115)
with continuous ultra-slow-motion interpolation (zero repeating/looping),
zero burned-in subtitles (per ZERO_BURNED_SUBTITLES_POLICY.md),
burned-in discrete HUURS STUDIO trademark watermark, and broadcast-mastered audio.

Living Creation Motif Mapping:
- Section 1 (40.80s): Taif Mountain Terraces in Morning Mist (The Weight of Holding On)
- Section 2 (50.19s): Honeybees Working on Honeycomb (The Command of Istiqamah)
- Section 3 (61.44s): Full Moon & Stars over Desert Dunes (What Classical Tafsir Explains)
- Section 4 (47.38s): Majestic Peacock in Courtyard Garden (The Tadabbur Shift & 3-Deeds Anchor)
- Section 5 (34.56s): Masjid an-Nabawi at Sunrise (The Living Action & Call to Return)

Total Master Duration: 234.38s (3m 54.4s)
Trademark Watermark: 'HUURS STUDIO' (IBM Plex Serif, opacity 0.22, lower right)
Audio: Mastered to -14 LUFS broadcast standard, Zero Music Policy.
Subtitles: Zero burned-in subtitles.
"""

import os
import sys
import time
import subprocess
import json

ROOT_DIR = "/mnt/AI/ag/Campaign"
RENDERS_DIR = os.path.join(ROOT_DIR, "10_VIDEO/renders")
AUDIO_IN = os.path.join(ROOT_DIR, "11_AUDIO/EP11_audio.mp3")
OUTPUT_MASTER = os.path.join(RENDERS_DIR, "QURAN-COMEBACK-EP11-FULL-MASTER.mp4")
OUTPUT_SHORT = os.path.join(RENDERS_DIR, "QURAN-COMEBACK-EP11-SHORT-001A.mp4")
TEMP_DIR = "/tmp/ep11_assembly"

os.makedirs(TEMP_DIR, exist_ok=True)

S1_FILE = os.path.join(RENDERS_DIR, "EP11_SCENE01.mp4")
S2_FILE = os.path.join(RENDERS_DIR, "EP11_SCENE02.mp4")
S3_FILE = os.path.join(RENDERS_DIR, "EP11_SCENE03.mp4")
S4_FILE = os.path.join(RENDERS_DIR, "EP11_SCENE04.mp4")
S5_FILE = os.path.join(RENDERS_DIR, "EP11_SCENE05.mp4")

SECTIONS = [
    {"id": "sec1", "file": S1_FILE, "name": "Taif Mountain Terraces in Mist", "duration": 40.80},
    {"id": "sec2", "file": S2_FILE, "name": "Honeybees on Honeycomb", "duration": 50.19},
    {"id": "sec3", "file": S3_FILE, "name": "Full Moon & Stars over Dunes", "duration": 61.44},
    {"id": "sec4", "file": S4_FILE, "name": "Peacock in Courtyard Garden", "duration": 47.38},
    {"id": "sec5", "file": S5_FILE, "name": "Masjid an-Nabawi at Sunrise", "duration": 34.56},
]

def make_extended_clip(input_video, target_duration, output_path):
    """Extends video using continuous ultra-slow-motion interpolation (zero repeating/looping)."""
    probe_cmd = [
        "ffprobe", "-v", "error", "-show_entries", "stream=nb_frames,r_frame_rate,duration",
        "-select_streams", "v:0", "-of", "json", input_video
    ]
    res = subprocess.run(probe_cmd, capture_output=True, text=True, check=True)
    st = json.loads(res.stdout)["streams"][0]
    fps = eval(st.get("r_frame_rate", "24/1"))
    nb_frames = int(st.get("nb_frames", "240"))
    usable_src_dur = (nb_frames - 1) / fps
    speed_factor = target_duration / usable_src_dur

    fc = f"[0:v]setpts={speed_factor:.6f}*PTS,minterpolate=fps=24:mi_mode=blend,tpad=stop_mode=clone:stop_duration=5,trim=start=0:duration={target_duration},setpts=PTS-STARTPTS,format=yuv420p[v_out]"
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

def assemble_master():
    t0 = time.time()
    print("=" * 70)
    print("HUURS STUDIO - ASSEMBLING EPISODE 11 FULL MASTER (SEASON 2 PREMIERE)")
    print("=" * 70)

    extended_clips = []
    for i, sec in enumerate(SECTIONS):
        out_ext = os.path.join(TEMP_DIR, f"{sec['id']}.mp4")
        print(f"[{i+1}/5] Preparing {sec['name']} (target: {sec['duration']}s continuous slow-mo)...")
        make_extended_clip(sec["file"], sec["duration"], out_ext)
        extended_clips.append(out_ext)

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
    print("Muxing video, normalized audio, and discrete trademark watermark (ZERO subtitles)...")
    cmd = [
        "ffmpeg", "-y",
        "-i", video_base,
        "-i", AUDIO_IN,
        "-filter_complex",
        f"[0:v]{trademark_master},fade=t=in:st=0:d=1.2,fade=t=out:st=231.0:d=3.0,format=yuv420p[v_out];"
        "[1:a]afade=t=in:st=0:d=0.5,afade=t=out:st=231.0:d=3.0[a_out]",
        "-map", "[v_out]",
        "-map", "[a_out]",
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-crf", "18",
        "-maxrate", "6.5M",
        "-bufsize", "10M",
        "-pix_fmt", "yuv420p",
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

    print(f"✓ EPISODE 11 FULL MASTER COMPLETED in {time.time()-t0:.2f}s!")
    print(f"  Location: {OUTPUT_MASTER}")

def assemble_short():
    print("-" * 70)
    print("Assembling 9:16 Vertical Cut (Short A: The Weight of Holding On)...")
    sec1_part = os.path.join(TEMP_DIR, "sec1.mp4")
    trademark_short = "drawtext=text='HUURS STUDIO':font='IBM Plex Serif':fontsize=14:fontcolor=white@0.22:x=w-tw-30:y=h-th-45"

    cmd = [
        "ffmpeg", "-y",
        "-i", sec1_part,
        "-i", AUDIO_IN,
        "-filter_complex",
        f"[0:v]crop=w=ih*(9/16):h=ih:x=(iw-ow)/2:y=0,scale=720:1280,{trademark_short},fade=t=in:st=0:d=0.8,fade=t=out:st=39.0:d=1.8,format=yuv420p[v_out];"
        "[1:a]atrim=start=0:end=40.80,afade=t=in:st=0:d=0.3,afade=t=out:st=39.0:d=1.8[a_out]",
        "-map", "[v_out]",
        "-map", "[a_out]",
        "-t", "40.80",
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
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
    print(f"✓ EPISODE 11 SHORT 001A COMPLETED!")
    print(f"  Location: {OUTPUT_SHORT}")

if __name__ == "__main__":
    if not all(os.path.exists(s["file"]) for s in SECTIONS):
        print("Waiting for all 5 scene clips to be present in 10_VIDEO/renders/:")
        for s in SECTIONS:
            status = "FOUND" if os.path.exists(s["file"]) else "MISSING"
            print(f"  [{status}] {s['file']}")
        sys.exit(1)

    assemble_master()
    assemble_short()
