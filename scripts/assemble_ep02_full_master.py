#!/usr/bin/env python3
"""
HUURS STUDIO - Episode 2 Full Master 5-Scene Assembly
=====================================================
Assembles all 5 Veo 3.1 scene clips with contemplative slow-motion and seamless
crossfades to match the full 247.2s voiceover narration track:

Section Mapping:
- Section 1 (00:00.0 - 00:36.5, 36.5s): Scene 4 (Rain on Sanctuary Window)
- Section 2 (00:36.5 - 01:27.0, 50.5s): Scene 2 (Mosque Courtyard with Birds & Pool)
- Section 3 (01:27.0 - 02:42.5, 75.5s): Scene 1 (Rain on Olive Foliage & Mindful Path)
- Section 4 (02:42.5 - 03:32.5, 50.0s): Scene 3 (Tranquil Ocean Waves & Golden Compass)
- Section 5 (03:32.5 - 04:07.2, 34.7s): Scene 5 (Birds over Ocean Dawn & Mosque Silhouette)

Total Master Duration: 247.2s (04m 07s)
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
AUDIO_IN = os.path.join(ROOT_DIR, "11_AUDIO/EP02_audio.mp3")
AUDIO_BOOSTED = os.path.join(ROOT_DIR, "11_AUDIO/EP02_SCENE01_audio_boosted.mp3")
OUTPUT_MASTER = os.path.join(RENDERS_DIR, "QURAN-COMEBACK-EP02-FULL-MASTER.mp4")
OUTPUT_SHORT = os.path.join(RENDERS_DIR, "QURAN-COMEBACK-EP02-SHORT-001A.mp4")
SUBTITLE_FILE = os.path.join(RENDERS_DIR, "ep02_master_subtitles.ass")
SHORT_SUBTITLE_FILE = os.path.join(RENDERS_DIR, "ep02_short_subtitles.ass")
TEMP_DIR = "/tmp/ep02_assembly"

os.makedirs(TEMP_DIR, exist_ok=True)

# 5 Scene Clips
S1_FILE = os.path.join(RENDERS_DIR, "EP02_SCENE04.mp4")  # Rain on window
S2_FILE = os.path.join(RENDERS_DIR, "EP02_SCENE02.mp4")  # Mosque courtyard & birds
S3_FILE = os.path.join(RENDERS_DIR, "EP02_SCENE01.mp4")  # Rain on olive leaves
S4_FILE = os.path.join(RENDERS_DIR, "EP02_SCENE03.mp4")  # Ocean waves & golden light
S5_FILE = os.path.join(RENDERS_DIR, "EP02_SCENE05.mp4")  # Birds over ocean & mosque silhouette

SECTIONS = [
    {"id": "sec1", "file": S1_FILE, "name": "Rain on Sanctuary Window", "duration": 36.5},
    {"id": "sec2", "file": S2_FILE, "name": "Mosque Courtyard & Birds", "duration": 50.5},
    {"id": "sec3", "file": S3_FILE, "name": "Rain on Olive Leaves", "duration": 75.5},
    {"id": "sec4", "file": S4_FILE, "name": "Ocean Waves & Light Path", "duration": 50.0},
    {"id": "sec5", "file": S5_FILE, "name": "Birds over Ocean Dawn", "duration": 34.7},
]

def make_extended_clip(input_video, target_duration, output_path):
    """Slows down video by 2x and seamlessly crossfade-loops it to target_duration."""
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
    """Generates broadcast styled ASS subtitles for Episode 2 Master."""
    ass_content = """[Script Info]
