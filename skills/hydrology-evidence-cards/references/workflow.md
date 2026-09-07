# Zotero to Source-Claim-Decision workflow V1.2

## 1. Bind the request

Record the user-specified Zotero item key or collection, current research question, intended decision, allowed output location and batch boundary. Do not broaden the literature set.

## 2. Establish source identity

Use Zotero read-only metadata and the official identifier or source when available. Assign source_work_id and source_manifestation_id. Check whether the same manifestation already has a card before creating one. Record acquisition channel separately from provenance.

## 3. Select level

- L0 for identity and deduplication.
- L1 for whether continued reading is justified.
- L2 when a located, source-checked claim is needed for a live question.
- L3 only after the three dynamic-reading gates pass.

Start at the least expensive level that answers the current decision. Do not fill empty fields merely because a template contains them.

## 4. Choose profile, roles and modules

Choose one source profile. Add all evidence roles that matter. Add the common water-context module when a specific water setting matters and every method module carrying a decisive assumption.

Example:

    python scripts/new_card.py --type original-research --level L2 --card-id EC-20260904-001 --title Example --manifestation-id SRC-2026-0042-V1 --source-work-id WORK-2026-0042 --source-version published-v1 --zotero-item-key ABCD1234 --research-question-id RQ-001 --role original_research --role software_validation --module hydro-forecast-ml --water-context --output EC-20260904-001_Example.md

## 5. Read only what supports the current level

For L0, use identity records. For L1, read the abstract or executive material and label it honestly. For L2, open the exact pages, tables, figures, clauses, rows, metadata or logs needed for each decisive claim. For L3, follow the stated minimum path through methods, supplements, data, code, versions or runs and stop at the predeclared condition.

## 6. Write claims

Create one claim-json block per proposition. Use a globally unique claim_id. Record source fact, evidence origin, exact scope, locator, permitted inference, support, non-support, interpretations, relations, independence groups and verification. Add the method_requirements demanded by the inference type.

Do not cap the complete record at three claims. Only the quick decision summary is limited to the most decision-relevant three.

## 7. Validate and review

During drafting:

    python scripts/validate_card.py CARD.md --mode draft

Before handoff:

    python scripts/validate_card.py CARD.md --mode final --index-root VAULT_OR_REPOSITORY

Then reopen every decisive locator and perform the manual scientific review in SKILL.md. Fix R01-R08 failures; do not waive them with prose.

## 8. Synthesize decisions

Only L2 or L3 claims may enter a Decision/Synthesis card. Create it with type decision-synthesis, list included and excluded claim IDs, group dependence and versions, expose conflicts, describe coverage and transferability, and record the six-dimension evidence profile with basis claim IDs.

    python scripts/new_card.py --type decision-synthesis --card-id DS-20260904-001 --title Decision --decision-id DEC-001 --research-question-id RQ-001 --decision-owner USER --output DS-20260904-001_Decision.md

An unresolved load-bearing conflict blocks approved status. The decision card must say what is supported, what remains unsupported and what evidence would change the decision.

## 9. Export the relation graph

    python scripts/export_graph.py VAULT_OR_REPOSITORY --output evidence-graph.json

Unresolved edges mean a referenced Source, Claim or Decision object is absent from the scanned root. The graph is a derived view and never becomes a second source of scientific facts.

## 10. Store and synchronize

Keep one formal Markdown per source manifestation and one per decision. Commit cards, rules, manifests and graph views to Git. Keep full text, Zotero databases, credentials, raw data, restricted reports, caches and run outputs in their authorised systems.

