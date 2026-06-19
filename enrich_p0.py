#!/usr/bin/env python3
import json

enrich = {
  'cn-001': {'phase':'surging','phase_zh':'爆发期','difficulty':1,'window':'4-6周','cpm':'$5-15','actions':{'creator':['拍30秒无声日常:冲咖啡/打扫/学习','用自然光+固定机位+环境音','绝对不加BGM——安静就是钩子'],'brand':['咖啡/香薰/文具品牌赞助','产品自然融入场景,不说广告词','找500-5000粉素人,不用大V'],'seller':['挂耳咖啡/香薰蜡烛/极简文具三件套','客单价29-69最佳','强调治愈系关键词'],'avoid':['不要加热门BGM','不要用美颜滤镜','不要口播推销']}},
  'cn-002': {'phase':'mature','phase_zh':'成熟期','difficulty':3,'window':'2-3周','cpm':'8-20','actions':{'creator':['做满头大汗-瞬间降温对比视频','测评不同品牌挂脖风扇续航/噪音','出行通勤场景植入'],'brand':['差异化:降噪<30dB/续航>12h/马卡龙色','投上班族通勤和户外运动达人','定价19.9-29.9冲动消费区间'],'seller':['宠物降温风扇/儿童安全风扇细分市场','深圳华强北3天出货','强调欧盟仓库提升溢价'],'avoid':['不要打价格战——9.9赛道已死','不要投传统3C测评号,转化率差3倍','不要上白色基础款,外观无差异化']}},
  'cn-003': {'phase':'surging','phase_zh':'爆发期','difficulty':3,'window':'3-6个月','cpm':'15-30','actions':{'creator':['差异化:AI+医疗/AI+法律/AI+设计','标题模板:别让你的同事先用AI','先免费内容引流-再199-299课程转化'],'brand':['在线教育平台赞助软技能类达人','优先25-40岁职场人画像的号','赞助时要求达人提供完课率数据'],'seller':['ChatGPT/Midjourney教程套餐','职场软技能课(沟通/管理/汇报)','退货率<3%品类最佳'],'avoid':['不要再做泛AI通识课','不要用复杂PPT/录屏','不要一上来就卖999高价课']}},
  'cn-004': {'phase':'surging','phase_zh':'爆发期','difficulty':2,'window':'2-4周','cpm':'10-25','actions':{'creator':['掌握1-2个AI视觉工具','拍摄前后对比+反应镜头格式','主动向品牌提案AI挑战方案'],'brand':['美妆/时尚/文旅品牌最适合','设计让用户变成更好自己的挑战','周五晚上8点发布'],'seller':['AI工具教程/模板套餐','Midjourney提示词包','手机端AI工具推荐'],'avoid':['不要设计让用户模仿你的挑战','不要周一到周四发布','不要只用静态对比图,必须录屏展示过程']}},
  'cn-005': {'phase':'surging','phase_zh':'爆发期','difficulty':1,'window':'3-6个月','cpm':'3-8','actions':{'creator':['找本地素人(粉丝300-3000)','内容:不美颜+不标准普通话=高转化','发布:工作日下午5-7点'],'brand':['连锁品牌:培训加盟商如何找本地达人','不做全国统一探店方案','火锅/烧烤/奶茶/甜品最适合'],'seller':['本地生活团购套餐','到店核销券','新品试吃/试住体验'],'avoid':['不要只找粉丝数多的达人','不要用美颜和精致剪辑','不要下午2-4点发']}},
  'us-001': {'phase':'surging','phase_zh':'爆发期','difficulty':1,'window':'4-6 Weeks','cpm':'$5-15','actions':{'creator':['Silent Vlog: natural light + ambient sound','Film 30s of coffee/cleaning/studying','ZERO music — silence IS the hook'],'brand':['Home/lifestyle: candles, coffee, stationery','Micro-influencers (500-5K) convert better','Integrate product into aesthetic, not sales pitch'],'seller':['Coffee beans, candles, desk accessories','$15-30 price range optimal','Bundle as Creator Kit'],'avoid':['Do NOT add trending sounds','No heavy editing or filters','No direct sales language']}},
  'us-002': {'phase':'mature','phase_zh':'成熟期','difficulty':2,'window':'2-3 Weeks','cpm':'$15-35','actions':{'creator':['Screen-record transformation process','Multi-style comparison drives retention','Pitch brands with AI Challenge proposals'],'brand':['Beauty/fashion: show product then transform','Gaming studios: Cyberpunk/Anime styles','$3-15K per integration market rate'],'seller':['AI art tool memberships','Midjourney prompt bundles','Style template packs'],'avoid':['Static images get 3x less engagement','No unlicensed AI tools (copyright risk)','Meta has not released tool publicly']}},
  'us-003': {'phase':'mature','phase_zh':'成熟期','difficulty':3,'window':'2-3 Weeks','cpm':'$8-18','actions':{'creator':['Summer survival kit format','Back-to-back comparison of 3+ fans','Before vs After in extreme heat'],'brand':['Differentiate on noise (<35dB) and battery (>12h)','Pastel/transparent for female, rugged for male','Target commute and outdoor interest tags'],'seller':['Pet cooling products (underserved)','Kids-safe neck fans','Bundle: fan + sunscreen + cooling towel'],'avoid':['Don\'t compete on $9.99','Avoid generic white-label designs','Don\'t target only male gadget audience']}},
  'us-004': {'phase':'surging','phase_zh':'爆发期','difficulty':3,'window':'6-12 Months','cpm':'$25-45','actions':{'creator':['ONE micro-skill: math, Excel, language','Heavy text overlays — 78% no sound','Daily posting: consistency > quality'],'brand':['EdTech: highest-ROI creator niche','$5K micro-creator outperforms $50K macro','Notion, Excel, coding platforms'],'seller':['Online courses $49-199','Productivity templates','Skill certification programs'],'avoid':['Don\'t cover multiple topics','Don\'t make academic — TikTok style matters','Don\'t skip text overlays']}},
  'us-005': {'phase':'surging','phase_zh':'爆发期','difficulty':1,'window':'6+ Months','cpm':'$5-12','actions':{'creator':['Hero product: crochet bee ($5-10)','Film EVERY creation session','Price $15-30 for impulse buy'],'brand':['Craft supply companies','TikTok Shop partnerships','Learn to Crochet starter kit'],'seller':['Crochet bee kits (volume)','Custom pet replicas ($45-80, margin)','Maker Kit subscription boxes'],'avoid':['Don\'t mass-produce — authenticity IS value','Don\'t skip filming process','Don\'t price below $10']}},
  'eu-001': {'phase':'surging','phase_zh':'爆发期','difficulty':2,'window':'6-12 Months','cpm':'15-28','actions':{'creator':['Post in English for all 27 markets','Euro-English accent is valued format','Cross-EU lifestyle comparison content'],'brand':['One EU-wide campaign covers 27 countries','200K budget = continent-wide reach','Prioritize multi-language creators'],'seller':['Cross-border EU e-commerce tools','Translation/localization services','EU market entry consulting'],'avoid':['Don\'t post in only one language','Don\'t ignore local nuances','Don\'t assume US strategies work in EU']}},
  'eu-002': {'phase':'surging','phase_zh':'爆发期','difficulty':3,'window':'Long-Term','cpm':'28-42','actions':{'creator':['EU Regulation Explainer format','Brands desperate for this content','Green finance/ESG angle for higher CPM'],'brand':['Find creators for sustainability explainers','60s TikTok explainer = 4x corporate report','CSRD requires this — compliance = demand'],'seller':['Sustainable product marketplace','Eco-certification consulting','Circular economy toolkits'],'avoid':['Don\'t greenwash — EU verifies claims','Don\'t use generic save-planet messaging','Don\'t ignore regulatory angle']}},
  'eu-003': {'phase':'surging','phase_zh':'爆发期','difficulty':2,'window':'Long-Term','cpm':'12-25','actions':{'creator':['Start 2 languages (native + English)','AI dubbing: 5 languages = 15min','Polyglot identity is marketable niche'],'brand':['Multi-language creators: 2.3x ROI','EU campaigns need multi-language','Sponsor language-learning content'],'seller':['AI dubbing/translation tools','Language learning apps','Multi-language content templates'],'avoid':['Don\'t post single-language only','Don\'t rely on auto-translate','Don\'t assume English-only reaches all']}},
  'eu-004': {'phase':'surging','phase_zh':'爆发期','difficulty':3,'window':'3-6 Months','cpm':'8-18','actions':{'creator':['Product unboxing + real use','German: quality/engineering angle','French: style/design angle'],'brand':['EU SMEs: list NOW','EU warehouse tag = 15-25% premium','Food/cosmetics/baby: EU-made is USP'],'seller':['EU-based return address essential','EU-made certification products','Next-day delivery capability'],'avoid':['Don\'t dropship without EU warehouse','Don\'t ignore 14-day return law','Don\'t underestimate German quality expectations']}},
  'eu-005': {'phase':'surging','phase_zh':'爆发期','difficulty':3,'window':'12+ Months','cpm':'35-55','actions':{'creator':['EU Law Explained: one regulation/video','How [EU Law] affects your daily life','100x less competition than US politics'],'brand':['Think tanks: your audience is on TikTok now','200M+ political ad market for 2027','Sponsor EU policy explainer creators'],'seller':['EU policy research reports','Compliance consulting DMA/DSA/AI Act','Political monitoring services'],'avoid':['Don\'t be partisan — explain, don\'t advocate','Don\'t ignore how-it-affects-you angle','Don\'t assume young Europeans don\'t care']}},
}

base = 'D:/网站源码/趋势播报站/data/'
for region in ['china','us','eu']:
    path = base + region + '.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for a in data:
        if a['id'] not in enrich:
            print(f'MISSING: {a["id"]}')
            continue
        e = enrich[a['id']]
        a['phase'] = e['phase']
        a['phase_zh'] = e['phase_zh']
        a['difficulty'] = e['difficulty']
        a['window'] = e['window']
        a['cpm'] = e['cpm']
        a['actions'] = e['actions']
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f'{region}: {len(data)} articles enriched')

print('Done')
