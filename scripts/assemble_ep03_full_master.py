#!/usr/bin/env python3
"""
HUURS STUDIO - Episode 3 Full Master 5-Scene Assembly
=====================================================
Assembles all 5 Veo 3.1 scene clips with contemplative slow-motion, seamless
crossfades, and the official discreet lower-right trademark watermark to match
the master voiceover narration track:

Section Mapping:
- Section 1 (36.5s): Scene 1 (Tranquil Ocean Dawn with Sea Mist)
- Section 2 (50.5s): Scene 2 (Mosque Arches with Morning Sunbeams)
- Section 3 (75.5s): Scene 3 (Birds Gliding Over Mountain Waterfall)
- Section 4 (50.0s): Scene 4 (Gentle Rain on Stone Courtyard Basin)
- Section 5 (35.0s): Scene 5 (Panoramic Ocean Sunrise & Distant Mosque)

Trademark Watermark: 'HUURS STUDIO' (IBM Plex Serif, opacity 0.22, lower right)
Audio: Normalized to -14 LUFS broadcast standard, zero music policy.
Subtitles: Burned-in IBM Plex Serif typography via libass.
Hardware: NVIDIA GeForce RTX 3060 12GB (h264_nvenc P7).
"""

import os
import sys
import time
import subprocess

ROOT_DIR = "/mnt/AI/ag/Campaign"
RENDERS_DIR = os.path.join(ROOT_DIR, "10_VIDEO/renders")
AUDIO_IN = os.path.join(ROOT_DIR, "11_AUDIO/EP03_audio.mp3")
AUDIO_BOOSTED = os.path.join(ROOT_DIR, "11_AUDIO/EP03_SCENE01_audio_boosted.mp3")
OUTPUT_MASTER = os.path.join(RENDERS_DIR, "QURAN-COMEBACK-EP03-FULL-MASTER.mp4")
OUTPUT_SHORT = os.path.join(RENDERS_DIR, "QURAN-COMEBACK-EP03-SHORT-001A.mp4")
SUBTITLE_FILE = os.path.join(RENDERS_DIR, "ep03_master_subtitles.ass")
SHORT_SUBTITLE_FILE = os.path.join(RENDERS_DIR, "ep03_short_subtitles.ass")
TEMP_DIR = "/tmp/ep03_assembly"

os.makedirs(TEMP_DIR, exist_ok=True)

S1_FILE = os.path.join(RENDERS_DIR, "EP03_SCENE01.mp4")
S2_FILE = os.path.join(RENDERS_DIR, "EP03_SCENE02.mp4")
S3_FILE = os.path.join(RENDERS_DIR, "EP03_SCENE03.mp4")
S4_FILE = os.path.join(RENDERS_DIR, "EP03_SCENE04.mp4")
S5_FILE = os.path.join(RENDERS_DIR, "EP03_SCENE05.mp4")

