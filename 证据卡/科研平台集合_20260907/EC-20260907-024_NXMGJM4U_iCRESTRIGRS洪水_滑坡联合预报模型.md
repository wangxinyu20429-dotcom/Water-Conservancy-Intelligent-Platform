---
card_schema: "evidence-card-v1.2"
card_id: "EC-20260907-024"
card_version: "1.1.0"
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
generator_or_pipeline_version: "hydrology-evidence-cards-v1.3-full-content-rewrite"
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

> **一句话读懂：** 暴雨同时引发洪水和滑坡，需要共享降雨与土壤水分状态。研究尝试以较少输入构建区域级联合预报。 小时洪水过程与观测总体一致；滑坡分类总体准确率报告为98.9%，真阳性率为56.4%，较独立TRIGRS有所改善。两个指标的差距意味着大量稳定网格可能抬高总体准确率。 最大限制是：90米网格、四个流域和单场飓风限制迁移；56.4%的真阳性率表明仍有明显漏报，部分数据需申请获得。

## 先看结论

- **研究了什么：** 对象是北卡罗来纳州西部四个流域在2004年Ivan飓风中的小时洪水与滑坡联合预报。
- **数据是什么：** 共享降雨和土壤水分状态，CREST使用流域水文/流量资料，TRIGRS使用90米网格地形和边坡参数；滑坡结果同事件清单比较。
- **方法是什么：** 作者连接CREST与TRIGRS，在北卡罗来纳州西部四个流域重建2004年Ivan飓风；以小时流量过程验证水文，并在90米网格上比较滑坡预测与清单。
- **得到什么：** 小时洪水过程与观测总体一致；滑坡分类总体准确率报告为98.9%，真阳性率为56.4%，较独立TRIGRS有所改善。两个指标的差距意味着大量稳定网格可能抬高总体准确率。
- **为什么值得用：** 可支持洪水—滑坡共用状态变量和联合预警设计，也提供一个必须同时报告召回率、误报率和总体准确率的典型案例。

## 研究要解决什么问题

暴雨同时引发洪水和滑坡，需要共享降雨与土壤水分状态。研究尝试以较少输入构建区域级联合预报。

这里真正需要回答的不是“论文用了什么软件”，而是作者如何把水文或灾害输入转成可以检验的结构、网络、地形或风险输出。本文的研究问题因此要放在它自己的对象和证据层级内理解：对象是北卡罗来纳州西部四个流域在2004年Ivan飓风中的小时洪水与滑坡联合预报。

## 研究对象与边界

对象是北卡罗来纳州西部四个流域在2004年Ivan飓风中的小时洪水与滑坡联合预报。

**独立分析单位：** 四个流域、小时过程和90米网格；网格类别高度不平衡。

这一区分决定了结果能外推到哪里。网格、道路节点、蒙特卡洛运行或同一事件的多个时步通常共享输入和模型假设，不能当作同等数量的独立真实案例。

## 数据到底是什么

| 数据层 | 本文实际使用或本轮可确认的内容 | 在证据链中的作用 |
|---|---|---|
| 原始／外部资料 | 共享降雨和土壤水分状态，CREST使用流域水文/流量资料，TRIGRS使用90米网格地形和边坡参数；滑坡结果同事件清单比较。 | 定义研究对象、边界条件或验证参照 |
| 派生／模拟数据 | 由上述资料经论文方法产生中间状态和输出；不得把模拟值写成现场实测 | 连接输入与最终结论 |
| 分析单位 | 四个流域、小时过程和90米网格；网格类别高度不平衡。 | 决定样本量和可推广范围 |
| 主要输出 | 小时流量、土壤水分、网格稳定/失稳分类及洪水—滑坡联合预报。 | 回答论文的研究问题 |
| 可获得性 | 本轮通过Zotero索引读取主文约59,996字符；原始数据、代码或补充材料是否完整开放，仍以原文数据/代码声明为准 | 决定能否独立复现 |

数据必须按性质使用。观测可以约束现实状态；模型派生量用于回答模型设定下的问题；人为情景用于比较可能后果。三者不能互相冒充。原文没有报告样本量、分辨率、预处理或数据拆分时，本卡保留缺口，不从同类论文补写。

## 方法是怎样一步步得到结果的

1. 作者连接CREST与TRIGRS，在北卡罗来纳州西部四个流域重建2004年Ivan飓风；
2. 以小时流量过程验证水文，并在90米网格上比较滑坡预测与清单。

方法链的核心输出是：小时流量、土壤水分、网格稳定/失稳分类及洪水—滑坡联合预报。。评价这条链时要逐段检查输入误差、参数来源、模块间转换和输出定义；前一模块“运行成功”不代表后一模块的科学结论已经被验证。

## 验证和比较是否站得住

