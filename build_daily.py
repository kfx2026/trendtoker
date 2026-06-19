#!/usr/bin/env python3
"""
TrendToker Daily Builder — 增量追加模式
用法: python build_daily.py <region> <date> <data_json_or_path>
只会: 1) 写入新的day JSON  2) 追加index  3) 重建region HTML
不会: 修改任何旧文件
"""

import json, os, sys, subprocess

BASE = r"D:\网站源码\趋势播报站"

def add_day(region, date, articles):
    """Add a new day of articles. Returns True on success."""
    if len(articles) != 5:
        print(f"  ⚠ Expected 5 articles, got {len(articles)}")
        return False

    region_dir = os.path.join(BASE, "data", region)
    os.makedirs(region_dir, exist_ok=True)

    # 1. Write immutable day file
    day_file = os.path.join(region_dir, f"{date}.json")
    if os.path.exists(day_file):
        print(f"  ⚠ {date}.json already exists — will NOT overwrite")
        return False

    with open(day_file, "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)
    print(f"  ✓ Created {region}/{date}.json ({len(articles)} articles)")

    # 2. Update index.json
    index_path = os.path.join(region_dir, "index.json")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            idx = json.load(f)
    else:
        idx = {"region": region, "dates": [], "total_articles": 0}

    if date not in idx["dates"]:
        idx["dates"].append(date)
        idx["dates"].sort()
        idx["total_articles"] += len(articles)
        idx["last_updated"] = date
        with open(index_path, "w", encoding="utf-8") as f:
            json.dump(idx, f, ensure_ascii=False, indent=2)
        print(f"  ✓ Updated index.json ({len(idx['dates'])} days, {idx['total_articles']} articles)")
    else:
        print(f"  ⚠ Date {date} already in index")

    # 3. Rebuild region page
    print(f"  Rebuilding {region}.html...")
    result = subprocess.run(
        [sys.executable, os.path.join(BASE, "build_static.py")],
        capture_output=True, text=True, cwd=BASE
    )
    print(result.stdout.strip())
    if result.returncode != 0:
        print(result.stderr)
        return False

    return True


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python build_daily.py <region> <date> [articles_json_file]")
        print("Example: python build_daily.py china 2026-06-04 today_china.json")
        sys.exit(1)

    region = sys.argv[1]
    date = sys.argv[2]

    if region not in ["china", "us", "eu"]:
        print(f"Unknown region: {region}")
        sys.exit(1)

    # Load articles from file path or stdin
    if len(sys.argv) >= 4:
        with open(sys.argv[3], "r", encoding="utf-8") as f:
            articles = json.load(f)
    else:
        articles = json.load(sys.stdin)

    if add_day(region, date, articles):
        print(f"\n✓ {region} {date} added successfully")
    else:
        print(f"\n✗ Failed to add {region} {date}")
