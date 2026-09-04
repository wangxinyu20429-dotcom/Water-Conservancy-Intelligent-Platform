---
card_schema: "evidence-card-v1.1"
card_id: "{{CARD_ID}}"
evidence_type: "survey-monitoring-statistics"
status: "draft"
zotero_item_key: "{{ZOTERO_KEY}}"
source_version: "{{SOURCE_VERSION}}"
reading_scope: "metadata_only"
source_provenance: "local_zotero"
direct_source_verified: false
created_at: "{{CREATED_AT}}"
updated_at: "{{CREATED_AT}}"
---

# 调查、监测与统计报告证据卡：{{TITLE}}

> 数字只有在总体、口径、时间、空间、分母和不确定性明确时才构成证据。本卡不把机构权威、发布规模或图表精美等同于统计有效性。

## 导师三分钟判断

- 当前统计问题：{{STATISTICAL_QUESTION}}
- 这份报告可能影响的决定：{{INTENDED_DECISION}}
- 统计产品性质：普查／抽样调查／监测网络／行政记录／统计汇编／其他：{{TYPE}}
- 目标总体与实际覆盖：{{TARGET_AND_COVERAGE}}
- 指标、时间和空间口径：{{MEASURE_PERIOD_GEOGRAPHY}}
- 最关键估计及不确定性：{{ESTIMATE_DENOMINATOR_UNCERTAINTY}}
- 最大边界：{{LOAD_BEARING_LIMIT}}
- 使用结论：可直接使用／限条件使用／仅作线索／暂不可用／与当前问题无关：{{WHY}}

### 决定性统计结论（最多三项）

| 声明 | 估计值、分母与口径 | 不确定性／修订状态 | 定位 |
| --- | --- | --- | --- |
| C01 | {{ESTIMATE}} | {{UNCERTAINTY_REVISION}} | {{LOCATOR}} |

## 来源身份与阅读边界

- 题名、发布机构与统计责任主体：{{TITLE}}；{{PUBLISHER_AND_STATISTICAL_AUTHORITY}}
- 调查／监测／统计期：{{REFERENCE_PERIOD}}
- 发布日期、版本、修订号和数据截点：{{DATE_AND_VERSION_BUNDLE}}
- 报告号／DOI／官方页面：{{IDENTIFIER}}；{{URL}}
- Zotero item key：{{ZOTERO_KEY}}
- 数据表、方法说明、问卷、代码本和修订记录的取得情况：{{MATERIALS}}
- 实际阅读范围：{{READ_SCOPE}}
- 未阅读或未取得：{{UNREAD_OR_MISSING}}
- 定位规则：{{LOCATOR_RULE}}

## 研究或使用问题

- 本卡要估计或比较的对象：{{ESTIMAND_OR_TARGET_QUANTITY}}
- 为什么该估计会改变研究、项目或管理判断：{{DECISION_RELEVANCE}}
- 预定比较：跨期／跨区／跨群体／阈值／趋势：{{COMPARISON}}
- 当前需要的精度和容许误差：{{REQUIRED_PRECISION}}

## 统计证据如何产生

### 目标总体、覆盖框和独立单位

- 目标总体、抽样框／站网／行政覆盖：{{TARGET_FRAME_COVERAGE}}
- 纳入、排除、停测、新增或替换规则：{{INCLUSION_CHANGES}}
- 基本单位、聚类和重复观测：{{UNIT_CLUSTER_REPEAT}}
- 样本量／站点数／事件数及各阶段分母：{{COUNTS_DENOMINATORS}}
- 覆盖不足或代表性缺口：{{COVERAGE_GAP}}

### 测量与指标口径

- 概念定义、观测变量、单位和阈值：{{CONSTRUCT_MEASURE_UNIT}}
- 仪器、问卷、行政字段或算法怎样产生值：{{MEASUREMENT_PROCESS}}
- 校准、检出限、测量误差和质量控制：{{MEASUREMENT_ERROR_QC}}
- 缺失、非响应、删失、异常和低于检出限的处理：{{MISSING_NONRESPONSE}}
- 指标分子、分母、聚合、季节性和标准化：{{NUMERATOR_DENOMINATOR_AGGREGATION}}

