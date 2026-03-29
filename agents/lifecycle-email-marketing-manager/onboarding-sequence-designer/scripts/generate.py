#!/usr/bin/env python3
"""
generate.py — Generates an onboarding sequence plan from structured input.

Reads JSON from stdin with activation moment, milestones, and email details.
Outputs a formatted markdown onboarding sequence plan.

Usage:
    cat onboarding-input.json | python3 generate.py
"""

from __future__ import annotations

import json
import sys
from datetime import datetime


def generate_milestone_table(milestones: list[dict]) -> str:
    rows = [
        "| ID | Action | Prerequisite | Typical Time | Email if Skipped |",
        "|----|--------|-------------|-------------|-----------------|",
    ]
    for m in milestones:
        rows.append(
            f"| {m.get('id', 'M?')} "
            f"| {m.get('action', 'TBD')} "
            f"| {m.get('prerequisite', 'None')} "
            f"| {m.get('typical_time', 'TBD')} "
            f"| {m.get('email_if_skipped', 'N/A')} |"
        )
    return "\n".join(rows)


def generate_email_section(emails: list[dict]) -> str:
    sections = []
    for i, email in enumerate(emails, 1):
        section = f"""### Email {i}: {email.get('name', 'Untitled')}

- **Trigger**: {email.get('trigger', 'TBD')}
- **Subject**: {email.get('subject', 'TBD')}
- **CTA**: {email.get('cta', 'TBD')}
- **Milestone**: {email.get('milestone', 'TBD')}
- **Suppression**: {email.get('suppression', 'Skip if milestone already completed')}"""
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

    activation = data.get("activation_moment", {})
    milestones = data.get("milestones", [])
    emails = data.get("emails", [])
    product = data.get("product_name", "Product")

    today = datetime.now().strftime("%Y-%m-%d")

    output = f"""# Onboarding Email Sequence Plan: {product}

## Metadata

| Field | Value |
|-------|-------|
| Date | {today} |
| Author | Lifecycle Email Marketing Manager |
| Version | 1.0 |
| Status | Draft |
| Skill | onboarding-sequence-designer |

## Executive Summary

{len(emails)}-email onboarding sequence for {product} guiding new users from signup \
to the activation moment: {activation.get('description', 'TBD')}. \
Target activation rate: {activation.get('target_rate', 'TBD')} \
(baseline: {activation.get('baseline_rate', 'TBD')}).

## Activation Moment Definition

**Action**: {activation.get('description', 'TBD')}
**Time window**: {activation.get('time_window', 'TBD')}
**Retention correlation**: {activation.get('retention_correlation', 'TBD')}

## Milestone Map

{generate_milestone_table(milestones)}

## Email Sequence

{generate_email_section(emails)}

## Recommendations

1. **P1**: Validate activation moment correlation with 90-day retention data before finalising sequence.
2. **P2**: A/B test the welcome email subject line in the first cohort.
3. **P3**: Add a celebration email at activation to reinforce the achievement and bridge to retention.
"""
    print(output)


if __name__ == "__main__":
    main()
