# Human-readable scientific core V1.4

This contract controls the visible part of every source card. It exists to prevent a structurally valid card from being scientifically empty.

## Common opening

Start with a one-sentence takeaway that identifies the object, the action taken by the source, the main result or output, and the largest boundary. Follow it with a short “先看结论” block that answers: what was studied, what data were used, how the study worked, what it found, and why the present project should care.

## Original empirical or modelling research

Use these visible sections in this order:

1. `研究要解决什么问题` — practical/scientific problem, author's gap, explicit question or hypothesis, and novelty claimed by the source.
2. `研究对象与边界` — water object/system, site, event/scenario, time span, scale, independent unit and comparator.
3. `数据到底是什么` — a compact table with source/acquisition, period, sample, resolution, variables/outcomes, preprocessing, calibration/validation/test use, and access. Separate observed, derived, simulated and assumed inputs.
4. `方法是怎样一步步得到结果的` — numbered input → model/analysis → coupling/inference → validation/comparison → output steps. Name equations, algorithms or software only after explaining their scientific role.
5. `验证和比较是否站得住` — baseline/comparator, calibration and validation independence, evaluation metrics, sensitivity/uncertainty analysis, negative controls or missing checks.
6. `最关键的结果` — three to five result groups. For each, give the finding, supporting number or qualitative evidence, comparator, uncertainty status, locator, and interpretation. State `no located numeric result` rather than inventing precision.
7. `作者如何解释这些结果` — keep author mechanism explanations separate from measured/simulated facts.
8. `这篇研究真正贡献了什么` — conceptual, data, method and empirical contribution; do not award novelty the paper did not demonstrate.
9. `复现需要什么` — inputs, code/model, parameters, random seeds, environment, expected outputs and acceptance checks; identify unavailable pieces.
10. `对当前水利科研平台的用途` — concrete use in problem framing, variables, design, benchmark or falsification; also state what it cannot support.
11. `结论边界` — design, data, spatial, temporal, measurement, model, inference and transfer limits, tied to affected findings.

Between validation and the final contribution assessment, add `全文证据链展开`. This section is the main depth test. It must explain at least one complete path from a concrete source input to a concrete conclusion, and normally cover: why the chosen data can address the question; how each principal model or analytical stage transforms the data; which parameter, threshold or assumption controls the transition; what comparison, observation or sensitivity analysis checks the output; how the decisive figures/tables relate to the stated result; and which link remains weak. Name the actual variables, modules, study groups, scenarios and outputs. Generic statements that could be copied into another paper do not count.

## Review or evidence synthesis

Replace data/method sections with `综述问题与范围`, `检索与纳入是怎样做的`, `纳入证据由什么构成`, `作者怎样分类或综合`, `最关键的综合结果`, `异质性、偏倚与证据确定性`, `哪些承重结论必须回原始研究核查`, and the common contribution/use/boundary sections. Record databases, final search date, strings, screening flow, included counts, study/data/model overlap and synthesis method when reported. A narrative review with no reproducible search must be labelled as such.

## Government, incident and engineering reports

Use `报告要回答什么`, `事件／工程对象与时间线`, `调查材料和数据来源`, `调查或评估方法`, `已确认事实与关键数字`, `原因／责任／机制结论的证据层级`, `仍未回答的问题`, `对平台的用途`, and `结论边界`. Separate contemporaneous facts, later verified facts, expert judgment, simulated counterfactuals and normative conclusions.

## Standards, guidelines, policy and official web records

Use `文件解决什么治理问题`, `发布机关、版本和适用对象`, `本轮实际读取范围`, `可确认的条款／事实`, `执行或符合性所需证据`, `科学证据边界`, and `后续补核`. A catalog page or announcement with no substantive attachment has no research data, research method or effect result; say this clearly and do not inflate it into a research card.

## Results discipline

- A table row must correspond to one interpretable result, not a keyword.
- Keep denominators: nodes, people, events, grid cells, runs, catchments and papers are not interchangeable.
- Keep time and place attached to numbers.
- Distinguish calibration fit, internal consistency, validation, external validation and operational performance.
- Treat overall accuracy cautiously when classes are imbalanced; report class-specific metrics when available.
- Simulation counts are not independent empirical events.
- Feature importance, correlation and sensitivity are not causal effects.
- “No uncertainty reported” is a substantive finding about evidence precision.

## Depth rule

Depth comes from reconstructing the evidence path, not from word count. A substantive full-text original study normally needs 4,500–7,000 visible Chinese characters for L1 and 6,000–10,000 for L2. A review normally needs at least 3,500 visible characters and enough detail to reproduce its evidence universe and synthesis logic; a substantial investigation report normally needs at least 3,000. Short official notices may be much shorter if the card explicitly states that no data, method or effect result exists. Repetition, generic domain background, raw abstracts and machine fields do not count.

For normal original research, the visible **data**, **method**, **validation**, **results**, and **全文证据链展开** sections should collectively reconstruct the study. Use 500, 700, 350, 800, and 1,000 non-whitespace characters as drafting targets when the source has that much substance. The hard lint floor is lower for each individual section because detailed method and result interpretation may sit in `全文证据链展开`; it additionally requires at least 1,600 characters across the five sections. A shorter section is acceptable only when another named section carries the detail or the card identifies the source-level reason and resulting limitation. Do not satisfy a minimum by repeating the abstract or a stock boundary sentence.

## Final self-check

Before handoff, a reader should be able to point to one visible place for each of these questions: What exactly was studied? On what observations or constructed inputs? What transformations produced the outputs? Against what was it checked? What were the actual results? Which statements are authors' explanations? What would be needed to reproduce it? Where does the conclusion stop? If any answer is missing, state the missing fact and its consequence.
