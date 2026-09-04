---
card_schema: "evidence-card-v1.1"
card_id: "{{CARD_ID}}"
evidence_type: "standard-guideline-policy"
status: "draft"
zotero_item_key: "{{ZOTERO_KEY}}"
source_version: "{{SOURCE_VERSION}}"
reading_scope: "metadata_only"
source_provenance: "local_zotero_or_official_source"
direct_source_verified: false
created_at: "{{CREATED_AT}}"
updated_at: "{{CREATED_AT}}"
---

# 标准、指南与政策证据卡：{{TITLE}}

> 本卡按具体条款使用来源。规范要求、制定理由、技术解释和本方判断分别记录；官方身份不能自动证明科学最优或工程有效。

## 导师三分钟判断

- 当前规范或政策问题：{{NORMATIVE_QUESTION}}
- 这份文件可能影响的决定：{{INTENDED_DECISION}}
- 发布主体、效力和适用地域：{{AUTHORITY_FORCE_JURISDICTION}}
- 当前有效版本与生效状态：{{VERSION_EFFECTIVE_STATUS}}
- 最关键要求／建议／许可／禁止：{{DECISIVE_CLAUSE}}
- 例外、过渡期或解释空间：{{EXCEPTION}}
- 使用结论：可直接使用／限条件使用／仅作线索／暂不可用／与当前问题无关：{{WHY}}

### 决定性条款（最多三项）

| 声明 | 规范词与条款内容 | 适用范围／例外 | 定位 |
| --- | --- | --- | --- |
| C01 | {{NORMATIVE_REQUIREMENT}} | {{SCOPE_EXCEPTION}} | {{CLAUSE_LOCATOR}} |

## 来源身份与阅读边界

- 文件全名、编号和文件类型：{{TITLE}}；{{DOCUMENT_ID_TYPE}}
- 发布、批准、解释和执行主体：{{AUTHORITIES}}
- 发布、实施、修订、废止日期：{{DATES}}
- 当前版本、替代／被替代关系和过渡安排：{{VERSION_RELATION}}
- 法律层级或规范力度：强制／推荐／指导／政策目标／解释文件：{{NORMATIVE_FORCE}}
- 官方稳定入口、档案或 DOI：{{URL_OR_IDENTIFIER}}
- Zotero item key：{{ZOTERO_KEY}}
- 正文、附录、编制说明、勘误和解释文件的取得与阅读范围：{{MATERIALS_AND_SCOPE}}
- 未阅读或未取得：{{UNREAD_OR_MISSING}}
- 定位规则：{{LOCATOR_RULE}}

## 研究或使用问题

- 本次只核查的具体规范命题：{{CARD_QUESTION}}
- 适用主体、对象、地域、时期和活动：{{TARGET_SCOPE}}
- 当前研究或工程需要判断的是“必须做什么”“如何证明符合”还是“为什么这样规定”：{{DECISION_TYPE}}
- 需要避免的越界：{{SCIENTIFIC_BOUNDARY}}

## 规范证据如何形成

### 效力与适用性

- 上位依据、授权条款和配套文件：{{LEGAL_OR_NORMATIVE_BASIS}}
- 强制性与推荐性内容怎样区分：{{MUST_SHOULD_MAY}}
- 术语定义、分类、阈值、公式、单位和基准：{{DEFINITIONS_THRESHOLDS}}
- 例外、豁免、地域差异、过渡期和旧项目处理：{{EXCEPTIONS_TRANSITION}}
- 谁负责解释、检查和裁决：{{INTERPRETATION_AUTHORITY}}

### 测量、执行与符合性

- 要求的测量、采样、计算、记录或报告程序：{{PROCEDURE}}
- 符合性判据、允许误差、频次和抽样规则：{{CONFORMITY_CRITERIA}}
- 所需文件、设备、人员资质和留痕：{{REQUIRED_EVIDENCE}}
- 不符合、复测、整改和申诉程序：{{NONCONFORMITY}}
- 条款能证明的是程序符合、结果符合，还是仅存在要求：{{CONFORMITY_LEVEL}}

### 制定依据与科学证据边界

- 编制说明或政策理由中引用的科学依据：{{RATIONALE_EVIDENCE}}
- 本轮是否直接核验上游研究：{{UPSTREAM_CHECK}}
- 制定依据、政策取舍和正式条款是否一致：{{RATIONALE_VS_CLAUSE}}
- 条款存在不能单独证明方法性能最优、因果有效或适合所有流域：{{LIMIT}}

## 决定性证据块

### C01｜{{ATOMIC_NORMATIVE_CLAIM}}

- 来源角色：规范约束／解释说明／制定依据／政策立场／本方判断
- 来源组件：正文／条款／附录／修订单／编制说明／解释文件
- 原文条款或事实：{{SOURCE_FACT}}
- 规范词与效力：必须／应／宜／可／不得／目标性表述：{{NORMATIVE_WORD_FORCE}}
- 适用主体、对象、地域、时期和条件：{{EXACT_SCOPE}}
- 例外、过渡和冲突规则：{{EXCEPTION_CONFLICT_RULE}}
- 精确定位：{{VERSION_CLAUSE_PAGE_APPENDIX}}
- 直接支持：{{DIRECTLY_SUPPORTS}}
- 不能支持：{{DOES_NOT_SUPPORT}}
- 发布方解释：{{PUBLISHER_INTERPRETATION}}
- 本方判断：{{ANALYST_JUDGMENT}}
- 上位依据、上游来源和独立性组：{{UPSTREAM_DEPENDENCY}}
- 核查状态和日期：{{CHECK}}

## 局限、冲突与适用审查

| 会改变使用的问题 | 已核事实 | 对哪些 Cxx 有影响 |
| --- | --- | --- |
| 文件是否有效及版本是否唯一 | {{FACT}} | {{CLAIMS}} |
| 管辖、对象和场景是否匹配 | {{FACT}} | {{CLAIMS}} |
| 条款、附录和解释文件是否冲突 | {{FACT}} | {{CLAIMS}} |
| 测量与符合性证据是否可执行 | {{FACT}} | {{CLAIMS}} |
| 制定理由是否被误当作科学结论 | {{FACT}} | {{CLAIMS}} |

## 本方使用边界

- 整卡使用结论：{{USE_VERDICT}}
- 可用于：{{CAN_USE_FOR}}
- 不可用于：{{CANNOT_USE_FOR}}
- 对当前研究或工程的影响：约束／定义／报告要求／仅作背景：{{CHANGE}}
- 受影响对象：{{AFFECTED_OBJECTS}}
- 依赖键：{{DEPENDENCY_KEY}}
- 复查触发：换版、生效、废止、官方解释或上位文件变化：{{RECHECK_TRIGGER}}

## 补读资格门与最小路径

| 资格门 | 是／否 | 依据 |
| --- | --- | --- |
| 有明确且高影响的规范或工程决策 | {{YES_NO}} | {{BASIS}} |
| 有可定位的条款、版本或解释缺口 | {{YES_NO}} | {{BASIS}} |
| 官方附件、解释或上位依据可能改变判断 | {{YES_NO}} | {{BASIS}} |

- 最小证据路径：{{MINIMUM_PATH}}
- 停止条件或未触发理由：{{STOP_REASON}}

## 复查与变更

| 日期 | 版本与核查范围 | 发现／修订 | 执行者 |
| --- | --- | --- | --- |
| {{DATE}} | {{SCOPE}} | {{CHANGE}} | {{WHO}} |