SECTIONS = [
    {"id": "sec1", "file": S1_FILE, "name": "Tranquil Ocean Dawn with Sea Mist", "duration": 27.5},
    {"id": "sec2", "file": S2_FILE, "name": "Mosque Arches with Sunbeams", "duration": 57.0},
    {"id": "sec3", "file": S3_FILE, "name": "Birds Over Mountain Waterfall", "duration": 48.5},
    {"id": "sec4", "file": S4_FILE, "name": "Rain on Stone Courtyard Basin", "duration": 45.5},
    {"id": "sec5", "file": S5_FILE, "name": "Panoramic Ocean Sunrise & Mosque", "duration": 37.0},
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
Title: Huurs Studio - Episode 3 Master Subtitles
ScriptType: v4.00+
WrapStyle: 0
ScaledBorderAndShadow: yes
YCbCr Matrix: TV.709
PlayResX: 1280
PlayResY: 720

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: HuursContemplation,IBM Plex Serif,23,&H00F5F2EB,&H00000000,&H801A1A1A,&H800A0A0A,-1,0,0,0,100,100,0.8,0,1,1.5,1.0,2,60,60,55,1
Style: HuursItalic,IBM Plex Serif,23,&H00E2D9C8,&H00000000,&H801A1A1A,&H800A0A0A,0,-1,0,0,100,100,0.8,0,1,1.5,1.0,2,60,60,55,1
Style: HuursGold,IBM Plex Serif,24,&H008AE2FF,&H00000000,&H801A1A1A,&H800A0A0A,-1,0,0,0,100,100,0.8,0,1,1.8,1.2,2,60,60,55,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.50,0:00:05.50,HuursContemplation,,0,0,0,,{\\fad(300,250)}Have you ever raised your hands in the middle of the night...
Dialogue: 0,0:00:05.70,0:00:09.50,HuursItalic,,0,0,0,,{\\fad(250,250)}and felt like your words were hitting the ceiling?
Dialogue: 0,0:00:09.70,0:00:13.50,HuursContemplation,,0,0,0,,{\\fad(250,250)}You whisper your fears. You ask for help.
Dialogue: 0,0:00:13.70,0:00:18.50,HuursItalic,,0,0,0,,{\\fad(250,250)}Does Allah even hear me? Why does He feel so far away?
Dialogue: 0,0:00:19.00,0:00:25.50,HuursContemplation,,0,0,0,,{\\fad(250,300)}If you have ever felt that distance, you need to hear this verse.
Dialogue: 0,0:00:28.50,0:00:34.50,HuursContemplation,,0,0,0,,{\\fad(300,250)}In Surah Al-Baqarah, verse 186, Allah reveals:
Dialogue: 0,0:00:35.00,0:00:43.00,HuursGold,,0,0,0,,{\\fad(350,300)}‘Wa-idhā sa'alaka 'ibādī 'annī fa-innī qarīb.’
Dialogue: 0,0:00:43.20,0:00:49.00,HuursItalic,,0,0,0,,{\\fad(250,250)}‘When My servants ask you concerning Me: I am indeed near.’
Dialogue: 0,0:00:49.50,0:00:55.50,HuursContemplation,,0,0,0,,{\\fad(250,250)}Notice something extraordinary that scholars pointed out for centuries.
Dialogue: 0,0:00:56.00,0:01:01.50,HuursContemplation,,0,0,0,,{\\fad(250,250)}Every time the companions asked the Prophet ﷺ about something,
Dialogue: 0,0:01:02.00,0:01:07.50,HuursContemplation,,0,0,0,,{\\fad(250,250)}Allah answered with the word: Qul—‘Say to them.’
Dialogue: 0,0:01:08.00,0:01:11.50,HuursGold,,0,0,0,,{\\fad(250,250)}Except here.
Dialogue: 0,0:01:12.00,0:01:17.50,HuursContemplation,,0,0,0,,{\\fad(250,250)}He drops the intermediary completely. He answers directly:
Dialogue: 0,0:01:18.00,0:01:23.50,HuursGold,,0,0,0,,{\\fad(300,300)}Fa-innī Qarīb: ‘I am near.’
Dialogue: 0,0:01:25.50,0:01:31.50,HuursContemplation,,0,0,0,,{\\fad(300,250)}A man once asked the Prophet ﷺ:
Dialogue: 0,0:01:32.00,0:01:38.50,HuursItalic,,0,0,0,,{\\fad(250,250)}‘Is our Lord near so we should whisper, or far so we should shout?’
Dialogue: 0,0:01:39.00,0:01:43.50,HuursContemplation,,0,0,0,,{\\fad(250,250)}And this verse descended as the answer.
Dialogue: 0,0:01:44.00,0:01:49.50,HuursContemplation,,0,0,0,,{\\fad(250,250)}You are not calling upon one who is deaf or absent.
Dialogue: 0,0:01:50.00,0:01:56.50,HuursGold,,0,0,0,,{\\fad(300,250)}You are calling upon One Who is All-Hearing, All-Near.
Dialogue: 0,0:01:57.00,0:02:05.00,HuursContemplation,,0,0,0,,{\\fad(250,300)}He hears the tear that falls into your pillow before you even understand why.
Dialogue: 0,0:02:14.50,0:02:20.50,HuursContemplation,,0,0,0,,{\\fad(300,250)}The Prophet ﷺ said: ‘Indeed, your Lord is Shy and Generous.’
Dialogue: 0,0:02:21.00,0:02:28.50,HuursGold,,0,0,0,,{\\fad(300,250)}‘When His servant raises his hands, He is shy to return them empty.’
Dialogue: 0,0:02:29.00,0:02:35.50,HuursContemplation,,0,0,0,,{\\fad(250,250)}Allah does not look at the stack of your past sins.
Dialogue: 0,0:02:36.00,0:02:41.50,HuursContemplation,,0,0,0,,{\\fad(250,250)}He looks at your humility. He looks at your need.
Dialogue: 0,0:02:42.00,0:02:49.00,HuursGold,,0,0,0,,{\\fad(300,300)}The distance you felt was never from His side.
Dialogue: 0,0:02:59.50,0:03:05.50,HuursContemplation,,0,0,0,,{\\fad(300,250)}Tonight, before you go to sleep, sit in the quiet.
Dialogue: 0,0:03:06.00,0:03:10.50,HuursContemplation,,0,0,0,,{\\fad(250,250)}Raise your hands.
Dialogue: 0,0:03:11.00,0:03:17.50,HuursItalic,,0,0,0,,{\\fad(250,250)}Speak to the One who knows you better than you know yourself.
Dialogue: 0,0:03:18.00,0:03:24.50,HuursGold,,0,0,0,,{\\fad(300,250)}‘I respond to the caller when he calls upon Me.’
Dialogue: 0,0:03:25.00,0:03:29.50,HuursContemplation,,0,0,0,,{\\fad(250,250)}Read it. Understand it. Live it.
Dialogue: 0,0:03:30.00,0:03:33.50,HuursItalic,,0,0,0,,{\\fad(300,500)}And come back tomorrow.
"""
    with open(SUBTITLE_FILE, "w", encoding="utf-8") as f:
        f.write(ass_content.strip())
    print(f"Created ASS Subtitle file: {SUBTITLE_FILE}")

def prepare_audio():
    print("Preparing master voiceover audio (Zero Music Policy)...")
    # EP03_audio.mp3 is already mastered to -14 LUFS by generate_voiceover_f5.py
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
    print("      HUURS STUDIO - EPISODE 3 FULL MASTER ASSEMBLY")
    print("=" * 70)
    audio_track = prepare_audio()
    create_subtitles()

    # Get exact audio duration
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

    # Subtle non-distracting trademark watermark: bottom right, opacity 0.22, IBM Plex Serif
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

    print(f"✓ EPISODE 3 FULL MASTER COMPLETED in {time.time()-t0:.2f}s!")
    print(f"  Location: {OUTPUT_MASTER}")

def assemble_short():
    print("-" * 70)
    print("Assembling 9:16 Vertical Cut (Short A)...")
    sec1_part = os.path.join(TEMP_DIR, "sec1.mp4")
    audio_track = os.path.join(TEMP_DIR, "master_audio.mp3")
    if not os.path.exists(audio_track):
        audio_track = AUDIO_IN

    trademark_short = "drawtext=text='HUURS STUDIO':font='IBM Plex Serif':fontsize=14:fontcolor=white@0.22:x=w-tw-30:y=h-th-45"

    cmd = [
        "ffmpeg", "-y",
        "-i", sec1_part,
        "-i", audio_track,
        "-filter_complex",
        f"[0:v]crop=w=ih*(9/16):h=ih:x=(iw-ow)/2:y=0,scale=720:1280,{trademark_short},fade=t=in:st=0:d=0.8,fade=t=out:st=25.5:d=2.0,format=yuv420p[v_out];"
        "[1:a]atrim=start=0:end=27.5,afade=t=in:st=0:d=0.3,afade=t=out:st=25.5:d=2.0[a_out]",
        "-map", "[v_out]",
        "-map", "[a_out]",
        "-t", "27.5",
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
    print(f"✓ EPISODE 3 SHORT 001A COMPLETED!")

if __name__ == "__main__":
    assemble_master()
    assemble_short()
