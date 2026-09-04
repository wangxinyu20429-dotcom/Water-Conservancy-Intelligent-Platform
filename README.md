# Water Conservancy Intelligent Platform

水利科研工作平台把项目文件、文献、科研知识和协作任务放到各自合适的位置，并用可追溯链接把它们连起来。

## Zotero 到证据卡 Skill

仓库包含可安装的 [`hydrology-evidence-cards`](skills/hydrology-evidence-cards/SKILL.md) Skill。它从本机 Zotero 只读获取指定来源和可用全文，按原文生成八类可追溯证据卡，围绕问题、证据生成机制、决定性声明、推断边界和研究决策组织。八个在Obsidian中直接可见的独立Markdown位于[证据卡模板](docs/证据卡模板)，使用入口见[证据卡科学架构与 Zotero Skill 使用 V1.1](docs/证据卡规范/07_证据卡科学架构与Zotero_Skill使用_V1.1.md)。

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
- [证据卡模板](docs/证据卡模板)：八类来源各一个完整Markdown模板。
- [证据卡规范](docs/证据卡规范)：分类说明、Zotero Skill、原文忠实性和质量检查。
- [可安装 Skills](skills)：供其他成员复制接入的可执行科研工作流。
- [图与形成依据](docs/图与形成依据)：可编辑实体架构图及预览图。
- [迁移说明](MIGRATION.md)：旧Project内容与本仓库的对应关系。

## 当前任务

| 任务 | 内容 | 里程碑 |
| --- | --- | --- |
| [T01](https://github.com/wangxinyu20429-dotcom/Water-Conservancy-Intelligent-Platform/issues/1) | 建立OneDrive目录并确认Zotero、Obsidian与GitHub入口 | M0 |
| [T02](https://github.com/wangxinyu20429-dotcom/Water-Conservancy-Intelligent-Platform/issues/2) | 把一份真实材料收进Zotero并登记文献链接 | M0 |
| [T03](https://github.com/wangxinyu20429-dotcom/Water-Conservancy-Intelligent-Platform/issues/3) | 按材料类型填写证据卡，并逐条对照原文复查 | M1 |
| [T04](https://github.com/wangxinyu20429-dotcom/Water-Conservancy-Intelligent-Platform/issues/4) | 把证据卡用于具体主题，写清比较条件和认识变化 | M1 |
| [T05](https://github.com/wangxinyu20429-dotcom/Water-Conservancy-Intelligent-Platform/issues/5) | 回答实际研究问题，缺证据时安排有目标的补读 | M1 |
| [T06](https://github.com/wangxinyu20429-dotcom/Water-Conservancy-Intelligent-Platform/issues/6) | 在主题中记录创新点候选、依据和下一项验证 | M1 |
| [T07](https://github.com/wangxinyu20429-dotcom/Water-Conservancy-Intelligent-Platform/issues/7) | 将Obsidian知识文件同步到集体GitHub并检查链接 | M1 |
| [T08](https://github.com/wangxinyu20429-dotcom/Water-Conservancy-Intelligent-Platform/issues/8) | 用真实材料检查整条流程并记录未通过的环节 | M1 |
| [T09](https://github.com/wangxinyu20429-dotcom/Water-Conservancy-Intelligent-Platform/issues/9) | 修复真实发现的问题，并回到出错步骤复验 | M2 |

里程碑：[M0](https://github.com/wangxinyu20429-dotcom/Water-Conservancy-Intelligent-Platform/milestone/1) · [M1](https://github.com/wangxinyu20429-dotcom/Water-Conservancy-Intelligent-Platform/milestone/2) · [M2](https://github.com/wangxinyu20429-dotcom/Water-Conservancy-Intelligent-Platform/milestone/3)

## 当前状态

V0.5文档和任务定义已经迁入本仓库。实际OneDrive目录、真实项目、共享权限、Zotero集合和第一份材料仍须从T01开始执行；迁移文档不改变任务完成状态。
