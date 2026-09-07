---
name: hydrology-theme-synthesis
description: Synthesize one or more hydrology evidence cards into a source-traceable research-theme dossier, rank frontier-reading priorities with bounded recency and journal-metric signals, and issue source-bound requests to recheck and improve the original cards. Use for evidence-card-to-theme synthesis, theme frontier mapping, key-literature triage, or theme-driven card feedback. Do not use to invent facts, auto-create formal research ideas, or treat journal metrics as article-level scientific credibility.
---

# Hydrology Theme Synthesis V1.0

Turn verified evidence-card claims into a research theme that can support literature review, research-question refinement, later idea discovery, and academic writing. The result is a living synthesis with an explicit feedback loop, not a keyword cluster or a second copy of source facts.

The invariant chain is:

Evidence-card version → admissible Claim → comparable evidence frame → theme synthesis → literature attention priority → targeted source recheck → original-card revision → theme recalculation → human and mentor decision.

## Required reading order

1. Read the active repository rules and any theme-governance files they require.
2. Read `references/theme-science.md`.
3. Read `references/priority-and-feedback.md`.
4. Read `references/execution.md`.
5. Read every input evidence card and any referenced Decision/Synthesis cards. Do not rely on a generated manifest without opening the decisive claims.
6. Copy `assets/theme-template.md` or run `scripts/build_theme.py` to create a draft dossier.
7. Complete the scientific synthesis and feedback ledger.
8. Run `scripts/validate_theme.py` in draft mode while working and final mode before handoff.
9. Reopen every load-bearing locator and complete the manual scientific review. A validator PASS is structural only.

When a feedback request requires opening Zotero full text, correcting a Claim, or raising a card from L1 to L2/L3, use the installed `hydrology-evidence-cards` workflow and its source-checking rules. Apply changes to the original source card, keep Git history, and regenerate the affected theme sections.

## Non-negotiable scientific boundaries

- A theme is a durable research problem with a stated scope, evidence structure, current knowledge, active unknowns, and continuing use. It is not a method name, dataset, region, journal, year band, task label, or repeated keyword.
- Only source-checked L2/L3 Claim objects may support a theme synthesis statement. L0/L1, abstracts, machine extraction, and unchecked paraphrases may guide search but cannot support the conclusion.
- Each synthesis statement must cite included `claim_id` values and state what those claims do and do not support.
- Do not count papers. Group shared data, station networks, projects, model families, preprint/publication pairs, reports of the same study, and superseded versions before comparing support.
- Record disagreement only after checking that the water object, region, period, event/scenario, intervention or exposure, comparator, outcome/metric, scale, and information set are sufficiently aligned. Different contexts usually indicate heterogeneity or transfer limits, not contradiction.
- Preserve negative results, failure settings, uncertainty, missing evidence, and evidence that weakens the preferred interpretation.
- Separate source facts, author interpretations, analyst synthesis, human review, and mentor decisions.
- Do not declare novelty, a formal idea, a proposal topic, or a causal mechanism merely because a gap appears in the current card set.
- Do not create or activate a formal theme, change its boundary, split, merge, rename, or archive it unless the active project rules and authorized human decision permit that action. A draft dossier or candidate signal is not a formal lifecycle decision.

## Workflow

### 1. Freeze the synthesis question and input snapshot

Write the current research question, intended use, target water context, as-of date, included card paths, card versions, and input hashes or Git revisions. Search for an existing theme and compare its question and boundary before proposing a new one. Never assign a formal ID automatically.

### 2. Build the admissibility ledger

For every card, register the exact source manifestation, artifact type, publication year, evidence roles, completion level, reading scope, version family, and independence groups. Classify each Claim as `included`, `context_only`, `excluded`, or `feedback_needed`. Only L2/L3 source-checked claims may be `included`. Give an explicit reason for every exclusion. Unknown means unknown; do not infer it from the title, journal, or neighbouring papers.

### 3. Compare claims within a common frame

