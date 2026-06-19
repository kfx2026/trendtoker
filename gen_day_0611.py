#!/usr/bin/env python3
"""Generate trend data for 2026-06-11"""
import json, os

today = '2026-06-11'

# ========== CHINA ==========
china_data = [
    {
        "id": "cn-051", "date": today,
        "badge": "Hot Trending", "badgeClass": "tag-china",
        "title_zh": "降温妆席卷全网：夏日美妆经济的流量密码",
        "title_en": "Cool-Down Makeup Sweeps Douyin: The Traffic Formula of Summer Beauty Economy",
        "summary_zh": "抖音热搜第一「天热了就化这个降温妆」引爆1200万热度，薄荷绿眼影+冰感底妆+水光唇釉三件套成为夏季美妆标配，相关产品搜索量48小时暴涨340%。",
        "summary_en": "The #1 Douyin trend 'Cool-Down Makeup' hit 12M heat index. Mint eyeshadow + ice-feel foundation + water-gloss lip combo became summer beauty essentials with 340% search surge in 48 hours.",
        "stats": {"heat": "12.1M", "growth": "+340%"},
        "trend": [15, 22, 35, 48, 67, 82, 95, 100, 98],
        "phase": "surging", "phase_zh": "爆发期",
        "difficulty": 2, "window": "2-3 weeks", "cpm": "$8-15",
        "actions": {
            "creator": ["拍摄降温妆教程对比（妆前38度vs妆后视觉降温）", "测评冰感底妆产品真实持妆力", "发起#我的降温神器 挑战话题"],
            "brand": ["投放美妆达人进行冰感产品种草", "联名推出限定降温彩妆礼盒", "赞助降温妆PK赛事"],
            "seller": ["上架薄荷绿系眼影盘+冰感妆前乳组合", "推出夏季美妆降温套装", "搭配便携小风扇做关联销售"],
            "avoid": ["不要做纯产品罗列无教程价值", "避免虚假降温效果夸大宣传", "不蹭医美冷冻概念"]
        },
        "content": {"zh": {
            "what": "抖音热搜第一「天热了就化这个降温妆」以1207万热度登顶，核心是通过冷色调妆容+冰感质地产品，在视觉和触感上营造「降温」效果。薄荷绿眼影、冰蓝色内眼线、水光冻感唇釉成为标配三件套，相关话题48小时内视频投稿量超12万条。",
            "data": "热度指数1207万，位列全站第一。相关产品（冰感底妆/薄荷眼影/水光唇釉）在抖音商城搜索量48小时暴涨340%。头部达人单条教程播放破800万，完播率达68%（远超美妆类均值42%）。「降温妆」相关话题累计播放已破5亿。",
            "analysis": "这波趋势的底层逻辑是「感官经济」——消费者不只买功能，更买感受。当气温突破35度，「凉感」本身就是溢价因子。从供给侧看，国货美妆品牌早在Q1就备好了冷色调夏季线，平台数据验证了他们的预判。从需求侧看，Z世代追求「妆容即态度」，降温妆既是实用技巧也是社交货币。关键转折点：当「降温妆」从技巧教程升级为「夏日人设标签」，消费决策从理性比价转向情感认同，品牌溢价空间打开。",
            "takeaway": "创作者：现在入场做降温妆教程仍有2-3周红利窗口，重点做「对比感」（热+冷），完播率比单纯教程高40%。卖家：冰感底妆+薄荷眼影组合装客单价可定在89-129元区间，搭配「你的夏日降温包」话术转化率更高。品牌方：投放策略从单品种草转向「降温人设」整套方案，选达人优先看其粉丝画像中18-28岁女性占比（目标>70%）。"
        }}
    },
    {
        "id": "cn-052", "date": today,
        "badge": "Hot Trending", "badgeClass": "tag-china",
        "title_zh": "世界杯梗王大赛：体育娱乐内容的变现新范式",
        "title_en": "World Cup Meme King Contest: New Monetization Paradigm for Sports Entertainment",
        "summary_zh": "「全抖音寻找世界杯梗王」+「世界杯预言家已就位」双话题叠加近2000万热度，UGC体育娱乐内容进入黄金窗口期，梗图/预测/解说三赛道同步爆发。",
        "summary_en": "Dual Douyin trends 'Find the World Cup Meme King' + 'World Cup Prophets' stacked 20M combined heat. UGC sports entertainment enters golden window with memes, predictions, and commentary tracks exploding simultaneously.",
        "stats": {"heat": "19.1M combined", "growth": "+280%"},
        "trend": [20, 30, 42, 55, 70, 85, 92, 100, 97],
        "phase": "surging", "phase_zh": "爆发期",
        "difficulty": 1, "window": "World Cup duration", "cpm": "$5-12",
        "actions": {
            "creator": ["做世界杯每日梗图合集+神预测打卡", "用AI生成球星搞笑表情包系列", "发起世界杯预言PK赛事"],
            "brand": ["赞助世界杯梗王评选活动", "投放体育+幽默双标签达人", "推出世界杯限定包装产品"],
            "seller": ["上架世界杯周边（球衣/手办/加油道具）", "开发世界杯主题手机壳/马克杯", "推出看球零食大礼包"],
            "avoid": ["不涉及赌球/博彩擦边内容", "不做球队国家政治化解读", "避免侵权使用FIFA官方素材"]
        },
        "content": {"zh": {
            "what": "世界杯赛事期间，抖音连续3个相关话题霸榜：「世界杯你的唐梓回来了」(1054万)、「世界杯预言家已就位」(1041万)、「全抖音寻找世界杯梗王」(868万)，合计近2000万热度。核心特征是UGC化——用户不只看球，更在「玩球」：做梗图、当预言家、模仿解说。",
            "data": "三话题合计热度1963万。世界杯相关视频日均新增投稿量超50万条，其中梗类内容占比38%、预测类占比27%、解说模仿类占比19%。头部梗王账号单日涨粉可达5-10万。抖音官方「世界杯梗王」活动奖金池超百万。",
            "analysis": "世界杯是四年一遇的流量核弹，但2026年的独特之处在于：第一，AI工具降低了梗图/视频创作门槛；第二，抖音官方重金扶持UGC（梗王活动百万奖金），形成「平台补贴-创作者涌入-内容丰富-用户留存」正循环；第三，体育娱乐内容的广告主付费意愿极强（啤酒/零食/运动品牌预算充足）。底层逻辑：大赛事IP+UGC众创+平台激励=短视频领域的「内容民主化」典范。",
            "takeaway": "创作者：世界杯期间每天发1条梗/预测内容，坚持整个赛程可实现账号从0到5万粉突破。选择细分角度（如专做「冷门球队日记」或「女球迷视角」）更容易脱颖而出。卖家：世界杯周边在赛事期间溢价空间50-100%，关键是预判热门球队提前备货。品牌方：体育+幽默双标签达人ROI最高，投放时选粉丝中25-40岁男性占比>60%的账号。"
        }}
    },
    {
        "id": "cn-053", "date": today,
        "badge": "Hot Trending", "badgeClass": "tag-china",
        "title_zh": "毕业季内容大爆发：从仪式感到消费力的完整链条",
        "title_en": "Graduation Season Content Explosion: The Full Chain from Ritual to Spending",
        "summary_zh": "「前奏一响毕业季登场」热度超920万，毕业照/毕业旅行/毕业礼物三大内容赛道同步起量，相关商品GMV周环比增长215%。",
        "summary_en": "Graduation Season Arrives with the First Beat hit 9.2M heat. Graduation photos, trips, and gifts surge simultaneously with 215% weekly GMV growth.",
        "stats": {"heat": "9.2M", "growth": "+215%"},
        "trend": [10, 18, 28, 42, 58, 75, 88, 100, 95],
        "phase": "surging", "phase_zh": "爆发期",
        "difficulty": 2, "window": "3-4 weeks", "cpm": "$6-14",
        "actions": {
            "creator": ["拍摄创意毕业照教程（航拍/延时/电影感）", "做毕业旅行攻略Vlog", "发起#我的毕业仪式感 话题挑战"],
            "brand": ["投放毕业季限定产品（定制礼品/旅行装备）", "赞助高校毕业典礼直播", "联合达人做毕业季礼物清单"],
            "seller": ["上架毕业纪念相册定制服务", "推出毕业旅行必备清单套装", "开发学士帽主题饰品/文创"],
            "avoid": ["不消费学生焦虑情绪", "避免贩卖「毕业即失业」焦虑", "不做虚假就业数据宣传"]
        },
        "content": {"zh": {
            "what": "每年6月是毕业季流量巅峰，今年「前奏一响毕业季登场」以920万热度占据抖音热搜第8位，关联话题「高考结束后你最想干什么」也有900万热度。毕业照创意、毕业旅行攻略、毕业礼物推荐三大赛道同步爆发，形成完整的内容-消费链条。",
            "data": "毕业季相关话题累计播放量破15亿。抖音商城「毕业礼物」搜索量周环比+180%，「毕业旅行」搜索+156%。毕业季相关商品GMV周环比增长215%，其中定制类产品（相册/戒指/手链）增速最快达340%。创意毕业照教程类视频平均完播率52%，高于同期大盘8个百分点。",
            "analysis": "毕业季内容的底层逻辑是「人生节点仪式化」——Z世代将毕业从一个时间点升级为一个「内容事件」。三层价值叠加：情感价值（青春记忆的物化需求）、社交价值（朋友圈/抖音的展示欲）、消费价值（礼物经济+旅行经济+服装经济）。平台侧，抖音把毕业季做成了电商节点（类似双11逻辑），从内容种草到商城转化全链路打通。",
            "takeaway": "创作者：毕业季内容窗口还有3-4周（到7月初），优先做「教程型」（怎么拍/怎么选/怎么玩），转化路径比纯情感内容更清晰。卖家：定制类产品（刻字饰品/照片书/毕业熊）利润率最高，客单价80-200元区间最好转化。品牌方：赞助高校毕业活动是性价比最高的校园营销，单场直播可覆盖数万精准年轻用户。"
        }}
    },
    {
        "id": "cn-054", "date": today,
        "badge": "Hot Trending", "badgeClass": "tag-china",
        "title_zh": "西瓜豆腐切：生活技巧类内容的爆款方法论",
        "title_en": "Watermelon Tofu Cut: The Viral Formula for Life Hack Content",
        "summary_zh": "「西瓜原来可以当成豆腐切」910万热度，一个简单切法引发全民模仿，背后是「反常识+即学即用+夏季场景」三要素叠加的爆款公式。",
        "summary_en": "You Can Cut Watermelon Like Tofu hit 9.1M heat. A simple cutting technique triggered nationwide imitation, driven by the formula of counter-intuition + instant applicability + summer context.",
        "stats": {"heat": "9.1M", "growth": "+180%"},
        "trend": [8, 15, 25, 40, 58, 72, 88, 100, 90],
        "phase": "surging", "phase_zh": "爆发期",
        "difficulty": 1, "window": "2 weeks", "cpm": "$3-8",
        "actions": {
            "creator": ["模仿西瓜豆腐切+升级版（花式水果切法合集）", "做夏季水果创意吃法系列", "拍「厨房冷知识」系列短视频"],
            "brand": ["投放厨房工具达人做产品植入", "联合水果品牌做夏日吃法活动", "赞助「厨房神操作」话题挑战"],
            "seller": ["上架水果切割神器/花式刀具套装", "推出夏季水果保鲜盒组合", "搭配西瓜勺/挖球器关联销售"],
            "avoid": ["不做危险刀具操作示范", "避免食品浪费争议内容", "不夸大工具功能"]
        },
        "content": {"zh": {
            "what": "一条「西瓜原来可以当成豆腐切」的视频以910万热度登上抖音热搜，展示了将西瓜横竖各切数刀形成整齐方块的技巧，看起来像切豆腐一样轻松。这个看似简单的内容引发了大量模仿和二创——有人切哈密瓜、切芒果、切各种水果都用「豆腐切法」。",
            "data": "话题热度910万，相关视频投稿量24小时内超8万条。原视频点赞破200万，评论区「学会了」占比超60%。「水果切割」相关商品搜索量48小时涨180%。该话题带动了整个「厨房冷知识」品类的流量上涨，品类整体播放量周涨65%。",
            "analysis": "这条内容的爆款逻辑值得拆解：第一，「反常识」——西瓜这么大的东西居然能像豆腐一样切，认知冲突制造了点击欲；第二，「即学即用」——不需要任何专业技能，看完就能在家复刻；第三，「夏季强场景」——6月正是吃西瓜的季节，需求与内容完美匹配。从平台经济角度看，这类内容的广告加载率极高（因为完播率高+互动率高），是抖音生态中的「高质量流量」。",
            "takeaway": "创作者：「反常识生活技巧」是永不过时的爆款模型，关键是找到大众高频场景中的认知盲区。当前窗口：夏季水果切法系列还有2周红利。卖家：水果切割工具趁热上架，客单价19-49元转化率最高。品牌方：厨房用品品牌可批量投放「生活技巧」达人，这类内容的产品植入接受度极高。"
        }}
    },
    {
        "id": "cn-055", "date": today,
        "badge": "Hot Trending", "badgeClass": "tag-china",
        "title_zh": "后高考消费潮：千万考生的第一笔自由支出",
        "title_en": "Post-Gaokao Spending Wave: 10 Million Students First Free Purchase",
        "summary_zh": "「高考结束后你最想干什么」900万热度引爆后高考经济，旅行/电子产品/驾校/医美四大赛道瓜分千万考生的第一笔「解放消费」。",
        "summary_en": "What Do You Want Most After Gaokao (9M heat) ignites post-exam economy. Travel, electronics, driving school, and aesthetics compete for 10M students first liberation spending.",
        "stats": {"heat": "9.0M", "growth": "+195%"},
        "trend": [12, 20, 32, 45, 60, 75, 88, 97, 100],
        "phase": "emerging", "phase_zh": "萌芽期",
        "difficulty": 2, "window": "4-6 weeks", "cpm": "$5-12",
        "actions": {
            "creator": ["做高考后必做清单Vlog", "拍学生党第一台笔记本电脑选购指南", "发起#高考后的第一件事 话题"],
            "brand": ["推出学生专属优惠（电子产品/旅行套餐）", "投放00后/05后画像达人", "赞助高考生采访类内容"],
            "seller": ["上架学生笔记本电脑+配件套装", "推出暑期旅行装备清单包", "开发高考纪念文创产品"],
            "avoid": ["不贩卖高考焦虑/成绩对比", "不做虚假产品性能宣传", "避免争议话题"]
        },
        "content": {"zh": {
            "what": "2026年高考于6月9日结束，超1000万考生迎来「解放时刻」。抖音话题「高考结束后你最想干什么」以900万热度持续发酵，评论区高频答案：旅行(32%)、买电子产品(24%)、学驾照(18%)、改变形象(15%)、睡觉(11%)。这些答案背后是一个万亿级的暑期消费市场。",
            "data": "2026年高考报名人数1342万（再创历史新高）。后高考消费市场预估规模超3000亿元。旅行消费预估800亿+；电子产品消费预估600亿+（笔记本+手机为主）；驾校报名预估增长45%。抖音「学生党好物」搜索量高考后48小时涨195%。",
            "analysis": "后高考消费潮的底层逻辑：第一，「补偿性消费」——高三一年压抑的消费欲望集中释放；第二，「身份转换」——从学生到准大学生，需要新装备来匹配新身份；第三，「家长钱包松动」——高考结束后家长的消费决策阈值显著降低。从时间窗口看，6月11日-7月底是这波消费的黄金6周。关键趋势：今年「理性消费」意识更强——学生们会在抖音做大量功课再下单，所以「真实测评」类内容比硬广更有效。",
            "takeaway": "创作者：做「学生党真实测评」系列（笔记本/手机/旅行装备），这批用户付费意愿强且粘性高。窗口期6周。卖家：学生3C套装客单价2000-4000元区间最好出量；旅行装备客单价200-500元。品牌方：投放策略瞄准「准大学生」人群包，选粉丝中18-20岁占比>40%的达人。"
        }}
    }
]

