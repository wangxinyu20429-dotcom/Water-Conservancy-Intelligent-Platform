# Water Conservancy Intelligent Platform

水利科研工作平台把项目文件、文献、科研知识和协作任务放到各自合适的位置，并用可追溯链接把它们连起来。

## Zotero 到证据卡 Skill

仓库包含可安装的 [`hydrology-evidence-cards`](skills/hydrology-evidence-cards/SKILL.md) Skill。它从本机 Zotero 只读取得指定来源和可用全文，按 Source—Claim—Decision 三层建立证据：来源版本只登记一次，Cxx 声明带全局 ID 和原文定位，平台判断写入第九张决策卡。V1.4要求把原文中的具体输入、模型或分析操作、中间输出、比较／验证和结论边界连成可复核的全文证据链。R09同时检查研究问题、对象、数据、方法、验证、结果、复现、边界、科研核心总深度和通用套话，不能再用摘要扩写或空标题冒充完整初读。详细合同见[human-readable-core.md](skills/hydrology-evidence-cards/references/human-readable-core.md)，原V1.2架构说明仍见[证据卡科学架构与 Zotero Skill 使用 V1.2](docs/证据卡规范/07_证据卡科学架构与Zotero_Skill使用_V1.2.md)。
## 证据卡到主题 Skill

[`hydrology-theme-synthesis`](skills/hydrology-theme-synthesis/SKILL.md) 把选定证据卡中的 L2/L3、已核 Claim 组织成主题问题、边界、比较框架、发展脉络和研究现状；再分开判断来源的科学作用与前沿关注优先级，并把承重缺口反馈到原证据卡补核。新近性占25%、经核的学科归一期刊信号占15%，两项只影响“先读、先核、先跟踪”的顺序，不改变 Claim 可信度。入口见[十二步闭环工作流](docs/主题规范/02_证据卡到主题闭环工作流_V1.0.md)，成品结构见[水利科研主题模板](docs/主题模板/01_水利科研主题模板_V1.0.md)。

## 科研平台集合真实运行成果

Zotero“科研平台”集合42个唯一来源各有一张独立证据卡，并由主题Skill形成5个候选主题。2026-09-08已按V1.4深化：37张取得Zotero索引正文的L1卡逐篇补写了来源特定的全文证据链，明确数据怎样进入方法、方法怎样产生结果、作者做了什么比较以及结论在哪里失效；1张L2详细草稿保留更完整的数据、算法、结果和逐条审计；3条官方网页与1条仅题录来源按真实材料范围写卡，不虚构论文式方法和结果。全部仍待课题组成员逐表逐图复核，因此候选主题只用于确定精读顺序和补证据任务，不能直接作为论文结论或创新性声明。

- [42张证据卡总索引](证据卡/科研平台集合_20260907/README.md)
- [5个候选主题与主题关系](主题/候选主题_科研平台集合_20260907/README.md)
- [本次读取、校验和停止条件](运行记录/ZOTERO-RUN-20260907-01_科研平台集合全量初读与候选主题.md)
- [首篇L2详细草稿：城市洪涝关键设施可达性](证据卡/EC-20260907-001_Gangwal_Dong_城市洪涝关键设施可达性.md)

本批次没有把PDF、Zotero数据库或本机路径提交到Git。期刊影响因子没有统一且可审计的来源，因此没有猜测具体数值；年份和来源类型只用于安排先读顺序。
## 从这里开始

