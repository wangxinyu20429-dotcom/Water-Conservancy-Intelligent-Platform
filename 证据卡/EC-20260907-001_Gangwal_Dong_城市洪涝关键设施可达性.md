---
card_schema: "evidence-card-v1.2"
card_id: "EC-20260907-001"
card_version: "1.2.0"
card_type: "source_evidence"
artifact_type: "journal_article"
evidence_roles: ["original_research", "method_validation", "risk_mapping"]
workflow_status: "extracted"
completion_level: "L2"
source_work_id: "WORK-DOI-10.1016-J.RESS.2022.108555"
source_manifestation_id: "SRC-DOI-10.1016-J.RESS.2022.108555-VOR"
source_version: "published-version-of-record"
source_snapshot_hash: "sha256:010bedcebbd6c08f6d8f0be9857db74940f0eb858c054df1200875721a917125"
source_provenance: "local_zotero_pdf"
acquired_via: "zotero_local_api"
acquired_at: "2026-09-03"
validity_checked_at: "2026-09-07"
language: "en"
access_level: "private_zotero_fulltext"
zotero_item_key: "YAC6YLJF"
project_ids: []
research_question_ids: ["RQ-20260907-001"]
decision_ids: []
related_card_ids: []
independence_group_ids: ["IG-GANGWAL-DONG-2022-HARRIS-FLOOD-ACCESS"]
version_family_ids: ["VF-DOI-10.1016-J.RESS.2022.108555"]
reading_scope: "partial_full_text"
extraction_method: "ai_assisted"
generator_or_pipeline_version: "hydrology-evidence-cards-v1.2"
verified_claim_ids: []
verified_by: ""
verified_at: ""
human_review_status: "not_started"
human_reviewer: ""
funding: ["University of Delaware Research Foundation project 21A00986"]
commissioning_party: []
declared_conflicts: ["Authors declared no known competing financial interests or personal relationships."]
review_independence: "not_assessed"
confidentiality: "public_metadata_private_fulltext"
water_context_status: "partial"
method_modules: []
l3_gate_decision: false
l3_gate_gap: false
l3_gate_change: false
relevance: "central"
verification_readiness: "partially_verified"
applicability: "transfer_check_required"
decision_effect: "no_change"
load_bearing_conflict: true
unresolved_conflict_ids: ["CONF-EC-20260907-001-01"]
recheck_trigger: "Resolve the 85-versus-98 hospital count and obtain human review before any claim becomes theme-bearing."
---

# EC-20260907-001 城市洪涝下关键设施可达性快速失效预警与冗余制图

> 这是同一正式来源版本的唯一证据记录。当前为AI辅助L2草稿：Codex已经对照Zotero索引文本和PDF决定性页面定位声明，但尚未由本人完成人工复核。`verified_claim_ids`为空，任何声明都不能进入正式主题综合。

## L0 来源登记

