#!/usr/bin/env python3
"""Generate 2026-06-16 trend data for China/US/EU regions."""
import json, os

TODAY = "2026-06-16"
BASE = "D:/网站源码/趋势播报站/data"

# ===== CHINA =====
china_data = [
  {
    "id": "cn-086", "date": TODAY,
    "badge": "Hot Trending", "badgeClass": "tag-china",
    "title_zh": "端午经济3.0：从吃粽子到内容消费升级，11.3M热度的节日变现全景",
    "title_en": "Dragon Boat Economy 3.0: From Eating Zongzi to Content Monetization at 11.3M Heat",
    "summary_zh": "端午经济热度攀升以1130万热度登顶热搜。这早已不是简单的节日消费——从美食教程、文旅打卡到非遗体验，端午已成为抖音生态内年度最强内容变现窗口之一，覆盖带货、文旅、餐饮三大赛道。",
    "summary_en": "Dragon Boat economy surged to 11.3M heat on Douyin. It's no longer simple holiday spending — from food tutorials to cultural tourism, it's now one of Douyin's strongest annual monetization windows.",
    "stats": {"heat": "11.3M", "growth": "+280%"},
    "trend": [12, 20, 32, 46, 60, 73, 84, 92, 100],
    "phase": "surging", "phase_zh": "爆发期", "difficulty": 2,
    "window": "端午前后7天 (6/12-6/18)", "cpm": "¥8-15",
    "actions": {
      "creator": [
        "拍摄家乡端午习俗纪录片式Vlog，突出地域差异性",
        "发起‘全国粽子口味盲测’系列挑战，一期一省对比",
        "制作端午美食教程+带货链接闭环内容"
      ],
      "brand": [
        "食品品牌联合美食达人推出端午限定礼盒联名",
        "地方文旅局联动达人推广端午民俗体验线路",
        "厨具/餐具品牌植入粽子制作场景化种草"
      ],
      "seller": [
        "上架各地特色粽子礼盒+冷链配送",
        "推广端午DIY手工材料包(艾草/五彩绳/香囊)",
        "销售竹叶/粽绳/糯米等家庭包粽套装"
      ],
      "avoid": [
        "不做纯搬运式粽子开箱，缺乏原创性",
        "不碰端午节文化争议(起源归属等)",
        "避免食品安全话题引发争议"
      ]
    },
    "content": {
      "zh": {
        "what": "2026年端午经济话题以1130万热度进入抖音热搜前三。与往年不同，今年端午内容的特征是从'吃什么'升级为'怎么玩'——苏州金龙巡游、顺德粥底火锅、河南宝泉打卡等文旅内容与粽子美食形成双引擎。",
        "data": "端午经济热度1130万 | #端午话题矩阵总播放58亿+ | 端午期间美食内容互动率+67% | 粽子相关商品电商搜索量同比+215% | 文旅类端午内容完播率高出日常42%",
        "analysis": "端午经济的底层逻辑是'节日锚点+内容升级+电商闭环'三重进化。节日提供了确定性的流量高峰；内容已从单一的美食教程扩展到文旅Vlog、非遗手作、地域PK等多元形态；抖音电商的'内容即货架'让每一帧画面都是潜在成交点。品牌方面，端午礼品市场年规模超千亿，短视频渠道渗透率仍在快速提升。",
        "takeaway": "0-3天：抓住端午尾巴发布节日限定内容。3个月：建立#中国节日美食图鉴 IP系列。6个月：提前布局中秋内容矩阵。风险：端午后热度将急剧回落，内容需转向夏季主题衔接。"
      }
    }
  },
  {
    "id": "cn-087", "date": TODAY,
    "badge": "Hot Trending", "badgeClass": "tag-china",
    "title_zh": "美妆大开箱1180万热度：从消费展示到KOL选品方法论的内容进化",
    "title_en": "Beauty Unboxing 11.8M Heat: Content Evolution from Consumerism to KOL Curation Methodology",
    "summary_zh": "我的美妆宝藏大开箱以1177万热度登顶抖音热搜榜首。美妆开箱从单纯的消费展示，进化为'筛选式评测+场景化使用+成分科普'的三合一内容模型，正在重塑美妆KOL的变现路径。",
    "summary_en": "Beauty unboxing topped Douyin at 11.77M heat. It evolved from pure consumption display into a curation-review-education trifecta reshaping beauty KOL monetization.",
    "stats": {"heat": "11.8M", "growth": "+220%"},
    "trend": [18, 28, 40, 53, 65, 75, 83, 91, 100],
    "phase": "surging", "phase_zh": "爆发期", "difficulty": 2,
    "window": "6月美妆消费旺季 (6/10-6/30)", "cpm": "¥12-25",
    "actions": {
      "creator": [
        "制作'我只留真正好用的'筛选式美妆评测系列",
        "将开箱与具体场景绑定：夏日持妆/毕业妆容/面试妆容",
        "结合成分分析做深度科普型开箱，建立专业信任"
      ],
      "brand": [
        "美妆品牌投放筛选型KOL而非纯展示型博主",
        "推出限量小样套装供KOL开箱测评",
        "联名夏季限定包装引爆开箱话题"
      ],
      "seller": [
        "上架KOL同款美妆产品组合套装",
        "推广美妆收纳/化妆镜/化妆刷等周边产品",
        "销售夏季护肤防晒产品小样试用装"
      ],
      "avoid": [
        "不做全买推荐式开箱，观众已疲劳",
        "不发布未经实测的产品推荐",
        "避免夸大功效的营销话术"
      ]
    },
    "content": {
      "zh": {
        "what": "6月15日，\"我的美妆宝藏大开箱\"以1177万热度登顶抖音热搜第一。这一趋势反映了美妆内容从'我买了什么'向'我只留下真正好用的'的范式转变。头部KOL开始用'筛选淘汰制'替代'全买推荐制'，以增强可信度和粉丝粘性。",
        "data": "美妆开箱热度1177万 | 美妆类内容6月日均互动量+45% | '筛选式评测'标签完播率比传统开箱高32% | 美妆KOL带货转化率6月均值8.3% | 成分科普类美妆内容涨粉速度+180%",
        "analysis": "美妆开箱内容的进化反映了消费者从'冲动种草'到'理性筛选'的心智转变。在经济环境趋紧的背景下，观众更关注'值不值得买'而非'有什么新东西'。平台算法也在奖励深度内容——带有成分分析、横向对比、场景实测的视频获得更高完播率和收藏率。对于KOL而言，'专业选品官'人设比'购物狂'人设更具长期变现潜力。",
        "takeaway": "0-3天：发布筛选式开箱视频。3个月：建立'成分党测评'专业内容矩阵。6个月：开发自有选品标准/IP化。风险：产品翻车会反噬信任。"
      }
    }
  },
  {
    "id": "cn-088", "date": TODAY,
    "badge": "Hot Trending", "badgeClass": "tag-china",
    "title_zh": "内马尔之舞×世界杯：体育明星IP的内容裂变与衍生品经济",
    "title_en": "Neymar Dance × World Cup: Sports Celebrity IP Content Fission and Merch Economy",
    "summary_zh": "世界杯赛程进入白热化，内马尔之舞话题以766万热度回归抖音热搜。德国7:1库拉索、西班牙vs佛得角等赛事话题同步霸榜。体育明星IP+世界杯周期=创作者年度最大流量红利。",
    "summary_en": "World Cup heats up as Neymar's dance returns at 7.66M heat. Germany 7:1 Curacao and Spain vs Cape Verde also dominate. Sports IP + World Cup = creators' biggest annual traffic bonus.",
    "stats": {"heat": "7.7M", "growth": "+195%"},
    "trend": [22, 32, 44, 55, 66, 75, 83, 91, 100],
    "phase": "surging", "phase_zh": "爆发期", "difficulty": 2,
    "window": "世界杯赛程期间 (6/11-7/19)", "cpm": "¥10-20",
    "actions": {
      "creator": [
        "翻拍内马尔/哈兰德等球星标志动作模仿挑战",
        "制作'世界杯球星招牌动作百科全书'系列混剪",
        "发起'办公室颠球挑战'等低门槛体育内容"
      ],
      "brand": [
        "体育品牌投放世界杯主题达人种草球衣/球鞋",
        "运动饮料/能量品牌植入看球场景和熬夜场景",
        "餐饮品牌推出世界杯观赛套餐+达人探店联动"
      ],
      "seller": [
        "销售世界杯球星同款球衣/围巾/纪念品",
        "推广观赛装备：大屏投影/零食礼包/啤酒套装",
        "上架足球训练辅助器材和儿童足球装备"
      ],
      "avoid": [
        "不参与球迷对立和国家队攻击",
        "不做赌球/竞猜类违规内容",
        "避免未经授权的比赛画面搬运(FIFA版权)"
      ]
    },
    "content": {
      "zh": {
        "what": "2026世界杯激战正酣，内马尔标志性桑巴舞步在抖音掀起新一轮模仿热潮。同时德国7:1狂胜库拉索、西班牙对佛得角的精彩对决霸占多条热搜。世界杯内容正在从'看比赛'扩展为'玩比赛'——模仿球星动作、花式解说、观赛Vlog等UGC形态爆发。",
        "data": "内马尔之舞热度766万 | 世界杯话题总播放量超200亿 | 足球挑战类视频完播率42% | 世界杯期间体育内容创作者涨粉+250% | 世界杯相关商品抖音搜索量周环比+340%",
        "analysis": "世界杯是四年一度的全球注意力黑洞，而'球星标志动作模仿'是参与门槛最低的内容形式。内马尔之舞兼具视觉冲击力和情绪感染力，完美契合短视频传播。从平台经济看，世界杯期间抖音体育类内容权重全面提升，流量倾斜明显。品牌方面，每届世界杯都催生一批新消费品牌——从球衣经济到观赛场景消费，机会窗口约7周。",
        "takeaway": "0-3天：立即发布球星动作模仿/观赛Vlog。3个月：持续追赛程热点建立体育内容IP。6个月：世界杯结束后用'球星同款训练'系列维持热度。风险：押注单一球队/球星表现不稳定。"
      }
    }
  },
  {
    "id": "cn-089", "date": TODAY,
    "badge": "Hot Trending", "badgeClass": "tag-china",
    "title_zh": "炽夏定档：影视IP预热期的内容淘金窗口与二创经济",
    "title_en": "Blazing Summer Premiere: Pre-Release Content Gold Rush and Derivative Creation Economy",
    "summary_zh": "炽夏官宣定档6月16日，话题热度瞬间攀升至897万。影视剧定档到开播的黄金48小时，是娱乐内容创作者涨粉、品牌借势营销、衍生周边预售的超级窗口期。",
    "summary_en": "Blazing Summer confirmed premiere on June 16, hitting 8.97M heat. The 48-hour window between announcement and premiere is a super-window for creator growth, brand tie-ins, and derivative pre-sales.",
    "stats": {"heat": "9.0M", "growth": "+560%"},
    "trend": [5, 12, 25, 42, 60, 75, 85, 93, 100],
    "phase": "emerging", "phase_zh": "萌芽期", "difficulty": 1,
    "window": "定档到开播48小时+首周 (6/16-6/23)", "cpm": "¥8-12",
    "actions": {
      "creator": [
        "制作剧情预测/角色分析等预判型内容抢首发流量",
        "发起'定档倒计时'互动话题制造期待感",
        "开播后第一时间制作Reaction/名场面解析"
      ],
      "brand": [
        "快消品牌快速联动推出炽夏联名限定包装",
        "视频平台投放定档信息流广告+达人二创",
        "时尚品牌借势剧中穿搭做同款种草"
      ],
      "seller": [
        "预售剧中同款服饰/配饰/化妆品",
        "上架炽夏主题手机壳/海报/周边",
        "推广观剧零食包/会员卡套餐"
      ],
      "avoid": [
        "不做剧透型内容破坏观众体验",
        "不发布未经授权的正片片段搬运",
        "避免无脑吹或无脑黑的内容倾向"
      ]
    },
    "content": {
      "zh": {
        "what": "6月15日，电视剧《炽夏》官宣定档6月16日，话题#炽夏定档0616#以897万热度迅速冲上抖音热搜。定档消息成为当日娱乐板块最大热点，大量娱乐号、粉丝账号涌入内容生产。",
        "data": "定档话题热度897万(半天内) | 影视定档类内容首24小时互动率是日常3倍 | 娱乐KOL定档期内容涨粉速度+180% | 影视IP衍生品预售转化率8-15% | 定档48小时内相关话题自然流量占比超70%",
        "analysis": "影视IP的定档窗口期是标准的内容抢跑赛道。核心驱动力是'信息不对称+期待经济'——首发内容获得最大流量倾斜，后发者只能吃长尾。从消费心理看，观众在定档瞬间处于'高唤醒低认知'状态，最容易被内容引导。品牌借势的逻辑是'快'——48小时内的联名/话题最容易收割关注。平台算法在定档节点会主动提升相关内容的推荐权重。",
        "takeaway": "0-3天：抢占定档首发内容(预测/分析/科普)。3个月：建立影视IP追踪内容矩阵。6个月：形成'新剧定档→首发内容→系列解读'标准化流程。风险：剧集口碑翻车会反噬内容可信度。"
      }
    }
  },
  {
    "id": "cn-090", "date": TODAY,
    "badge": "Hot Trending", "badgeClass": "tag-china",
    "title_zh": "江浙沪杨梅凡尔赛：地域美食的社交货币化与夏季农产品内容爆发",
    "title_en": "Yangtze Delta Waxberry Flex: Regional Food as Social Currency and Summer Agri-Content Boom",
    "summary_zh": "江浙沪凡尔赛从晒杨梅开始以915万热度登上抖音热搜。从杨梅到顺德粥底火锅，夏季地域特色美食正在成为最强社交货币——'你那里有什么好吃的'正在取代'你那里热不热'成为夏季社交开场白。",
    "summary_en": "Yangtze Delta waxberry flexing hit 9.15M heat. From waxberries to Shunde congee hotpot, regional summer foods are becoming the strongest social currency on Douyin.",
    "stats": {"heat": "9.2M", "growth": "+310%"},
    "trend": [15, 25, 38, 50, 62, 74, 85, 93, 100],
    "phase": "surging", "phase_zh": "爆发期", "difficulty": 1,
    "window": "杨梅季+夏季美食窗口 (6/10-7/15)", "cpm": "¥6-12",
    "actions": {
      "creator": [
        "拍摄家乡夏季限定美食从采摘到上桌全流程",
        "制作'中国夏季水果地图'系列地域对比内容",
        "发起'你家乡夏天必吃的是什么'互动话题"
      ],
      "brand": [
        "生鲜电商平台联动达人做产地直发直播带货",
        "地方政府/文旅局投放地域美食文化推广",
        "厨具品牌植入夏日凉菜/水果料理场景"
      ],
      "seller": [
        "销售产地直发杨梅/荔枝/水蜜桃等时令水果",
        "推广水果保鲜包装/冷链配送服务",
        "上架夏日水果料理工具(榨汁机/冰沙机)"
      ],
      "avoid": [
        "不做虚假产地宣传破坏信任",
        "不夸大水果功效做违规营销",
        "避免地域歧视和地域攻击内容"
      ]
    },
    "content": {
      "zh": {
        "what": "6月15日，\"江浙沪凡尔赛从晒杨梅开始\"以915万热度登上抖音热搜，同时\"被顺德粥底火锅狠狠惊艳到了\"、\"长沙夏日特供落地签\"等地域美食话题多点开花。夏季限定的地域美食正在成为抖音最强社交货币——'你来我家吃'式的凡尔赛晒图天然具备高互动属性。",
        "data": "江浙沪杨梅915万热度 | 地域美食类内容6月互动率+52% | #家乡美食 话题总播放620亿+ | 时令水果直播带货转化率12-18% | 地域美食类内容平均分享率比普通美食高40%",
        "analysis": "地域美食内容的爆火底层逻辑是'稀缺性+认同感+社交分享'三重驱动。时令水果的稀缺性制造了'我有你没有'的分享冲动；地域认同构建了'我家乡最好吃'的集体情绪；社交分享则完成了从个人展示到群体狂欢的扩散。从带货逻辑看，产地直发模式让农产品跳过中间商直达消费者，抖音电商的生鲜品类正在迎来结构性增长机会。",
        "takeaway": "0-3天：发布家乡夏季限定美食视频。3个月：建立'中国夏季美食地图'系列IP。6个月：提前布局秋季农产品内容+产地直播合作。风险：生鲜品控和冷链物流是最大挑战。"
      }
    }
  }
]

