# Terminal-Bench 2.1 调研报告 · 第一部分:任务分类体系

> 版本说明:Terminal-Bench 2.1 是 Terminal-Bench 2.0 的"更严格验证版"数据集(同名 89 任务,其中 26 个被修改修复),无独立论文;分类体系与任务构成继承自论文 arXiv:2601.11868(Terminal-Bench 2.0)。
> 来源:https://github.com/harbor-framework/terminal-bench-2-1 ; https://ar5iv.labs.arxiv.org/html/2601.11868 ; https://terminal-bench.com/

## 1. 任务领域分类(16 个 category,共 89 个任务)

分类由任务作者自报(论文 Figure 4 图注:"Categories were assigned by the task author")。逐类数量按论文 Appendix H 的 89 行任务表逐条统计(COUNT=89 全部对上),任务目录在官方仓库 `laude-institute/terminal-bench-2` 与 `harbor-framework/terminal-bench-2-1` 中同名存在。

| 类别(Category) | 任务数 | 占比 | 代表性任务(官方仓库同名任务目录) |
|---|---|---|---|
| Software Engineering | 26 | 29.2% | cobol-modernization、path-tracing、write-compressor、torch-tensor-parallelism 等 |
| System Administration | 9 | 10.1% | mailman、nginx-request-logging、qemu-alpine-ssh、install-windows-3.11 |
| Scientific Computing | 8 | 9.0% | adaptive-rejection-sampler、dna-assembly、raman-fitting、tune-mjcf |
| Security | 8 | 9.0% | break-filter-js-from-html、crack-7z-hash、password-recovery、openssl-selfsigned-cert |
| Data Science | 8 | 9.0% | hf-model-inference、mcmc-sampling-stan、mteb-leaderboard、sam-cell-seg |
| Debugging | 5 | 5.6% | custom-memory-heap-crash、overfull-hbox、sqlite-db-truncate |
| File Operations | 5 | 5.6% | db-wal-recovery、extract-elf、gcode-to-text、large-scale-text-editing |
| Model Training | 4 | 4.5% | train-fasttext、pytorch-model-cli、count-dataset-tokens |
| Mathematics | 4 | 4.5% | feal-differential-cryptanalysis、largest-eigenval |
| Data Processing | 4 | 4.5% | log-summary-date-ranges、regex-log、financial-document-processor |
| Machine Learning | 3 | 3.4% | caffe-cifar-10、distribution-search、llm-inference-batching-scheduler |
| Games | 1 | 1.1% | chess-best-move |
| Personal Assistant | 1 | 1.1% | constraints-scheduling |
| Optimization | 1 | 1.1% | portfolio-optimization |
| Data Querying | 1 | 1.1% | sparql-university |
| Video Processing | 1 | 1.1% | video-processing |

合计 = 89 任务。论文摘要原文:"a set of 89 challenging tasks"。来源:https://ar5iv.labs.arxiv.org/html/2601.11868(§2.2、Figure 4、Appendix H)

## 2. 难度分层

- 作者估计难度(论文 §4.3 原文):"Each task in Terminal-Bench 2.0 includes an author-estimated difficulty for a human to complete the task (medium or hard)"。
- 经验难度(empirical difficulty,与作者难度不同,基于 Terminus 2 在前沿模型上的平均通过率,论文原文):"Easy if Terminus 2 resolves the task with ≥66.7% of the selected frontier models, Medium if the resolution rate lies between 33.3% and 66.7%, and Hard if the resolution rate is <33.3%"。
- 按论文 Appendix H 逐任务难度标签统计(非论文原表,据附录解析):Medium 55 个、Hard 30 个、Easy 4 个(Easy 任务:cobol-modernization、fix-git、overfull-hbox、prove-plus-comm)。
- 人估难度与经验难度相关性:r = 0.436, p < 0.001;93.3% 的人类 hard 任务在经验上也是 hard;最大分歧是人类标 medium 而模型觉得 hard(54.5%)。
- 来源:https://ar5iv.labs.arxiv.org/html/2601.11868(§4.3、Appendix H)

## 3. 任务构成要素(五元组)

论文 §2.1 原文:"A Terminal-Bench task consists of an instruction, a Docker image, a set of tests, an example solution, and a time limit (Figure 2). The instruction describes the task that the agent must complete within the specified time limit in the Docker container. The tests verify that all outcomes described in the instruction have been achieved by testing properties of the **final container state**; they do not test the agent's commands or console output." —— 即:指令(instruction)+ Docker 镜像 + 测试集(tests)+ 示例解(example/oracle solution)+ 时限(time limit);结果是"outcome-driven"(结果驱动):只检查最终容器状态,不检查过程。

2.x 版任务的 Harbor 格式长这样(官方仓库抓取的真实 task.toml 实例 `adaptive-rejection-sampler/task.toml`):

```toml
schema_version = "1.1"
[task]
name = "terminal-bench/adaptive-rejection-sampler"
[metadata]
difficulty = "medium"
category = "scientific-computing"
[verifier]
timeout_sec = 900.0
[agent]
timeout_sec = 900.0
[environment]
docker_image = "alexgshaw/adaptive-rejection-sampler:20251031"
cpus = 1
memory_mb = 2048
storage_mb = 10240
allow_internet = true
```

任务目录结构(官方 Harbor 文档 "Task Structure" 原文):`instruction.md / task.toml / environment/ (Dockerfile ...) / solution/ (solve.sh ...) / tests/ (test.sh ...)`。来源:https://harborframework.com/docs/task-format ; 任务文件原文:https://github.com/laude-institute/terminal-bench-2/blob/main/adaptive-rejection-sampler/task.toml

v1 版(original-tasks)额外字段含 `parser_name`(pytest/python)、`max_agent_timeout_sec`(默认 360s)、`max_test_timeout_sec`(默认 60s)、`run_tests_in_same_shell` 等。来源:https://deepwiki.com/laude-institute/terminal-bench/1.2-key-concepts ; https://github.com/harbor-framework/terminal-bench-1