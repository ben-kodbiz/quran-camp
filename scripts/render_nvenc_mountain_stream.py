#!/usr/bin/env python3
"""
HUURS STUDIO - Local RTX 3060 NVENC Video Renderer
===================================================
Renders an ultra-optimized 720p cinematic documentary clip of the mountain stream
using FFmpeg hardware acceleration on NVIDIA GeForce RTX 3060 12GB.

Pipeline:
1. Source: High-res documentary photograph of mountain stream (09_IMAGE/QURAN-COMEBACK-STREAM-SOURCE-001.jpg)
2. Motion: Floating-point supersampled 2.5D Ken Burns tracking shot along stream flow
3. Film Grain: Subtle 35mm documentary grain to prevent digital banding
4. Audio: Pristine 48kHz stereo ambient water acoustics
5. Encoder: h264_nvenc with preset P7 (Slowest/Highest Quality), spatial/temporal AQ, CQ 16
"""

import os
import sys
import time
import json
import subprocess

ROOT_DIR = "/mnt/AI/ag/Campaign"
IMAGE_PATH = os.path.join(ROOT_DIR, "09_IMAGE/QURAN-COMEBACK-STREAM-SOURCE-001.jpg")
AUDIO_SRC = os.path.join(ROOT_DIR, "10_VIDEO/renders/QURAN-COMEBACK-VEO-001-SCENE04.mp4")
OUTPUT_DIR = os.path.join(ROOT_DIR, "10_VIDEO/renders")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "QURAN-COMEBACK-FFMPEG-NVENC-001.mp4")

def render():
    if not os.path.exists(IMAGE_PATH):
        print(f"Error: Source image not found at {IMAGE_PATH}")
        sys.exit(1)

    print("=" * 70)
    print("      HUURS STUDIO - LOCAL RTX 3060 NVENC CINEMATIC RENDERER")
    print("=" * 70)
    print(f"Source Image : {IMAGE_PATH}")
    print(f"Output Target: {OUTPUT_FILE}")
    print(f"Resolution   : 1280 × 720 (Strict 720p Hard Ceiling)")
    print(f"Duration     : 10.00 seconds (240 frames @ 24.00 fps)")
    print(f"Hardware Acc : NVIDIA GeForce RTX 3060 12GB (NVENC P7 Preset)")
    print("-" * 70)

    start_time = time.time()

    # Filtergraph:
    # 1. Supersample to 2752x1536 for jitter-free floating-point subpixel motion
    # 2. zoompan: slow push-in (1.0 to 1.11) + gentle downward pan following water flow
    # 3. Downscale with lanczos to 1280x720 with square pixel SAR 1:1
    # 4. Subtle 35mm grain and broadcast fade in/out
    filter_complex = (
        "[0:v]scale=2752:1536:flags=lanczos,"
        "zoompan=z='min(zoom+0.00045,1.11)':x='iw/2-(iw/zoom/2)':y='(ih-ih/zoom)*(on/240)':d=240:s=2752x1536:fps=24,"
        "scale=1280:720:flags=lanczos,setsar=1,"
        "noise=c0s=1.5:allf=t,"
        "fade=t=in:st=0:d=0.75,"
        "fade=t=out:st=9.25:d=0.75,"
        "format=yuv420p[v_out]"
    )

    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-i", IMAGE_PATH,
        "-i", AUDIO_SRC,
        "-filter_complex", filter_complex,
        "-map", "[v_out]",
        "-map", "1:a",
        "-t", "10.0",
        "-c:v", "h264_nvenc",
        "-preset", "p7",
        "-tune", "hq",
        "-rc", "vbr",
        "-cq", "16",
        "-spatial-aq", "1",
        "-temporal-aq", "1",
        "-b:v", "7M",
        "-maxrate", "10M",
        "-bufsize", "14M",
        "-profile:v", "high",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "-movflags", "+faststart",
        OUTPUT_FILE
    ]

    print("Executing FFmpeg render pipeline on RTX 3060...")
    res = subprocess.run(cmd, capture_output=True, text=True)

    if res.returncode != 0:
        print("FFmpeg Render Failed:")
        print(res.stderr[-1000:])
        sys.exit(1)

    elapsed = time.time() - start_time
    file_size_mb = os.path.getsize(OUTPUT_FILE) / (1024 * 1024)

    # ffprobe analysis
    probe_cmd = [
        "ffprobe", "-v", "quiet",
        "-print_format", "json",
        "-show_streams", "-show_format",
        OUTPUT_FILE
    ]
    probe_res = subprocess.run(probe_cmd, capture_output=True, text=True)
    probe_data = json.loads(probe_res.stdout)

    v_stream = next((s for s in probe_data.get("streams", []) if s.get("codec_type") == "video"), {})
    a_stream = next((s for s in probe_data.get("streams", []) if s.get("codec_type") == "audio"), {})

    width = v_stream.get("width")
    height = v_stream.get("height")
    codec = v_stream.get("codec_name")
    fps = eval(v_stream.get("r_frame_rate", "24/1"))
    bitrate_kbps = int(v_stream.get("bit_rate", "0")) / 1000

    print("\n" + "=" * 70)
    print("RENDER SUCCESSFUL!")
    print("=" * 70)
    print(f"File Path    : {OUTPUT_FILE}")
    print(f"Video Codec  : {codec.upper()} (Lavc h264_nvenc P7 High)")
    print(f"Resolution   : {width} × {height} ({'100% 720p COMPLIANT' if width == 1280 and height == 720 else 'NON-COMPLIANT'})")
    print(f"Aspect Ratio : SAR {v_stream.get('sample_aspect_ratio')} | DAR {v_stream.get('display_aspect_ratio')}")
    print(f"Framerate    : {fps:.2f} fps ({v_stream.get('nb_frames')} frames)")
    print(f"Duration     : {float(probe_data['format']['duration']):.2f} s")
    print(f"Video Bitrate: {bitrate_kbps:.1f} kbps")
    print(f"Audio Codec  : {a_stream.get('codec_name', 'none').upper()} ({a_stream.get('sample_rate', '0')} Hz, {a_stream.get('channels')} channels)")
    print(f"File Size    : {file_size_mb:.2f} MB")
    print(f"Render Time  : {elapsed:.2f} seconds ({240/elapsed:.1f} fps rendering speed)")
    print(f"Cost         : $0.00 (Offline RTX 3060 compute)")
    print("=" * 70)

if __name__ == "__main__":
    render()
