---
card_schema: "evidence-card-v1.1"
card_id: "{{CARD_ID}}"
evidence_type: "review-synthesis"
status: "draft"
zotero_item_key: "{{ZOTERO_KEY}}"
source_version: "{{SOURCE_VERSION}}"
reading_scope: "metadata_only"
source_provenance: "local_zotero"
direct_source_verified: false
created_at: "{{CREATED_AT}}"
updated_at: "{{CREATED_AT}}"
---

# 综述与证据综合证据卡：{{TITLE}}

> 本卡评价的是“这次综合怎样形成结论”，不是把综述中的每句话当成已独立核验的事实。引用单篇原始研究时，必须说明是否打开了原始来源。

## 导师三分钟判断

- 当前综合问题：{{REVIEW_QUESTION}}
- 这份综述可能影响的决定：{{INTENDED_DECISION}}
- 综述类型：系统综述／范围综述／证据图谱／Meta分析／叙述综述／其他：{{TYPE}}
- 证据宇宙：{{DATABASE_DATE_LANGUAGE_GREY_LITERATURE}}
- 纳入证据规模与真正独立单位：{{STUDIES_DATASETS_POPULATIONS}}
- 最关键综合结果：{{EFFECT_OR_PATTERN_WITH_UNCERTAINTY}}
- 最大边界：{{LOAD_BEARING_LIMIT}}
- 使用结论：可直接使用／限条件使用／仅作线索／暂不可用／与当前问题无关：{{WHY}}

### 决定性综合结论（最多三项）

| 声明 | 综合结果 | 异质性／确定性／范围 | 定位 |
| --- | --- | --- | --- |
| C01 | {{SYNTHESIS_RESULT}} | {{CERTAINTY_AND_SCOPE}} | {{LOCATOR}} |

## 来源身份与阅读边界

- 题名：{{TITLE}}
- 作者／组织：{{CREATORS}}
- 年份、版本与发表状态：{{DATE}}；{{VERSION_RELATION}}
- DOI／官方页面：{{DOI}}；{{URL}}
- Zotero item key：{{ZOTERO_KEY}}
- 协议、注册或预先计划：{{PROTOCOL_REGISTRATION}}
- 更新、勘误、撤稿或旧版关系：{{VERSION_CHECK}}
- 实际取得并阅读：{{READ_MATERIALS}}
- 未阅读或未取得：{{UNREAD_OR_MISSING}}
- 定位规则：{{LOCATOR_RULE}}

## 研究或使用问题

- 综述明确的问题结构：研究对象／暴露或干预／比较／结果／情境：{{QUESTION_STRUCTURE}}
- 本卡要核的决策问题：{{CARD_QUESTION}}
- 目标不是“综述了什么”，而是要判断：{{DECISION_TEST}}

## 证据综合如何形成

### 检索与筛选边界

- 检索库、平台、网站和其他来源：{{SOURCES}}
- 末次检索日期、语言、文献类型和时间限制：{{SEARCH_BOUNDARY}}
- 纳入排除标准：{{ELIGIBILITY}}
- 去重、双人筛选、冲突解决和流程数量：{{SCREENING_PROCESS_COUNTS}}
- 未检索或排除的证据域及其可能影响：{{MISSING_EVIDENCE_DOMAIN}}

### 证据单位、提取与偏倚

- 纳入研究数、报告数、数据集数、样本或流域数：{{EVIDENCE_UNITS}}
- 多报告、共享数据、重复样本或同一模型家族怎样处理：{{OVERLAP_AND_INDEPENDENCE}}
- 数据提取和核对方式：{{EXTRACTION}}
- 单项研究偏倚／质量工具及结果：{{RISK_OF_BIAS}}
- 发表偏倚、选择性报告或小样本效应：{{REPORTING_BIAS}}
- 研究类型是否适合该工具；报告完整性是否被误当作研究质量：{{APPRAISAL_FIT}}

### 综合模型与可比性

