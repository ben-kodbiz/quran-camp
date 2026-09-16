#!/usr/bin/env python3
"""
HUURS STUDIO - F5-TTS Voiceover Generator & Pipeline Integration
================================================================
Generates high-fidelity, contemplative voiceover narration for any episode
using open-source zero-shot voice cloning (F5-TTS) accelerated by NVIDIA RTX 3060.

Features:
- Zero-cost, 100% local GPU inference
- Clones timbre, warmth, and cadence from Huurs reference narrator
- Markdown script parser (extracts dialogue, strips visual/math cues)
- Contemplative pacing engine (inserts natural breath & silence pauses)
- EBU R128 mastering to -14 LUFS broadcast standard (Zero Music Policy)

Usage:
    python3 scripts/generate_voiceover_f5.py --episode 3
    python3 scripts/generate_voiceover_f5.py --script 08_SCRIPTS/QURAN-COMEBACK-SCRIPT-003.md --output 11_AUDIO/EP03_audio.mp3
"""

import os
import re
import sys
import time
import json
import argparse
import subprocess
import numpy as np
import soundfile as sf

ROOT_DIR = "/mnt/AI/ag/Campaign"
DEFAULT_REF_AUDIO = os.path.join(ROOT_DIR, "11_AUDIO/reference_voices/huurs_narrator_ep02.wav")
DEFAULT_REF_TEXT = "If you ask ten people on the street what the Qur'an is, you'll get ten different answers."

