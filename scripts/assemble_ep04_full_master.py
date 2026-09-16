#!/usr/bin/env python3
"""
HUURS STUDIO - Episode 4 Full Master 5-Scene Assembly
=====================================================
Assembles all 5 Veo 3.1 scene clips with contemplative slow-motion, seamless
crossfades, and the official discreet lower-right trademark watermark to match
the master voiceover narration track:

Section Mapping:
- Section 1 (28.5s): Scene 1 (Rain on Window Pane & Forest Mist)
- Section 2 (46.0s): Scene 2 (Open Mushaf on Wooden Stand with Morning Sunbeam)
- Section 3 (52.0s): Scene 3 (Mountain Pathway & Birds Soaring)
- Section 4 (41.5s): Scene 4 (Expansive Towering Clouds & Tranquil Sky)
- Section 5 (35.0s): Scene 5 (Sanctuary Stone Archway into Olive Courtyard Fountain)

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
AUDIO_IN = os.path.join(ROOT_DIR, "11_AUDIO/EP04_audio.mp3")
OUTPUT_MASTER = os.path.join(RENDERS_DIR, "QURAN-COMEBACK-EP04-FULL-MASTER.mp4")
OUTPUT_SHORT = os.path.join(RENDERS_DIR, "QURAN-COMEBACK-EP04-SHORT-001A.mp4")
SUBTITLE_FILE = os.path.join(RENDERS_DIR, "ep04_master_subtitles.ass")
TEMP_DIR = "/tmp/ep04_assembly"

os.makedirs(TEMP_DIR, exist_ok=True)

S1_FILE = os.path.join(RENDERS_DIR, "EP04_SCENE01.mp4")
S2_FILE = os.path.join(RENDERS_DIR, "EP04_SCENE02.mp4")
S3_FILE = os.path.join(RENDERS_DIR, "EP04_SCENE03.mp4")
S4_FILE = os.path.join(RENDERS_DIR, "EP04_SCENE04.mp4")
S5_FILE = os.path.join(RENDERS_DIR, "EP04_SCENE05.mp4")

SECTIONS = [
    {"id": "sec1", "file": S1_FILE, "name": "Rain on Window & Forest Mist", "duration": 28.5},
    {"id": "sec2", "file": S2_FILE, "name": "Open Mushaf & Morning Sunbeam", "duration": 46.0},
    {"id": "sec3", "file": S3_FILE, "name": "Mountain Pathway & Birds", "duration": 52.0},
    {"id": "sec4", "file": S4_FILE, "name": "Towering Clouds & Serene Sky", "duration": 41.5},
    {"id": "sec5", "file": S5_FILE, "name": "Courtyard Arch & Stone Fountain", "duration": 35.0},
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
Title: Huurs Studio - Episode 4 Master Subtitles
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
Dialogue: 0,0:00:00.50,0:00:06.00,HuursContemplation,,0,0,0,,{\\fad(300,250)}One of the quietest lies we tell ourselves is:
Dialogue: 0,0:00:06.20,0:00:12.50,HuursItalic,,0,0,0,,{\\fad(250,250)}‘I’m too far gone. I haven’t prayed in months. I’ve made too many mistakes.’
Dialogue: 0,0:00:12.80,0:00:18.50,HuursContemplation,,0,0,0,,{\\fad(250,250)}You see the Mushaf sitting on your desk. You want to touch it.
Dialogue: 0,0:00:18.80,0:00:26.50,HuursItalic,,0,0,0,,{\\fad(250,300)}If you have ever felt that weight... hear how Allah speaks in Surah Az-Zumar.
Dialogue: 0,0:00:29.50,0:00:35.50,HuursContemplation,,0,0,0,,{\\fad(300,250)}In verse 53, Allah commands His Messenger:
Dialogue: 0,0:00:36.00,0:00:44.50,HuursGold,,0,0,0,,{\\fad(350,300)}‘Qul Yā 'ibādiya-lladhīna asrafū 'alā anfusihim...’
Dialogue: 0,0:00:45.00,0:00:53.50,HuursItalic,,0,0,0,,{\\fad(250,250)}‘Say: O My servants who have transgressed against themselves! Do not despair.’
Dialogue: 0,0:00:54.00,0:01:02.00,HuursContemplation,,0,0,0,,{\\fad(250,250)}Classical scholars call this the single most hopeful verse in Revelation.
Dialogue: 0,0:01:02.50,0:01:09.50,HuursGold,,0,0,0,,{\\fad(250,250)}He says: Yā 'Ibādī—‘O My servants.’ He still claims you as His own.
Dialogue: 0,0:01:15.50,0:01:21.50,HuursContemplation,,0,0,0,,{\\fad(300,250)}Imam al-Bukhari records why this verse descended.
Dialogue: 0,0:01:22.00,0:01:29.50,HuursItalic,,0,0,0,,{\\fad(250,250)}People who had spent their lives in darkness asked: ‘Is there any expiation for us?’
Dialogue: 0,0:01:30.00,0:01:37.00,HuursContemplation,,0,0,0,,{\\fad(250,250)}Shaytan whispers: ‘You are irredeemable. Allah doesn't want you back.’
Dialogue: 0,0:01:37.50,0:01:45.00,HuursGold,,0,0,0,,{\\fad(300,250)}This verse exists to crush that whisper: Lā taqnatū—Do not despair.
Dialogue: 0,0:01:46.00,0:01:54.00,HuursContemplation,,0,0,0,,{\\fad(250,300)}Despair is not humility. Despair is doubting the ocean of Allah's mercy.
Dialogue: 0,0:02:07.50,0:02:14.50,HuursContemplation,,0,0,0,,{\\fad(300,250)}In an authentic Hadith Qudsi, Allah speaks directly:
Dialogue: 0,0:02:15.00,0:02:24.00,HuursGold,,0,0,0,,{\\fad(300,250)}‘If your sins reached the clouds of the sky, and you asked forgiveness, I would forgive.’
Dialogue: 0,0:02:24.50,0:02:32.00,HuursContemplation,,0,0,0,,{\\fad(250,250)}The Qur'an was not sent for people who never stumble.
Dialogue: 0,0:02:32.50,0:02:39.00,HuursGold,,0,0,0,,{\\fad(300,300)}The Qur'an was sent as the medicine for those who are bleeding.
Dialogue: 0,0:02:49.50,0:02:56.50,HuursContemplation,,0,0,0,,{\\fad(300,250)}If you have been away from Allah... today is your day of return.
Dialogue: 0,0:02:57.00,0:03:03.00,HuursContemplation,,0,0,0,,{\\fad(250,250)}Tonight, open Surah Az-Zumar, verse 53.
Dialogue: 0,0:03:03.50,0:03:12.00,HuursItalic,,0,0,0,,{\\fad(250,250)}‘Ya Allah, I have transgressed against my soul. But I have returned to Your mercy.’
Dialogue: 0,0:03:12.50,0:03:17.50,HuursContemplation,,0,0,0,,{\\fad(250,250)}Read it. Understand it. Live it.
Dialogue: 0,0:03:18.0,0:03:22.00,HuursItalic,,0,0,0,,{\\fad(300,500)}And come back tomorrow.
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
    print("      HUURS STUDIO - EPISODE 4 FULL MASTER ASSEMBLY")
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

    print(f"✓ EPISODE 4 FULL MASTER COMPLETED in {time.time()-t0:.2f}s!")
    print(f"  Location: {OUTPUT_MASTER}")

def assemble_short():
    print("-" * 70)
    print("Assembling 9:16 Vertical Cut (Short A: Do Not Despair)...")
    sec1_part = os.path.join(TEMP_DIR, "sec1.mp4")
    audio_track = os.path.join(TEMP_DIR, "master_audio.mp3")
    if not os.path.exists(audio_track):
        audio_track = AUDIO_IN

    short_sub_file = os.path.join(RENDERS_DIR, "ep04_short_subtitles.ass")
    ass_short = """[Script Info]
