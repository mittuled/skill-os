#!/usr/bin/env python3
"""
generate.py — Generates the output template for tool-policy-manager

Renders the output template for tool-policy-manager with provided or placeholder data.

Usage:
    python3 generate.py                    # Generate with placeholder data
    python3 generate.py -o output.md       # Write to file
    python3 generate.py --data input.json  # Use custom data

Dependencies: Python 3.10+ standard library only.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE_PATH = Path(__file__).parent.parent / "assets" / "tool-policy-change-report-template.md"


def load_template() -> str:
    """Load the output template."""
    if not TEMPLATE_PATH.exists():
        print(f"Error: Template not found: {TEMPLATE_PATH}", file=sys.stderr)
        sys.exit(1)
    return TEMPLATE_PATH.read_text(encoding="utf-8")


def load_data(path: Path | None) -> dict:
    """Load custom data or return defaults."""
    if path and path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {
        "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "author": "[Agent Role]",
        "version": "1.0",
        "status": "Draft",
        "skill": "tool-policy-manager",
    }


def render_template(template: str, data: dict) -> str:
    """Replace placeholder tokens in the template with actual data."""
    result = template
    result = result.replace("[YYYY-MM-DD]", data.get("date", datetime.now(timezone.utc).strftime("%Y-%m-%d")))
    result = result.replace("[Agent role / human name]", data.get("author", "[Author]"))
    result = result.replace("[1.0]", data.get("version", "1.0"))
    result = result.replace("[Draft / Review / Final]", data.get("status", "Draft"))
    result = result.replace("[skill-slug that produced this]", data.get("skill", "tool-policy-manager"))
    return result


def main() -> None:
    args = sys.argv[1:]
    
    if "-h" in args or "--help" in args:
        print("Usage: python3 generate.py [--data input.json] [-o output.md]")
        sys.exit(0)
    
    data_path = None
    if "--data" in args:
        idx = args.index("--data") + 1
        if idx < len(args):
            data_path = Path(args[idx])
    
    template = load_template()
    data = load_data(data_path)
    rendered = render_template(template, data)
    
    if "-o" in args:
        idx = args.index("-o") + 1
        if idx < len(args):
            Path(args[idx]).write_text(rendered, encoding="utf-8")
            print(f"Output written to {args[idx]}")
        else:
            print("Error: -o requires a filename", file=sys.stderr)
            sys.exit(1)
    else:
        print(rendered)


if __name__ == "__main__":
    main()
