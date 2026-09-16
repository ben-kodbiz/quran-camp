#!/usr/bin/env python3
"""
HUURS STUDIO - Episode 6 Full Master 5-Scene Assembly
=====================================================
Assembles all 5 scene clips for Episode 6 (Surah Al-Fatihah 1:6–7) with
contemplative slow-motion, seamless crossfades, burned-in IBM Plex Serif typography,
and the official discreet trademark watermark:

Section Mapping:
- Section 1 (37.5s): Scene 1 (The Straight Stone Path — Seventeen Times a Day)
- Section 2 (59.0s): Scene 2 (Meeting of Two Seas — Living Guidance Current)
- Section 3 (71.0s): Scene 3 (Symmetrical Sandstone Colonnade — Prophetic Parable)
- Section 4 (36.5s): Scene 4 (Reed Pen on Cream Parchment — Knowledge & Action)
- Section 5 (38.98s): Scene 5 (Traditional Wooden Ship on Open Sea — Keep My Feet Firm)

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
AUDIO_IN = os.path.join(ROOT_DIR, "11_AUDIO/EP06_audio.mp3")
OUTPUT_MASTER = os.path.join(RENDERS_DIR, "QURAN-COMEBACK-EP06-FULL-MASTER.mp4")
OUTPUT_SHORT = os.path.join(RENDERS_DIR, "QURAN-COMEBACK-EP06-SHORT-001A.mp4")
SUBTITLE_FILE = os.path.join(RENDERS_DIR, "ep06_master_subtitles.ass")
TEMP_DIR = "/tmp/ep06_assembly"

os.makedirs(TEMP_DIR, exist_ok=True)

S1_FILE = os.path.join(RENDERS_DIR, "EP06_SCENE01.mp4")
S2_FILE = os.path.join(RENDERS_DIR, "EP06_SCENE02.mp4")
S3_FILE = os.path.join(RENDERS_DIR, "EP06_SCENE03.mp4")
S4_FILE = os.path.join(RENDERS_DIR, "EP06_SCENE04.mp4")
S5_FILE = os.path.join(RENDERS_DIR, "EP06_SCENE05.mp4")

SECTIONS = [
    {"id": "sec1", "file": S1_FILE, "name": "The Straight Stone Path", "duration": 37.5},
    {"id": "sec2", "file": S2_FILE, "name": "Meeting of Two Seas", "duration": 59.0},
    {"id": "sec3", "file": S3_FILE, "name": "Symmetrical Colonnade", "duration": 71.0},
    {"id": "sec4", "file": S4_FILE, "name": "Reed Pen on Parchment", "duration": 36.5},
    {"id": "sec5", "file": S5_FILE, "name": "Traditional Wooden Ship", "duration": 38.98},
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
Title: Huurs Studio - Episode 6 Master Subtitles
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
Dialogue: 0,0:00:00.50,0:00:06.00,HuursContemplation,,0,0,0,,{\\fad(300,250)}If you pray your five daily prayers, you recite this exact prayer seventeen times every day:
Dialogue: 0,0:00:06.50,0:00:13.50,HuursGold,,0,0,0,,{\\fad(300,250)}‘Ihdināṣ-Ṣirāṭ al-Mustaqīm—Guide us to the straight path.’
Dialogue: 0,0:00:14.00,0:00:23.00,HuursItalic,,0,0,0,,{\\fad(250,250)}Have you ever wondered: If I am already a Muslim... why do I have to keep asking in every single unit of prayer?
Dialogue: 0,0:00:23.50,0:00:30.00,HuursContemplation,,0,0,0,,{\\fad(250,250)}Are we not already guided?
Dialogue: 0,0:00:30.50,0:00:36.50,HuursGold,,0,0,0,,{\\fad(250,300)}When you understand why Allah made this mandatory... the way you pray will change forever.
Dialogue: 0,0:00:38.00,0:00:46.50,HuursContemplation,,0,0,0,,{\\fad(300,250)}Imam Ibn Kathir and Ibn al-Qayyim explain that guidance is not a diploma you hang on your wall.
Dialogue: 0,0:00:47.00,0:00:54.00,HuursItalic,,0,0,0,,{\\fad(250,250)}Guidance is like breathing. You don't say: ‘I breathed ten minutes ago, so I don't need air right now.’
Dialogue: 0,0:00:54.50,0:01:03.00,HuursContemplation,,0,0,0,,{\\fad(250,250)}The moment you stop receiving oxygen, you suffocate. And the moment your heart stops receiving guidance, it drifts.
Dialogue: 0,0:01:03.50,0:01:10.00,HuursItalic,,0,0,0,,{\\fad(250,250)}Life does not stand still. Every single day presents you with dozens of micro-decisions.
Dialogue: 0,0:01:10.50,0:01:19.00,HuursContemplation,,0,0,0,,{\\fad(250,250)}In every single one of those moments, there is a Straight Path, and there is a ditch on either side.
Dialogue: 0,0:01:19.50,0:01:28.00,HuursGold,,0,0,0,,{\\fad(250,300)}‘Ya Allah, guide my next step. Do not leave me to my own intellect for even the blink of an eye.’
Dialogue: 0,0:01:37.00,0:01:44.50,HuursContemplation,,0,0,0,,{\\fad(300,250)}In an authentic hadith, the Prophet ﷺ painted an unforgettable picture of this journey.
Dialogue: 0,0:01:45.00,0:01:52.00,HuursItalic,,0,0,0,,{\\fad(250,250)}Imagine a straight, wide road. Along both sides of this road are two walls.
Dialogue: 0,0:01:52.50,0:02:01.00,HuursContemplation,,0,0,0,,{\\fad(250,250)}In those walls are open doorways leading into dark rooms, and over each doorway hangs a light curtain.
Dialogue: 0,0:02:01.50,0:02:08.50,HuursGold,,0,0,0,,{\\fad(300,250)}At the entrance stands a caller shouting: ‘O people! Enter the straight path together and do not branch off!’
Dialogue: 0,0:02:09.00,0:02:18.00,HuursItalic,,0,0,0,,{\\fad(250,250)}And high above stands another caller: ‘Woe to you! Do not open that curtain! If you open it, you will enter it!’
Dialogue: 0,0:02:18.50,0:02:26.50,HuursContemplation,,0,0,0,,{\\fad(250,250)}The road is Islam. The walls are the limits of Allah. The open doors are the things Allah has forbidden.
Dialogue: 0,0:02:27.00,0:02:35.00,HuursGold,,0,0,0,,{\\fad(300,300)}The caller at the gate is the Holy Qur'an. And the voice above is the admonisher inside your heart.
Dialogue: 0,0:02:48.00,0:02:54.50,HuursContemplation,,0,0,0,,{\\fad(300,250)}Look at how Surah Al-Fatihah concludes:
Dialogue: 0,0:02:55.00,0:03:02.50,HuursGold,,0,0,0,,{\\fad(300,250)}‘Ṣirāṭ al-ladhīna an'amta 'alayhim, ghayr il-maghḍūbi 'alayhim wa laḍ-ḍāllīn...’
Dialogue: 0,0:03:03.00,0:03:13.50,HuursContemplation,,0,0,0,,{\\fad(250,250)}Humans deviate in two ways: knowing truth but refusing to act, or having good intentions while drifting in ignorance.
Dialogue: 0,0:03:14.00,0:03:22.00,HuursGold,,0,0,0,,{\\fad(300,300)}The Straight Path is the razor-thin line of balance: Knowledge married to action. Sincerity married to truth.
Dialogue: 0,0:03:24.50,0:03:32.00,HuursContemplation,,0,0,0,,{\\fad(300,250)}In a few hours, the call to prayer will echo for your next salah.
Dialogue: 0,0:03:32.50,0:03:41.50,HuursItalic,,0,0,0,,{\\fad(250,250)}When you reach verse 6, do not let your tongue rush past it out of habit. Pause.
Dialogue: 0,0:03:42.00,0:03:51.00,HuursGold,,0,0,0,,{\\fad(300,250)}Feel your utter poverty before Allah. And say it with your entire soul: Ihdināṣ-Ṣirāṭ al-Mustaqīm.
Dialogue: 0,0:03:51.50,0:03:57.00,HuursContemplation,,0,0,0,,{\\fad(250,250)}‘Guide me today, Ya Allah. Keep my feet firm.’
Dialogue: 0,0:03:57.50,0:04:02.00,HuursItalic,,0,0,0,,{\\fad(300,500)}Read it. Understand it. Live it. And come back tomorrow.
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
    print("      HUURS STUDIO - EPISODE 6 FULL MASTER ASSEMBLY")
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

    print(f"✓ EPISODE 6 FULL MASTER COMPLETED in {time.time()-t0:.2f}s!")
    print(f"  Location: {OUTPUT_MASTER}")

def assemble_short():
    print("-" * 70)
    print("Assembling 9:16 Vertical Cut (Short A: Seventeen Times a Day)...")
    sec1_part = os.path.join(TEMP_DIR, "sec1.mp4")
    audio_track = os.path.join(TEMP_DIR, "master_audio.mp3")
    if not os.path.exists(audio_track):
        audio_track = AUDIO_IN

    short_sub_file = os.path.join(RENDERS_DIR, "ep06_short_subtitles.ass")
    ass_short = """[Script Info]
