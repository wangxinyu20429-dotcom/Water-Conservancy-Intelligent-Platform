---
card_schema: "evidence-card-v1.2"
card_id: "{{CARD_ID}}"
card_version: "1.2.0"
card_type: "source_evidence"
artifact_type: "{{ARTIFACT_TYPE}}"
evidence_roles: {{EVIDENCE_ROLES}}
workflow_status: "{{WORKFLOW_STATUS}}"
completion_level: "{{COMPLETION_LEVEL}}"
source_work_id: "{{SOURCE_WORK_ID}}"
source_manifestation_id: "{{SOURCE_MANIFESTATION_ID}}"
source_version: "{{SOURCE_VERSION}}"
source_snapshot_hash: "{{SOURCE_SNAPSHOT_HASH}}"
source_provenance: "{{SOURCE_PROVENANCE}}"
acquired_via: "{{ACQUIRED_VIA}}"
acquired_at: "{{ACQUIRED_AT}}"
validity_checked_at: "{{VALIDITY_CHECKED_AT}}"
language: "{{LANGUAGE}}"
access_level: "{{ACCESS_LEVEL}}"
zotero_item_key: "{{ZOTERO_ITEM_KEY}}"
project_ids: {{PROJECT_IDS}}
research_question_ids: {{RESEARCH_QUESTION_IDS}}
decision_ids: {{DECISION_IDS}}
related_card_ids: []
independence_group_ids: []
version_family_ids: []
reading_scope: "{{READING_SCOPE}}"
extraction_method: "{{EXTRACTION_METHOD}}"
generator_or_pipeline_version: "{{GENERATOR_VERSION}}"
verified_claim_ids: []
verified_by: ""
verified_at: ""
human_review_status: "not_started"
human_reviewer: ""
funding: []
commissioning_party: []
declared_conflicts: []
review_independence: "unknown"
confidentiality: "{{CONFIDENTIALITY}}"
water_context_status: "{{WATER_CONTEXT_STATUS}}"
method_modules: {{METHOD_MODULES}}
l3_gate_decision: false
l3_gate_gap: false
l3_gate_change: false
relevance: "{{RELEVANCE}}"
verification_readiness: "{{VERIFICATION_READINESS}}"
applicability: "{{APPLICABILITY}}"
decision_effect: "no_change"
load_bearing_conflict: false
unresolved_conflict_ids: []
recheck_trigger: "{{RECHECK_TRIGGER}}"
---

# {{CARD_ID}} {{TITLE}}

> 本文件是一个来源版本的唯一证据记录。来源身份只在这里维护；声明用全局 claim_id 连接多个研究问题和决策。机器校验通过只表示结构规则满足，不表示科学结论已经人工确认。

## L0 来源登记

- 题名：{{TITLE}}
- 作者／责任机构：{{CREATORS}}
- 年份／发布日期：{{DATE}}
- 来源／出版者／仓库：{{VENUE}}
- DOI／ISBN／标准号／数据或软件标识符：{{IDENTIFIER}}
- 正式入口：{{SOURCE_URL}}
- 当前取得材料：
- 未取得材料及 missing_status：
- 同一作品、版本家族和独立性组说明：

允许的 missing_status 只有：not_applicable、not_obtained、not_read、not_reported、not_found_after_check、conflict_pending。
