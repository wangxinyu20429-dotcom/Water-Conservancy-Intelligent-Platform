---
card_schema: "evidence-card-v1.1"
card_id: "{{CARD_ID}}"
evidence_type: "dataset-data-product"
status: "draft"
zotero_item_key: "{{ZOTERO_KEY}}"
source_version: "{{SOURCE_VERSION}}"
reading_scope: "metadata_only"
source_provenance: "local_zotero_or_official_source"
direct_source_verified: false
created_at: "{{CREATED_AT}}"
updated_at: "{{CREATED_AT}}"
---

# 数据集及数据产品证据卡：{{TITLE}}

> 数据存在、数据可访问、数据质量良好和数据适合当前任务是四个不同命题。本卡按组件和版本分别核查，不能用许可证或官方身份代替适用性验证。

## 导师三分钟判断

- 当前数据问题：{{DATA_QUESTION}}
- 数据将用于什么变量、模型或决策：{{INTENDED_USE}}
- 数据性质：实测／遥感反演／再分析／模拟／调查／融合／派生指标：{{DATA_NATURE}}
- 关键覆盖：变量、对象、空间、时间和分辨率：{{COVERAGE}}
- 版本束：产品／处理流／数据截点／接口／许可：{{VERSION_BUNDLE}}
- 最关键质量或适用性证据：{{DECISIVE_QUALITY_EVIDENCE}}
- 最大边界：{{LOAD_BEARING_LIMIT}}
- 使用结论：可直接使用／限条件使用／仅作线索／暂不可用／与当前问题无关：{{WHY}}

### 决定性数据声明（最多三项）

| 声明 | 数据属性／质量／许可／适用性 | 组件与版本 | 定位 |
| --- | --- | --- | --- |
| C01 | {{DATA_CLAIM}} | {{COMPONENT_VERSION}} | {{LOCATOR}} |

## 来源身份与阅读边界

- 数据集／产品名称和发布者：{{TITLE}}；{{PUBLISHER}}
- DOI、永久标识、目录和下载入口：{{DOI}}；{{URL}}
- Zotero item key：{{ZOTERO_KEY}}
- 产品版本、处理流、数据截点、接口和许可证版本：{{VERSION_BUNDLE}}
- 数据论文、技术文档、元数据、字段字典、质量报告和变更记录关系：{{ARTIFACT_RELATION}}
- 本轮实际取得：元数据／样例／完整数据／API响应／校验和：{{ACQUIRED}}
- 实际阅读和检查范围：{{READ_AND_INSPECTION_SCOPE}}
- 未阅读、未下载或未取得：{{UNREAD_OR_MISSING}}
- 定位规则：{{LOCATOR_RULE}}

## 研究或使用问题

- 当前任务需要的数据对象、变量、时空尺度、时效和精度：{{FIT_REQUIREMENTS}}
- 要判断的具体命题：变量存在／覆盖足够／误差可接受／许可允许／能与另一数据对齐：{{CARD_QUESTION}}
- 接受或排除阈值：{{DECISION_THRESHOLD}}

## 数据证据如何产生

### 数据生成与来源链

- 原始观测、传感器、站网、卫星、模式或上游数据库：{{UPSTREAM_SOURCES}}
- 采样／观测／模拟单位与频次：{{UNIT_FREQUENCY}}
- 算法、反演、同化、插值、融合或聚合流程：{{PROCESSING_PIPELINE}}
- 校准、训练和验证使用的参考数据：{{CALIBRATION_VALIDATION}}
- 上游版本、再处理和可追溯性：{{PROVENANCE}}

### 覆盖、变量和语义

- 对象／流域／站点／网格及纳入规则：{{ENTITY_COVERAGE}}
- 时间起止、频率、延迟和缺口：{{TIME_COVERAGE}}
- 空间范围、分辨率、坐标参考和垂直基准：{{SPATIAL_COVERAGE}}
- 核心变量、定义、单位、编码、质量标记和缺失值：{{VARIABLE_SEMANTICS}}
- 实测、估计、模拟和派生值是否清楚区分：{{OBSERVED_ESTIMATED_SIMULATED}}

### 质量、不确定性和变化