### 估计、加权和不确定性

- 抽样设计或监测设计：{{DESIGN}}
- 权重、校准、插补、模型估计或季调：{{WEIGHTING_MODEL}}
- 方差、标准误、置信区间或其他不确定性：{{UNCERTAINTY}}
- 保密处理、四舍五入、抑制和可能偏差：{{DISCLOSURE_EFFECT}}
- 初值／快报／修订值／最终值关系：{{REVISION_STATUS}}

## 决定性证据块

### C01｜{{ATOMIC_STATISTICAL_CLAIM}}

- 声明性质与推断类型：统计事实／发布方解释／本方判断；描述／比较／趋势／关联
- 原文统计事实：{{SOURCE_FACT}}
- 数据来源与估计过程：{{DATA_AND_ESTIMATION}}
- 数值、单位、分子、分母和不确定性：{{VALUE_UNIT_DENOMINATOR_INTERVAL}}
- 总体、地域、时期、尺度和口径：{{EXACT_SCOPE}}
- 精确定位及表注／脚注上下文：{{VERSION_TABLE_PAGE_NOTE}}
- 直接支持：{{DIRECTLY_SUPPORTS}}
- 不能支持：{{DOES_NOT_SUPPORT}}
- 发布方解释：{{PUBLISHER_INTERPRETATION}}
- 本方判断：{{ANALYST_JUDGMENT}}
- 与其他表、版本或来源的冲突：{{CONFLICT}}
- 核查状态和日期：{{CHECK}}

## 可比性与变化归因

- 跨期定义、框架、站网、行政区或仪器是否变化：{{TIME_COMPARABILITY}}
- 跨区采集强度、尺度和标准是否一致：{{SPACE_COMPARABILITY}}
- 名义变化与真实变化是否可区分：{{NOMINAL_REAL_CHANGE}}
- 趋势是否可能来自口径、覆盖、修订或缺失变化：{{ALTERNATIVE_EXPLANATIONS}}
- 只有统计关联时，不把变化写成政策、工程或气候因素造成：{{CAUSAL_BOUNDARY}}

## 局限与有效性威胁

| 会改变结论的威胁 | 已核事实 | 对哪些 Cxx 有影响 |
| --- | --- | --- |
| 覆盖误差与代表性 | {{FACT}} | {{CLAIMS}} |
| 测量和分类误差 | {{FACT}} | {{CLAIMS}} |
| 非响应、缺失与插补 | {{FACT}} | {{CLAIMS}} |
| 权重、模型与不确定性 | {{FACT}} | {{CLAIMS}} |
| 修订、保密和可比性 | {{FACT}} | {{CLAIMS}} |

## 本方使用边界

- 整卡使用结论：{{USE_VERDICT}}
- 可用于：{{CAN_USE_FOR}}
- 不可用于：{{CANNOT_USE_FOR}}
- 对当前认识的影响：加强／削弱／限定／无变化：{{CHANGE}}
- 受影响主题、数据需求或工程决策：{{AFFECTED_OBJECTS}}
- 复查触发：新一版、口径修订、站网变化或错误更正：{{RECHECK_TRIGGER}}

## 补读资格门与最小路径

| 资格门 | 是／否 | 依据 |
| --- | --- | --- |
| 有明确且高影响的研究决策 | {{YES_NO}} | {{BASIS}} |
| 有可定位的决定性证据缺口 | {{YES_NO}} | {{BASIS}} |
| 方法表、微数据或修订记录可能改变判断 | {{YES_NO}} | {{BASIS}} |

- 最小证据路径：{{MINIMUM_PATH}}
- 停止条件或未触发理由：{{STOP_REASON}}

## 复查与变更

| 日期 | 版本与核查范围 | 发现／修订 | 执行者 |
| --- | --- | --- | --- |
| {{DATE}} | {{SCOPE}} | {{CHANGE}} | {{WHO}} |
