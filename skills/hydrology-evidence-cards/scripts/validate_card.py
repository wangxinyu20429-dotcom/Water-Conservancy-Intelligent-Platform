#!/usr/bin/env python3
"""Validate an evidence card's structure and unresolved drafting markers."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

COMMON = [
    "来源身份",
    "材料与阅读范围",
    "研究或使用问题",
    "声明—原文证据对应表",
    "局限",
    "本方使用边界",
    "复查与变更",
]

SPECIFIC = {
    "original-research": ["研究设计", "数据、方法与验证", "主要结果"],
    "review-synthesis": ["检索与筛选", "质量或偏倚评估", "综合方法与结果"],
    "survey-monitoring-statistics": ["总体、抽样与监测设计", "统计口径与数据处理", "主要统计发现"],
    "engineering-report": ["工程阶段、目标与约束", "方案、计算与实施", "效果、验收与运行证据"],
    "book-chapter": ["概念、理论与推导", "证据来源与引文谱系", "方法、例题与适用域"],
    "standard-guideline-policy": ["效力、范围与版本", "规范性条款与要求", "符合性证据与例外"],
    "dataset-data-product": ["覆盖、变量与结构", "生成、处理与质量控制", "偏差、许可与适用性"],
    "software-model-code": ["功能、输入输出与假设", "版本、环境与实现关系", "测试、运行与科学验证边界"],
}


def frontmatter_value(text: str, key: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*[\"']?([^\n\"']+)", text)
    return match.group(1).strip() if match else None


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("card")
    p.add_argument("--mode", choices=["draft", "final"], default="draft")
    args = p.parse_args()
    path = Path(args.card)
    text = path.read_text(encoding="utf-8")
    evidence_type = frontmatter_value(text, "evidence_type")
    errors: list[str] = []
    warnings: list[str] = []
    if evidence_type not in SPECIFIC:
        errors.append(f"unknown or missing evidence_type: {evidence_type}")
    for heading in COMMON + SPECIFIC.get(evidence_type or "", []):
        if heading not in text:
            errors.append(f"missing required section: {heading}")
    for key in ["card_id", "zotero_item_key", "source_version", "reading_scope", "status"]:
        if not frontmatter_value(text, key):
            errors.append(f"missing frontmatter field: {key}")
    if "| C01" not in text and "| C1" not in text:
        warnings.append("no C01 claim row found")
    if args.mode == "final":
        markers = sorted(set(re.findall(r"\{\{[^}]+\}\}|〔[^〕]+〕|待填写", text)))
        if markers:
            errors.append("unresolved template markers: " + ", ".join(markers[:10]))
        if frontmatter_value(text, "status") in {"draft", "模板", "待填写"}:
            errors.append("final card still has draft status")
        if frontmatter_value(text, "reading_scope") in {"未填写", "待填写", "unknown"}:
            errors.append("final card does not declare actual reading scope")
    print(f"card: {path}")
    print(f"type: {evidence_type}")
    for item in warnings:
        print(f"WARNING: {item}")
    for item in errors:
        print(f"ERROR: {item}")
    if errors:
        raise SystemExit(1)
    print("PASS: structural checks completed; scientific accuracy still requires source review")


if __name__ == "__main__":
    main()
