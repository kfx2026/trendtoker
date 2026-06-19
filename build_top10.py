#!/usr/bin/env python3
"""Build weekly Top 10 trends page from aggregated data.
Reads us.json, eu.json, china.json → ranks by growth score → generates top10.html
"""
import json
import os
import re
import math
from datetime import datetime, timedelta

BASE = os.path.dirname(os.path.abspath(__file__))
NOW = datetime.now()
CUTOFF = NOW - timedelta(days=7)

REGIONS = {
    "us": {"name_zh": "美国", "name_en": "US", "flag": "🇺🇸"},
    "eu": {"name_zh": "欧洲", "name_en": "EU", "flag": "🇪🇺"},
    "china": {"name_zh": "中国", "name_en": "China", "flag": "🇨🇳"},
}

def parse_heat(heat_str):
    """Parse heat string to a numeric score for ranking.
    Examples: '18.2M views' → 18.2e6, '250K+ videos' → 250e3, 'Sustained growth format' → 10000
    """
    if not heat_str:
        return 0
    s = heat_str.lower().replace(",", "").replace("views", "").replace("videos", "").strip()
    m = re.search(r'([\d.]+)\s*m', s)
    if m:
        return float(m.group(1)) * 1_000_000
    m = re.search(r'([\d.]+)\s*k', s)
    if m:
        return float(m.group(1)) * 1_000
    m = re.search(r'([\d.]+)', s)
    if m:
        return float(m.group(1))
    # Text-based heat (e.g. "Sustained growth format")
    return 10000

def parse_growth(growth_str):
    """Parse growth string to numeric percentage.
    Examples: '+560% week-over-week' → 560, '+120% adoption' → 120
    """
    if not growth_str:
        return 0
    m = re.search(r'[\+\-]?(\d+)%', growth_str)
    if m:
        return int(m.group(1))
    return 0

def get_score(article, region):
    """Composite score: log(heat) * growth * recency bonus"""
    heat = parse_heat(article.get("stats", {}).get("heat", ""))
    growth = parse_growth(article.get("stats", {}).get("growth", ""))
    # Recency: articles from today get 2x, yesterday 1.5x, etc.
    try:
        date = datetime.strptime(article.get("date", ""), "%Y-%m-%d")
        days_ago = (NOW - date).days
        recency = max(1.0, 3.0 - days_ago * 0.3)
    except:
        recency = 1.0
    # Score
    if heat <= 0:
        heat = 10000
    score = math.log10(heat) * max(growth, 1) * recency
    return score

