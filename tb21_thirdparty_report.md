# Terminal-Bench 2.1 第三方对比评测数据收集报告(DeepSeek V4 Flash 0731 / GLM-5.2 / Claude Opus 4.8)

**采集方式与可信度声明(必读)**:本会话沙箱**无出站直连网络**(pwsh/Invoke-WebRequest 对 example.com、github.com、huggingface.co 等全部"连接被重置";子代理实测同样失败),故全部数据来自 **web_search 返回的链接标题与摘要片段**(含一次 100+ 次检索的子代理汇总)。凡在标题/摘要中出现过的数字均原样保留并标注来源;页面正文深度的数字(如 PR diff 表格、JS 渲染榜单)列为"未获取到数值"。**没有编造任何数字。**

---

## 一、8 个指定来源逐一核查结果

### 1. GitHub Maka-Agent PR #2208 —— 可访问状态:找到(仅元数据,正文数值未获取)
- URL: https://github.com/Maka-Agent/maka-agent/pull/2208 (diff: https://patch-diff.githubusercontent.com/raw/Maka-Agent/maka-agent/pull/2208.diff)
- 标题原样:"docs(eval): record the four-arm Terminal-Bench 2.1 comparison"(作者 Astro-Han)
- 四个 arm 的模型/配置、各自分数、harness/轮次/工具:**未获取到数值**(正文/diff 无法抓取,搜索引擎无正文索引)
- 佐证(来源同仓):PR #1983 "feat(headless): benchmark three agents on DeepSeek V4 Flash";Issue #1970 "eval(headless): benchmark Maka, Codex, and Claude Code synchronously on DeepSeek V4 Flash"——可推断四臂评测与 Maka/Codex/Claude Code 三 agent × DeepSeek V4 Flash 相关,但具体 arm 构成与分数未获确认: https://github.com/Maka-Agent/maka-agent/pull/1983 、 https://github.com/Maka-Agent/maka-agent/issues/1970

