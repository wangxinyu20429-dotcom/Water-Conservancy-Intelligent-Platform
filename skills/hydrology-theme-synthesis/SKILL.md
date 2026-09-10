---
name: hydrology-theme-synthesis
description: Run a traceable hydrology literature-to-theme workflow through small-sample deep reading or large-corpus discovery, select key full texts, admit source-checked Claims, build a deep research-theme dossier, and drive evidence, corpus, or discovery-model feedback. Use for candidate-direction discovery, evidence-card-to-theme synthesis, key-literature triage, topic-trend interpretation, or theme-driven recalculation. Do not use to invent facts, auto-create formal ideas, or treat bibliometric signals as scientific credibility.
---

# Hydrology Theme Synthesis V1.2

Run a traceable route from a frozen hydrology question to candidate directions and key full texts, then turn source-checked evidence-card Claims into a research theme that supports literature review, research-question refinement, later idea discovery, and academic writing. The result is a living synthesis with explicit feedback and recalculation, not a keyword cluster or a second copy of source facts.

The invariant chain is:

Research question and boundary → small-sample or large-corpus route → candidate-direction discovery and human boundary review → theme-level resource allocation → within-theme full-text queue → evidence card → admissible Claim → comparable evidence frame → deep theme synthesis → bounded insight → source, corpus or discovery-model feedback → affected-stage rerun → human and mentor decision.

## Required reading order

1. Read the active repository rules and any theme-governance files they require.
2. Read `references/discovery-workflow.md` and select the route before ranking literature.
3. Read `references/theme-science.md`.
4. Read `references/priority-and-feedback.md`.
5. Read `references/execution.md`.
6. For a deep theme dossier, read `references/deep-narrative.md` before drafting prose.
7. Create a run ledger with `scripts/init_workflow_run.py`, then update it as each stage completes.
8. Read every input evidence card and any referenced Decision/Synthesis cards. Do not rely on a generated manifest without opening the decisive claims.
9. Copy `assets/theme-template.md` or run `scripts/build_theme.py` to create a draft dossier after key full texts have evidence cards.
10. Complete the scientific narrative, structured synthesis and all three feedback routes.
11. Run `scripts/validate_workflow_run.py` and `scripts/validate_theme.py` in draft mode while working and final mode before handoff. Run `scripts/validate_theme_batch.py` when producing more than one theme.
12. Reopen every load-bearing locator and complete the manual scientific review. A validator PASS is structural only.

When a feedback request requires opening Zotero full text, correcting a Claim, or raising a card from L1 to L2/L3, use the installed `hydrology-evidence-cards` workflow and its source-checking rules. Apply changes to the original source card, keep Git history, and regenerate the affected theme sections.

## Non-negotiable scientific boundaries

- A theme is a durable research problem with a stated scope, evidence structure, current knowledge, active unknowns, and continuing use. It is not a method name, dataset, region, journal, year band, task label, or repeated keyword.
- Only source-checked L2/L3 Claim objects may support a theme synthesis statement. L0/L1, abstracts, machine extraction, and unchecked paraphrases may guide search but cannot support the conclusion.
- Each synthesis statement must cite included `claim_id` values and state what those claims do and do not support.
- Do not count papers. Group shared data, station networks, projects, model families, preprint/publication pairs, reports of the same study, and superseded versions before comparing support.
- Record disagreement only after checking that the water object, region, period, event/scenario, intervention or exposure, comparator, outcome/metric, scale, and information set are sufficiently aligned. Different contexts usually indicate heterogeneity or transfer limits, not contradiction.
- Preserve negative results, failure settings, uncertainty, missing evidence, and evidence that weakens the preferred interpretation.
- Separate source facts, author interpretations, analyst synthesis, human review, and mentor decisions.
- A topic cluster or trend is a discovery object. It cannot enter a scientific conclusion until key full texts produce admissible Claims.
- Topic growth is a theme-level corpus signal. Do not copy it onto individual papers or use it as evidence quality.
- Field-year normalized citations and journal position may order reading. They do not admit Claims or change certainty.
- Do not declare novelty, a formal idea, a proposal topic, or a causal mechanism merely because a gap appears in the current card set.
- Do not create or activate a formal theme, change its boundary, split, merge, rename, or archive it unless the active project rules and authorized human decision permit that action. A draft dossier or candidate signal is not a formal lifecycle decision.

## Deep narrative requirement

The default deliverable is a deep theme dossier. Its marked visible scientific narrative must contain at least 10,000 non-whitespace Chinese/Latin characters after frontmatter, folded blocks, code, audit structures, headings, tables and link targets are removed. The threshold is a completeness floor, not a writing target.

