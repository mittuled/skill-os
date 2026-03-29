#!/usr/bin/env python3
"""Generate a jtbd story map from JSON parameters.

Usage:
    echo '{"product_name": "Example", "jtbd_inventory": "...", "outcome_statements_ranked": "...", "user_stories_with_acceptance_criteria": "..."}' | python3 generate.py
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
        "skill": "jtbd-to-stories",
        "output_type": "jtbd-story-map",
        "product": params["product_name"],
        "generated_date": date.today().isoformat(),
        "sections": {},
    }

    sections = ['JTBD Inventory', 'Outcome Statements (Ranked)', 'User Stories with Acceptance Criteria', 'Story Map', 'Coverage Gap Analysis']
    for section in sections:
        key = section.lower().replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "")
        result["sections"][key] = params.get(key, f"[Pending: {section}]")

    result["status"] = "draft"
    json.dump(result, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
