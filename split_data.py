#!/usr/bin/env python3
"""Split existing china.json/us.json/eu.json into per-day files.
Each day = 5 articles, each file = immutable forever.
Also creates index.json for each region."""

import json, os
from collections import defaultdict

BASE = r"D:\网站源码\趋势播报站\data"

for region in ["china", "us", "eu"]:
    src = os.path.join(BASE, f"{region}.json")
    with open(src, "r", encoding="utf-8") as f:
        articles = json.load(f)
    
    # Group by date
    by_date = defaultdict(list)
    for a in articles:
        date = a["date"]
        by_date[date].append(a)
    
    # Create region directory
    region_dir = os.path.join(BASE, region)
    os.makedirs(region_dir, exist_ok=True)
    
    # Write per-day files
    dates = sorted(by_date.keys())
    for date in dates:
        day_file = os.path.join(region_dir, f"{date}.json")
        day_articles = by_date[date]
        with open(day_file, "w", encoding="utf-8") as f:
            json.dump(day_articles, f, ensure_ascii=False, indent=2)
        print(f"  {region}/{date}.json: {len(day_articles)} articles")
    
    # Write index.json
    index = {
        "region": region,
        "dates": dates,
        "total_articles": len(articles),
        "last_updated": dates[-1]
    }
    with open(os.path.join(region_dir, "index.json"), "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
    
    print(f"[{region}] {len(dates)} days, {len(articles)} articles total → data/{region}/")

# Keep old files as backup
for f in ["china.json", "us.json", "eu.json"]:
    src = os.path.join(BASE, f)
    bak = os.path.join(BASE, f + ".bak")
    if os.path.exists(src):
        os.rename(src, bak)
        print(f"Backed up {f} → {f}.bak")

print("\nDone! New structure:")
for region in ["china", "us", "eu"]:
    d = os.path.join(BASE, region)
    files = sorted([f for f in os.listdir(d) if f.endswith('.json')])
    print(f"  data/{region}/: {files}")
