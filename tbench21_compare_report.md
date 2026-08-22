# Terminal-Bench 2.1 三模型公开原始跑分对比报告(v1.2b)
日期:2026-08 检索基准 | 调研方法:web_search 多轮中英文检索 + 两个子代理独立取证;沙箱无出站直连网络(正文/JS 榜单/PR diff/README 无法抓取),所有数值仅取自搜索结果标题/摘要/URL 可见信息,逐条标注来源 URL;无 URL 可核验的转述一律隔离在附录且不参与结论。

## 0. 结论摘要(先给答案)
- **最高分:Claude Opus 4.8**——第三方复测 TB v2.1 = 90% pass@1(Blackbox),为三个模型公开证据中最高的单一数值。
- **第二名证据打架:GLM-5.2 与 DeepSeek V4 Flash (0731) 排序随评测环境翻转**(GLM-5.2:TB2.1 榜单解读 81 分 / 第三方 82.7;V4 Flash:无官方 TB2.1 记录、无可核验的独立 TB2.1 数值),公开记录无法稳定分出高下。
- 诚信限定:三模型在 TB2.1 上不存在"同一机构、同一 harness、同一时点"的三方同配置官方横评;官方榜单以 agent 组合行为条目(如 "Claude Code + Opus 4.8"),官方单元格数值本次未读取。结论为基于可比较第三方证据的最优推断。
- 基准背景:官方 https://www.tbench.ai/news/terminal-bench-2-1 、https://www.tbench.ai/leaderboard/terminal-bench/2.1 、https://github.com/harbor-framework/terminal-bench-2-1 、EvalScope https://evalscope.readthedocs.io/zh-cn/v1.8.0/benchmarks/terminal_bench_v2_1.html 、论文 https://arxiv.org/html/2601.11868 ;第三方榜 https://artificialanalysis.ai/evaluations/terminalbench-v2-1 、https://www.vals.ai/benchmarks/terminal-bench-2-1 、https://benchlm.ai/benchmarks/valsterminalbench21 、https://llm-stats.com/benchmarks/terminal-bench-2.1 ;提交统计 arXiv 2606.20683。原生 vs CLI 两栏分类与轮次/工具/沙箱细则未在摘要呈现,须访问官方页面核验。

## 1. Claude Opus 4.8(Anthropic,2026-05-28~06-01 发布)
- 最强证据:Blackbox 复测 TB v2.1 = 90% pass@1,标题原词 "TB v2.1 Blackbox — GPT-5.6 Sol + Opus 4.8 (90% pass@1)" https://www.blackbox.ai/blog/tb-v2-1-blackbox-gpt-5-6-sol-opus-4-8 (第三方;90% 归属"GPT-5.6 Sol + Opus 4.8 组合",单模型贡献未披露,复测配置未披露)。
- 官方榜单 "Claude Code + Opus 4.8" 组合行 https://www.tbench.ai/leaderboard/terminal-bench/2.1?models=Codex+CLI+%2B+GPT-5.5,Claude+Code+%2B+Opus+4.8 (数值:未获取);Vals 页面 https://www.vals.ai/benchmarks/terminal-bench-2-1?suggested=open-weights-table (数值:未获取)。
- 环境敏感性:GeekPark/Floatboat 对照《贵 57.1 倍的 Claude Opus 4.8 五项全输,赢它的不是模型,是 Harness》,HLR 区间 0.26~1.42x https://w.geekpark.net/news/368637 。
- 差价:codingfleet《Claude Opus 4.8 vs GLM-5.2: 0.7 Points From the Coding King at 1/6 the Price》(GLM-5.2 差 0.7 分、价 1/6;编码基准口径,是否 TB2.1 未确认) https://codingfleet.com/blog/claude-opus-4-8-vs-glm-5-2/ 。
- 发布信息:https://ai.zhiding.cn/2026/0601/3188968.shtml 、https://www.eweek.com/news/anthropic-claude-opus-4-8-ai-honesty/ ;社区复测数据集 https://huggingface.co/datasets/cody-vi4/tbench-2-1-cody-opus48 (README 分数未获取,license apache-2.0)。

