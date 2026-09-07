#!/usr/bin/env python3
"""Meaningful invariant tests for evidence-card hard rules R01-R08."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
from validate_card import validate_text  # noqa: E402


def frontmatter(**overrides: object) -> str:
    data: dict[str, object] = {
        "card_schema": "evidence-card-v1.2", "card_id": "EC-TEST-001", "card_version": "1.2.0",
        "card_type": "source_evidence", "artifact_type": "journal_article", "evidence_roles": ["original_research"],
        "workflow_status": "source_checked", "completion_level": "L2", "source_work_id": "WORK-1",
        "source_manifestation_id": "SRC-1", "source_version": "v1", "source_snapshot_hash": "sha256:test",
        "source_provenance": "publisher", "acquired_via": "zotero_local_api", "acquired_at": "2026-09-04",
        "validity_checked_at": "2026-09-04", "language": "en", "access_level": "internal", "zotero_item_key": "ABCD1234",
        "project_ids": ["P1"], "research_question_ids": ["RQ1"], "decision_ids": [], "related_card_ids": [],
        "independence_group_ids": ["DATA-1"], "version_family_ids": ["VER-1"], "reading_scope": "full_text",
        "extraction_method": "human", "generator_or_pipeline_version": "", "verified_claim_ids": ["EC-TEST-001-C01"],
        "verified_by": "tester", "verified_at": "2026-09-04", "human_review_status": "completed", "human_reviewer": "tester",
        "funding": [], "commissioning_party": [], "declared_conflicts": [], "review_independence": "independent",
        "confidentiality": "internal", "water_context_status": "not_applicable", "method_modules": [],
        "l3_gate_decision": False, "l3_gate_gap": False, "l3_gate_change": False, "relevance": "central",
        "verification_readiness": "verified", "applicability": "conditional", "decision_effect": "strengthens",
        "load_bearing_conflict": False, "unresolved_conflict_ids": [], "recheck_trigger": "new version",
    }
    data.update(overrides)
    lines = ["---"]
    for key, value in data.items():
        lines.append(f"{key}: {json.dumps(value, ensure_ascii=False)}")
    lines.extend(["---", "", "# Test"])
    return "\n".join(lines)


def valid_claim() -> dict[str, object]:
    return {
        "claim_id": "EC-TEST-001-C01", "source_id": "SRC-1", "claim_type": "numeric",
        "statement_role": "source_fact", "inference_type": "comparative", "support_status": "supported",
        "statement": "The reported value differs between the stated conditions.", "evidence_origin": "reported analysis",
        "scope": {"object_or_denominator": "10 stations", "spatial": "Basin A", "temporal": "2001-2020", "comparator": "method B"},
        "numeric": {"value": 0.12, "reported_unit": "m3/s", "uncertainty": "95% CI 0.10-0.14"},
        "locator": {"material": "main text", "page_or_section": "p. 8", "table_figure_clause_or_row": "Table 2", "context": "row 3"},
        "directly_supports": "the bounded comparison", "does_not_support": "causality or other basins",
        "author_interpretation": "improved estimate", "analyst_judgment": "conditional use", "method_requirements": {},
        "relations": {"supports": [], "contradicts": [], "qualifies": [], "depends_on": [], "reproduces": [], "supersedes": []},
        "independence_group_ids": ["DATA-1"], "verification_status": "source_checked", "verified_by": "tester", "verified_at": "2026-09-04",
    }


def source_text(claim: dict[str, object], **meta: object) -> str:
    return frontmatter(**meta) + "\n\n~~~claim-json\n" + json.dumps(claim, ensure_ascii=False, indent=2) + "\n~~~\n"


def expect(name: str, text: str, expected_code: str | None) -> None:
    errors, _, _ = validate_text(text, "final")
    joined = "\n".join(errors)
    if expected_code is None and errors:
        raise AssertionError(f"{name}: expected PASS, got {joined}")
    if expected_code is not None and expected_code not in joined:
        raise AssertionError(f"{name}: expected {expected_code}, got {joined}")
    print(f"PASS {name}")


def main() -> None:
    claim = valid_claim()
    expect("valid L2 source", source_text(claim), None)

    expect("R01 L1 direct use blocked", source_text(claim, completion_level="L1", reading_scope="abstract", verification_readiness="verified", applicability="direct"), "R01")

    no_unit = copy.deepcopy(claim)
    no_unit["numeric"]["reported_unit"] = ""  # type: ignore[index]
    expect("R02 numeric completeness", source_text(no_unit), "R02")

    prediction = copy.deepcopy(claim)
    prediction["claim_type"] = "textual"
    prediction["numeric"] = None
    prediction["inference_type"] = "prediction"
    prediction["method_requirements"] = {"issue_time": "08:00"}
    expect("R04 prediction controls", source_text(prediction), "R04")

    expect("R06 dynamic source version bundle", source_text(claim, artifact_type="dataset", source_snapshot_hash="", validity_checked_at="", recheck_trigger=""), "R06")

    expect("R07 conflict blocks approval", source_text(claim, workflow_status="approved", load_bearing_conflict=True, unresolved_conflict_ids=["CONFLICT-1"]), "R07")

    expect("R08 AI provenance", source_text(claim, extraction_method="ai_assisted", generator_or_pipeline_version="", source_snapshot_hash="", human_review_status="not_started", human_reviewer="", verified_claim_ids=[]), "R08")

    decision = {
        "decision_id": "DEC-1", "research_question_ids": ["RQ1"], "included_claims": ["EC-TEST-001-C01"], "excluded_claims": [],
        "exclusion_reasons": {}, "independence_groups": {"DATA-1": ["EC-TEST-001-C01"]}, "version_families": {}, "agreements": [],
        "conflicts": [], "unresolved_conflicts": [], "coverage": {}, "transferability": {},
        "evidence_profile": {k: {"level": "medium", "basis_claim_ids": ["EC-TEST-001-C01"]} for k in ["directness", "internal_validity", "independence", "precision", "applicability", "reproducibility"]},
        "current_conclusion": "conditional", "supported": "bounded claim", "unsupported": "generalization", "decision_effect": "limits",
        "remaining_evidence_gap": "external validation", "next_update_trigger": "new independent study",
    }
    decision_meta = "\n".join([
        "---", 'card_schema: "evidence-card-v1.2"', 'card_id: "DS-1"', 'card_version: "1.2.0"', 'card_type: "decision_synthesis"',
        'workflow_status: "approved"', 'completion_level: "L2"', 'decision_id: "DEC-1"', 'research_question_ids: ["RQ1"]',
        'as_of_date: "2026-09-04"', 'decision_owner: "tester"', 'load_bearing_conflict: false', 'unresolved_conflict_ids: []',
        'included_claim_ids: ["EC-TEST-001-C01"]', 'excluded_claim_ids: []', 'independence_group_ids: ["DATA-1"]', 'version_family_ids: []',
        "---", "", "# Decision", "", "~~~decision-json", json.dumps(decision, ensure_ascii=False, indent=2), "~~~",
    ])
    expect("valid decision synthesis", decision_meta, None)
    errors, _, _ = validate_text(decision_meta, "final", {
        "EC-TEST-001-C01": {"completion_level": "L1", "verification_status": "not_checked"}
    })
    if "R01" not in "\n".join(errors):
        raise AssertionError("decision inclusion gate: expected R01 for an L1 unverified claim")
    print("PASS decision inclusion gate")
    print("ALL TESTS PASSED")


if __name__ == "__main__":
    main()
