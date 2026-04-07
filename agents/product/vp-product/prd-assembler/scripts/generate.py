#!/usr/bin/env python3
"""Generate a prd from JSON parameters.

Usage:
    echo '{"product_name": "Example", "problem_statement": "...", "success_criteria": "...", "user_stories_moscow_rice": "..."}' | python3 generate.py
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
        "skill": "prd-assembler",
        "output_type": "prd",
        "product": params["product_name"],
        "generated_date": date.today().isoformat(),
        "sections": {},
    }

    sections = ['Problem Statement', 'Success Criteria', 'User Stories (MoSCoW/RICE)', 'Design Requirements', 'Technical Constraints', 'Scope Boundaries', 'Traceability Matrix']
    for section in sections:
        key = section.lower().replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "")
        result["sections"][key] = params.get(key, f"[Pending: {section}]")

    result["status"] = "draft"
    json.dump(result, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