- 哪些研究被合并，哪些没有，理由是什么：{{GROUPING}}
- 效应量、方向、单位、换算和权重：{{EFFECT_MEASURE_WEIGHTING}}
- 固定／随机／层级／叙述综合及其假设：{{SYNTHESIS_MODEL}}
- 异质性、亚组、调节变量和敏感性分析：{{HETEROGENEITY}}
- 证据确定性或结论置信度怎样形成：{{CERTAINTY_METHOD}}

## 决定性证据块

### C01｜{{ATOMIC_SYNTHESIS_CLAIM}}

- 声明性质与推断类型：综合事实／综述作者解释／本方判断；描述／比较／关联／因果／预测／机制
- 原文综合结果：{{SOURCE_FACT}}
- 证据基础：{{NUMBER_AND_TYPE_OF_STUDIES_PARTICIPANTS_BASINS_EVENTS}}
- 数值、单位、分母、区间和异质性：{{EFFECT_UNCERTAINTY_HETEROGENEITY}}
- 精确范围与纳入条件：{{SCOPE}}
- 精确定位及上下文：{{VERSION_PAGE_SECTION_FIGURE_TABLE}}
- 直接支持：{{DIRECTLY_SUPPORTS}}
- 不能支持：{{DOES_NOT_SUPPORT}}
- 综述作者解释：{{AUTHOR_INTERPRETATION}}
- 本方判断：{{ANALYST_JUDGMENT}}
- 证据重叠、来源依赖与冲突：{{OVERLAP_DEPENDENCY_CONFLICT}}
- 原始研究核验状态：未打开／已打开部分／直接来源已复核：{{PRIMARY_SOURCE_CHECK}}
- 核查状态和日期：{{CHECK}}

### 不宜合并、负结果与分歧

- 未合并证据及原因：{{NOT_SYNTHESIZED}}
- 结论相反或边界不同的研究：{{CONTRADICTORY}}
- 重要空白是否来自“没有研究”还是“没有检索到／没有报告”：{{ABSENCE_TYPE}}
- 结论对排除高偏倚研究、模型选择或口径变化是否敏感：{{SENSITIVITY}}

## 关键原始研究追踪

只列会改变当前结论且需要回到原文的研究。

| 关联 Cxx | 原始研究 | 综述怎样使用 | 是否独立核原文 | 下一步 |
| --- | --- | --- | --- | --- |
| C01 | {{PRIMARY_STUDY}} | {{ROLE}} | 否／部分／是 | {{ACTION}} |

## 局限与有效性威胁

| 会改变结论的威胁 | 已核事实 | 对哪些 Cxx 有影响 |
| --- | --- | --- |
| 检索覆盖和选择 | {{FACT}} | {{CLAIMS}} |
| 单项研究偏倚 | {{FACT}} | {{CLAIMS}} |
| 研究重叠和非独立 | {{FACT}} | {{CLAIMS}} |
| 异质性与不宜合并 | {{FACT}} | {{CLAIMS}} |
| 发表偏倚和结论确定性 | {{FACT}} | {{CLAIMS}} |

## 本方使用边界

- 整卡使用结论：{{USE_VERDICT}}
- 可用于：{{CAN_USE_FOR}}
- 不可用于：{{CANNOT_USE_FOR}}
- 对当前认识的影响：加强／削弱／限定／无变化：{{CHANGE}}
- 受影响主题、问题或决策：{{AFFECTED_OBJECTS}}
- 需要回到哪些原始研究后才能升级：{{PRIMARY_SOURCES_NEEDED}}

## 动态精读三门判定

| 资格门 | 是／否 | 依据 |
| --- | --- | --- |
| 有明确且高影响的研究决策 | {{YES_NO}} | {{BASIS}} |
| 有可定位的决定性证据缺口 | {{YES_NO}} | {{BASIS}} |
| 新材料可能改变当前判断 | {{YES_NO}} | {{BASIS}} |

- 最小证据路径：{{MINIMUM_PATH}}
- 停止条件或未触发理由：{{STOP_REASON}}

## 复查与变更

| 日期 | 核查范围 | 发现／修订 | 执行者 |
| --- | --- | --- | --- |
| {{DATE}} | {{SCOPE}} | {{CHANGE}} | {{WHO}} |