Build comparison frames around the scientific question rather than vocabulary. At minimum align the water object, independent unit, place, period, event/scenario, exposure or method, information set, comparator, outcome/metric, denominator, uncertainty, validation design, scale, and transfer conditions. Split a frame when a difference changes the meaning of the result. Do not average or rank incompatible results.

### 4. Propose candidate theme structure

Write a one-sentence theme argument and one or more active questions. Test the literature, direction and use basis; problem coherence; explainable boundary; evidence organization; independent judgment; and continuing value in `references/theme-science.md`. Prefer an active question or comparison dimension before creating a subtheme. Record split or merge suggestions for human review.

### 5. Synthesize the knowledge state

For each statement, record its proposition, wording strength, knowledge state, supporting/limiting/opposing Claim IDs, independence/version groups, comparison frame, transfer boundary, six-dimensional evidence profile, strongest permissible conclusion, and unsupported remainder. Describe development by changes in questions, data, methods, validation and applicability, not by year alone.

### 6. Rank important literature on two separate axes

Identify each source's `scientific_role`, then calculate `frontier_attention_score` for reading and update priority using `references/priority-and-feedback.md`. Recency and a verified field-normalized journal signal together carry 40% of this attention score. They never change verification status, evidence certainty, or Claim truth.

Preserve older foundational work and long-term records with a reasoned exception. Mark journal metric `not_applicable` for non-journal sources and renormalize applicable weights. Mark missing metrics `unknown`; never guess or treat unknown as low impact.

### 7. Generate source-bound feedback requests

Each request names the original card and Claim, exact problem, theme consequence, smallest source material, allowed action, possible result, stop condition and status. A generated request is `proposed` and cannot alter the card. Mark `applied` only after checking the exact source, changing the original card and recording changed Claim IDs.

### 8. Recalculate and preserve the audit trail

After an original card changes, update the input snapshot, rerun admissibility and priority calculations, and revise only affected statements. Record before/after meaning. If new evidence overturns a load-bearing statement, lower the theme status and stop downstream strong claims until reviewed.

### 9. Prepare the writing and idea interface

List which statements may support background, review, problem framing, method choice or limitations. Opportunity signals require evidence basis, nearest known work in the current set, missing novelty search, disconfirming evidence, feasibility dependencies and next verification. Keep them as signals until a separate workflow and human decision promote them.

### 10. Hand off for human and mentor review

Present the argument, scope, important sources and reasons, load-bearing gaps, proposed card repairs and decisions required. AI may draft and revise. A human confirms source fidelity; the mentor decides formal lifecycle and research direction under active project rules.

## Priority formula

Use 0–4 components: evidence quality and independence E=25%, question directness D=20%, decisive-gap closure G=15%, recency R=25%, and verified field-normalized journal signal V=15%.

`frontier_attention_score = 25*E/4 + 20*D/4 + 15*G/4 + 25*R/4 + 15*V/4`.

If a component is legitimately not applicable, remove its weight and renormalize remaining applicable weights to 100. If unknown, report a provisional range and `ranking_completeness`; never silently substitute zero. This score answers what to inspect first, not which result is true.

## Output contract

Produce one theme dossier from `assets/theme-template.md`, containing its input/admissibility manifest, literature-priority ledger, card-feedback ledger, writing/idea-readiness interface and validation record. Use one formal Markdown as the theme source of truth; dashboards and graphs remain derived views.

## Commands

Create a draft:

~~~text
python scripts/build_theme.py --theme-ref draft:flood-chain --title "极端洪涝灾害链" --card path/to/EC-001.md --card path/to/EC-002.md --output path/to/theme.md
~~~

Validate:

~~~text
python scripts/validate_theme.py path/to/theme.md --mode draft --index-root path/to/vault
python scripts/validate_theme.py path/to/theme.md --mode final --index-root path/to/vault
~~~

Final PASS means only that encoded structure and provenance rules passed. It does not replace source review, expert synthesis, novelty search, or mentor confirmation.