- 原题名：Critical facility accessibility rapid failure early-warning detection and redundancy mapping in urban flooding
- 作者：Utkarsh Gangwal；Shangjia Dong
- 期刊与版本：*Reliability Engineering & System Safety*, Volume 224 (2022), Article 108555；正式期刊版
- 日期：PDF首页标注 online 2022-04-27；Zotero期刊日期字段为2022-08-01。两者分别表示在线发表和卷期日期，不作为版本冲突。
- DOI：[10.1016/j.ress.2022.108555](https://doi.org/10.1016/j.ress.2022.108555)
- 出版页面：[ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0951832022002046)
- Zotero入口：[个人库条目 YAC6YLJF](zotero://select/library/items/YAC6YLJF)；该链接只对本机/同一私人库有效。
- 当前取得材料：15页PDF，Zotero全文索引15/15页；ScienceDirect网页快照；PDF附件键`8E59ARLB`。
- 未取得或未读：在线补充材料为`not_obtained`；代码和底层数据实体为`not_found_after_check`（主文未给出单独Data/Code Availability声明）；参考文献逐条身份为`not_read`。
- 版本与独立性：本卡只代表上述正式期刊版。文中所有Harvey和500年一遇情景结果属于同一研究、同一作者团队和同一Harris County道路网络证据组，不得按图表或模拟次数重复计为独立研究。
- 本地保存边界：PDF和临时全文留在Zotero/临时读取环境；Git只保存本卡与稳定链接。

## L1 快速筛选

### 当前研究问题

该文在 Harris County 案例中，用什么证据支持城市洪涝下关键设施道路可达性快速失效的早期预警、关键道路识别与可达冗余制图？这些结果能够支持什么，在哪些模型假设和数据边界外不能使用？

### 快速决策摘要

- 潜在证据角色：城市洪涝道路网络功能失效建模方法；关键设施可达性指标；早期预警点和关键道路候选识别；设施可达冗余与社会脆弱性空间叠置。
- 关键线索：在作者构造的Harvey 38小时道路失效序列中，三类设施曲线均在第20步、即10小时处得到预警点；500年一遇情景的1000条模拟序列形成预警区域而不是唯一时刻。
- 首要风险：洪水传播序列部分由情景工程生成；道路失效为二元；出行半径预设；没有独立城市外部验证；医院数量在正文与图注中分别为85和98。
- 升级L2：是。本轮目的就是验证Zotero→证据卡链路，且正式PDF足以建立有页码和图号的条件性声明。
- 快速摘要依据：`EC-20260907-001-C02`、`EC-20260907-001-C05`、`EC-20260907-001-C12`。

### 阅读边界

- 已读：PDF主文的研究问题、方法、实验设计、结果、讨论与结论；重点回看PDF第5—12页的式(1)—式(2)、图2—图9和相邻正文。
- 未读：在线补充材料；作者引用的外部原始数据/代码；参考文献逐条核验。
- 当前允许判断：作者提出的方法如何定义可达性和预警点；在指定Harris County道路网络、出行半径和构造失效序列下得到的结果；作者公开报告的限制。
- 当前禁止判断：真实实时洪水预报已得到验证；识别道路在现实中实施保护必然延迟系统失效；社会脆弱性导致可达性损失；方法已经跨城市迁移；本文证明了普遍城市洪涝规律。

## L2 可用证据

### 原创研究的证据生成机制

#### 背景、缺口与任务

作者认为传统网络渗流阈值侧重完全崩溃，实际灾害中可能达不到；现有关键设施可达性研究也较少追踪道路扰动序列中的快速下降起点。论文因此把任务限定为：在逐步移除受洪水影响道路时，用“可在限定距离内到达至少一个关键设施的节点集合”刻画功能，找出下降速率开始加快的点，并将该点对应回道路网络。

#### 研究对象和分析单位

- 区域：美国Texas州Harris County。
- 道路网络：正文报告144,315个节点和203,671条边，按无向图处理。
- 设施类型：医院、食品商店、药房。商店1,235家、药房1,070家在正文与图注一致；医院数量存在85/98冲突。
- 洪水情景：2017 Hurricane Harvey，以及一个覆盖500年一遇洪泛区的模拟情景。
- 主要分析单位：道路网络节点、道路边，以及按逐步道路失效形成的网络状态；1000次Monte Carlo运行不是1000个独立城市或独立实证研究。

#### 数据与失效序列

- Harvey情景：作者报告38小时内28,143条边失效；187个洪水监测站中有128个出现淹没状态。传感器状态按2小时使用，邻近已失效道路及情景道路按30分钟扩展。
- 由于监测站不能覆盖详细淹没传播，作者按低程、相邻传播及每个分水区每30分钟移除`n=10`条低洼道路等规则补全序列，使总过程匹配38小时。
- 500年一遇情景：静态洪泛区内共58,956条边被移除；以38小时为总传播时间，随机选择初始失效位置并构造1000条序列。
- 这是一项网络模拟与案例研究。Harvey序列含真实传感器信息，但不等于逐道路、逐时刻的完整观测洪水传播。

#### 方法、指标和比较

- 可达性指标：robust component `R_t`，即仍可通过完整道路、且在出行半径内到达至少一个指定设施的节点集合。
- 出行半径：医院5 miles；商店与药房4 miles。正文说明这些阈值可按地区出行行为改变。
- 预警检测：把每步`R_t`与`t_i`放在log-log尺度，连接首尾点，并寻找与该线平行且y轴截距最大的曲线点；作者将它解释为可达性下降速率开始加快的预警点，而不是曲线最陡点。
- 辅助检查：比较相邻步可达性曲线梯度的差，观察预警点后波动是否增大。
- 韧性比较：用可达性曲线下面积AUC描述不同设施情景的整体网络韧性；论文同时强调预警发生时刻不能替代AUC。

#### 验证设计的实际强度

- 方法在一个真实城市道路网络上展示，并对500年一遇情景的初始位置与失效序列做1000次Monte Carlo变化。
- “验证预警点”的主要证据是同一模拟曲线在预警点后梯度差波动增加，属于内部一致性检查。
- 没有独立城市、独立洪水事件、留出道路网络或现实预警运行结果；不能把内部曲线检查写成外部预测验证。
- 论文提供访问半径敏感性分析，但没有用实际居民出行调查对5/4 miles阈值作本地校准。

#### 资金、冲突、数据与复现

- 资金：University of Delaware Research Foundation，project #21A00986。
- 作者声明：无已知可能影响研究的竞争性经济利益或个人关系。
- 主文未提供单独的数据和代码可用性声明。本轮未取得在线补充材料，也没有实际运行模型，所以复现状态为`not_checked`。
- Zotero `extra` 中存在“影响因子13.7、JCR Q1”等条目，但未附指标年份、学科类别、百分位和可核来源；本卡只把它视为元数据线索，不进入主题的期刊指标分。

### 公共水利情境

~~~water-context-json
{
  "water_object_type": "urban road network and critical-facility access under flood disruption",
  "basin_ids": [],
  "station_ids": [],
  "administrative_region_codes": [],
  "spatial_extent": "Harris County, Texas, United States",
  "spatial_support": "road intersections and road edges; census-tract overlay for social vulnerability",
  "spatial_resolution": "network node/edge; exact GIS resolution not_reported",
  "crs": "not_reported",
  "vertical_datum": "not_reported",
  "start_date": "2017-08-26 for the Harvey flooding chronology",
  "end_date": "not_reported; modeled disruption duration is 38 h",
  "temporal_resolution": "sensor state every 2 h; engineered road removals every 30 min",
  "aggregation_period": "38 h per disruption sequence",
  "water_year_definition": "not_applicable",
  "time_zone": "not_reported",
  "hydroclimate_regime": "not_reported",
  "regulated_status": "unknown",
  "major_human_interventions": [],
  "event_or_scenario": "2017 Hurricane Harvey sensor-informed engineered sequence and simulated 500-year flood sequences",
  "return_period": "500 years for the simulated floodplain scenario",
  "climate_scenario": "not_applicable",
  "baseline_period": "no-flood connected road network",
  "projection_period": "not_applicable",
  "variables": [
    {"name": "road-edge disruption state", "reported_unit": "binary intact/disrupted", "normalized_unit": "binary intact/disrupted", "conversion_rule": "not_applicable"},
    {"name": "robust-component size R_t", "reported_unit": "road-network nodes", "normalized_unit": "road-network nodes", "conversion_rule": "not_applicable"},
    {"name": "critical-facility access radius", "reported_unit": "mile", "normalized_unit": "mile", "conversion_rule": "not_applicable"},
    {"name": "early-warning time", "reported_unit": "h", "normalized_unit": "h", "conversion_rule": "not_applicable"}
  ]
}
~~~

未启用五类条件方法模块：本文的承重方法是道路网络渗流/可达性模拟，未直接执行水文水动力模型、机器学习预测、频率估计、遥感反演或具体水工程运行安全评价。把它硬套进这些模块会制造错误方法身份。

### 决定性声明

~~~claim-json
{
  "claim_id": "EC-20260907-001-C01",
  "source_id": "SRC-DOI-10.1016-J.RESS.2022.108555-VOR",
  "claim_type": "textual",
  "statement_role": "source_fact",
  "inference_type": "descriptive",
  "support_status": "supported",
  "statement": "论文把在每一扰动步仍能沿完整道路、且在预设出行半径内到达至少一个指定关键设施的道路节点集合定义为robust component，并用其规模R_t表示设施可达性。",
  "evidence_origin": "作者的方法定义与式(1)",
  "scope": {"object_or_denominator": "道路网络节点对医院、食品商店或药房的阈值可达性", "spatial": "方法定义；案例应用于Harris County", "temporal": "逐步道路失效状态", "comparator": "不使用最大连通子图；改用与设施相连且在距离阈值内的节点并集"},
  "numeric": null,
  "locator": {"material": "published PDF", "page_or_section": "PDF p.5, Section 3.1", "table_figure_clause_or_row": "Eq. (1) and adjacent text", "context": "hospital radius 5 miles; grocery and pharmacy radius 4 miles"},
  "directly_supports": "解释本文可达性结果到底测量了什么。",
  "does_not_support": "不证明居民实际选择该设施、道路通行时间、设施容量或服务质量。",
  "author_interpretation": "该指标比只看最大连通分量更能表达社区与关键设施之间的功能联系。",
  "analyst_judgment": "这是阈值化网络可达性，不应简写成现实服务可获得性。",
  "method_requirements": {"graph_direction": "undirected", "facility_types": ["hospital", "grocery", "pharmacy"], "access_rule": "at least one intact path within the preset radius"},
  "relations": {"supports": ["EC-20260907-001-C02"], "contradicts": [], "qualifies": ["EC-20260907-001-C06", "EC-20260907-001-C09"], "depends_on": [], "reproduces": [], "supersedes": []},
  "independence_group_ids": ["IG-GANGWAL-DONG-2022-HARRIS-FLOOD-ACCESS"],
  "verification_status": "partially_source_checked",
  "verified_by": "Codex AI-assisted PDF and indexed-text cross-check",
  "verified_at": "2026-09-07"
}
~~~

~~~claim-json
{
  "claim_id": "EC-20260907-001-C02",
  "source_id": "SRC-DOI-10.1016-J.RESS.2022.108555-VOR",
  "claim_type": "textual",
  "statement_role": "source_fact",
  "inference_type": "descriptive",
  "support_status": "supported",
  "statement": "预警点由log-log尺度R_t—t_i曲线的几何构造确定：连接首尾点后，取与该线平行且y轴截距最大的曲线点；目标是下降速率开始加快的位置，而不是绝对最陡点。",
  "evidence_origin": "作者的预警算法定义、式(2)和示意图",
  "scope": {"object_or_denominator": "每一条逐步道路失效序列对应的设施可达性曲线", "spatial": "网络方法；Harris County案例", "temporal": "按失效步序排列", "comparator": "预警点前后R_t下降形态"},
  "numeric": null,
  "locator": {"material": "published PDF", "page_or_section": "PDF pp.5-6, Section 3.2", "table_figure_clause_or_row": "Eq. (2), Fig. 1(b-c)", "context": "gradient-difference fluctuation is used as an internal check"},
  "directly_supports": "复述作者如何从模拟曲线得到预警点。",
  "does_not_support": "不证明该点具有统计校准的报警概率、提前量或业务误报/漏报性能。",
  "author_interpretation": "该点可作为快速可达性损失的早期指示。",
  "analyst_judgment": "属于基于曲线形态的事后/情景检测规则，不能自动称为实时预测模型。",
  "method_requirements": {"input": "ordered road-disruption sequence", "outcome": "robust-component curve", "internal_check": "increase of step-wise slope-difference fluctuation after the detected point"},
  "relations": {"supports": ["EC-20260907-001-C05", "EC-20260907-001-C07"], "contradicts": [], "qualifies": [], "depends_on": ["EC-20260907-001-C01", "EC-20260907-001-C12"], "reproduces": [], "supersedes": []},
  "independence_group_ids": ["IG-GANGWAL-DONG-2022-HARRIS-FLOOD-ACCESS"],
  "verification_status": "partially_source_checked",
  "verified_by": "Codex AI-assisted PDF and indexed-text cross-check",
  "verified_at": "2026-09-07"
}
~~~

~~~claim-json
{
  "claim_id": "EC-20260907-001-C03",
  "source_id": "SRC-DOI-10.1016-J.RESS.2022.108555-VOR",
  "claim_type": "numeric",
  "statement_role": "source_fact",
  "inference_type": "descriptive",
  "support_status": "unresolved",
  "statement": "正文第4.1节报告Harris County案例包含85家医院。",
  "evidence_origin": "作者实验设计正文",
  "scope": {"object_or_denominator": "案例中的医院设施数量", "spatial": "Harris County, Texas", "temporal": "论文案例数据版本；具体设施数据日期not_reported", "comparator": "图2图注报告98家医院"},
  "numeric": {"value": 85, "reported_unit": "hospitals", "normalized_value": 85, "normalized_unit": "hospitals", "conversion_rule": "not_applicable", "uncertainty": "conflict_pending"},
  "locator": {"material": "published PDF", "page_or_section": "PDF p.6, Section 4.1", "table_figure_clause_or_row": "Study site paragraph", "context": "same paragraph also reports 1,235 groceries and 1,070 pharmacies"},
  "directly_supports": "证明正文确实给出85这一数值。",
  "does_not_support": "在与图注冲突解决前，不能确定实际进入分析的医院数量就是85。",
  "author_interpretation": "not_applicable",
  "analyst_judgment": "与C04构成同一正式PDF内部冲突。",
  "method_requirements": {"conflict_id": "CONF-EC-20260907-001-01", "resolution_needed": "supplement, source data, correction record, or author clarification"},
  "relations": {"supports": [], "contradicts": ["EC-20260907-001-C04"], "qualifies": ["EC-20260907-001-C06", "EC-20260907-001-C08", "EC-20260907-001-C09"], "depends_on": [], "reproduces": [], "supersedes": []},
  "independence_group_ids": ["IG-GANGWAL-DONG-2022-HARRIS-FLOOD-ACCESS"],
  "verification_status": "partially_source_checked",
  "verified_by": "Codex AI-assisted PDF visual check",
  "verified_at": "2026-09-07"
}
~~~

~~~claim-json
{
  "claim_id": "EC-20260907-001-C04",
  "source_id": "SRC-DOI-10.1016-J.RESS.2022.108555-VOR",
  "claim_type": "numeric",
  "statement_role": "source_fact",
  "inference_type": "descriptive",
  "support_status": "unresolved",
  "statement": "图2图注报告Harris County案例包含98家医院。",
  "evidence_origin": "作者图2图注",
  "scope": {"object_or_denominator": "案例中的医院设施数量", "spatial": "Harris County, Texas", "temporal": "论文案例数据版本；具体设施数据日期not_reported", "comparator": "正文第4.1节报告85家医院"},
  "numeric": {"value": 98, "reported_unit": "hospitals", "normalized_value": 98, "normalized_unit": "hospitals", "conversion_rule": "not_applicable", "uncertainty": "conflict_pending"},
  "locator": {"material": "published PDF", "page_or_section": "PDF p.5", "table_figure_clause_or_row": "Fig. 2 caption", "context": "caption also reports 1,235 groceries and 1,070 pharmacies"},
  "directly_supports": "证明图注确实给出98这一数值。",
  "does_not_support": "在与正文冲突解决前，不能确定实际进入分析的医院数量就是98。",
  "author_interpretation": "not_applicable",
  "analyst_judgment": "与C03构成同一正式PDF内部冲突。",
  "method_requirements": {"conflict_id": "CONF-EC-20260907-001-01", "resolution_needed": "supplement, source data, correction record, or author clarification"},
  "relations": {"supports": [], "contradicts": ["EC-20260907-001-C03"], "qualifies": ["EC-20260907-001-C06", "EC-20260907-001-C08", "EC-20260907-001-C09"], "depends_on": [], "reproduces": [], "supersedes": []},
  "independence_group_ids": ["IG-GANGWAL-DONG-2022-HARRIS-FLOOD-ACCESS"],
  "verification_status": "partially_source_checked",
  "verified_by": "Codex AI-assisted PDF visual check",
  "verified_at": "2026-09-07"
}
~~~

~~~claim-json
{
  "claim_id": "EC-20260907-001-C05",
  "source_id": "SRC-DOI-10.1016-J.RESS.2022.108555-VOR",
  "claim_type": "numeric",
  "statement_role": "source_fact",
  "inference_type": "descriptive",
  "support_status": "supported",
  "statement": "在作者构造的Hurricane Harvey 38小时道路失效序列中，医院、食品商店和药房三条可达性曲线的预警点均为第20个失效时步，对应模拟开始后10小时。",
  "evidence_origin": "Harvey情景结果曲线及正文",
  "scope": {"object_or_denominator": "同一Harris County道路网络上的三类设施可达性曲线", "spatial": "Harris County, Texas", "temporal": "作者构造的38 h Harvey道路失效序列", "comparator": "预警点前后曲线下降速率"},
  "numeric": {"value": 10, "reported_unit": "h", "normalized_value": 10, "normalized_unit": "h", "conversion_rule": "20 steps × 0.5 h per step", "uncertainty": "no_interval_reported"},
  "locator": {"material": "published PDF", "page_or_section": "PDF p.7, Section 4.2", "table_figure_clause_or_row": "Fig. 4(a-c) and adjacent result paragraph", "context": "all three curves are reported at t20"},
  "directly_supports": "证明该预警算法在这一条作者构造的Harvey失效序列中给出的时步和时间。",
  "does_not_support": "不提供真实预警提前量、预测概率、误报率、漏报率或跨事件泛化性能。",
  "author_interpretation": "作者把该点视为灾害发生后、设施可达性开始快速下降之前的预警。",
  "analyst_judgment": "这是特定输入序列上的情景检测结果，时间值依赖道路失效排序和30分钟步长。",
  "method_requirements": {"sequence": "Harvey sensor-informed and rule-completed road-disruption sequence", "time_step": "30 min", "warning_algorithm": "maximum-intercept parallel-line construction in log-log space"},
  "relations": {"supports": [], "contradicts": [], "qualifies": [], "depends_on": ["EC-20260907-001-C02", "EC-20260907-001-C12"], "reproduces": [], "supersedes": []},
  "independence_group_ids": ["IG-GANGWAL-DONG-2022-HARRIS-FLOOD-ACCESS"],
  "verification_status": "partially_source_checked",
  "verified_by": "Codex AI-assisted PDF visual and indexed-text cross-check",
  "verified_at": "2026-09-07"
}
~~~

~~~claim-json
{
  "claim_id": "EC-20260907-001-C06",
  "source_id": "SRC-DOI-10.1016-J.RESS.2022.108555-VOR",
  "claim_type": "numeric",
  "statement_role": "source_fact",
  "inference_type": "descriptive",
  "support_status": "supported",
  "statement": "在Harvey情景的10小时预警点，仍可在作者设定的设施半径内到达至少一个设施的道路节点数，医院为115,764，食品商店为136,952，药房为135,787。",
  "evidence_origin": "Harvey情景预警点结果正文",
  "scope": {"object_or_denominator": "144,315个道路网络节点中满足阈值可达规则的节点数", "spatial": "Harris County, Texas", "temporal": "Harvey情景t20 = 10 h", "comparator": "三类设施；未报告该时点区间估计"},
  "numeric": {"value": [115764, 136952, 135787], "reported_unit": "road-network nodes [hospital, grocery, pharmacy]", "normalized_value": [115764, 136952, 135787], "normalized_unit": "road-network nodes [hospital, grocery, pharmacy]", "conversion_rule": "not_applicable", "uncertainty": "no_interval_reported"},
  "locator": {"material": "published PDF", "page_or_section": "PDF p.7, Section 4.2", "table_figure_clause_or_row": "paragraph following Fig. 4", "context": "values reported at the common early-warning time"},
  "directly_supports": "量化特定情景、特定阈值下预警点的网络节点可达规模。",
  "does_not_support": "不等于可获得服务的人口数、成功就医/购物人数、设施容量或行程时间。",
  "author_interpretation": "三类设施在预警点仍覆盖较大数量的道路节点。",
  "analyst_judgment": "应保留‘道路节点数’分母和5/4 miles阈值，不能改写成人口覆盖率。",
  "method_requirements": {"hospital_radius": "5 miles", "grocery_radius": "4 miles", "pharmacy_radius": "4 miles", "network_nodes": 144315},
  "relations": {"supports": [], "contradicts": [], "qualifies": [], "depends_on": ["EC-20260907-001-C01", "EC-20260907-001-C03", "EC-20260907-001-C04", "EC-20260907-001-C05"], "reproduces": [], "supersedes": []},
  "independence_group_ids": ["IG-GANGWAL-DONG-2022-HARRIS-FLOOD-ACCESS"],
  "verification_status": "partially_source_checked",
  "verified_by": "Codex AI-assisted PDF visual and indexed-text cross-check",
  "verified_at": "2026-09-07"
}
~~~

~~~claim-json
{
  "claim_id": "EC-20260907-001-C07",
  "source_id": "SRC-DOI-10.1016-J.RESS.2022.108555-VOR",
  "claim_type": "numeric",
  "statement_role": "source_fact",
  "inference_type": "descriptive",
  "support_status": "supported",
  "statement": "在500年一遇静态洪泛区情景中，作者对随机初始失效位置和道路失效顺序运行1000次Monte Carlo模拟；所得预警点分布为一个时段范围，而不是单一固定时刻。",
  "evidence_origin": "500年一遇情景设计与结果",
  "scope": {"object_or_denominator": "同一静态洪泛区、同一道路和设施数据上的1000条构造失效序列", "spatial": "Harris County, Texas", "temporal": "每条序列均被设定为38 h", "comparator": "不同随机起点和道路失效顺序"},
  "numeric": {"value": 1000, "reported_unit": "Monte Carlo simulation sequences", "normalized_value": 1000, "normalized_unit": "Monte Carlo simulation sequences", "conversion_rule": "not_applicable", "uncertainty": "simulation-distribution shown; exact interval endpoints not transcribed in this card"},
  "locator": {"material": "published PDF", "page_or_section": "PDF pp.6-8, Sections 4.1-4.2", "table_figure_clause_or_row": "scenario description and Fig. 5", "context": "random initial road failure and sequence variation"},
  "directly_supports": "说明预警点对作者设定的随机失效序列存在变异，并记录模拟次数。",
  "does_not_support": "1000次运行不是1000次独立洪水事件，也不能提供跨城市经验置信区间。",
  "author_interpretation": "500年一遇情景下早期预警表现为一个预警区域。",
  "analyst_judgment": "这些重复运行估计的是模型内序列不确定性，证据独立性仍为一个研究组。",
  "method_requirements": {"flood_map": "static 500-year floodplain", "failed_edges": 58956, "modeled_duration": "38 h", "randomization": "initial failed edge and subsequent sequence"},
  "relations": {"supports": ["EC-20260907-001-C08"], "contradicts": [], "qualifies": ["EC-20260907-001-C05"], "depends_on": ["EC-20260907-001-C02", "EC-20260907-001-C12"], "reproduces": [], "supersedes": []},
  "independence_group_ids": ["IG-GANGWAL-DONG-2022-HARRIS-FLOOD-ACCESS"],
  "verification_status": "partially_source_checked",
  "verified_by": "Codex AI-assisted PDF visual and indexed-text cross-check",
  "verified_at": "2026-09-07"
}
~~~

~~~claim-json
{
  "claim_id": "EC-20260907-001-C08",
  "source_id": "SRC-DOI-10.1016-J.RESS.2022.108555-VOR",
  "claim_type": "comparative",
  "statement_role": "author_interpretation",
  "inference_type": "comparative",
  "support_status": "partially_supported",
  "statement": "在500年一遇模拟结果中，医院的预警时点分布相对更晚且更宽，医院可达性曲线AUC也低于食品商店和药房；作者把这一差异与医院数量更少、空间分布更稀疏联系起来。",
  "evidence_origin": "设施类型比较结果与作者讨论",
  "scope": {"object_or_denominator": "三类设施在同一500年一遇模拟框架下的预警时点分布和AUC", "spatial": "Harris County, Texas", "temporal": "1000条、每条38 h的模拟序列", "comparator": "hospital versus grocery and pharmacy"},
  "numeric": null,
  "locator": {"material": "published PDF", "page_or_section": "PDF pp.8-9, Section 4.2", "table_figure_clause_or_row": "Figs. 5-6 and adjacent discussion", "context": "facility number and spatial distribution are offered as explanation"},
  "directly_supports": "支持该模型和案例内三类设施输出的相对差异以及作者给出的解释。",
  "does_not_support": "未做因果识别或正式中介检验，不能证明设施数量或稀疏性导致了该差异。",
  "author_interpretation": "医院更少且更分散，使其可达性更易受道路失效影响。",
  "analyst_judgment": "可作为待检验机制假设，不能升级为已证实因果机制；医院数量冲突还会影响解释可信度。",
  "method_requirements": {"comparison_basis": "same network model and simulated sequences", "causal_test": "not_reported", "facility_count_conflict": "CONF-EC-20260907-001-01"},
  "relations": {"supports": [], "contradicts": [], "qualifies": [], "depends_on": ["EC-20260907-001-C03", "EC-20260907-001-C04", "EC-20260907-001-C07", "EC-20260907-001-C13"], "reproduces": [], "supersedes": []},
  "independence_group_ids": ["IG-GANGWAL-DONG-2022-HARRIS-FLOOD-ACCESS"],
  "verification_status": "partially_source_checked",
  "verified_by": "Codex AI-assisted PDF visual and indexed-text cross-check",
  "verified_at": "2026-09-07"
}
~~~

~~~claim-json
{
  "claim_id": "EC-20260907-001-C09",
  "source_id": "SRC-DOI-10.1016-J.RESS.2022.108555-VOR",
  "claim_type": "numeric",
  "statement_role": "source_fact",
  "inference_type": "comparative",
  "support_status": "partially_supported",
  "statement": "按5 miles医院可达阈值，至少可达一家医院的节点数由无洪水基线的120,874降至Harvey情景的83,613，并在500年一遇情景降至55,127；作者分别报告相对基线下降30.83%和54.39%。",
  "evidence_origin": "医院可达冗余结果",
  "scope": {"object_or_denominator": "144,315个道路网络节点；指标为5 miles内至少可达一家医院", "spatial": "Harris County, Texas", "temporal": "无洪水基线、Harvey道路失效终态、500年一遇情景终态", "comparator": "two flood scenarios versus no-flood network"},
  "numeric": {"value": [120874, 83613, 55127, 30.83, 54.39], "reported_unit": "nodes [baseline, Harvey, 500-year] and percent decrease [Harvey, 500-year]", "normalized_value": [120874, 83613, 55127, 30.83, 54.39], "normalized_unit": "nodes and percent", "conversion_rule": "percent decreases reported by authors; not independently recomputed for verification", "uncertainty": "no_interval_reported"},
  "locator": {"material": "published PDF", "page_or_section": "PDF pp.10-11, Section 4.4", "table_figure_clause_or_row": "Fig. 8 and adjacent text", "context": "hospital-access redundancy maps"},
  "directly_supports": "量化作者模型中医院阈值可达节点在两个洪水情景下的减少。",
  "does_not_support": "不表示人口、患者、医疗需求、设施容量、拥堵、救护车响应或实际就医成功率的同幅下降。",
  "author_interpretation": "更强洪水情景造成更广泛的医院可达冗余损失。",
  "analyst_judgment": "可用于定义网络可达性暴露指标，但迁移到现实服务公平性前必须引入人口和服务能力数据。",
  "method_requirements": {"access_radius": "5 miles", "measure": "number of nodes with at least one reachable hospital", "facility_count_conflict": "CONF-EC-20260907-001-01"},
  "relations": {"supports": ["EC-20260907-001-C11"], "contradicts": [], "qualifies": [], "depends_on": ["EC-20260907-001-C01", "EC-20260907-001-C03", "EC-20260907-001-C04", "EC-20260907-001-C12"], "reproduces": [], "supersedes": []},
  "independence_group_ids": ["IG-GANGWAL-DONG-2022-HARRIS-FLOOD-ACCESS"],
  "verification_status": "partially_source_checked",
  "verified_by": "Codex AI-assisted PDF visual and indexed-text cross-check",
  "verified_at": "2026-09-07"
}
~~~

~~~claim-json
{
  "claim_id": "EC-20260907-001-C10",
  "source_id": "SRC-DOI-10.1016-J.RESS.2022.108555-VOR",
  "claim_type": "numeric",
  "statement_role": "source_fact",
  "inference_type": "descriptive",
  "support_status": "partially_supported",
  "statement": "在500年一遇情景的1000条模拟序列中，被标为预警点对应关键道路的单条道路最大出现频次，医院、食品商店和药房分别为307、359和399；图示频次经Min-Max归一化。",
  "evidence_origin": "关键道路出现频次和空间分布结果",
  "scope": {"object_or_denominator": "每类设施1000条模拟序列中预警点对应的道路边", "spatial": "Harris County 500-year floodplain affected roads", "temporal": "1000条构造失效序列", "comparator": "hospital, grocery, pharmacy"},
  "numeric": {"value": [307, 359, 399], "reported_unit": "occurrences out of 1000 simulations [hospital, grocery, pharmacy]", "normalized_value": [0.307, 0.359, 0.399], "normalized_unit": "proportion of simulations", "conversion_rule": "occurrence count divided by 1000; map colors use author Min-Max normalization", "uncertainty": "simulation frequency; no sampling interval reported"},
  "locator": {"material": "published PDF", "page_or_section": "PDF pp.9-10, Section 4.3", "table_figure_clause_or_row": "Fig. 7 and adjacent text", "context": "maximum occurrence frequencies and Min-Max visualization"},
  "directly_supports": "识别模型内对预警点定位较敏感、在不同模拟序列中反复出现的道路候选。",
  "does_not_support": "没有干预对照或实地保护实验，不能证明加固这些道路会延迟失效、提高韧性或产生相应效益。",
  "author_interpretation": "高频道路可作为提升关键设施可达性的重点基础设施。",
  "analyst_judgment": "应称为模型筛选出的候选关键道路；工程优先级仍需流量、替代路线、造价和干预效果验证。",
  "method_requirements": {"simulation_runs": 1000, "selection_event": "road edge at detected early-warning point", "map_scaling": "Min-Max normalization by facility type"},
  "relations": {"supports": [], "contradicts": [], "qualifies": [], "depends_on": ["EC-20260907-001-C02", "EC-20260907-001-C07", "EC-20260907-001-C12"], "reproduces": [], "supersedes": []},
  "independence_group_ids": ["IG-GANGWAL-DONG-2022-HARRIS-FLOOD-ACCESS"],
  "verification_status": "partially_source_checked",
  "verified_by": "Codex AI-assisted PDF visual and indexed-text cross-check",
  "verified_at": "2026-09-07"
}
~~~

~~~claim-json
{
  "claim_id": "EC-20260907-001-C11",
  "source_id": "SRC-DOI-10.1016-J.RESS.2022.108555-VOR",
  "claim_type": "textual",
  "statement_role": "source_fact",
  "inference_type": "association",
  "support_status": "partially_supported",
  "statement": "论文把人口普查区社会脆弱性指数与洪水后无法在5 miles内到达任何医院的道路节点进行空间叠置，用于显示可达冗余不足与社会脆弱性可能共同出现的区域。",
  "evidence_origin": "社会脆弱性和医院可达冗余叠置分析",
  "scope": {"object_or_denominator": "census-tract SVI and road nodes with zero reachable hospitals", "spatial": "Harris County, Texas", "temporal": "Harvey and 500-year scenario end states", "comparator": "spatial coincidence across mapped areas"},
  "numeric": null,
  "locator": {"material": "published PDF", "page_or_section": "PDF pp.10-11, Section 4.4", "table_figure_clause_or_row": "Fig. 9 and adjacent text", "context": "SVI is overlaid with zero-hospital-access nodes"},
  "directly_supports": "支持把模型可达性损失与社会脆弱性作为空间联合筛查层。",
  "does_not_support": "未估计统计关联强度或因果效应，也未测量居民实际医疗利用和健康结果。",
  "author_interpretation": "叠置结果可帮助识别洪水中需要重点关注的高脆弱性、低冗余区域。",
  "analyst_judgment": "适合生成公平性筛查假设，不能表述为社会脆弱性导致可达性失败或已证实健康不平等。",
  "method_requirements": {"social_layer": "census-tract Social Vulnerability Index", "access_layer": "road nodes with zero hospitals within 5 miles", "statistical_test": "not_reported"},
  "relations": {"supports": [], "contradicts": [], "qualifies": ["EC-20260907-001-C09"], "depends_on": ["EC-20260907-001-C09", "EC-20260907-001-C12"], "reproduces": [], "supersedes": []},
  "independence_group_ids": ["IG-GANGWAL-DONG-2022-HARRIS-FLOOD-ACCESS"],
  "verification_status": "partially_source_checked",
  "verified_by": "Codex AI-assisted PDF visual and indexed-text cross-check",
  "verified_at": "2026-09-07"
}
~~~

~~~claim-json
{
  "claim_id": "EC-20260907-001-C12",
  "source_id": "SRC-DOI-10.1016-J.RESS.2022.108555-VOR",
  "claim_type": "textual",
  "statement_role": "source_fact",
  "inference_type": "descriptive",
  "support_status": "supported",
  "statement": "Harvey道路失效序列只部分来自监测站状态，并由低程、相邻传播和每个分水区每30分钟移除10条低洼道路的规则补全；500年一遇情景基于静态洪泛区构造；两类情景均把道路表示为完整或失效的二元状态。",
  "evidence_origin": "实验设计、情景构造和作者限制说明",
  "scope": {"object_or_denominator": "进入道路网络可达性计算的道路失效时序", "spatial": "Harris County, Texas", "temporal": "Harvey 38 h and simulated 500-year 38 h sequences", "comparator": "sensor-informed engineered Harvey sequence versus static-map simulation"},
  "numeric": null,
  "locator": {"material": "published PDF", "page_or_section": "PDF pp.6, 11-12, Sections 4.1 and 5-6", "table_figure_clause_or_row": "scenario-generation paragraphs and limitations", "context": "traffic flow and partial failure are not modeled"},
  "directly_supports": "界定研究结果依赖的失效输入、时间构造和道路状态简化。",
  "does_not_support": "不能把模拟时序当作逐路段实测水深或经过水动力模型校准的真实传播过程。",
  "author_interpretation": "这些设定支持在数据有限时展示网络可达性方法，同时构成后续改进方向。",
  "analyst_judgment": "这是所有数值结果的承重边界；任何跨区域或实时预警应用必须重新建立洪水—道路失效映射。",
  "method_requirements": {"Harvey_sensors": "187 installed, 128 showing inundation", "Harvey_failed_edges": 28143, "rule_completion": "10 low-lying roads per watershed per 30 min", "flood500_failed_edges": 58956, "road_state": "binary"},
  "relations": {"supports": [], "contradicts": [], "qualifies": ["EC-20260907-001-C05", "EC-20260907-001-C06", "EC-20260907-001-C07", "EC-20260907-001-C08", "EC-20260907-001-C09", "EC-20260907-001-C10", "EC-20260907-001-C11"], "depends_on": [], "reproduces": [], "supersedes": []},
  "independence_group_ids": ["IG-GANGWAL-DONG-2022-HARRIS-FLOOD-ACCESS"],
  "verification_status": "partially_source_checked",
  "verified_by": "Codex AI-assisted PDF visual and indexed-text cross-check",
  "verified_at": "2026-09-07"
}
~~~

~~~claim-json
{
  "claim_id": "EC-20260907-001-C13",
  "source_id": "SRC-DOI-10.1016-J.RESS.2022.108555-VOR",
  "claim_type": "textual",
  "statement_role": "source_fact",
  "inference_type": "descriptive",
  "support_status": "supported",
  "statement": "论文区分预警时点与整体网络韧性：预警时点表示可达性开始快速下降的位置，AUC表示整条可达性曲线下的整体表现；作者指出二者没有强相关关系。",
  "evidence_origin": "结果解释与讨论",
  "scope": {"object_or_denominator": "三类设施的预警时点和可达性曲线AUC", "spatial": "Harris County案例", "temporal": "Harvey and 500-year disruption sequences", "comparator": "early-warning timing versus AUC-based robustness"},
  "numeric": null,
  "locator": {"material": "published PDF", "page_or_section": "PDF pp.8-9 and 11-12, Sections 4.2 and 5-6", "table_figure_clause_or_row": "Figs. 5-6 and discussion/conclusion", "context": "no detailed correlation statistic is reported in the main text"},
  "directly_supports": "防止把较早或较晚的预警点直接等同于较高或较低的整体韧性。",
  "does_not_support": "主文未给出相关系数、置信区间或假设检验，因此不能量化‘不强相关’的大小或不确定性。",
  "author_interpretation": "预警信息和韧性信息回答不同问题，应同时考虑。",
  "analyst_judgment": "主题综合时必须将‘变化点检测性能’与‘系统整体韧性’拆成不同结果域。",
  "method_requirements": {"warning_metric": "curve-shape change point", "resilience_metric": "area under accessibility curve", "reported_correlation_statistic": "not_reported"},
  "relations": {"supports": [], "contradicts": [], "qualifies": ["EC-20260907-001-C05", "EC-20260907-001-C08"], "depends_on": ["EC-20260907-001-C01", "EC-20260907-001-C02"], "reproduces": [], "supersedes": []},
  "independence_group_ids": ["IG-GANGWAL-DONG-2022-HARRIS-FLOOD-ACCESS"],
  "verification_status": "partially_source_checked",
  "verified_by": "Codex AI-assisted PDF visual and indexed-text cross-check",
  "verified_at": "2026-09-07"
}
~~~

~~~claim-json
{
  "claim_id": "EC-20260907-001-C14",
  "source_id": "SRC-DOI-10.1016-J.RESS.2022.108555-VOR",
  "claim_type": "comparative",
  "statement_role": "source_fact",
  "inference_type": "comparative",
  "support_status": "partially_supported",
  "statement": "出行半径敏感性分析显示，食品商店和药房的可达节点规模约在3 miles后趋于平台，而医院在更大半径下仍继续增加；论文据此为案例采用医院5 miles、商店和药房4 miles，但没有用本地实际出行行为校准这些阈值。",
  "evidence_origin": "访问半径敏感性分析和方法说明",
  "scope": {"object_or_denominator": "无洪水道路网络中不同设施半径对应的可达节点规模", "spatial": "Harris County, Texas", "temporal": "baseline network", "comparator": "facility types across tested radii up to 12 miles"},
  "numeric": null,
  "locator": {"material": "published PDF", "page_or_section": "PDF p.6, Section 4.1", "table_figure_clause_or_row": "Fig. 3 and adjacent text", "context": "tested distance thresholds and selected radii"},
  "directly_supports": "证明设施类型和访问半径会改变robust-component规模，并说明案例阈值的图形依据。",
  "does_not_support": "不证明5/4 miles是Harris County居民、应急车辆或其他城市的真实可接受出行阈值。",
  "author_interpretation": "不同设施密度和分布需要不同访问距离。",
  "analyst_judgment": "迁移研究必须把半径作为情景参数或使用出行时间/行为数据校准，不能原样套用。",
  "method_requirements": {"tested_radius_max": "12 miles", "selected_hospital_radius": "5 miles", "selected_grocery_radius": "4 miles", "selected_pharmacy_radius": "4 miles", "local_behavior_calibration": "not_reported"},
  "relations": {"supports": [], "contradicts": [], "qualifies": ["EC-20260907-001-C01", "EC-20260907-001-C06", "EC-20260907-001-C09"], "depends_on": [], "reproduces": [], "supersedes": []},
  "independence_group_ids": ["IG-GANGWAL-DONG-2022-HARRIS-FLOOD-ACCESS"],
  "verification_status": "partially_source_checked",
  "verified_by": "Codex AI-assisted PDF visual and indexed-text cross-check",
  "verified_at": "2026-09-07"
}
~~~

## 冲突、缺失与审计风险

| 冲突ID | 冲突字段 | 来源内证据A | 来源内证据B | 当前处理 | 解除条件 |
|---|---|---|---|---|---|
| `CONF-EC-20260907-001-01` | 医院数量 | 第4.1节正文：85家 | 图2图注：98家 | 原样保留两值；C03、C04均为`unresolved`；所有依赖设施数量的解释受限定 | 查阅补充材料/底层设施数据/勘误，或取得作者澄清，并由本人复核记录 |

- 主文没有给出单独的数据与代码可用性声明；本轮也未取得在线补充材料，因此不得宣称数据或代码开放。
- Harvey序列含真实监测站信息，但逐道路时序经过规则补全；“真实事件案例”不能缩写成“完全实测验证”。
- 500年一遇的1000次运行共享同一城市、网络、静态洪泛区与模型假设，只能算一个依赖证据组。
- 论文没有业务预警的概率校准、误报/漏报、外部城市验证、交通流、道路部分失效、设施容量或实际居民行为结果。

## 三层判断分离

### 来源直接给出的事实

本文给出了可达性指标、预警点算法、两种情景构造、特定半径下的网络节点结果、AUC比较、关键道路出现频次及SVI空间叠置。它证明的是一个案例网络模拟中这些量如何产生和变化。

### 作者的解释

作者认为预警点可在快速可达性损失前提供警示，高频关键道路可帮助优先配置基础设施资源，医院较少且更分散可能解释其较低韧性和不同预警分布，SVI叠置可定位需要关注的社区。

### 本平台的条件性判断

本文对“城市洪涝—道路网络—关键设施阈值可达性”方法链具有较高直接相关性，可贡献指标、算法和可复核案例数值。其证据仍停留在单城市模拟和内部一致性层级。研究机会可围绕洪水—道路动态耦合、概率校准、行为/容量约束和跨事件验证提出，但不能把这些缺口写成本文已经解决的结论，也不能在医院数量冲突和人工复核完成前让本卡承载正式主题。

## 对后续工作的四维支持

| 维度 | 本卡能支持什么 | 不能支持什么 | 下一步需要的证据 |
|---|---|---|---|
| 概念 | 严格区分设施阈值可达性、变化点式预警和AUC韧性 | 不能把网络节点可达等同人口服务可得或健康结果 | 设施容量、人口/需求、出行行为与服务利用研究 |
| 方法 | 提供道路逐步失效→可达曲线→预警点→关键道路/冗余图的可实现链路 | 不能证明算法已具实时业务预测性能 | 动态水动力/积水观测耦合、时间外验证、误报漏报和校准实验 |
| 比较 | 在同一网络和假设下比较Harvey/500年一遇及三类设施 | 不能跨城市、跨设施制度直接推广 | 多城市、多事件、不同道路与设施数据口径的独立重复研究 |
| 决策 | 形成候选关键道路与高脆弱性低冗余区域的筛查层 | 不能直接决定工程投资或声称干预有效 | 工程可行性、成本、交通流、替代路线和干预前后效果证据 |

## 人工复核清单

本人在将任何声明升级为`source_checked`前，应在Zotero正式PDF逐项完成并签名：

- [ ] 对照第3.1节式(1)及相邻文字，确认`R_t`、道路完整性和距离阈值含义（C01）。
- [ ] 对照第3.2节式(2)和图1，确认预警点几何算法及其并非最陡点（C02）。
- [ ] 对照图2图注与第4.1节正文，确认85/98医院冲突确实存在；记录补充材料、勘误或底层数据检查结果（C03—C04）。
- [ ] 对照图4及相邻段落，确认`t20 = 10 h`和三类设施节点数（C05—C06）。
- [ ] 对照情景构造段、图5—图6，确认1000次运行的随机化对象、预警区域和AUC比较（C07—C08、C13）。
- [ ] 对照图7，确认307/359/399的分母、频次含义和Min-Max仅用于图示（C10）。
- [ ] 对照图8—图9，确认医院节点数、百分比和SVI叠置含义（C09、C11）。
- [ ] 对照第4.1节及讨论/结论，确认Harvey规则补全、静态洪泛区、二元道路和交通流限制（C12）。
- [ ] 对照图3，确认访问半径测试范围、平台形态和5/4 miles选择（C14）。
- [ ] 检查在线补充材料、数据/代码入口与论文勘误；若未取得，保持`not_obtained/not_found_after_check`。
- [ ] 将逐条确认的声明ID写入`verified_claim_ids`，填写本人姓名与日期；未逐条查看的声明不得批量勾选。

## L3 动态精读资格门

- 决策门（精读会改变当前主题/机会/方法选择）：`false`。当前没有已批准正式主题或研究机会需要本卡改变。
- 缺口门（存在已界定且只能由更深材料解决的关键缺口）：`false`。85/98冲突值得核查，但先做人工主文复核与补充材料/勘误查询，不足以单独强行开启全量精读。
- 变更门（已有新结果会改变既有证据判断）：`false`。本卡为首篇实验卡，没有既有正式判断被新结果取代。

结论：当前停在AI辅助L2草稿。下一步是人工逐条复核和处理`CONF-EC-20260907-001-01`；三门未同时满足，不建立`DR-`，不从单卡生成正式主题或Idea。
