#!/usr/bin/env python3
"""Generate a market sizing brief from JSON parameters.

Usage:
    echo '{"product_name": "Example", "market_boundary_definition": "...", "tam_top-down": "...", "sam_bottom-up": "..."}' | python3 generate.py
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
        "skill": "market-sizer",
        "output_type": "market-sizing-brief",
        "product": params["product_name"],
        "generated_date": date.today().isoformat(),
        "sections": {},
    }

    sections = ['Market Boundary Definition', 'TAM (Top-Down)', 'SAM (Bottom-Up)', 'SOM (Penetration)', 'Triangulation and Sensitivity']
    for section in sections:
        key = section.lower().replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "")
        result["sections"][key] = params.get(key, f"[Pending: {section}]")

    result["status"] = "draft"
    json.dump(result, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
