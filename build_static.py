#!/usr/bin/env python3
"""
TrendToker Static Builder v2 — 增量架构
- 数据源: data/{region}/{YYYY-MM-DD}.json (每天5条，不可变)
- 索引: data/{region}/index.json
- 输出: china.html / us.html / eu.html (内嵌最新3天×5=15条)
- 铁律: 旧数据文件永不修改、永不删除
"""

import json, os, sys, datetime

BASE = r"D:\网站源码\趋势播报站"
DAYS_TO_SHOW = 30  # Show latest N days on region pages
PER_PAGE = 10     # Pagination

REGIONS = {
    "china": {"flag": "🇨🇳", "accent": "#FE2C55", "label_en": "China Market", "label_zh": "中国区", "default_lang": "zh"},
    "us":    {"flag": "🇺🇸", "accent": "#161823", "label_en": "US Market", "label_zh": "美国区", "default_lang": "en"},
    "eu":    {"flag": "🇪🇺", "accent": "#003399", "label_en": "EU Market", "label_zh": "欧盟区", "default_lang": "en"},
}


def load_region_data(region):
    """Load latest N days of articles for a region."""
    data_dir = os.path.join(BASE, "data", region)
    index_path = os.path.join(data_dir, "index.json")
    
    if not os.path.exists(index_path):
        print(f"  ⚠ No index.json for {region}, skipping")
        return []
    
    with open(index_path, "r", encoding="utf-8") as f:
        idx = json.load(f)
    
    dates = sorted(idx.get("dates", []), reverse=True)  # newest first
    latest = dates[:DAYS_TO_SHOW]  # take latest N
    
    articles = []
    for date in latest:  # newest first display order
        day_file = os.path.join(data_dir, f"{date}.json")
        if os.path.exists(day_file):
            with open(day_file, "r", encoding="utf-8") as f:
                day_articles = json.load(f)
            articles.extend(day_articles)
    
    return articles


def ensure_bilingual(articles):
    """Fill missing bilingual content from article metadata."""
    for a in articles:
        content = a.get("content", {})
        # Skip if both languages exist and are non-empty
        has_en = "en" in content and content["en"] and any(content["en"].values())
        has_zh = "zh" in content and content["zh"] and any(content["zh"].values())
        
        if not has_zh:
            # Generate Chinese from metadata
            t = a.get("title_zh", "") or a.get("title_en", "")
            s = a.get("summary_zh", "") or a.get("summary_en", "")
            ph = a.get("phase_zh", "") or a.get("phase", "爆发期")
            badge = a.get("badge", "")
            diff = a.get("difficulty", 1)
            win = a.get("window", "-")
            st = a.get("stats", {})
            cpm = a.get("cpm", "-")
            content["zh"] = {
                "what": f"{t}。{s}",
                "data": f"关键指标：热度={st.get('heat','-')}，增长={st.get('growth','-')}，CPM={cpm}，难度={'★'*diff}，窗口期={win}。生命周期阶段：{ph}。",
                "analysis": f"该趋势处于{ph}阶段，难度{'较低' if diff<=2 else '中等' if diff<=3 else '较高'}。核心驱动力包括平台算法变化、用户消费行为迁徙及内容供给创新。{'低门槛意味着新手友好，' if diff<=2 else ''}创作者应在{win}窗口期内建立内容壁垒。品牌方可评估用户画像重合度，小预算测试ROI。卖家应关注供应链匹配度与利润空间。",
                "takeaway": f"创作者：聚焦{badge or '该赛道'}，{'低' if diff<=2 else '中'}门槛快速产出差异化内容。品牌：小预算验证后规模化。卖家：优先选择退货率低的品类。核心原则：原创性优于同质化。"
            }
        
        if not has_en:
            # Generate English from metadata
            t = a.get("title_en", "") or a.get("title_zh", "")
            s = a.get("summary_en", "") or a.get("summary_zh", "")
            ph = a.get("phase", "surging")
            badge = a.get("badge", "")
            diff = a.get("difficulty", 1)
            win = a.get("window", "-")
            st = a.get("stats", {})
            cpm = a.get("cpm", "-")
            content["en"] = {
                "what": f"{t}. {s}",
                "data": f"Key metrics: heat={st.get('heat','-')}, growth={st.get('growth','-')}, CPM={cpm}, difficulty={'★'*diff}, window={win}. Phase: {ph}.",
                "analysis": f"This trend is in the {ph} phase with {'low' if diff<=2 else 'moderate' if diff<=3 else 'high'} barriers to entry. Core drivers include platform algorithm shifts, evolving consumer behavior, and content supply-side innovation. Creators should build content moats within the {win} window. Brands should evaluate audience overlap for sponsorship ROI. Sellers should prioritize categories with high margins and low return rates.",
                "takeaway": f"Creators: Focus on {badge or 'this niche'}, leverage {'low' if diff<=2 else 'moderate'} barriers to produce differentiated content fast. Brands: Test small-budget campaigns before scaling. Sellers: Prioritize products with strong margins. Core rule: originality beats homogeneity."
            }
    
    return articles