## 2. GLM-5.2(智谱,2026-06-17 开源, MIT, 1M 上下文)
- TB2.1 榜单解读 81 分:yun88 https://www.yun88.com/news/9547.html (第三方;评测配置未注明)。
- 82.7:orcarouter《Qwen 3.8 vs GLM-5.2: 86.6 vs 82.7 on Terminal-Bench》 https://www.orcarouter.ai/blog/qwen-3-8-vs-glm-5-2 (第三方;TB 版本未注明 2.1,原生/harness 配置未注明)。
- 距离佐证:yun88 https://www.yun88.com/news/9599.html ("只差 1% 了?");codingfleet"差 0.7 分、价 1/6" https://codingfleet.com/blog/claude-opus-4-8-vs-glm-5-2/ 。
- 官方:博客 https://glm5.app/blog/glm-5-2-benchmarks 、仓库 https://github.com/zai-org/GLM-5 (官方 TB 数值未在摘要呈现);ai-primer 报道其 Vals 与 Design Arena 第一、AA Coding Index 50.7 https://www.ai-primer.com/engineer/stories/glm-5-2-ranks-aa-vals-design-arena 。
- 发布信息:https://news.qq.com/rain/a/20260617A03E2E00 、https://www.donews.com/news/detail/4/6600647.html 。

## 3. DeepSeek V4 Flash (0731)(DeepSeek,2026-07-31 正式版 API 公测)
- 官方身份:官方 HF 仓库 https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731 ;Vercel AI Gateway https://vercel-docs.vercel.sh/ai-gateway/models/deepseek-v4-flash-0731/about ;官方发布 https://api-docs.deepseek.com/news/news260821/ ;InfoQ https://xie.infoq.cn/article/ce3ac43042f3ec16db28d876f ;正式版 2026-07-31 上线(新浪)。
- **官方 TB2.1 记录:未获取**(tbench.ai 官方榜单未见 DeepSeek 条目证据;多轮检索无官方数值)。
- 带 URL 的可核验第三方数据:
  * autoprompt-skill 开源仓库 docs/benchmarks/terminal-bench-2.1.md:完成率 67.42%(裸)→82.02%(加 tool/coding skill 增强),同一模型上 +14.61 分 https://raw.githubusercontent.com/Spielewoy/autoprompt-skill/main/docs/benchmarks/terminal-bench-2.1.md 。
  * VentureBeat《DeepSeek's top-ranked V4 Flash stumbles on real agent tasks as its prices surge》:真实任务失败率 46.2% / 通过率 53.8%(KuCoin 转载 https://www.kucoin.com/news/flash/deepseek-s-v4-flash-fails-46-2-of-real-world-tasks-despite-low-pricing 、followin https://followin.io/en/feed/27013318 ;任务集未确认是否 TB2.1,非 TB 官方 harness) https://venturebeat.com/orchestration/deepseeks-top-ranked-v4-flash-stumbles-on-real-agent-tasks-as-its-prices-surge 。涨价背景:最高涨幅 1100%(媒体转述),"$0.28 Agentic Output Floor"(Yahoo Finance)。
  * 其他基准(非 TB2.1):SuperCLUE-Terminal 46 分 vs Kimi K3 61 分 https://www.sohu.com/a/1059258552_122014422 (两套量表,不可混用);Telco-GAIA 40.0% https://arxiv.org/abs/2607.20510 ;AA 智能指数 50(+10 vs 前版,子代理经 artificialanalysis 检索转述)。
- 版本时点:科创板日报 2026-08-02《DeepSeek-V4系列迎重大升级 性能追平旗舰模型 Agent能力大幅增强》 https://finance.eastmoney.com/a/202608023829160949.html ——前后评测存在权重版本差异。

## 4. 同配置判定(根锚问题答案)
- 配置假设:同一评测口径、同为"原生 Agent"、相同预算/沙箱/工具集。
- 排序结论:**Claude Opus 4.8 最高**(90% pass@1,Blackbox 混合 harness,第三方;GLM-5.2 最高约 81~82.7,另有"差 0.7 分"说法);**GLM-5.2 与 V4 Flash 排序随环境翻转、公开记录无法稳定区分**(GLM:81/82.7 带 URL;V4 Flash:无官方 TB2.1 记录、无带 URL 的独立 TB2.1 数值,仅完成率 67.42→82.02 与 46.2% 失败率为可核验参考)。
- 严格"同一官方原生 agent 配置三方同测"的记录不存在;结论为最优推断。82.7 数字同时出现在 GLM-5.2(orcarouter)与若干转述中,横比须回原文核验。

