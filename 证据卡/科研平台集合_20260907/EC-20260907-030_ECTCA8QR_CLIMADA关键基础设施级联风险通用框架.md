---
card_schema: "evidence-card-v1.2"
card_id: "EC-20260907-030"
card_version: "1.0.0"
card_type: "source_evidence"
artifact_type: "journal_article"
evidence_roles: ["context_only"]
workflow_status: "screened"
completion_level: "L1"
source_work_id: "DOI-10.1016/j.ress.2023.109194"
source_manifestation_id: "ZOTERO-ATTACHMENT-EBDCQI4C"
source_version: "zotero-indexed-attachment"
source_snapshot_hash: "sha256:623881012301f247b719409bd46cf188d249091b2dd99bec70d503717f4952dd"
source_provenance: "local_zotero"
acquired_via: "zotero_local_api"
acquired_at: "2026-09-07"
validity_checked_at: "2026-09-07"
language: "en"
access_level: "private_zotero_fulltext"
zotero_item_key: "ECTCA8QR"
project_ids: []
source_batch: "ZOTERO-RUN-20260907-01"
research_question_ids: []
decision_ids: []
related_card_ids: []
independence_group_ids: ["IG-ECTCA8QR"]
version_family_ids: ["VF-10.1016/j.ress.2023.109194"]
reading_scope: "full_text"
extraction_method: "ai_assisted"
generator_or_pipeline_version: "hydrology-evidence-cards-v1.2-batch-screening"
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

# EC-20260907-030 CLIMADA关键基础设施级联风险通用框架

> **初读结论：** 开源CLIMADA扩展框架把危险度、暴露、脆弱性、组件损坏、基础设施依赖和人口服务中断串联，并在2018年Michael飓风案例中用停电与媒体资料校正主要动态。

## 文献信息与原文入口

- **原题名：** A generalized natural hazard risk modelling framework for infrastructure failure cascades
- **作者／责任机构：** Evelyn Mühlhofer；Elco E. Koks；Chahan M. Kropf；Giovanni Sansavini；David N. Bresch
- **日期：** 06/2023
- **期刊／发布机构：** Reliability Engineering & System Safety
- **DOI或正式入口：** [10.1016/j.ress.2023.109194](https://doi.org/10.1016/j.ress.2023.109194)
- **Zotero入口：** [打开条目](zotero://select/library/items/ECTCA8QR)
- **本轮实际读取：** Zotero索引全文约99,168字符，索引页数18/18
- **当前证据级别：** L1机器辅助初读；尚未完成人工逐条原文复核，不能承载正式主题结论。

## 这份来源为什么值得读

自然灾害对基础设施的最终影响常表现为服务中断，且会沿电力、医疗、交通等依赖传播。研究寻求可迁移且数据需求相对克制的通用模型。

## 来源具体做了什么

框架先计算危险度、暴露与脆弱性造成的组件损坏，再按网络依赖传播级联，最后计算人口服务可得性；应用覆盖佛罗里达、乔治亚和阿拉巴马六类网络，并利用停电和媒体观察校准。

## 初读抓到的主要结果或观点

案例能再现若干重要服务中断动态与热点，这些结果超出直接资产损坏图。模型使用较简约的依赖启发式以提高可迁移性。

## 对科研平台的潜在价值

可作为平台“危险—损坏—服务—人口”统一对象链的强候选，并与本地网络模型和灾情记录结合验证。

## 使用边界

启发式依赖减少数据需求，也牺牲局地细节；媒体资料不等于完整验证。通用框架不能声称覆盖所有基础设施相互作用。

## 下一步精读任务

精读六类网络、依赖规则、校准资料、验证指标、开放代码版本和人口服务算法；识别需要本地替换的参数。

**候选主题信号：** CLIMADA、关键基础设施、级联风险、服务中断。这些标签只用于后续聚合，不代表主题已经成立。

<details>
<summary><strong>机器审计与校验字段（默认折叠）</strong></summary>

以下声明只记录本轮初读线索，尚未人工核验，不得作为主题承重证据。

~~~claim-json
{
  "claim_id": "EC-20260907-030-C01",
  "source_id": "ZOTERO-ATTACHMENT-EBDCQI4C",
  "claim_type": "textual",
  "statement_role": "analyst_judgment",
  "inference_type": "descriptive",
  "support_status": "not_checked",
  "statement": "开源CLIMADA扩展框架把危险度、暴露、脆弱性、组件损坏、基础设施依赖和人口服务中断串联，并在2018年Michael飓风案例中用停电与媒体资料校正主要动态。",
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
  "independence_group_ids": ["IG-ECTCA8QR"],
  "verification_status": "not_checked",
  "verified_by": "",
  "verified_at": ""
}
~~~

</details>
