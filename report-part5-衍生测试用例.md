# Terminal-Bench 2.1 调研报告 · 第五部分:自制 3 道衍生测试用例(自验评测规则理解)

> 设计意图:这 3 道用例不是对资料的复述,而是从 Terminal-Bench 2.1 评测规则中"衍生"出的情景判断题,用以检验对规则的理解是否达到"能正确应用"的水平。每题给出情景、考察知识点、参考答案、判分标准四要素。依据:论文 arXiv:2601.11868、2.1 README、Harbor 文档、Z.ai 验证数据卡。

---

## 用例 1:结果驱动判定 —— "过程一团糟,结局恰恰好"

**情景**:某 agent 在任务 `cobol-modernization`(software-engineering,easy)中,轨迹记录显示:前 40 条命令全部以非零状态退出(比如误装包、反复 `cd` 失败、编译报错),但在第 41 条命令时它成功执行了一个一次性 Python 脚本,该脚本生成的文件在字节级与 GnuCOBOL 输出一致。随后 verifier 运行 `tests/test.sh`,全部编译与比对测试通过,并在 `/logs/verifier/reward.txt` 写入 `1`。

**考察知识点**(评测规则):Terminal-Bench 是 outcome-driven(结果驱动)框架——"The tests verify that all outcomes described in the instruction have been achieved by testing properties of the **final container state**; they do not test the agent's commands or console output"(论文 §2.1);2.x 判定以测试脚本写出的 reward 文件为准(Harbor 文档:reward.txt 整数/浮点,Harbor 读取判定)。

**参考答案**:该任务应判定为 **resolved(解决)**:虽命令过程充满失败,但判定只看最终容器状态属性与测试结果;reward.txt=1 ⇒ 该任务记为成功,计入 resolution rate。若 agent 修过测试脚本本身则另当别论(那构成 reward hacking 滥用,而 2.1 专门为此加固了 26 个任务),但本情景中测试是官方 verifier 运行的。

**判分标准**:答"resolved/通过/得 1 分"并说明"不检查过程命令,只看最终状态与测试"得满分;若答"因命令失败而不得分"则判定为未理解结果驱动规则。

---

## 用例 2:提交合规 —— "把超时翻 4 倍再只投 1 次,行不行?"

**情景**:某研究团队在本地用 Harbor 运行 `terminal-bench/terminal-bench-2-1` 时,发现自己的 agent 在 900 秒内经常差一步完成。于是他们把每个任务的 `[agent] timeout_sec` 从 900 改为 3600,`[environment] cpus` 从 1 改为 8,每任务只跑 1 次 trial,把得分最高的一次结果 `--upload --public` 提交到 2.1 排行榜。

**考察知识点**(评测规则):(a) 2.1 排行榜提交规则原文 "Note: submissions may not modify timeouts or resources"(tbench.ai leaderboard);(b) 2.1 README 要求 "you must run at least 5 trials per task and upload them to Harbor Hub publicly";(c) 标准任务配置为 `[agent] timeout_sec = 900.0`、`[verifier] timeout_sec = 900.0`、`build_timeout_sec = 600.0`、`cpus = 1`。

**参考答案**:该提交**不合规、不应被榜单接受**:修改 timeout 与资源违反"不得修改超时/资源"规则;每任务仅 1 次 trial 违反"至少 5 trials"要求(且自选最高一次提交构成选择性上报)。正确做法:保持任务原配置,`harbor run -d terminal-bench/terminal-bench-2-1 -a <agent> -m <provider/model> -k 5 ... --upload --public`,全部 trials 公开可查。

**判分标准**:答出"违规"并同时指出"改 timeout/资源"与"不足 5 trials/选择上报"两个违规点得满分;只答出其中一个得半分;答"合规"判定为未理解提交规则。

---

## 用例 3:难度分层与失败归因 —— "8 个模型只有 2 个解出来,到底难不难?"

**情景**:新任务 X 在 8 个前沿模型(N=8)上由 Terminus 2 统一评测,结果只有 2 个模型 resolved。同时,人工检查失败轨迹发现:多个失败轨迹中,模型在 `pip install` 报错后,连续 4 次重复执行完全相同的安装命令而不改变策略,最后声明"任务完成"并退出;verifier 运行测试全部失败。

**考察知识点**(评测规则):(a) 经验难度定义——"Easy if Terminus 2 resolves the task with ≥66.7% of the selected frontier models, Medium if the resolution rate lies between 33.3% and 66.7%, and Hard if the resolution rate is <33.3%"(论文 §4.3);(b) TAT 失败分类——"Step Repetition: re-executes the same phase without a meaningful strategy change"(Appendix C.1)、"Premature termination: declares completion before satisfying objectives"。

**参考答案**:分辨率 2/8 = 25% < 33.3% ⇒ 经验难度 **Hard**。失败轨迹同时命中 TAT 的 **Step Repetition(步骤重复,** Execution 类——重复同一命令未换策略**)与 **Premature termination(过早终止,** Verification 类——目标未满足即宣称完成**),且命令失败样本还对应论文 §4.5 的"调用不可用命令/安装失败"高发类别(可执行文件未装/不在 PATH 占命令失败 24.1%)。

**判分标准**:算出 25% 并正确映射到 Hard(阈值 <33.3%)得一半分;正确识别 Step Repetition 或 Premature termination 至少一类(并说出所属大类)得另一半分;两问全对得满分。

---

## 附:3 道用例与评测规则维度的对应关系(自验清单)

| 用例 | 覆盖的评测规则维度 | 依据来源 |
|---|---|---|
| 用例1 | 判定机制:结果驱动、最终容器状态、reward 文件评分 | 论文 §2.1;Harbor 文档 task-format |
| 用例2 | 超时配置(900s)、提交合规(不改 timeout/资源、≥5 trials 公开上传) | tbench.ai leaderboard;2.1 README |
| 用例3 | 经验难度阈值(≥66.7% / 33.3–66.7% / <33.3%);TAT 失败分类(Step Repetition、Premature termination) | 论文 §4.3、Appendix C.1 |

来源URL:
- https://ar5iv.labs.arxiv.org/html/2601.11868(论文:§2.1、§4.3、§4.5、Appendix C.1)
- https://tbench.ai/leaderboard/terminal-bench/2.1(提交规则原文)
- https://github.com/harbor-framework/terminal-bench-2-1(README:至少 5 trials、26 任务修改说明)
- https://harborframework.com/docs/task-format(reward 文件、timeout 配置)