# ========== US ==========
us_data = [
    {
        "id": "us-051", "date": today,
        "badge": "Hot Trending", "badgeClass": "tag-us",
        "title_zh": "Rock Music Glitch编辑法：中级创作者的流量加速器",
        "title_en": "Rock Music Glitch Edit: The Traffic Accelerator for Mid-Level Creators",
        "summary_zh": "Charli XCX新单曲「Rock Music」的vocal glitch段落催生全新编辑格式——卡帧定格技术让产品/穿搭瞬间成为视觉焦点，中级编辑难度却有高级视觉效果。",
        "summary_en": "Charli XCX's 'Rock Music' vocal glitch spawns a new editing format. Stuck-frame technique makes products/outfits the visual focal point with mid-level effort but premium output.",
        "stats": {"heat": "8.2M views/day", "growth": "+420%"},
        "trend": [10, 18, 30, 48, 65, 80, 95, 100, 92],
        "phase": "surging", "phase_zh": "爆发期",
        "difficulty": 3, "window": "10-14 days", "cpm": "$12-22",
        "actions": {
            "creator": ["Master the stuck-frame animation on your best outfit/product shot", "Create tutorial content teaching the glitch edit technique", "Batch-film 5+ glitch reveals in one session for daily posting"],
            "brand": ["Commission creators to glitch-freeze your product as the hero moment", "Launch a branded glitch challenge with prize incentive", "Use the format for new product reveals and launch teasers"],
            "seller": ["Feature products in glitch-freeze moments for organic product discovery", "Create compilation reels of top glitch edits featuring your items", "Use the format for before/after product demonstrations"],
            "avoid": ["Don't use copyrighted audio for commercial accounts without clearance", "Avoid over-produced versions that lose the raw appeal", "Don't wait - this format has a 2-week peak window"]
        },
        "content": {"zh": {
            "what": "Charli XCX于5月7日发布新单曲「Rock Music」，歌曲中刻意设计的vocal glitch（人声卡顿）段落成为TikTok创作者的新宠。创作者在视频中配合这段卡顿，使用「stuck frame」（卡帧定格）动画将高光时刻冻结——效果像是算法本身停下来盯着你的穿搭或产品看。",
            "data": "该格式日均新视频产出量超15万条，参与创作者中60%为粉丝1万-50万的中腰部账号。使用该音频的视频平均播放量比创作者日常高3.2倍。编辑教程类内容完播率达71%。音频使用量周增长420%，目前仍处于攀升期。",
            "analysis": "这个趋势的精妙之处在于「技术门槛的甜蜜点」——不像简单对口型那么无门槛（导致内容同质化），也不像专业特效那么高门槛（劝退大部分创作者）。它精准命中了中级创作者的能力区间，让他们能产出「看起来比实际难度高」的内容。从平台经济角度：TikTok算法偏爱「高完播+高互动」内容，卡帧效果天然制造「想看第二遍」的冲动，推动完播率和循环播放率上升。",
            "takeaway": "创作者：学会这个编辑技巧投入产出比极高——一次学会可反复使用，且该格式在不同垂类都适用。窗口期10-14天。卖家：让你的产品成为「被算法定格的那一帧」——在产品展示视频中使用该技术。品牌方：这是目前性价比最高的品牌内容格式之一，中腰部达人就能做出视觉冲击力强的内容。"
        }}
    },
    {
        "id": "us-052", "date": today,
        "badge": "Hot Trending", "badgeClass": "tag-us",
        "title_zh": "2026 Summer Anthem：7秒视频百万播放的极简公式",
        "title_en": "2026 Summer Anthem: The 7-Second Formula for Million-View Videos",
        "summary_zh": "Josh Fawaz混音版「Like a Prayer」被封为2026非官方夏季圣歌，格式极简（7秒对口型+文字标签），小型创作者首次尝试即获百万播放，48小时窗口期。",
        "summary_en": "Josh Fawaz's 'Like a Prayer' remix crowned 2026's unofficial Summer Anthem. Ultra-simple format delivers million views for small creators on first try. 48-hour window.",
        "stats": {"heat": "12.5M views/day", "growth": "+680%"},
        "trend": [5, 12, 25, 45, 68, 85, 100, 95, 80],
        "phase": "surging", "phase_zh": "爆发期",
        "difficulty": 1, "window": "48-72 hours", "cpm": "$4-8",
        "actions": {
            "creator": ["Film a 7-sec lip sync with eye contact and energy - post within 24 hours", "Create a Summer Anthem reaction or ranking video", "Use the audio as background for any summer lifestyle content"],
            "brand": ["Jump on the audio immediately for brand accounts - low effort, high reward", "Create employee/team versions for employer branding content", "Use as soundtrack for summer collection reveals"],
            "seller": ["Feature summer products with the anthem as background audio", "Create quick product montages using the 7-second format", "Leverage the hashtag #summeranthem for product discovery"],
            "avoid": ["Don't over-produce - the charm is simplicity and raw energy", "Don't wait more than 48 hours - anthem audio saturates fast", "Don't use without checking audio licensing for commercial accounts"]
        },
        "content": {"zh": {
            "what": "Josh Fawaz混音版Madonna经典「Like a Prayer」被TikTok创作者集体封为「2026非官方夏季圣歌」。格式极简：录7秒视频对着镜头唱，叠加文字「2026 Summer Anthem」，打上#summeranthem标签，发布。没有B-roll，没有剧情，没有创意门槛。",
            "data": "音频使用量72小时内暴涨680%。小型创作者（粉丝<1万）报告首次尝试即获百万级播放量。#summeranthem标签累计播放已破8亿。该音频目前是TikTok全球使用量Top 3之一。日均新视频产出超20万条。",
            "analysis": "「Summer Anthem」现象的底层逻辑是「集体仪式感经济」——每年夏天TikTok社区都会自发选举一首「夏季圣歌」，参与即归属。Madonna原曲自带的怀旧情感（跨代际共鸣）+ Josh Fawaz混音的现代节奏感 = 完美的情感钩子。从创作者经济角度：这是罕见的「零门槛百万播放」机会，但圣歌类音频的生命周期极短（通常2周内饱和）。",
            "takeaway": "创作者：如果你还没发，现在立刻拍一条——7秒，不需要准备。这是目前TikTok上投入产出比最离谱的格式。卖家：用这个音频作为任何夏季产品视频的背景音，蹭音频流量红利。品牌方：品牌账号直接参与，零成本获取品牌曝光——但必须在48小时内行动。"
        }}
    },
    {
        "id": "us-053", "date": today,
        "badge": "Hot Trending", "badgeClass": "tag-us",
        "title_zh": "Product Demo Proof：TikTok Shop从「说」到「证」的营销革命",
        "title_en": "Product Demo Proof: TikTok Shop's Marketing Revolution from Tell to Show",
        "summary_zh": "「展示它有效」取代「解释为什么有效」成为TikTok Shop第一转化公式。对比测试+耐久性验证+可洗性证明三层叠加，让产品自己说话。",
        "summary_en": "Show it works replaces explain why it works as TikTok Shop's #1 conversion formula. Contrast test + durability proof + washability demo creates products that sell themselves.",
        "stats": {"heat": "6.8M views/day", "growth": "+250%"},
        "trend": [20, 28, 38, 50, 62, 75, 88, 100, 96],
        "phase": "mature", "phase_zh": "成熟期",
        "difficulty": 2, "window": "Evergreen", "cpm": "$15-30",
        "actions": {
            "creator": ["Film real-time product tests with genuine reactions", "Create proof stack videos: contrast - durability - washability - verdict", "Do comparison videos: cheap vs expensive with visible proof"],
            "brand": ["Shift UGC briefs from feature-listing to proof-demonstration", "Send products to creators with specific test scenarios", "Create branded put it to the test series"],
            "seller": ["Film every product being tested, stained, stretched, and recovered", "Use split-screen before/after as thumbnail hooks", "Include urgency elements after proof demonstration"],
            "avoid": ["Never fake a demo result - audiences are forensic", "Don't over-explain - let the visual proof carry the message", "Avoid studio lighting that makes results look artificial"]
        },
        "content": {"zh": {
            "what": "TikTok Shop营销正在经历一场静默革命：「Product Demo Proof」（产品实证展示）取代了传统的功能介绍和口播种草。核心变化：不再「告诉观众为什么好」，而是「让观众亲眼看到好」。有效的证明叠加公式：对比-鲜艳度测试-耐久性测试-可洗性测试-包装展示-紧迫感。",
            "data": "使用「实证展示」格式的TikTok Shop视频，平均转化率比传统口播高3.8倍。带有明确before/after对比的视频，完播率高出均值47%。该格式在美妆、清洁用品、厨房工具三个品类表现最强，合计贡献TikTok Shop日GMV的28%。",
            "analysis": "「从说到证」的转变反映了消费者信任结构的根本性变化。在信息过载时代，观众对「口说」的信任已降至历史最低。但「眼见为实」的心理机制无法被通胀：当你亲眼看到一个产品在极端测试中表现优异，大脑会绕过理性分析直接建立信任。从平台经济角度：TikTok Shop的核心挑战是「从娱乐场景转化为购买场景」——Product Demo Proof完美解决了这个问题。",
            "takeaway": "创作者：学会「proof stacking」技术——单一证据弱，多重证据叠加后信任感指数级增长。卖家：重新审视所有产品视频——如果还在「说」而不是「证」，立刻转型。品牌方：给UGC创作者的Brief从「请介绍5个优点」改为「请用3个场景测试我们的产品」。"
        }}
    },
    {
        "id": "us-054", "date": today,
        "badge": "Hot Trending", "badgeClass": "tag-us",
        "title_zh": "Deep Sea Diver舞蹈挑战：全民可参与的娱乐变现引擎",
        "title_en": "Deep Sea Diver Dance Challenge: The All-Inclusive Entertainment Monetization Engine",
        "summary_zh": "「Deep Sea Diver」舞蹈挑战因极高包容性爆火——可正常跳、夸张跳、让宠物跳、让玩偶跳，任何人/物都能参与，成为品牌激活的完美载体。",
        "summary_en": "Deep Sea Diver dance challenge goes viral for extreme inclusivity. Anyone or anything can join, making it the perfect brand activation vehicle.",
        "stats": {"heat": "5.4M views/day", "growth": "+310%"},
        "trend": [8, 15, 25, 38, 52, 68, 82, 95, 100],
        "phase": "surging", "phase_zh": "爆发期",
        "difficulty": 1, "window": "2-3 weeks", "cpm": "$6-14",
        "actions": {
            "creator": ["Do the dance then create who wore it better with pets/objects", "Film reaction videos to the best/worst attempts", "Create compilations of unexpected participants (grandma, baby, cat)"],
            "brand": ["Have your brand mascot do the dance via stop-motion", "Launch employee dance challenge for employer branding", "Sponsor a best Deep Sea Diver competition with prizes"],
            "seller": ["Feature products dancing via stop-motion for visibility", "Use the audio for energetic product reveal videos", "Create pet-themed merch tie-ins"],
            "avoid": ["Don't force corporate vibes into a fun format", "Avoid over-choreographed versions - imperfection is the charm", "Don't use without the original audio"]
        },
        "content": {"zh": {
            "what": "「Deep Sea Diver」成为本周TikTok最火舞蹈挑战，但爆火原因不是舞蹈本身多精彩，而是其极端的包容性设计：你可以正常跳、夸张跳、让猫跳、让毛绒玩具跳、让奶奶跳。任何人、任何物体都可以「参与」。",
            "data": "音频使用量周增长310%，日均新视频超8万条。宠物版本平均播放量比人类版本高2.5倍。玩偶/物品版本比人类版本高1.8倍。品牌账号参与率达到近6个月最高水平。该挑战跨越了所有年龄段和粉丝量级。",
            "analysis": "「Deep Sea Diver」的成功揭示了2026年舞蹈挑战的进化方向：从「模仿精确度」转向「创意改编度」。新一代挑战设计为「框架+自由度」——给你一个基本动作框架，但鼓励用任何方式重新诠释。这大幅扩大了参与者基数，而参与者基数直接决定了趋势的病毒传播力。从品牌角度：极高的参与度+极低的创意门槛=品牌激活的完美载体。",
            "takeaway": "创作者：差异化在于「谁/什么来跳」——让宠物、产品、奶奶来跳，播放量会远超本人跳。卖家：用定格动画让产品「跳舞」，曝光效果比硬广高5倍且无广告感。品牌方：这是难得的「零违和感品牌参与」机会。"
        }}
    },
    {
        "id": "us-055", "date": today,
        "badge": "Hot Trending", "badgeClass": "tag-us",
        "title_zh": "Summerween美学：恐怖+夏日的反季节内容金矿",
        "title_en": "Summerween Aesthetic: The Counter-Seasonal Content Goldmine of Horror + Summer",
        "summary_zh": "「Summerween」将万圣节的诡异美学与夏日温暖场景混搭，创造出全新视觉语言——spooky summer正在从亚文化走向主流，时尚/饮品/家居/旅行多品类共振。",
        "summary_en": "Summerween blends Halloween's eerie aesthetic with warm summer scenes. Spooky summer moves from subculture to mainstream across fashion, beverages, home decor, and travel.",
        "stats": {"heat": "3.8M views/day", "growth": "+190%"},
        "trend": [5, 10, 18, 28, 40, 55, 70, 85, 100],
        "phase": "emerging", "phase_zh": "萌芽期",
        "difficulty": 2, "window": "All summer", "cpm": "$8-18",
        "actions": {
            "creator": ["Create summerween aesthetic content: warm visuals + eerie audio + spooky overlay", "Film spooky summer outfit checks or drink recipes", "Start a summerween content series for consistent posting"],
            "brand": ["Launch limited spooky summer product colorways or packaging", "Partner with horror-aesthetic creators for unexpected brand collabs", "Create summerween-themed social content for standing out"],
            "seller": ["Curate summerween product bundles (gothic summer items)", "List black/dark summer clothing with summerween positioning", "Create spooky summer home decor collections"],
            "avoid": ["Don't go too dark - the charm is the contrast with summer warmth", "Avoid actual gore or disturbing content", "Don't force it if your brand has no natural connection"]
        },
        "content": {"zh": {
            "what": "「Summerween」（夏日万圣节）是一个正在从TikTok亚文化走向主流的美学运动：将万圣节的诡异/哥特元素与夏季的温暖场景进行混搭，创造出一种「温暖中的诡异」视觉语言。用户收集夏季素材-添加诡异音乐-标注summerween或spooky summer。",
            "data": "#summerween标签播放量周增长190%，累计播放超2亿。跨越多个品类：时尚（黑色夏装/哥特泳衣增长220%）、饮品（黑色柠檬水/烟雾鸡尾酒增长180%）、家居（暗色调夏日装饰增长150%）、旅行（诡异目的地打卡增长200%）。核心受众：18-30岁，女性占72%。",
            "analysis": "「Summerween」的崛起反映了一个深层消费心理：年轻消费者对「标准化夏日美学」产生了审美疲劳，需要差异化的自我表达方式。万圣节美学天然具有反叛性和独特性，将其嫁接到夏季场景中制造了一种「熟悉中的陌生感」——这正是病毒传播的核心机制。从商业角度：这是一个「反季节」机会——当所有品牌都做标准夏季营销时，Summerween获得了极低的竞争成本和极高的辨识度。",
            "takeaway": "创作者：Summerween是少见的「长周期」趋势（整个夏天都适用），适合做系列内容建立个人品牌。卖家：黑色/哥特风夏季产品目前竞争极低但需求增长快——黑色泳衣、暗色调太阳镜、哥特风防晒伞都是蓝海品类。品牌方：如果品牌调性偏暗/独立/另类，这是天赐的夏季营销差异化机会。"
        }}
    }
]

