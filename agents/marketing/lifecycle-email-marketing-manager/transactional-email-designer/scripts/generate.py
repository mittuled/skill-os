#!/usr/bin/env python3
"""
generate.py — Generates a transactional email template specification.

Reads JSON from stdin with email types, brand details, and sender config.
Outputs a formatted markdown template library document.

Usage:
    cat transactional-input.json | python3 generate.py
"""

from __future__ import annotations

import json
import sys
from datetime import datetime


def generate_inventory(templates: list[dict]) -> str:
    rows = [
        "| Template | Category | Trigger | Priority | Secondary CTA |",
        "|----------|----------|---------|----------|--------------|",
    ]
    for t in templates:
        rows.append(
            f"| {t.get('name', 'TBD')} "
            f"| {t.get('category', 'TBD')} "
            f"| {t.get('trigger', 'TBD')} "
            f"| {t.get('priority', 'Normal')} "
            f"| {t.get('secondary_cta', 'No')} |"
        )
    return "\n".join(rows)


def generate_specs(templates: list[dict]) -> str:
    sections = []
    for t in templates:
        section = f"""### {t.get('name', 'Untitled')}

- **Category**: {t.get('category', 'TBD')}
- **Subject pattern**: {t.get('subject_pattern', 'TBD')}
- **Preheader**: {t.get('preheader', 'TBD')}
- **Primary content**: {t.get('primary_content', 'TBD')}
- **Secondary CTA**: {t.get('secondary_cta_detail', 'None')}
- **Plain text**: {t.get('plain_text_notes', 'Include all content in readable format')}"""
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

    templates = data.get("templates", [])
    brand = data.get("brand", {})
    sender = data.get("sender_config", {})
    product = data.get("product_name", "Product")

    today = datetime.now().strftime("%Y-%m-%d")

    output = f"""# Transactional Email Template Library: {product}

## Metadata

| Field | Value |
|-------|-------|
| Date | {today} |
| Author | Lifecycle Email Marketing Manager |
| Version | 1.0 |
| Status | Draft |
| Skill | transactional-email-designer |

## Executive Summary

Template library covering {len(templates)} transactional email types for {product}. \
All templates use a dedicated sending domain ({sender.get('domain', 'TBD')}) \
with SPF, DKIM, and DMARC authentication. Target inbox placement: >99%.

## Template Inventory

{generate_inventory(templates)}

## Template Specifications

{generate_specs(templates)}

## Sender Configuration

| Setting | Value |
|---------|-------|
| Sending domain | {sender.get('domain', 'TBD')} |
| SPF | {sender.get('spf', 'TBD')} |
| DKIM selector | {sender.get('dkim_selector', 'TBD')} |
| DMARC policy | {sender.get('dmarc', 'p=quarantine')} |
| Bounce handling | Hard bounce: suppress after 1 attempt. Soft bounce: retry 3x over 24h. |

## Recommendations

1. **P1**: Deploy sender authentication (SPF, DKIM, DMARC) before sending any transactional email.
2. **P2**: Test all templates across Gmail, Outlook, Apple Mail, and mobile before launch.
3. **P3**: Monitor inbox placement weekly for the first month and investigate any drops below 98%.
"""
    print(output)


if __name__ == "__main__":
    main()
