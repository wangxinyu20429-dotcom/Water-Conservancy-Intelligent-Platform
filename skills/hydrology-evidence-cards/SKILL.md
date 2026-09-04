---
name: hydrology-evidence-cards
description: Read a user-specified source and available indexed full text from local Zotero, then register one versioned Source, extract source-located Claim objects, and connect verified claims to a separate platform Decision/Synthesis card. Supports L0-L3 completion, eight source profiles, water context, hydrology method modules, AI provenance, relation-graph export, and R01-R08 hard validation. Use for Zotero-to-Obsidian evidence work in water research. Do not use for literature discovery, bibliographic identity correction, or unsupported novelty generation.
---

# Hydrology Evidence Cards V1.2

Build auditable research evidence from exact source content. Do not write a generic literature summary.

The invariant chain is:

Source version → Claim → locator and evidence-generating design → permitted inference and boundary → Decision/Synthesis.

Machine validation proves only that the structure and explicit rules pass. It never proves that a scientific claim is true.

## Required reading order

1. Read references/evidence-architecture.md.
2. Read references/evidence-boundaries.md.
3. Read references/source-classification.md and choose one source profile plus every applicable evidence role.
4. For Zotero input, read references/zotero-access.md.
5. Read references/workflow.md.
6. Create a card with scripts/new_card.py or assemble it from assets/base, one assets/templates profile, and conditional assets/modules.
7. Run scripts/validate_card.py in draft mode during work and final mode before handoff.
8. Reopen every decisive locator and complete the manual scientific review. A script PASS is not scientific approval.

## Object and granularity rules

- Register an exact source manifestation or release once. Use source_work_id to group manifestations of the same intellectual work and source_manifestation_id for the exact version used.
- Do not copy full source metadata for each research question. Add globally unique Claim objects to the single source card and link their claim_id values to multiple Decision cards.
- Separate artifact_type from evidence_roles. A journal article can supply original_research, dataset_quality, and software_validation roles at the same time.
- Each claim-json block contains one proposition. Preserve direction, unit, denominator, comparison, uncertainty, qualifiers and precise locator.
- A platform Decision/Synthesis card is a ninth card type. It references claim_id values, records inclusion, exclusion, dependence, conflicts, coverage, transferability and the current decision. It is not a published review source card.
- Use independence_group_ids and version_family_ids to prevent repeated counting of the same station network, dataset, project, model family, preprint/publication pair, report series or commissioned work.

## Completion levels

| Level | Purpose | Minimum content | Permitted use |
| --- | --- | --- | --- |
| L0 | identity, deduplication and version registration | exact source identity, manifestation, acquisition and access state | inventory only |
| L1 | rapid screening | current question, potential role, result clue and first boundary | discovery and prioritisation only |
| L2 | usable evidence | at least one located and source-checked claim with scope, support boundary and verification record | may enter Decision/Synthesis |
| L3 | full audit | all decisive claims, triggered method modules, conflicts, supplementary or run checks, independent review | high-impact, disputed or reproduction decisions |

L0 and L1 must not be marked verified or directly applicable. Enter L3 only when all three dynamic-reading gates are true: a clear high-impact decision exists, a decisive evidence gap is located, and opening new material may change the judgment.

## Source profiles

| Type key | Profile | Scientific center |
| --- | --- | --- |
| original-research | assets/templates/01_original-research.md | design, independent unit, information path, inference, decisive results and failure conditions |
| review-synthesis | assets/templates/02_review-synthesis.md | search universe, inclusion, overlap, bias, synthesis, heterogeneity and certainty |
| survey-monitoring-statistics | assets/templates/03_survey-monitoring-statistics.md | coverage, measurement, denominator, station history, uncertainty, revisions and comparability |
| engineering-report | assets/templates/04_engineering-report.md | evidence strata, criteria, boundary conditions, measured versus simulated evidence, failure and remaining risk |
| book-chapter | assets/templates/05_book-chapter.md | proposition, definition, derivation, translation, source lineage and domain |
| standard-guideline-policy | assets/templates/06_standard-guideline-policy.md | authority, clause, force, applicability, version, conformity and scientific boundary |
| dataset-data-product | assets/templates/07_dataset-data-product.md | immutable snapshot, generating process, variables, quality, licence and fitness |
| software-model-code | assets/templates/08_software-model-code.md | fixed artifact, environment, input/output contract, run evidence, reproduction and scientific validation |
| decision-synthesis | assets/templates/09_platform-decision-synthesis.md | cross-source claim synthesis, dependence, conflict, transferability and decision effect |

