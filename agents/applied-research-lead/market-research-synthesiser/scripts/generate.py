#!/usr/bin/env python3
"""
generate.py — Synthesise market research findings from multiple sources into an actionable strategy brief.

Usage:
    echo '<json>' | python3 generate.py
    python3 generate.py < input.json
    python3 generate.py < input.json -o output.json

Dependencies: Python 3.10+ standard library only.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

SOURCE_TYPES = ["customer_interviews", "survey", "analyst_report", "competitor_analysis", "desk_research", "usage_data"]
CONFIDENCE_LEVELS = ["high", "medium", "low"]
REQUIRED_FIELDS = ["research_question", "sources"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "sources" in data:
        for src in data["sources"]:
            if "type" not in src or "findings" not in src:
                errors.append("Each source needs 'type' and 'findings' fields")
            if "type" in src and src["type"] not in SOURCE_TYPES:
                errors.append(f"Source type must be one of {SOURCE_TYPES}")
    return errors


def synthesise_research(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    sources = data["sources"]
    all_findings = []
    source_summary = []

    for src in sources:
        source_summary.append({
            "type": src["type"],
            "sample_size": src.get("sample_size"),
            "findings_count": len(src["findings"]),
        })
        for finding in src["findings"]:
            all_findings.append({
                "finding": finding,
                "source_type": src["type"],
                "confidence": src.get("confidence", "medium"),
            })

    # Group findings by confidence
    high_conf = [f for f in all_findings if f["confidence"] == "high"]
    medium_conf = [f for f in all_findings if f["confidence"] == "medium"]
    low_conf = [f for f in all_findings if f["confidence"] == "low"]

    # Source diversity score
    unique_types = len(set(s["type"] for s in sources))
    if unique_types >= 3:
        source_diversity = "strong"
    elif unique_types == 2:
        source_diversity = "moderate"
    else:
        source_diversity = "weak — findings from single source type carry high confirmation bias risk"

    return {
        "error": None,
        "result": {
            "research_question": data["research_question"],
            "synthesis_date": data.get("synthesis_date", "2026-03-31"),
            "total_sources": len(sources),
            "total_findings": len(all_findings),
            "source_diversity": source_diversity,
            "source_summary": source_summary,
            "high_confidence_findings": [f["finding"] for f in high_conf],
            "medium_confidence_findings": [f["finding"] for f in medium_conf],
            "low_confidence_findings": [f["finding"] for f in low_conf],
            "strategic_implications": data.get("strategic_implications", []),
            "open_questions": data.get("open_questions", []),
            "recommended_actions": data.get("recommended_actions", []),
            "confidence_caveats": [
                "Low confidence findings should not drive major product decisions without additional validation",
                "All findings from single sources require corroboration before strategic commitment",
            ],
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = synthesise_research(data)
    output = json.dumps(result, indent=2)
    args = sys.argv[1:]
    if "-o" in args:
        idx = args.index("-o") + 1
        if idx < len(args):
            Path(args[idx]).write_text(output + "\n", encoding="utf-8")
        else:
            sys.exit(1)
    else:
        print(output)


if __name__ == "__main__":
    main()
