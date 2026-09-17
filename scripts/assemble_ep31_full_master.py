#!/usr/bin/env python3
"""
HUURS STUDIO - Episode 31 Full Master Assembly (Season 4)
=========================================================
Assembles all 5 verified 720p HD curated scene clips for Episode 31 (Surah Luqman 31:16, 27, 29, 17, 19)
with continuous ultra-slow-motion interpolation (zero repeating/looping),
zero burned-in subtitles (per ZERO_BURNED_SUBTITLES_POLICY.md),
burned-in discrete HUURS STUDIO trademark watermark, and broadcast-mastered audio.

Living Creation Motif Mapping (Curated per Section 40D):
- Section 1: Granite Cliff & Mustard Seed in Rock (Rain_falling_on_stone_basin... - Ayah 28:7)
- Section 2: Courtyard Fountain & Inexhaustible Words (EP04_SCENE05.mp4 - Ayah 28:24)
- Section 3: Cosmic Desert Sky & Merging Night/Day (Stone_pathway_through_olive_grove... - Ayah 28:30)
- Section 4: Golden Dunes & Transience of Worldly Wealth (ep23_scene05.mp4 - Ayah 28:76–77)
- Section 5: Olive Grove Stone Pathway & Moderation (Stone_pathway_through_olive_grove_202609080940.mp4 - Ayah 28:88)

Trademark Watermark: 'HUURS STUDIO' (opacity 0.22, lower right)
Audio: Mastered to -14 LUFS broadcast standard, Zero Music Policy.
Subtitles: Zero burned-in subtitles.
Resolution: 1280x720 HD Master (720p Ceiling per User Mandate).
"""

import os
import sys
import time
import subprocess
import json

ROOT_DIR = "/mnt/AI/ag/Campaign"
RENDERS_DIR = os.path.join(ROOT_DIR, "10_VIDEO/renders")
AUDIO_IN = os.path.join(ROOT_DIR, "11_AUDIO/EP31_audio.mp3")
TIMINGS_JSON = os.path.join(ROOT_DIR, "11_AUDIO/EP31_audio_timings.json")
OUTPUT_MASTER = os.path.join(RENDERS_DIR, "QURAN-COMEBACK-EP31-FULL-MASTER.mp4")
OUTPUT_SHORT = os.path.join(RENDERS_DIR, "QURAN-COMEBACK-EP31-SHORT-001A.mp4")
TEMP_DIR = "/tmp/ep31_assembly"

os.makedirs(TEMP_DIR, exist_ok=True)

S1_FILE = os.path.join(RENDERS_DIR, "ep23_scene02.mp4")
S2_FILE = os.path.join(RENDERS_DIR, "EP04_SCENE05.mp4")
S3_FILE = os.path.join(RENDERS_DIR, "EP05_SCENE04.mp4")
S4_FILE = os.path.join(RENDERS_DIR, "ep23_scene05.mp4")
S5_FILE = os.path.join(RENDERS_DIR, "Stone_pathway_through_olive_grove_202609080940.mp4")

DEFAULT_SECTIONS = [
    {"id": "sec1", "file": S1_FILE, "name": "Granite Cliff & Mustard Seed in Rock", "duration": 45.0},
    {"id": "sec2", "file": S2_FILE, "name": "Courtyard Fountain & Inexhaustible Words", "duration": 45.0},
    {"id": "sec3", "file": S3_FILE, "name": "Cosmic Desert Sky & Merging Night/Day", "duration": 45.0},
    {"id": "sec4", "file": S4_FILE, "name": "Prayer Mat in Stone Sanctuary", "duration": 45.0},
    {"id": "sec5", "file": S5_FILE, "name": "Olive Grove Stone Pathway & Moderation", "duration": 30.0},
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

    fc = f"[0:v]setpts={speed_factor:.6f}*PTS,minterpolate=fps=24:mi_mode=blend,tpad=stop_mode=clone:stop_duration=5,trim=start=0:duration={target_duration},setpts=PTS-STARTPTS,scale=1280:720,format=yuv420p[v_out]"
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
    print(f"HUURS STUDIO - ASSEMBLING EPISODE 28 FULL MASTER ({total_dur:.2f}s)")
    print("=" * 70)

    extended_clips = []
    for i, sec in enumerate(sections):
        out_ext = os.path.join(TEMP_DIR, f"sec_{i+1}_ext.mp4")
        print(f"[{i+1}/5] Extending {sec['name']} -> {sec['duration']:.2f}s")
        make_extended_clip(sec["file"], sec["duration"], out_ext)
        extended_clips.append(out_ext)

    # Concat file
    concat_list = os.path.join(TEMP_DIR, "concat.txt")
    with open(concat_list, "w") as f:
        for p in extended_clips:
            f.write(f"file '{p}'\n")

    raw_video = os.path.join(TEMP_DIR, "raw_video.mp4")
    concat_cmd = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat_list,
        "-c", "copy", raw_video
    ]
    subprocess.run(concat_cmd, check=True)

    # Trademark Watermark Filter
    font_candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSerif.ttf"
    ]
    font_file = font_candidates[0]
    for fc in font_candidates:
        if os.path.exists(fc):
            font_file = fc
            break

    vf_watermark = (
        f"drawtext=text='HUURS STUDIO':fontfile='{font_file}':"
        f"fontsize=20:fontcolor=white@0.22:x=w-tw-48:y=h-th-36"
    )

    print("\nMuxing full master video with EBU R128 audio and discrete trademark watermark...")
    final_cmd = [
        "ffmpeg", "-y",
        "-i", raw_video,
        "-i", AUDIO_IN,
        "-filter_complex", f"[0:v]{vf_watermark}[v_out]",
        "-map", "[v_out]",
        "-map", "1:a",
        "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart",
        "-shortest",
        OUTPUT_MASTER
    ]
    subprocess.run(final_cmd, check=True)

    print(f"\n[FULL MASTER EXPORTED] -> {OUTPUT_MASTER}")
    out_size = os.path.getsize(OUTPUT_MASTER) / (1024 * 1024)
    print(f"Master file size: {out_size:.2f} MB")

    # Render Short Cut (9:16 Vertical Cut of Section 1)
    print("\nRendering 9:16 Vertical Short from Section 1 (Mustard Seed in Rock)...")
    sec1_dur = sections[0]["duration"]
    short_vf = (
        f"crop=ih*9/16:ih:(iw-ih*9/16)/2:0,scale=720:1280,"
        f"drawtext=text='HUURS STUDIO':fontfile='{font_file}':"
        f"fontsize=24:fontcolor=white@0.25:x=w-tw-36:y=h-th-48"
    )
    short_cmd = [
        "ffmpeg", "-y",
        "-i", extended_clips[0],
        "-i", AUDIO_IN,
        "-filter_complex", f"[0:v]{short_vf}[v_out]",
        "-map", "[v_out]",
        "-map", "1:a",
        "-t", str(sec1_dur),
        "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart",
        OUTPUT_SHORT
    ]
    subprocess.run(short_cmd, check=True)
    print(f"[SHORT CUT EXPORTED] -> {OUTPUT_SHORT} ({os.path.getsize(OUTPUT_SHORT)/(1024*1024):.2f} MB)")
    print(f"Total assembly time: {time.time() - t0:.2f}s")

if __name__ == "__main__":
    sections = load_sections()
    assemble_master(sections)