- QA/QC 流程、审核和异常处理：{{QUALITY_CONTROL}}
- 精度、偏差、误差、置信信息及评估样本：{{QUALITY_METRICS}}
- 缺失、删失、站网变化、漂移和已知异常：{{MISSING_BIAS}}
- 与独立数据的验证及其时空范围：{{INDEPENDENT_VALIDATION}}
- 版本变化、修订历史和旧版保存：{{REVISION_PROVENANCE}}

### 获取、许可与复现

- 访问方式、认证、配额、文件格式和体量：{{ACCESS}}
- 许可证、署名、再分发、商用和衍生品限制：{{LICENSE}}
- 数据与元数据校验和、持久标识和引用格式：{{PERSISTENCE}}
- 下载脚本、查询参数、切片范围和获取日期：{{RETRIEVAL_RECIPE}}
- 敏感性、隐私、主权或安全限制：{{RESTRICTIONS}}

## 决定性证据块

### C01｜{{ATOMIC_DATA_CLAIM}}

- 来源角色：数据属性／数据质量／版本关系／许可条件／任务适用性
- 来源组件：目录元数据／字段字典／质量报告／许可证／变更记录／实际数据检查
- 原文或实查事实：{{SOURCE_OR_INSPECTION_FACT}}
- 数据生成或检查依据：{{HOW_ESTABLISHED}}
- 对象、变量、时空范围、分辨率和单位：{{EXACT_SCOPE}}
- 数值、误差、分母和不确定性：{{VALUE_UNCERTAINTY}}
- 版本束与精确定位：{{VERSION_COMPONENT_LOCATOR}}
- 直接支持：{{DIRECTLY_SUPPORTS}}
- 不能支持：{{DOES_NOT_SUPPORT}}
- 发布方解释：{{PUBLISHER_INTERPRETATION}}
- 本方适用性判断：{{FITNESS_JUDGMENT}}
- 上游来源、独立性组和冲突：{{UPSTREAM_DEPENDENCY_CONFLICT}}
- 核查状态和日期：{{CHECK}}

## 任务适用性检验

不要由元数据直接写“可用”。把要求与证据逐项对照。

| 当前任务要求 | 数据证据 | 差距 | 结论 |
| --- | --- | --- | --- |
| 对象与时空覆盖 | {{EVIDENCE}} | {{GAP}} | 满足／限条件／不满足／未核 |
| 变量语义与单位 | {{EVIDENCE}} | {{GAP}} | {{RESULT}} |
| 精度、缺失和偏差 | {{EVIDENCE}} | {{GAP}} | {{RESULT}} |
| 时效、访问和可复现获取 | {{EVIDENCE}} | {{GAP}} | {{RESULT}} |
| 许可与共享边界 | {{EVIDENCE}} | {{GAP}} | {{RESULT}} |

## 局限与有效性威胁

- 已知最严重的误差或偏差：{{KEY_BIAS}}
- 质量评估是否独立且覆盖目标流域／时期：{{VALIDATION_MATCH}}
- 元数据与实际文件、接口或样例是否一致：{{METADATA_DATA_CONSISTENCY}}
- 版本升级会影响哪些变量或结论：{{VERSION_IMPACT}}
- 未做的实际抽查及因此不能作出的判断：{{UNTESTED}}

## 本方使用边界

- 整卡使用结论：{{USE_VERDICT}}
- 可用于：{{CAN_USE_FOR}}
- 不可用于：{{CANNOT_USE_FOR}}
- 对当前研究可执行性的影响：{{CHANGE}}
- 受影响主题、方法、项目或数据流程：{{AFFECTED_OBJECTS}}
- 依赖键：{{DEPENDENCY_KEY}}
- 复查触发：数据更新、算法重处理、接口、许可或质量报告变化：{{RECHECK_TRIGGER}}

## 补读／取数资格门与最小路径

| 资格门 | 是／否 | 依据 |
| --- | --- | --- |
| 有明确且高影响的数据使用决策 | {{YES_NO}} | {{BASIS}} |
| 有可定位的决定性适用性缺口 | {{YES_NO}} | {{BASIS}} |
| 小样本下载、质量报告或版本记录可能改变判断 | {{YES_NO}} | {{BASIS}} |

- 最小路径：{{MINIMUM_PATH}}
- 停止条件或未触发理由：{{STOP_REASON}}

## 复查与变更

| 日期 | 版本／组件与核查范围 | 发现／修订 | 执行者 |
| --- | --- | --- | --- |
| {{DATE}} | {{SCOPE}} | {{CHANGE}} | {{WHO}} |
