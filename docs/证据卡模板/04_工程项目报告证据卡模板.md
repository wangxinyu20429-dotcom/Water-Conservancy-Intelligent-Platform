---
card_schema: "evidence-card-v1.1"
card_id: "{{CARD_ID}}"
evidence_type: "engineering-report"
status: "draft"
zotero_item_key: "{{ZOTERO_KEY}}"
source_version: "{{SOURCE_VERSION}}"
reading_scope: "metadata_only"
source_provenance: "local_zotero"
direct_source_verified: false
created_at: "{{CREATED_AT}}"
updated_at: "{{CREATED_AT}}"
---

# 工程项目报告证据卡：{{TITLE}}

> 工程证据必须区分设计预期、计算结果、试验结果、验收记录和长期运行表现。某一层成立不能自动升级到更高层。

## 导师三分钟判断

- 当前工程问题：{{ENGINEERING_QUESTION}}
- 这份报告可能影响的决定：{{INTENDED_DECISION}}
- 工程对象、地点与阶段：规划／可研／设计／施工／试验／验收／运行／事故复盘：{{OBJECT_STAGE}}
- 当前最高证据层：设计假设／模拟／实验室试验／现场试验／验收实测／长期运行／事故记录：{{EVIDENCE_STRATUM}}
- 最关键工程事实：{{DECISIVE_FACT_WITH_THRESHOLD}}
- 最大边界条件或失效模式：{{LOAD_BEARING_LIMIT}}
- 使用结论：可直接使用／限条件使用／仅作线索／暂不可用／与当前问题无关：{{WHY}}

### 决定性工程结论（最多三项）

| 声明 | 证据层与结果 | 判据／边界 | 定位 |
| --- | --- | --- | --- |
| C01 | {{RESULT_AND_STRATUM}} | {{CRITERION_BOUNDARY}} | {{LOCATOR}} |

## 来源身份与阅读边界

- 报告题名、编号、编制与委托单位：{{TITLE}}；{{REPORT_ID_ORGANIZATIONS}}
- 工程项目、地点和阶段：{{PROJECT_LOCATION_STAGE}}
- 编制、审查、批准、竣工或修订日期：{{DATES}}
- 版本、状态和取代关系：{{VERSION_RELATION}}
- DOI／档案号／官方或授权入口：{{IDENTIFIER}}；{{URL}}
- Zotero item key：{{ZOTERO_KEY}}
- 主报告、附图、计算书、试验、验收、运行记录和变更单的取得情况：{{MATERIALS}}
- 实际阅读范围及定位规则：{{READ_SCOPE_AND_LOCATOR}}
- 未阅读或未取得：{{UNREAD_OR_MISSING}}

## 研究或使用问题

- 需要判断的工程命题：性能／安全／适应性／可实施性／故障原因／运行效果：{{DECISION_CLAIM}}
- 预定使用场景和决策阈值：{{USE_SCENARIO_THRESHOLD}}
- 当前项目与报告项目的关键差异：{{TRANSFER_GAP}}

## 工程证据如何产生

### 工程边界与基础资料

- 工程系统边界、服务对象和运行方式：{{SYSTEM_BOUNDARY}}
- 水文、地形、地质、气象、调度和既有设施资料：{{BASE_DATA}}
- 资料年份、代表性、极值处理和安全等级：{{REPRESENTATIVENESS}}
- 设计工况、校核工况、常态和异常工况：{{OPERATING_SCENARIOS}}
- 法规、标准、业主约束和资源约束：{{CONSTRAINTS}}

### 方案、计算与变更

- 备选方案与比较准则：{{ALTERNATIVES_CRITERIA}}
- 关键模型、公式、参数、边界和校准：{{MODEL_CALCULATION}}
- 现场调查、实验室或现场试验：{{TESTS}}
- 设计到施工的偏差、变更及其批准依据：{{DEVIATIONS_CHANGES}}
- 哪些结论来自估算、模拟、试验、实测或专家判断：{{EVIDENCE_SOURCE_MAP}}

