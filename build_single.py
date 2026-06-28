#!/usr/bin/env python3
"""Build globalshortvideotrend.top as single-file HTML"""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, 'data')

# Load china/eu/us data
regions = {}
for region in ['china', 'eu', 'us']:
    path = os.path.join(DATA, f'{region}.json')
    if os.path.exists(path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                regions[region] = json.load(f)
        except:
            pass

# Count articles
total_articles = 0
articles_sample = []
for rname, rdata in regions.items():
    if isinstance(rdata, list):
        total_articles += len(rdata)
        articles_sample.extend(rdata[:5])
    elif isinstance(rdata, dict):
        items = rdata.get('trends', rdata.get('articles', []))
        total_articles += len(items)
        articles_sample.extend(items[:5])

regions_display = {
    'china': {'name': 'China', 'emoji': '🇨🇳', 'desc': 'Douyin, Kuaishou, Bilibili, Weibo trends'},
    'eu': {'name': 'Europe', 'emoji': '🇪🇺', 'desc': 'TikTok, Instagram, YouTube trends'},
    'us': {'name': 'USA', 'emoji': '🇺🇸', 'desc': 'TikTok, Instagram, YouTube trends'}
}

def esc(s):
    if not s: return ''
    return str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('"','&quot;')

html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Global Short Video Trends — Daily Trend Analysis from China, Europe & USA</title>
<meta name="description" content="Daily short video trend analysis across China (Douyin), Europe, and USA (TikTok). ''' + str(total_articles) + '''+ trend reports covering viral content, creator strategies, and platform algorithms.">
<meta name="keywords" content="short video trends, TikTok trends, Douyin trends, viral content, social media analytics, creator economy">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://globalshortvideotrend.top/">
<meta property="og:title" content="Global Short Video Trends — Daily Analysis">
<meta property="og:description" content="Daily trend analysis from China (Douyin), Europe, and USA (TikTok) short video platforms.">
<meta property="og:url" content="https://globalshortvideotrend.top/">
<meta property="og:type" content="website">
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Global Short Video Trends",
  "url": "https://globalshortvideotrend.top/",
  "description": "Daily short video trend analysis across China, Europe, and USA markets. ''' + str(total_articles) + '''+ reports.",
  "about": {"@type": "Thing", "name": "Short Video Trends", "description": "Global short video platform trend analysis"}
}
</script>
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;color:#111;background:#f8f9fa;line-height:1.7}
.container{max-width:1100px;margin:0 auto;padding:0 24px}
.nav{position:sticky;top:0;z-index:100;background:rgba(255,255,255,.95);backdrop-filter:blur(12px);border-bottom:1px solid #dee2e6;padding:16px 0}
.nav-inner{max-width:1100px;margin:0 auto;padding:0 24px;display:flex;justify-content:space-between;align-items:center}
.nav-logo{font-size:20px;font-weight:700;text-decoration:none;color:#111}
.hero{padding:60px 24px 50px;text-align:center;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);color:#fff}
.hero h1{font-size:34px;font-weight:800;max-width:650px;margin:0 auto 12px;line-height:1.25}
.hero p{font-size:16px;opacity:.9;max-width:500px;margin:0 auto}
.hero-stats{display:flex;justify-content:center;gap:40px;margin-top:28px;flex-wrap:wrap}
.hero-stat{text-align:center}
.hero-stat-num{font-size:26px;font-weight:800}
.hero-stat-label{font-size:12px;opacity:.8;margin-top:4px;text-transform:uppercase}
.section{padding:48px 0}
.section-title{font-size:22px;font-weight:700;margin-bottom:20px}
.region-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:20px}
.region-card{background:#fff;border:1px solid #dee2e6;border-radius:12px;padding:28px;text-decoration:none;color:inherit;transition:all .15s}
.region-card:hover{border-color:#667eea;transform:translateY(-2px);box-shadow:0 4px 16px rgba(0,0,0,.08)}
.region-emoji{font-size:36px;margin-bottom:12px}
.region-name{font-size:18px;font-weight:700;margin-bottom:6px}
.region-desc{font-size:13px;color:#666;line-height:1.7}
.footer{background:#111;color:rgba(255,255,255,.7);padding:40px 24px;margin-top:48px}
.footer-inner{max-width:1100px;margin:0 auto;text-align:center}
.footer p{font-size:13px;line-height:1.8}
.footer a{color:rgba(255,255,255,.9)}
.footer-divider{border:0;border-top:1px solid rgba(255,255,255,.15);margin:16px 0}
@media(max-width:768px){
  .hero h1{font-size:24px}
  .region-grid{grid-template-columns:1fr}
}
</style>
</head>
<body>
<nav class="nav"><div class="nav-inner">
<a class="nav-logo" href="/">Global Short Video Trends</a>
</div></nav>

<header class="hero">
<h1>Global Short Video Trends — Daily Analysis</h1>
<p>Track viral content, creator strategies, and platform algorithms across China 🇨🇳, Europe 🇪🇺, and USA 🇺🇸</p>
<div class="hero-stats">
<div class="hero-stat"><div class="hero-stat-num">3</div><div class="hero-stat-label">Regions</div></div>
<div class="hero-stat"><div class="hero-stat-num">''' + str(total_articles) + '''</div><div class="hero-stat-label">Reports</div></div>
<div class="hero-stat"><div class="hero-stat-num">Daily</div><div class="hero-stat-label">Updates</div></div>
</div></header>

<main class="container">
<section class="section">
<h2 class="section-title">Trend Regions</h2>
<div class="region-grid">
'''
for rid, info in regions_display.items():
    count = len(regions.get(rid, [])) if isinstance(regions.get(rid, []), list) else 0
    html += f'''<a href="/{rid}.html" class="region-card">
<div class="region-emoji">{info['emoji']}</div>
<div class="region-name">{info['name']}</div>
<div class="region-desc">{info['desc']} — {count} reports</div>
</a>
'''

html += '''</div></section>
</main>

<footer class="footer"><div class="footer-inner">
<p><strong>Global Short Video Trends</strong> — Data-driven trend analysis for the creator economy</p>
<hr class="footer-divider">
<p>Trend data is updated daily. Content is for informational purposes only.</p>
<p>© 2026 · <a href="https://globalshortvideotrend.top/">globalshortvideotrend.top</a></p>
</div></footer>
</body></html>'''

out_path = os.path.join(BASE, 'index_single.html')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html)

size_kb = os.path.getsize(out_path) / 1024
print(f"Generated: {out_path}, Size: {size_kb:.1f} KB, Articles: {total_articles}")