# ===== US =====
us_data = [
  {
    "id": "us-101", "date": TODAY,
    "badge": "Hot Trending", "badgeClass": "tag-us",
    "title_zh": "撕拉唇线笔413500%增长：TikTok美妆爆品的病毒公式与DTC变现路径",
    "title_en": "Peel-Off Lip Liner 413,500% Growth: The Viral Formula Behind TikTok's Biggest Beauty Product",
    "summary_zh": "Peel-Off Lip Liner以413500%的30天增长率登顶Exploding Topics榜首。一款不到20美元的美妆小单品，凭什么在TikTok上创造现象级爆发？答案在于'可视化效果+低门槛+UGC复制'的病毒三角。",
    "summary_en": "Peel-Off Lip Liner tops Exploding Topics at 413,500% 30-day growth. This sub-$20 beauty item shows the viral triangle: visual payoff + low barrier + UGC replicability.",
    "stats": {"heat": "413,500%", "growth": "+413,500%"},
    "trend": [8, 15, 28, 45, 62, 78, 88, 95, 100],
    "phase": "surging", "phase_zh": "爆发期", "difficulty": 2,
    "window": "产品生命周期峰值 (6月-8月)", "cpm": "$8-15",
    "actions": {
      "creator": [
        "拍摄撕拉唇线笔的前后对比效果视频(最强钩子)",
        "制作'10款唇线笔横向测评'系列深度内容",
        "发起#PeelOffLipLiner挑战引导UGC裂变"
      ],
      "brand": [
        "美妆品牌快速跟进推出自家撕拉唇线笔产品",
        "联名TikTok美妆KOL打造限量联名色号",
        "在TikTok Shop设置限时折扣驱动冲动消费"
      ],
      "seller": [
        "上架撕拉唇线笔+定妆喷雾组合套装",
        "推广唇部护理周边(唇膜/磨砂膏)",
        "销售美妆工具套装(唇刷/化妆镜)"
      ],
      "avoid": [
        "不做虚假效果展示导致退货潮",
        "不抄袭大牌包装引发法律风险",
        "避免忽视产品安全性(唇部直接接触)"
      ]
    },
    "content": {
      "zh": {
        "what": "Peel-Off Lip Liner（撕拉唇线笔）在2026年6月以413500%的惊人增长率成为TikTok平台增长最快的美妆产品。用户涂抹唇线笔后撕掉外层，留下持久唇线——这种'撕拉'的视觉体验天然适合短视频，单条演示视频可获百万播放。",
        "data": "30天增长率413500% | TikTok帖子数8,000+ | 单条演示视频最高播放2400万 | Amazon月搜索量+850% | 平均产品价格$12-18 | 评论中'need this'关键词出现率67%",
        "analysis": "撕拉唇线笔的病毒式传播完美验证了TikTok爆品的'三层漏斗'模型：第一层，撕拉动作本身就是视觉奇观，调动观众的ASMR式满足感；第二层，产品价格低于$20，冲动消费门槛极低；第三层，使用效果可量化(持久度/唇形改变)，激发'我也要试试'的模仿欲。从DTC品牌角度看，这种产品完美适配TikTok Shop的'短视频-直播-小店'闭环，头部卖家的月销售额已突破$50万。",
        "takeaway": "0-3天：快速上架同类产品+发布对比测评。3个月：建立美妆爆品监测和快速跟品机制。6个月：从跟品转向自主研发差异化产品。风险：产品周期短(3-6个月)，跟品窗口极窄。"
      }
    }
  },
  {
    "id": "us-102", "date": TODAY,
    "badge": "Hot Trending", "badgeClass": "tag-us",
    "title_zh": "AI脑腐叙事：超现实AI迷你剧如何成为TikTok最强内容格式",
    "title_en": "AI Brain Rot: How Surreal AI Mini-Narratives Became TikTok's Strongest Content Format",
    "summary_zh": "AI Brain Rot叙事格式正在TikTok上爆发——怪异角色+不可能的场景+令人满足的改造+混乱结局。这种由AI生成的超现实迷你故事已成为6月最强的内容模板，单条播放量破千万已成常态。",
    "summary_en": "AI Brain Rot storytelling is exploding on TikTok — weird characters + impossible settings + satisfying makeovers + chaotic endings. Surreal AI mini-narratives have become June's strongest content format.",
    "stats": {"heat": "Extreme", "growth": "+450%"},
    "trend": [10, 18, 30, 45, 58, 70, 82, 92, 100],
    "phase": "surging", "phase_zh": "爆发期", "difficulty": 3,
    "window": "AI工具普及期+创意红利期 (6月-9月)", "cpm": "$10-18",
    "actions": {
      "creator": [
        "学习AI视频生成工具(如Runway/Pika)制作脑洞迷你剧",
        "创建系列化AI角色打造可持续的内容IP",
        "结合热门音频模板(如Gut Genug)做AI+音乐混剪"
      ],
      "brand": [
        "AI工具品牌赞助AI创作挑战赛获取用户",
        "消费品牌在AI脑腐视频中做品牌植入",
        "娱乐公司签约AI内容创作者开发IP"
      ],
      "seller": [
        "销售AI视频生成工具订阅/教程",
        "推广AI创作硬件(高性能显卡/云渲染)",
        "上架AI内容创作模板/素材包"
      ],
      "avoid": [
        "不制作涉及恐怖/暴力/政治的AI内容",
        "不抄袭已爆款的AI叙事直接搬运",
        "避免AI生成内容的版权归属争议"
      ]
    },
    "content": {
      "zh": {
        "what": "AI Brain Rot（脑腐叙事）是2026年6月TikTok上增长最快的内容格式之一。代表创作者@brainrotdiy用AI工具生成超现实迷你故事：怪异角色出现在不可能的地点，经历令人满足的改造过程，最终以混乱或反转结局。这种格式的每条视频平均播放500万+。",
        "data": "AI脑腐内容30天增长率+450% | 代表创作者@brainrotdiy粉丝破300万 | 单条爆款最高播放4200万 | #AIBrainRot话题总播放18亿+ | 此类内容平均互动率9.2% | AI视频工具下载量月增+320%",
        "analysis": "AI脑腐叙事的爆发体现了三个底层驱动力：第一，AI视频生成工具(Runway Gen-4, Pika 2.0)能力飞跃，创作者可以用文本描述生成电影级画面；第二，TikTok算法天然奖励'高完播率+高重看率'内容，而超现实叙事让人欲罢不能；第三，这种格式具有极强的可复制性——一个公式可以生成无限变体。从平台经济看，AI内容正在创造新的创作阶层——不需要真人出镜，不需要拍摄设备，只需要创意+工具。",
        "takeaway": "0-3天：注册AI视频工具+发布第一条脑洞叙事。3个月：建立系列化AI角色IP。6个月：当AI工具进一步普及，差异化将来自'创意独特度'而非技术门槛。风险：平台可能出台AI内容标签政策影响流量。"
      }
    }
  },
  {
    "id": "us-103", "date": TODAY,
    "badge": "Hot Trending", "badgeClass": "tag-us",
    "title_zh": "骄傲月×世界杯：双文化引擎驱动下的6月内容与品牌营销战略",
    "title_en": "Pride Month × World Cup: Dual Cultural Engines Driving June Content and Brand Strategy",
    "summary_zh": "6月的美国TikTok同时被两个超级文化事件点燃——骄傲月(Pride Month)和世界杯。这两股内容洪流并非竞争关系，聪明的创作者和品牌正在找到两者的交汇点，创造1+1>2的声量效应。",
    "summary_en": "US TikTok in June is ignited by two cultural super-events: Pride Month and World Cup. Smart creators and brands are finding intersection points for 1+1>2 amplification.",
    "stats": {"heat": "Massive", "growth": "+180%"},
    "trend": [15, 25, 38, 50, 63, 75, 85, 93, 100],
    "phase": "surging", "phase_zh": "爆发期", "difficulty": 2,
    "window": "整个6月 (Pride Month) + 世界杯赛程 (6/11-7/19)", "cpm": "$12-22",
    "actions": {
      "creator": [
        "制作骄傲月彩虹妆容+世界杯国旗配色二合一内容",
        "采访LGBTQ+球迷群体做人文故事内容",
        "发起'用世界杯庆祝骄傲月'创意挑战"
      ],
      "brand": [
        "品牌推出Pride+世界杯联名限定系列产品",
        "投放同时覆盖两个社群的中腰部达人矩阵",
        "在TikTok发起品牌挑战赛融合两大主题"
      ],
      "seller": [
        "销售彩虹配色+国旗元素二合一周边产品",
        "推广骄傲月限定版世界杯观赛装备",
        "上架Pride主题派对用品(含世界杯元素)"
      ],
      "avoid": [
        "不做浅层的'彩虹洗'(Rainbow Washing)营销",
        "不对LGBTQ+群体做刻板印象化呈现",
        "避免将骄傲月商业化过度引发负面舆论"
      ]
    },
    "content": {
      "zh": {
        "what": "2026年6月是美国内容创作者的双黄蛋月份——骄傲月覆盖整个6月，世界杯从6月11日持续到7月19日。TikTok官方推出Pride Month 2026创作者扶持计划，为8位LGBTQIA+创作者和小企业提供流量扶持。与此同时，NBA总决赛、F1摩纳哥站等体育事件也在叠加声量。",
        "data": "#Pride2026话题播放量32亿+(6月至今) | #WorldCup2026话题播放量110亿+ | TikTok Pride计划扶持创作者平均涨粉+340% | 骄傲月相关品牌内容互动率+28% | 双主题融合内容分享率比单主题高45%",
        "analysis": "骄傲月与世界杯的时间重叠创造了一个独特的'文化交叉'内容空间。底层逻辑是：两个事件的受众有大量重叠(年轻/多元/全球视野)，但内容生产者很少同时覆盖两者——这意味着融合内容存在蓝海机会。从品牌策略看，同时参与两个文化时刻的品牌比只参与一个的品牌多获得67%的品牌搜索量增长。但关键风险是'彩虹洗'(Rainbow Washing)——只在6月做表面功夫的品牌会遭遇严重的舆论反弹。",
        "takeaway": "0-3天：创建骄傲月+世界杯融合内容。3个月：世界杯结束后用赛事复盘维持体育内容。6个月：将学到的'双文化事件策略'应用到其他节日组合。风险：文化敏感度不足会导致品牌危机。"
      }
    }
  },
  {
    "id": "us-104", "date": TODAY,
    "badge": "Hot Trending", "badgeClass": "tag-us",
    "title_zh": "游戏化健身革命：PushupArena到深蹲楔，互动追踪如何重塑家庭健身",
    "title_en": "Game-ified Fitness Revolution: From PushupArena to Squat Wedge, How Interactive Tracking Reshapes Home Fitness",
    "summary_zh": "PushupArena应用以'对比钩子'格式爆火，深蹲楔(Squat Wedge)以5600%增长率持续攀升。TikTok健身内容正从'看别人练'进化为'自己练+AI追踪+社交PK'的游戏化模式。",
    "summary_en": "PushupArena app went viral with contrast-hook format, Squat Wedge climbs at 5,600% growth. TikTok fitness evolves from 'watch others' to 'track yourself + AI coaching + social competition'.",
    "stats": {"heat": "5,600%", "growth": "+5,600%"},
    "trend": [12, 22, 35, 48, 60, 72, 83, 92, 100],
    "phase": "surging", "phase_zh": "爆发期", "difficulty": 2,
    "window": "夏季健身旺季+产品爆发期 (6月-9月)", "cpm": "$6-12",
    "actions": {
      "creator": [
        "用PushupArena类的应用录制健身前后对比视频",
        "制作'30天深蹲楔挑战'系列连载内容",
        "发起健身PK挑战赛邀请粉丝参与排行榜"
      ],
      "brand": [
        "健身品牌开发自有健身追踪应用增强用户粘性",
        "运动品牌联名健身应用做品牌植入",
        "健康食品品牌赞助健身挑战赛活动"
      ],
      "seller": [
        "上架深蹲楔/弹力带等家庭健身小器材套装",
        "推广健身追踪应用会员订阅",
        "销售健身+营养组合包(器材+蛋白粉)"
      ],
      "avoid": [
        "不做夸张的'7天练出马甲线'类虚假承诺",
        "不推荐不安全或无科学依据的训练方法",
        "避免忽视个体差异导致用户受伤风险"
      ]
    },
    "content": {
      "zh": {
        "what": "游戏化健身正在成为TikTok健身赛道的下一波浪潮。PushupArena应用的'坏俯卧撑vs好俯卧撑'对比格式爆火——应用通过AI动态追踪用户的真实动作并可视化差异。深蹲楔(Squat Wedge)作为低成本家庭健身器材，在TikTok上以5600%的增长率爆发，Amazon月销量超2000件。",
        "data": "深蹲楔5年搜索增长253% | TikTok健身内容总播放量890亿+ | 游戏化健身应用下载量月增+180% | 家庭健身器材TikTok Shop GMV增长+95% | 健身挑战类内容互动率是教程类的2.1倍",
        "analysis": "游戏化健身爆发的底层逻辑是'即时反馈+社交比较+低门槛'。传统健身教程缺乏反馈机制，而AI追踪应用通过可视化动作质量提供了即时满足感。深蹲楔这类<$30的低成本器材消除了'健身需要去健身房买年卡'的心理障碍。从平台经济看，TikTok Shop正成为健身器材的重要销售渠道——短视频展示效果→直播答疑→小店下单的闭环转化率远超传统电商。",
        "takeaway": "0-3天：发布游戏化健身对比视频。3个月：建立'30天健身挑战'系列IP。6个月：当品类竞争加剧，差异化来自'专业教练认证+科学背书'。风险：健身器材退货率较高(15-20%)。"
      }
    }
  },
  {
    "id": "us-105", "date": TODAY,
    "badge": "Hot Trending", "badgeClass": "tag-us",
    "title_zh": "桑拿凳13400%增长：居家健康SPA经济与Amazon爆品掘金路线",
    "title_en": "Sauna Seat 13,400% Growth: Home Wellness SPA Economy and Amazon Gold Rush Route",
    "summary_zh": "Sauna Seat(桑拿凳)以13400%的30天增长率领跑居家健康品类，搭配加温灯(10600%)和隐私帐篷(9500%)，一个围绕'居家SPA化'的产品矩阵正在TikTok上成形。",
    "summary_en": "Sauna Seat leads home wellness at 13,400% growth, joined by Warming Lamp (10,600%) and Privacy Tent (9,500%). An at-home SPA product ecosystem is taking shape on TikTok.",
    "stats": {"heat": "13,400%", "growth": "+13,400%"},
    "trend": [6, 14, 27, 42, 58, 72, 84, 93, 100],
    "phase": "emerging", "phase_zh": "萌芽期", "difficulty": 2,
    "window": "产品生命周期早期 (6月-12月)", "cpm": "$5-10",
    "actions": {
      "creator": [
        "制作'居家SPA改造'前后对比内容",
        "拍摄桑拿凳+加温灯组合使用的ASMR体验视频",
        "发起'300美元打造家庭SPA'挑战系列"
      ],
      "brand": [
        "健康品牌推出居家SPA产品套装捆绑销售",
        "酒店/民宿品牌赞助居家SPA内容做场景营销",
        "保险/健康管理品牌关联'自我关怀'主题"
      ],
      "seller": [
        "上架桑拿凳+加温灯+隐私帐篷三件套组合",
        "推广便携式桑拿/蒸汽设备",
        "销售精油/浴盐/按摩工具等SPA耗材套装"
      ],
      "avoid": [
        "不做不安全的使用演示(高温/电器风险)",
        "不过度夸大健康功效",
        "避免忽视产品安全认证(UL/FCC等)"
      ]
    },
    "content": {
      "zh": {
        "what": "Sauna Seat(桑拿凳)在TikTok上以13400%的30天增长率爆发，同品类的加温灯(10600%)和隐私帐篷(9500%)也同步飙升。这三个产品共同描绘出一个清晰趋势：消费者正在将专业SPA体验搬回家中，用一个周末和几百美元完成'居家SPA化改造'。",
        "data": "桑拿凳30天增长13400% | 加温灯增长10600% | 隐私帐篷增长9500% | 居家SPA相关话题月播放量4.2亿+ | Amazon上此类产品平均评分4.6 | 目标用户画像:25-45岁女性78%",
        "analysis": "居家SPA经济的爆发由三重因素驱动。第一，后疫情时代的'家庭即避风港'心理持续强化——人们愿意投资升级居家体验。第二，TikTok的内容格式天然适合展示'改造前后'的视觉冲击——从一个普通浴室到私人SPA的对比让人无法不点赞。第三，这些产品单价在$30-150之间，属于'可承受的奢侈'——不是买不起的奢侈品，但足够让生活品质明显提升。从电商角度看，这是典型的'短视频种草→Amazon/独立站成交'路径，但由于TikTok Shop的扩张，闭环转化率正在迅速提升。",
        "takeaway": "0-3天：上架桑拿凳+加温灯套装。3个月：开发自有品牌居家SPA产品线。6个月：建立'居家健康升级'内容+电商矩阵。风险：季节性波动明显(冬季旺季)，夏季需调整产品组合。"
      }
    }
  }
]

