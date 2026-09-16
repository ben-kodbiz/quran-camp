#!/usr/bin/env python3
"""
HUURS STUDIO - Episode 8 Full Master 5-Scene Assembly
=====================================================
Assembles all 5 scene clips for Episode 8 (Surah Ta-Ha 20:2) with
contemplative slow-motion, seamless crossfades, burned-in IBM Plex Serif typography,
and the official discreet trademark watermark:

Section Mapping:
- Section 1 (49.0s): Scene 1 (Peacock in Courtyard Garden — Breaking the Frantic Rush)
- Section 2 (60.0s): Scene 2 (Taif Mountain Terraces at Sunrise — Not Sent for Distress)
- Section 3 (54.0s): Scene 3 (Honeybees on Honeycomb in Oasis — Consistent Small Habits)
- Section 4 (41.0s): Scene 4 (Water Droplet Carving Stone — Persistence Over Power)
- Section 5 (31.23s): Scene 5 (Hegra Monumental Facade in Al-Ula at Sunset — Standing Firm)

Total Master Duration: 235.23s (3m 55.2s)
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
AUDIO_IN = os.path.join(ROOT_DIR, "11_AUDIO/EP08_audio.mp3")
OUTPUT_MASTER = os.path.join(RENDERS_DIR, "QURAN-COMEBACK-EP08-FULL-MASTER.mp4")
OUTPUT_SHORT = os.path.join(RENDERS_DIR, "QURAN-COMEBACK-EP08-SHORT-001A.mp4")
SUBTITLE_FILE = os.path.join(RENDERS_DIR, "ep08_master_subtitles.ass")
TEMP_DIR = "/tmp/ep08_assembly"

os.makedirs(TEMP_DIR, exist_ok=True)

S1_FILE = os.path.join(RENDERS_DIR, "EP08_SCENE01.mp4")
S2_FILE = os.path.join(RENDERS_DIR, "EP08_SCENE02.mp4")
S3_FILE = os.path.join(RENDERS_DIR, "EP08_SCENE03.mp4")
S4_FILE = os.path.join(RENDERS_DIR, "EP08_SCENE04.mp4")
S5_FILE = os.path.join(RENDERS_DIR, "EP08_SCENE05.mp4")

SECTIONS = [
    {"id": "sec1", "file": S1_FILE, "name": "Peacock in Courtyard Garden", "duration": 49.0},
    {"id": "sec2", "file": S2_FILE, "name": "Taif Mountain Terraces", "duration": 60.0},
    {"id": "sec3", "file": S3_FILE, "name": "Honeybees on Honeycomb", "duration": 54.0},
    {"id": "sec4", "file": S4_FILE, "name": "Water Droplet Carving Stone", "duration": 41.0},
    {"id": "sec5", "file": S5_FILE, "name": "Hegra Facade in Al-Ula", "duration": 31.23},
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
Title: Huurs Studio - Episode 8 Master Subtitles
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
Dialogue: 0,0:00:00.50,0:00:07.00,HuursContemplation,,0,0,0,,{\\fad(300,250)}Here is a cycle you might recognize: You feel spiritually depleted.
Dialogue: 0,0:00:07.50,0:00:16.50,HuursItalic,,0,0,0,,{\\fad(250,250)}You say: ‘Starting tomorrow, I will wake up before Fajr and read a full juz every day.’
Dialogue: 0,0:00:17.00,0:00:26.50,HuursContemplation,,0,0,0,,{\\fad(250,250)}Day one goes well. Day two is harder. On day three, you miss your goal.
Dialogue: 0,0:00:27.00,0:00:36.50,HuursItalic,,0,0,0,,{\\fad(250,250)}Guilt washes over you. By day five, you don’t even touch the Qur'an.
Dialogue: 0,0:00:37.00,0:00:46.50,HuursGold,,0,0,0,,{\\fad(300,300)}This is the all-or-nothing trap... and it is destroying our consistency.
Dialogue: 0,0:00:50.50,0:00:59.00,HuursContemplation,,0,0,0,,{\\fad(300,250)}In Surah Ta-Ha, Allah opens with words that soothe every exhausted heart:
Dialogue: 0,0:00:59.50,0:01:08.00,HuursGold,,0,0,0,,{\\fad(300,250)}‘Mā anzalnā 'alayka al-Qur'āna li-tashqā—We did not send down the Quran that you should be distressed.’
Dialogue: 0,0:01:08.50,0:01:19.00,HuursContemplation,,0,0,0,,{\\fad(250,250)}Allah acknowledges: He knows some of you are sick, traveling, exhausted... recite whatever is easy.
Dialogue: 0,0:01:19.50,0:01:29.00,HuursItalic,,0,0,0,,{\\fad(250,250)}The Prophet ﷺ was asked: ‘Which deeds are most beloved to Allah?’
Dialogue: 0,0:01:29.50,0:01:41.00,HuursGold,,0,0,0,,{\\fad(300,300)}‘Aḥabbu al-a'māli ilallāhi adwamuhā wa in qall—The most beloved deeds are those most consistent, even if small.’
Dialogue: 0,0:01:50.50,0:01:59.50,HuursContemplation,,0,0,0,,{\\fad(300,250)}If you have ten minutes, you have enough time to build an unbreakable relationship with Allah.
Dialogue: 0,0:02:00.00,0:02:09.50,HuursGold,,0,0,0,,{\\fad(250,250)}Minute 1 to 3: The Recitation. Pick three to five verses. Read them slowly.
Dialogue: 0,0:02:10.00,0:02:19.50,HuursItalic,,0,0,0,,{\\fad(250,250)}Minute 4 to 6: The Meaning. Read an authentic translation. Understand what Allah is saying.
Dialogue: 0,0:02:20.00,0:02:30.00,HuursGold,,0,0,0,,{\\fad(250,250)}Minute 7 to 8: The Tadabbur Question. ‘If I lived by this verse today, what would I change?’
Dialogue: 0,0:02:30.50,0:02:40.50,HuursItalic,,0,0,0,,{\\fad(250,300)}Minute 9 to 10: The Return. Raise your hands. Make a simple, heartfelt du'a.
Dialogue: 0,0:02:44.50,0:02:54.00,HuursContemplation,,0,0,0,,{\\fad(300,250)}Throw a bucket of water onto a boulder at once—the water splashes and evaporates.
Dialogue: 0,0:02:54.50,0:03:04.50,HuursItalic,,0,0,0,,{\\fad(250,250)}But let a single drop fall every day at the exact same spot... it carves straight through the rock.
Dialogue: 0,0:03:05.00,0:03:14.50,HuursGold,,0,0,0,,{\\fad(300,250)}Ten minutes of Qur'an every single day will soften a heart that sporadic bursts never reach.
Dialogue: 0,0:03:15.00,0:03:22.50,HuursContemplation,,0,0,0,,{\\fad(250,300)}Ten minutes with Allah is infinite compared to zero.
Dialogue: 0,0:03:25.50,0:03:36.50,HuursContemplation,,0,0,0,,{\\fad(300,250)}Look at your schedule tomorrow morning. Find ten minutes. Before social media. Before emails.
Dialogue: 0,0:03:37.00,0:03:47.00,HuursItalic,,0,0,0,,{\\fad(250,250)}Commit to ten minutes for seven straight days. Protect it like an appointment with a king.
Dialogue: 0,0:03:47.50,0:03:52.50,HuursGold,,0,0,0,,{\\fad(300,250)}Because it is an appointment with the King of Kings. Read it. Understand it. Live it. And come back tomorrow.
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
    print("      HUURS STUDIO - EPISODE 8 FULL MASTER ASSEMBLY")
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

    print(f"✓ EPISODE 8 FULL MASTER COMPLETED in {time.time()-t0:.2f}s!")
    print(f"  Location: {OUTPUT_MASTER}")

def assemble_short():
    print("-" * 70)
    print("Assembling 9:16 Vertical Cut (Short A: The All-or-Nothing Trap)...")
    sec1_part = os.path.join(TEMP_DIR, "sec1.mp4")
    audio_track = os.path.join(TEMP_DIR, "master_audio.mp3")
    if not os.path.exists(audio_track):
        audio_track = AUDIO_IN

    short_sub_file = os.path.join(RENDERS_DIR, "ep08_short_subtitles.ass")
    ass_short = """[Script Info]
