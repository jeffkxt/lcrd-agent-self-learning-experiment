# LCRD-Agent 自治学习示例：Terminal-Bench 2.1 调研任务

> 本目录为 LCRD-Agent（Goal-Stop-Marker 契约框架）的**自治学习能力示范轨迹**。
> 模型：DeepSeek-V4-Flash-0731，任务为完整调研 Terminal-Bench 2.1 评测集，自主规划检索、资料汇总，并自行生成测试用例校验自身对评测规则的理解。
> ⚠️ 注意：这是**实验原型轨迹输出**，不是官方权威评测文档；所有结论基于公开网页、论文、仓库抓取内容，存在第三方信息偏差风险，请勿直接当作正式论文引用。
> 📊 资源消耗参考：工具调用累计耗时 128 分 48 秒，首 token 平均 39 秒，总输出 token 约 144k，端到端整体耗时约 89 分钟。（注：工具调用为端到端耗时中工具执行阶段的累计，二者口径不同，见下文"资源指标"说明。）

## 任务 Goal-Stop-Marker 原始指令

```
Goal：调研 Terminal-Bench 2.1 完整评测集，整理：任务分类、评估指标、开源执行器、常见模型失败样本类型。
约束：自主规划完整学习检索步骤；资料汇总完成后，自行设计 3 道衍生测试用例，验证自身是否真正理解 Terminal-Bench 2.1 的评测规则。
Stop：四大信息项全部整理完毕，3 道衍生测试用例撰写完成，无遗漏目标。
Marker：输出结构化完整报告，单独小节放置自制 3 条测试用例，所有引用附带原始来源链接。
```

## 任务简述
这是一个长耗时的复杂调研任务，全程由 LCRD 契约约束：
1. 框架仅设置 Goal、Stop、Marker 边界条件，**不预设检索步骤、不写死查询语句，检索策略完全交给模型自主规划**；
2. 过程中发生两次工具链路（opencode-go）中断，Agent 在 LCRD 约束下恢复上下文，没有遗忘原始目标、没有裁剪需求，没有发生长链推理漂移；
3. 模型优先抓取论文、GitHub 官方仓库、项目官网一手来源，甄别无效/404 废弃仓库，区分 TB 2.0 论文与 TB 2.1 修订版，规避自媒体二手转述信息；
4. 调研完成后，**自主生成 3 道情景式衍生测试用例**，用来验证自己是否读懂 TB 2.1 的评测规则（结果驱动判定、榜单提交合规、经验难度与失败模式归因）；
5. 输出多份结构化 Markdown 报告，同时留存大量原始抓取源文件作为证据链，满足 Marker「可复核」的要求。

> 与传统 RAG-Agent 的关键差异：
> - 传统 Agent：人预先编排好每一步搜索、每一步解析；
> - LCRD-Agent：人只定目标与验收条件，**检索、筛选、归纳、自我校验全部交由模型自治**；出现错误不修改框架逻辑，而是把整条轨迹作为能力缺陷样本留存，用于后续模型训练补强。

## 目录文件清单

```
./
├── README.md                              # 本说明文档
├── Terminal-Bench-2.1-调研报告.md          # 总报告，完整汇总四大模块 + 3 道自制测试用例
├── report-part1-任务分类.md
├── report-part2-评估指标.md
├── report-part3-开源执行器.md
├── report-part4-失败样本类型.md
├── report-part5-衍生测试用例.md
├── Terminal-Bench-2.1-深度笔记.md          # 一手资料深度笔记，大量原文摘抄与来源标注
├── tbench21_compare_report.md             # Claude Opus4.8 / GLM-5.2 / DeepSeek-V4-Flash-0731 TB2.1 跑分对比
├── tb21_thirdparty_report.md              # 第三方评测数据源取证报告，区分官方 / 第三方，标注取证限制
└── tb_sources/                            # 原始抓取网页、仓库、论文片段（证据链，用于复核报告内容）
```

> 💡 文件名说明：本目录早期版本部分文件名含空格（如 `Terminal-Bench-2.1 - 调研报告.md`），已在本地整理版中统一改为连字符命名（如上所示），避免命令行与脚本引用时出错。

