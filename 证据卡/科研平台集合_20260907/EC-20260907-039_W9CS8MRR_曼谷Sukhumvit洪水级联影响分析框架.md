---
card_schema: "evidence-card-v1.2"
card_id: "EC-20260907-039"
card_version: "1.4.0"
card_type: "source_evidence"
artifact_type: "journal_article"
evidence_roles: ["context_only"]
workflow_status: "screened"
completion_level: "L1"
source_work_id: "DOI-10.3390/w10010081"
source_manifestation_id: "ZOTERO-ATTACHMENT-3822QJHE"
source_version: "zotero-indexed-attachment"
source_snapshot_hash: "sha256:d2060ab11944a7e7677f4ebfa92ee701d148be430f72d96d8c0c0910b20f0f40"
source_provenance: "local_zotero"
acquired_via: "zotero_local_api"
acquired_at: "2026-09-07"
validity_checked_at: "2026-09-07"
language: "unknown"
access_level: "private_zotero_fulltext"
zotero_item_key: "W9CS8MRR"
project_ids: []
source_batch: "ZOTERO-RUN-20260907-01"
research_question_ids: []
decision_ids: []
related_card_ids: []
independence_group_ids: ["IG-W9CS8MRR"]
version_family_ids: ["VF-10.3390/w10010081"]
reading_scope: "full_text"
extraction_method: "ai_assisted"
generator_or_pipeline_version: "hydrology-evidence-cards-v1.4-deep-rewrite"
verified_claim_ids: []
verified_by: ""
verified_at: ""
human_review_status: "not_started"
human_reviewer: ""
funding: []
commissioning_party: []
declared_conflicts: []
review_independence: "not_assessed"
confidentiality: "internal"
water_context_status: "not_applicable"
method_modules: []
l3_gate_decision: false
l3_gate_gap: false
l3_gate_change: false
relevance: "supporting"
verification_readiness: "clue_only"
applicability: "transfer_check_required"
decision_effect: "no_change"
load_bearing_conflict: false
unresolved_conflict_ids: []
recheck_trigger: "Only upgrade after a human reopens the exact source and verifies decisive locators."
---

# EC-20260907-039 曼谷Sukhumvit洪水级联影响分析框架

> **一句话读懂：** 直接损失图难以表达服务延迟、营业损失和居民不便。研究旨在系统识别洪水对城市基础设施与服务的间接和级联影响。 案例指出道路易涝会向多项基础设施和服务传播，居民与企业尤其关心上学、通勤、采购订单和商务活动延误。供水抢修因道路受阻延迟会带来服务与收入损失，污染洪水侵入供水系统还涉及公共健康。 最大限制是：作者称框架具有通用性，但结论来自单一地区且数据量大；访谈和估算的代表性、损失计算和验证程度需核验。

## 先看结论

- **研究了什么：** 对象是曼谷Sukhumvit地区洪水对道路、公用事业、居民和企业服务的间接及级联影响。
- **数据是什么：** 危险度来自既有1D—2D MIKEFLOOD模型；影响资料来自现场调查、居民和企业访谈、公用事业记录及GIS空间数据。样本量和代表性需回原文表格核对。
- **方法是什么：** 作者使用既有1D—2D MIKEFLOOD模型描述危险度，结合现场调查、居民和企业访谈、公用事业记录，绘制因果环图、HAZUR韧性图、树图和GIS地图。
- **得到什么：** 案例指出道路易涝会向多项基础设施和服务传播，居民与企业尤其关心上学、通勤、采购订单和商务活动延误。供水抢修因道路受阻延迟会带来服务与收入损失，污染洪水侵入供水系统还涉及公共健康。
- **为什么值得用：** 可作为平台从直接淹没扩展到服务、行为和经济后果的早期方法来源，也提供不同受众的可视化选择。

## 研究要解决什么问题

直接损失图难以表达服务延迟、营业损失和居民不便。研究旨在系统识别洪水对城市基础设施与服务的间接和级联影响。

## 研究对象与边界

对象是曼谷Sukhumvit地区洪水对道路、公用事业、居民和企业服务的间接及级联影响。

**独立分析单位：** 受访者/企业、公用事业记录、基础设施节点和空间单元。

这一区分决定了结果能外推到哪里。网格、道路节点、蒙特卡洛运行或同一事件的多个时步通常共享输入和模型假设，不能当作同等数量的独立真实案例。

## 数据到底是什么

| 数据层 | 本文实际使用或本轮可确认的内容 | 在证据链中的作用 |
|---|---|---|
| 原始／外部资料 | 危险度来自既有1D—2D MIKEFLOOD模型；影响资料来自现场调查、居民和企业访谈、公用事业记录及GIS空间数据。样本量和代表性需回原文表格核对。 | 定义研究对象、边界条件或验证参照 |
| 派生／模拟数据 | 由上述资料经论文方法产生中间状态和输出；不得把模拟值写成现场实测 | 连接输入与最终结论 |
| 分析单位 | 受访者/企业、公用事业记录、基础设施节点和空间单元。 | 决定样本量和可推广范围 |
| 主要输出 | 受淹与服务延迟路径、企业损失、居民不便、供水抢修延迟和潜在公共健康影响。 | 回答论文的研究问题 |
| 可获得性 | 本轮通过Zotero索引读取主文约100,233字符；原始数据、代码或补充材料是否完整开放，仍以原文数据/代码声明为准 | 决定能否独立复现 |