### 2. VentureBeat 文章 —— 可访问状态:找到(标题+转载数值,正文未抓取)
- URL: https://venturebeat.com/orchestration/deepseeks-top-ranked-v4-flash-stumbles-on-real-agent-tasks-as-its-prices-surge
- 标题:"DeepSeek's top-ranked V4 Flash stumbles on real agent tasks as its prices surge"
- 核心数值(来自转载标题):**真实世界任务失败率 46.2%**——KuCoin 转载 "DeepSeek's V4 Flash Fails 46.2% of Real-World Tasks Despite Low Pricing"(https://www.kucoin.com/news/flash/deepseek-s-v4-flash-fails-46-2-of-real-world-tasks-despite-low-pricing);对应通过率 **53.8%**(中文转载 "登顶榜单但实测通过率仅 53.8%", https://followin.io/en/feed/27013318 )
- 是否 Terminal-Bench 2.1:**未能确认**(转载摘要仅写 "real-world tasks",未见任务集名称)
- 涨价背景:最高涨幅 1100%(腾讯新闻/新浪转载)、"V4 Pro 高峰期涨幅达 11 倍"(南方都市报)、"$0.28 Agentic Output Floor"(Yahoo Finance)、"DeepSeek V4 Flash 0731: $0.14/M"(dev.to)

### 3. aicoderscope 六月榜单分析 —— 可访问状态:找到(链接+标题,分数未获取)
- URL: https://aicoderscope.com/blog/terminal-bench-21-june-2026-leaderboard-analysis/ (dev.to 转载: https://dev.to/jovan_chan_9500711396d4e6/terminal-bench-21-in-june-2026-the-1-model-is-one-you-cant-use-heres-the-leaderboard-that-4074 )
- 标题:"Terminal-Bench 2.1 in June 2026: The #1 Model Is One You Can't Use — Here's the Leaderboard That Actually Matters"(2026 年 6 月)
- "#1 模型"所指、各模型分数(Opus 4.8/GLM-5.2/DeepSeek V4)、评测环境:**未获取到数值**(正文无法抓取)

### 4. codingfleet 2026 榜单 —— 可访问状态:找到(链接+标题,榜单分数未获取)
- URL: https://codingfleet.com/blog/terminal-bench-leaderboard-2026/
- 标题:"Terminal-Bench 2.1 Leaderboard 2026: AI Models Ranked by CLI Coding"
- 榜单具体分数与指标(pass@1):**未获取到数值**
- 同站关联文章:"Claude Opus 4.8 vs GLM-5.2: 0.7 Points From the Coding King at 1/6 the Price"——GLM-5.2 距 Opus 4.8 **差 0.7 分**、价格为 **1/6**(https://codingfleet.com/blog/claude-opus-4-8-vs-glm-5-2/;未确认是否 TB2.1 口径)

### 5. llm-stats 榜单页 —— 可访问状态:找到(链接,分数未获取)
- URL: https://llm-stats.com/benchmarks/terminal-bench-2.1 (模型页 https://llm-stats.com/models/deepseek-v4-flash-vision-exp ;博客 https://llm-stats.com/blog/research/claude-opus-4-8-launch 、 https://llm-stats.com/blog/research/glm-5-2-vs-claude-opus-4-8 )
- Opus 4.8 / GLM-5.2 / DeepSeek V4 Flash 分数:**未获取到数值**(JS 渲染页,摘要无数字)

### 6. blackbox.ai 复测 —— 可访问状态:找到(链接+标题,Opus 4.8 = 90% pass@1)
- URL: https://www.blackbox.ai/blog/tb-v2-1-blackbox-gpt-5-6-sol-opus-4-8
- 标题原样:"TB v2.1 Blackbox — GPT-5.6 Sol + Opus 4.8 (**90% pass@1**)"——**Claude Opus 4.8 在 TB v2.1 复测 = 90% pass@1**
- GPT-5.6 Sol 同测成绩、复测配置(harness、轮次、工具、是否 Claude Code 原生/官方 API):**未获取到数值**

### 7. HuggingFace 数据集 cody-vi4/tbench-2-1-cody-opus48 —— 可访问状态:找到(页面/README/commit,README 内容未获取)
- URL: https://huggingface.co/datasets/cody-vi4/tbench-2-1-cody-opus48 (README: https://huggingface.co/datasets/cody-vi4/tbench-2-1-cody-opus48/blob/main/README.md )
- 已知:license **apache-2.0**;commit "Upload README.md with huggingface_hub"(2a8fc21)、"Add files using upload-large-folder tool"(6c2bcba);含 COMPLIANCE.md
- README 中记录的 Opus 4.8 分数与配置(harness/轮次/工具):**未获取到数值**

### 8. orcarouter "Qwen 3.8 vs GLM-5.2" —— 可访问状态:找到(链接+标题)
- URL: https://www.orcarouter.ai/blog/qwen-3-8-vs-glm-5-2
- 标题原样:"Qwen 3.8 vs GLM-5.2: **86.6 vs 82.7** on Terminal-Bench"——按标题顺序:Qwen 3.8 = **86.6**,GLM-5.2 = **82.7**
- 是否 Terminal-Bench **2.1**:**未能确认**(标题仅写 "Terminal-Bench")
- 82.7 是否 GLM-5.2:按标题序最直接解读为是,但无正文佐证;评测环境(harness、agent 形态、是否原生):**未获取到数值**
- 关联文章: https://www.orcarouter.ai/blog/o3-vs-glm-5-2 ("o3 vs GLM 5.2: Open-Weight Model Beats Retiring Flagship")、 https://www.orcarouter.ai/blog/glm-5-5-vs-qwen-3-8

---

## 二、每模型分数清单(分数、指标、来源、日期、环境、官方/第三方)

### DeepSeek V4 Flash (0731)
| 数值 | 指标 | 来源 URL | 日期 | 评测环境 | 性质 |
|---|---|---|---|---|---|
| **82.7%** | 未明示(疑 TB 通过率) | aitoolsrecap 文章标题("$0.14/M, Terminal-Bench 82.7%",见于子代理检索) | 2026-08 前后 | 未注明 | 第三方 |
| **完成率 67.42→82.02(+14.61%)** | 完成率 | autoprompt-skill 仓库: https://raw.githubusercontent.com/Spielewoy/autoprompt-skill/main/docs/benchmarks/terminal-bench-2.1.md (jdon/仓库摘要转述) | 2026 | TB2.1 + coding skill(工具增强) | 第三方 |
| **46.2% 失败 / 53.8% 通过** | 真实任务通过率 | KuCoin: https://www.kucoin.com/news/flash/deepseek-s-v4-flash-fails-46-2-of-real-world-tasks-despite-low-pricing ;followin: https://followin.io/en/feed/27013318 | 2026-08 | "real-world agent tasks"(任务集未确认,未知是否 TB2.1) | 第三方(媒体实测,转述自 VentureBeat) |
| **54.4 分** | DeepSWE(agentic SWE) | BlockBeats 转述(子代理检索) | 2026 | DeepSWE 基准 | 第三方 |
| **46 分** | SuperCLUE-Terminal(中文终端,非 TB) | 子代理检索 | 2026 | 中文终端编程测评 | 第三方 |
| **50 分(+10 vs 前版)** | artificialanalysis 智能指数 | artificialanalysis(子代理检索) | 2026 | 非 Terminal-Bench | 第三方 |
| 官方发布背景 | —— | InfoQ:"DeepSeek V4 Flash 0731 发布:Agent 能力反超 Pro Preview,开源模型前三易主"( https://xie.infoq.cn/article/ce3ac43042f3ec16db28d876f );DeepSeek 官方 news: https://api-docs.deepseek.com/news/news260821/ | 2026-08 | —— | 官方发布 |

### GLM-5.2
| 数值 | 指标 | 来源 URL | 日期 | 评测环境 | 性质 |
|---|---|---|---|---|---|
| **82.7** | 未明示 | https://www.orcarouter.ai/blog/qwen-3-8-vs-glm-5-2 (标题"86.6 vs 82.7 on Terminal-Bench") | 2026 | 未注明(TB 版本/是否原生未确认) | 第三方 |
| **81 分** | TB2.1 榜单分 | yun88 "Terminal-Bench 2.1 榜单解读:GLM-5.2 拿下 81 分,离 Claude Opus 4.8 还差多远"(子代理检索) | 2026 | TB2.1 | 第三方 |
| **距 Opus 4.8 差 0.7 分,价 1/6** | 编码对比 | https://codingfleet.com/blog/claude-opus-4-8-vs-glm-5-2/ | 2026 | 编码基准(是否 TB2.1 未确认) | 第三方 |
| **与 V4 Flash 差距 1.7 分,换 harness 后消失** | TB 类基准 | Towards AI "DeepSeek V4-Flash vs GLM-5.2: The 1.7-Point Win Collapses When You Swap the Harness"(子代理检索) | 2026 | 双 harness 对照 | 第三方 |
| 官方发布/官方基准 | —— | zai-org GLM-5.2( https://lambda.ai/inference-models/zai-org/glm-5.2 );"Official GLM-5.2 coding benchmarks"( https://featherless.ai/blog/whats-new-in-glm-5-2-run-it-on-featherless );glm5.app/blog/glm-5-2-benchmarks | 2026-06-17 发布 | 官方 | 官方发布 |

### Claude Opus 4.8
| 数值 | 指标 | 来源 URL | 日期 | 评测环境 | 性质 |
|---|---|---|---|---|---|
| **90% pass@1** | pass@1 | https://www.blackbox.ai/blog/tb-v2-1-blackbox-gpt-5-6-sol-opus-4-8 (标题) | 2026 | TB v2.1;blackbox.ai 复测;harness/轮次/工具未披露 | 第三方复测 |
| **五项基准"全输"**、价格贵 **57.1 倍** | 5 项基准综合 | GeekPark: https://w.geekpark.net/news/368637 ("贵 57.1 倍的 Claude Opus 4.8 五项全输,赢它的不是模型,是 Harness";Floatboat 浮舟 harness 击败 Opus 4.8;HLR 区间 0.26~1.42x) | 2026(约 6 月) | Floatboat harness vs 原生 | 第三方复测 |
| 官方榜单跟踪 | —— | 官方 tbench.ai: https://www.tbench.ai/leaderboard/terminal-bench/2.1?models=Codex+CLI+%2B+GPT-5.5,Claude+Code+%2B+Opus+4.8 (跟踪 Claude Code + Opus 4.8,具体分数未取到);Vals AI: https://www.vals.ai/benchmarks/terminal-bench-2-1?suggested=open-weights-table | 2026 | 官方主持人榜/第三方平台 | 官方榜单(分数未获取) |
| StateM 论文基线 | 95.3% 为该 harness+模型;Opus 单项未取到 | arXiv 2608.15089v1: https://arxiv.org/abs/2608.15089v1 | 2026-08 | harness scaling,$15 run | 第三方学术 |

---

## 三、"同模型不同环境"分数差(环境偏差分析核心)

**DeepSeek V4 Flash 0731**(同一模型,不同环境/集合):
- 82.7%(TB,如确认为该口径)→ 53.8% 通过率(VentureBeat 真实任务)→ 46(SuperCLUE-Terminal)→ 54.4(DeepSWE)→ 50(AA 指数)→ 完成率 67.42→82.02(TB2.1 + coding skill)。
- 偏差来源:**任务集不同 + harness/工具不同**;最高分(82.7)与最低(46)相差约 **36 分**。

**GLM-5.2**:
- 82.7(orcarouter,未确认 2.1)→ 81(yun88,TB2.1)→ 距 Opus 4.8 0.7 分(codingfleet)→ 对 V4 Flash 的 1.7 分优势"换 harness 即消失"(Towards AI)。
- 偏差来源:**榜单口径与 harness 差异**;82.7 vs 81 差 1.7 分(与 Towards AI 标题巧合一致)。

**Claude Opus 4.8**:
- 90% pass@1(blackbox 复测,TB v2.1)→ 五项全输(GeekPark/Floatboat harness 对比,5 项含 TB 类,具体分数未取到)。
- 偏差来源:**harness 决定论**——同模型在 blackbox 复测登顶、在 Floatboat 对照中输给另一 harness 组合;价格贵 57.1 倍。

**harness 效应旁证**(非单模型,但直接支撑环境偏差):
- "同一个模型差 20 分:DeepSeek 的 harness 依赖性和合成数据的隐藏天花板"(yage.ai);dev.to "The harness, not the model, moved DeepSeek's score by twenty tasks"
- Maka+同款 Kimi K3 第三方 harness 反超官方 KimiCode **10 个百分点**( https://www.80aj.com/2026/07/19/harness-maka-kimi-k3/ ;https://ai-coding.wiselychen.com/local-first-model-needs-local-first-harness/ )
- DeepSeek V4 Flash 换 **8 套 harness**:Pi agent 成功率最高且最省钱、Claude Code 最快但最贵(ChainThink/BlockBeats 转述)
- Composio/Ante 组合成功率 **47%–67%**;Ante(15MB Rust agent)自称 TB2.1 **82.7%**(AI Weekly 转述)——注意与 GLM-5.2(82.7)、V4 Flash(82.7%)数值撞车,疑为不同口径巧合,需正文核实
- StateM 论文以 **harness scaling** 在 TB2.1 达 **95.3%** raw accuracy

---

## 四、官方发布 vs 第三方复测区分

**官方发布/官方基准**:
- DeepSeek V4 Flash 0731 官方发布:DeepSeek API docs( https://api-docs.deepseek.com/news/news260821/ )与 InfoQ 报道;涨价最高 1100% 为媒体转述官方调价。
- GLM-5.2 官方:zai-org( https://lambda.ai/inference-models/zai-org/glm-5.2 )、官方 coding benchmarks(featherless/glm5.app 转载官方数据);2026-06-17 发布(凤凰网/DoNews)。
- Anthropic Opus 4.8 官方发布:2026 年 5-6 月(eweek: https://www.eweek.com/news/anthropic-claude-opus-4-8-ai-honesty/ ;agentbreaking/comparedge 评测)。
- 官方 Terminal-Bench 2.1 榜单:tbench.ai( https://www.tbench.ai/leaderboard/terminal-bench/2.1 )——具体分数本次未取到。

**第三方复测/社区跑分**:
- Blackbox(Opus 4.8 = 90% pass@1)、VentureBeat(V4 Flash 46.2% 失败)、Vals AI、codingfleet、aicoderscope、orcarouter(GLM-5.2 82.7)、llm-stats、GeekPark/Floatboat(Opus 4.8 五项全输)、StateM(harness scaling)、autoprompt-skill(V4 Flash + skill 67.42→82.02)、SuperCLUE、DeepSWE、artificialanalysis、Maka-Agent PR #2208(开源 harness 项目内部四臂对比)、HF cody-vi4/tbench-2-1-cody-opus48(社区数据集)。

---

## 五、未找到/无法访问项(明确清单)
1. PR #2208 四臂的模型构成与各臂分数、评测环境(harness/轮次/工具)— 正文与 diff 无法抓取,无搜索索引。
2. VentureBeat 正文(具体任务集名称、任务数、单个任务失败细节)— 仅获得转载标题级数字(46.2%/53.8%)。
3. aicoderscope 正文:各模型分数、"#1 模型"所指、评测环境。
4. codingfleet 榜单表格分数与指标。
5. llm-stats 榜单数值(JS 渲染)。
6. blackbox 复测配置(harness、轮次、工具、是否 Claude Code 原生/官方 API)与 GPT-5.6 Sol 同测分数。
7. HF 数据集 README 中的分数与配置。
8. orcarouter 文章的 TB 版本(是否为 2.1)与评测环境、原生 agent 与否。
9. Vals AI / 官方 tbench.ai 的具体分数数值。

**共同原因**:沙箱无直连网络(所有目标站点抓取被断),web_search 仅返回链接与标题及少数转载数字;所有"数值"均来自标题/摘要原文,未做推断。

## 六、日期说明
- 全部来源处于 2026 年时间线:GLM-5.2 2026-06-17 发布;aicoderscope 2026-06;Opus 4.8 发布于 2026-05-31 前后(agentmarketcap);V4 Flash 0731 与涨价 2026-08(InfoQ/DeepSeek news260821);PR #2208、StateM(arXiv 2608=2026-08)、80aj 2026-07-19。多数第三方榜单位页无具体日期,已标注"未注明"。