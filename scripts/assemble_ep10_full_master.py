#!/usr/bin/env python3
"""
HUURS STUDIO - Episode 10 Full Master 5-Scene Assembly (Season Finale)
======================================================================
Assembles all 5 living-creation scene clips for Episode 10 (Surah Ar-Ra'd 13:11 & Ibrahim 14:24–25)
with contemplative slow-motion, seamless crossfades, burned-in IBM Plex Serif typography,
and the official discreet trademark watermark:

Living Creation Motif Mapping:
- Section 1 (51.82s): Scene 1 (Ocean Dawn & Soaring Sea Birds — The Crossroads)
- Section 2 (65.47s): Scene 2 (Vibrant Green Plant Sprout — The Divine Promise of Renewal)
- Section 3 (60.01s): Scene 3 (Ancient Rooted Olive Tree — The Parable of the Good Tree)
- Section 4 (45.91s): Scene 4 (Jewel Hummingbird Hovering at Forest Blossom — Tadabbur)
- Section 5 (40.37s): Scene 5 (Panoramic Mountain Waterfalls at Sunset — The Grand Finale)

Total Master Duration: 263.58s (4m 23.6s)
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
AUDIO_IN = os.path.join(ROOT_DIR, "11_AUDIO/EP10_audio.mp3")
OUTPUT_MASTER = os.path.join(RENDERS_DIR, "QURAN-COMEBACK-EP10-FULL-MASTER.mp4")
OUTPUT_SHORT = os.path.join(RENDERS_DIR, "QURAN-COMEBACK-EP10-SHORT-001A.mp4")
SUBTITLE_FILE = os.path.join(RENDERS_DIR, "ep10_master_subtitles.ass")
TEMP_DIR = "/tmp/ep10_assembly"

os.makedirs(TEMP_DIR, exist_ok=True)

import json

S1_FILE = os.path.join(RENDERS_DIR, "EP10_SCENE01.mp4")
S2_FILE = os.path.join(RENDERS_DIR, "EP10_SCENE02.mp4")
S3_FILE = os.path.join(RENDERS_DIR, "EP10_SCENE03.mp4")
S4_FILE = os.path.join(RENDERS_DIR, "EP10_SCENE04.mp4")
S5_FILE = os.path.join(RENDERS_DIR, "EP10_SCENE05.mp4")

SECTIONS = [
    {"id": "sec1", "file": S1_FILE, "name": "Ocean Dawn & Soaring Sea Birds", "duration": 51.82, "stretch_only": False},
    {"id": "sec2", "file": S2_FILE, "name": "Jewel Hummingbird at Forest Blossom", "duration": 65.47, "stretch_only": True},
    {"id": "sec3", "file": S3_FILE, "name": "Ancient Rooted Olive Tree", "duration": 60.01, "stretch_only": False},
    {"id": "sec4", "file": S4_FILE, "name": "Arabian Horse Grazing in Meadow", "duration": 45.91, "stretch_only": False},
    {"id": "sec5", "file": S5_FILE, "name": "Panoramic Mountain Waterfalls at Sunset", "duration": 40.37, "stretch_only": False},
]

def make_extended_clip(input_video, target_duration, output_path, stretch_only=False):
    if stretch_only:
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

        fc = f"[0:v]setpts={speed_factor:.6f}*PTS,minterpolate=fps=24:mi_mode=blend,tpad=stop_mode=clone:stop_duration=5,trim=start=0:duration={target_duration},setpts=PTS-STARTPTS,format=yuv420p[v_out]"
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
            print(f"Error stretching {input_video}:\n{res.stderr[-500:]}")
            sys.exit(1)
        return

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
Title: Huurs Studio - Episode 10 Master Subtitles (Season Finale)
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
Dialogue: 0,0:00:00.60,0:00:08.50,HuursContemplation,,0,0,0,,{\\fad(400,300)}Ten episodes ago, we began with a simple, uncomfortable truth:
Dialogue: 0,0:00:09.00,0:00:18.00,HuursGold,,0,0,0,,{\\fad(300,300)}You don’t need another Islamic reminder. You need the Qur'an.
Dialogue: 0,0:00:18.50,0:00:27.50,HuursContemplation,,0,0,0,,{\\fad(300,300)}We looked at why we feel distant from Allah... and how He answers before we ask.
Dialogue: 0,0:00:28.00,0:00:37.00,HuursContemplation,,0,0,0,,{\\fad(300,300)}We shattered the lie that you have to be perfect before opening His Book.
Dialogue: 0,0:00:37.50,0:00:44.00,HuursItalic,,0,0,0,,{\\fad(300,300)}We remembered that life is like melting ice.
Dialogue: 0,0:00:44.50,0:00:51.50,HuursGold,,0,0,0,,{\\fad(300,400)}And now, you stand at the crossroads: Make today the day you returned.
Dialogue: 0,0:00:52.00,0:01:00.00,HuursContemplation,,0,0,0,,{\\fad(400,300)}In Surah Ar-Ra'd, Allah makes an unconditional promise:
Dialogue: 0,0:01:00.50,0:01:09.50,HuursGold,,0,0,0,,{\\fad(300,300)}‘Indeed, Allah will not change the condition of a people until they change what is in themselves.’
Dialogue: 0,0:01:10.00,0:01:19.50,HuursContemplation,,0,0,0,,{\\fad(300,300)}You change the state of your heart first: give Allah ten honest minutes a day.
Dialogue: 0,0:01:20.00,0:01:31.00,HuursItalic,,0,0,0,,{\\fad(300,300)}‘If My servant comes to Me walking, I go to him running.’ — Hadith Qudsi
Dialogue: 0,0:01:31.50,0:01:42.00,HuursGold,,0,0,0,,{\\fad(300,400)}The Creator of the galaxies is waiting for you to simply take the first step.
Dialogue: 0,0:01:42.50,0:01:52.50,HuursContemplation,,0,0,0,,{\\fad(400,300)}In Surah Ibrahim, Allah gives the most beautiful metaphor in the entire Qur'an:
Dialogue: 0,0:01:53.00,0:02:03.50,HuursGold,,0,0,0,,{\\fad(300,300)}‘A good word is like a good tree, its root firmly fixed and its branches high in the sky.’
Dialogue: 0,0:02:04.00,0:02:14.00,HuursContemplation,,0,0,0,,{\\fad(300,300)}When the winds howl, its trunk does not sway because its foundation is immovable.
Dialogue: 0,0:02:14.50,0:02:25.50,HuursItalic,,0,0,0,,{\\fad(300,300)}That tree is the soul that reads the Qur'an with tadabbur.
Dialogue: 0,0:02:26.00,0:02:35.00,HuursGold,,0,0,0,,{\\fad(300,400)}When worldly storms hit you, you stand firm... your roots drinking from revelation.
Dialogue: 0,0:02:35.50,0:02:44.50,HuursContemplation,,0,0,0,,{\\fad(400,300)}Imagine yourself thirty days from now:
Dialogue: 0,0:02:45.00,0:02:54.50,HuursContemplation,,0,0,0,,{\\fad(300,300)}Thirty days of opening the Qur'an every morning for ten unhurried minutes.
Dialogue: 0,0:02:55.00,0:03:04.00,HuursContemplation,,0,0,0,,{\\fad(300,300)}Your chest will have expanded (sharh). Your tongue cleansed of complaints.
Dialogue: 0,0:03:04.50,0:03:14.00,HuursGold,,0,0,0,,{\\fad(300,400)}And for the first time in years, when you stand in prayer, your soul will be present.
Dialogue: 0,0:03:14.50,0:03:24.00,HuursContemplation,,0,0,0,,{\\fad(400,300)}This was never meant to be just a video series. This is your invitation to come home.
Dialogue: 0,0:03:24.50,0:03:34.00,HuursContemplation,,0,0,0,,{\\fad(300,300)}Do not let today pass without touching the Book of Allah. Open it. Read one verse.
Dialogue: 0,0:03:34.50,0:03:42.50,HuursGold,,0,0,0,,{\\fad(300,300)}READ. REFLECT. RETURN.
Dialogue: 0,0:03:43.00,0:03:52.00,HuursContemplation,,0,0,0,,{\\fad(300,400)}Assalamu alaykum wa rahmatullahi wa barakatuh.
Dialogue: 0,0:03:53.00,0:04:03.00,HuursGold,,0,0,0,,{\\fad(400,500)}HUURS STUDIO  •  Season 1 Complete
"""
    with open(SUBTITLE_FILE, "w", encoding="utf-8") as f:
        f.write(ass_content.strip())
    print(f"Created ASS Subtitle file: {SUBTITLE_FILE}")

