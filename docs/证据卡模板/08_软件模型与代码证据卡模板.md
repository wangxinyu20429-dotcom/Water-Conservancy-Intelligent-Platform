---
card_schema: "evidence-card-v1.1"
card_id: "{{CARD_ID}}"
evidence_type: "software-model-code"
status: "draft"
zotero_item_key: "{{ZOTERO_KEY}}"
source_version: "{{SOURCE_VERSION}}"
reading_scope: "metadata_only"
source_provenance: "local_zotero_or_official_source"
direct_source_verified: false
created_at: "{{CREATED_AT}}"
updated_at: "{{CREATED_AT}}"
---

# 软件、模型与代码证据卡：{{TITLE}}

> 可下载、可安装、测试通过、产生输出、复现论文和科学有效是不同状态。本卡分别记录科学模型、具体实现、运行环境和验证证据。

## 导师三分钟判断

- 当前实现或模型问题：{{SOFTWARE_QUESTION}}
- 该制品可能影响的决定：{{INTENDED_DECISION}}
- 科学模型／算法与本实现的关系：{{MODEL_IMPLEMENTATION_RELATION}}
- 被核版本：release／tag／commit／容器摘要／模型权重：{{ARTIFACT_VERSION}}
- 当前最高状态：仅发现／可获取／可安装／测试通过／样例运行／目标运行／结果复现／独立验证：{{HIGHEST_STATE}}
- 最关键验证或运行事实：{{DECISIVE_FACT}}
- 最大边界：{{LOAD_BEARING_LIMIT}}
- 使用结论：可直接使用／限条件使用／仅作线索／暂不可用／与当前问题无关：{{WHY}}

### 决定性实现声明（最多三项）

| 声明 | 实现／运行／验证事实 | 版本和环境 | 定位 |
| --- | --- | --- | --- |
| C01 | {{SOFTWARE_CLAIM}} | {{VERSION_ENVIRONMENT}} | {{LOCATOR}} |

## 来源身份与阅读边界

- 软件／模型／仓库名称和维护者：{{TITLE}}；{{MAINTAINERS}}
- 仓库、归档 DOI、包索引、模型卡或官方页面：{{URL}}；{{DOI}}
- Zotero item key：{{ZOTERO_KEY}}
- 当前版本、固定 commit、release、容器和权重标识：{{VERSION_BUNDLE}}
- 论文版本、归档快照与活仓库关系：{{PAPER_ARCHIVE_LIVE_RELATION}}
- 许可证、依赖许可证和模型／数据许可：{{LICENSES}}
- 实际取得并检查：README／文档／源代码／测试／发布记录／运行日志：{{MATERIALS}}
- 未阅读、未克隆、未运行或未取得：{{UNREAD_OR_MISSING}}
- 代码定位规则：{{COMMIT_FILE_LINE_FUNCTION}}

## 研究或使用问题

- 要核查的具体命题：接口存在／算法已实现／特定输入可运行／输出正确／论文结果可复现／目标流域有效：{{CARD_QUESTION}}
- 目标输入、输出、规模、时效、精度和计算资源：{{USE_REQUIREMENTS}}
- 接受或停止判据：{{DECISION_THRESHOLD}}

## 软件与模型证据如何产生

### 科学模型与实现边界

- 科学方程、算法或概念模型：{{SCIENTIFIC_MODEL}}
- 实现了哪些部分，省略、近似或新增哪些部分：{{IMPLEMENTED_SCOPE}}
- 输入、输出、单位、坐标、时间基准和数据契约：{{IO_CONTRACT}}
- 默认参数、初始化、随机性、数值精度和停止条件：{{DEFAULTS_NUMERICS}}
- 适用假设、业务前提和不支持场景：{{ASSUMPTIONS_LIMITS}}

### 版本、环境与可追溯性

- 语言、运行时、操作系统、硬件和关键依赖：{{ENVIRONMENT}}
- 安装、构建、配置、种子和外部服务：{{SETUP}}
- 数据、模型权重、配置与代码如何绑定：{{ARTIFACT_BINDING}}
- 从论文方法到函数／配置／脚本的映射：{{PAPER_CODE_MAPPING}}
- 活仓库后续变化是否会改变论文解释：{{VERSION_DRIFT}}

### 验证、确认与运行状态

