# Terminal-Bench 2.1 调研报告 · 第四部分:常见模型失败样本类型

> 来源:论文(arXiv:2601.11868,Terminal-Bench 2.0/2.1 的官方论文)§4.4/§4.5 + Appendix C/E;Terminal-Bench 2.1 README;Z.ai Terminal-Bench 2.0 Verified 数据集卡。

## 1. 轨迹级失败分类(论文 TAT —— Terminal Agent Taxonomy,9 类)

论文对模型轨迹做错误分析,基于 MAST(Multi-Agent System Taxonomy)构建简化分类,三大类 + 九小类(Appendix C.1 原文定义):

**Execution(执行类)**
1. **Disobey Specification(违反规格)**:直接违背任务的显式指令要求。
2. **Step Repetition(步骤重复)**:无意义地重复执行同一阶段,未采用新策略(含 abort-loops)。
3. **Unaware of termination conditions(不知终止条件)**:超过合理停止点仍继续行动。

**Coherence(一致性类)**
4. **Reasoning-Action Mismatch(推理-行动不一致)**:陈述的推理与实际动作/日志/产物矛盾。
5. **Context Loss(上下文丢失)**:遗忘或自相矛盾地对待近期上下文。
6. **Task Derailment(任务偏离)**:偏离既定目标。

**Verification(验证类)**
7. **Premature termination(过早终止)**:在满足目标之前就宣称完成。
8. **No or incorrect Verification(无验证或错误验证)**:未经实质性检查就标记完成或绕过验证器。
9. **Weak Verification(验证薄弱)**:依赖的验证未覆盖任务关键性质(测试假通过)。

统计结论(论文原文):"Execution errors dominate for Opus 4.5 and GPT-5.2, while coherence and verification errors occur at lower rates. Conversely, the open sourced model evaluated (Qwen Coder) displays a more balanced error pattern"。标注方法:Docent + 自研 pipeline 标注,GPT-5(high-reasoning)为主判官,与 120 条人工标注一致率 90%。

## 2. 命令级失败统计(论文 §4.5 + Appendix E)

- 论文原文:"command failures calling executables that are not installed or not in PATH are the most frequent (24.1% of all failures) followed by failures when running executables (9.6%)"——**最常见的失败样本类型是:调用的可执行文件未安装或不在 PATH(占全部命令失败的 24.1%)**,其次是运行可执行文件时报错(9.6%)。
- 模型间命令错误率:9.2%(Grok 4)~ 26.7%(GPT-OSS-120B);3,800 个失败命令被均匀采样分类。
- Appendix E.2 命令失败一级类别:Invocation & CLI;Filesystem & Permissions;Environment & Configuration;Build, Toolchain & Packages;Packages & repositories;Network & Remote Access;Runtime, Interpreters & Processes;Interpreters & REPLs;Services & platforms;Data & Formats;Testing & Quality。典型叶节点原文示例:"A required utility is not installed or not in PATH; this does not include wrong versions."、"A file not found ... A referenced regular file does not exist and cannot be opened"、"DNS resolution failure: Hostnames cannot be resolved"、"Process crash / segmentation fault"、"Assertion or spec violation: A test fails because outputs or invariants do not match expectations"。

## 3. v1 侧失败模式机制(FailureMode)

- DeepWiki 原文:"When a task is not resolved, a failure mode categorizes why it failed. This distinction helps separate task quality issues from agent limitations."——未解决任务按 failure mode 归类:Agent 执行阶段捕获 timeout/context length/agent errors;测试执行阶段捕获 timeout;全部通过则为 FailureMode.NONE。

## 4. Terminal-Bench 2.1 修复的"失败样本"问题(26 个被修改任务)

- 2.1 README 原文:"26 tasks were modified to fix bugs, modify timeouts or resources, or improve robustness to reward hacking. Many changes were taken directly from Z.ai's Terminal-Bench 2.0 Verified changes"——即 2.1 修改任务的三大原因:**修 bug、调整超时/资源、提高对 reward hacking 的稳健性**(防止作弊式"奖励黑客":让 verifier 误判通过的技巧)。
- Z.ai 验证工作(数据集卡原文):environment fixes(更新 Dockerfiles 与指令以支持 Claude Code Agent 运行环境,89 个任务)与 instruction fixes(修正指令与测试不一致,11 个任务);2026.08.18 再评审修复 6 个任务:Grading/Test Fixes 4 个(dna-insert、make-doom-for-mips、filter-js-from-html、install-windows-3.11——verifier "misjudged valid submissions"(假阴性)或"let non-compliant outputs through"(假阳性));Instruction Fixes 2 个(pytorch-model-cli、raman-fitting——测试隐含约定未写进指令)。——**典型的"失败样本"还包括评测自身的假阳性/假阴性**,这正是模型分数被高估/低估的来源。
- 论文 Limitations 提到的作弊/污染风险(原文):"In theory, an agent could locate our dataset and cheat by reading the oracle solutions. In practice, we have not observed this behavior";"We include the Big-Bench canary string in each file in our repository to aid in training corpus decontamination."——即**读 oracle 解作弊、训练语料污染**也是失败/失真样本的来源之一。

## 5. 失败类型小结表

| 层面 | 失败样本类型 | 关键统计/出处 |
|---|---|---|
| 轨迹(Execution) | 违反规格、步骤重复、不知终止条件 | TAT(论文 Appendix C.1) |
| 轨迹(Coherence) | 推理-行动错位、上下文丢失、任务偏离 | TAT(论文 Appendix C.1) |
| 轨迹(Verification) | 过早终止、无/错误验证、验证薄弱 | TAT(论文 Appendix C.1) |
| 命令 | 可执行文件未装/不在 PATH | 24.1% 全部命令失败(论文 §4.5) |
| 命令 | 运行可执行文件失败 | 9.6%(论文 §4.5) |
| 机制 | timeout / context length | v1 FailureMode(DeepWiki) |
| 数据集 | 指令-测试不一致、verifier 假阳/假阴性 | Z.ai Verified 修复清单 |
| 稳健性 | reward hacking、读 oracle 作弊 | 2.1 README、论文 Limitations |

来源URL:
- https://ar5iv.labs.arxiv.org/html/2601.11868(论文全文:§4.4、§4.5、Appendix C.1、Appendix E.2、Limitations)
- https://github.com/harbor-framework/terminal-bench-2-1(README:"26 tasks were modified ...")
- https://huggingface.co/datasets/zai-org/terminal-bench-2-verified(Z.ai 数据集卡)
- https://deepwiki.com/laude-institute/terminal-bench/1.2-key-concepts(FailureMode)