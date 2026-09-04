---
card_schema: "evidence-card-v1.1"
card_id: "{{CARD_ID}}"
evidence_type: "book-chapter"
status: "draft"
zotero_item_key: "{{ZOTERO_KEY}}"
source_version: "{{SOURCE_VERSION}}"
reading_scope: "metadata_only"
source_provenance: "local_zotero"
direct_source_verified: false
created_at: "{{CREATED_AT}}"
updated_at: "{{CREATED_AT}}"
---

# 图书与章节证据卡：{{TITLE}}

> 图书适合厘清概念、理论、方法和知识谱系。书中转述的研究结果仍是二次来源；未打开原始文献时，不写成已经独立核验。

## 导师三分钟判断

- 当前理论或方法问题：{{QUESTION}}
- 本书／章节可能影响的决定：{{INTENDED_DECISION}}
- 主要证据角色：概念界定／理论命题／数学推导／方法步骤／历史谱系／案例说明：{{ROLE}}
- 最关键命题或定义：{{DECISIVE_PROPOSITION}}
- 它由什么论证或来源支持：{{ARGUMENT_OR_SOURCE}}
- 最大适用边界：{{LOAD_BEARING_LIMIT}}
- 使用结论：可直接使用／限条件使用／仅作线索／暂不可用／与当前问题无关：{{WHY}}

### 决定性命题（最多三项）

| 声明 | 命题／定义／推导 | 依据类型 | 定位 |
| --- | --- | --- | --- |
| C01 | {{PROPOSITION}} | {{DERIVATION_CITATION_EXAMPLE}} | {{LOCATOR}} |

## 来源身份与阅读边界

- 书名、章节名、作者／编者：{{TITLE}}；{{CHAPTER}}；{{CREATORS}}
- 版次、卷次、出版年、出版社和译本：{{EDITION_VOLUME_DATE_PUBLISHER_TRANSLATION}}
- ISBN／DOI／官方目录：{{IDENTIFIER}}；{{URL}}
- Zotero item key：{{ZOTERO_KEY}}
- 原版与译本、旧版与新版关系：{{VERSION_RELATION}}
- 实际阅读的页码和章节：{{READ_SCOPE}}
- 注释、参考文献、附录和习题是否阅读：{{ANCILLARY_SCOPE}}
- 未阅读或未取得：{{UNREAD_OR_MISSING}}
- 定位规则：{{LOCATOR_RULE}}

## 研究或使用问题

- 要厘清的概念、命题、方法或历史判断：{{CARD_QUESTION}}
- 当前争议或术语歧义：{{AMBIGUITY}}
- 本卡需要得到的可使用输出：定义／假设／公式／方法步骤／原始来源线索：{{EXPECTED_OUTPUT}}

## 知识与论证如何形成

### 概念、符号与命题

- 核心术语的原文定义和相邻概念边界：{{DEFINITIONS}}
- 符号、单位、坐标、基准和约定：{{NOTATION}}
- 命题、定理、模型或机制陈述：{{PROPOSITIONS}}
- 明示前提和隐含前提：{{ASSUMPTIONS}}
- 与本领域其他版本或学派的差异：{{ALTERNATIVE_FORMULATIONS}}

### 论证、推导与方法

- 论证起点、关键中间步和结论：{{ARGUMENT_CHAIN}}
- 公式由定义、数学推导、经验拟合还是引用得到：{{FORMULA_ORIGIN}}
- 方法输入、步骤、输出和停止条件：{{METHOD_PROCEDURE}}
- 例题、图表或案例是说明性、校准性还是验证性证据：{{EXAMPLE_ROLE}}
- 反例、例外或不成立条件：{{COUNTEREXAMPLES}}

### 原始来源谱系

- 作者自有论证与引用他人内容的边界：{{AUTHOR_VS_CITED}}
- 关键定义／公式／数据的最早可定位来源：{{UPSTREAM_SOURCE}}
- 本轮是否打开原始来源：{{PRIMARY_SOURCE_CHECK}}
- 多个教材是否共享同一上游来源：{{INDEPENDENCE_GROUP}}
- 版次更新是否改变关键内容：{{EDITION_CHANGE}}

## 决定性证据块

### C01｜{{ATOMIC_BOOK_CLAIM}}

- 声明性质与推断类型：定义／理论命题／推导／方法建议／历史叙述／本方判断
- 原文事实或命题：{{SOURCE_FACT}}
- 论证或证据来源：{{DERIVATION_CITATION_EXAMPLE}}
- 前提、符号、单位和适用域：{{ASSUMPTIONS_SCOPE}}
- 精确定位及上下文：{{EDITION_CHAPTER_PAGE_EQUATION_FIGURE}}
- 直接支持：{{DIRECTLY_SUPPORTS}}
- 不能支持：{{DOES_NOT_SUPPORT}}
- 作者解释：{{AUTHOR_INTERPRETATION}}
- 本方判断：{{ANALYST_JUDGMENT}}
- 上游来源、版本差异与冲突：{{UPSTREAM_VERSION_CONFLICT}}
- 原始来源核验和声明核查状态：{{CHECK}}

## 局限与适用域

| 会改变使用的问题 | 已核事实 | 对哪些 Cxx 有影响 |
| --- | --- | --- |
| 定义与学派差异 | {{FACT}} | {{CLAIMS}} |
| 推导前提或近似 | {{FACT}} | {{CLAIMS}} |
| 经验材料和引用谱系 | {{FACT}} | {{CLAIMS}} |
| 版本、译文或时代变化 | {{FACT}} | {{CLAIMS}} |
| 从教学示例外推到真实水利问题 | {{FACT}} | {{CLAIMS}} |

## 本方使用边界

- 整卡使用结论：{{USE_VERDICT}}
- 可用于：{{CAN_USE_FOR}}
- 不可用于：{{CANNOT_USE_FOR}}
- 对当前认识的影响：加强／削弱／限定／无变化：{{CHANGE}}
- 受影响术语、理论框架、方法或主题：{{AFFECTED_OBJECTS}}
- 需要追到哪些原始来源才能作为结果证据：{{PRIMARY_SOURCES_NEEDED}}

## 补读资格门与最小路径

| 资格门 | 是／否 | 依据 |
| --- | --- | --- |
| 有明确且高影响的理论或方法决策 | {{YES_NO}} | {{BASIS}} |
| 有可定位的决定性证据缺口 | {{YES_NO}} | {{BASIS}} |
| 原版、其他章节或原始文献可能改变判断 | {{YES_NO}} | {{BASIS}} |

- 最小证据路径：{{MINIMUM_PATH}}
- 停止条件或未触发理由：{{STOP_REASON}}

## 复查与变更

| 日期 | 版次与核查范围 | 发现／修订 | 执行者 |
| --- | --- | --- | --- |
| {{DATE}} | {{SCOPE}} | {{CHANGE}} | {{WHO}} |