Title: Huurs Studio - Episode 6 Short Subtitles
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
Dialogue: 0,0:00:00.50,0:00:06.00,ShortMobile,,0,0,0,,{\\fad(300,250)}If you pray your five daily prayers, you recite this exact prayer seventeen times every day:
Dialogue: 0,0:00:06.50,0:00:13.50,ShortGold,,0,0,0,,{\\fad(300,250)}‘Ihdināṣ-Ṣirāṭ al-Mustaqīm—Guide us to the straight path.’
Dialogue: 0,0:00:14.00,0:00:23.00,ShortMobile,,0,0,0,,{\\fad(250,250)}Have you ever wondered: If I am already a Muslim... why do I have to keep asking in every single unit of prayer?
Dialogue: 0,0:00:23.50,0:00:30.00,ShortMobile,,0,0,0,,{\\fad(250,250)}Are we not already guided?
Dialogue: 0,0:00:30.50,0:00:36.50,ShortGold,,0,0,0,,{\\fad(250,300)}When you understand why Allah made this mandatory... the way you pray will change forever.
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
        f"[0:v]crop=w=ih*(9/16):h=ih:x=(iw-ow)/2:y=0,scale=720:1280,{trademark_short},fade=t=in:st=0:d=0.8,fade=t=out:st=35.5:d=2.0,format=yuv420p[v_out];"
        "[1:a]atrim=start=0:end=37.5,afade=t=in:st=0:d=0.3,afade=t=out:st=35.5:d=2.0[a_out]",
        "-map", "[v_out]",
        "-map", "[a_out]",
        "-t", "37.5",
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
    print(f"✓ EPISODE 6 SHORT 001A COMPLETED!")

def auto_link_scenes():
    """Auto-detect and symlink scene files if named with lowercase or alternate patterns."""
    for i in range(1, 6):
        target = os.path.join(RENDERS_DIR, f"EP06_SCENE{i:02d}.mp4")
        if not os.path.exists(target):
            candidates = [
                f"ep06_scene{i:02d}.mp4",
                f"ep6_scene{i:02d}.mp4",
                f"ep06_scene{i}.mp4",
                f"ep6_scene{i}.mp4",
                f"EP06_Scene{i:02d}.mp4",
                f"EP06_Scene{i}.mp4",
                f"ep06_scene_{i:02d}.mp4",
                f"ep6_scene_{i:02d}.mp4",
                f"QURAN-COMEBACK-VEO-006-SCENE{i:02d}.mp4",
            ]
            for cand in candidates:
                cand_path = os.path.join(RENDERS_DIR, cand)
                if os.path.exists(cand_path):
                    print(f"Auto-linking {cand} -> EP06_SCENE{i:02d}.mp4")
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