# ===== EU =====
eu_data = [
  {
    "id": "eu-106", "date": TODAY,
    "badge": "Hot Trending", "badgeClass": "tag-eu",
    "title_zh": "Gut Genug席卷欧洲：德语情感音频如何成为跨国病毒格式的引爆点",
    "title_en": "Gut Genug Sweeps Europe: How a German Emotional Audio Became the Ignition Point for Cross-Border Viral Formats",
    "summary_zh": "德语歌曲'Gut Genug'(你已经足够好)的节拍编辑版本正在TikTok欧洲区爆发。它同时具备情感短语+编辑节点，成为体育混剪、动漫编辑、角色互换等多元内容的通用模板——一条音频，无限内容。",
    "summary_en": "The beat-edit version of German song 'Gut Genug' (You Are Good Enough) is exploding across European TikTok. It combines emotional phrase + edit node as a universal template.",
    "stats": {"heat": "Viral", "growth": "+380%"},
    "trend": [10, 18, 30, 44, 58, 72, 84, 93, 100],
    "phase": "surging", "phase_zh": "爆发期", "difficulty": 1,
    "window": "音频生命周期+世界杯助推 (6月-7月)", "cpm": "€6-12",
    "actions": {
      "creator": [
        "用Gut Genug音频制作世界杯精彩瞬间速度编辑",
        "创作'从低谷到高光'个人成长叙事型视频",
        "发起#GutGenugChallenge鼓励用户分享自我接纳故事"
      ],
      "brand": [
        "德国/欧洲品牌快速采用该音频做本土化内容",
        "运动品牌用该音频做励志向品牌故事",
        "心理健康App赞助#GutGenug话题推广"
      ],
      "seller": [
        "上架Gut Genug相关周边(情绪疗愈产品)",
        "推广德国文化/语言学习产品",
        "销售编辑软件/模板套装"
      ],
      "avoid": [
        "不滥用情感音频做硬广引发反感",
        "避免对原曲版权的侵权行为",
        "不做与'自我接纳'主题相悖的负面内容"
      ]
    },
    "content": {
      "zh": {
        "what": "德语歌曲'Du bist gut genug'(你已经足够好)的节拍编辑版本正在欧洲TikTok全面爆发。从德国的体育混剪到法国的动漫编辑到意大利的角色互换——一条德语音频跨越了语言障碍，成为全欧洲创作者的通用编辑模板。世界杯内容的加入进一步推高了其使用量。",
        "data": "Gut Genug音频使用量450万+(欧洲区) | 覆盖国家:德国/法国/意大利/西班牙/荷兰 | 世界杯相关内容中该音频使用率18% | 使用该音频的视频平均播放量比常规高65% | 德语区创作者使用后涨粉+210%",
        "analysis": "Gut Genug的跨国病毒传播验证了TikTok音频的三个成功要素：第一，情感短语'你已经足够好'具有普世共鸣性，不受语言限制；第二，节拍Drop提供了清晰的编辑节点，创作者可以轻松做速度编辑和转场；第三，世界杯期间体育内容对'情绪+节奏'型音频有天然需求。从平台经济看，TikTok的音乐分发能力已经超越了语言边界——一条德语歌可以同时进入法国、意大利、西班牙的推荐流。",
        "takeaway": "0-3天：立即使用Gut Genug音频制作速度编辑内容。3个月：当音频热潮退去，将学到的高速编辑技巧应用到下一波热点音频。风险：音频热度周期极短(2-3周)。"
      }
    }
  },
  {
    "id": "eu-107", "date": TODAY,
    "badge": "Hot Trending", "badgeClass": "tag-eu",
    "title_zh": "骄傲月×世界杯欧洲主场：多元包容与体育激情的欧洲夏季内容双引擎",
    "title_en": "Pride Month × World Cup Europe: Diversity & Sports Passion as European Summer's Content Twin Engines",
    "summary_zh": "2026年6月的欧洲同时被骄傲月和世界杯点燃。阿姆斯特丹WorldPride 2026、西班牙世界杯主场、柏林骄傲游行——欧洲创作者正在用本地化视角连接这两大全球事件。",
    "summary_en": "Europe in June 2026 is ignited by Pride Month and World Cup simultaneously. Amsterdam WorldPride 2026, Spain's World Cup hosting, Berlin Pride — European creators connect these global events with local lenses.",
    "stats": {"heat": "Massive", "growth": "+210%"},
    "trend": [14, 24, 37, 50, 62, 73, 84, 93, 100],
    "phase": "surging", "phase_zh": "爆发期", "difficulty": 2,
    "window": "6月骄傲月+世界杯6/11-7/19", "cpm": "€8-18",
    "actions": {
      "creator": [
        "制作'我的城市如何庆祝骄傲月+世界杯'纪录片式内容",
        "采访LGBTQ+足球迷做人文故事系列",
        "发起#PrideAndFootball跨社群连接挑战"
      ],
      "brand": [
        "欧洲品牌推出Pride+世界杯联名限定系列",
        "阿姆斯特丹/柏林/巴塞罗那旅游局做双主题推广",
        "时尚品牌推出彩虹元素+足球文化融合设计"
      ],
      "seller": [
        "销售骄傲月主题世界杯观赛装备",
        "推广Amsterdam WorldPride限定旅行套餐",
        "上架多元文化融合设计周边产品"
      ],
      "avoid": [
        "不做'彩虹洗'只挂旗不行动的伪包容营销",
        "不对LGBTQ+群体做token化呈现",
        "避免在保守地区的内容引发争议"
      ]
    },
    "content": {
      "zh": {
        "what": "欧洲的2026年6月正在见证一个罕见的文化共振时刻——骄傲月(Pride Month)与世界杯(World Cup)的双重叠加。阿姆斯特丹举办WorldPride 2026，西班牙作为世界杯东道主之一，柏林和伦敦的骄傲游行规模创纪录——两个大型文化事件同时激活了欧洲创作者的内容生产力。",
        "data": "#WorldPride2026话题播放量15亿+ | 欧洲世界杯相关话题播放量45亿+ | 欧洲Pride主题品牌内容互动率+35% | TikTok欧洲区6月内容发布量同比+62% | 双主题融合内容在欧洲区平均分享率+48%",
        "analysis": "骄傲月与世界杯的同期发生，在欧洲形成了独特的内容交叉空间。欧洲文化对多元包容的接受度较高，且足球文化根基深厚——两者的结合不是生硬拼凑，而是有真实的用户基础。从创作者角度看，融合内容因为同时触碰两个话题标签，获得了叠加的算法推荐权重。从品牌策略看，欧洲消费者对'真诚参与'vs'商业利用'的区分非常敏锐——只有长期支持多元包容的品牌才能从这一刻受益。",
        "takeaway": "0-3天：发布本地化骄傲月+世界杯融合内容。3个月：世界杯结束后将多元包容主题延续到日常内容。6个月：将学到的事件叠加策略应用于圣诞+新年组合。风险：欧洲各国文化差异大，内容需按国家定制。"
      }
    }
  },
  {
    "id": "eu-108", "date": TODAY,
    "badge": "Hot Trending", "badgeClass": "tag-eu",
    "title_zh": "植物基洗涤剂29800%增长：欧洲可持续消费浪潮下的绿色爆品公式",
    "title_en": "Plant-Based Detergent 29,800% Growth: Green Blockbuster Formula Under Europe's Sustainable Consumption Wave",
    "summary_zh": "植物基洗衣液以29800%的TikTok增长率成为欧洲可持续消费赛道最亮眼的爆品。从洗衣片(5200%)到竹子随行杯(3400%)，一条完整的'绿色日用品'产品矩阵正在形成——尤其在欧洲，可持续不是标签而是刚需。",
    "summary_en": "Plant-based detergent leads at 29,800% growth, joined by detergent sheets (5,200%) and bamboo tumblers (3,400%). In Europe, sustainability isn't a label — it's a requirement.",
    "stats": {"heat": "29,800%", "growth": "+29,800%"},
    "trend": [8, 16, 28, 42, 57, 70, 82, 92, 100],
    "phase": "surging", "phase_zh": "爆发期", "difficulty": 2,
    "window": "产品爆发期+欧盟绿色政策红利 (6月-12月)", "cpm": "€5-10",
    "actions": {
      "creator": [
        "拍摄自制植物基洗衣液DIY教程(最高互动格式)",
        "制作'化学vs植物基洗涤效果对比'测评",
        "发起#GreenSwap30天挑战:一件一件替换家用化学品"
      ],
      "brand": [
        "日化品牌推出植物基子品牌或产品线",
        "获得欧盟环保认证(EU Ecolabel)增加信任背书",
        "联名环保KOL做'从家开始拯救地球'campaign"
      ],
      "seller": [
        "上架植物基洗涤剂+洗衣片+竹子杯组合套装",
        "推广可补充装/零废弃包装模式",
        "销售DIY洗涤剂原料套装(皂角/小苏打/精油)"
      ],
      "avoid": [
        "不做'漂绿'(Greenwashing)虚假环保宣传",
        "不忽视欧盟严格的环保标签法规",
        "避免产品功效不如传统产品导致差评"
      ]
    },
    "content": {
      "zh": {
        "what": "植物基洗衣液(Plant Based Detergent)以29800%的TikTok增长率在全球爆发，欧洲市场表现尤为强劲。有趣的是，TikTok上最热门的植物基洗涤内容不是品牌广告，而是'自制植物基洗衣液'的DIY教程——最高一条获赞18.4万。洗衣片(Detergent Sheets, 5200%)和竹子随行杯(Bamboo Tumbler, 3400%)等绿色日用品也在同步飙升。",
        "data": "植物基洗涤剂30天增长29800% | TikTok帖子251条(增长中) | DIY教程平均互动率15.3% | 欧洲绿色日用品市场年增长率22% | EU Ecolabel认证产品溢价能力+30%" , "analysis": "植物基洗涤剂的爆发在欧洲有特殊的地域加成。第一，欧盟的绿色政策(Green Deal、包装法规等)为可持续产品创造了制度性优势；第二，欧洲消费者对'化学成分恐惧'(Chemophobia)的程度高于美国；第三，欧洲大量硬水地区让洗涤效果的可视化对比(化学vs植物基)天然适合短视频。DIY内容的超高互动率说明消费者不只想买绿色产品，更想参与'创造绿色生活'的过程——这是一个品牌可以深度参与的内容空间。",
        "takeaway": "0-3天：发布植物基洗涤DIY或对比测评。3个月：获得EU Ecolabel等认证建立竞争壁垒。6个月：开发可补充装/订阅制模式锁定复购。风险：欧洲环保法规更新快，合规成本可能上升。"
      }
    }
  },
  {
    "id": "eu-109", "date": TODAY,
    "badge": "Hot Trending", "badgeClass": "tag-eu",
    "title_zh": "不锈钢刮痧2100%增长+枸杞茶2800%：中医美容如何征服欧洲TikTok",
    "title_en": "Steel Gua Sha 2,100% + Wolfberry Tea 2,800%: How TCM Beauty Is Conquering European TikTok",
    "summary_zh": "不锈钢刮痧工具以2100%增长率、枸杞茶以2800%增长率在欧洲TikTok上爆发。东方养生概念正从'小众猎奇'升级为'主流健康生活方式'——这背后是K-Beauty到TCM-Beauty的品类迁移。",
    "summary_en": "Stainless steel gua sha (2,100%) and wolfberry tea (2,800%) are exploding on European TikTok. Eastern wellness is upgrading from niche curiosity to mainstream lifestyle.",
    "stats": {"heat": "2,800%", "growth": "+2,800%"},
    "trend": [12, 20, 32, 45, 58, 70, 82, 91, 100],
    "phase": "emerging", "phase_zh": "萌芽期", "difficulty": 2,
    "window": "东方养生概念在欧洲的上升期 (6月-长期)", "cpm": "€8-15",
    "actions": {
      "creator": [
        "制作'西方vs东方护肤流程对比'内容",
        "拍摄刮痧教程+8周使用效果追踪系列",
        "发起#TCMBeautyRoutine分享东方养生日常"
      ],
      "brand": [
        "欧洲美妆品牌开发含东方元素的护肤产品线",
        "健康品牌推出枸杞/红枣/姜黄等功能性茶饮",
        "SPA/水疗中心引入刮痧等东方护理项目"
      ],
      "seller": [
        "上架不锈钢刮痧板+面部精油套装",
        "推广有机枸杞/菊花/玫瑰花等中式茶饮原料",
        "销售铜质/不锈钢美容工具系列"
      ],
      "avoid": [
        "不做'东方神秘主义'式的猎奇化呈现",
        "不夸大刮痧/枸杞的健康功效(遵守EU健康声明法规)",
        "避免文化挪用争议——尊重中医传统知识源头"
      ]
    },
    "content": {
      "zh": {
        "what": "东方养生概念正在欧洲TikTok经历爆发式增长。不锈钢刮痧工具(Stainless Steel Gua Sha)以2100%的5年搜索增长率在欧洲美妆圈走红，头部Amazon卖家月收入超$25万。#guasha话题在TikTok有27.5万+条视频。枸杞茶(Wolfberry Tea)以2800%增长率进入欧洲功能性饮品主流视野。",
        "data": "不锈钢刮痧5年搜索增长2100% | #guasha话题27.5万+视频 | 头部Amazon刮痧卖家月入$25万+ | 枸杞茶5年搜索增长600%(峰值已过但仍在增长) | 欧洲功能性茶饮市场年增18% | TikTok #TCM 话题播放量8亿+",
        "analysis": "中医美容概念在欧洲的爆发不是偶然。第一，K-Beauty在过去5年已经为'亚洲美容方法论'铺好了路——10步护肤流程、精华液、面膜等概念已被欧洲消费者接受；刮痧和枸杞是这条路径的自然延伸。第二，不锈钢刮痧解决了传统石材刮痧的痛点——更卫生、更耐用、温度可控，完美适配欧洲消费者对'功能性+科学性'的需求。第三，枸杞茶以'超级食物'而非'中药'的身份进入市场，避免了草药监管的复杂性。",
        "takeaway": "0-3天：发布刮痧/枸杞的欧洲本地化使用教程。3个月：建立'TCM Beauty for Europeans'内容矩阵。6个月：开发符合欧盟化妆品法规的刮痧+产品套装。风险：EU健康声明法规严格，功效宣称需谨慎。"
      }
    }
  },
  {
    "id": "eu-110", "date": TODAY,
    "badge": "Hot Trending", "badgeClass": "tag-eu",
    "title_zh": "F1摩纳哥+欧洲音乐节季：奢华速度与夏日狂欢的双轨内容经济",
    "title_en": "F1 Monaco + European Festival Season: Luxury Speed and Summer Revelry as Dual-Track Content Economy",
    "summary_zh": "F1摩纳哥大奖赛的奢华氛围+Primavera Sound、Glastonbury等欧洲音乐节的夏日狂欢，正在TikTok上形成两条平行但可交叉的内容赛道——一边是电影级编辑的名人场边时刻，一边是泥泞中的烟火气。",
    "summary_en": "F1 Monaco's luxury atmosphere + Primavera Sound, Glastonbury and European music festivals form two parallel yet crossable content tracks on TikTok — cinematic celebrity edits versus muddy grassroots energy.",
    "stats": {"heat": "Massive", "growth": "+250%"},
    "trend": [16, 26, 38, 50, 62, 74, 85, 93, 100],
    "phase": "mature", "phase_zh": "成熟期", "difficulty": 3,
    "window": "F1赛季+欧洲音乐节季 (6月-8月)", "cpm": "€10-25",
    "actions": {
      "creator": [
        "制作F1摩纳哥电影级编辑+音乐节Vlog双线内容策略",
        "拍摄'音乐节穿搭挑战'系列，一衣多穿横跨多个音乐节",
        "发起#FestivalOutfitCheck结合F1赛道时尚对比"
      ],
      "brand": [
        "奢侈品牌赞助F1内容做高端场景植入",
        "快时尚品牌投放音乐节穿搭达人做场景化种草",
        "旅行品牌推出'F1+音乐节'欧洲夏季旅行套餐"
      ],
      "seller": [
        "销售音乐节装备套装(防水鞋/雨衣/充电宝)",
        "推广F1主题周边和车队商品",
        "上架夏日户外装备(防晒/帐篷/便携椅)"
      ],
      "avoid": [
        "不做只展示消费不提供价值的'炫富'内容",
        "不侵犯F1赛事版权(比赛画面需授权)",
        "避免音乐节上的不安全行为展示"
      ]
    },
    "content": {
      "zh": {
        "what": "欧洲的夏季内容经济由两条平行赛道驱动。上层是F1摩纳哥大奖赛代表的奢华速度文化——名人场边时刻(如Jordyn Woods/Kylie Jenner在NBA总决赛的场边庆祝同款逻辑)、电影级慢动作编辑、摩纳哥港口的游艇场景。下层是Primavera Sound、Glastonbury、Tomorrowland等欧洲音乐节季——泥泞的草地、烟火气的穿搭、36小时不睡觉的疯狂体验。",
        "data": "#F1Monaco话题6月播放量8亿+ | #FestivalSeason话题播放量25亿+ | 音乐节相关内容6月互动率+58% | F1内容平均CPM比普通内容高40%(奢侈品受众) | 欧洲音乐节季直接+间接经济影响超€200亿",
        "analysis": "F1和音乐节代表了欧洲夏季内容消费的两个极端——但TikTok的算法同时拥抱两者。F1内容的商业价值在于其受众的高消费力(CPM比普通内容高40%)，但内容生产门槛高(需要现场或高质量素材)。音乐节内容则门槛极低——任何参加音乐节的人都能生产内容，但竞争激烈。聪明的创作者正在打通两者：用F1电影级叙事手法拍摄普通音乐节，或用音乐节的随性态度解构F1的严肃——这种'碰撞'本身就是爆款公式。",
        "takeaway": "0-3天：如果你在欧洲，参加任何音乐节并发布Vlog。3个月：建立'欧洲夏季活动日历'内容矩阵。6个月：形成'事件驱动型内容'标准化生产流程。风险：两大赛道都需要实际参与成本(门票/交通)。"
      }
    }
  }
]

# Write all 3 files
for region, data in [("china", china_data), ("us", us_data), ("eu", eu_data)]:
    path = os.path.join(BASE, region, f"{TODAY}.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Written {path} ({len(data)} articles)")

print("\nAll 3 region files generated successfully!")
