#!/usr/bin/env python3
"""
HUURS STUDIO - Pilot Cut Assembly: Episode 1 Scene 1 (Broadcast Master)
======================================================================
Combines:
1. Video: 10s Veo 3.1 B-roll (QURAN-COMEBACK-VEO-001-SCENE01.mp4) extended to 38s
   using cinematic breathing ping-pong motion + subtle soft-focus vignette
2. Audio: Master Voiceover (11_AUDIO/EP01_SCENE01_audio.mp3, 37.7s) + Veo ambient room tone
   Mixed with normalize=0 and EBU R128 loudnorm (-14 LUFS / -1.0 dBTP YouTube Broadcast Standard)
3. Typography: Editorial IBM Plex Serif subtitles burned in via libass
4. Hardware: NVIDIA GeForce RTX 3060 12GB (h264_nvenc P7)
"""

import os
import sys
import time
import subprocess

ROOT_DIR = "/mnt/AI/ag/Campaign"
VIDEO_IN = os.path.join(ROOT_DIR, "10_VIDEO/renders/QURAN-COMEBACK-VEO-001-SCENE01.mp4")
AUDIO_IN = os.path.join(ROOT_DIR, "11_AUDIO/EP01_SCENE01_audio.mp3")
OUTPUT_DIR = os.path.join(ROOT_DIR, "10_VIDEO/renders")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "QURAN-COMEBACK-EP01-SCENE01-PILOT.mp4")
SUBTITLE_FILE = os.path.join(OUTPUT_DIR, "scene01_subtitles.ass")

def create_subtitles():
    ass_content = """[Script Info]
Title: Huurs Studio - Episode 1 Scene 1
ScriptType: v4.00+
WrapStyle: 0
ScaledBorderAndShadow: yes
YCbCr Matrix: TV.709
PlayResX: 1280
PlayResY: 720

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: HuursContemplation,IBM Plex Serif,24,&H00F5F2EB,&H00000000,&H801A1A1A,&H800A0A0A,-1,0,0,0,100,100,0.8,0,1,1.5,1.0,2,60,60,55,1
Style: HuursItalic,IBM Plex Serif,24,&H00E2D9C8,&H00000000,&H801A1A1A,&H800A0A0A,0,-1,0,0,100,100,0.8,0,1,1.5,1.0,2,60,60,55,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.20,0:00:03.20,HuursContemplation,,0,0,0,,{\\fad(300,300)}What if the answer to that emptiness inside you...
Dialogue: 0,0:00:03.35,0:00:06.00,HuursItalic,,0,0,0,,{\\fad(250,250)}isn't another ten-minute lecture?
Dialogue: 0,0:00:06.20,0:00:11.20,HuursContemplation,,0,0,0,,{\\fad(300,300)}What if the reason you feel so tired... so spiritually scattered...
Dialogue: 0,0:00:11.50,0:00:15.50,HuursContemplation,,0,0,0,,{\\fad(300,300)}isn't that you lack Islamic reminders,
Dialogue: 0,0:00:15.60,0:00:19.20,HuursContemplation,,0,0,0,,{\\fad(250,250)}but that you've spent months listening to everyone talk ABOUT Allah...
Dialogue: 0,0:00:19.30,0:00:23.20,HuursItalic,,0,0,0,,{\\fad(250,350)}without ever sitting down to listen to Allah Himself?
Dialogue: 0,0:00:23.60,0:00:27.20,HuursContemplation,,0,0,0,,{\\fad(300,300)}Take an honest look at your day.
Dialogue: 0,0:00:27.30,0:00:30.80,HuursContemplation,,0,0,0,,{\\fad(250,250)}We scroll through hundreds of religious posts.
Dialogue: 0,0:00:30.90,0:00:34.20,HuursContemplation,,0,0,0,,{\\fad(250,300)}We save motivational reels we never re-watch.
Dialogue: 0,0:00:34.30,0:00:36.50,HuursItalic,,0,0,0,,{\\fad(300,300)}Today, let's stop scrolling.
Dialogue: 0,0:00:36.60,0:00:38.20,HuursContemplation,,0,0,0,,{\\fad(300,500)}Let's come back.
"""
    with open(SUBTITLE_FILE, "w", encoding="utf-8") as f:
        f.write(ass_content.strip())
    print(f"Created ASS Subtitle file: {SUBTITLE_FILE}")

