# 八类独立证据卡模板与 Zotero Skill 使用 V1.0

2026-09-04。本文件是使用入口；八类模板的正式可复制版本位于仓库 `skills/hydrology-evidence-cards/assets/templates/`。每种来源一个独立 Markdown，不再从总说明中手工拼装。

## 八个独立模板

1. [原创研究](../../skills/hydrology-evidence-cards/assets/templates/01_original-research.md)
2. [综述与证据综合](../../skills/hydrology-evidence-cards/assets/templates/02_review-synthesis.md)
3. [调查、监测与统计报告](../../skills/hydrology-evidence-cards/assets/templates/03_survey-monitoring-statistics.md)
4. [工程项目报告](../../skills/hydrology-evidence-cards/assets/templates/04_engineering-report.md)
5. [图书与章节](../../skills/hydrology-evidence-cards/assets/templates/05_book-chapter.md)
6. [标准、指南与政策](../../skills/hydrology-evidence-cards/assets/templates/06_standard-guideline-policy.md)
7. [数据集及数据产品](../../skills/hydrology-evidence-cards/assets/templates/07_dataset-data-product.md)
8. [软件、模型与代码](../../skills/hydrology-evidence-cards/assets/templates/08_software-model-code.md)

每个文件都能单独复制使用，并完整包含公共字段、类型专属字段、声明—原文定位、使用边界和复查记录。`01_八类证据卡分类与填写说明_V0.4.md`继续解释分类原理；本文件负责进入可执行模板。

## Skill 能做什么

`skills/hydrology-evidence-cards/`是一套可复制安装的 Codex Skill。它通过 Zotero Desktop 本地只读 API：

1. 查找并消歧指定条目；
2. 读取题录、子附件和 Zotero 已索引全文；
3. 判断八类主模板，不能可靠判断时保留待分类；
4. 建立带 Zotero key、来源版本和阅读范围的独立卡片；
5. 按原文提取 Cxx 声明、对象、条件、数字、单位、不确定性和位置；
6. 区分来源事实、作者解释、忠实归纳和本方判断；
7. 检查必需结构和未清理占位符；
8. 明确提示结构通过不等于科学正确。

Skill 不进行无边界文献搜索，不删除或修改 Zotero 条目，不把全文上传 Git，也不因一张卡完成就自动建立主题、创新点或正式选题。

## 单篇操作

1. 在 Zotero 核对来源身份和实际附件。
2. 明确本轮问题，并确认库中没有同源同版的正式卡。
3. 调用 `$hydrology-evidence-cards`，提供题名、DOI或 item key、研究问题和输出目录。
4. Skill 建立临时读取包；临时全文不进入 Git。
5. Skill 根据来源实际目的选择模板，先填写身份和阅读范围，再读方法、结果、局限。
6. 每条将用于后续判断的声明写入 Cxx 表，并给具体位置。
7. 运行 final 结构校验，再逐条对照原文复查。
8. 只提交证据卡及允许分享的链接；PDF、Zotero数据库和临时包留在原处。

完整操作、安装和失败处理见 Skill 的 `SKILL.md` 与 `references/`。

## 验收

- [ ] 选择了一个有理由的主类型，没有只按文件后缀或发布机构分类。
- [ ] 一个来源同一版本只有一张正式卡。
- [ ] Zotero item key、来源版本和实际阅读范围已填。
- [ ] 主要声明都能回到页、节、图、表、条款、变量或代码位置。
- [ ] 数值保留对象、时间、尺度、分母、单位、比较和不确定性。
- [ ] 二次转述没有冒充已核原始研究。
- [ ] 缺失、未读、不适用和冲突使用不同状态。
- [ ] 可支持、只能作为线索和不能支持的内容都写清。
- [ ] final 校验通过，且已完成真实原文复查。
- [ ] Git 中没有全文、数据、凭据和本机缓存。
