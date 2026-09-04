---
card_schema: "evidence-card-v1.1"
card_id: "{{CARD_ID}}"
evidence_type: "original-research"
status: "draft"
zotero_item_key: "{{ZOTERO_KEY}}"
source_version: "{{SOURCE_VERSION}}"
reading_scope: "metadata_only"
source_provenance: "local_zotero"
direct_source_verified: false
created_at: "{{CREATED_AT}}"
updated_at: "{{CREATED_AT}}"
---

# 原创研究证据卡：{{TITLE}}

> 本卡只保留能解释科研判断的内容。模板提示在定稿前删除；没有核到的内容按“未取得／未阅读／原文未报告（已查：…）／冲突待核”填写，不以常识补足。

## 导师快速判断稿

### 当前决策锚点

- 当前研究问题：{{RESEARCH_QUESTION}}
- 这篇文献可能影响的决定：{{INTENDED_DECISION}}
- 研究类型与主要推断目标：{{STUDY_AND_INFERENCE_TYPE}}
- 本轮直接来源范围：{{DIRECT_SOURCE_SCOPE}}

### 证据主链

| 环节 | 只写决定判断的内容 |
| --- | --- |
| 研究对象与边界 | {{POPULATION_BASIN_PERIOD_SCALE}} |
| 证据如何产生 | {{DESIGN_DATA_COMPARISON_VALIDATION}} |
| 最关键结果 | {{DECISIVE_RESULT_WITH_EFFECT_AND_UNCERTAINTY}} |
| 允许的推断 | {{SUPPORTED_INFERENCE}} |
| 最大限制 | {{LOAD_BEARING_LIMIT}} |
| 当前使用结论 | 可直接使用／限条件使用／仅作线索／暂不可用／与当前问题无关：{{WHY}} |

### 决定性结果（最多三项）

| 声明 | 原文结果与比较条件 | 为什么会改变决策 | 定位 |
| --- | --- | --- | --- |
| C01 | {{RESULT}} | {{DECISION_EFFECT}} | {{LOCATOR}} |

### 最大边界（最多两项）

1. {{BOUNDARY_1}}
2. {{BOUNDARY_2}}

## 初读卡片（3—5分钟）

用连续文字写清：研究要解决什么；用什么对象、数据和设计回答；最重要的结果是什么；结果只在什么范围内成立；对当前研究问题产生何种改变。一般控制在 500—800 个中文字符，复杂材料也不要用堆字段代替判断。

## 完整证据档案

## 一、文献身份与证据状态

- 题名：{{TITLE}}
- 作者：{{CREATORS}}
- 年份与出版状态：{{DATE}}
- 期刊／会议／学位授予单位：{{VENUE}}
- DOI／稳定标识：{{DOI}}
- 官方页面：{{URL}}
- Zotero item key：{{ZOTERO_KEY}}
- 本次使用版本及版本关系：{{VERSION_RELATION}}
- 勘误、撤稿、关注声明或更新检查：{{VERSION_CHECK}}
- 实际取得并阅读：{{READ_MATERIALS}}
- 已取得但未读：{{UNREAD_MATERIALS}}
- 未取得：{{MISSING_MATERIALS}}
- 定位规则：{{PDF_OR_PRINT_PAGE_RULE}}

## 二、研究背景、知识缺口与研究问题

- 来源明确提出的知识缺口：{{AUTHOR_STATED_GAP}}
- 可检验的研究问题／假设：{{RQ_OR_HYPOTHESIS}}
- 推断目标或目标量：{{ESTIMAND_TARGET_OR_PROPOSITION}}
- 本文贡献声称：{{AUTHOR_CLAIMED_CONTRIBUTION}}
- 本卡只核查的当前问题：{{CARD_QUESTION}}

## 三、研究对象、尺度与适用范围

用完整句子说明对象、流域／站点／事件、时间范围、空间与时间尺度、观测或实验单位、纳入排除条件。必须特别回答：

- 真正独立的分析单位是什么：{{INDEPENDENT_UNIT}}
- 训练、校准、验证、测试或对照对象是否在时间、空间、实体或数据来源上独立：{{INDEPENDENCE}}
- 目标总体或适用域与样本之间有什么差距：{{TRANSPORT_GAP}}
- 暴露、输入、干预、预测时可用信息和目标变量分别是什么：{{INFORMATION_AVAILABLE_AT_DECISION_TIME}}

## 四、数据、方法与验证设计

先写一段方法逻辑：输入什么，经过什么处理和模型，输出什么，用什么比较或证据识别结论。

### 证据生成设计

| 关键环节 | 内容及其对解释的影响 | 定位 |
| --- | --- | --- |
| 数据来源、生成与筛选 | {{DATA_PROVENANCE_SELECTION}} | {{LOCATOR}} |
| 预处理、缺失、异常与尺度转换 | {{PROCESSING}} | {{LOCATOR}} |
| 方法／模型／实验过程 | {{METHOD_CHAIN}} | {{LOCATOR}} |
| 基线、对照与消融 | {{COMPARATORS}} | {{LOCATOR}} |
| 切分、调参、选模和最终测试 | {{SPLIT_TUNING_TEST}} | {{LOCATOR}} |
| 指标、统计推断与不确定性 | {{METRICS_UNCERTAINTY}} | {{LOCATOR}} |

