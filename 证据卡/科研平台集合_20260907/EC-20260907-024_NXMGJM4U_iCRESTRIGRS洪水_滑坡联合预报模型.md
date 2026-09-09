---
card_schema: "evidence-card-v1.2"
card_id: "EC-20260907-024"
card_version: "1.6.0"
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
generator_or_pipeline_version: "hydrology-evidence-cards-v1.6-deep-source-specific"
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

## 论文的核心结论

- **研究了什么：** 对象是北卡罗来纳州西部四个流域在2004年Ivan飓风中的小时洪水与滑坡联合预报。
- **数据是什么：** 共享降雨和土壤水分状态，CREST使用流域水文/流量资料，TRIGRS使用90米网格地形和边坡参数；滑坡结果同事件清单比较。
- **方法是什么：** 作者连接CREST与TRIGRS，在北卡罗来纳州西部四个流域重建2004年Ivan飓风；以小时流量过程验证水文，并在90米网格上比较滑坡预测与清单。
- **得到什么：** 小时洪水过程与观测总体一致；滑坡分类总体准确率报告为98.9%，真阳性率为56.4%，较独立TRIGRS有所改善。两个指标的差距意味着大量稳定网格可能抬高总体准确率。

## 研究问题、对象与边界

暴雨同时引发洪水和滑坡，需要共享降雨与土壤水分状态。研究尝试以较少输入构建区域级联合预报。

对象是北卡罗来纳州西部四个流域在2004年Ivan飓风中的小时洪水与滑坡联合预报。

**独立分析单位：** 四个流域、小时过程和90米网格；网格类别高度不平衡。

## 数据与证据材料

| 数据层 | 本文实际使用或本轮可确认的内容 | 在证据链中的作用 |
|---|---|---|
| 原始／外部资料 | 共享降雨和土壤水分状态，CREST使用流域水文/流量资料，TRIGRS使用90米网格地形和边坡参数；滑坡结果同事件清单比较。 | 定义研究对象、边界条件或验证参照 |
| 分析单位 | 四个流域、小时过程和90米网格；网格类别高度不平衡。 | 决定样本量和可推广范围 |
| 主要输出 | 小时流量、土壤水分、网格稳定/失稳分类及洪水—滑坡联合预报。 | 回答论文的研究问题 |

## 研究设计与方法链

1. 作者连接CREST与TRIGRS，在北卡罗来纳州西部四个流域重建2004年Ivan飓风；
2. 以小时流量过程验证水文，并在90米网格上比较滑坡预测与清单。

### 水文状态怎样改善滑坡初始条件

iCRESTRIGRS把网格化CREST水文模型与TRIGRS坡稳模型耦合。CREST以VIC型产流曲线分配净降水为地表径流和入渗，用多线性水库表示地表/地下储量并逐格汇流；SCE-UA用于率定水文参数。CREST计算的土壤饱和度、地下水位和水文通量再成为TRIGRS瞬态入渗和安全系数计算的动态初始/边界条件，替代孤立TRIGRS对前期湿润状态的简化设定。

### 数据、事件和比较

案例覆盖北卡罗来纳西部四个流域及Hurricane Ivan在2004年9月16—18日触发的洪水、滑坡和泥石流。Stage IV小时降雨、卫星实际蒸散、DEM、土地覆盖、土壤纹理、四个USGS站流量和滑坡清单共同使用；栅格统一到3 arcsec，约90 m。风暴前24 h区域平均降雨约130 mm，不同位置峰值时间可相差5 h。耦合模型小时流量在四站相关系数均大于0.80，相对偏差处于±34%，三站NSCE不低于0.65，French Broad站因洪峰时间偏移表现较差。

### 滑坡指标不能只看总体准确率

耦合模型滑坡总体准确率98.9%，真正率56.4%，并优于独立TRIGRS。极高总体准确率可能主要来自非滑坡栅格占多数，真正率说明仍漏掉约四成已知滑坡；洪峰时移还暴露汇流和降雨空间误差。研究支持“动态水文状态有助于滑坡起始预测”，但不充分证明业务预警能力，因为使用历史事件资料，输入可获得时点、独立事件验证、误报率和提前量仍需核验。