def parse_script(script_path):
    """Parses a Huurs markdown script and extracts spoken dialogue paragraphs across all sections."""
    with open(script_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find PRODUCTION SCRIPT & DIALOGUE section
    match = re.search(r"## PRODUCTION SCRIPT & DIALOGUE(.*?)(?=\n## |\Z)", content, re.DOTALL)
    text = match.group(1) if match else content

    # Find sections
    sections_raw = re.split(r"### \d\d:\d\d", text)
    sections = []

    for s_raw in sections_raw:
        if not s_raw.strip():
            continue
        # Extract vo lines
        vo_match = re.search(r"\*\*\(VOICEOVER\):\*\*(.*?)(?=\*\*\[|\n###|\Z)", s_raw, re.DOTALL)
        if not vo_match:
            continue
        
        vo_text = vo_match.group(1).strip()
        
        # Remove Arabic honorifics / non-latin glyphs
        vo_text = vo_text.replace("ﷺ", "peace be upon him")
        vo_text = vo_text.replace("˹O Prophet˺", "")
        vo_text = vo_text.replace("˹", "").replace("˺", "")
        # Remove markdown bold/italics
        vo_text = re.sub(r"\*\*(.*?)\*\*", r"\1", vo_text)
        vo_text = re.sub(r"\*(.*?)\*", r"\1", vo_text)
        # Normalize quotes
        vo_text = vo_text.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
        # Remove Arabic script characters (kept in visual on-screen graphics)
        vo_text = re.sub(r"[\u0600-\u06FF]", "", vo_text)
        
        # Split into non-empty paragraphs
        paras = [p.strip().strip('"') for p in vo_text.split("\n\n") if p.strip()]
        cleaned_paras = []
        for p in paras:
            p = " ".join(p.split())
            # Skip visual, stage cues, math, or markdown lines
            if p.startswith("[") or p.startswith("*") or set(p) <= {"-", " "} or "$$" in p or "\\text" in p:
                continue
            if p:
                cleaned_paras.append(p)
        
        if cleaned_paras:
            sections.append(cleaned_paras)

    return sections

def generate_voiceover(script_path, output_mp3, ref_audio, ref_text, speed=0.88):
    """Executes F5-TTS inference and masters final audio."""
    print("=" * 70)
    print("      HUURS STUDIO - F5-TTS VOICEOVER GENERATION PIPELINE")
    print("=" * 70)
    print(f"Script:    {script_path}")
    print(f"Reference: {ref_audio}")
    print(f"Output:    {output_mp3}")
    print(f"Pacing:    speed={speed} (contemplative slow-burn)")
    print("-" * 70)

    sections = parse_script(script_path)
    total_paras = sum(len(s) for s in sections)
    print(f"Parsed {len(sections)} sections, total {total_paras} spoken contemplation units.")

    # Lazy-import F5TTS
    from f5_tts.api import F5TTS
    f5 = F5TTS(model="F5TTS_v1_Base")

    sample_rate = 24000
    assembled_samples = []

    # Contemplative pause profiles (in seconds)
    section_pause = np.zeros(int(1.8 * sample_rate), dtype=np.float32)
    paragraph_pause = np.zeros(int(1.1 * sample_rate), dtype=np.float32)

    temp_wav_dir = "/tmp/huurs_f5_chunks"
    os.makedirs(temp_wav_dir, exist_ok=True)

    chunk_idx = 0
    t_start = time.time()

    for sec_idx, paras in enumerate(sections):
        print(f"\n--- [Section {sec_idx + 1}/{len(sections)}] ---")
        for p_idx, text in enumerate(paras):
            chunk_idx += 1
            print(f"  ({chunk_idx}/{total_paras}) \"{text[:65]}...\"")
            chunk_file = os.path.join(temp_wav_dir, f"chunk_{chunk_idx:03d}.wav")
            
            t0 = time.time()
            f5.infer(
                ref_file=ref_audio,
                ref_text=ref_text,
                gen_text=text,
                speed=speed,
                file_wave=chunk_file
            )
            dur = time.time() - t0
            
            data, sr = sf.read(chunk_file)
            assembled_samples.append(data.astype(np.float32))
            assembled_samples.append(paragraph_pause)
            print(f"       -> Generated {len(data)/sr:.1f}s audio in {dur:.2f}s")
            
        assembled_samples.append(section_pause)
        sec_samples_total = sum(len(s) for s in assembled_samples)
        # Calculate duration of this section
        prev_samples = sum(len(s) for s in assembled_samples[:-len(paras)*2 - 1]) if sec_idx > 0 else 0
        current_sec_dur = (sec_samples_total - prev_samples) / sample_rate
        print(f"       >>> Section {sec_idx + 1} Duration: {current_sec_dur:.2f}s")

    raw_audio = np.concatenate(assembled_samples)
    raw_wav = os.path.join(temp_wav_dir, "raw_assembled.wav")
    sf.write(raw_wav, raw_audio, sample_rate)
    raw_dur = len(raw_audio) / sample_rate
    print(f"\nTotal raw narration duration: {raw_dur:.2f}s (generated in {time.time() - t_start:.1f}s)")

    # Audio Mastering: Highpass filter @ 60Hz + Loudnorm to -14 LUFS (Zero Music Policy)
    print("\nMastering audio to Huurs Studio Broadcast Standard (-14 LUFS, 48kHz)...")
    os.makedirs(os.path.dirname(output_mp3), exist_ok=True)
    
    cmd = [
        "ffmpeg", "-y", "-i", raw_wav,
        "-af", "highpass=f=60,loudnorm=I=-14:TP=-1.0:LRA=7",
        "-c:a", "libmp3lame", "-b:a", "192k", "-ar", "48000",
        output_mp3
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("FFmpeg mastering failed:", res.stderr[-500:])
        sys.exit(1)

    # Save section timings JSON
    timing_json = os.path.splitext(output_mp3)[0] + "_timings.json"
    timings_data = {
        "output_mp3": output_mp3,
        "total_duration": raw_dur,
        "sections": []
    }
    sample_pos = 0
    for sec_idx, paras in enumerate(sections):
        sec_chunk_count = len(paras) * 2 + 1
        sec_sample_count = sum(len(assembled_samples[sample_pos + i]) for i in range(sec_chunk_count))
        sec_dur = sec_sample_count / sample_rate
        timings_data["sections"].append({
            "section_index": sec_idx + 1,
            "duration": round(sec_dur, 2)
        })
        sample_pos += sec_chunk_count

    with open(timing_json, "w") as f:
        json.dump(timings_data, f, indent=2)
    print(f"✓ Section timings saved to: {timing_json}")

    print(f"✓ Master voiceover delivered successfully: {output_mp3}")
    print("=" * 70)

def main():
    parser = argparse.ArgumentParser(description="Huurs Studio F5-TTS Voiceover Generator")
    parser.add_argument("--episode", type=int, help="Episode number (e.g. 3)")
    parser.add_argument("--script", type=str, help="Path to markdown script")
    parser.add_argument("--output", type=str, help="Path to target output mp3")
    parser.add_argument("--ref-audio", type=str, default=DEFAULT_REF_AUDIO, help="Reference audio for voice cloning")
    parser.add_argument("--ref-text", type=str, default=DEFAULT_REF_TEXT, help="Reference transcript")
    parser.add_argument("--speed", type=float, default=0.88, help="Pacing speed (default 0.88 for contemplation)")
    args = parser.parse_args()

    if args.episode:
        ep_str = f"{args.episode:03d}"
        script_path = os.path.join(ROOT_DIR, f"08_SCRIPTS/QURAN-COMEBACK-SCRIPT-{ep_str}.md")
        output_mp3 = os.path.join(ROOT_DIR, f"11_AUDIO/EP{args.episode:02d}_audio.mp3")
    elif args.script and args.output:
        script_path = args.script
        output_mp3 = args.output
    else:
        parser.print_help()
        sys.exit(1)

    if not os.path.exists(script_path):
        print(f"Error: Script not found: {script_path}")
        sys.exit(1)

    generate_voiceover(script_path, output_mp3, args.ref_audio, args.ref_text, args.speed)

if __name__ == "__main__":
    main()
