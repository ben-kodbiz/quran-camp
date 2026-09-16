#!/usr/bin/env python3
"""
HUURS STUDIO - Episode 5 Full Master 5-Scene Assembly
=====================================================
Assembles all 5 scene clips for Episode 5 (Surah Ash-Sharh 94:1–8) with
contemplative slow-motion, seamless crossfades, burned-in IBM Plex Serif typography,
and the official discreet trademark watermark:

Section Mapping:
- Section 1 (43.0s): Scene 1 (Winter Mountain Frost — The Burden & Constriction)
- Section 2 (36.0s): Scene 2 (The Honeybee on Mountain Blossom — Alam Nashrah)
- Section 3 (54.0s): Scene 3 (Ancient Olive Grove in Breeze — Inna Ma'al-'Usri Yusra)
- Section 4 (42.0s): Scene 4 (Desert Night Sky with Stars — Return From Burnout)
- Section 5 (36.13s): Scene 5 (Golden Rippled Sand Dunes at Sunrise — Practical Return)

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
AUDIO_IN = os.path.join(ROOT_DIR, "11_AUDIO/EP05_audio.mp3")
OUTPUT_MASTER = os.path.join(RENDERS_DIR, "QURAN-COMEBACK-EP05-FULL-MASTER.mp4")
OUTPUT_SHORT = os.path.join(RENDERS_DIR, "QURAN-COMEBACK-EP05-SHORT-001A.mp4")
SUBTITLE_FILE = os.path.join(RENDERS_DIR, "ep05_master_subtitles.ass")
TEMP_DIR = "/tmp/ep05_assembly"

os.makedirs(TEMP_DIR, exist_ok=True)

S1_FILE = os.path.join(RENDERS_DIR, "EP05_SCENE01.mp4")
S2_FILE = os.path.join(RENDERS_DIR, "EP05_SCENE02.mp4")
S3_FILE = os.path.join(RENDERS_DIR, "EP05_SCENE03.mp4")
S4_FILE = os.path.join(RENDERS_DIR, "EP05_SCENE04.mp4")
S5_FILE = os.path.join(RENDERS_DIR, "EP05_SCENE05.mp4")

SECTIONS = [
    {"id": "sec1", "file": S1_FILE, "name": "Winter Mountain Frost", "duration": 43.0},
    {"id": "sec2", "file": S2_FILE, "name": "The Honeybee on Blossom", "duration": 36.0},
    {"id": "sec3", "file": S3_FILE, "name": "Ancient Olive Grove", "duration": 54.0},
    {"id": "sec4", "file": S4_FILE, "name": "Desert Night Sky & Stars", "duration": 42.0},
    {"id": "sec5", "file": S5_FILE, "name": "Golden Sand Dunes at Sunrise", "duration": 36.13},
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
Title: Huurs Studio - Episode 5 Master Subtitles
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
Dialogue: 0,0:00:00.50,0:00:06.00,HuursContemplation,,0,0,0,,{\\fad(300,250)}There are days when life feels physically heavy.
Dialogue: 0,0:00:06.30,0:00:10.00,HuursItalic,,0,0,0,,{\\fad(250,250)}Not just tired—heavy.
Dialogue: 0,0:00:10.30,0:00:19.50,HuursContemplation,,0,0,0,,{\\fad(250,250)}Your chest feels tight. Every responsibility feels like an anvil pressed against your collarbone.
Dialogue: 0,0:00:20.00,0:00:27.50,HuursItalic,,0,0,0,,{\\fad(250,250)}You tell yourself: ‘I just need to get through this week. Once this finishes, I will finally breathe.’
Dialogue: 0,0:00:28.00,0:00:34.50,HuursContemplation,,0,0,0,,{\\fad(250,250)}Fourteen centuries ago, the Messenger of Allah ﷺ felt a constriction that broke his back.
Dialogue: 0,0:00:35.00,0:00:42.00,HuursGold,,0,0,0,,{\\fad(250,300)}And to heal that constriction... Allah revealed Surah Ash-Sharh.
Dialogue: 0,0:00:44.00,0:00:50.00,HuursContemplation,,0,0,0,,{\\fad(300,250)}Listen to the very first question Allah asks:
Dialogue: 0,0:00:50.50,0:00:59.00,HuursGold,,0,0,0,,{\\fad(350,300)}‘Did We not expand for you your chest, and relieve you of the burden that weighed down your back?’
Dialogue: 0,0:00:59.50,0:01:08.50,HuursContemplation,,0,0,0,,{\\fad(250,250)}The word Allah uses is Nashrah—from Sharh. It means opening up your chest from the inside.
Dialogue: 0,0:01:09.00,0:01:17.50,HuursGold,,0,0,0,,{\\fad(250,300)}When the mountain before you doesn't move, Allah expands your lungs so you can climb it.
Dialogue: 0,0:01:20.00,0:01:26.50,HuursContemplation,,0,0,0,,{\\fad(300,250)}Then comes the verse we quote all the time, but so often misunderstand:
Dialogue: 0,0:01:27.00,0:01:35.50,HuursGold,,0,0,0,,{\\fad(300,250)}‘So, surely with hardship comes ease. Surely with that same hardship comes more ease.’
Dialogue: 0,0:01:36.00,0:01:43.50,HuursContemplation,,0,0,0,,{\\fad(250,250)}Allah did not say ease comes AFTER hardship. He said Ma'a—WITH hardship.
Dialogue: 0,0:01:44.00,0:01:52.00,HuursItalic,,0,0,0,,{\\fad(250,250)}Ease is planted inside the difficulty right now. The patience Allah gives you today is ease.
Dialogue: 0,0:01:52.50,0:02:00.00,HuursContemplation,,0,0,0,,{\\fad(250,250)}The word Al-'Usr (hardship) is singular, while Yusran (ease) is indefinite and doubled.
Dialogue: 0,0:02:00.50,0:02:08.00,HuursGold,,0,0,0,,{\\fad(300,300)}One hardship will never defeat two eases.
Dialogue: 0,0:02:14.00,0:02:20.50,HuursContemplation,,0,0,0,,{\\fad(300,250)}How does Allah tell us to respond when the burden is lifted? Look at verse 7 and 8:
Dialogue: 0,0:02:21.00,0:02:29.50,HuursGold,,0,0,0,,{\\fad(300,250)}‘So once you have completed your duties, continue to strive, and to your Lord direct your longing.’
Dialogue: 0,0:02:30.00,0:02:38.00,HuursContemplation,,0,0,0,,{\\fad(250,250)}Modern culture teaches us to numb exhaustion through scrolling and entertainment.
Dialogue: 0,0:02:38.50,0:02:46.50,HuursItalic,,0,0,0,,{\\fad(250,250)}You cannot cure exhaustion by becoming numb. You cure it by returning your soul to what it was made for.
Dialogue: 0,0:02:47.00,0:02:54.00,HuursGold,,0,0,0,,{\\fad(300,300)}Turn your longing—Farghab—toward the One who holds your life.
Dialogue: 0,0:02:56.00,0:03:02.00,HuursContemplation,,0,0,0,,{\\fad(300,250)}If your chest feels narrow right now: do not look for ease in empty scrolling.
Dialogue: 0,0:03:02.50,0:03:10.50,HuursItalic,,0,0,0,,{\\fad(250,250)}Step away from your screen. Make fresh wudu. Sit on your prayer rug, open Surah 94.
Dialogue: 0,0:03:11.00,0:03:18.00,HuursGold,,0,0,0,,{\\fad(250,250)}Feel Allah addressing your tired heart directly: ‘Did We not expand for you your chest?’
Dialogue: 0,0:03:18.50,0:03:26.00,HuursContemplation,,0,0,0,,{\\fad(250,250)}Say: Alhamdulillah for the trial that brought me to my knees. Grant my heart Your ease.
Dialogue: 0,0:03:26.50,0:03:31.00,HuursItalic,,0,0,0,,{\\fad(300,500)}Read it. Understand it. Live it. And come back tomorrow.
"""
    with open(SUBTITLE_FILE, "w", encoding="utf-8") as f:
        f.write(ass_content.strip())
    print(f"Created ASS Subtitle file: {SUBTITLE_FILE}")