用小时流量过程验证水文模块，以滑坡清单评价联合模型并与独立TRIGRS比较。总体准确率必须同真阳性率共同解释。

需要区分五种证据：参数校准、同一数据内的拟合、内部一致性检查、独立样本验证和真实业务表现。只有论文实际完成的层级才能写进结论。若只做情景比较，结果说明模型内部机制或敏感性；若同观测比较，还要检查观测误差、评价分母和是否在调参后重复使用同一数据。

## 最关键的研究结果

### 结果1

小时洪水过程与观测总体一致；

**怎样理解：** 该结果只在上述研究对象、输入、比较和模型设定内成立；若原文没有同时报告不确定性或外部验证，本卡不替作者补出。

### 结果2

滑坡分类总体准确率报告为98.9%，真阳性率为56.4%，较独立TRIGRS有所改善。

**怎样理解：** 该结果只在上述研究对象、输入、比较和模型设定内成立；若原文没有同时报告不确定性或外部验证，本卡不替作者补出。

### 结果3

两个指标的差距意味着大量稳定网格可能抬高总体准确率。

**怎样理解：** 该结果只在上述研究对象、输入、比较和模型设定内成立；若原文没有同时报告不确定性或外部验证，本卡不替作者补出。

**结果精度状态：** 本卡只保留当前正文中已经识别的方向和明确数字。对没有定位到置信区间、误差范围或重复试验的结果，统一理解为“原文在当前阅读范围内未报告/本轮未定位到不确定性”，不能据此制造更高精度。

## 作者如何解释这些结果

作者的解释集中在以下逻辑：小时洪水过程与观测总体一致；滑坡分类总体准确率报告为98.9%，真阳性率为56.4%，较独立TRIGRS有所改善。两个指标的差距意味着大量稳定网格可能抬高总体准确率。 这属于作者依据模型、观测或案例给出的机制解释。它若没有干预对照、识别设计或独立样本支撑，就不能升级为一般因果规律。

## 这篇研究真正贡献了什么

可支持洪水—滑坡共用状态变量和联合预警设计，也提供一个必须同时报告召回率、误报率和总体准确率的典型案例。

对本平台而言，贡献应拆成可检查对象：它是否给出新的数据、把既有数据连成新的方法链、提供可复用的指标/对照，或只提出值得验证的框架。本文当前最可用的是与上述研究对象直接相连的方法和结果，不是从题名推演出的泛化创新点。

## 复现需要什么

至少需要：共享降雨和土壤水分状态，CREST使用流域水文/流量资料，TRIGRS使用90米网格地形和边坡参数；滑坡结果同事件清单比较。；需要完整实现或取得论文使用的方法、参数和软件环境；需要按作者定义生成小时流量、土壤水分、网格稳定/失稳分类及洪水—滑坡联合预报。；还要用用小时流量过程验证水文模块，以滑坡清单评价联合模型并与独立TRIGRS比较。总体准确率必须同真阳性率共同解释。作为最低核验线索。若数据、代码、随机种子、版本或补充材料未获得，只能称“可重建方法逻辑”，不能称“已复现”。

## 对当前水利科研平台的用途

可支持洪水—滑坡共用状态变量和联合预警设计，也提供一个必须同时报告召回率、误报率和总体准确率的典型案例。

**可以支持：** 研究问题拆解、数据字段设计、候选方法或评价指标选择，以及确定下一轮精读和验证任务。

**不能直接支持：** 把单一案例数字写成通用阈值，把模拟相关写成现实因果，把软件可运行写成预测可靠，或在未经导师确认时直接形成正式选题。

## 结论边界与下一步精读

90米网格、四个流域和单场飓风限制迁移；56.4%的真阳性率表明仍有明显漏报，部分数据需申请获得。

下一步应做：精读混淆矩阵、滑坡清单质量、耦合接口、参数率定和提前量；比较更新的联合预报模型。。复核时优先重开承载主要数字的表/图、数据和方法章节、验证段落及数据代码声明；若这些材料不存在，应把缺失本身记录为证据限制。

## 文献信息与原文入口

- **原题名：** iCRESTRIGRS: A coupled modeling system for cascading flood–landslide disaster forecasting
- **作者／责任机构：** Ke Zhang；Xianwu Xue；Yang Hong；Jonathan J. Gourley；Ning Lu；Zhanming Wan；Zhen Hong；Rick Wooten
- **日期：** 2016-12-20
- **期刊／发布机构：** Hydrology and Earth System Sciences
- **DOI或正式入口：** [10.5194/hess-20-5035-2016](https://doi.org/10.5194/hess-20-5035-2016)
- **Zotero入口：** [打开条目](zotero://select/library/items/NXMGJM4U)
- **本轮实际读取：** Zotero索引全文约60,009字符，索引页数14/14
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