def assemble():
    create_subtitles()

    print("=" * 70)
    print("      HUURS STUDIO - PILOT ASSEMBLY (EPISODE 1 SCENE 1)")
    print("=" * 70)
    print(f"Video Source : {VIDEO_IN}")
    print(f"Audio Source : {AUDIO_IN}")
    print(f"Output Target: {OUTPUT_FILE}")
    print(f"Audio Target : Broadcast Loudness (-14 LUFS, Peak -1.0 dBTP)")
    print("-" * 70)

    start_time = time.time()

    filter_complex = (
        # Split video into fwd and rev for seamless ping-pong
        "[0:v]split=2[fwd][rev_src];"
        "[rev_src]reverse[rev];"
        "[fwd][rev]concat=n=2:v=1:a=0[pingpong1];"
        "[pingpong1]split=2[p1][p2];"
        "[p1][p2]concat=n=2:v=1:a=0[extended];"
        # Subtle vignette, grain, subtitles, and fades
        "[extended]trim=duration=38.5,"
        "vignette=PI/6,"
        "noise=c0s=1.5:allf=t,"
        f"subtitles={SUBTITLE_FILE},"
        "fade=t=in:st=0:d=0.8,"
        "fade=t=out:st=37.5:d=1.0,"
        "format=yuv420p[v_out];"
        # Audio: Ambient bed at soft background level (-28dB) + primary voiceover
        # amix normalize=0 preserves 100% vocal gain, loudnorm locks -14 LUFS broadcast standard
        "[0:a]aloop=loop=-1:size=48000*10,atrim=duration=38.5,volume=0.03,aformat=sample_rates=48000:channel_layouts=stereo[amb];"
        "[1:a]aformat=sample_rates=48000:channel_layouts=stereo[vox];"
        "[vox][amb]amix=inputs=2:duration=first:dropout_transition=2:normalize=0,"
        "loudnorm=I=-14:TP=-1.0:LRA=7,"
        "afade=t=in:st=0:d=0.4,"
        "afade=t=out:st=37.5:d=1.0[a_out]"
    )

    cmd = [
        "ffmpeg", "-y",
        "-i", VIDEO_IN,
        "-i", AUDIO_IN,
        "-filter_complex", filter_complex,
        "-map", "[v_out]",
        "-map", "[a_out]",
        "-t", "38.5",
        "-c:v", "h264_nvenc",
        "-preset", "p7",
        "-tune", "hq",
        "-rc", "vbr",
        "-cq", "17",
        "-spatial-aq", "1",
        "-temporal-aq", "1",
        "-b:v", "6M",
        "-maxrate", "9M",
        "-bufsize", "12M",
        "-profile:v", "high",
        "-c:a", "aac",
        "-b:a", "256k",
        "-ar", "48000",
        "-movflags", "+faststart",
        OUTPUT_FILE
    ]

    print("Rendering assembly on RTX 3060 with Broadcast Audio...")
    res = subprocess.run(cmd, capture_output=True, text=True)

    if res.returncode != 0:
        print("Assembly Render Failed:")
        print(res.stderr[-1000:])
        sys.exit(1)

    elapsed = time.time() - start_time
    file_size_mb = os.path.getsize(OUTPUT_FILE) / (1024 * 1024)

    print("\n" + "=" * 70)
    print("BROADCAST PILOT CUT ASSEMBLY SUCCESSFUL!")
    print("=" * 70)
    print(f"Output File  : {OUTPUT_FILE}")
    print(f"Duration     : 38.50 seconds")
    print(f"Audio Profile: 48kHz Stereo AAC (256kbps) @ -14 LUFS Broadcast Master")
    print(f"File Size    : {file_size_mb:.2f} MB")
    print(f"Render Time  : {elapsed:.2f} seconds")
    print("=" * 70)

if __name__ == "__main__":
    assemble()
