# Terminal-Bench 2.1 完整评测集调研报告

> 调研日期:2026-02(基于官方一手资料:论文 arXiv:2601.11868、harbor-framework 官方仓库、tbench.ai / terminal-bench.com 官网、Harbor 文档、Z.ai 验证数据集卡)
> 重要版本说明:Terminal-Bench 2.1 是 Terminal-Bench 2.0 的"更严格验证版"(同名 89 任务,其中 26 个被修改),无独立论文;分类体系、评测规则与失败分析继承自官方论文 arXiv:2601.11868(Terminal-Bench 2.0)。来源:https://github.com/harbor-framework/terminal-bench-2-1 、https://terminal-bench.com/
> 分部成果文件索引(本报告各章与已独立完成的成果文件一一对应):report-part1-任务分类.md、report-part2-评估指标.md、report-part3-开源执行器.md、report-part4-失败样本类型.md、report-part5-衍生测试用例.md

---

## 一、任务分类

### 1.1 任务领域分类(16 个 category,共 89 个任务)

分类由任务作者自报(论文 Figure 4 图注:"Categories were assigned by the task author");逐类数量按论文 Appendix H 的 89 行任务表逐条统计(合计 89,与论文摘要 "a set of 89 challenging tasks" 一致)。官方任务仓库:https://github.com/laude-institute/terminal-bench-2(2.0)与 https://github.com/harbor-framework/terminal-bench-2-1(2.1),任务目录同名。

| 类别(Category) | 任务数 | 代表性任务 |
|---|---|---|
| Software Engineering | 26 | cobol-modernization、path-tracing、write-compressor、torch-tensor-parallelism |
| System Administration | 9 | mailman、nginx-request-logging、qemu-alpine-ssh、install-windows-3.11 |
| Scientific Computing | 8 | adaptive-rejection-sampler、dna-assembly、raman-fitting、tune-mjcf |
| Security | 8 | break-filter-js-from-html、crack-7z-hash、password-recovery、openssl-selfsigned-cert |
| Data Science | 8 | hf-model-inference、mcmc-sampling-stan、mteb-leaderboard、sam-cell-seg |
| Debugging | 5 | custom-memory-heap-crash、overfull-hbox、sqlite-db-truncate |
| File Operations | 5 | db-wal-recovery、extract-elf、gcode-to-text、large-scale-text-editing |
| Model Training | 4 | train-fasttext、pytorch-model-cli、count-dataset-tokens |
| Mathematics | 4 | feal-differential-cryptanalysis、largest-eigenval |
| Data Processing | 4 | log-summary-date-ranges、regex-log、financial-document-processor |
| Machine Learning | 3 | caffe-cifar-10、distribution-search、llm-inference-batching-scheduler |
| Games | 1 | chess-best-move |
| Personal Assistant | 1 | constraints-scheduling |
| Optimization | 1 | portfolio-optimization |
| Data Querying | 1 | sparql-university |
| Video Processing | 1 | video-processing |

来源:https://ar5iv.labs.arxiv.org/html/2601.11868(§2.2、Figure 4、Appendix H)

### 1.2 难度分层

- 作者估计难度(论文 §4.3 原文):"Each task in Terminal-Bench 2.0 includes an author-estimated difficulty for a human to complete the task (medium or hard)"。
- 经验难度(论文原文):"Easy if Terminus 2 resolves the task with ≥66.7% of the selected frontier models, Medium if the resolution rate lies between 33.3% and 66.7%, and Hard if the resolution rate is <33.3%"。
- 按 Appendix H 统计:Medium 55、Hard 30、Easy 4(Easy 任务:cobol-modernization、fix-git、overfull-hbox、prove-plus-comm)。
- 人估与经验难度相关性:r = 0.436, p < 0.001;93.3% 人类 hard 任务经验上亦 hard;最大分歧:人类标 medium 而模型觉得 hard(54.5%)。
- 来源:https://ar5iv.labs.arxiv.org/html/2601.11868(§4.3、Appendix H)

### 1.3 任务构成要素(五元组)

论文 §2.1 原文:"A Terminal-Bench task consists of an instruction, a Docker image, a set of tests, an example solution, and a time limit (Figure 2) ... The tests verify that all outcomes described in the instruction have been achieved by testing properties of the **final container state**; they do not test the agent's commands or console output."——指令 + Docker 镜像 + 测试集 + 示例解 + 时限,结果驱动(outcome-driven)。

