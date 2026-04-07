#!/usr/bin/env python3
"""Generate a changelog entry from JSON parameters.

Usage:
    echo '{"product_name": "Example", "release_summary": "...", "new_features": "...", "improvements": "..."}' | python3 generate.py
"""

import json
import sys
from datetime import date


def main() -> None:
    params = json.load(sys.stdin)
    if "product_name" not in params:
        json.dump({"error": "Missing required field: product_name"}, sys.stdout, indent=2)
        sys.exit(1)

    result = {
        "skill": "changelog-publisher-pmm",
        "output_type": "changelog-entry",
        "product": params["product_name"],
        "generated_date": date.today().isoformat(),
        "sections": {},
    }

    sections = ['Release Summary', 'New Features', 'Improvements', 'Bug Fixes', 'Visual Aids']
    for section in sections:
        key = section.lower().replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "")
        result["sections"][key] = params.get(key, f"[Pending: {section}]")

    result["status"] = "draft"
    json.dump(result, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