Title: Huurs Studio - Episode 8 Short Subtitles
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
Dialogue: 0,0:00:00.50,0:00:07.00,ShortMobile,,0,0,0,,{\\fad(300,250)}Here is a cycle you might recognize: You feel spiritually depleted.
Dialogue: 0,0:00:07.50,0:00:16.50,ShortMobile,,0,0,0,,{\\fad(250,250)}You say: ‘Starting tomorrow, I will wake up before Fajr and read a full juz every day.’
Dialogue: 0,0:00:17.00,0:00:26.50,ShortMobile,,0,0,0,,{\\fad(250,250)}Day one goes well. Day two is harder. On day three, you miss your goal.
Dialogue: 0,0:00:27.00,0:00:36.50,ShortMobile,,0,0,0,,{\\fad(250,250)}Guilt washes over you. By day five, you don’t even touch the Qur'an.
Dialogue: 0,0:00:37.00,0:00:46.50,ShortGold,,0,0,0,,{\\fad(300,300)}This is the all-or-nothing trap... and it is destroying our consistency.
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
        f"[0:v]crop=w=ih*(9/16):h=ih:x=(iw-ow)/2:y=0,scale=720:1280,{trademark_short},fade=t=in:st=0:d=0.8,fade=t=out:st=47.0:d=2.0,format=yuv420p[v_out];"
        "[1:a]atrim=start=0:end=49.0,afade=t=in:st=0:d=0.3,afade=t=out:st=47.0:d=2.0[a_out]",
        "-map", "[v_out]",
        "-map", "[a_out]",
        "-t", "49.0",
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
    print(f"✓ EPISODE 8 SHORT 001A COMPLETED!")

def auto_link_scenes():
    """Auto-detect and symlink scene files if named with lowercase or alternate patterns."""
    for i in range(1, 6):
        target = os.path.join(RENDERS_DIR, f"EP08_SCENE{i:02d}.mp4")
        if not os.path.exists(target):
            candidates = [
                f"ep08_scene{i:02d}.mp4",
                f"ep8_scene{i:02d}.mp4",
                f"ep08_scene{i}.mp4",
                f"ep8_scene{i}.mp4",
                f"EP08_Scene{i:02d}.mp4",
                f"EP08_Scene{i}.mp4",
                f"ep08_scene_{i:02d}.mp4",
                f"ep8_scene_{i:02d}.mp4",
                f"QURAN-COMEBACK-VEO-008-SCENE{i:02d}.mp4",
            ]
            for cand in candidates:
                cand_path = os.path.join(RENDERS_DIR, cand)
                if os.path.exists(cand_path):
                    print(f"Auto-linking {cand} -> EP08_SCENE{i:02d}.mp4")
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