## 5. 评测环境差异导致的分数偏差清单(每条带来源 URL)
1) **Harness/工程框架效应(最大偏差源,10~20+ 分)**:LangChain 官方方法论(仅优化运行环境,TB 2.0 从 52.8%→66.5%、第 30→5 名) https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering (CSDN 复述 https://blog.csdn.net/weixin_63196346/article/details/162478997 );《The Harness Effect》同模型换工具差 16 分 https://codex.danielvaughan.com/2026/04/19/the-harness-effect-same-model-different-tool-different-score/ ;StateM:harness scaling 在 TB2.1 达 95.3% 原始准确率、约 15 美元 https://arxiv.org/abs/2608.15089v1 。
2) **Skill/工具增强在同一模型上的分数差**:V4 Flash + autoprompt skill 完成率 67.42→82.02(+14.61 分) https://raw.githubusercontent.com/Spielewoy/autoprompt-skill/main/docs/benchmarks/terminal-bench-2.1.md 。
3) **Agent 类型与混合配置**:Blackbox 90% 为 GPT-5.6 Sol + Opus 4.8 混合 harness;官方榜单用 "Claude Code + Opus 4.8" 等 CLI 组合行;混合/CLI 成绩当"模型原生分"会系统性高估 https://www.blackbox.ai/blog/tb-v2-1-blackbox-gpt-5-6-sol-opus-4-8 、https://www.tbench.ai/leaderboard/terminal-bench/2.1 。
4) **沙箱与权限策略**:BoundaryBench 在 NIST 加固沙箱下横评 Claude Code、Codex、Terminus 2、Grok,策略收紧改变工具可用性与得分 https://github.com/boundary-bench/boundary-bench 、https://agentmarketcap.ai/blog/2026/08/07/boundarybench-sandbox-policy-coding-agents 。
5) **预算/轮次/成本上限**:VentureBeat 报道 V4 Flash 涨价(最高涨幅 1100%,媒体转述)与真实任务表现反差 https://venturebeat.com/orchestration/deepseeks-top-ranked-v4-flash-stumbles-on-real-agent-tasks-as-its-prices-surge ;StateM 15 美元低成本刷出高分 https://arxiv.org/abs/2608.15089v1 。
6) **口径混淆与复测证伪**:SuperCLUE-Terminal 46 分是另一量表 https://www.sohu.com/a/1059258552_122014422 ;"自验证 Skill 反超 Fable 5"被社区复测证伪 https://post.smzdm.com/p/a6zd3m2o/ 、https://www.sohu.com/a/1065420177_122980439 。
7) **版本时点差**:Opus 4.8(5 月底)、GLM-5.2(6 月中)、V4 Flash(7 月底)发布错开,V4 系列 8 月初"重大升级" https://finance.eastmoney.com/a/202608023829160949.html 。
8) **同数字多归属的小分差风险**:82.7(orcarouter)与 81(yun88)对 GLM-5.2 差 1.7 分,处于环境噪声范围;小分差结论必须回到各自原文核验。

## 6. 数据可信度与取证限制声明
- 沙箱无出站直连网络(正文、JS 榜单、PR diff、README 无法抓取),全部数值来自 web_search 标题/摘要/URL;官方 tbench.ai 单元格数值、Vals/AA/llm-stats 页内数值、Anthropic/智谱官方博客数值、Maka-Agent PR #2208 四臂构成与分数(https://github.com/Maka-Agent/maka-agent/pull/2208 ,正文未获取)、HF README 分数均标"未获取"。
- 已确认数值(均带 URL):Opus 4.8 = 90% pass@1(Blackbox,第三方);GLM-5.2 = 81(yun88,第三方)与 82.7(orcarouter,第三方,版本未注明);V4 Flash = 67.42→82.02 完成率(autoprompt-skill 仓库,含工具增强)、46.2% 真实任务失败率(VentureBeat/KuCoin,非 TB harness)、46 分(SuperCLUE-Terminal,另一基准)。无编造数值、无编造 URL。

## 7. 附录:未核验转述(无 URL,不参与结论)
以下条目仅存在于子代理检索转述中,本次取证未能取得可核验的 URL,故不参与排序结论,仅作线索提示:
1) aitoolsrecap 文章标题转述:"$0.14/M, Terminal-Bench 82.7%"(指 DeepSeek V4 Flash;该 82.7 与 GLM-5.2 的 82.7、Ante 自称 82.7% 撞车,归属可信度存疑,必须回原文核实)。
2) Towards AI 文章标题转述:《DeepSeek V4-Flash vs GLM-5.2: The 1.7-Point Win Collapses When You Swap the Harness》(V4 Flash 对 GLM-5.2 的 1.7 分优势换 harness 后消失)。
3) 八套 harness 对比转述:V4 Flash 换 8 套 harness,Pi agent 成功率最高且最省钱、Claude Code 最快但最贵(ChainThink/BlockBeats 转述);另 Composio/Ante 组合成功率 47%–67%(ai-primer 检索页 https://www.ai-primer.com/engineer/stories/agent-harness-cost-spread 存在但数值未直接读取)。
结论依据不受附录影响:排序仅依据第 1~4 节中带 URL 的证据。
