/* ============================================
   TrendToker — main.js
   ============================================ */

// Language state
let currentLang = localStorage.getItem('lang') || 'en';

// I18N strings
const I18N = {
  en: {
    home: 'Home', viral: 'Viral Top', niche: 'Trend Radar', audio: 'Viral Audio', ecom: 'E-Commerce', about: 'About',
    hero_badge: 'TRENDING NOW',
    hero_desc: 'Breaking down today\'s biggest TikTok trends — data-driven analysis for creators, marketers, and brands.',
    section_viral: 'Today\'s Viral Top',
    section_niche: 'Niche Trend Radar',
    section_audio: 'Viral Audio Library',
    section_ecom: 'E-Commerce Boom',
    section_desc_viral: 'Top trending videos & rapid follower growth — analyzed daily',
    section_desc_niche: 'Emerging niches, new challenges, rising trends — what to watch',
    section_desc_audio: 'Trending sounds & music blowing up on TikTok this week',
    section_desc_ecom: 'TikTok Shop hot products & shopping trends for sellers',
    sidebar_trending: '7-Day Hot List',
    sidebar_categories: 'Categories',
    sidebar_subscribe: 'Stay Updated',
    sidebar_sub_placeholder: 'Your email',
    sidebar_sub_btn: 'Subscribe',
    sidebar_ad: 'Advertisement',
    footer_about: 'TrendToker is an independent news analysis website covering TikTok global trends. We provide daily data-driven trend reports for creators, marketers, and brands.',
    footer_disclaimer: 'All trends and data are based on public TikTok Creator Center information. We do NOT host, store, or distribute any copyrighted media files. This site is not affiliated with TikTok official.',
    footer_links: 'Quick Links',
    footer_legal: 'Legal',
    privacy: 'Privacy Policy',
    terms: 'Terms of Use',
    sitemap: 'Sitemap',
    contact: 'Contact',
    copyright: '© 2026 TrendToker. All rights reserved.',
    read_more: 'Read More',
    hot: 'HOT',
    new: 'NEW',
    rising: 'RISING',
    trend: 'TREND',
    search_placeholder: 'Search trends...',
    no_results: 'No results found',
    loading: 'Loading...',
  },
  zh: {
    home: '首页', viral: '今日爆款', niche: '赛道风向', audio: '热门音乐', ecom: '跨境电商', about: '关于',
    hero_badge: '今日趋势',
    hero_desc: '每日拆解 TikTok 全球最热趋势——为创作者、营销人和品牌提供数据驱动的趋势分析。',
    section_viral: '今日爆款快讯',
    section_niche: '赛道风向雷达',
    section_audio: '热门音乐榜单',
    section_ecom: '跨境电商爆品',
    section_desc_viral: '当日最高播放、最快涨粉视频 + 爆火原因拆解',
    section_desc_niche: '正在飙升/降温的细分赛道、新玩法、新挑战',
    section_desc_audio: '本周全网刷屏 BGM 与音效趋势',
    section_desc_ecom: 'TikTok Shop 爆款品类与带货趋势',
    sidebar_trending: '七日热度榜',
    sidebar_categories: '分类目录',
    sidebar_subscribe: '订阅更新',
    sidebar_sub_placeholder: '输入邮箱',
    sidebar_sub_btn: '订阅',
    sidebar_ad: '广告',
    footer_about: 'TrendToker 是独立的新闻分析网站，覆盖 TikTok 全球趋势。我们每日为创作者、营销人和品牌提供数据驱动的趋势报告。',
    footer_disclaimer: '所有趋势和数据基于 TikTok Creator Center 公开信息。我们不存储或分发任何受版权保护的媒体文件。本站与 TikTok 官方无关。',
    footer_links: '快速链接',
    footer_legal: '法律',
    privacy: '隐私政策',
    terms: '使用条款',
    sitemap: '站点地图',
    contact: '联系我们',
    copyright: '© 2026 TrendToker. 版权所有.',
    read_more: '阅读全文',
    hot: '爆款',
    new: '最新',
    rising: '上升',
    trend: '趋势',
    search_placeholder: '搜索趋势...',
    no_results: '无结果',
    loading: '加载中...',
  }
};

// Get translation
function t(key) {
  return (I18N[currentLang] && I18N[currentLang][key]) || (I18N.en[key]) || key;
}

// Toggle language
function toggleLang() {
  currentLang = currentLang === 'en' ? 'zh' : 'en';
  localStorage.setItem('lang', currentLang);
  window.location.reload();
}

// Set initial lang button text
function initLang() {
  const btn = document.getElementById('langBtn');
  if (btn) btn.textContent = currentLang === 'en' ? '中文' : 'English';
}

// Hamburger menu
function toggleMenu() {
  document.getElementById('navLinks').classList.toggle('open');
}

// Navbar scroll effect
function initNavScroll() {
  const nav = document.querySelector('.navbar');
  if (!nav) return;
  window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 40);
  }, { passive: true });
}

// Image lazy loading with fade
function initLazyImages() {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        if (img.dataset.src) {
          img.src = img.dataset.src;
          img.removeAttribute('data-src');
        }
        img.classList.add('loaded');
        observer.unobserve(img);
      }
    });
  }, { rootMargin: '100px' });
  document.querySelectorAll('img[data-src]').forEach(img => observer.observe(img));
}

// Subscribe form
function initSubscribe() {
  const form = document.getElementById('subscribeForm');
  if (!form) return;
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const input = form.querySelector('input');
    if (input && input.value) {
      alert(currentLang === 'zh' ? '感谢订阅！' : 'Thank you for subscribing!');
      input.value = '';
    }
  });
}

// Init all
document.addEventListener('DOMContentLoaded', () => {
  initLang();
  initNavScroll();
  initLazyImages();
  initSubscribe();
});