2.x 任务为 Harbor 格式,真实实例(`adaptive-rejection-sampler/task.toml`):`[task] name`、`[metadata] difficulty/category`、`[verifier] timeout_sec=900`、`[agent] timeout_sec=900`、`[environment] docker_image/cpus=1/memory_mb=2048/storage_mb=10240/allow_internet=true`。任务目录:`instruction.md / task.toml / environment/ / solution/ / tests/`。v1 版另有 `parser_name`、`max_agent_timeout_sec`(默认 360s)、`max_test_timeout_sec`(默认 60s)、`run_tests_in_same_shell` 等字段。
来源:https://ar5iv.labs.arxiv.org/html/2601.11868 、https://harborframework.com/docs/task-format 、https://github.com/laude-institute/terminal-bench-2/blob/main/adaptive-rejection-sampler/task.toml 、https://deepwiki.com/laude-institute/terminal-bench/1.2-key-concepts

---

## 二、评估指标与评测规则

### 2.1 核心指标:任务解决率(Resolution Rate)

- 得分 = 被解决任务数 / 总任务数;每任务二值。论文原文:"frontier models and agents resolve less than 65% of tasks, with smaller models scoring around 15%";"Codex CLI paired with GPT-5.2 achieves the highest average resolution rate of 63%";开源模型最佳 "Terminus 2 and Kimi K2 Thinking ... resolving 36% of tasks on average"。
- 来源:https://ar5iv.labs.arxiv.org/html/2601.11868(摘要、§1、§4)

### 2.2 判定机制

