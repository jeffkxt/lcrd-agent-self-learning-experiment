# Terminal-Bench 2.1 调研报告 · 第二部分:评估指标与评测规则

## 1. 核心指标:任务解决率(Task Resolution Rate)

- 论文摘要原文:"frontier models and agents score less than 65% on the benchmark";§1:"frontier models and agents resolve less than 65% of tasks, with smaller models scoring around 15%"。
- 论文 §4 原文:"Codex CLI paired with GPT-5.2 achieves the highest average resolution rate of 63%, followed by Terminus 2 with Claude Opus 4.5 and Terminus 2 with Gemini 3 Pro at 58% and 57%";"Terminus 2 and Kimi K2 Thinking performing best among the open-weight models, resolving 36% of tasks on average"。
- 即:得分 = 被解决任务数 / 总任务数(resolution rate),每任务二值(解决/未解决)。
- 来源:https://ar5iv.labs.arxiv.org/html/2601.11868

## 2. 判定机制:结果驱动 + 测试全通过

- 论文 §2.1 原文(判定原则):"The tests verify that all outcomes described in the instruction have been achieved by testing properties of the **final container state**; they do not test the agent's commands or console output. This is intentional as Terminal-Bench is an outcome-driven framework where each agent is free to accomplish the task using a variety of approaches." —— 只检查最终容器状态属性,不检查命令与过程,允许任意实现路径。
- v1(1.x)判定原文(DeepWiki):"Parsers return a dictionary mapping test names to status: A task is considered resolved when all tests return UnitTestStatus.PASSED."(全部单元测试 PASSED = 解决;未解决时记录 failure_mode)。来源:https://deepwiki.com/laude-institute/terminal-bench/1.2-key-concepts
- 2.x(Harbor 格式)判定:测试脚本写 reward 文件,Harbor 读取该文件判定成败。Harbor 文档原文:"the test script must produce a reward file in the /logs/verifier/ directory ... reward.txt — A plain text file containing a single integer or float value, typically 1 for success or 0 for failure; reward.json — A JSON file that can define multiple metrics as rewards, but they must be floats or integers ... Harbor will read reward.json by default and fall back to reward.txt." —— 机制上支持浮点(如 0.95,即部分得分/连续得分),但 Terminal-Bench 2.0/2.1 测试脚本惯例是输出 0 或 1(1=成功);官方示例 `echo 1 > /logs/verifier/reward.txt`。来源:https://harborframework.com/docs/task-format

## 3. 超时(timeout)规则

- 论文 §2.1:任务构成含 time limit("The instruction describes the task that the agent must complete within the specified time limit in the Docker container")。
- 2.x 任务文件(抓取原文):`[agent] timeout_sec = 900.0`、`[verifier] timeout_sec = 900.0`、`[environment] build_timeout_sec = 600.0`(各任务普遍是 agent/verifier 900 秒)。
- v1 默认值(DeepWiki):`max_agent_timeout_sec` 默认 360s、`max_test_timeout_sec` 默认 60s(具体任务文件里可为 900/300)。
- 2.1 排行榜提交规则原文:"Note: submissions may not modify timeouts or resources"。来源:https://tbench.ai/leaderboard/terminal-bench/2.1

## 4. 多步/多指标与奖励策略

- Harbor 配置字段:`multi_step_reward_strategy: "mean" | "final" | null`(多步任务奖励按平均、最终值或空)。来源:https://harborframework.com/docs/task-format
- 对多判据/LLM 判定场景,官方指引使用 Rewardkit(文档原文 "For verifiers with multiple criteria, score aggregation, and LLM judging, see Rewardkit")。来源:https://harborframework.com/docs/task-format

## 5. 排行榜与提交要求(2.1)

- tbench.ai 排行榜 "terminal-bench@2.1" 原文:"Showing 17 entries",榜首:"1 / Claude Code / Fable 5 / xhigh / 83.8% ± 1.2% / Jun 7, 2026";第 2 名 "Codex / GPT-5.5 / xhigh / 83.1%";第 3 名 "Terminus 2 / Fable 5 / high / 80.4%";第 17 名 "Claude Code / GLM-5.1 / max / 58.7%";"Results in this leaderboard correspond to terminal-bench/terminal-bench-2-1";"A Terminal-Bench team member ran the evaluation and verified the results."。来源:https://tbench.ai/leaderboard/terminal-bench/2.1
- 2.1 README 提交要求原文:"you must run at least 5 trials per task and upload them to Harbor Hub publicly"(`harbor run -d terminal-bench/terminal-bench-2-1 -a <agent> -m <provider/model> -k 5 ... --upload --public`)。来源:https://github.com/harbor-framework/terminal-bench-2-1
- Z.ai 数据卡对 2.1 的目标表述:"This modified version addresses environment and instruction issues we discovered in Terminal-Bench 2.0"(修复环境问题与指令-测试不一致,89 任务环境修复 + 11 任务指令修复)。来源:https://huggingface.co/datasets/zai-org/terminal-bench-2-verified