数据必须按性质使用。观测可以约束现实状态；模型派生量用于回答模型设定下的问题；人为情景用于比较可能后果。三者不能互相冒充。原文没有报告样本量、分辨率、预处理或数据拆分时，本卡保留缺口，不从同类论文补写。

## 方法是怎样一步步得到结果的

1. 作者使用既有1D—2D MIKEFLOOD模型描述危险度，结合现场调查、居民和企业访谈、公用事业记录，绘制因果环图、HAZUR韧性图、树图和GIS地图。

方法链的核心输出是：受淹与服务延迟路径、企业损失、居民不便、供水抢修延迟和潜在公共健康影响。。评价这条链时要逐段检查输入误差、参数来源、模块间转换和输出定义；前一模块“运行成功”不代表后一模块的科学结论已经被验证。

## 验证和比较是否站得住

使用因果环图、HAZUR韧性图、树图和GIS互相连接影响路径，主要是多源案例三角互证；通用性尚需跨城市验证。

需要区分五种证据：参数校准、同一数据内的拟合、内部一致性检查、独立样本验证和真实业务表现。只有论文实际完成的层级才能写进结论。若只做情景比较，结果说明模型内部机制或敏感性；若同观测比较，还要检查观测误差、评价分母和是否在调参后重复使用同一数据。

## 全文证据链展开

### 多来源材料怎样形成级联图

曼谷Sukhumvit案例把既有1D—2D MIKEFLOOD淹没结果与现场调查、访谈和公用事业记录结合。水动力模型提供哪里、何时、以多深的水直接影响道路和设施；调查与访谈补充设施之间的服务依赖、停运后果和居民/企业感受；记录资料约束资产和服务状态。作者随后用因果环图、HAZUR韧性图、树图和GIS地图分别表达反馈关系、基础设施依赖、后果分解和空间分布。

### 级联终点超出直接损失

道路积水不仅造成道路资产损坏，还会引起交通拥堵和延误，阻碍人员、商品和维修队伍到达；服务中断继续影响商业收入、居民舒适度以及其他基础设施运行。研究因此把关键服务、资产与货物流失、延误、收入损失和生活干扰纳入后果链。不同图形是同一证据的表达工具，不应被当成多份独立验证。

### 迁移框架需要哪些本地证据

作者认为方法经调整可用于其他城市，但分析需要大量本地信息。设施拓扑、服务关系、容量、备用路径、洪水模型精度和访谈代表性都会改变级联路径。案例主要证明系统化追踪间接影响是可行的，并识别道路作为传播枢纽；它没有用统一对照证明每项间接损失的因果份额。平台复用时应把每条边标注为观测、机构记录、专家判断或模型假设，并优先核验承重边。

### 定量洪水结果与定性依赖证据怎样结合

MIKEFLOOD给出Sukhumvit案例的积水深度、范围和时间，现场调查、公用事业记录与访谈补充设施功能和跨系统关系。因果环图、HAZUR韧性图、树图和GIS地图分别组织反馈、依赖、后果层次与空间位置；这些图使用的是相互关联的材料，不应被当成多次独立验证。每条级联边最好标明来自模拟、运营记录还是受访者判断。

案例显示交通可能成为间接影响传播枢纽，但收入损失、服务中断和生活干扰的因果份额未必都有统一计量。该框架适合做系统复盘和识别需要补证的关系；要迁移到其他城市，还需本地洪水模型、设施拓扑、服务容量、备用路径和利益相关者资料。只有当关键边被事件记录或对照情景验证后，才能进一步用于定量干预排序。

## 最关键的研究结果

### 结果1

案例指出道路易涝会向多项基础设施和服务传播，居民与企业尤其关心上学、通勤、采购订单和商务活动延误。

### 结果2

供水抢修因道路受阻延迟会带来服务与收入损失，污染洪水侵入供水系统还涉及公共健康。

**结果精度状态：** 本卡只保留当前正文中已经识别的方向和明确数字。对没有定位到置信区间、误差范围或重复试验的结果，统一理解为“原文在当前阅读范围内未报告/本轮未定位到不确定性”，不能据此制造更高精度。

## 作者如何解释这些结果

作者的解释集中在以下逻辑：案例指出道路易涝会向多项基础设施和服务传播，居民与企业尤其关心上学、通勤、采购订单和商务活动延误。供水抢修因道路受阻延迟会带来服务与收入损失，污染洪水侵入供水系统还涉及公共健康。 这属于作者依据模型、观测或案例给出的机制解释。它若没有干预对照、识别设计或独立样本支撑，就不能升级为一般因果规律。