def main():
    all_articles = []
    for region_key, region_info in REGIONS.items():
        fpath = os.path.join(BASE, "data", f"{region_key}.json")
        if not os.path.exists(fpath):
            continue
        with open(fpath, "r", encoding="utf-8") as f:
            articles = json.load(f)
        for art in articles:
            try:
                date = datetime.strptime(art.get("date", ""), "%Y-%m-%d")
                if date < CUTOFF:
                    continue
            except:
                continue
            art["_region"] = region_key
            art["_region_info"] = region_info
            art["_score"] = get_score(art, region_key)
            all_articles.append(art)

    # Sort by score descending, take top 10
    all_articles.sort(key=lambda x: x["_score"], reverse=True)
    top10 = all_articles[:10]

    # Generate top10.html
    html = generate_html(top10)
    outpath = os.path.join(BASE, "top10.html")
    with open(outpath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated {outpath} with {len(top10)} articles")

    # Also save top10.json for potential reuse
    json_out = []
    for a in top10:
        json_out.append({
            "id": a["id"],
            "date": a["date"],
            "title_zh": a["title_zh"],
            "title_en": a["title_en"],
            "summary_zh": a["summary_zh"],
            "summary_en": a["summary_en"],
            "stats": a["stats"],
            "phase": a["phase"],
            "phase_zh": a["phase_zh"],
            "cpm": a["cpm"],
            "region": a["_region"],
            "score": round(a["_score"], 1),
        })
    json_path = os.path.join(BASE, "data", "top10.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(json_out, f, ensure_ascii=False, indent=2)
    print(f"Saved top10.json with {len(json_out)} entries")

def generate_html(articles):
    items_json = []
    for i, a in enumerate(articles):
        items_json.append({
            "@type": "ListItem",
            "position": i + 1,
            "item": {
                "@type": "Article",
                "name": a["title_en"],
                "url": f"https://globalshortvideotrend.top/article.html?id={a['id']}",
                "description": a.get("summary_en", ""),
            }
        })

    schema = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "Weekly Top 10 Short Video Trends",
        "description": "Ranked top 10 trending short video topics across US, EU, and China this week.",
        "numberOfItems": len(articles),
        "itemListElement": items_json,
    }

    # Build rank cards HTML
    cards_html = []
    medals = ["🥇", "🥈", "🥉"] + [str(i) for i in range(4, 11)]
    for i, a in enumerate(articles):
        region = a["_region_info"]
        medal = medals[i]
        score = round(a["_score"], 1)
        heat = a.get("stats", {}).get("heat", "")
        growth = a.get("stats", {}).get("growth", "")
        phase_zh = a.get("phase_zh", "")
        cpm = a.get("cpm", "")
        article_url = f"article.html?id={a['id']}"

        cards_html.append(f'''        <div class="top10-card rank-{i+1}">
          <div class="top10-rank">{medal}</div>
          <div class="top10-body">
            <div class="top10-meta">
              <span class="top10-region">{region['flag']} {region['name_en']}</span>
              <span class="top10-phase ph-{a.get('phase','')}">{phase_zh}</span>
              <span class="top10-date">{a['date']}</span>
            </div>
            <h3 class="top10-title-zh">{a['title_zh']}</h3>
            <h4 class="top10-title-en">{a['title_en']}</h4>
            <p class="top10-summary">{a.get('summary_zh', '')}</p>
            <div class="top10-stats">
              <span class="stat-heat">🔥 {heat}</span>
              <span class="stat-growth">📈 {growth}</span>
              <span class="stat-cpm">💰 CPM {cpm}</span>
              <span class="stat-score">⭐ 得分 {score}</span>
            </div>
            <a href="{article_url}" class="top10-readmore">📖 深度分析 →</a>
          </div>
        </div>''')

    cards_block = "\n".join(cards_html)

    html = f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Weekly Top 10 Trends | 全球短视频热点排行榜</title>
<meta name="description" content="Top 10 trending short video topics this week across US, EU, and China. Data-driven rankings with heat, growth, CPM, and lifecycle analysis.">
<meta name="robots" content="index, follow"><meta name="baidu-site-verification" content="codeva-OcnBgecQNl">
<link rel="canonical" href="https://globalshortvideotrend.top/top10">
<link rel="stylesheet" href="css/style.css">
<script>(function(){{var bp=document.createElement('script');bp.src='https://zz.bdstatic.com/linksubmit/push.js';var s=document.getElementsByTagName('script')[0];s.parentNode.insertBefore(bp,s);}})();</script>
<script type="application/ld+json">
{json.dumps(schema, ensure_ascii=False)}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "Weekly Top 10 Trends | TrendToker",
  "url": "https://globalshortvideotrend.top/top10",
  "description": "Top 10 trending short video topics this week across US, EU, and China. Data-driven rankings with heat, growth, CPM, and lifecycle analysis."
}}
</script>
</head><body>
<nav class="navbar"><div class="nav-inner">
<a href="index.html" class="nav-logo">Trend<span>Toker</span></a>
<div class="nav-links"><a href="china.html">China</a><a href="us.html">US</a><a href="eu.html">EU</a><a href="top10.html" class="nav-active">🏆 Top10</a><a href="about.html">About</a></div>
<div class="nav-right"><div class="nav-util"><button onclick="history.back()" title="Back">‹</button><button onclick="location.reload()" title="Refresh">↻</button></div><button class="lang-btn" id="langBtn" onclick="swL()">中文</button><div class="hamburger" onclick="toggleMenu()"><span></span><span></span><span></span></div></div>
</div></nav>
<main class="main">
<div class="container">
  <div class="hero fade-in" style="background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);padding:40px 30px;border-radius:16px;margin-bottom:32px;color:#fff">
    <div class="badge" style="background:rgba(255,255,255,0.2);color:#fff">WEEKLY RANKING</div>
    <h1>🏆 本周 Top 10 趋势排行榜</h1>
    <p>Top 10 Trending Short Video Topics This Week</p>
    <p style="opacity:0.85;font-size:14px">跨美/欧/中三区综合排名 · 数据驱动 · 每日更新</p>
  </div>

  <div class="ad-slot top"><div class="ad-inner"><div class="ad-label">Advertisement</div><div class="ad-desktop"><ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px"></ins></div><div class="ad-mobile"><ins class="adsbygoogle" style="display:inline-block;width:320px;height:50px"></ins></div></div></div>

  <div class="top10-list">
{cards_block}
  </div>

  <div class="ad-slot"><div class="ad-inner"><div class="ad-label">Advertisement</div><div class="ad-desktop"><ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px"></ins></div><div class="ad-mobile"><ins class="adsbygoogle" style="display:inline-block;width:320px;height:50px"></ins></div></div></div>

  <div class="top10-footer" style="text-align:center;padding:40px 0;color:#888">
    <p>排名基于热度(views)、增长率(growth%)、时效性(recency)综合计算</p>
    <p>数据范围：{CUTOFF.strftime('%Y-%m-%d')} ~ {NOW.strftime('%Y-%m-%d')}</p>
    <p><a href="index.html">← 返回首页</a> · <a href="rss.xml">RSS订阅</a></p>
  </div>
</div>
</main>
<script src="js/main.js"></script>
</body></html>'''

    return html

if __name__ == "__main__":
    main()
