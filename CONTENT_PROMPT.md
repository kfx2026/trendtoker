/* ============================================
   TrendToker — Content Generation Prompt v2.0
   深度分析版 | Deep Analysis Edition
   每日 5 篇/区域 批量生成提示词
   ============================================
   Copy the prompt below and paste into AI.
   Replace [DATE] with today's date.
   Replace [REGION] with: us / china / eu
   ============================================ */

CONTENT_GENERATION_PROMPT="You are a senior TikTok trend analyst and content strategist for TrendToker. Generate 5 deep-analysis trend reports for [DATE] in the [REGION] market.

IMPORTANT RULES:
- All data cited must be based on publicly available information from TikTok Creator Center or credible sources.
- Do NOT generate fake statistics. Use realistic estimates with ranges if exact numbers unavailable.
- DEPTH IS NON-NEGOTIABLE: Each trend must include full deep analysis modules (algorithm, psychology, structure, monetization, cases, lifecycle, niche adaptation).
- Use professional, analytical tone — like a Bloomberg analyst writing about social media economics.
- Chinese content (zh) is the PRIMARY language. English fields are supplementary.

═══════════════════════════════════════════
DATA STRUCTURE — EACH TREND ENTRY:
═══════════════════════════════════════════

{
  \"id\": \"[region]-[###]\",
  \"date\": \"[DATE]\",
  \"badge\": \"Hot Trending\",
  \"badgeClass\": \"tag-[region]\",
  \"title_zh\": \"[中文标题，20-35字，含核心数据或卖点]\",
  \"title_en\": \"[English title, 50-80 chars, journalistic]\",
  \"summary_zh\": \"[中文摘要，2-3句话含关键数据]\",
  \"summary_en\": \"[English summary, 2-3 sentences]\",
  \"stats\": {
    \"heat\": \"[X]M views/day\",
    \"growth\": \"+[X]%\"
  },
  \"trend\": [数组9个数字，模拟30天热度曲线，最高100],
  \"phase\": \"emerging|surging|mature|declining\",
  \"phase_zh\": \"萌芽期|爆发期|成熟期|衰退期\",
  \"difficulty\": [1-5, 制作难度],
  \"window\": \"[时间窗口，如 '10-14 days' 或 'Evergreen']\",
  \"cpm\": \"$[X]-[Y]\",
  \"actions\": {
    \"creator\": [\"3条具体行动建议\"],
    \"brand\": [\"3条品牌行动建议\"],
    \"seller\": [\"3条卖家行动建议\"],
    \"avoid\": [\"3条避坑建议\"]
  },
  \"content\": {
    \"zh\": {
      \"what\": \"[现象描述 150-200字：什么趋势？谁发起？什么形式？具体是什么样的内容？]\",

      \"data\": \"[数据面板 100-150字：日均播放/参与创作者数/增长率/完播率/核心受众画像等硬数据]\",

      \"deep_analysis\": {
        \"algorithm\": \"[算法推荐机理 200-300字：解释TikTok推荐引擎为什么偏爱该内容。涉及完播率权重、互动信号密度、音频热度加速器、内容多样性奖励等具体机制。不要只说'算法偏爱'，要解释WHY。]\",
        \"psychology\": \"[用户心理分析 200-300字：解释观众为什么被吸引。涉及FOMO、社会认同、多巴胺预期、认知失调、注意力捕获等心理学概念。要有编号的多层分析（①②③）。]\",
        \"structure\": \"[最优内容结构 150-200字：给出具体的时间轴/公式/模板。如'前3秒…中间5秒…结尾2秒'。让创作者看完就知道怎么拍。]\"
      },

      \"monetization\": {
        \"cpm_breakdown\": \"[CPM细分分析 100-150字：按品类/格式细分CPM范围，对比同期常规内容，解释溢价原因。]\",
        \"revenue_paths\": \"[变现路径 150-200字：列出3-4条具体变现方式，每条含预估收入范围。如Creator Fund、品牌合作、教程付费、联盟营销等。]\",
        \"brand_pricing\": \"[品牌合作报价参考 100-150字：按粉丝量级给出合作报价范围，含ROI预估。]\"
      },

      \"cases\": [
        {
          \"account\": \"[@账号名（粉丝数，赛道标签）]\",
          \"result\": \"[具体成果数据：播放量、涨粉数、GMV等]\",
          \"strategy\": \"[核心策略复盘：做对了什么？可复制的要素是什么？]\"
        },
        {
          \"account\": \"[第二个案例]\",
          \"result\": \"[具体成果]\",
          \"strategy\": \"[策略复盘]\"
        },
        {
          \"account\": \"[第三个案例]\",
          \"result\": \"[具体成果]\",
          \"strategy\": \"[策略复盘]\"
        }
      ],

      \"lifecycle\": {
        \"historical_comparison\": \"[历史趋势类比 100-150字：找到过去最类似的趋势，对比生命周期规律。如'该趋势与2024年的XXX类似——都是…']\",
        \"decay_prediction\": \"[衰退预测 100-150字：当前处于第几天？预计何时达峰→何时衰退→何时消亡？给出具体天数预估。]\",
        \"optimal_entry\": \"[最佳入场时机 100-150字：现在还来得及吗？分层策略——新手/已入场/迟到者各该怎么做。]\"
      },

      \"niche_adapt\": {
        \"beauty\": \"[美妆类适配 50-80字：该趋势在美妆赛道怎么用？具体到拍什么场景、推什么产品。]\",
        \"food\": \"[美食类适配 50-80字]\",
        \"tech\": \"[科技类适配 50-80字]\",
        \"fashion\": \"[时尚穿搭类适配 50-80字]\",
        \"lifestyle\": \"[生活方式类适配 50-80字]\"
      },

      \"takeaway\": \"[实践启示 150-200字：分创作者/卖家/品牌方三个角色，给出最终结论和行动建议。含窗口期+预期收益。]\"
    }
  }
}

═══════════════════════════════════════════
深度分析写作标准（QUALITY CHECKLIST）:
═══════════════════════════════════════════

□ algorithm 必须解释具体算法机制（完播率权重、流量池突破条件、音频加速器等），不能只说"算法推荐"
□ psychology 必须引用至少2个心理学概念（FOMO、峰终定律、社会认同、多巴胺预期等），有编号层次
□ structure 必须给出可直接执行的时间轴/公式，如"前3秒+中间5秒+结尾2秒"
□ monetization 必须有具体数字范围（$X-Y），不能只说"收入不错"
□ cases 必须有3个不同量级的案例（大号/中号/小号或品牌号），每个含具体数据
□ lifecycle 必须给出天数级别的预测（"第X天达峰"），不能只说"即将衰退"
□ niche_adapt 必须覆盖5个垂类，每个给出具体场景而非泛泛建议
□ takeaway 必须分角色（创作者/卖家/品牌），含时间窗口+预期收益数字

═══════════════════════════════════════════
每日5条趋势选题方向:
═══════════════════════════════════════════

- 2条：爆发期趋势（当周新爆的格式/音频/挑战）
- 1条：成熟期趋势（已验证但仍有机会的常青格式）
- 1条：萌芽期趋势（刚露苗头，有先发优势的新方向）
- 1条：电商/变现相关趋势（TikTok Shop/带货/品牌合作相关）

GENERATE NOW FOR DATE: [DATE], REGION: [REGION]"
