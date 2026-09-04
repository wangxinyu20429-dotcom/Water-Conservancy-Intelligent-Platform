#!/usr/bin/env python3
"""Create a standalone evidence-card skeleton from a selected template."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from pathlib import Path
from typing import Any

TEMPLATES = {
    "original-research": "01_original-research.md",
    "review-synthesis": "02_review-synthesis.md",
    "survey-monitoring-statistics": "03_survey-monitoring-statistics.md",
    "engineering-report": "04_engineering-report.md",
    "book-chapter": "05_book-chapter.md",
    "standard-guideline-policy": "06_standard-guideline-policy.md",
    "dataset-data-product": "07_dataset-data-product.md",
    "software-model-code": "08_software-model-code.md",
}


def item_data(path: str | None) -> dict[str, Any]:
    if not path:
        return {}
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    if isinstance(raw, list):
        if len(raw) != 1:
            raise SystemExit("--item-json must contain exactly one Zotero item")
        raw = raw[0]
    return raw.get("data", raw)


def creators_text(data: dict[str, Any]) -> str:
    names = []
    for creator in data.get("creators", []):
        name = creator.get("name") or " ".join(
            x for x in [creator.get("firstName"), creator.get("lastName")] if x
        )
        if name:
            names.append(name)
    return "; ".join(names)


def safe_filename(value: str) -> str:
    value = re.sub(r'[<>:"/\\|?*]+', "_", value).strip(" ._")
    return value[:90] or "Untitled"


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--type", required=True, choices=sorted(TEMPLATES))
    p.add_argument("--item-json")
    p.add_argument("--title")
    p.add_argument("--zotero-key")
    p.add_argument("--card-id")
    p.add_argument("--output")
    p.add_argument("--overwrite", action="store_true")
    args = p.parse_args()

    data = item_data(args.item_json)
    title = args.title or data.get("title") or "待填写来源题名"
    key = args.zotero_key or data.get("key") or "待绑定"
    card_id = args.card_id or f"EC-{dt.date.today():%Y%m%d}-待编号"
    template = Path(__file__).resolve().parent.parent / "assets" / "templates" / TEMPLATES[args.type]
    text = template.read_text(encoding="utf-8")
    replacements = {
        "{{CARD_ID}}": card_id,
        "{{TITLE}}": title,
        "{{ZOTERO_KEY}}": str(key),
        "{{CREATORS}}": creators_text(data) or "待核对",
        "{{DATE}}": str(data.get("date") or "待核对"),
        "{{DOI}}": str(data.get("DOI") or "未填写"),
        "{{URL}}": str(data.get("url") or "未填写"),
        "{{CREATED_AT}}": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    output = Path(args.output or f"{card_id}_{safe_filename(title)}.md").expanduser().resolve()
    if output.exists() and not args.overwrite:
        raise SystemExit(f"Refusing to overwrite existing file: {output}")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(text, encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()