def build_rank_items(articles, region, page_num=1):
    """Generate HTML for a page of rank items."""
    items = []
    for j, a in enumerate(articles):
        i = (page_num - 1) * PER_PAGE + j
        badge_cls = a.get("badgeClass", "tag-china").replace("tag-", "")
        phase = a.get("phase", "surging")
        phase_zh = a.get("phase_zh", "爆发期")
        stats_html = ""
        if a.get("stats"):
            for _, v in list(a["stats"].items())[:2]:
                stats_html += f'<span>📊 {v}</span>'

        items.append(f"""
      <a href="article.html?r={region}&id={a['id']}" class="rank-item fade-in" style="animation-delay:{j*0.08}s">
        <div class="rank-num r{i<3 and i+1 or 'x'}">{i+1}</div>
        <div class="rank-body">
          <div class="rank-badges"><span class="rank-badge b-{badge_cls}">{a['badge']}</span><span class="ph-badge ph-{phase}"><span class="lzh">{phase_zh}</span><span class="len">{phase}</span></span></div>
          <div class="rank-title"><span class="lzh">{a['title_zh']}</span><span class="len">{a['title_en']}</span></div>
          <div class="rank-desc"><span class="lzh">{a['summary_zh']}</span><span class="len">{a['summary_en']}</span></div>
          <div class="rank-meta"><span>📅 {a['date']}</span>{stats_html}<span>⭐ {"★"*a.get('difficulty',1)}</span><span>💰 {a.get('cpm','-')}</span></div>
        </div>
        <div class="rank-chart"><canvas id="c{i}"></canvas></div>
      </a>""")

    return "".join(items)


def build_charts_js(articles, accent):
    """Generate Chart.js initialization code."""
    plugin = f"""
// Gradient fill plugin
const gPlugin = {{
  id: 'gFill',
  beforeDraw: function(chart) {{
    const ctx = chart.ctx;
    const ca = chart.chartArea;
    if (!ca) return;
    const grad = ctx.createLinearGradient(0, ca.top, 0, ca.bottom);
    grad.addColorStop(0, '{accent}33');
    grad.addColorStop(0.5, '{accent}10');
    grad.addColorStop(1, '{accent}00');
    chart.data.datasets[0].backgroundColor = grad;
  }}
}};
Chart.register(gPlugin);
"""
    charts = []
    for i, a in enumerate(articles):
        d = a.get('trend', [])
        if not d:
            continue
        mx = max(d)
        charts.append(f"""    {{
      const ctx = document.getElementById('c{i}');
      if (!ctx) return;
      const d = {json.dumps(d)};
      const mx = Math.max(...d);
      new Chart(ctx, {{
        type: 'line',
        data: {{ labels: d.map(function(_,j){{return j+1}}), datasets: [{{ data: d, borderColor: '{accent}', borderWidth: 2, pointRadius: d.map(function(v){{return v===mx?3:0}}), pointBackgroundColor: '{accent}', pointBorderColor: '#fff', pointBorderWidth: 1.5, fill: true, tension: 0.4 }}] }},
        options: {{ 
          responsive: true, maintainAspectRatio: false,
          interaction: {{ intersect: false, mode: 'index' }},
          plugins: {{ legend: {{ display: false }}, tooltip: {{ enabled: false }} }},
          scales: {{
            x: {{ display: false }},
            y: {{ display: true, position: 'right',
              grid: {{ color: 'rgba(0,0,0,0.04)', drawBorder: false }},
              ticks: {{ font: {{ size: 8 }}, color: '#c5c6ca', maxTicksLimit: 2, callback: function(v){{return v>=1000?(v/1000).toFixed(1)+'k':v}} }},
              border: {{ display: false }}
            }}
          }}
        }}
      }});
    }}""")
    return plugin + "\n" + "\n".join(charts)


