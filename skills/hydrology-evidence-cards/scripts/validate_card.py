#!/usr/bin/env python3
"""Validate evidence-card v1.2 structure and hard rules R01-R08."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


SOURCE_REQUIRED = [
    "card_schema", "card_id", "card_version", "card_type", "artifact_type",
    "evidence_roles", "workflow_status", "completion_level", "source_work_id",
    "source_manifestation_id", "source_version", "source_snapshot_hash",
    "source_provenance", "acquired_via", "acquired_at", "validity_checked_at",
    "language", "access_level", "project_ids", "research_question_ids",
    "decision_ids", "related_card_ids", "independence_group_ids",
    "version_family_ids", "reading_scope", "extraction_method",
    "generator_or_pipeline_version", "verified_claim_ids", "verified_by",
    "verified_at", "human_review_status", "human_reviewer", "funding",
    "commissioning_party", "declared_conflicts", "review_independence",
    "confidentiality", "water_context_status", "method_modules",
    "l3_gate_decision", "l3_gate_gap", "l3_gate_change", "relevance",
    "verification_readiness", "applicability", "decision_effect",
    "load_bearing_conflict", "unresolved_conflict_ids", "recheck_trigger",
]

ENUMS = {
    "workflow_status": {"ingested", "screened", "extracted", "source_checked", "peer_reviewed", "approved", "superseded", "archived", "draft"},
    "completion_level": {"L0", "L1", "L2", "L3"},
    "reading_scope": {"metadata", "abstract", "partial_full_text", "full_text", "supplement", "data_sample", "full_data", "source_code", "actual_run", "mixed"},
    "extraction_method": {"human", "ai_assisted", "automated"},
    "human_review_status": {"not_started", "in_progress", "completed"},
    "water_context_status": {"not_applicable", "partial", "complete"},
    "relevance": {"central", "supporting", "peripheral", "irrelevant"},
    "verification_readiness": {"verified", "partially_verified", "clue_only", "currently_unusable"},
    "applicability": {"direct", "conditional", "transfer_check_required", "not_applicable"},
    "decision_effect": {"strengthens", "weakens", "limits", "contradicts", "no_change"},
}

DYNAMIC_ARTIFACTS = {
    "standard", "guideline", "regulation", "policy", "official_interpretation",
    "dataset", "data_product", "database", "api", "statistical_product",
    "monitoring_bulletin", "software_release", "repository", "model_package",
    "workflow", "container", "model_weights",
}

CLAIM_REQUIRED = {
    "claim_id", "source_id", "claim_type", "statement_role", "inference_type",
    "support_status", "statement", "evidence_origin", "scope", "locator",
    "directly_supports", "does_not_support", "author_interpretation",
    "analyst_judgment", "method_requirements", "relations",
    "independence_group_ids", "verification_status", "verified_by", "verified_at",
}

RELATIONS = {"supports", "contradicts", "qualifies", "depends_on", "reproduces", "supersedes"}
SUPPORT_STATES = {"supported", "partially_supported", "not_supported", "contradicted", "unresolved", "not_reported", "not_checked"}
INFERENCE_TYPES = {"descriptive", "comparative", "association", "causal", "prediction", "mechanism", "transferability", "normative", "implementation"}
VERIFICATION_STATES = {"not_checked", "metadata_checked", "partially_source_checked", "source_checked", "independently_reproduced"}


def parse_scalar(raw: str) -> Any:
    value = raw.strip()
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return value.strip("\"'")


def parse_frontmatter(text: str) -> dict[str, Any]:
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    data: dict[str, Any] = {}
    for line in parts[1].splitlines():
        if not line.strip() or line.lstrip().startswith("#") or ":" not in line:
            continue
        key, raw = line.split(":", 1)
        if key.strip() and not key.startswith((" ", "\t")):
            data[key.strip()] = parse_scalar(raw)
    return data


def json_blocks(text: str, language: str) -> tuple[list[dict[str, Any]], list[str]]:
    pattern = rf"(?ms)^(```|~~~){re.escape(language)}\s*\n(.*?)^\1\s*$"
    objects: list[dict[str, Any]] = []
    errors: list[str] = []
    for index, match in enumerate(re.finditer(pattern, text), start=1):
        try:
            value = json.loads(match.group(2))
            if not isinstance(value, dict):
                errors.append(f"R00 {language} block {index} must contain one JSON object")
            else:
                objects.append(value)
        except json.JSONDecodeError as exc:
            errors.append(f"R00 invalid {language} block {index}: {exc.msg} at line {exc.lineno}")
    return objects, errors


def blank(value: Any) -> bool:
    return value is None or value == "" or (isinstance(value, str) and "{{" in value)


def nonempty_dict_fields(value: Any, fields: list[str]) -> bool:
    return isinstance(value, dict) and all(field in value and not blank(value[field]) for field in fields)


def list_value(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def validate_claim(claim: dict[str, Any], final: bool) -> list[str]:
    errors: list[str] = []
    cid = claim.get("claim_id") or "<unknown>"
    for key in sorted(CLAIM_REQUIRED - set(claim)):
        errors.append(f"R00 {cid} missing field: {key}")

    if claim.get("support_status") not in SUPPORT_STATES:
        errors.append(f"R03 {cid} invalid support_status; not_supported, contradicted, not_reported and not_checked are distinct states")
    if claim.get("inference_type") not in INFERENCE_TYPES:
        errors.append(f"R04 {cid} invalid inference_type")
    if claim.get("verification_status") not in VERIFICATION_STATES:
        errors.append(f"R00 {cid} invalid verification_status")

    relations = claim.get("relations")
    if not isinstance(relations, dict) or set(relations) != RELATIONS or any(not isinstance(v, list) for v in relations.values()):
        errors.append(f"R00 {cid} relations must contain exactly six relation arrays")

    if claim.get("claim_type") == "numeric":
        numeric = claim.get("numeric")
        scope = claim.get("scope")
        locator = claim.get("locator")
        if not isinstance(numeric, dict) or blank(numeric.get("value")) or blank(numeric.get("reported_unit")):
            errors.append(f"R02 {cid} numeric claim requires value and reported_unit")
        if not nonempty_dict_fields(scope, ["object_or_denominator", "spatial", "temporal", "comparator"]):
            errors.append(f"R02 {cid} numeric claim requires denominator/object, spatial and temporal scope, and comparator")
        if not nonempty_dict_fields(locator, ["material", "page_or_section"]):
            errors.append(f"R02 {cid} numeric claim requires a precise locator")
        if not isinstance(numeric, dict) or blank(numeric.get("uncertainty")):
            errors.append(f"R02 {cid} numeric claim requires uncertainty or the literal not_reported")

    inference = claim.get("inference_type")
    req = claim.get("method_requirements") if isinstance(claim.get("method_requirements"), dict) else {}
    required_by_inference = {
        "causal": ["identification_design", "confounding_assessment", "alternative_explanations"],
        "prediction": ["issue_time", "lead_time", "decision_time_information", "independent_validation"],
        "transferability": ["target_context_match", "transfer_gaps"],
        "normative": ["normative_scope", "scientific_validity_status"],
    }
    if inference in required_by_inference and not nonempty_dict_fields(req, required_by_inference[inference]):
        errors.append(f"R04 {cid} {inference} claim lacks required inference controls: {', '.join(required_by_inference[inference])}")
    if inference == "normative" and str(req.get("scientific_validity_status", "")).lower() in {"true", "proven", "validated", "scientifically_valid"}:
        errors.append(f"R04 {cid} normative force cannot establish scientific validity")

    forbidden_upgrades = {
        "acceptance": {"long_term_effective", "extreme_condition_safe"},
        "installed": {"paper_reproduced", "scientifically_valid"},
        "downloadable": {"fit_for_purpose", "scientifically_valid"},
        "review_secondary": {"primary_source_verified"},
        "book_secondary": {"primary_source_verified"},
    }
    evidence_state = req.get("evidence_state")
    claimed_state = req.get("claimed_state")
    if evidence_state in forbidden_upgrades and claimed_state in forbidden_upgrades[evidence_state]:
        errors.append(f"R05 {cid} forbidden evidence-state upgrade: {evidence_state} -> {claimed_state}")

    if final:
        for key in ["claim_id", "source_id", "statement", "evidence_origin", "directly_supports", "does_not_support"]:
            if blank(claim.get(key)):
                errors.append(f"R00 {cid} final claim has blank field: {key}")
        locator = claim.get("locator")
        if not isinstance(locator, dict) or blank(locator.get("material")) or not any(not blank(locator.get(k)) for k in ["page_or_section", "table_figure_clause_or_row"]):
            errors.append(f"R00 {cid} final claim lacks a source locator")
        if claim.get("verification_status") in {"not_checked", "metadata_checked"}:
            errors.append(f"R01 {cid} final decisive claim is not source checked")
    return errors


def validate_source(meta: dict[str, Any], text: str, final: bool) -> tuple[list[str], list[str], list[dict[str, Any]]]:
    errors: list[str] = []
    warnings: list[str] = []
    for key in SOURCE_REQUIRED:
        if key not in meta:
            errors.append(f"R00 missing frontmatter field: {key}")
    if meta.get("card_schema") != "evidence-card-v1.2":
        errors.append("R00 card_schema must be evidence-card-v1.2")
    for key, choices in ENUMS.items():
        if key in meta and meta[key] not in choices:
            errors.append(f"R00 invalid {key}: {meta[key]}")

    level = meta.get("completion_level")
    scope = meta.get("reading_scope")
    readiness = meta.get("verification_readiness")
    applicability = meta.get("applicability")
    workflow = meta.get("workflow_status")
    verified = list_value(meta.get("verified_claim_ids"))

    if scope in {"metadata", "abstract"}:
        if readiness in {"verified", "partially_verified"} or applicability == "direct" or verified or workflow in {"source_checked", "peer_reviewed", "approved"}:
            errors.append("R01 metadata/abstract reading cannot be source-verified, direct, or contain verified claims")
    if level in {"L0", "L1"} and (readiness in {"verified", "partially_verified"} or applicability == "direct"):
        errors.append("R01 L0/L1 cannot be verified, partially verified, or directly applicable")

    claims, block_errors = json_blocks(text, "claim-json")
    errors.extend(block_errors)
    if level in {"L2", "L3"} and not claims:
        errors.append("R00 L2/L3 source card requires at least one claim-json block")
    ids = [str(c.get("claim_id")) for c in claims if c.get("claim_id")]
    if len(ids) != len(set(ids)):
        errors.append("R00 duplicate claim_id in card")
    for claim in claims:
        errors.extend(validate_claim(claim, final))
        if final and claim.get("source_id") != meta.get("source_manifestation_id"):
            errors.append(f"R00 {claim.get('claim_id')} source_id differs from source_manifestation_id")

    if meta.get("artifact_type") in DYNAMIC_ARTIFACTS and level in {"L2", "L3"}:
        for key in ["validity_checked_at", "source_snapshot_hash", "source_version", "recheck_trigger"]:
            if blank(meta.get(key)) and final:
                errors.append(f"R06 dynamic source requires {key}")

    unresolved = list_value(meta.get("unresolved_conflict_ids"))
    if meta.get("load_bearing_conflict") is True or unresolved:
        if workflow == "approved" or readiness == "verified" or applicability == "direct":
            errors.append("R07 unresolved load-bearing conflict blocks approved, verified, and direct states")

    if meta.get("extraction_method") in {"ai_assisted", "automated"}:
        required_ai = ["generator_or_pipeline_version", "source_snapshot_hash", "human_reviewer"]
        if final and any(blank(meta.get(k)) for k in required_ai):
            errors.append("R08 AI extraction requires generator version, source snapshot hash, and human reviewer")
        if final and meta.get("human_review_status") != "completed":
            errors.append("R08 AI extraction requires completed human review")
        if final and not verified:
            errors.append("R08 AI extraction requires verified_claim_ids")

    if final:
        for key in ["card_id", "source_work_id", "source_manifestation_id", "source_version", "source_provenance", "acquired_via", "acquired_at"]:
            if blank(meta.get(key)):
                errors.append(f"R00 final source card has blank field: {key}")
        if level in {"L2", "L3"} and workflow not in {"source_checked", "peer_reviewed", "approved"}:
            errors.append("R01 final L2/L3 card must have source_checked, peer_reviewed, or approved workflow status")
        missing_verified = sorted(set(ids) - set(str(x) for x in verified))
        if level in {"L2", "L3"} and missing_verified:
            errors.append("R01 decisive claims absent from verified_claim_ids: " + ", ".join(missing_verified))
        if level == "L3" and not all(meta.get(key) is True for key in ["l3_gate_decision", "l3_gate_gap", "l3_gate_change"]):
            errors.append("R04 L3 requires all three dynamic-reading gates to be true")

    if meta.get("water_context_status") in {"partial", "complete"}:
        contexts, context_errors = json_blocks(text, "water-context-json")
        errors.extend(context_errors)
        if len(contexts) != 1:
            errors.append("R00 water_context_status partial/complete requires exactly one water-context-json block")
        elif final and meta.get("water_context_status") == "complete":
            context = contexts[0]
            for key in ["water_object_type", "spatial_extent", "spatial_support", "start_date", "end_date", "temporal_resolution", "time_zone"]:
                if blank(context.get(key)):
                    errors.append(f"R00 complete water context has blank field: {key}")
            for index, var in enumerate(list_value(context.get("variables")), start=1):
                if not isinstance(var, dict) or blank(var.get("name")) or blank(var.get("reported_unit")):
                    errors.append(f"R02 water variable {index} requires name and reported_unit")
                elif var.get("reported_unit") != var.get("normalized_unit") and blank(var.get("conversion_rule")):
                    errors.append(f"R02 water variable {index} unit conversion requires conversion_rule")

    if not final and meta.get("extraction_method") in {"ai_assisted", "automated"} and meta.get("human_review_status") != "completed":
        warnings.append("R08 draft contains AI-assisted extraction that is not yet human-reviewed")
    return errors, warnings, claims


def validate_decision(meta: dict[str, Any], text: str, final: bool, known_claims: dict[str, dict[str, Any]] | None) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    for key in ["card_schema", "card_id", "card_version", "card_type", "workflow_status", "completion_level", "decision_id", "research_question_ids", "as_of_date", "decision_owner", "load_bearing_conflict", "unresolved_conflict_ids", "included_claim_ids", "excluded_claim_ids", "independence_group_ids", "version_family_ids"]:
        if key not in meta:
            errors.append(f"R00 missing decision frontmatter field: {key}")
    blocks, block_errors = json_blocks(text, "decision-json")
    errors.extend(block_errors)
    if len(blocks) != 1:
        errors.append("R00 decision card requires exactly one decision-json block")
        return errors, warnings
    decision = blocks[0]
    required = ["decision_id", "research_question_ids", "included_claims", "excluded_claims", "exclusion_reasons", "independence_groups", "version_families", "agreements", "conflicts", "unresolved_conflicts", "coverage", "transferability", "evidence_profile", "current_conclusion", "supported", "unsupported", "decision_effect", "remaining_evidence_gap", "next_update_trigger"]
    for key in required:
        if key not in decision:
            errors.append(f"R00 decision-json missing field: {key}")
    included = [str(x) for x in list_value(decision.get("included_claims"))]
    excluded = [str(x) for x in list_value(decision.get("excluded_claims"))]
    if set(included) & set(excluded):
        errors.append("R03 a claim cannot be both included and excluded")
    if list_value(meta.get("included_claim_ids")) != list_value(decision.get("included_claims")):
        errors.append("R00 frontmatter included_claim_ids differs from decision-json included_claims")
    if list_value(meta.get("excluded_claim_ids")) != list_value(decision.get("excluded_claims")):
        errors.append("R00 frontmatter excluded_claim_ids differs from decision-json excluded_claims")
    if known_claims is not None:
        missing = sorted((set(included) | set(excluded)) - set(known_claims))
        if missing:
            errors.append("R00 decision references unknown claim_id: " + ", ".join(missing))
        for claim_id in included:
            indexed = known_claims.get(claim_id)
            if not indexed:
                continue
            if indexed.get("completion_level") not in {"L2", "L3"}:
                errors.append(f"R01 decision includes {claim_id} below L2")
            if indexed.get("verification_status") not in {"source_checked", "independently_reproduced"}:
                errors.append(f"R01 decision includes {claim_id} without source-level verification")
    profile = decision.get("evidence_profile")
    dimensions = ["directness", "internal_validity", "independence", "precision", "applicability", "reproducibility"]
    if not isinstance(profile, dict):
        errors.append("R00 evidence_profile must be an object")
    else:
        for dimension in dimensions:
            item = profile.get(dimension)
            if not isinstance(item, dict) or item.get("level") not in {"high", "medium", "low", "unknown"} or not isinstance(item.get("basis_claim_ids"), list):
                errors.append(f"R00 evidence_profile.{dimension} requires level and basis_claim_ids")
            elif any(str(cid) not in included for cid in item.get("basis_claim_ids", [])):
                errors.append(f"R00 evidence_profile.{dimension} cites a claim not included in the decision")
    unresolved = list_value(decision.get("unresolved_conflicts")) or list_value(meta.get("unresolved_conflict_ids"))
    if meta.get("load_bearing_conflict") is True or unresolved:
        if meta.get("workflow_status") == "approved":
            errors.append("R07 unresolved load-bearing conflict blocks approved decision")
    if final:
        for key in ["card_id", "decision_id", "as_of_date", "decision_owner"]:
            if blank(meta.get(key)):
                errors.append(f"R00 final decision card has blank field: {key}")
        for key in ["current_conclusion", "supported", "unsupported", "next_update_trigger"]:
            if blank(decision.get(key)):
                errors.append(f"R00 final decision-json has blank field: {key}")
        if not included:
            errors.append("R01 final decision synthesis requires at least one included claim")
    return errors, warnings


def collect_claim_index(root: Path) -> tuple[dict[str, dict[str, Any]], list[str]]:
    seen: dict[str, dict[str, Any]] = {}
    source_seen: dict[str, Path] = {}
    errors: list[str] = []
    for path in root.rglob("*.md"):
        try:
            text = path.read_text(encoding="utf-8-sig")
        except OSError:
            continue
        meta = parse_frontmatter(text)
        if meta.get("card_schema") != "evidence-card-v1.2":
            continue
        manifestation = meta.get("source_manifestation_id")
        if meta.get("card_type") == "source_evidence" and manifestation and not blank(manifestation):
            if manifestation in source_seen and source_seen[manifestation] != path:
                errors.append(f"R00 duplicate source_manifestation_id {manifestation}: {source_seen[manifestation]} and {path}")
            source_seen[manifestation] = path
        claims, _ = json_blocks(text, "claim-json")
        for claim in claims:
            cid = claim.get("claim_id")
            if not cid or blank(cid):
                continue
            cid = str(cid)
            if cid in seen and seen[cid]["path"] != path:
                errors.append(f"R00 duplicate claim_id {cid}: {seen[cid]['path']} and {path}")
            seen[cid] = {
                "path": path,
                "completion_level": meta.get("completion_level"),
                "verification_status": claim.get("verification_status"),
                "source_manifestation_id": meta.get("source_manifestation_id"),
            }
    return seen, errors


def validate_text(text: str, mode: str = "draft", known_claims: dict[str, dict[str, Any]] | None = None) -> tuple[list[str], list[str], dict[str, Any]]:
    meta = parse_frontmatter(text)
    final = mode == "final"
    errors: list[str] = []
    warnings: list[str] = []
    if not meta:
        return ["R00 missing or invalid flat YAML frontmatter"], warnings, meta
    if final:
        markers = sorted(set(re.findall(r"\{\{[^}]+\}\}|〔[^〕]+〕|待填写", text)))
        if markers:
            errors.append("R00 unresolved template markers: " + ", ".join(markers[:10]))
    card_type = meta.get("card_type")
    if card_type == "source_evidence":
        e, w, _ = validate_source(meta, text, final)
    elif card_type == "decision_synthesis":
        e, w = validate_decision(meta, text, final, known_claims)
    else:
        e, w = [f"R00 unknown card_type: {card_type}"], []
    errors.extend(e)
    warnings.extend(w)
    return errors, warnings, meta


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("card")
    parser.add_argument("--mode", choices=["draft", "final"], default="draft")
    parser.add_argument("--index-root", help="Optional vault/repository root for duplicate and cross-card claim checks")
    args = parser.parse_args()

    path = Path(args.card)
    text = path.read_text(encoding="utf-8-sig")
    known: dict[str, dict[str, Any]] | None = None
    index_errors: list[str] = []
    if args.index_root:
        known, index_errors = collect_claim_index(Path(args.index_root))
    errors, warnings, meta = validate_text(text, args.mode, known)
    errors = index_errors + errors

    print(f"card: {path}")
    print(f"type: {meta.get('card_type')}")
    print(f"level: {meta.get('completion_level')}")
    for item in warnings:
        print(f"WARNING: {item}")
    for item in errors:
        print(f"ERROR: {item}")
    if errors:
        raise SystemExit(1)
    print("PASS: R01-R08 structural checks completed; scientific validity still requires source review")


if __name__ == "__main__":
    main()
