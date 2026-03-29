#!/usr/bin/env python3
"""Generate a opportunity brief from JSON parameters.

Usage:
    echo '{"product_name": "Example", "target_persona": "...", "problem_statement": "...", "market_sizing_tam_sam_som": "..."}' | python3 generate.py
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
        "skill": "opportunity-framer",
        "output_type": "opportunity-brief",
        "product": params["product_name"],
        "generated_date": date.today().isoformat(),
        "sections": {},
    }

    sections = ['Target Persona', 'Problem Statement', 'Market Sizing (TAM/SAM/SOM)', 'Strategic Fit Assessment']
    for section in sections:
        key = section.lower().replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "")
        result["sections"][key] = params.get(key, f"[Pending: {section}]")

    result["status"] = "draft"
    json.dump(result, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
