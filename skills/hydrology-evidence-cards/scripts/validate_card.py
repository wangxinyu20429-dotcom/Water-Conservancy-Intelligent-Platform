#!/usr/bin/env python3
"""Validate evidence-card structure without claiming scientific correctness."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

COMMON_FRONTMATTER = [
    "card_schema",
    "card_id",
    "evidence_type",
    "status",
    "zotero_item_key",
    "source_version",
    "reading_scope",
    "source_provenance",
    "direct_source_verified",
]

SPECIFIC_HEADINGS = {
    "original-research": [
        "导师快速判断稿",
        "初读卡片（3—5分钟）",
        "完整证据档案",
        "一、文献身份与证据状态",
        "二、研究背景、知识缺口与研究问题",
        "三、研究对象、尺度与适用范围",
        "四、数据、方法与验证设计",
        "五、主要结果与差异、失败情景",
        "六、作者声称、实际新增与平台初步判断",
        "七、文献价值、主题关联及关联理由",
        "八、适用边界、局限、待核验问题与后续阅读提示",
        "本卡收口",
    ],
    "review-synthesis": [
        "导师三分钟判断",
        "来源身份与阅读边界",
        "证据综合如何形成",
        "决定性证据块",
        "关键原始研究追踪",
        "本方使用边界",
    ],
    "survey-monitoring-statistics": [
        "导师三分钟判断",
        "来源身份与阅读边界",
        "统计证据如何产生",
        "决定性证据块",
        "可比性与变化归因",
        "本方使用边界",
    ],
    "engineering-report": [
        "导师三分钟判断",
        "来源身份与阅读边界",
        "工程证据如何产生",
        "决定性证据块",
        "局限、失效与迁移性",
        "本方使用边界",
    ],
    "book-chapter": [
        "导师三分钟判断",
        "来源身份与阅读边界",
        "知识与论证如何形成",
        "决定性证据块",
        "原始来源谱系",
        "本方使用边界",
    ],
    "standard-guideline-policy": [
        "导师三分钟判断",
        "来源身份与阅读边界",
        "规范证据如何形成",
        "决定性证据块",
        "本方使用边界",
    ],
    "dataset-data-product": [
        "导师三分钟判断",
        "来源身份与阅读边界",
        "数据证据如何产生",
        "决定性证据块",
        "任务适用性检验",
        "本方使用边界",
    ],
    "software-model-code": [
        "导师三分钟判断",
        "来源身份与阅读边界",
        "软件与模型证据如何产生",
        "决定性证据块",
        "状态证据表",
        "本方使用边界",
    ],
}

CLAIM_LABEL_GROUPS = [
    ("source fact", ["原文事实", "原文综合结果", "原文统计事实", "原文条款或事实", "原文或实查事实", "原文事实或命题"]),
    ("evidence origin", ["证据来源", "证据基础", "数据来源与估计过程", "证据层与产生方式", "论证或证据来源", "来源组件", "数据生成或检查依据", "证据产生方式"]),
    ("scope", ["精确范围", "总体、地域、时期、尺度和口径", "工程对象、位置、时段和系统边界", "前提、符号、单位和适用域", "适用主体、对象、地域、时期和条件", "对象、变量、时空范围、分辨率和单位", "输入、输出、配置、环境和适用范围"]),
    ("locator", ["精确定位"]),
    ("direct support", ["直接支持"]),
    ("non-support", ["不能支持"]),
    ("analyst judgment", ["本方判断", "本方适用性判断"]),
    ("check state", ["核查状态"]),
]


def frontmatter_value(text: str, key: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*[\"']?([^\n\"']+)", text)
    return match.group(1).strip() if match else None


def claim_blocks(text: str) -> list[str]:
    starts = list(re.finditer(r"(?m)^###\s+C\d{2}\b.*$", text))
    blocks: list[str] = []
    for i, start in enumerate(starts):
        end = starts[i + 1].start() if i + 1 < len(starts) else len(text)
        blocks.append(text[start.start():end])
    return blocks


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("card")
    parser.add_argument("--mode", choices=["draft", "final"], default="draft")
    args = parser.parse_args()

    path = Path(args.card)
    text = path.read_text(encoding="utf-8-sig")
    evidence_type = frontmatter_value(text, "evidence_type")
    errors: list[str] = []
    warnings: list[str] = []

    if evidence_type not in SPECIFIC_HEADINGS:
        errors.append(f"unknown or missing evidence_type: {evidence_type}")

    for key in COMMON_FRONTMATTER:
        if not frontmatter_value(text, key):
            errors.append(f"missing frontmatter field: {key}")

    for heading in SPECIFIC_HEADINGS.get(evidence_type or "", []):
        if heading not in text:
            errors.append(f"missing required section: {heading}")

    blocks = claim_blocks(text)
    if not blocks:
        errors.append("no Cxx decisive claim block found")
    else:
        for index, block in enumerate(blocks, start=1):
            for label, alternatives in CLAIM_LABEL_GROUPS:
                if not any(item in block for item in alternatives):
                    errors.append(f"C{index:02d} missing {label}")

    if not any(verdict in text for verdict in [
        "可直接使用", "限条件使用", "仅作线索", "暂不可用", "与当前问题无关"
    ]):
        errors.append("missing defined use verdict")

    if "动态精读三门判定" not in text and "补读资格门与最小路径" not in text and "补读／取数资格门与最小路径" not in text and "补读／运行资格门与最小路径" not in text:
        errors.append("missing three-gate follow-up reading decision")

    if args.mode == "final":
        markers = sorted(set(re.findall(r"\{\{[^}]+\}\}|〔[^〕]+〕|待填写", text)))
        if markers:
            errors.append("unresolved template markers: " + ", ".join(markers[:10]))
        if frontmatter_value(text, "status") in {"draft", "template", "模板", "待填写"}:
            errors.append("final card still has draft/template status")
        if frontmatter_value(text, "source_version") in {"unknown", "unverified", "待核对", "待绑定"}:
            errors.append("final card does not bind a source version")
        if frontmatter_value(text, "reading_scope") in {"metadata_only", "unknown", "未填写", "待填写"}:
            errors.append("final card does not declare substantive reading scope")
        if frontmatter_value(text, "direct_source_verified") != "true":
            errors.append("final card does not declare direct-source verification")


    print(f"card: {path}")
    print(f"type: {evidence_type}")
    print(f"decisive_claim_blocks: {len(blocks)}")
    for item in warnings:
        print(f"WARNING: {item}")
    for item in errors:
        print(f"ERROR: {item}")
    if errors:
        raise SystemExit(1)
    print("PASS: structural evidence-chain checks completed; scientific accuracy still requires source review")


if __name__ == "__main__":
    main()
