---
name: hydrology-evidence-cards
description: Read items and indexed full text from a local Zotero library and create one source-grounded Markdown evidence card per paper, review, survey or monitoring report, engineering report, book chapter, standard or policy, dataset, or software/model/code source. Use for Zotero-to-Obsidian evidence-card creation, evidence extraction, card revision, or card validation in water-conservancy research. Do not use for literature discovery, citation-metadata verification, or unsupported topic/innovation generation.
---

# Hydrology Evidence Cards

Create a traceable card from material actually available and actually read. Keep source statements, author interpretation, and the analyst's inference separate. Never complete a field from general knowledge, a similar paper, a title, or an abstract when the card says the full text was checked.

## Route the request

1. Confirm the requested source, research question, output folder, and whether one item or a bounded batch is intended.
2. Read `references/evidence-boundaries.md` before extracting scientific claims.
3. Read `references/source-classification.md` and select exactly one primary card type. Add secondary modules only when a composite source genuinely contains them.
4. For Zotero input, follow `references/zotero-access.md`. Use `scripts/zotero_reader.py` only against Zotero Desktop's local read-only API; never edit `zotero.sqlite`.
5. Follow `references/workflow.md` from identity check through validation and handoff.
6. Copy the matching standalone template from `assets/templates/`. Use `scripts/new_card.py` to create a populated skeleton when useful.
7. Read the source sections needed for each claim. Record the exact version and reading coverage before writing results.
8. Run `scripts/validate_card.py --mode final CARD.md`. Treat a passing result as structural validation only; manually recheck scientific claims and source locations.

## Select the template

| Primary source type | Template |
| --- | --- |
| Original empirical, modelling, theoretical, qualitative, thesis, conference, or methods research | `assets/templates/01_original-research.md` |
| Narrative, scoping, systematic review, evidence map, or meta-analysis | `assets/templates/02_review-synthesis.md` |
| Government survey, census, monitoring bulletin, statistical yearbook, or institutional statistical report | `assets/templates/03_survey-monitoring-statistics.md` |
| Feasibility, design, construction, operation, post-evaluation, incident, or engineering technical report | `assets/templates/04_engineering-report.md` |
| Monograph, textbook, handbook, or chapter | `assets/templates/05_book-chapter.md` |
| Standard, specification, guideline, regulation, or policy | `assets/templates/06_standard-guideline-policy.md` |
| Dataset, data product, metadata record, or data paper used mainly to describe data | `assets/templates/07_dataset-data-product.md` |
| Software, model package, repository, release, implementation paper used mainly to describe code | `assets/templates/08_software-model-code.md` |

Do not classify a journal article as a review from Zotero `itemType` alone. Inspect the article's stated purpose and methods. Do not classify every official document as a statistical report or every report as an engineering report. If evidence supports more than one type, choose the type that matches the source's main evidentiary role and note the additional role.

## Non-negotiable evidence rules

- One source and one version per formal card. Update the existing card instead of creating a parallel duplicate.
- State whether the evidence comes from title/abstract, partial full text, full text, supplement, data, code, or another source's quotation.
- Give each consequential claim a local `Cxx` identifier and a precise page, section, figure, table, clause, record, or file-and-line locator.
- Preserve populations, basins, stations, periods, scales, sample units, denominators, units, uncertainty, comparison conditions, and modal qualifiers.
- Mark absent information as `原文未报告（已查：…）`, unavailable material as `未取得`, unread material as `未阅读`, and irrelevant fields as `不适用（原因）`.
- Never infer causality from association, field performance from simulation, replication from executable code, validity from standards compliance, or independent confirmation from a review's secondary citation.
- Keep quoted text short. Store bibliographic identity and links in Git; keep licensed full text in Zotero or the authorized document store.
- Do not create formal topics, innovations, opportunities, or scientific conclusions merely because the card is complete.

## Output contract

Return one Markdown file for each source. The filename should be stable and filesystem-safe, for example `EC-20260904-001_Short_Title.md`. Include the Zotero item key and source version in frontmatter. If the source cannot support a final card, still create a clearly marked `draft` only when the user requested a draft; otherwise report the exact missing material and stop.

When handling more than one item, write a manifest containing the requested scope, matched Zotero keys, card paths, primary types, reading coverage, validation result, and unresolved blockers. Do not silently add search results outside the requested scope.

## References

- `references/workflow.md`: operational sequence, naming, batch behavior, and handoff.
- `references/evidence-boundaries.md`: scientific fidelity and claim rules.
- `references/source-classification.md`: decision rules for the eight source types.
- `references/zotero-access.md`: local Zotero commands and failure handling.
- `references/installation.md`: installation and portability for other users.
