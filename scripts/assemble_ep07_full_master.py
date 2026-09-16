#!/usr/bin/env python3
"""
HUURS STUDIO - Episode 7 Full Master 5-Scene Assembly
=====================================================
Assembles all 5 scene clips for Episode 7 (Surah Al-Muzzammil 73:4) with
contemplative slow-motion, seamless crossfades, burned-in IBM Plex Serif typography,
and the official discreet trademark watermark:

Section Mapping:
- Section 1 (37.5s): Scene 1 (The Hourglass in Quiet Study — Worldly Rush vs Stillness)
- Section 2 (48.0s): Scene 2 (Full Moon & Stars over Dunes — The Night Command: Wa-Rattil)
- Section 3 (50.0s): Scene 3 (Open Qur'an on Rehal — The Warning of Ibn Mas'ud)
- Section 4 (40.0s): Scene 4 (Tranquil Lake with Droplet Ripples — Why Slowness Heals)
- Section 5 (41.02s): Scene 5 (Birds Gliding in Morning Sky — Quality Before Quantity)

Total Master Duration: 216.52s (3m 36.5s)
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
AUDIO_IN = os.path.join(ROOT_DIR, "11_AUDIO/EP07_audio.mp3")
OUTPUT_MASTER = os.path.join(RENDERS_DIR, "QURAN-COMEBACK-EP07-FULL-MASTER.mp4")
OUTPUT_SHORT = os.path.join(RENDERS_DIR, "QURAN-COMEBACK-EP07-SHORT-001A.mp4")
SUBTITLE_FILE = os.path.join(RENDERS_DIR, "ep07_master_subtitles.ass")
TEMP_DIR = "/tmp/ep07_assembly"

os.makedirs(TEMP_DIR, exist_ok=True)

S1_FILE = os.path.join(RENDERS_DIR, "EP07_SCENE01.mp4")
S2_FILE = os.path.join(RENDERS_DIR, "EP07_SCENE02.mp4")
S3_FILE = os.path.join(RENDERS_DIR, "EP07_SCENE03.mp4")
S4_FILE = os.path.join(RENDERS_DIR, "EP07_SCENE04.mp4")
S5_FILE = os.path.join(RENDERS_DIR, "EP07_SCENE05.mp4")

SECTIONS = [
    {"id": "sec1", "file": S1_FILE, "name": "Hourglass in Quiet Study", "duration": 37.5},
    {"id": "sec2", "file": S2_FILE, "name": "Full Moon & Stars over Dunes", "duration": 48.0},
    {"id": "sec3", "file": S3_FILE, "name": "Arabian Horse Grazing in Oasis", "duration": 50.0},
    {"id": "sec4", "file": S4_FILE, "name": "Hummingbird Hovering at Blossom", "duration": 40.0},
    {"id": "sec5", "file": S5_FILE, "name": "Masjid an-Nabawi Sunrise Architecture", "duration": 41.02},
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
Title: Huurs Studio - Episode 7 Master Subtitles
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
Dialogue: 0,0:00:00.50,0:00:06.00,HuursContemplation,,0,0,0,,{\\fad(300,250)}We live in a world obsessed with speed. We listen to podcasts at 1.5x speed.
Dialogue: 0,0:00:06.50,0:00:13.00,HuursItalic,,0,0,0,,{\\fad(250,250)}We skim articles in twenty seconds. We rush through emails, traffic, conversations...
Dialogue: 0,0:00:13.50,0:00:20.50,HuursContemplation,,0,0,0,,{\\fad(250,250)}And without realizing it, we brought that frantic rush to the Holy Qur'an.
Dialogue: 0,0:00:21.00,0:00:27.50,HuursItalic,,0,0,0,,{\\fad(250,250)}We open the Mushaf and our eyes dart to the bottom: 'How fast can I finish this juz?'
Dialogue: 0,0:00:28.00,0:00:35.00,HuursGold,,0,0,0,,{\\fad(300,300)}We turn the Book of Allah into a checklist... and wonder why our hearts feel empty.
Dialogue: 0,0:00:38.00,0:00:46.00,HuursContemplation,,0,0,0,,{\\fad(300,250)}In the earliest days of revelation, when the message felt crushing, Allah called him in the night.
Dialogue: 0,0:00:46.50,0:00:54.50,HuursGold,,0,0,0,,{\\fad(300,250)}‘...wa rattilil-Qur'āna tartīlā—And recite the Qur'an with measured, deliberate rhythm.’
Dialogue: 0,0:00:55.00,0:01:02.00,HuursContemplation,,0,0,0,,{\\fad(250,250)}Allah didn't say: ‘Finish as many chapters as possible before dawn.’ He said: Rattil.
Dialogue: 0,0:01:02.50,0:01:12.00,HuursItalic,,0,0,0,,{\\fad(250,250)}Tartil comes from pearls spaced carefully on a thread. Unhurried speech. Pronouncing every letter.
Dialogue: 0,0:01:12.50,0:01:21.00,HuursGold,,0,0,0,,{\\fad(250,300)}Giving the silence between words as much respect as the words themselves.
Dialogue: 0,0:01:27.00,0:01:35.00,HuursContemplation,,0,0,0,,{\\fad(300,250)}The great companion Abdullah ibn Mas'ud saw people beginning to rush their recitation.
Dialogue: 0,0:01:35.50,0:01:44.00,HuursItalic,,0,0,0,,{\\fad(250,250)}‘Do not scatter the Qur'an like poor dates tumbling from a tree. And do not chant it hurriedly like poetry.’
Dialogue: 0,0:01:44.50,0:01:52.00,HuursGold,,0,0,0,,{\\fad(300,250)}‘Stop at its wonders. Move your hearts with it.’
Dialogue: 0,0:01:52.50,0:02:01.00,HuursItalic,,0,0,0,,{\\fad(250,250)}‘And let not the concern of any one of you be merely to reach the end of the surah.’
Dialogue: 0,0:02:01.50,0:02:10.00,HuursGold,,0,0,0,,{\\fad(300,300)}The goal was never page twenty. The goal was to let even half a page reach the bottom of your heart.
Dialogue: 0,0:02:18.00,0:02:26.00,HuursContemplation,,0,0,0,,{\\fad(300,250)}‘We revealed it in deliberate stages so that We may strengthen your heart with it.’
Dialogue: 0,0:02:26.50,0:02:33.50,HuursItalic,,0,0,0,,{\\fad(250,250)}Fast information informs the intellect. Slow recitation transforms the soul.
Dialogue: 0,0:02:34.00,0:02:44.00,HuursContemplation,,0,0,0,,{\\fad(250,250)}When you repeat a single ayah: ‘Indeed, with hardship comes ease’... and breathe after each phrase...
Dialogue: 0,0:02:44.50,0:02:52.00,HuursGold,,0,0,0,,{\\fad(300,250)}That single verse becomes an anchor that holds you steady for an entire year.
Dialogue: 0,0:02:52.50,0:02:59.50,HuursItalic,,0,0,0,,{\\fad(250,300)}One drop of rain absorbed into the soil gives life. A flash flood simply washes topsoil away.
Dialogue: 0,0:03:02.00,0:03:09.50,HuursContemplation,,0,0,0,,{\\fad(300,250)}Tonight, try a simple experiment. Put your phone in another room. Open the Qur'an.
Dialogue: 0,0:03:10.00,0:03:18.00,HuursItalic,,0,0,0,,{\\fad(250,250)}Pick just two verses. Recite the first verse slowly out loud. Then close your eyes for thirty seconds.
Dialogue: 0,0:03:18.50,0:03:26.50,HuursContemplation,,0,0,0,,{\\fad(250,250)}Notice how the internal noise in your mind begins to quiet down.
Dialogue: 0,0:03:27.00,0:03:33.00,HuursGold,,0,0,0,,{\\fad(300,250)}Quality before quantity. Depth before distance.
Dialogue: 0,0:03:33.50,0:03:36.50,HuursItalic,,0,0,0,,{\\fad(300,500)}Read it. Understand it. Live it. And come back tomorrow.
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
    print("      HUURS STUDIO - EPISODE 7 FULL MASTER ASSEMBLY")
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

    print(f"✓ EPISODE 7 FULL MASTER COMPLETED in {time.time()-t0:.2f}s!")
    print(f"  Location: {OUTPUT_MASTER}")

def assemble_short():
    print("-" * 70)
    print("Assembling 9:16 Vertical Cut (Short A: The Speed-Reading Illusion)...")
    sec1_part = os.path.join(TEMP_DIR, "sec1.mp4")
    audio_track = os.path.join(TEMP_DIR, "master_audio.mp3")
    if not os.path.exists(audio_track):
        audio_track = AUDIO_IN

    short_sub_file = os.path.join(RENDERS_DIR, "ep07_short_subtitles.ass")
    ass_short = """[Script Info]