1. 阅读[产品说明](docs/产品与流程/01_产品说明_V0.5.md)，理解系统边界。
2. 按[科研工作操作手册](docs/产品与流程/02_科研工作操作手册_V0.5.md)执行T01：建立OneDrive目录并确认四处入口。
3. 在[工作入口与开始记录](docs/产品与流程/03_工作入口与开始记录_V0.5.md)填写真实地址、权限和本轮材料。
4. 按[任务与里程碑](docs/产品与流程/05_里程碑与任务顺序_V0.5.md)推进，并在本仓库[Issues](https://github.com/wangxinyu20429-dotcom/Water-Conservancy-Intelligent-Platform/issues)提交实际交付和阻碍。

## 工具分工

| 位置 | 保存内容 |
| --- | --- |
| OneDrive | 项目原件、RAW/INTERIM/PROCESSED数据、运行记录、图表和正式交付 |
| Zotero | 题录、DOI、合法PDF/附件、版本关系和原文批注 |
| Obsidian | 本仓库的本地副本；用于写证据卡、主题、问题和创新候选 |
| 本GitHub仓库 | 可共享的Markdown、规则、任务、修改历史和评议记录 |

GitHub不保存项目原始数据、文献全文、Zotero数据库、凭据或个人机器路径。文件入口可打开不等于科研结论已经核验。

## 文档结构

- [产品与流程](docs/产品与流程)：产品说明、操作手册、入口记录、填写模板、任务顺序和验收。
- [证据卡模板](docs/证据卡模板)：公共骨架、八类独立来源入口和第九张平台综合决策卡；Skill 装配后每个来源仍输出一个独立 Markdown。
- [证据卡模块](docs/证据卡模块)：公共水利情境及预测、模拟、频率气候、监测遥感、工程安全方法模块。
- [证据卡规范](docs/证据卡规范)：V1.2 科学架构、外部实践对照、原文忠实性和质量检查。
- [主题模板](docs/主题模板)：一份主题档案的完整事实源模板。
- [主题规范](docs/主题规范)：外部实践对照、十二步生成、文献排序和原卡反馈闭环。
- [可安装 Skills](skills)：供其他成员复制接入的可执行科研工作流。
- [证据卡](证据卡)：单篇来源证据卡和批次索引。
- [主题](主题)：由证据卡生成的候选主题、阅读优先级和反向补核队列。
- [运行记录](运行记录)：每次真实读取的输入范围、交付、检查结果和停止条件。
- [图与形成依据](docs/图与形成依据)：可编辑实体架构图及预览图。
- [迁移说明](MIGRATION.md)：旧Project内容与本仓库的对应关系。

## 当前任务

| 任务 | 内容 | 里程碑 |
| --- | --- | --- |
| [T01](https://github.com/wangxinyu20429-dotcom/Water-Conservancy-Intelligent-Platform/issues/1) | 建立OneDrive目录并确认Zotero、Obsidian与GitHub入口 | M0 |
| [T02](https://github.com/wangxinyu20429-dotcom/Water-Conservancy-Intelligent-Platform/issues/2) | 把一份真实材料收进Zotero并登记文献链接 | M0 |
| [T03](https://github.com/wangxinyu20429-dotcom/Water-Conservancy-Intelligent-Platform/issues/3) | 为唯一来源版本建立真实 L0—L3 卡、Cxx 定位、人审和 R01—R09 结果 | M1 |
| [T04](https://github.com/wangxinyu20429-dotcom/Water-Conservancy-Intelligent-Platform/issues/4) | 用主题Skill完成Claim准入、比较框架、发展脉络、研究现状和关键文献排序 | M1 |
| [T05](https://github.com/wangxinyu20429-dotcom/Water-Conservancy-Intelligent-Platform/issues/5) | 用主题反推原卡承重缺口，按三门触发最小补核并重算主题 | M1 |
| [T06](https://github.com/wangxinyu20429-dotcom/Water-Conservancy-Intelligent-Platform/issues/6) | 从已核主题声明生成机会信号和写作接口，不自动宣称新颖性 | M1 |
| [T07](https://github.com/wangxinyu20429-dotcom/Water-Conservancy-Intelligent-Platform/issues/7) | 将Obsidian知识文件同步到集体GitHub并检查链接 | M1 |
| [T08](https://github.com/wangxinyu20429-dotcom/Water-Conservancy-Intelligent-Platform/issues/8) | 用真实材料检查整条流程并记录未通过的环节 | M1 |
| [T09](https://github.com/wangxinyu20429-dotcom/Water-Conservancy-Intelligent-Platform/issues/9) | 修复真实发现的问题，并回到出错步骤复验 | M2 |

里程碑：[M0](https://github.com/wangxinyu20429-dotcom/Water-Conservancy-Intelligent-Platform/milestone/1) · [M1](https://github.com/wangxinyu20429-dotcom/Water-Conservancy-Intelligent-Platform/milestone/2) · [M2](https://github.com/wangxinyu20429-dotcom/Water-Conservancy-Intelligent-Platform/milestone/3)

## 当前状态

V0.5文档和任务定义已经迁入本仓库。Zotero“科研平台”集合的42个唯一来源已完成首轮证据卡筛查和候选主题生成；下一步按主题优先级进行人工源文复核，再重新计算主题。OneDrive入口、项目数据和共享权限仍按T01逐项登记。