# ========== EU ==========
eu_data = [
    {
        "id": "eu-051", "date": today,
        "badge": "Hot Trending", "badgeClass": "tag-eu",
        "title_zh": "音乐节内容爆发：欧洲夏季最大流量引擎启动",
        "title_en": "Festival Content Explosion: Europe's Biggest Summer Traffic Engine Fires Up",
        "summary_zh": "Download Festival、Parklife、Isle of Wight等欧洲顶级音乐节集中开启，音乐节穿搭/微Vlog/朋友群像三大内容赛道同步爆发，驱动时尚+美妆+旅行跨品类增长。",
        "summary_en": "Download Festival, Parklife, Isle of Wight top European festivals launch simultaneously. Festival fits, micro-vlogs, and friend group content explode across fashion, beauty, and travel.",
        "stats": {"heat": "9.5M views/day", "growth": "+380%"},
        "trend": [10, 18, 30, 45, 62, 78, 90, 100, 95],
        "phase": "surging", "phase_zh": "爆发期",
        "difficulty": 2, "window": "8-10 weeks", "cpm": "$10-20",
        "actions": {
            "creator": ["Film festival fit checks with outfit details and links", "Create day-in-my-life micro-vlogs at festivals", "Post friend group photo dump narratives with trending audio"],
            "brand": ["Sponsor festival creators for on-site brand activation", "Launch festival-exclusive product drops or colorways", "Create virtual festival experiences for non-attendees"],
            "seller": ["Stock festival essentials: glitter, body chains, rain ponchos, portable chargers", "Bundle festival survival kits with curated product mixes", "List waterproof bags and fanny packs with festival positioning"],
            "avoid": ["Don't post heavily edited content - raw authenticity wins", "Avoid promoting alcohol irresponsibly", "Don't gate-keep - inclusive festival content performs better"]
        },
        "content": {"zh": {
            "what": "6月是欧洲音乐节季的核心月份：Download Festival（英国摇滚）、Isle of Wight Festival（英国综合）、Parklife Festival（曼彻斯特电子/嘻哈）等顶级音乐节集中开启。音乐节内容已成为TikTok每年夏季最大的美学驱动力——同时影响时尚、美妆、友情内容、旅行行为和创作者叙事。",
            "data": "音乐节相关内容日均播放量超9.5M（欧洲区），周增长380%。穿搭检查类视频平均播放量是日常穿搭的4.2倍。旅行微Vlog格式在音乐节场景下完播率达62%。音乐节相关商品（面部亮片/身体链/雨衣/便携充电器）销售周增长超300%。",
            "analysis": "音乐节内容的爆发力来自三个维度的叠加：第一，「限时稀缺性」——FOMO驱动非参与者的内容消费欲；第二，「多品类共振」——一个音乐节同时驱动时尚、美妆、旅行、社交四个内容赛道；第三，「真实感溢价」——音乐节环境天然产出真实内容，完美契合2026年「反精致化」的平台审美。从品牌角度：音乐节是「场景化营销」的极致——产品不是被广告，而是被「使用」。",
            "takeaway": "创作者：音乐节内容窗口长达8-10周，建议做系列：节前（准备）-节中（实拍）-节后（回顾）。卖家：音乐节必备清单现在上架正当时，整个夏天都有稳定需求。品牌方：赞助音乐节现场创作者是ROI最高的夏季营销之一。"
        }}
    },
    {
        "id": "eu-052", "date": today,
        "badge": "Hot Trending", "badgeClass": "tag-eu",
        "title_zh": "Olivia Rodrigo新专辑明日发行：定义2026伤感女孩夏天",
        "title_en": "Olivia Rodrigo New Album Drops Tomorrow: Defining 2026's Sad Girl Summer",
        "summary_zh": "Olivia Rodrigo第三张专辑「you seem pretty sad for a girl so in love」6月12日全球发行，预计将成为2026夏季TikTok配乐主力，「伤感女孩夏天」美学即将席卷全平台。",
        "summary_en": "Olivia Rodrigo's third album drops globally June 12. Expected to dominate 2026 summer TikTok soundtracks as Sad Girl Summer aesthetic sweeps the platform.",
        "stats": {"heat": "7.2M views/day", "growth": "+520%"},
        "trend": [8, 15, 28, 42, 60, 78, 92, 100, 100],
        "phase": "emerging", "phase_zh": "萌芽期",
        "difficulty": 1, "window": "6-8 weeks", "cpm": "$8-16",
        "actions": {
            "creator": ["Prepare reaction/first listen content for June 12 release", "Create sad girl summer aesthetic content using album tracks", "Film emotional storytelling videos matched to new audio"],
            "brand": ["Prepare summer campaigns aligned with emotional/vulnerable aesthetics", "Partner with lifestyle creators for album-soundtrack branded content", "Create playlist-style product recommendations matched to album moods"],
            "seller": ["Stock sad girl aesthetic products (journaling supplies, candles, comfort items)", "List vinyl/CD pre-orders and album merchandise", "Bundle self-care products with sad girl summer positioning"],
            "avoid": ["Don't trivialize mental health themes in the album", "Avoid using audio without checking commercial licensing", "Don't force cheerful brand messaging against the album's emotional tone"]
        },
        "content": {"zh": {
            "what": "Olivia Rodrigo第三张录音室专辑「you seem pretty sad for a girl so in love」将于6月12日（明天）全球发行。作为Z世代最具影响力的音乐人之一，她的新专辑预计将直接定义2026年夏季TikTok的情感基调——「Sad Girl Summer」美学即将全面席卷。",
            "data": "专辑预热期Olivia Rodrigo相关内容在TikTok日均播放量达720万次，周增长520%。上一张专辑「GUTS」发行时产出超过1200万条UGC视频。本次新专辑在欧洲市场的粉丝基数已较上一张专辑增长80%。",
            "analysis": "「Olivia Rodrigo效应」的底层逻辑是「情感共振经济」——她的音乐精准捕捉了Z世代的情感状态，粉丝用她的音频配自己的故事。从创作者经济角度：新专辑发行=音频红利爆发，率先使用新音频的创作者获得算法初期流量倾斜。从品牌角度：Olivia的受众画像极精准（16-28岁女性），是美妆、时尚、生活方式品牌的核心人群。",
            "takeaway": "创作者：明天专辑发行日是黄金24小时——立刻做First Listen Reaction或用新音频配内容。整个夏天都可以持续用不同曲目做内容。卖家：「Sad Girl Summer」相关产品在未来6-8周持续增长。品牌方：如果目标受众是16-28岁女性，现在就准备Olivia Rodrigo音频相关的品牌内容策略。"
        }}
    },
    {
        "id": "eu-053", "date": today,
        "badge": "Hot Trending", "badgeClass": "tag-eu",
        "title_zh": "Padel板网球席卷欧洲：运动社交新贵的商业爆发",
        "title_en": "Padel Sweeps Europe: The Commercial Explosion of the New Social Sport",
        "summary_zh": "Padel（板网球）作为欧洲增速最快的运动项目，在TikTok上的内容量6月暴涨280%。「夏季准备+运动社交+轻奢生活方式」三标签叠加，驱动装备/场馆/服装全链条增长。",
        "summary_en": "Padel, Europe's fastest-growing sport, sees 280% content surge on TikTok in June. Summer prep + social sport + premium lifestyle triple-tag drives growth across equipment, venues, and apparel.",
        "stats": {"heat": "4.6M views/day", "growth": "+280%"},
        "trend": [12, 20, 30, 42, 55, 68, 80, 92, 100],
        "phase": "emerging", "phase_zh": "萌芽期",
        "difficulty": 2, "window": "All summer", "cpm": "$10-22",
        "actions": {
            "creator": ["Create padel beginner guides and trick shot compilations", "Film padel social lifestyle vlogs (sport + brunch + friends)", "Do gear reviews and court comparisons"],
            "brand": ["Sponsor padel creators for authentic sport-lifestyle content", "Launch padel-specific product lines (eyewear, activewear, drinks)", "Host brand-sponsored padel tournaments or social events"],
            "seller": ["Stock padel rackets, balls, grips, and accessories", "Bundle padel starter kits for beginners", "List padel-adjacent lifestyle products (sport sunglasses, grip bags)"],
            "avoid": ["Don't position padel as elitist - accessibility is its growth driver", "Avoid comparing to tennis dismissively", "Don't ignore the social/lifestyle angle - pure sport content underperforms"]
        },
        "content": {"zh": {
            "what": "Padel（板网球）是一种介于网球和壁球之间的拍类运动，场地更小、规则更简单、社交属性更强。它已成为欧洲增速最快的运动——在西班牙有超过600万玩家，英国、意大利、瑞典的球场数量2025-2026年翻倍增长。6月进入夏季后，Padel在TikTok上的内容量暴涨280%。",
            "data": "Padel相关TikTok内容日均播放量460万（欧洲区），6月周增长280%。欧洲Padel装备市场2026年预估规模12亿欧元，同比增长45%。英国球场建设增速达120%。TikTok上Padel内容互动率是常规运动内容的2.3倍。Padel装备在TikTok Shop欧洲站销售增长超200%。",
            "analysis": "Padel的爆发遵循了经典的「社交运动病毒传播」路径：低门槛入门-社交场景驱动-生活方式身份认同-装备消费升级。在TikTok上，Padel内容的成功关键不是专业技术展示，而是「运动社交生活方式」的展示——朋友们一起打球-然后去喝brunch-周末生活方式。Padel是「新中产运动」定位，受众具有高消费力（25-45岁城市中产），品牌价值极高。",
            "takeaway": "创作者：Padel内容在欧洲市场竞争度还很低——现在入场做「Padel生活方式」博主有巨大先发优势。关键：不要只拍打球，要拍完整生活场景。卖家：初学者套装客单价100-200欧元区间最好出量。品牌方：赞助Padel赛事/达人/场馆，能快速建立「活力+社交+品质」的品牌联想。"
        }}
    },
    {
        "id": "eu-054", "date": today,
        "badge": "Hot Trending", "badgeClass": "tag-eu",
        "title_zh": "Micro-Vlog微纪录：反精致主义的夏日叙事革命",
        "title_en": "Micro-Vlog Aesthetic: The Anti-Polished Summer Narrative Revolution",
        "summary_zh": "景观式微Vlog成为欧洲TikTok夏季内容的主导叙事方式——火车旅行/咖啡日常/音乐节记录，观察性+社交原生取代精修纪实，真实感成为最大流量密码。",
        "summary_en": "Landscape micro-vlogs dominate European TikTok summer content. Observational + socially native replaces polished documentary as authenticity becomes the ultimate traffic code.",
        "stats": {"heat": "6.1M views/day", "growth": "+220%"},
        "trend": [15, 22, 32, 44, 58, 70, 82, 93, 100],
        "phase": "mature", "phase_zh": "成熟期",
        "difficulty": 1, "window": "All summer", "cpm": "$6-14",
        "actions": {
            "creator": ["Film spontaneous moments throughout your day - don't plan shots", "Use trending audio as subtle background, not as the focus", "Post daily micro-vlogs documenting small summer moments"],
            "brand": ["Commission creators for unscripted day-in-the-life content", "Shift from polished ads to observational content for organic reach", "Create a summer day with brand series with real creators"],
            "seller": ["Feature products being naturally used in micro-vlog settings", "Create atmospheric product videos with lo-fi summer aesthetics", "Use train/cafe/city walk settings for lifestyle product placement"],
            "avoid": ["Don't over-edit or color-grade heavily - rawness is the point", "Avoid scripted voiceovers - ambient sound or trending audio only", "Don't force product placement - it breaks the authentic vibe"]
        },
        "content": {"zh": {
            "what": "「Micro-Vlog」（微纪录）是一种高度随性的短视频叙事风格——不是精心策划的Vlog，而是对日常瞬间的即兴记录：火车窗外的风景、咖啡馆的午后、朋友间的碎片对话、音乐节的片段、周末的城市漫步。它强调「观察性」而非「表演性」。",
            "data": "Micro-Vlog格式在欧洲TikTok日均播放量超610万，6月周增长220%。该格式的完播率均值达58%。使用该格式的创作者粉丝增长率比同期高1.8倍。品牌使用micro-vlog风格的内容互动率高出传统广告3.2倍。",
            "analysis": "微纪录的崛起是2026年「反精致主义」浪潮的集中体现。信息过载时代，精心制作的内容不再稀缺，反而是「真实的、未经加工的、不完美的」瞬间变得稀缺且珍贵。欧洲夏季的场景天然适合这种叙事风格。从品牌传播角度：消费者对品牌的信任正从「信息传递」转向「氛围传递」——一个在微纪录中自然出现的产品比任何口播都更有说服力。",
            "takeaway": "创作者：微纪录是目前创作门槛最低但回报最高的格式——只需一部手机和观察力。关键：不要「为了拍而做」，而是「正在做然后顺便拍」。卖家：让产品自然出现在微纪录场景中——场景化的产品展示比白底图效果好10倍。品牌方：把Brief从「请介绍产品」改为「带着产品过一天吧」。"
        }}
    },
    {
        "id": "eu-055", "date": today,
        "badge": "Hot Trending", "badgeClass": "tag-eu",
        "title_zh": "Going Analog数字排毒：屏幕疲劳时代的反向消费浪潮",
        "title_en": "Going Analog Digital Detox: The Counter-Consumption Wave in the Age of Screen Fatigue",
        "summary_zh": "「走向模拟」运动在欧洲年轻用户中持续升温——手账日记/胶片摄影/阅读/手工爱好成为新社交货币，「刻意离线」从生活方式升级为消费决策驱动力。",
        "summary_en": "Going Analog movement grows among young European users. Bullet journals, film photography, reading, crafts become new social currency as intentional offline evolves into consumption driver.",
        "stats": {"heat": "3.9M views/day", "growth": "+175%"},
        "trend": [10, 16, 24, 34, 45, 56, 68, 82, 100],
        "phase": "emerging", "phase_zh": "萌芽期",
        "difficulty": 1, "window": "Long-term trend", "cpm": "$8-16",
        "actions": {
            "creator": ["Document your analog hobbies: journaling setup, film development, reading lists", "Create screen time vs analog time comparison content", "Film ASMR-style analog activity videos (pen on paper, camera clicking)"],
            "brand": ["Position products as part of the intentional living movement", "Create content showing your product enabling offline experiences", "Partner with bookstagrammers and journal creators"],
            "seller": ["Stock analog lifestyle products: journals, fountain pens, film cameras, craft kits", "Bundle digital detox starter kits (journal + pen + book + candle)", "List vintage/retro tech products with analog lifestyle positioning"],
            "avoid": ["Don't ironically promote digital detox on digital platforms without self-awareness", "Avoid being preachy about screen time - aspirational beats judgmental", "Don't sell analog as expensive - accessibility drives adoption"]
        },
        "content": {"zh": {
            "what": "「Going Analog」（走向模拟）是一场正在欧洲年轻用户中加速的生活方式运动：主动选择模拟/离线的方式来替代数字化体验——用手账代替APP记录、用胶片相机代替手机拍照、用纸质书代替电子阅读器、用手工代替刷视频。",
            "data": "「Going Analog」相关内容在欧洲日均播放量390万，6月周增长175%。手账/日记本销售增长130%、胶片相机增长200%、实体书销售增长45%、手工材料包增长160%。核心受众：18-30岁、女性占68%、城市居住、高教育水平、中高收入。",
            "analysis": "「数字排毒」运动的底层驱动力是「注意力疲劳」的集体觉醒。有趣的悖论：这些「反数字化」内容恰恰通过TikTok传播——人们在社交媒体上「展示自己不在社交媒体上」。这不是虚伪，而是「策展式生活」的新形态。从消费角度：「Going Analog」创造了全新消费品类——消费者不是在买笔记本，是在买「手写的仪式感」；不是在买胶片相机，是在买「等待冲洗的期待感」。",
            "takeaway": "创作者：「Going Analog」是长期趋势，适合建立个人IP。关键是展示过程之美——ASMR式的感官内容表现最好。卖家：模拟生活方式产品是高毛利蓝海——消费者为「仪式感」买单的溢价空间在50-200%。品牌方：将品牌与「有意识的生活」关联——不是「产品很好」而是「产品帮你慢下来」。"
        }}
    }
]

# Write files
for region, data in [('china', china_data), ('us', us_data), ('eu', eu_data)]:
    os.makedirs(f'data/{region}', exist_ok=True)
    filepath = f'data/{region}/{today}.json'
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f'Written: {filepath} ({len(data)} articles)')

print('All data files generated successfully!')