- Set `narrative_status: in_progress` while evidence is insufficient or prose is incomplete. Set `ready_for_handoff` only after the validator reports at least 10,000 visible scientific characters.
- Do not satisfy the floor with bibliographic inventories, repeated source summaries, boilerplate, machine fields, long quotations, generic limitations or rephrased copies of the same point.
- A deep narrative must make the research direction intelligible: define the problem chain, organize the evidence landscape, compare data and measurement, compare method families, explain what the current sources found, trace development, distinguish heterogeneity from conflict, derive bounded independent insights, identify disconfirming evidence, and convert gaps into exact source-recheck requests.
- Each independent insight must show its source premises, reasoning step, strongest permitted conclusion, transfer boundary, and what observation would weaken or overturn it. Analytical originality comes from comparison and inference discipline; it does not authorize invented facts or novelty claims.
- L0/L1 material may be described only as an initial-reading map. It must not be worded as confirmed consensus. Only admitted L2/L3 Claims may carry a formal theme conclusion.
- If the source set cannot support 10,000 substantive characters, stop at `BLOCKED_SOURCE_LIMIT`, name what evidence is missing, and leave `narrative_status: in_progress`. Never pad the text.

## Workflow

### 1. Freeze the research task and create the run ledger

Record the research question, intended use, time and spatial scope, water objects, languages, source types, inclusion and exclusion rules, as-of date and allowed conclusion level. Create one run ledger from `assets/workflow-run-template.md`. The ledger records which route was chosen, why, the candidate directions, priority decisions, full-text queue, three feedback types, reruns and mentor decision.

### 2. Select and execute the discovery route

Use `small_sample` when the user already has a bounded Zotero collection, full texts or evidence cards. Verify metadata, DOI, manifestation and readable full text; form only preliminary groups from titles and abstracts. Do not calculate topic growth without adequate time slices and denominators.

Use `large_corpus` for hundreds to hundreds of thousands of records. Preserve the retrieval and exclusion funnel; normalize titles and abstracts; separate LLM entity extraction, deterministic rules, topic modeling and trend statistics; test topic stability; and send only human-reviewed candidate directions onward. Follow `references/discovery-workflow.md`. If required corpus tools or data are unavailable, record the blocked stage instead of simulating a DTM result.

Use `hybrid` only when a large-corpus map and a bounded expert-selected Zotero set are both real inputs. Record which output came from which route.

### 3. Review candidate directions and allocate reading resources

Human review removes false clusters, distinguishes research themes from search facets, writes the candidate boundary and records unstable items. First allocate full-text reading resources across themes using question relevance, topic trend, stability, corpus coverage and basin or object gaps. Then rank documents within each theme using question directness, decisive-gap value, expected scientific role, recency, field-year normalized citation signal and verified field-year journal signal.

Do not create a discovery-stage composite score unless a registered pilot, sensitivity analysis and mentor-frozen weights exist. Preserve component values, source, unknown/not-applicable state and a plain-language reason. Hu et al. did not provide a composite reading-priority formula.

### 4. Freeze the synthesis question and input snapshot

Write the current research question, intended use, target water context, as-of date, included card paths, card versions, and input hashes or Git revisions. Search for an existing theme and compare its question and boundary before proposing a new one. Never assign a formal ID automatically.

### 5. Build the admissibility ledger

For every card, register the exact source manifestation, artifact type, publication year, evidence roles, completion level, reading scope, version family, and independence groups. Classify each Claim as `included`, `context_only`, `excluded`, or `feedback_needed`. Only L2/L3 source-checked claims may be `included`. Give an explicit reason for every exclusion. Unknown means unknown; do not infer it from the title, journal, or neighbouring papers.

### 6. Compare claims within a common frame

Build comparison frames around the scientific question rather than vocabulary. At minimum align the water object, independent unit, place, period, event/scenario, exposure or method, information set, comparator, outcome/metric, denominator, uncertainty, validation design, scale, and transfer conditions. Split a frame when a difference changes the meaning of the result. Do not average or rank incompatible results.

### 7. Propose candidate theme structure

Write a one-sentence theme argument and one or more active questions. Test the literature, direction and use basis; problem coherence; explainable boundary; evidence organization; independent judgment; and continuing value in `references/theme-science.md`. Prefer an active question or comparison dimension before creating a subtheme. Record split or merge suggestions for human review.

### 8. Synthesize the knowledge state

For each statement, record its proposition, wording strength, knowledge state, supporting/limiting/opposing Claim IDs, independence/version groups, comparison frame, transfer boundary, six-dimensional evidence profile, strongest permissible conclusion, and unsupported remainder. Describe development by changes in questions, data, methods, validation and applicability, not by year alone.

