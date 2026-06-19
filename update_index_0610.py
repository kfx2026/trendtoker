#!/usr/bin/env python3
"""Update index.json for all 3 regions and run build_static.py"""
import json, os, subprocess, sys

BASE = r"D:\网站源码\趋势播报站"
DATE = "2026-06-10"

for region in ["china", "us", "eu"]:
    index_path = os.path.join(BASE, "data", region, "index.json")
    idx = {}
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            idx = json.load(f)

    if DATE not in idx.get("dates", []):
        day_file = os.path.join(BASE, "data", region, f"{DATE}.json")
        with open(day_file, "r", encoding="utf-8") as f:
            articles = json.load(f)

        idx.setdefault("dates", []).append(DATE)
        idx["dates"].sort()
        idx["total_articles"] = idx.get("total_articles", 0) + len(articles)
        idx["last_updated"] = DATE

        with open(index_path, "w", encoding="utf-8") as f:
            json.dump(idx, f, ensure_ascii=False, indent=2)
        print(f"  ✓ Updated {region}/index.json ({len(idx['dates'])} days, {idx['total_articles']} articles)")
    else:
        print(f"  ⚠ {DATE} already in {region}/index.json")

# Run build_static.py
print("\nRebuilding static HTML...")
result = subprocess.run([sys.executable, os.path.join(BASE, "build_static.py")],
                       capture_output=True, text=True, cwd=BASE)
print(result.stdout)
if result.stderr:
    print("STDERR:", result.stderr)
if result.returncode != 0:
    print(f"build_static.py returned {result.returncode}")
    sys.exit(1)

print("\n✓ Done!")