- v1:"Parsers return a dictionary mapping test names to status: A task is considered resolved when all tests return UnitTestStatus.PASSED."(来源:https://deepwiki.com/laude-institute/terminal-bench/1.2-key-concepts)
- 2.x(Harbor):测试脚本写 reward 文件到 `/logs/verifier/`——"reward.txt — A plain text file containing a single integer or float value, typically 1 for success or 0 for failure; reward.json — A JSON file that can define multiple metrics as rewards"("Harbor will read reward.json by default and fall back to reward.txt");机制上支持浮点部分得分(如 0.95),TB 2.0/2.1 惯例输出 0/1;多步任务 `multi_step_reward_strategy: "mean" | "final" | null`。(来源:https://harborframework.com/docs/task-format)

### 2.3 超时与提交规则

- 超时:2.x 任务 `[agent] timeout_sec = 900.0`、`[verifier] timeout_sec = 900.0`、`[environment] build_timeout_sec = 600.0`;v1 默认 agent 360s / test 60s。(来源:任务文件原文、DeepWiki)
- 2.1 排行榜提交规则原文:"Note: submissions may not modify timeouts or resources"(https://tbench.ai/leaderboard/terminal-bench/2.1);"you must run at least 5 trials per task and upload them to Harbor Hub publicly"(https://github.com/harbor-framework/terminal-bench-2-1)
- 2.1 排行榜现状(网页原文):17 条记录,榜首 "Claude Code / Fable 5 / xhigh / 83.8% ± 1.2%",第 2 "Codex / GPT-5.5 / 83.1%",第 3 "Terminus 2 / Fable 5 / 80.4%"。来源:https://tbench.ai/leaderboard/terminal-bench/2.1

---

## 三、开源执行器(评测运行框架/Harness)

### 3.1 Harbor(官方 runner,2.1 的指定执行器)

- 仓库:https://github.com/harbor-framework/harbor ;安装 `uv tool install "harbor[daytona]"`;登录 `harbor auth login`。
- 运行命令(官方 README/文档原文):

```shell
harbor run -d terminal-bench/terminal-bench-2-1 -a <agent> -m <provider/model> -k 5 -n <concurrency> --upload --public
```

参数:`-d` 数据集、`-a` agent、`-m` 模型、`-k` 每任务 trials(≥5)、`-n` 并发、`--upload --public` 公开上传;还支持 `-l` 限量冒烟、`--env daytona` 云沙箱、`--agent-import-path` 自定义 agent、`--include-task-name` 单任务;提交走 `cd leaderboard && uv run lb submit <job-url>`。
- 来源:https://github.com/harbor-framework/terminal-bench-2-1 、https://tbench.ai/docs/run-terminal-bench-2-1 、https://harborframework.com/docs/task-format

### 3.2 terminal-bench pip 包(tb CLI,官方 1.x harness)

- 仓库/PyPI:https://github.com/harbor-framework/terminal-bench-1 ;`pip install terminal-bench`。
- 运行(README 原文):`tb run --agent terminus --model anthropic/claude-3-7-latest --dataset-name terminal-bench-core --dataset-version 0.1.1 --n-concurrent 8`。
- 构成(README 原文):"Terminal-Bench consists of two parts: a **dataset of tasks**, and an **execution harness** that connects a language model to our terminal sandbox."—— 任务数据集 + 执行 harness(依赖 uv 与 Docker)。
- 来源:https://github.com/harbor-framework/terminal-bench-1 、https://deepwiki.com/laude-institute/terminal-bench/1.2-key-concepts

### 3.3 EvalScope(第三方框架)

- 阿里 ModelScope 的评测框架,官方文档设有专门 "Terminal-Bench-2.1" 页:https://evalscope.readthedocs.io/zh-cn/latest/benchmarks/terminal_bench_v2_1.html(源码文档:https://github.com/modelscope/evalscope/blob/main/docs/en/benchmarks/terminal_bench_v2_1.md)

---

## 四、常见模型失败样本类型

### 4.1 轨迹级(TAT,9 类,论文 Appendix C.1)

- Execution:Disobey Specification(违反规格)、Step Repetition(步骤重复)、Unaware of termination conditions(不知终止条件)
- Coherence:Reasoning-Action Mismatch(推理-行动不一致)、Context Loss(上下文丢失)、Task Derailment(任务偏离)
- Verification:Premature termination(过早终止)、No or incorrect Verification(无/错误验证)、Weak Verification(验证薄弱)
- 统计(论文原文):"Execution errors dominate for Opus 4.5 and GPT-5.2, while coherence and verification errors occur at lower rates. Conversely, the open sourced model evaluated (Qwen Coder) displays a more balanced error pattern"。
- 来源:https://ar5iv.labs.arxiv.org/html/2601.11868(§4.4、Appendix C.1)

### 4.2 命令级(论文 §4.5 + Appendix E)

- 原文:"command failures calling executables that are not installed or not in PATH are the most frequent (24.1% of all failures) followed by failures when running executables (9.6%)"——**最常见的失败样本 = 调用的可执行文件未安装或不在 PATH**;命令错误率 9.2%(Grok 4)~ 26.7%(GPT-OSS-120B)。
- 一级类别:Invocation & CLI;Filesystem & Permissions;Environment & Configuration;Build/Toolchain/Packages;Packages & repositories;Network & Remote Access;Runtime/Interpreters/Processes;Interpreters & REPLs;Services & platforms;Data & Formats;Testing & Quality。
- 来源:https://ar5iv.labs.arxiv.org/html/2601.11868(§4.5、Appendix E.2)

### 4.3 机制与数据集层面

- v1 FailureMode:timeout / context length / agent errors / test timeout(来源:https://deepwiki.com/laude-institute/terminal-bench/1.2-key-concepts)
- 2.1 修 26 个任务的原因(README 原文):"fix bugs, modify timeouts or resources, or improve robustness to reward hacking"(修 bug、调超时/资源、防 reward hacking);多数改动取自 Z.ai Terminal-Bench 2.0 Verified(89 任务环境修复 + 11 任务指令修复;2026.08.18 再修 6 个:Grading/Test Fixes 4 个 —— verifier 假阴性/假阳性;Instruction Fixes 2 个 —— 测试隐含约定未写进指令)。来源:https://github.com/harbor-framework/terminal-bench-2-1 、https://huggingface.co/datasets/zai-org/terminal-bench-2-verified
- 作弊/污染风险(论文 Limitations):读 oracle 解作弊(实践中未观察到)、训练语料污染(仓库含 Big-Bench canary 字符串)。来源:https://ar5iv.labs.arxiv.org/html/2601.11868

---

## 五、自制 3 道衍生测试用例(自验评测规则理解)

> 设计意图:从 Terminal-Bench 2.1 评测规则中"衍生"的情景判断题,验证对规则的理解达到"能正确应用"的水平。

### 用例 1:结果驱动判定 —— "过程一团糟,结局恰恰好"

- **情景**:agent 在 `cobol-modernization` 中前 40 条命令全部失败,第 41 条命令成功执行一次性 Python 脚本,生成文件与 GnuCOBOL 输出字节级一致;verifier 运行 `tests/test.sh` 全部通过,`/logs/verifier/reward.txt` 写入 `1`。
- **考察知识点**(评测规则):结果驱动(outcome-driven)判定——只检查最终容器状态属性,不检查命令过程(论文 §2.1);2.x 以 reward 文件为准(Harbor 文档)。
- **参考答案**:判定 **resolved**:过程命令失败不影响结果;reward=1 ⇒ 记入 resolution rate(若 agent 篡改测试脚本则构成 reward hacking,2.1 已加固 26 个任务,本情景为官方 verifier 运行)。
- **判分标准**:答"通过/1 分"并说明"只看最终状态与测试"得满分;答"因命令失败不得分"则未理解结果驱动规则。

### 用例 2:提交合规 —— "把超时翻 4 倍再只投 1 次,行不行?"

- **情景**:团队把 `[agent] timeout_sec` 900→3600、`cpus` 1→8,每任务只跑 1 次 trial,挑最高分 `--upload --public` 提交榜单。
- **考察知识点**(评测规则):提交规则原文 "submissions may not modify timeouts or resources"(tbench.ai leaderboard);"at least 5 trials per task and upload them to Harbor Hub publicly"(2.1 README);标准配置 timeout_sec=900。
- **参考答案**:**不合规**:改 timeout/资源违规;1 次 trial 不足 5 次且自选最高分构成选择性上报。正确做法:`harbor run -d terminal-bench/terminal-bench-2-1 ... -k 5 ... --upload --public`。
- **判分标准**:指出两个违规点得满分,只答一个得半分,答"合规"判未理解。

### 用例 3:难度分层与失败归因 —— "8 个模型只有 2 个解出来,到底难不难?"

- **情景**:任务 X 在 8 个前沿模型上由 Terminus 2 评测,仅 2 个 resolved;失败轨迹中模型在 `pip install` 报错后连续 4 次重复相同命令,最后声明完成退出,测试全败。
- **考察知识点**(评测规则):经验难度阈值(Easy ≥66.7%、Medium 33.3–66.7%、Hard <33.3%,论文 §4.3);TAT 失败分类(Step Repetition、Premature termination,Appendix C.1)。
- **参考答案**:2/8=25% <33.3% ⇒ **Hard**;轨迹命中 **Step Repetition**(Execution 类)+ **Premature termination**(Verification 类);命令失败对应"可执行文件未装/不在 PATH"(占命令失败 24.1%)。
- **判分标准**:难度映射正确得一半,识别至少一类 TAT 失败(含大类)得另一半。

### 用例自验清单

| 用例 | 覆盖的评测规则维度 | 依据来源 |
|---|---|---|
| 用例1 | 结果驱动判定、reward 文件评分 | 论文 §2.1;Harbor 文档 |
| 用例2 | 超时配置(900s)、提交合规(≥5 trials 公开上传、不改 timeout/资源) | tbench.ai leaderboard;2.1 README |
| 用例3 | 经验难度阈值;TAT 失败分类 | 论文 §4.3、Appendix C.1 |

---

## 六、来源链接清单(全部引用出处)

1. 论文全文(HTML):https://ar5iv.labs.arxiv.org/html/2601.11868(§1、§2.1、§4.3–4.5、Appendix C.1/E.2/H、Limitations)
2. 论文摘要页:https://arxiv.org/abs/2601.11868
3. OpenReview(ICLR 2026):https://openreview.net/forum?id=a7Qa4CcHak
4. Terminal-Bench 2.1 官方仓库:https://github.com/harbor-framework/terminal-bench-2-1
5. Terminal-Bench 2.0 任务仓库:https://github.com/laude-institute/terminal-bench-2
6. Terminal-Bench 1.x 仓库:https://github.com/harbor-framework/terminal-bench-1
7. Harbor 框架仓库:https://github.com/harbor-framework/harbor
8. Harbor 任务格式文档:https://harborframework.com/docs/task-format
9. 官网首页:https://terminal-bench.com/
10. tbench.ai 文档(运行 2.1):https://tbench.ai/docs/run-terminal-bench-2-1
11. tbench.ai 基准浏览:https://tbench.ai/benchmarks/terminal-bench-2
12. tbench.ai 排行榜(2.1):https://tbench.ai/leaderboard/terminal-bench/2.1
13. Z.ai Verified 数据集卡:https://huggingface.co/datasets/zai-org/terminal-bench-2-verified
14. DeepWiki(1.x 概念):https://deepwiki.com/laude-institute/terminal-bench/1.2-key-concepts
15. EvalScope 2.1 文档:https://evalscope.readthedocs.io/zh-cn/latest/benchmarks/terminal_bench_v2_1.html
16. EvalScope 仓库:https://github.com/modelscope/evalscope
17. Harbor Hub 数据集页:https://hub.harborframework.com/datasets/terminal-bench/terminal-bench-2-1/latest