Zotero itemType is only a clue. Choose artifact_type from what the object is and evidence_roles from what its claims do in the current research decision.

## Conditional modules

- Add assets/modules/water-context.md when the evidence concerns a concrete water object, basin, station, period, event, scenario or engineering system.
- Add method-hydro-forecast-ml.md for forecasting or machine-learning claims.
- Add method-hydrodynamic-simulation.md for hydrologic or hydrodynamic simulation.
- Add method-frequency-drought-climate.md for frequency analysis, drought or climate projections.
- Add method-monitoring-quality-remote-sensing.md for monitoring, water quality or remote sensing.
- Add method-engineering-operation-safety.md for engineering operations and safety.

Conditional modules follow the inference and method, not the publication format. Include only relevant modules, but do not omit a module that carries a decisive inference assumption.

## Claim rules

- Distinguish source_fact, author_interpretation and analyst_judgment.
- Distinguish descriptive, comparative, association, causal, prediction, mechanism, transferability, normative and implementation inference types.
- Distinguish supported, partially_supported, not_supported, contradicted, unresolved, not_reported and not_checked. Never merge these states.
- Numeric claims require value, reported unit, denominator or object, temporal and spatial scope, comparator, locator, and uncertainty or the literal not_reported.
- Causal claims require identification design, confounding assessment and alternative explanations.
- Prediction claims require issue time, lead time, information available at decision time and independent validation.
- Transfer claims require a target-context match and explicit transfer gaps.
- Normative claims support clauses and applicability. Normative force does not establish scientific validity.
- Use relations supports, contradicts, qualifies, depends_on, reproduces and supersedes to build a graph between claims.

## Non-upgrade rules

- Engineering acceptance does not prove long-term effectiveness or safety in untested extreme conditions.
- Software installation or example execution does not prove paper reproduction or scientific validity.
- Data access does not prove quality or fitness for the current task.
- A review's paraphrase does not become source-checked primary evidence until the original source is checked.
- A book's paraphrase does not become primary empirical evidence.
- An official source proves identity, clause, release or record only within that source's authority.

## Missing information and AI provenance

Use only: not_applicable, not_obtained, not_read, not_reported, not_found_after_check, conflict_pending. Never fill a gap from general knowledge or a similar source.

AI-assisted or automated extraction must record extraction_method, generator_or_pipeline_version, source_snapshot_hash, human_review_status, human_reviewer and verified_claim_ids. AI extraction confidence, scientific evidence certainty and applicability to the current decision are separate concepts.

## Manual scientific review

For each decisive claim, reopen the named source version and locator and verify:

1. The fact preserves direction, unit, denominator, comparison, uncertainty and qualifiers.
2. The independent unit and evidence-generating design support the stated inference type.
3. Training, calibration, validation, testing and operational information are separated where relevant.
4. Negative results, failure settings, internal conflicts and unsupported transfer are visible.
5. Source fact, author interpretation and analyst judgment remain distinct.
6. Independence groups and version families prevent duplicated evidence.
7. What the claim supports and does not support is explicit.
8. An unresolved load-bearing conflict blocks approved, verified or direct status.

## Output and storage contract

Return one Markdown source card per exact source version and one Decision/Synthesis card per platform decision. Use stable file names such as EC-20260904-001_Short_Title.md and DS-20260904-001_Decision.md.

For a bounded batch, also create a manifest containing the requested scope, matched Zotero keys, source and manifestation IDs, output paths, levels, reading coverage, validation result and unresolved blockers. Do not expand the batch beyond the user's item list or collection.

Git may store bibliographic identity, source links, cards, manifests and derived graph JSON. Keep licensed full text, Zotero databases, credentials, temporary extracts, restricted project files and large datasets in their authorised systems.