def build_region_page(region, cfg):
    """Build single region page from day files."""
    articles = load_region_data(region)
    if not articles:
        print(f"  ⚠ No data for {region}")
        return

    ensure_bilingual(articles)  # Fill missing en/zh content

    total = len(articles)
    pages = (total + PER_PAGE - 1) // PER_PAGE

    # Build pages HTML
    pages_html = []
    for p in range(1, pages + 1):
        start = (p - 1) * PER_PAGE
        page_articles = articles[start:start + PER_PAGE]
        items = build_rank_items(page_articles, region, p)
        pages_html.append(f'<div class="page" data-page="{p}" style="display:{p==1 and "block" or "none"}">{items}</div>')
    
    rank_html = "".join(pages_html)

    # Pagination
    pager = ""
    if pages > 1:
        pager = '<div class="pager" id="pager" style="display:none">'
        pager += '<button class="pg-btn" id="pgPrev" onclick="goPage(cur-1)">Prev</button>'
        for p in range(1, pages + 1):
            active = " active" if p == 1 else ""
            pager += f'<button class="pg-num{active}" onclick="goPage({p})">{p}</button>'
        pager += '<button class="pg-btn" id="pgNext" onclick="goPage(cur+1)">Next</button>'
        pager += '</div>'

    # Charts JS
    charts_js = build_charts_js(articles, cfg['accent'])

    # Build HTML
    default_lang = cfg['default_lang']
    ts = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    
    html = f'''<!DOCTYPE html><html lang="{default_lang}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{region.upper()} TikTok Report | TrendToker</title>
<meta name="description" content="Daily Top 5 trends — lifecycle tracking, CPM data, and actionable playbooks.">
<meta name="robots" content="index, follow"><meta name="baidu-site-verification" content="codeva-OcnBgecQNl"><link rel="stylesheet" href="css/style.css">
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<script>(function(){{var bp=document.createElement('script');bp.src='https://zz.bdstatic.com/linksubmit/push.js';var s=document.getElementsByTagName('script')[0];s.parentNode.insertBefore(bp,s);}})();</script>
<!-- build: {ts} -->
</head><body>
<nav class="navbar"><div class="nav-inner">
<a href="index.html" class="nav-logo">Trend<span>Toker</span></a>
<div class="nav-links">
<a href="china.html" id="nChina" {region=="china" and 'class="active"' or ""}>China</a>
<a href="us.html" id="nUS" {region=="us" and 'class="active"' or ""}>US</a>
<a href="eu.html" id="nEU" {region=="eu" and 'class="active"' or ""}>EU</a>
<a href="about.html" id="nAbout">About</a>
</div>
<div class="nav-right"><div class="nav-util"><button onclick="history.back()" title="Back">‹</button><button onclick="location.reload()" title="Refresh">↻</button></div><button class="lang-btn" id="langBtn" onclick="swL()">中文</button><div class="hamburger" onclick="toggleMenu()"><span></span><span></span><span></span></div></div>
</div></nav>
<main class="main">
<div class="hero fade-in"><div class="badge">{cfg['flag']} <span id="hLabel">{cfg['label_en']}</span></div><h1 id="hTitle">{region.upper()} TikTok Daily Trend Report</h1><p id="hSub">Top 5 trending — lifecycle tracking, CPM data, and actionable playbooks</p></div>
<div class="ad-slot top"><div class="ad-inner"><div class="ad-label">Advertisement</div><div class="ad-desktop"><ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px"></ins></div><div class="ad-mobile"><ins class="adsbygoogle" style="display:inline-block;width:320px;height:50px"></ins></div></div></div>
<div class="rank-list" id="RL">{rank_html}</div>
<div class="ad-slot"><div class="ad-inner"><div class="ad-label">Advertisement</div><div class="ad-desktop"><ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px"></ins></div><div class="ad-mobile"><ins class="adsbygoogle" style="display:inline-block;width:320px;height:50px"></ins></div></div></div>
{pager}
</main>
<div class="ad-slot bottom"><div class="ad-inner"><div class="ad-label">Advertisement</div><div class="ad-desktop"><ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px"></ins></div><div class="ad-mobile"><ins class="adsbygoogle" style="display:inline-block;width:320px;height:50px"></ins></div></div></div>
<footer class="footer"><p id="ftCopy">&copy; 2026 TrendToker</p></footer>
<script>
var L = localStorage.getItem('lang') || null;
if(!L)L='{default_lang}';
applyLang(L);

function applyLang(lang){{
  L=lang;
  localStorage.setItem('lang',lang);
  document.querySelectorAll('.lzh').forEach(function(el){{el.style.display=lang==='zh'?'inline':'none'}});
  document.querySelectorAll('.len').forEach(function(el){{el.style.display=lang==='en'?'inline':'none'}});
  document.getElementById('langBtn').textContent=lang==='zh'?'English':'中文';
  var t={{hTitle:['{region.upper()} TikTok Daily Trend Report','{region.upper()}区TikTok趋势日报'],hSub:['Top 5 trending — lifecycle tracking, CPM data, and actionable playbooks','每日Top5爆款 — 生命周期追踪、CPM数据、行动清单'],nChina:['China','中国区'],nUS:['US','美国区'],nEU:['EU','欧盟区'],nAbout:['About','关于'],ftCopy:['© 2026 TrendToker','© 2026 TrendToker'],hLabel:['{cfg['label_en']}','{cfg['label_zh']}'],pgPrev:['Prev','上一页'],pgNext:['Next','下一页']}};
  Object.keys(t).forEach(function(k){{var e=document.getElementById(k);if(e)e.textContent=t[k][lang==='zh'?1:0]}});
}}

function toggleMenu(){{var n=document.querySelector('.nav-links');n.style.display=n.style.display==='flex'?'none':'flex'}}
function swL(){{applyLang(L==='en'?'zh':'en')}}

// Pagination
var cur=1, total={pages};
document.getElementById('pager').style.display=total>1?'flex':'none';
function goPage(n){{
  if(n<1||n>total)return;
  document.querySelectorAll('.page').forEach(function(el){{el.style.display='none'}});
  var pg=document.querySelector('.page[data-page="'+n+'"]');
  if(pg)pg.style.display='block';
  document.querySelectorAll('.pg-num').forEach(function(el,i){{el.classList.toggle('active',i+1===n)}});
  cur=n;
  document.getElementById('pgPrev').disabled=cur<=1;
  document.getElementById('pgNext').disabled=cur>=total;
}}

// Charts
setTimeout(function(){{
{charts_js}
}},300);
</script>
</body></html>'''

    out_path = os.path.join(BASE, f"{region}.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    # Also write combined JSON for article.html compatibility
    combined_path = os.path.join(BASE, "data", f"{region}.json")
    with open(combined_path, "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)

    kb = len(html) // 1024
    print(f"  Built {region}.html ({total} articles, {kb}KB, {pages} pages) → data/{region}.json")


def main():
    print("TrendToker Static Builder v2\n")
    for region, cfg in REGIONS.items():
        build_region_page(region, cfg)
    print(f"\nDone! Showing latest {DAYS_TO_SHOW} days per region.")
    print("Old data files remain untouched in data/{region}/YYYY-MM-DD.json")

if __name__ == "__main__":
    main()
