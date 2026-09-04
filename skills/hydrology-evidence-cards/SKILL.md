---
name: hydrology-evidence-cards
description: Read a specified source and available indexed full text from local Zotero, then create or revise one source-grounded Markdown evidence card whose decisive claims, evidence-generating design, validity boundaries, locators, and research-decision effect are traceable. Supports original research, reviews, surveys/statistical reports, engineering reports, books, standards/policies, datasets, and software/models/code. Use for Zotero-to-Obsidian evidence cards and evidence-card validation in water research. Do not use for literature discovery, citation-metadata verification, or unsupported topic and novelty generation.
---

# Hydrology Evidence Cards

Produce a decision-grade evidence record, not a generic summary. The card must show:

current question → how evidence was produced → decisive evidence → permitted inference → validity boundary → what it supports and does not support → effect on the current research decision.

More fields do not make a stronger card. Read only the material required to establish this chain, but preserve every condition that can change the conclusion.

## Required reading order

1. Read references/evidence-architecture.md.
2. Read references/evidence-boundaries.md.
3. Read references/source-classification.md and choose one primary card type from the source's evidence-producing role.
4. For Zotero input, read references/zotero-access.md.
5. Follow references/workflow.md.
6. Copy the matching standalone template from assets/templates or use scripts/new_card.py.
7. Before handoff, run scripts/validate_card.py --mode final CARD.md and perform the manual scientific review required below.

## Source routing

| Primary source type | Template | Scientific center |
| --- | --- | --- |
| Original empirical, modelling, theoretical, qualitative, thesis, conference, or methods research | assets/templates/01_original-research.md | inference target, independent unit, information path, comparison and validation, decisive results, failure conditions |
| Narrative, scoping, systematic review, evidence map, or meta-analysis | assets/templates/02_review-synthesis.md | search universe, eligibility, evidence unit, bias, synthesis, heterogeneity, overlap, certainty |
| Government survey, census, monitoring bulletin, statistical yearbook, or institutional statistical report | assets/templates/03_survey-monitoring-statistics.md | target population, coverage, measurement, denominator, weighting, uncertainty, revision, comparability |
| Feasibility, design, construction, operation, post-evaluation, incident, or engineering technical report | assets/templates/04_engineering-report.md | project stage, evidence stratum, boundary conditions, criteria, measured versus simulated evidence, failure and transfer |
| Monograph, textbook, handbook, or chapter | assets/templates/05_book-chapter.md | proposition, definition, reasoning or derivation, source lineage, edition, domain of application |
| Standard, specification, guideline, regulation, or policy | assets/templates/06_standard-guideline-policy.md | authority, force, scope, current clause, exception, conformity evidence, scientific boundary |
| Dataset, data product, metadata record, or data paper used mainly to describe data | assets/templates/07_dataset-data-product.md | generating process, variable semantics, coverage, quality, missingness, version bundle, licence, fitness for purpose |
| Software, model package, repository, release, or implementation resource | assets/templates/08_software-model-code.md | fixed artifact, model-implementation relation, input/output contract, verification, validation, run state, version drift |

Zotero itemType is only a clue. A data paper used to test a scientific hypothesis can be original research; a software paper centered on performance experiments can be original research. Choose the source role that produces the claim used in the current decision.

## Evidence-card construction rules

- One source and one version per formal card. Update the existing card instead of creating a parallel duplicate.
- Begin with one current research or use question and one intended decision. Do not write a card with only a broad topic.
- Original research keeps the formal eight-part initial-reading structure and a top three-minute judgment layer. Non-paper sources use their own evidence mechanism and do not inherit the paper structure.
- Create only the Cxx blocks needed for decisive claims. One Cxx expresses one falsifiable proposition.
- For every Cxx record the source fact, evidence origin, exact scope, value and uncertainty when applicable, locator with context, permitted inference, direct support, non-support, source interpretation, analyst judgment, dependency, conflict, and check state.
- State the true independent unit. Grid cells, timesteps, repeated measurements, reports from one dataset, and multiple pages from one authority are not automatically independent evidence.
- Separate descriptive, comparative, associative, causal, predictive, mechanistic, normative, implementation, and transfer claims. Never upgrade the inference type.
- A reporting checklist can reveal missing reporting; it does not prove methodological quality.
- A source's official status can support a clause, release, version, or record. It does not automatically prove scientific validity or fitness for the current task.
- Data existence, accessibility, quality, licence, and fitness are separate claims.
- Software discovery, availability, installation, project tests, example execution, target execution, paper replication, and independent scientific validation are separate states.
- Preserve population, basin, station, event, period, scale, sample unit, denominator, unit, uncertainty, comparison conditions, and modal qualifiers.
- Use 原文未报告（已查：…）, 未取得, 未阅读, 无法辨认, 不适用（原因）, or 冲突待核 precisely. Never fill gaps from general knowledge or a similar source.
- Do not create formal topics, innovations, opportunities, or scientific conclusions merely because the card is complete.

## Dynamic reading gate

Open supplementary material, code, additional tables, or upstream sources only when all three are true:

1. a clear high-impact decision exists;
2. a decisive gap is precisely located;
3. the new material may realistically change the judgment.

Then follow the minimum evidence path and stop at the stated stop condition. A valid result can be “still insufficient.”

## Manual scientific review

After structural validation, reopen each decisive locator and ask:

1. Is the source and version the one named in the card?
2. Does the quoted or paraphrased fact preserve direction, unit, denominator, comparison, uncertainty, and qualifier?
3. Did the design actually permit the claimed inference?
4. Are training, calibration, validation, test, comparator, and operational information separated?
5. Are negative results, failure settings, internal conflicts, and unsupported transfer visible?
6. Are source fact, source interpretation, faithful synthesis, and analyst judgment separate?
7. Does the use verdict state what the card can and cannot support?
8. Would a reasonable change in an omitted boundary reverse the decision? If yes, the card is not complete.

A PASS from the script is structural only.

## Output contract

Return one Markdown file per source. Use a stable, filesystem-safe name such as EC-20260904-001_Short_Title.md. Include the Zotero item key, exact source version, reading scope, source provenance, and direct-source verification state in frontmatter.

For a bounded batch, also write a manifest with requested scope, matched Zotero keys, output paths, card types, source versions, reading coverage, validation result, and unresolved blockers. Never expand a batch beyond the user's explicit collection or item list.

Store bibliographic identity and allowed links in Git. Keep licensed full text, Zotero databases, credentials, temporary extracts, restricted project files, and large data in their authorized systems.