### 联合预报怎样从降雨走到滑坡概率

iCRESTRIGRS把分布式降雨—径流过程与坡体入渗、孔压和稳定分析连接。降雨既控制坡面与河道洪水，也改变土体含水状态和安全系数，因此模型能够在统一气象驱动下输出洪水与降雨诱发滑坡危险。关键接口包括网格降雨、土壤水分、地下水或孔压状态以及地形和土体参数；这些量的空间分辨率和更新时间决定两类危险是否真正同步。

评价联合模型不能只看某一张危险分区图。洪水需要用流量、水位或淹没资料验证，滑坡需要用发生位置和时间评价命中、漏报与虚警，并检查同一场降雨校准后是否又用于验证。联合输出适合研究共同时段和空间重叠风险，但不自动证明洪水触发了滑坡或二者存在级联。迁移到其他流域必须重新构建地形、土地覆盖、土壤水力和强度参数，并报告资料不足带来的不确定性。


## 深入阅读：联合预报的状态共享与评价

### CREST提供的不是一个静态湿度值

CREST按网格处理降雨、入渗、地表和地下储量及汇流，经SCE-UA率定后生成小时流量和土壤饱和状态。TRIGRS再使用这些动态状态计算入渗、孔压与安全系数。方法增量在于滑坡模型继承事件前和事件中的湿润过程，而不是为整场风暴设同一个初始地下水位。

### 四流域水文验证有明显差异

Ivan事件覆盖2004年9月16—18日，风暴前24 h区域平均降雨约130 mm，不同位置峰值相差可达5 h。四个USGS站小时流量相关系数均大于0.80，相对偏差在±34%内，三站NSCE不低于0.65；French Broad站洪峰时移较明显。因而“总体一致”必须保留站点差异，洪峰时序误差会进一步影响滑坡状态。

### 分类不平衡改变98.9%的意义

90 m网格中绝大多数位置没有滑坡，总体准确率容易被真阴性抬高。98.9%与56.4%真阳性率并列说明模型正确识别了大量稳定网格，却仍漏掉约四成已知滑坡。完整评价还需假阳性率、精确率、空间容忍和滑坡清单漏记。业务预警不能只宣传总体准确率。

### 联合输出不等于灾害级联

洪水和滑坡共享降雨与土壤水分，说明它们有共同驱动和状态耦合；论文并未因此证明洪水直接触发滑坡或滑坡反过来改变洪水。若研究级联，还需物质进入河道、堵塞或河床变化等反馈。当前模型适合同时预报两类危险并分析共现窗口。

### 迁移和前瞻预报要求

新流域需要地形、土地覆盖、土壤水力和强度参数以及可靠滑坡清单。还应按预报时点限制输入，报告提前量并在独立风暴验证。本文支持动态水文状态改善滑坡初始条件的假设，但单场历史重建和有限流域不足以证明普遍业务性能。

## 比较、验证与不确定性

用小时流量过程验证水文模块，以滑坡清单评价联合模型并与独立TRIGRS比较。总体准确率必须同真阳性率共同解释。

## 关键结果

### 结果1

小时洪水过程与观测总体一致；

### 结果2

滑坡分类总体准确率报告为98.9%，真阳性率为56.4%，较独立TRIGRS有所改善。

### 结果3

两个指标的差距意味着大量稳定网格可能抬高总体准确率。

## 科学贡献

本文用CREST提供的时变土壤水分改善TRIGRS滑坡初始状态，在同一降雨过程下联合输出小时洪水与90米网格滑坡可能性。这一状态耦合是方法增量。评价上，98.9%总体准确率与56.4%真阳性率的差距使类别不平衡问题成为结论的一部分：模型能正确识别大量稳定网格，但仍漏掉明显比例的真实滑坡。

## 对后续研究的具体价值

可支持洪水—滑坡共用状态变量和联合预警设计，也提供一个必须同时报告召回率、误报率和总体准确率的典型案例。

## 证据边界与待核问题

90米网格、四个流域和单场飓风限制迁移；56.4%的真阳性率表明仍有明显漏报，部分数据需申请获得。

下一步应做：精读混淆矩阵、滑坡清单质量、耦合接口、参数率定和提前量；比较更新的联合预报模型。

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
