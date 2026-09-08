---
card_schema: "evidence-card-v1.2"
card_id: "EC-20260907-024"
card_version: "1.0.0"
card_type: "source_evidence"
artifact_type: "journal_article"
evidence_roles: ["context_only"]
workflow_status: "screened"
completion_level: "L1"
source_work_id: "DOI-10.5194/hess-20-5035-2016"
source_manifestation_id: "ZOTERO-ATTACHMENT-ZL9QTNK7"
source_version: "zotero-indexed-attachment"
source_snapshot_hash: "sha256:a671f919c752a7302c7f4a8d82e1e5f53ad4380e3262f0b1ae39e883494d69f3"
source_provenance: "local_zotero"
acquired_via: "zotero_local_api"
acquired_at: "2026-09-07"
validity_checked_at: "2026-09-07"
language: "English"
access_level: "private_zotero_fulltext"
zotero_item_key: "NXMGJM4U"
project_ids: []
source_batch: "ZOTERO-RUN-20260907-01"
research_question_ids: []
decision_ids: []
related_card_ids: []
independence_group_ids: ["IG-NXMGJM4U"]
version_family_ids: ["VF-10.5194/hess-20-5035-2016"]
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

# EC-20260907-024 iCRESTRIGRS洪水—滑坡联合预报模型

> **初读结论：** CREST水文模型与TRIGRS边坡稳定模型耦合后，在北卡罗来纳州Ivan飓风案例中取得较高总体分类准确率，但滑坡真阳性率仅56.4%，显示类别不平衡会掩盖漏报。

## 文献信息与原文入口

- **原题名：** iCRESTRIGRS: A coupled modeling system for cascading flood–landslide disaster forecasting
- **作者／责任机构：** Ke Zhang；Xianwu Xue；Yang Hong；Jonathan J. Gourley；Ning Lu；Zhanming Wan；Zhen Hong；Rick Wooten
- **日期：** 2016-12-20
- **期刊／发布机构：** Hydrology and Earth System Sciences
- **DOI或正式入口：** [10.5194/hess-20-5035-2016](https://doi.org/10.5194/hess-20-5035-2016)
- **Zotero入口：** [打开条目](zotero://select/library/items/NXMGJM4U)
- **本轮实际读取：** Zotero索引全文约60,009字符，索引页数14/14
- **当前证据级别：** L1机器辅助初读；尚未完成人工逐条原文复核，不能承载正式主题结论。

## 这份来源为什么值得读

暴雨同时引发洪水和滑坡，需要共享降雨与土壤水分状态。研究尝试以较少输入构建区域级联合预报。

## 来源具体做了什么

作者连接CREST与TRIGRS，在北卡罗来纳州西部四个流域重建2004年Ivan飓风；以小时流量过程验证水文，并在90米网格上比较滑坡预测与清单。

## 初读抓到的主要结果或观点

小时洪水过程与观测总体一致；滑坡分类总体准确率报告为98.9%，真阳性率为56.4%，较独立TRIGRS有所改善。两个指标的差距意味着大量稳定网格可能抬高总体准确率。

## 对科研平台的潜在价值

可支持洪水—滑坡共用状态变量和联合预警设计，也提供一个必须同时报告召回率、误报率和总体准确率的典型案例。

## 使用边界

90米网格、四个流域和单场飓风限制迁移；56.4%的真阳性率表明仍有明显漏报，部分数据需申请获得。

## 下一步精读任务

精读混淆矩阵、滑坡清单质量、耦合接口、参数率定和提前量；比较更新的联合预报模型。

**候选主题信号：** 洪水滑坡、联合预报、CREST、TRIGRS。这些标签只用于后续聚合，不代表主题已经成立。

<details>
<summary><strong>机器审计与校验字段（默认折叠）</strong></summary>

以下声明只记录本轮初读线索，尚未人工核验，不得作为主题承重证据。

~~~claim-json
{
  "claim_id": "EC-20260907-024-C01",
  "source_id": "ZOTERO-ATTACHMENT-ZL9QTNK7",
  "claim_type": "textual",
  "statement_role": "analyst_judgment",
  "inference_type": "descriptive",
  "support_status": "not_checked",
  "statement": "CREST水文模型与TRIGRS边坡稳定模型耦合后，在北卡罗来纳州Ivan飓风案例中取得较高总体分类准确率，但滑坡真阳性率仅56.4%，显示类别不平衡会掩盖漏报。",
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
  "independence_group_ids": ["IG-NXMGJM4U"],
  "verification_status": "not_checked",
  "verified_by": "",
  "verified_at": ""
}
~~~

</details>