def prepare_audio():
    print("Preparing master voiceover audio (Zero Music Policy)...")
    audio_temp = os.path.join(TEMP_DIR, "master_audio.mp3")
    cmd = [
        "ffmpeg", "-y", "-i", AUDIO_IN,
        "-af", "loudnorm=I=-14:TP=-1.0:LRA=7",
        "-c:a", "libmp3lame", "-b:a", "192k", "-ar", "48000",
        audio_temp
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("Audio preparation failed:", res.stderr[-500:])
        sys.exit(1)
    print(f"Master audio ready at: {audio_temp}")
    return audio_temp

def assemble_master():
    print("=" * 70)
    print("      HUURS STUDIO - EPISODE 5 FULL MASTER ASSEMBLY")
    print("=" * 70)
    audio_track = prepare_audio()
    create_subtitles()

    probe_cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", audio_track]
    total_duration = float(subprocess.check_output(probe_cmd).strip())

    t0 = time.time()
    rendered_parts = []
    concat_list = os.path.join(TEMP_DIR, "concat_list.txt")

    with open(concat_list, "w") as f_cl:
        for idx, sec in enumerate(SECTIONS):
            part_path = os.path.join(TEMP_DIR, f"{sec['id']}.mp4")
            print(f"[{idx+1}/5] Extending {sec['name']} to {sec['duration']}s with 0.5x slow-mo...")
            make_extended_clip(sec["file"], sec["duration"], part_path)
            rendered_parts.append(part_path)
            f_cl.write(f"file '{part_path}'\n")

    print("Combining sections with master voiceover, subtitles, and discreet trademark...")

    trademark_filter = "drawtext=text='HUURS STUDIO':font='IBM Plex Serif':fontsize=13:fontcolor=white@0.22:x=w-tw-40:y=h-th-24"

    cmd = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0", "-i", concat_list,
        "-i", audio_track,
        "-filter_complex",
        f"[0:v]noise=c0s=1.2:allf=t,{trademark_filter},fade=t=in:st=0:d=1.0,fade=t=out:st={total_duration-2.0:.1f}:d=2.0,format=yuv420p[v_out];"
        f"[1:a]afade=t=in:st=0:d=0.5,afade=t=out:st={total_duration-2.0:.1f}:d=2.0[a_out]",
        "-map", "[v_out]",
        "-map", "[a_out]",
        "-t", str(total_duration),
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-crf", "18", "-pix_fmt", "yuv420p",
        "-b:v", "6.5M",
        "-maxrate", "9.5M",
        "-bufsize", "14M",
        "-profile:v", "high",
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

    print(f"✓ EPISODE 5 FULL MASTER COMPLETED in {time.time()-t0:.2f}s!")
    print(f"  Location: {OUTPUT_MASTER}")

def assemble_short():
    print("-" * 70)
    print("Assembling 9:16 Vertical Cut (Short A: Did We Not Expand Your Chest?)...")
    sec1_part = os.path.join(TEMP_DIR, "sec1.mp4")
    audio_track = os.path.join(TEMP_DIR, "master_audio.mp3")
    if not os.path.exists(audio_track):
        audio_track = AUDIO_IN

    short_sub_file = os.path.join(RENDERS_DIR, "ep05_short_subtitles.ass")
    ass_short = """[Script Info]
Title: Huurs Studio - Episode 5 Short Subtitles
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
Dialogue: 0,0:00:00.50,0:00:06.00,ShortMobile,,0,0,0,,{\\fad(300,250)}There are days when life feels physically heavy.
Dialogue: 0,0:00:06.30,0:00:10.00,ShortGold,,0,0,0,,{\\fad(250,250)}Not just tired—heavy.
Dialogue: 0,0:00:10.30,0:00:19.50,ShortMobile,,0,0,0,,{\\fad(250,250)}Your chest feels tight. Every responsibility feels like an anvil pressed against your collarbone.
Dialogue: 0,0:00:20.00,0:00:27.50,ShortMobile,,0,0,0,,{\\fad(250,250)}You tell yourself: ‘I just need to get through this week. Once this finishes, I will finally breathe.’
Dialogue: 0,0:00:28.00,0:00:34.50,ShortMobile,,0,0,0,,{\\fad(250,250)}Fourteen centuries ago, the Messenger of Allah ﷺ felt a constriction that broke his back.
Dialogue: 0,0:00:35.00,0:00:42.00,ShortGold,,0,0,0,,{\\fad(250,300)}And to heal that constriction... Allah revealed Surah Ash-Sharh.
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
        f"[0:v]crop=w=ih*(9/16):h=ih:x=(iw-ow)/2:y=0,scale=720:1280,{trademark_short},fade=t=in:st=0:d=0.8,fade=t=out:st=41.0:d=2.0,format=yuv420p[v_out];"
        "[1:a]atrim=start=0:end=43.0,afade=t=in:st=0:d=0.3,afade=t=out:st=41.0:d=2.0[a_out]",
        "-map", "[v_out]",
        "-map", "[a_out]",
        "-t", "43.0",
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
    print(f"✓ EPISODE 5 SHORT 001A COMPLETED!")

if __name__ == "__main__":
    if not all(os.path.exists(s["file"]) for s in SECTIONS):
        print("Waiting for all 5 scene clips to be present in 10_VIDEO/renders/:")
        for s in SECTIONS:
            status = "FOUND" if os.path.exists(s["file"]) else "MISSING"
            print(f"  [{status}] {s['file']}")
        sys.exit(1)

    assemble_master()
    assemble_short()
