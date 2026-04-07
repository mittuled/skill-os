#!/usr/bin/env python3
"""
generate.py — Generates a retention email sequence plan from structured input.

Reads JSON from stdin with churn signals, segments, and email details.
Outputs a formatted markdown retention sequence plan.

Usage:
    cat retention-input.json | python3 generate.py
"""

from __future__ import annotations

import json
import sys
from datetime import datetime


def generate_signal_table(signals: list[dict]) -> str:
    rows = [
        "| Signal | Data Source | Threshold | Severity |",
        "|--------|-----------|-----------|----------|",
    ]
    for s in signals:
        rows.append(
            f"| {s.get('name', 'TBD')} "
            f"| {s.get('source', 'TBD')} "
            f"| {s.get('threshold', 'TBD')} "
            f"| {s.get('severity', 'TBD')} |"
        )
    return "\n".join(rows)


def generate_email_sections(emails: list[dict]) -> str:
    sections = []
    for i, email in enumerate(emails, 1):
        section = f"""### Email {i}: {email.get('name', 'Untitled')}

- **Trigger**: {email.get('trigger', 'TBD')}
- **Tier**: {email.get('tier', 'TBD')}
- **Subject**: {email.get('subject', 'TBD')}
- **Approach**: {email.get('approach', 'TBD')}
- **CTA**: {email.get('cta', 'TBD')}
- **Recovery exit**: {email.get('recovery_signal', 'User returns to healthy engagement')}"""
        sections.append(section)
    return "\n\n".join(sections)


def main() -> None:
    raw = sys.stdin.read().strip()
    if not raw:
        print(json.dumps({"error": "No input provided. Send JSON via stdin."}))
        sys.exit(1)

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(json.dumps({"error": f"Invalid JSON: {e}"}))
        sys.exit(1)

    signals = data.get("churn_signals", [])
    segments = data.get("segments", [])
    emails = data.get("emails", [])
    product = data.get("product_name", "Product")
    revenue_at_risk = data.get("revenue_at_risk", "TBD")

    today = datetime.now().strftime("%Y-%m-%d")

    seg_rows = [
        "| Segment | Account Value | Risk Level | Intervention Tier |",
        "|---------|--------------|------------|-------------------|",
    ]
    for seg in segments:
        seg_rows.append(
            f"| {seg.get('name', 'TBD')} "
            f"| {seg.get('value', 'TBD')} "
            f"| {seg.get('risk_level', 'TBD')} "
            f"| {seg.get('tier', 'TBD')} |"
        )

    output = f"""# Retention Email Sequence Plan: {product}

## Metadata

| Field | Value |
|-------|-------|
| Date | {today} |
| Author | Lifecycle Email Marketing Manager |
| Version | 1.0 |
| Status | Draft |
| Skill | retention-email-designer |

## Executive Summary

Retention sequence for {product} targeting at-risk users identified by \
{len(signals)} churn risk signals. Estimated revenue at risk: {revenue_at_risk}. \
{len(emails)} emails across {len(segments)} intervention tiers.

## Churn Risk Signals

{generate_signal_table(signals)}

## Segment Definitions

{chr(10).join(seg_rows)}

## Email Sequence

{generate_email_sections(emails)}

## Recommendations

1. **P1**: Validate churn signals against historical data before launch to minimise false positives.
2. **P2**: Coordinate with CS on high-value account handoff triggers.
3. **P3**: Review recovery rates monthly and adjust signal thresholds based on observed patterns.
"""
    print(output)


if __name__ == "__main__":
    main()
