#!/usr/bin/env python3
"""
HUURS STUDIO - Vertical Short 1A Generator (9:16, 720x1280)
============================================================
Renders Episode 1 Short A ("The Emotional Hook") for YouTube Shorts,
Instagram Reels, and TikTok:
- Resolution: 720 × 1280 (Strict 720p ceiling compliance)
- Visual: Scene 4 Mountain Stream cropped & reframed to 9:16
- Audio: Voiceover audio excerpt + ambient stream bed @ -14 LUFS
- Typography: Bold vertical editorial subtitles
"""

import os
import subprocess

ROOT_DIR = "/mnt/AI/ag/Campaign"
VIDEO_IN = os.path.join(ROOT_DIR, "10_VIDEO/renders/QURAN-COMEBACK-VEO-001-SCENE04.mp4")
AUDIO_IN = os.path.join(ROOT_DIR, "11_AUDIO/EP01_SCENE01_audio.mp3")
OUTPUT_DIR = os.path.join(ROOT_DIR, "10_VIDEO/renders")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "QURAN-COMEBACK-EP01-SHORT-001A.mp4")
SUBTITLE_FILE = os.path.join(OUTPUT_DIR, "short01a_subtitles.ass")

ass_content = """[Script Info]
Title: Huurs Studio - Short 1A
ScriptType: v4.00+
WrapStyle: 0
PlayResX: 720
PlayResY: 1280

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: ShortTitle,IBM Plex Serif,32,&H00F5F2EB,&H00000000,&H80111111,&H80000000,-1,0,0,0,100,100,0.5,0,1,2.0,1.5,2,40,40,240,1
Style: ShortItalic,IBM Plex Serif,30,&H00E2D9C8,&H00000000,&H80111111,&H80000000,0,-1,0,0,100,100,0.5,0,1,2.0,1.5,2,40,40,240,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.20,0:00:03.20,ShortTitle,,0,0,0,,{\\fad(200,200)}What if the answer to that\\nemptiness inside you...
Dialogue: 0,0:00:03.35,0:00:06.00,ShortItalic,,0,0,0,,{\\fad(200,200)}isn't another lecture?
Dialogue: 0,0:00:06.20,0:00:11.20,ShortTitle,,0,0,0,,{\\fad(200,200)}What if the reason you feel so tired...\\nso spiritually scattered...
Dialogue: 0,0:00:11.50,0:00:15.50,ShortTitle,,0,0,0,,{\\fad(200,200)}isn't that you lack reminders,
Dialogue: 0,0:00:15.60,0:00:20.00,ShortTitle,,0,0,0,,{\\fad(200,200)}but that you spend months listening\\nto everyone talk ABOUT Allah...
Dialogue: 0,0:00:20.10,0:00:24.00,ShortItalic,,0,0,0,,{\\fad(200,200)}without sitting down to listen\\nto Allah Himself?
Dialogue: 0,0:00:24.20,0:00:27.50,ShortTitle,,0,0,0,,{\\fad(200,200)}Today, let's stop scrolling.
Dialogue: 0,0:00:27.60,0:00:30.00,ShortTitle,,0,0,0,,{\\fad(200,400)}Let's come back.
"""
with open(SUBTITLE_FILE, "w", encoding="utf-8") as f:
    f.write(ass_content.strip())

trademark_short = "drawtext=text='HUURS STUDIO':font='IBM Plex Serif':fontsize=14:fontcolor=white@0.22:x=w-tw-30:y=h-th-45"

# Loop 10s video to 30.0s, crop center 9:16 (405x720) and scale to 720x1280
filter_complex = (
    "[0:v]loop=loop=-1:size=240:start=0,trim=duration=30.0,"
    "crop=405:720:(in_w-405)/2:0,scale=720:1280:flags=lanczos,"
    f"{trademark_short},"
    "fade=t=in:st=0:d=0.5,"
    "fade=t=out:st=29.2:d=0.8,"
    "format=yuv420p[v_out];"
    "[0:a]aloop=loop=-1:size=48000*10,atrim=duration=30.0,volume=0.08,aformat=sample_rates=48000:channel_layouts=stereo[amb];"
    "[1:a]atrim=duration=30.0,aformat=sample_rates=48000:channel_layouts=stereo[vox];"
    "[vox][amb]amix=inputs=2:duration=first:dropout_transition=2:normalize=0,"
    "loudnorm=I=-14:TP=-1.0:LRA=7,"
    "afade=t=in:st=0:d=0.3,"
    "afade=t=out:st=29.2:d=0.8[a_out]"
)

cmd = [
    "ffmpeg", "-y",
    "-i", VIDEO_IN,
    "-i", AUDIO_IN,
    "-filter_complex", filter_complex,
    "-map", "[v_out]",
    "-map", "[a_out]",
    "-t", "30.0",
    "-c:v", "libx264",
    "-preset", "veryfast",
    "-crf", "18",
    "-pix_fmt", "yuv420p",
    "-c:a", "aac",
    "-b:a", "192k",
    "-movflags", "+faststart",
    OUTPUT_FILE
]

print("Rendering Vertical Short 1A on RTX 3060...")
subprocess.run(cmd, check=True)
print(f"Render complete: {OUTPUT_FILE}")