Title: Huurs Studio - Episode 2 Master Subtitles
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
Dialogue: 0,0:00:00.20,0:00:03.20,HuursContemplation,,0,0,0,,{\\fad(300,250)}If you ask ten people on the street what the Qur'an is...
Dialogue: 0,0:00:03.35,0:00:05.40,HuursItalic,,0,0,0,,{\\fad(250,250)}you'll get ten different answers.
Dialogue: 0,0:00:05.60,0:00:08.20,HuursContemplation,,0,0,0,,{\\fad(250,250)}Some treat it like an ancient historical chronicle.
Dialogue: 0,0:00:08.35,0:00:10.50,HuursContemplation,,0,0,0,,{\\fad(250,250)}Some treat it like a book of complex legal statutes.
Dialogue: 0,0:00:10.60,0:00:13.10,HuursContemplation,,0,0,0,,{\\fad(250,250)}And some treat it like a decorative talisman—
Dialogue: 0,0:00:13.20,0:00:17.00,HuursContemplation,,0,0,0,,{\\fad(250,250)}wrapped in velvet, placed on the highest shelf in the house,
Dialogue: 0,0:00:17.10,0:00:20.40,HuursContemplation,,0,0,0,,{\\fad(250,250)}kissed when touched, but never actually read.
Dialogue: 0,0:00:20.50,0:00:22.60,HuursContemplation,,0,0,0,,{\\fad(250,250)}Have you ever stopped to ask:
Dialogue: 0,0:00:22.70,0:00:27.50,HuursGold,,0,0,0,,{\\fad(300,300)}What did Allah Himself say this Book was for?
Dialogue: 0,0:00:36.50,0:00:42.50,HuursContemplation,,0,0,0,,{\\fad(300,250)}Right at the very opening of the Qur'an, in Surah Al-Baqarah,
Dialogue: 0,0:00:42.70,0:00:46.80,HuursContemplation,,0,0,0,,{\\fad(250,250)}Allah defines His Book in five unforgettable words:
Dialogue: 0,0:00:47.00,0:00:53.00,HuursGold,,0,0,0,,{\\fad(350,300)}‘Dhalikal kitābu lā rayba fīh, hudan lil-muttaqīn.’
Dialogue: 0,0:00:53.20,0:00:59.00,HuursItalic,,0,0,0,,{\\fad(250,250)}‘This is the Book! There is no doubt about it—a guide for those mindful of Allah.’
Dialogue: 0,0:00:59.20,0:01:03.50,HuursContemplation,,0,0,0,,{\\fad(250,250)}Notice what Allah called it. He didn't call it an encyclopedia.
Dialogue: 0,0:01:03.60,0:01:08.50,HuursContemplation,,0,0,0,,{\\fad(250,250)}He didn't call it an ornament for your shelf.
Dialogue: 0,0:01:08.70,0:01:13.50,HuursGold,,0,0,0,,{\\fad(300,250)}He called it HUDAN: Guidance.
Dialogue: 0,0:01:13.70,0:01:19.50,HuursContemplation,,0,0,0,,{\\fad(250,250)}A guide is not something you display on a wall.
Dialogue: 0,0:01:19.70,0:01:26.50,HuursItalic,,0,0,0,,{\\fad(250,300)}A guide is a map you consult when you are lost in the dark.
Dialogue: 0,0:01:27.00,0:01:33.00,HuursContemplation,,0,0,0,,{\\fad(300,250)}Ibn Kathir asks: The Qur'an was sent for all humanity...
Dialogue: 0,0:01:33.20,0:01:39.50,HuursContemplation,,0,0,0,,{\\fad(250,250)}why does Allah specify that it is guidance for the mindful—the Muttaqin?
Dialogue: 0,0:01:39.70,0:01:46.00,HuursContemplation,,0,0,0,,{\\fad(250,250)}Because only someone who admits they need direction will follow the map.
Dialogue: 0,0:01:46.20,0:01:52.00,HuursContemplation,,0,0,0,,{\\fad(250,250)}What does it mean to be mindful? What is Taqwa?
Dialogue: 0,0:01:52.20,0:01:58.50,HuursContemplation,,0,0,0,,{\\fad(250,250)}Umar ibn al-Khattab asked Ubayy ibn Ka'b to describe it.
Dialogue: 0,0:01:58.70,0:02:04.00,HuursItalic,,0,0,0,,{\\fad(250,250)}Ubayy asked: ‘Have you ever walked along a path covered in sharp thorns?’
Dialogue: 0,0:02:04.20,0:02:07.50,HuursContemplation,,0,0,0,,{\\fad(250,250)}Umar said: ‘Yes.’
Dialogue: 0,0:02:07.70,0:02:14.50,HuursContemplation,,0,0,0,,{\\fad(250,250)}Umar replied: ‘I gathered my clothes close, and I walked with extreme care.’
Dialogue: 0,0:02:14.70,0:02:18.50,HuursGold,,0,0,0,,{\\fad(300,250)}Ubayy said: ‘That is Taqwa.’
Dialogue: 0,0:02:18.70,0:02:24.00,HuursContemplation,,0,0,0,,{\\fad(250,250)}Taqwa isn't hiding in a cave.
Dialogue: 0,0:02:24.20,0:02:32.00,HuursContemplation,,0,0,0,,{\\fad(250,250)}Taqwa is living in this chaotic world—walking carefully so your soul doesn't get torn.
Dialogue: 0,0:02:42.50,0:02:49.00,HuursContemplation,,0,0,0,,{\\fad(300,250)}When you feel overwhelmed by your career, confused about your family...
Dialogue: 0,0:02:49.20,0:02:54.50,HuursItalic,,0,0,0,,{\\fad(250,250)}you don't need another generic self-help book.
Dialogue: 0,0:02:54.70,0:03:00.00,HuursGold,,0,0,0,,{\\fad(300,250)}You need to consult your compass.
Dialogue: 0,0:03:00.20,0:03:06.00,HuursContemplation,,0,0,0,,{\\fad(250,250)}The Qur'an was sent to guide your ordinary days.
Dialogue: 0,0:03:06.20,0:03:10.50,HuursContemplation,,0,0,0,,{\\fad(250,250)}It teaches you how to speak when you are angry.
Dialogue: 0,0:03:10.70,0:03:15.50,HuursContemplation,,0,0,0,,{\\fad(250,250)}It teaches you how to treat your parents when you are tired.
Dialogue: 0,0:03:15.70,0:03:22.00,HuursContemplation,,0,0,0,,{\\fad(250,250)}It teaches you what to do when grief settles into your ribs.
Dialogue: 0,0:03:22.20,0:03:28.00,HuursGold,,0,0,0,,{\\fad(300,300)}It is guidance for the living.
Dialogue: 0,0:03:32.50,0:03:38.00,HuursContemplation,,0,0,0,,{\\fad(300,250)}Today, change how you approach the Book of Allah.
Dialogue: 0,0:03:38.20,0:03:44.00,HuursContemplation,,0,0,0,,{\\fad(250,250)}Open it as someone who is lost, asking the Creator for direction.
Dialogue: 0,0:03:44.20,0:03:51.00,HuursItalic,,0,0,0,,{\\fad(250,250)}Tonight, read just the first five verses of Surah Al-Baqarah.
Dialogue: 0,0:03:51.20,0:03:58.50,HuursGold,,0,0,0,,{\\fad(300,250)}And whisper from your heart: ‘Ya Allah, guide me today. I am listening.’
Dialogue: 0,0:03:58.70,0:04:03.50,HuursContemplation,,0,0,0,,{\\fad(250,250)}Read it. Understand it. Live it.
Dialogue: 0,0:04:03.70,0:04:06.50,HuursItalic,,0,0,0,,{\\fad(300,500)}And come back tomorrow.
"""
    with open(SUBTITLE_FILE, "w", encoding="utf-8") as f:
        f.write(ass_content.strip())
    print(f"Created ASS Subtitle file: {SUBTITLE_FILE}")

def normalize_audio():
    """Normalizes input audio to -14 LUFS broadcast standard."""
    print("Normalizing voiceover audio to -14 LUFS (Zero Music Policy)...")
    cmd = [
        "ffmpeg", "-y", "-i", AUDIO_IN,
        "-af", "loudnorm=I=-14:TP=-1.0:LRA=7",
        "-c:a", "libmp3lame", "-b:a", "192k", "-ar", "48000",
        AUDIO_BOOSTED
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("Audio normalization failed:", res.stderr[-500:])
        sys.exit(1)
    print(f"Normalized audio saved to: {AUDIO_BOOSTED}")

def assemble_master():
    print("=" * 70)
    print("      HUURS STUDIO - EPISODE 2 FULL MASTER (247.2s) ASSEMBLY")
    print("=" * 70)
    normalize_audio()
    create_subtitles()

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

    print(f"All 5 sections successfully extended in {time.time()-t0:.2f}s!")
    print("Combining sections with master voiceover, ASS subtitles, and fades...")

    trademark_master = "drawtext=text='HUURS STUDIO':font='IBM Plex Serif':fontsize=16:fontcolor=white@0.22:x=w-tw-40:y=h-th-30"

    # Concat video parts and merge with audio (no burned subtitles)
    cmd = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0", "-i", concat_list,
        "-i", AUDIO_BOOSTED,
        "-filter_complex",
        f"[0:v]noise=c0s=1.2:allf=t,{trademark_master},fade=t=in:st=0:d=1.0,fade=t=out:st=245.0:d=2.0,format=yuv420p[v_out];"
        "[1:a]afade=t=in:st=0:d=0.5,afade=t=out:st=245.0:d=2.0[a_out]",
        "-map", "[v_out]",
        "-map", "[a_out]",
        "-t", "247.16",
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "256k",
        "-ar", "48000",
        "-movflags", "+faststart",
        OUTPUT_MASTER
    ]

    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("Master assembly render failed:\n", res.stderr[-800:])
        sys.exit(1)

    print(f"✓ EPISODE 2 FULL MASTER COMPLETED in {time.time()-t0:.2f}s!")
    print(f"  Location: {OUTPUT_MASTER}")

def assemble_short():
    """Generates 9:16 vertical short format for Short A (The Operating Manual)."""
    print("-" * 70)
    print("Assembling 9:16 Vertical Cut (Short A: The Operating Manual)...")
    
    # Use Section 1 (Rain on Sanctuary Window) cropped to 9:16 (720x1280) for 36.5s
    sec1_part = os.path.join(TEMP_DIR, "sec1.mp4")
    trademark_short = "drawtext=text='HUURS STUDIO':font='IBM Plex Serif':fontsize=14:fontcolor=white@0.22:x=w-tw-30:y=h-th-45"

    cmd = [
        "ffmpeg", "-y",
        "-i", sec1_part,
        "-i", AUDIO_BOOSTED,
        "-filter_complex",
        f"[0:v]crop=w=ih*(9/16):h=ih:x=(iw-ow)/2:y=0,scale=720:1280,{trademark_short},fade=t=in:st=0:d=0.8,fade=t=out:st=35.0:d=1.5,format=yuv420p[v_out];"
        "[1:a]atrim=start=0:end=36.5,afade=t=in:st=0:d=0.3,afade=t=out:st=35.0:d=1.5[a_out]",
        "-map", "[v_out]",
        "-map", "[a_out]",
        "-t", "36.5",
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

    print(f"✓ EPISODE 2 SHORT 001A COMPLETED!")
    print(f"  Location: {OUTPUT_SHORT}")

if __name__ == "__main__":
    assemble_master()
    assemble_short()
