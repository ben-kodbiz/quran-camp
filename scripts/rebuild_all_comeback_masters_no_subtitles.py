#!/usr/bin/env python3
"""
HUURS STUDIO - Master Batch Rebuilder (Zero Burned-In Subtitles Mandate)
======================================================================
Sequentially re-assembles all 10 episodes of the "Come Back to the Qur'an" series
(both 16:9 Full Masters and 9:16 Vertical Shorts, plus the Scene 1 Pilot)
with zero burned-in subtitles, preserving pure cinematic nature visuals,
discrete HUURS STUDIO trademark watermark, and -14 LUFS broadcast audio.
"""

import os
import sys
import time
import subprocess
import glob

SCRIPTS_DIR = "/mnt/AI/ag/Campaign/scripts"
RENDERS_DIR = "/mnt/AI/ag/Campaign/10_VIDEO/renders"

TASKS = [
    {"name": "Episode 01 Full Master", "cmd": ["python3", os.path.join(SCRIPTS_DIR, "assemble_ep01_full_master.py")]},
    {"name": "Episode 01 Vertical Short", "cmd": ["python3", os.path.join(SCRIPTS_DIR, "render_ep01_short01a.py")]},
    {"name": "Episode 01 Pilot", "cmd": ["python3", os.path.join(SCRIPTS_DIR, "assemble_scene01_pilot.py")]},
    {"name": "Episode 02 (Master & Short)", "cmd": ["python3", os.path.join(SCRIPTS_DIR, "assemble_ep02_full_master.py")]},
    {"name": "Episode 03 (Master & Short)", "cmd": ["python3", os.path.join(SCRIPTS_DIR, "assemble_ep03_full_master.py")]},
    {"name": "Episode 04 (Master & Short)", "cmd": ["python3", os.path.join(SCRIPTS_DIR, "assemble_ep04_full_master.py")]},
    {"name": "Episode 05 (Master & Short)", "cmd": ["python3", os.path.join(SCRIPTS_DIR, "assemble_ep05_full_master.py")]},
    {"name": "Episode 06 (Master & Short)", "cmd": ["python3", os.path.join(SCRIPTS_DIR, "assemble_ep06_full_master.py")]},
    {"name": "Episode 07 (Master & Short)", "cmd": ["python3", os.path.join(SCRIPTS_DIR, "assemble_ep07_full_master.py")]},
    {"name": "Episode 08 (Master & Short)", "cmd": ["python3", os.path.join(SCRIPTS_DIR, "assemble_ep08_full_master.py")]},
    {"name": "Episode 09 (Master & Short)", "cmd": ["python3", os.path.join(SCRIPTS_DIR, "assemble_ep09_full_master.py")]},
    {"name": "Episode 10 (Master & Short)", "cmd": ["python3", os.path.join(SCRIPTS_DIR, "assemble_ep10_full_master.py")]},
]

def main():
    t_global = time.time()
    print("=" * 75)
    print("HUURS STUDIO — BATCH MASTER REBUILD (ZERO BURNED-IN SUBTITLES)")
    print("=" * 75)
    print(f"Total Assemblies Scheduled: {len(TASKS)}")
    print(f"Target Directory: {RENDERS_DIR}")
    print("-" * 75)

    results = []
    for idx, task in enumerate(TASKS, 1):
        t0 = time.time()
        print(f"\n[{idx}/{len(TASKS)}] Executing: {task['name']}...")
        sys.stdout.flush()
        res = subprocess.run(task["cmd"], capture_output=True, text=True)
        dur = time.time() - t0
        if res.returncode != 0:
            print(f"  FAILED in {dur:.2f}s!")
            print("  Error excerpt:\n", res.stderr[-800:])
            results.append({"name": task["name"], "status": "FAILED", "duration": dur})
            sys.exit(1)
        else:
            print(f"  ✓ SUCCESS in {dur:.2f}s")
            results.append({"name": task["name"], "status": "SUCCESS", "duration": dur})

    print("\n" + "=" * 75)
    print("BATCH REBUILD COMPLETE!")
    print(f"Total Elapsed Time: {time.time() - t_global:.2f}s")
    print("=" * 75)
    for r in results:
        print(f"  [{r['status']}] {r['name']:<35} ({r['duration']:.2f}s)")

if __name__ == "__main__":
    main()