## 核心关键发现摘要
1. **版本区分**：arXiv:2601.11868 论文描述的是 Terminal-Bench 2.0（89 任务）；**Terminal-Bench 2.1 是 2.0 的修订验证版本，无独立论文**。关于"被修改的任务数"，两套口径并存：官方仓库 README 口径为 **26 个任务被修改**（修复 bug、调整 timeout/资源、提升防 reward-hacking 鲁棒性）；Snorkel/tbench.ai 官方新闻按"问题任务"口径记为 **28 个任务被修复**（9 个外部依赖漂移、8 个资源预算过紧、其余为指令-测试不一致），差异源于一个任务可能修复多个问题类别 [citation:2][citation:4][citation:5]。本实验报告正文采用官方仓库 README 的 26 口径，特此说明。
2. **结果驱动评测**：TB 2.x 只校验**最终容器状态**（产出文件、运行服务、计算值等），不审查中间命令执行过程；测试脚本输出 `reward.txt` / `reward.json` 作为判定依据 [citation:9]。
3. **提交硬性规则**：榜单提交**禁止修改任务 timeout 与硬件资源，每个任务至少跑 5 次 trial 并且公开上传**（Harbor Hub）[citation:2]。
4. **两套失败分类体系**
   - TAT 轨迹级：Execution、Coherence、Verification 三大类，含步骤重复、过早终止、上下文丢失、任务偏离等 9 个子类型；
   - 命令级统计：最频发错误为 `可执行文件未安装/不在 PATH`，占全部命令失败的 24.1%。
5. **Harness 效应影响巨大**：同一模型仅更换 Agent 执行框架/沙箱配置，分数波动可达 **3–20+ 分**，波动幅度经常大于模型之间的分差；公开榜单跨来源对比须严格对齐环境与 harness，否则结论不可靠 [citation:7]。DeepSeek 官方自报的 V4-Flash-0731 TB 2.1 分数（82.7）与独立测评 Artificial Analysis 的测量值（79）即存在 3.7 分差异，正是 harness 敏感性的体现 [citation:20]。
6. **关于 DeepSeek-V4-Flash-0731 的 TB 2.1 跑分现状**：本实验**未向 Harbor Hub 提交官方榜单 trial，故无本实验自测的官方榜单分数**；但 DeepSeek-V4-Flash-0731 在 Together AI、NVIDIA 模型卡及 evals.report 等均有 **82.7%（Terminal-Bench 2.1）** 的官方/验证跑分记录 [citation:12][citation:13][citation:15]。该 82.7 为厂商自报值（DeepSeek Harness minimal 模式，未开源），跨 harness 不可直接横向对比。

## 本次运行观测：资源消耗、模型表现 & 待补强子能力
### 📈 本次运行资源指标
- 模型上下文窗口：1M token（DeepSeek-V4-Flash-0731 原生支持）[citation:13]
- 工具调用累计耗时：128 分 48 秒
- 首 token 平均耗时：39 秒
- 总输出 token：约 144k
- 端到端整体耗时：约 89 分钟

> ⚠️ 口径说明：工具调用累计耗时（128 分 48 秒）是端到端整体耗时（约 89 分钟）中**工具执行阶段的累计**，因工具调用与模型推理在端到端时间轴上存在重叠/穿插，二者并非简单的"包含"关系，数值不可直接相减比较。

### ✅ 表现亮点
- 超长任务下 LCRD 契约生效：工具两次断开后恢复，Goal 目标全程不漂移，不私自缩减任务范围；
- 具备一手资料甄别能力，能够识别 404 失效仓库，勘误 TB 2.0 / TB 2.1 版本混淆；
- 区分事实记录与推断结论，对无法获取的网页数据明确标注取证限制，**不编造数字和来源**；
- 完成调研后可自主出题做自我理解校验，不只是做资料摘抄。

### ⚠️ 暴露的模型短板（作为训练样本入库）
1. 没有自主设置检索轮次上限，深度抓取大量附录时任务耗时极高（本次端到端约 89 分钟）；
2. 遇到多来源互相冲突的数字口径（如 26 vs 28 个任务被修改），仅并列记录，缺少自动溯源原始 PR/文档做交叉核验的自主流程；
3. 批量抓取大量原始文档后，缺少自主去重、压缩摘要逻辑，证据文件体积膨胀。

> LCRD-Agent 设计哲学：出现上述问题，**不属于框架 bug，属于模型子能力经验不足；完整轨迹保存，作为负样本供给基座后续训练迭代**，框架本身不做代偿式补丁。

## 相关链接
- LCRD 项目主仓库：（填写你的仓库地址）
- Terminal-Bench 2.1 官方仓库：https://github.com/harbor-framework/terminal-bench-2-1
- Terminal-Bench 2.0 论文（arXiv:2601.11868）：https://arxiv.org/abs/2601.11868
- DeepSeek-V4-Flash-0731 模型卡（Together AI）：https://www.together.ai/models/deepseek-v4-flash-0731
- Terminal-Bench 2.1 官方新闻（28 任务修复口径）：https://www.tbench.ai/news/terminal-bench-2-1

## Contact
If you are interested in LCRD‑Agent framework, autonomous‑agent long‑chain experiment, want to discuss or give feedback, feel free to contact me:
**jeffkxt@gmail.com**

## License
本目录下轨迹报告文档采用 MIT 协议；

⚠️：`tb_sources/` 内原始抓取内容版权归原作者所有，请遵守原项目开源协议。请确认 `tb_sources/` 内未包含需登录方可访问的内容；若含 Terminal‑Bench 官方仓库完整任务文件，请另行核对官方仓库 LICENSE 是否允许再分发。