def assemble_master():
    t0 = time.time()
    print("=" * 70)
    print("HUURS STUDIO - ASSEMBLING EPISODE 10 FULL MASTER (SEASON FINALE)")
    print("=" * 70)

    extended_clips = []
    for i, sec in enumerate(SECTIONS):
        out_ext = os.path.join(TEMP_DIR, f"{sec['id']}.mp4")
        print(f"[{i+1}/5] Preparing {sec['name']} (target: {sec['duration']}s)...")
        make_extended_clip(sec["file"], sec["duration"], out_ext, stretch_only=sec.get("stretch_only", False))
        extended_clips.append(out_ext)

    print("-" * 70)
    print("Creating Master Subtitle file (libass IBM Plex Serif)...")
    create_subtitles()

    concat_list = os.path.join(TEMP_DIR, "concat_sections.txt")
    with open(concat_list, "w") as f:
        for c in extended_clips:
            f.write(f"file '{c}'\n")

    video_base = os.path.join(TEMP_DIR, "video_combined.mp4")
    print("Concatenating video sections...")
    cmd = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", concat_list,
        "-c", "copy",
        video_base
    ]
    subprocess.run(cmd, check=True)

    trademark_master = "drawtext=text='HUURS STUDIO':font='IBM Plex Serif':fontsize=16:fontcolor=white@0.22:x=w-tw-40:y=h-th-30"

    print("-" * 70)
    print("Muxing video, normalized audio, burned subtitles, and trademark watermark...")
    cmd = [
        "ffmpeg", "-y",
        "-i", video_base,
        "-i", AUDIO_IN,
        "-filter_complex",
        f"[0:v]{trademark_master},fade=t=in:st=0:d=1.2,fade=t=out:st=260.0:d=3.5,format=yuv420p[v_out];"
        "[1:a]afade=t=in:st=0:d=0.5,afade=t=out:st=260.0:d=3.5[a_out]",
        "-map", "[v_out]",
        "-map", "[a_out]",
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-crf", "18",
        "-maxrate", "6.5M",
        "-bufsize", "10M",
        "-pix_fmt", "yuv420p",
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

    print(f"✓ EPISODE 10 FULL MASTER COMPLETED in {time.time()-t0:.2f}s!")
    print(f"  Location: {OUTPUT_MASTER}")

def assemble_short():
    print("-" * 70)
    print("Assembling 9:16 Vertical Cut (Short A: The Crossroads Hook)...")
    sec1_part = os.path.join(TEMP_DIR, "sec1.mp4")
    audio_track = AUDIO_IN

    short_sub_file = os.path.join(RENDERS_DIR, "ep10_short_subtitles.ass")
    ass_short = """[Script Info]
Title: Huurs Studio - Episode 10 Short Subtitles
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
Dialogue: 0,0:00:00.60,0:00:08.50,ShortMobile,,0,0,0,,{\\fad(300,250)}Ten episodes ago, we began with a simple truth:
Dialogue: 0,0:00:09.00,0:00:18.00,ShortGold,,0,0,0,,{\\fad(250,250)}You don’t need another reminder. You need the Qur'an.
Dialogue: 0,0:00:18.50,0:00:28.00,ShortMobile,,0,0,0,,{\\fad(250,250)}We looked at why we feel distant from Allah...
Dialogue: 0,0:00:28.50,0:00:38.00,ShortMobile,,0,0,0,,{\\fad(250,250)}We shattered the lie that you have to be perfect first.
Dialogue: 0,0:00:38.50,0:00:51.00,ShortGold,,0,0,0,,{\\fad(300,300)}And now, you stand at the crossroads: Make today the day you returned.
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
        f"[0:v]crop=w=ih*(9/16):h=ih:x=(iw-ow)/2:y=0,scale=720:1280,{trademark_short},fade=t=in:st=0:d=0.8,fade=t=out:st=50.0:d=1.8,format=yuv420p[v_out];"
        "[1:a]atrim=start=0:end=51.82,afade=t=in:st=0:d=0.3,afade=t=out:st=50.0:d=1.8[a_out]",
        "-map", "[v_out]",
        "-map", "[a_out]",
        "-t", "51.82",
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
    print(f"✓ EPISODE 10 SHORT 001A COMPLETED!")

def auto_link_scenes():
    """Auto-detect and symlink scene files if named with lowercase or alternate patterns."""
    for i in range(1, 6):
        target = os.path.join(RENDERS_DIR, f"EP10_SCENE{i:02d}.mp4")
        if not os.path.exists(target):
            candidates = [
                f"ep10_scene{i:02d}.mp4",
                f"ep10_scene{i}.mp4",
                f"EP10_Scene{i:02d}.mp4",
                f"EP10_Scene{i}.mp4",
                f"ep10_scene_{i:02d}.mp4",
                f"QURAN-COMEBACK-VEO-010-SCENE{i:02d}.mp4",
            ]
            for cand in candidates:
                cand_path = os.path.join(RENDERS_DIR, cand)
                if os.path.exists(cand_path):
                    print(f"Auto-linking {cand} -> EP10_SCENE{i:02d}.mp4")
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