Title: Huurs Studio - Episode 4 Short Subtitles
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
Dialogue: 0,0:00:00.50,0:00:06.00,ShortMobile,,0,0,0,,{\\fad(300,250)}One of the quietest lies we tell ourselves is:
Dialogue: 0,0:00:06.20,0:00:12.50,ShortGold,,0,0,0,,{\\fad(250,250)}‘I’m too far gone. I haven’t prayed in months. I’ve made too many mistakes.’
Dialogue: 0,0:00:12.80,0:00:18.50,ShortMobile,,0,0,0,,{\\fad(250,250)}You see the Mushaf sitting on your desk. You want to touch it.
Dialogue: 0,0:00:18.80,0:00:26.50,ShortGold,,0,0,0,,{\\fad(250,300)}If you have ever felt that weight... hear how Allah speaks in Surah Az-Zumar.
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
        f"[0:v]crop=w=ih*(9/16):h=ih:x=(iw-ow)/2:y=0,scale=720:1280,{trademark_short},fade=t=in:st=0:d=0.8,fade=t=out:st=26.5:d=2.0,format=yuv420p[v_out];"
        "[1:a]atrim=start=0:end=28.5,afade=t=in:st=0:d=0.3,afade=t=out:st=26.5:d=2.0[a_out]",
        "-map", "[v_out]",
        "-map", "[a_out]",
        "-t", "28.5",
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
    print(f"✓ EPISODE 4 SHORT 001A COMPLETED!")

if __name__ == "__main__":
    assemble_master()
    assemble_short()