- 单元、集成、回归和数值测试证明什么：{{VERIFICATION}}
- 与解析解、基准实现或独立实现比较：{{BENCHMARK}}
- 与观测、实验或真实工程比较：{{VALIDATION}}
- 校准数据与验证数据是否独立：{{CALIBRATION_VALIDATION_INDEPENDENCE}}
- 性能、稳定性、资源消耗和失败处理：{{PERFORMANCE_FAILURES}}
- 本次实际执行的命令、输入版本、环境、输出和日志：{{ACTUAL_RUN}}
- 若未运行，明确写“未运行”，不得保留看似完成的空日志。

## 决定性证据块

### C01｜{{ATOMIC_SOFTWARE_CLAIM}}

- 来源角色：实现条件／版本关系／运行事实／验证结果／维护者解释／本方判断
- 来源组件：release／commit／代码／测试／README／文档／容器／运行日志
- 原文或实查事实：{{SOURCE_OR_RUN_FACT}}
- 证据产生方式：静态检查／项目测试／样例运行／目标运行／结果复现／独立验证：{{HOW_ESTABLISHED}}
- 输入、输出、配置、环境和适用范围：{{EXACT_SCOPE}}
- 数值、容差、基准和不确定性：{{VALUE_TOLERANCE}}
- 版本束与精确定位：{{COMMIT_FILE_LINE_LOG_ARCHIVE}}
- 直接支持：{{DIRECTLY_SUPPORTS}}
- 不能支持：{{DOES_NOT_SUPPORT}}
- 作者或维护方解释：{{MAINTAINER_INTERPRETATION}}
- 本方判断：{{ANALYST_JUDGMENT}}
- 上游论文、数据、依赖和独立性组：{{UPSTREAM_DEPENDENCY}}
- 核查状态和日期：{{CHECK}}

## 状态证据表

只勾有真实证据的最高状态，后一级不能由前一级推出。

| 状态 | 本轮证据 | 结论 |
| --- | --- | --- |
| 固定版本可获取 | {{EVIDENCE}} | 是／否／未核 |
| 可在记录环境安装或构建 | {{EVIDENCE}} | {{RESULT}} |
| 项目自带测试通过 | {{EVIDENCE}} | {{RESULT}} |
| 官方样例产生预期输出 | {{EVIDENCE}} | {{RESULT}} |
| 当前目标输入成功运行 | {{EVIDENCE}} | {{RESULT}} |
| 与论文指定结果在容差内一致 | {{EVIDENCE}} | {{RESULT}} |
| 独立数据或实现验证科学结论 | {{EVIDENCE}} | {{RESULT}} |

## 局限、安全与维护

- 已知 bug、开放问题、失败输入和数值不稳定：{{KNOWN_ISSUES}}
- 维护活跃度只记录事实，不作为科学有效性：{{MAINTENANCE_FACTS}}
- 安全、隐私、凭据和外部调用边界：{{SECURITY}}
- 论文版本无法绑定、依赖漂移或未固定随机性：{{REPRODUCIBILITY_GAPS}}
- 目标流域、尺度、硬件或业务环境迁移风险：{{TRANSFER_RISK}}

## 本方使用边界

- 整卡使用结论：{{USE_VERDICT}}
- 可用于：{{CAN_USE_FOR}}
- 不可用于：{{CANNOT_USE_FOR}}
- 对当前研究可执行性或方法判断的影响：{{CHANGE}}
- 受影响主题、项目、数据或实验：{{AFFECTED_OBJECTS}}
- 依赖键：{{DEPENDENCY_KEY}}
- 复查触发：release、commit、依赖、模型权重、接口、许可或安全公告变化：{{RECHECK_TRIGGER}}

## 补读／运行资格门与最小路径

| 资格门 | 是／否 | 依据 |
| --- | --- | --- |
| 有明确且高影响的实现或科学决策 | {{YES_NO}} | {{BASIS}} |
| 有可定位的决定性代码、版本或运行缺口 | {{YES_NO}} | {{BASIS}} |
| 打开代码、固定环境或最小运行可能改变判断 | {{YES_NO}} | {{BASIS}} |

- 最小路径：{{MINIMUM_PATH}}
- 预先定义的期望、容差和停止条件：{{EXPECTED_TOLERANCE_STOP}}
- 未触发理由：{{STOP_REASON}}

## 复查与变更

| 日期 | 版本／环境与核查范围 | 发现／修订 | 执行者 |
| --- | --- | --- | --- |
| {{DATE}} | {{SCOPE}} | {{CHANGE}} | {{WHO}} |
