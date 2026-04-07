#!/usr/bin/env python3
"""
generate.py — Generates a nurture campaign plan from structured input.

Reads JSON from stdin with segment, stages, and email details.
Outputs a formatted markdown nurture sequence plan.

Usage:
    cat nurture-input.json | python3 generate.py
"""

from __future__ import annotations

import json
import sys
from datetime import datetime


def generate_sequence_table(emails: list[dict]) -> str:
    rows = ["| # | Trigger | Timing | Subject Line | CTA | Asset |",
            "|---|---------|--------|-------------|-----|-------|"]
    for i, email in enumerate(emails, 1):
        rows.append(
            f"| {i} | {email.get('trigger', 'Time-based')} "
            f"| {email.get('timing', 'TBD')} "
            f"| {email.get('subject', 'TBD')} "
            f"| {email.get('cta', 'TBD')} "
            f"| {email.get('asset', 'N/A')} |"
        )
    return "\n".join(rows)


def generate_branch_table(branches: list[dict]) -> str:
    rows = ["| Signal | Condition | Action |",
            "|--------|-----------|--------|"]
    for branch in branches:
        rows.append(
            f"| {branch.get('signal', 'TBD')} "
            f"| {branch.get('condition', 'TBD')} "
            f"| {branch.get('action', 'TBD')} |"
        )
    return "\n".join(rows)


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

    segment = data.get("segment", {})
    emails = data.get("emails", [])
    branches = data.get("branches", [])
    journey = data.get("journey_stages", [])

    today = datetime.now().strftime("%Y-%m-%d")

    journey_rows = ["| Stage | Key Question | Content Type | Exit Signal |",
                    "|-------|-------------|-------------|-------------|"]
    for stage in journey:
        journey_rows.append(
            f"| {stage.get('name', 'TBD')} "
            f"| {stage.get('question', 'TBD')} "
            f"| {stage.get('content_type', 'TBD')} "
            f"| {stage.get('exit_signal', 'TBD')} |"
        )

    output = f"""# Nurture Sequence Plan

## Metadata

| Field | Value |
|-------|-------|
| Date | {today} |
| Author | Lifecycle Email Marketing Manager |
| Version | 1.0 |
| Status | Draft |
| Skill | nurture-campaign-builder |

## Executive Summary

Nurture programme targeting {segment.get('name', 'TBD')} segment with \
{len(emails)} emails across {len(journey)} buyer journey stages. \
Entry trigger: {segment.get('entry_trigger', 'TBD')}. \
Target conversion: {segment.get('target_conversion', 'TBD')}.

## Target Segment

| Attribute | Value |
|-----------|-------|
| Segment | {segment.get('name', 'TBD')} |
| Entry Trigger | {segment.get('entry_trigger', 'TBD')} |
| Monthly Volume | {segment.get('monthly_volume', 'TBD')} |
| Baseline Conversion | {segment.get('baseline_conversion', 'TBD')} |
| Target Conversion | {segment.get('target_conversion', 'TBD')} |

## Buyer Journey Map

{chr(10).join(journey_rows)}

## Email Sequence

{generate_sequence_table(emails)}

## Branch Logic

{generate_branch_table(branches)}

## Recommendations

1. **P1**: Monitor first-cycle deliverability and adjust send frequency if bounce rate exceeds 3%.
2. **P2**: A/B test subject lines on the first two emails before scaling to full volume.
3. **P3**: Review branch logic triggers after 30 days and adjust thresholds based on actual engagement data.
"""
    print(output)


if __name__ == "__main__":
    main()
