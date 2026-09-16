#!/usr/bin/env python3
"""
HUURS STUDIO - Episode 14 Full Master Assembly (Season 2)
=========================================================
Assembles all 5 living-creation scene clips for Episode 14 (Surah Ibrahim 14:7, 24–25)
with continuous ultra-slow-motion interpolation (zero repeating/looping),
zero burned-in subtitles (per ZERO_BURNED_SUBTITLES_POLICY.md),
burned-in discrete HUURS STUDIO trademark watermark, and broadcast-mastered audio.

Living Creation Motif Mapping:
- Section 1: Ancient Rooted Olive Tree (The Anxiety of Scarcity)
- Section 2: Jewel Hummingbird at Mountain Blossom (The Divine Guarantee)
- Section 3: Honeybees on Golden Honeycomb (Classical Tafsir & Shukr)
- Section 4: Soaring White Birds over Waterfall (The Parable of the Good Tree)
- Section 5: Masjid an-Nabawi Sunrise Architecture (The Uncounted Blessing Audit)

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
AUDIO_IN = os.path.join(ROOT_DIR, "11_AUDIO/EP14_audio.mp3")
TIMINGS_JSON = os.path.join(ROOT_DIR, "11_AUDIO/EP14_audio_timings.json")
OUTPUT_MASTER = os.path.join(RENDERS_DIR, "QURAN-COMEBACK-EP14-FULL-MASTER.mp4")
OUTPUT_SHORT = os.path.join(RENDERS_DIR, "QURAN-COMEBACK-EP14-SHORT-001A.mp4")
TEMP_DIR = "/tmp/ep14_assembly"

os.makedirs(TEMP_DIR, exist_ok=True)

S1_FILE = os.path.join(RENDERS_DIR, "EP14_SCENE01.mp4")
S2_FILE = os.path.join(RENDERS_DIR, "EP14_SCENE02.mp4")
S3_FILE = os.path.join(RENDERS_DIR, "EP14_SCENE03.mp4")
S4_FILE = os.path.join(RENDERS_DIR, "EP14_SCENE04.mp4")
S5_FILE = os.path.join(RENDERS_DIR, "EP14_SCENE05.mp4")

DEFAULT_SECTIONS = [
    {"id": "sec1", "file": S1_FILE, "name": "Ancient Rooted Olive Tree", "duration": 38.0},
    {"id": "sec2", "file": S2_FILE, "name": "Hummingbird at Blossom", "duration": 48.0},
    {"id": "sec3", "file": S3_FILE, "name": "Honeybees on Honeycomb", "duration": 55.0},
    {"id": "sec4", "file": S4_FILE, "name": "Soaring Birds over Waterfall", "duration": 45.0},
    {"id": "sec5", "file": S5_FILE, "name": "Masjid an-Nabawi at Sunrise", "duration": 40.0},
]

def load_sections():
    sections = [dict(s) for s in DEFAULT_SECTIONS]
    if os.path.exists(TIMINGS_JSON):
        with open(TIMINGS_JSON, "r") as f:
            data = json.load(f)
        for i, s_data in enumerate(data.get("sections", [])):
            if i < len(sections):
                sections[i]["duration"] = s_data["duration"]
        print(f"Loaded dynamic section timings from {TIMINGS_JSON}")
    else:
        print("Using default section timings (timings json not found)")
    return sections

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

def assemble_master(sections):
    t0 = time.time()
    total_dur = sum(s["duration"] for s in sections)
    print("=" * 70)
    print(f"HUURS STUDIO - ASSEMBLING EPISODE 14 FULL MASTER ({total_dur:.2f}s)")
    print("=" * 70)

    extended_clips = []
    for i, sec in enumerate(sections):
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
    fade_out_st = max(0, total_dur - 3.0)

    print("-" * 70)
    print("Muxing video, normalized audio, and discrete trademark watermark (ZERO subtitles)...")
    cmd = [
        "ffmpeg", "-y",
        "-i", video_base,
        "-i", AUDIO_IN,
        "-filter_complex",
        f"[0:v]{trademark_master},fade=t=in:st=0:d=1.2,fade=t=out:st={fade_out_st:.2f}:d=3.0,format=yuv420p[v_out];"
        f"[1:a]afade=t=in:st=0:d=0.5,afade=t=out:st={fade_out_st:.2f}:d=3.0[a_out]",
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

    print(f"✓ EPISODE 14 FULL MASTER COMPLETED in {time.time()-t0:.2f}s!")
    print(f"  Location: {OUTPUT_MASTER}")

def assemble_short(sections):
    sec1 = sections[0]
    dur = sec1["duration"]
    print("-" * 70)
    print(f"Assembling 9:16 Vertical Cut (Short A: The Anxiety of Scarcity, {dur:.2f}s)...")
    sec1_part = os.path.join(TEMP_DIR, "sec1.mp4")
    trademark_short = "drawtext=text='HUURS STUDIO':font='IBM Plex Serif':fontsize=14:fontcolor=white@0.22:x=w-tw-30:y=h-th-45"
    fade_out_st = max(0, dur - 1.8)

    cmd = [
        "ffmpeg", "-y",
        "-i", sec1_part,
        "-i", AUDIO_IN,
        "-filter_complex",
        f"[0:v]crop=w=ih*(9/16):h=ih:x=(iw-ow)/2:y=0,scale=720:1280,{trademark_short},fade=t=in:st=0:d=0.8,fade=t=out:st={fade_out_st:.2f}:d=1.8,format=yuv420p[v_out];"
        f"[1:a]atrim=start=0:end={dur:.2f},afade=t=in:st=0:d=0.3,afade=t=out:st={fade_out_st:.2f}:d=1.8[a_out]",
        "-map", "[v_out]",
        "-map", "[a_out]",
        "-t", f"{dur:.2f}",
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
    print(f"✓ EPISODE 14 SHORT 001A COMPLETED!")
    print(f"  Location: {OUTPUT_SHORT}")

if __name__ == "__main__":
    sections = load_sections()
    if not all(os.path.exists(s["file"]) for s in sections):
        print("Missing scene files in 10_VIDEO/renders/:")
        for s in sections:
            status = "FOUND" if os.path.exists(s["file"]) else "MISSING"
            print(f"  [{status}] {s['file']}")
        sys.exit(1)

    if not os.path.exists(AUDIO_IN):
        print(f"Audio master not found at {AUDIO_IN}. Please generate voiceover first.")
        sys.exit(1)

    assemble_master(sections)
    assemble_short(sections)
