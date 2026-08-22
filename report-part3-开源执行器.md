# Terminal-Bench 2.1 调研报告 · 第三部分:开源执行器(评测运行框架/Harness)

## 1. Harbor —— 官方评测执行器(Terminal-Bench 2.1 的官方 runner)

- **名称**:Harbor(评测与优化 agent 的官方框架)
- **作者组织**:harbor-framework(Terminal-Bench 官方团队;README 指出安装 Harbor 以运行 2.1)
- **仓库 URL**:https://github.com/harbor-framework/harbor
- **安装**(2.1 README 原文):`uv tool install "harbor[daytona]"`(daytona 为云沙箱 provider 可选依赖,可并行化;其它选项见 `harbor run --help`);登录:`harbor auth login`
- **运行 Terminal-Bench 2.1 的命令**(2.1 README 原文,提交排行榜要求"at least 5 trials per task and upload them to Harbor Hub publicly"):

```shell
harbor run -d terminal-bench/terminal-bench-2-1 \
  -a <agent> \
  -m <provider/model> \
  --ak reasoning_effort=<effort> \
  -e <sandbox> \
  -k 5 \
  -n <concurrency> \
  --upload \
  --public
```

参数含义:`-d` 数据集名(terminal-bench/terminal-bench-2-1)、`-a` agent、`-m` 模型 provider/model、`--ak` 附加参数(如推理强度)、`-e` 沙箱、`-k` 每个任务 trials 次数(排行榜至少 5)、`-n` 并发数、`--upload`/`--public` 公开上传 Harbor Hub;补传命令 `harbor upload <job-dir> --public`;提交 PR 流程:克隆 https://github.com/harbor-framework/terminal-bench-2-1 后 `cd leaderboard && uv run lb submit <job-url>`。
- **tbench.ai 官方运行指引额外命令**(原文转写):冒烟测试 `harbor run -d terminal-bench/terminal-bench-2-1 -a oracle -l 5`;带 agent 运行 `harbor run -d terminal-bench/terminal-bench-2-1 -a claude-code -m anthropic/claude-opus-4-1 -k 5`;云沙箱并行 `... --env daytona -n 32 -k 5`;自定义 agent `harbor run -d terminal-bench/terminal-bench-2-1 --agent-import-path "path.to.agent:SomeAgent" -k 5`;单任务 `--include-task-name "<task-name>"`。
- **核心功能**(Harbor 文档 https://harborframework.com/docs/task-format):容器化环境运行(task.toml 配置 [task]/[metadata]/[verifier]/[agent]/[environment]);超时控制(agent/verifier timeout_sec=900、build_timeout_sec=600);验证器读取 reward 文件判定(reward.txt 整数/浮点或 reward.json 多指标,默认同容器验证,可用 environment_mode="separate" 独立打分环境);多步奖励策略 multi_step_reward_strategy: "mean"|"final"|null。
- **信息来源**:https://github.com/harbor-framework/terminal-bench-2-1(README,本地抓取 tb_sources/tb21_README.md)、https://tbench.ai/docs/run-terminal-bench-2-1(本地抓取 tb_sources/tbench_run21.txt)、https://harborframework.com/docs/task-format

## 2. terminal-bench pip 包(tb CLI)—— 官方 1.x 执行器(harness)

- **名称**:terminal-bench(发布为 pip 包,CLI 为 `tb`)
- **作者组织**:laude-institute(现仓库 harbor-framework/terminal-bench-1,原 laude-institute/terminal-bench)
- **仓库/PyPI URL**:https://github.com/harbor-framework/terminal-bench-1 ;PyPI: `pip install terminal-bench`(或 `uv tool install terminal-bench`)
- **运行命令**(README 原文):

```bash
tb run \
    --agent terminus \
    --model anthropic/claude-3-7-latest \
    --dataset-name terminal-bench-core \
    --dataset-version 0.1.1 \
    --n-concurrent 8
```

- **功能与构成**(README 原文):"Terminal-Bench consists of two parts: a **dataset of tasks**, and an **execution harness** that connects a language model to our terminal sandbox."——(a) 任务数据集(每任务含英文指令 instruction、验证完成情况的 test script、参考 oracle 解);(b) 执行 harness:连接语言模型到沙箱终端环境,依赖 uv 和 Docker;`tb run --help` 查看全部选项;判定规则:所有 tests 返回 UnitTestStatus.PASSED 即 resolved(DeepWiki: https://deepwiki.com/laude-institute/terminal-bench/1.2-key-concepts)。
- **信息来源**:https://github.com/harbor-framework/terminal-bench-1(README,本地抓取 tb_sources/tb1_README.md)、https://deepwiki.com/laude-institute/terminal-bench/1.2-key-concepts

## 3. EvalScope —— 第三方评测框架(Terminal-Bench 2.1 支持)

- **名称**:EvalScope(MLOps/LLM 评测框架,阿里 ModelScope 团队)
- **作者组织**:modelscope / Alibaba
- **文档 URL**:https://evalscope.readthedocs.io/zh-cn/latest/benchmarks/terminal_bench_v2_1.html(官方文档设专门 "Terminal-Bench-2.1" 基准页;源码文档 https://github.com/modelscope/evalscope/blob/main/docs/en/benchmarks/terminal_bench_v2_1.md )
- **功能**:作为第三方框架将 Terminal-Bench 2.1 接入评测流水线(提供基准适配与配置化评测入口),与官方 Harbor 执行器互为补充。
- **信息来源**:https://evalscope.readthedocs.io/zh-cn/latest/benchmarks/terminal_bench_v2_1.html 、https://github.com/modelscope/evalscope

## 4. 小结

| 执行器 | 组织 | 类型 | 2.1 支持方式 | 仓库/文档 |
|---|---|---|---|---|
| Harbor | harbor-framework | 官方 runner | `harbor run -d terminal-bench/terminal-bench-2-1 ...` | https://github.com/harbor-framework/harbor |
| terminal-bench (tb) | laude-institute→harbor-framework | 官方 1.x harness | 1.x 数据集(2.1 由 Harbor 承接) | https://github.com/harbor-framework/terminal-bench-1 |
| EvalScope | modelscope | 第三方框架 | 专门 2.1 基准页 | https://evalscope.readthedocs.io/zh-cn/latest/benchmarks/terminal_bench_v2_1.html |