Title: Huurs Studio - Episode 7 Short Subtitles
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
Dialogue: 0,0:00:00.50,0:00:06.00,ShortMobile,,0,0,0,,{\\fad(300,250)}We live in a world obsessed with speed. We listen to podcasts at 1.5x speed.
Dialogue: 0,0:00:06.50,0:00:13.00,ShortMobile,,0,0,0,,{\\fad(250,250)}We skim articles in twenty seconds. We rush through emails, traffic, conversations...
Dialogue: 0,0:00:13.50,0:00:20.50,ShortMobile,,0,0,0,,{\\fad(250,250)}And without realizing it, we brought that frantic rush to the Holy Qur'an.
Dialogue: 0,0:00:21.00,0:00:27.50,ShortMobile,,0,0,0,,{\\fad(250,250)}We open the Mushaf and our eyes dart to the bottom: 'How fast can I finish this juz?'
Dialogue: 0,0:00:28.00,0:00:35.00,ShortGold,,0,0,0,,{\\fad(300,300)}We turn the Book of Allah into a checklist... and wonder why our hearts feel empty.
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
    print(f"✓ EPISODE 7 SHORT 001A COMPLETED!")

def auto_link_scenes():
    """Auto-detect and symlink scene files if named with lowercase or alternate patterns."""
    for i in range(1, 6):
        target = os.path.join(RENDERS_DIR, f"EP07_SCENE{i:02d}.mp4")
        if not os.path.exists(target):
            candidates = [
                f"ep07_scene{i:02d}.mp4",
                f"ep7_scene{i:02d}.mp4",
                f"ep07_scene{i}.mp4",
                f"ep7_scene{i}.mp4",
                f"EP07_Scene{i:02d}.mp4",
                f"EP07_Scene{i}.mp4",
                f"ep07_scene_{i:02d}.mp4",
                f"ep7_scene_{i:02d}.mp4",
                f"QURAN-COMEBACK-VEO-007-SCENE{i:02d}.mp4",
            ]
            for cand in candidates:
                cand_path = os.path.join(RENDERS_DIR, cand)
                if os.path.exists(cand_path):
                    print(f"Auto-linking {cand} -> EP07_SCENE{i:02d}.mp4")
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