### 仅在适用时展开

- 观测或准实验：混杂控制、识别假设、时间先后和敏感性分析。
- 预测或机器学习：样本依赖、信息泄漏、超参数选择、分布外测试和基线公平性。
- 数值模拟：方程、边界和初始条件、参数来源、校准、数值误差和验证对象。
- 理论研究：前提、定义、命题、推导关键步、反例和适用域。
- 定性研究：取样、资料饱和、编码过程、研究者角色、反例和可信度策略。

## 五、主要结果与差异、失败情景

本节以 Cxx 原子声明块为核心。只保留会影响当前问题的结果；每个声明只表达一个命题。

### C01｜{{ATOMIC_CLAIM}}

- 声明性质与推断类型：来源事实／作者解释／本方判断；描述／比较／关联／因果／预测／机制／可迁移性
- 原文事实：{{SOURCE_FACT}}
- 证据来源：{{TABLE_FIGURE_ANALYSIS_EXPERIMENT}}
- 效应与不确定性：{{EFFECT_SIZE_UNIT_DENOMINATOR_INTERVAL}}
- 精确范围：{{OBJECT_PLACE_PERIOD_SCALE_CONDITION_COMPARATOR}}
- 精确定位及上下文：{{VERSION_PAGE_SECTION_FIGURE_TABLE_AND_CONTEXT}}
- 直接支持：{{DIRECTLY_SUPPORTS}}
- 不能支持：{{DOES_NOT_SUPPORT}}
- 作者解释：{{AUTHOR_INTERPRETATION}}
- 本方判断：{{ANALYST_JUDGMENT}}
- 冲突、替代解释与来源依赖：{{CONFLICT_ALTERNATIVES_DEPENDENCY}}
- 核查状态：未定位／已定位待复核／直接来源已复核／冲突待核；核查人和日期：{{CHECK}}

### 结果全貌

- 与主要结论一致的结果：{{CONVERGENT_RESULTS}}
- 负结果、失效流域／时段／情景：{{FAILURES}}
- 敏感性、稳健性、消融或替代口径：{{ROBUSTNESS}}
- 摘要、正文、图表、补充材料或代码之间的冲突：{{INTERNAL_CONFLICTS}}

## 六、作者声称、实际新增与平台初步判断

分别写，不合并：

- 作者声称的新意：{{AUTHOR_NOVELTY}}
- 由本轮已核证据实际证明的新增：{{EVIDENCE_BACKED_INCREMENT}}
- 尚未由本文证明的部分：{{UNPROVEN_PART}}
- 本方初步判断及依据 Cxx：{{PLATFORM_JUDGMENT_WITH_CLAIMS}}

## 七、文献价值、主题关联及关联理由

- 对当前主题／问题的具体作用：定义问题／提供方法／提供比较／限制外推／反证／仅作线索：{{ROLE}}
- 改变了哪一项既有认识：加强／削弱／限定／无变化：{{CHANGE}}
- 关联主题或对象：{{AFFECTED_OBJECTS}}
- 可复用的数据、方法、指标或反例：{{REUSABLE_ELEMENT}}
- 必须连同哪些 Cxx 和边界一起引用：{{REQUIRED_CLAIMS}}

## 八、适用边界、局限、待核验问题与后续阅读提示

### 会改变结论的有效性威胁

| 威胁 | 来源已报告的事实 | 本方判断 | 对 Cxx 的影响 |
| --- | --- | --- | --- |
| 选择、比较或混杂 | {{FACT}} | {{JUDGMENT}} | {{CLAIMS}} |
| 测量、标签或构念 | {{FACT}} | {{JUDGMENT}} | {{CLAIMS}} |
| 统计、样本依赖或多重分析 | {{FACT}} | {{JUDGMENT}} | {{CLAIMS}} |
| 信息泄漏、验证或复现 | {{FACT}} | {{JUDGMENT}} | {{CLAIMS}} |
| 外推与业务条件 | {{FACT}} | {{JUDGMENT}} | {{CLAIMS}} |

### 动态精读三门判定

| 资格门 | 是／否 | 依据 |
| --- | --- | --- |
| 有明确且高影响的研究决策 | {{YES_NO}} | {{BASIS}} |
| 有可定位的决定性证据缺口 | {{YES_NO}} | {{BASIS}} |
| 新材料可能改变当前判断 | {{YES_NO}} | {{BASIS}} |

- 三门全为“是”时的最小证据路径：{{MINIMUM_PATH}}
- 停止条件：{{STOP_CONDITION}}
- 未触发或停止理由：{{STOP_REASON}}

## 加工与复核记录

仅记录真实发生的身份核对、原文复查、冲突处理和实质修订。机器结构检查通过不等于科研结论通过。

| 日期 | 操作与范围 | 发现或改动 | 执行者／核查者 |
| --- | --- | --- | --- |
| {{DATE}} | {{ACTION}} | {{CHANGE}} | {{WHO}} |

## 本卡收口

- 整卡使用结论：{{USE_VERDICT}}
- 可用于：{{CAN_USE_FOR}}
- 不可用于：{{CANNOT_USE_FOR}}
- 下一步：{{NEXT_ACTION}}
- 受影响对象：{{AFFECTED_OBJECTS}}