Before filling the machine ledger, write the human-readable scientific narrative inside the template markers. Use evidence-card IDs at the paragraph where a source is interpreted. The structured blocks audit the narrative; they do not replace it.

### 9. Rank post-card recheck attention separately

After evidence cards exist, identify each source's `scientific_role`, then calculate `frontier_attention_score` for source recheck and frontier tracking using `references/priority-and-feedback.md`. This E25/D20/G15/R25/V15 formula is different from candidate discovery. Citation and topic growth do not enter it. Recency and a verified field-normalized journal signal together carry 40% of this attention score. They never change verification status, evidence certainty, or Claim truth.

Preserve older foundational work and long-term records with a reasoned exception. Mark journal metric `not_applicable` for non-journal sources and renormalize applicable weights. Mark missing metrics `unknown`; never guess or treat unknown as low impact.

### 10. Generate one of three feedback types

Use `source_recheck` when a specific source locator, Claim, version, method or result may change the theme; it must name the original card, affected Claims, smallest source material and stop condition. Use `corpus_supplement` when missing regions, periods, languages, source types, methods or evidence roles require a new retrieval record. Use `discovery_model_correction` when an LLM, dictionary, rule, geocoder or topic model shows systematic error; record the affected stage, configuration and human validation sample.

A generated request is `proposed` and cannot alter the card, corpus or model output. Mark it `applied` only after performing the stated check or change and recording what downstream objects must be recomputed.

### 11. Recalculate and preserve the audit trail

After an original card changes, update the input snapshot, rerun admissibility and recheck priority, and revise affected statements. After corpus supplementation, rerun deduplication, extraction, candidate directions, trend and full-text queues. After discovery-model correction, rerun the affected extraction, clustering, trend and human classification stages. Record before/after meaning. If new evidence overturns a load-bearing statement, lower the theme status and stop downstream strong claims until reviewed.

### 12. Prepare the writing and idea interface

List which statements may support background, review, problem framing, method choice or limitations. Opportunity signals require evidence basis, nearest known work in the current set, missing novelty search, disconfirming evidence, feasibility dependencies and next verification. Keep them as signals until a separate workflow and human decision promote them.

### 13. Hand off for human and mentor review

Present the argument, scope, important sources and reasons, load-bearing gaps, proposed card repairs and decisions required. AI may draft and revise. A human confirms source fidelity; the mentor decides formal lifecycle and research direction under active project rules.

## Priority formula

Use 0–4 components: evidence quality and independence E=25%, question directness D=20%, decisive-gap closure G=15%, recency R=25%, and verified field-normalized journal signal V=15%.

`frontier_attention_score = 25*E/4 + 20*D/4 + 15*G/4 + 25*R/4 + 15*V/4`.

If a component is legitimately not applicable, remove its weight and renormalize remaining applicable weights to 100. If unknown, report a provisional range and `ranking_completeness`; never silently substitute zero. This score answers what to inspect first, not which result is true.

## Output contract

Produce one workflow run ledger from `assets/workflow-run-template.md` whenever the task includes route selection, candidate discovery or key-full-text selection. Produce one theme dossier from `assets/theme-template.md` after evidence cards exist. The dossier contains a marked deep scientific narrative, input/admissibility manifest, post-card literature-priority ledger, feedback ledger, writing/idea-readiness interface and validation record. Use one formal Markdown per object as its source of truth; dashboards and graphs remain derived views.

## Commands

Create a workflow run:

~~~text
python scripts/init_workflow_run.py --workflow-ref run:20260910-flood --title "洪涝研究方向发现与主题深化" --question "极端洪涝研究中哪些方向值得进入全文证据审查？" --intended-use "候选方向发现和主题形成" --route hybrid --output 运行记录/20260910_洪涝工作流.md
python scripts/validate_workflow_run.py 运行记录/20260910_洪涝工作流.md --mode draft
~~~

Create a draft:

~~~text
python scripts/build_theme.py --theme-ref draft:flood-chain --title "极端洪涝灾害链" --card path/to/EC-001.md --card path/to/EC-002.md --output path/to/theme.md
~~~

Validate:

~~~text
python scripts/validate_theme.py path/to/theme.md --mode draft --index-root path/to/vault
python scripts/validate_theme.py path/to/theme.md --mode final --index-root path/to/vault
~~~

Validate the workflow before mentor handoff:

~~~text
python scripts/validate_workflow_run.py path/to/workflow-run.md --mode final
~~~

Final PASS means only that encoded structure and provenance rules passed. It does not prove topic-model validity, source fidelity, scientific correctness, novelty, or mentor approval.