### 验收、运行和故障

- 验收指标、阈值、测量方法和责任主体：{{ACCEPTANCE}}
- 实测期间、样本量、工况和设备状态：{{OBSERVATION_WINDOW}}
- 计划值、设计值、实测值和允许值的对照：{{PLANNED_DESIGNED_MEASURED_ALLOWED}}
- 故障、险情、异常、维修和未达标情况：{{FAILURES}}
- 长期运行证据是否足以覆盖季节、极端事件和退化：{{LONG_TERM_COVERAGE}}

## 决定性证据块

### C01｜{{ATOMIC_ENGINEERING_CLAIM}}

- 声明性质与推断类型：工程事实／报告解释／本方判断；设计／模拟／试验／验收／运行／原因分析
- 原文事实：{{SOURCE_FACT}}
- 证据层与产生方式：{{EVIDENCE_STRATUM_AND_METHOD}}
- 数值、单位、工况、比较值和判据：{{VALUE_CONDITION_COMPARATOR_CRITERION}}
- 工程对象、位置、时段和系统边界：{{EXACT_SCOPE}}
- 精确定位及图纸／表格／附件上下文：{{VERSION_PAGE_DRAWING_TABLE_ATTACHMENT}}
- 直接支持：{{DIRECTLY_SUPPORTS}}
- 不能支持：{{DOES_NOT_SUPPORT}}
- 报告解释或责任方陈述：{{REPORT_INTERPRETATION}}
- 本方判断：{{ANALYST_JUDGMENT}}
- 冲突、设计变更、数据缺口与替代解释：{{CONFLICT_GAPS}}
- 核查状态和日期：{{CHECK}}

## 局限、失效与迁移性

| 会改变结论的问题 | 已核事实 | 对哪些 Cxx 有影响 |
| --- | --- | --- |
| 基础资料和设计工况代表性 | {{FACT}} | {{CLAIMS}} |
| 模型、参数与计算假设 | {{FACT}} | {{CLAIMS}} |
| 测量、试验和验收独立性 | {{FACT}} | {{CLAIMS}} |
| 运行窗口与极端情景覆盖 | {{FACT}} | {{CLAIMS}} |
| 当前工程与目标工程差异 | {{FACT}} | {{CLAIMS}} |

- 失败模式及触发条件：{{FAILURE_MODES}}
- 反事实或替代原因是否被检验：{{ALTERNATIVE_CAUSES}}
- 报告利益关系、编审关系和未公开附件：{{CONFLICT_OF_INTEREST}}

## 本方使用边界

- 整卡使用结论：{{USE_VERDICT}}
- 可用于：{{CAN_USE_FOR}}
- 不可用于：{{CANNOT_USE_FOR}}
- 对当前认识的影响：加强／削弱／限定／无变化：{{CHANGE}}
- 受影响项目、方案、参数或风险：{{AFFECTED_OBJECTS}}
- 迁移到当前工程前必须再核：{{TRANSFER_REQUIREMENTS}}
- 复查触发：竣工、设计变更、新运行期、事故调查或标准换版：{{RECHECK_TRIGGER}}

## 补读资格门与最小路径

| 资格门 | 是／否 | 依据 |
| --- | --- | --- |
| 有明确且高影响的工程决策 | {{YES_NO}} | {{BASIS}} |
| 有可定位的决定性证据缺口 | {{YES_NO}} | {{BASIS}} |
| 计算书、图纸、监测或运行记录可能改变判断 | {{YES_NO}} | {{BASIS}} |

- 最小证据路径：{{MINIMUM_PATH}}
- 停止条件或未触发理由：{{STOP_REASON}}

## 复查与变更

| 日期 | 版本与核查范围 | 发现／修订 | 执行者 |
| --- | --- | --- | --- |
| {{DATE}} | {{SCOPE}} | {{CHANGE}} | {{WHO}} |
