#!/usr/bin/env python3
"""
generate.py — Generate v1 brand identity specifications including logo, colour palette, and typography.

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

COLOUR_PALETTE_ROLES = ["primary", "secondary", "accent", "background", "text", "error", "success", "warning"]

TYPOGRAPHY_ROLES = {
    "display": {"usage": "Hero headlines, large marketing type", "size_range": "48-96px"},
    "heading": {"usage": "Section headers, feature titles", "size_range": "24-48px"},
    "body": {"usage": "Body copy, descriptions", "size_range": "14-18px"},
    "ui": {"usage": "Button labels, form labels, navigation", "size_range": "12-16px"},
    "code": {"usage": "Code snippets, technical strings", "size_range": "12-14px"},
}

LOGO_VARIANTS = ["primary", "reversed", "monochrome", "icon_only", "wordmark_only"]

REQUIRED_FIELDS = ["brand_name", "colour_palette", "typography"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "colour_palette" in data:
        for colour in data["colour_palette"]:
            if "role" not in colour or "hex" not in colour:
                errors.append("Each colour needs 'role' and 'hex' fields")
    if "typography" in data:
        for font in data["typography"]:
            if "role" not in font or "family" not in font:
                errors.append("Each typography entry needs 'role' and 'family' fields")
    return errors


def generate_identity(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    colours = {c["role"]: c for c in data["colour_palette"]}
    fonts = {f["role"]: f for f in data["typography"]}

    identity = {
        "brand_name": data["brand_name"],
        "version": "1.0",
        "logo": {
            "concept": data.get("logo_concept", "Wordmark with optional icon mark"),
            "variants_required": LOGO_VARIANTS,
            "usage_rules": [
                "Minimum size: 120px wide for wordmark, 32px for icon",
                "Clear space: equal to height of capital letter on all sides",
                "Never distort, rotate, or apply effects to the logo",
                "Only approved colour combinations may be used",
            ],
            "formats_to_deliver": ["SVG (master)", "PNG (web)", "PDF (print)"],
        },
        "colour_system": {
            "colours": colours,
            "combination_rules": [
                f"Primary on Background: {colours.get('primary', {}).get('hex', 'TBD')} on {colours.get('background', {}).get('hex', 'TBD')}",
                f"Text on Background: ensure WCAG AA contrast ratio (4.5:1 minimum)",
                "Never use accent colour as background for body text",
            ],
            "accessibility": "All text/background combinations must meet WCAG 2.1 AA (4.5:1 for normal, 3:1 for large text)",
        },
        "typography_system": {
            "fonts": fonts,
            "scale": {role: config for role, config in TYPOGRAPHY_ROLES.items()},
            "usage_rules": [
                "Use only approved typefaces from the system",
                "Never stretch or condense font widths",
                "Line height: 1.5x for body copy, 1.2x for headings",
                "Letter spacing: default except for ALL CAPS labels (+0.05em)",
            ],
        },
        "usage_guidelines_url": f"https://brand.{data['brand_name'].lower().replace(' ', '')}.com/guidelines",
    }

    return {"error": None, "result": identity}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_identity(data)
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
