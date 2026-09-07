# 文献优先级与证据卡反馈

## 1. 两个轴

`scientific_role`说明来源在主题论证中的作用；`frontier_attention_score`决定先读、先补核、先跟踪谁。两者不能合并。

旧论文可以是承重的定义、方法或长期记录；新高影响期刊论文可以优先跟踪，但未核声明不能进入主题结论。

## 2. 科学作用

允许多选：

- `load_bearing_evidence`
- `boundary_or_negative_evidence`
- `foundational_concept_or_method`
- `current_frontier`
- `dataset_or_measurement_basis`
- `implementation_or_engineering`
- `context_only`

每个作用必须连接 Claim IDs，不能由期刊名、年份或被引量单独决定。

## 3. 前沿关注评分

| 分项 | 权重 | 4分含义 | 0分含义 |
| --- | ---: | --- | --- |
| E 证据质量与独立性 | 25% | 声明已核、设计适配、独立性清楚、限制已处理 | 尚无可用证据 |
| D 问题直接性 | 20% | 直接回答核心问题且口径匹配 | 只有关键词关系 |
| G 缺口闭合价值 | 15% | 能改变承重判断、边界或下一步 | 不改变主题 |
| R 新近性 | 25% | 距 as_of_year 不超过2年 | 超过20年且无前沿作用 |
| V 期刊信号 | 15% | 已核同年同学科 JIF 百分位≥90 | 百分位<25 |

`score = 25E/4 + 20D/4 + 15G/4 + 25R/4 + 15V/4`

### R分

0–2年=4；3–5年=3；6–10年=2；11–20年=1；超过20年=0。在线优先与正式卷期跨年时记录选择。奠基研究、定义、历史基线和长序列资料可设置 `foundational_exception`，保留在核心集中，但R仍照实填写。

### V分

优先使用有来源的 JCR 学科内 JIF percentile：≥90=4；75–<90=3；50–<75=2；25–<50=1；<25=0。

只有分区时可降级：Q1=3.5、Q2=2.5、Q3=1.5、Q4=0.5，并写 `metric_resolution: quartile_only`。只有原始JIF而没有学科和年度百分位/分区时不计算V。

评分指标必须记录 `metric_name`、`metric_value`、`metric_year`、`category`、`percentile_or_quartile`、`source`、`checked_at`。无法取得写 `unknown`；非期刊来源写 `not_applicable`，不按低影响处理。

### 缺项

`not_applicable`时移除对应权重并将其余适用权重归一到100。`unknown`时用0和4分别计算区间，报告 `ranking_completeness`，排序标 provisional。不得用精确小数掩盖未知。

同分依次比较 G、D、E、R、V，仍同分则并列。

## 4. 禁止解释

不得因为影响因子高而提高Claim可信度，不得因为年份新而自动推翻旧研究，不得因顶刊免核原文，不得因低影响期刊或非期刊来源而自动降级科学作用。

## 5. 反馈动作

允许动作：

- `targeted_recheck`
- `correct_locator`
- `split_claim`
- `merge_duplicate`
- `add_boundary`
- `add_relation`
- `add_independence_group`
- `update_version`
- `downgrade_verification`
- `request_level_upgrade`

反馈必须同时满足：有明确主题判断；有可定位的决定性缺口；最小新材料可能改变判断。记录 `pre_check_judgment`、`decisive_gap`、`expected_theme_change`、`required_material` 和 `stop_condition`。

## 6. 反馈状态

- `proposed`：发现问题，尚未开源；
- `source_checked`：已核来源，尚未改卡；
- `applied`：已改原卡并登记 changed_claim_ids；
- `rejected`：核查后无需修改或请求越界；
- `blocked`：材料不可得、版本不明或权限受限。

`proposed`不能改变卡片事实。`applied`后必须重新运行证据卡校验和主题综合，不另建“修正版证据卡”。

## 7. 优先顺序

先处理会推翻主题的一语论证、可能把伪冲突改为情境差异、影响单位/方向/因果/预测/迁移、造成重复计数、阻断后续idea或写作的缺口。只增加字数而不改变判断、边界或下一步的请求应停止。