## 这篇研究真正贡献了什么

可作为平台从直接淹没扩展到服务、行为和经济后果的早期方法来源，也提供不同受众的可视化选择。

对本平台而言，贡献应拆成可检查对象：它是否给出新的数据、把既有数据连成新的方法链、提供可复用的指标/对照，或只提出值得验证的框架。本文当前最可用的是与上述研究对象直接相连的方法和结果，不是从题名推演出的泛化创新点。

## 复现需要什么

至少需要：危险度来自既有1D—2D MIKEFLOOD模型；影响资料来自现场调查、居民和企业访谈、公用事业记录及GIS空间数据。样本量和代表性需回原文表格核对。；需要完整实现或取得论文使用的方法、参数和软件环境；需要按作者定义生成受淹与服务延迟路径、企业损失、居民不便、供水抢修延迟和潜在公共健康影响。；还要用使用因果环图、HAZUR韧性图、树图和GIS互相连接影响路径，主要是多源案例三角互证；通用性尚需跨城市验证。作为最低核验线索。若数据、代码、随机种子、版本或补充材料未获得，只能称“可重建方法逻辑”，不能称“已复现”。

## 对当前水利科研平台的用途

可作为平台从直接淹没扩展到服务、行为和经济后果的早期方法来源，也提供不同受众的可视化选择。

**可以支持：** 研究问题拆解、数据字段设计、候选方法或评价指标选择，以及确定下一轮精读和验证任务。

**不能直接支持：** 把单一案例数字写成通用阈值，把模拟相关写成现实因果，把软件可运行写成预测可靠，或在未经导师确认时直接形成正式选题。

## 结论边界与下一步精读

作者称框架具有通用性，但结论来自单一地区且数据量大；访谈和估算的代表性、损失计算和验证程度需核验。

下一步应做：精读样本、访谈问题、依赖矩阵、损失计算和验证；比较后续定量网络模型，区分关系识别与影响量化。。复核时优先重开承载主要数字的表/图、数据和方法章节、验证段落及数据代码声明；若这些材料不存在，应把缺失本身记录为证据限制。

## 文献信息与原文入口

- **原题名：** Methodological framework for analysing cascading effects from flood events: The case of sukhumvit area, bangkok, thailand
- **作者／责任机构：** Geofrey Hilly；Zoran Vojinovic；Sutat Weesakul；Arlex Sanchez；Duc Nguyen Hoang；Slobodan Djordjevic；Albert S. Chen；Barry Evans
- **日期：** 2018
- **期刊／发布机构：** Water
- **DOI或正式入口：** [10.3390/w10010081](https://doi.org/10.3390/w10010081)
- **Zotero入口：** [打开条目](zotero://select/library/items/W9CS8MRR)
- **本轮实际读取：** Zotero索引全文约100,258字符，索引页数26/26
- **当前证据级别：** L1机器辅助初读；尚未完成人工逐条原文复核，不能承载正式主题结论。

<details>
<summary><strong>校勘与人工复核备注（默认折叠）</strong></summary>

本卡由Zotero索引正文和既有初读记录重写，目的是让数据、方法和结果可见。尚未由课题组成员逐表逐图复核；任何进入正式主题或论文的承重数字，都必须回到Zotero原文核对页码、图表、单位、分母和限定语。

</details>

<details>
<summary><strong>机器审计与校验字段（默认折叠）</strong></summary>

以下声明只记录本轮初读线索，尚未人工核验，不得作为主题承重证据。

~~~claim-json
{
  "claim_id": "EC-20260907-039-C01",
  "source_id": "ZOTERO-ATTACHMENT-3822QJHE",
  "claim_type": "textual",
  "statement_role": "analyst_judgment",
  "inference_type": "descriptive",
  "support_status": "not_checked",
  "statement": "曼谷案例把水动力模型、现场调查、访谈和公用事业记录结合，追踪道路受淹如何传播到供水、供电、交通、商业与公共健康，并比较多种可视化方式。",
  "evidence_origin": "AI-assisted screening of Zotero indexed text and source metadata",
  "scope": {"object_or_denominator": "source-level screening", "spatial": "not_checked", "temporal": "not_checked", "comparator": "not_checked"},
  "numeric": null,
  "locator": {"material": "Zotero indexed full text", "page_or_section": "abstract/conclusion or visible webpage; exact locator pending", "table_figure_clause_or_row": "not_checked", "context": "screening only"},
  "directly_supports": "检索、聚类和确定下一步精读顺序。",
  "does_not_support": "不支持正式科研结论、因果判断、效果量、迁移结论或主题激活。",
  "author_interpretation": "not_checked",
  "analyst_judgment": "初读表述，需人工回到原文复核。",
  "method_requirements": {},
  "relations": {"supports": [], "contradicts": [], "qualifies": [], "depends_on": [], "reproduces": [], "supersedes": []},
  "independence_group_ids": ["IG-W9CS8MRR"],
  "verification_status": "not_checked",
  "verified_by": "",
  "verified_at": ""
}
~~~

</details>
