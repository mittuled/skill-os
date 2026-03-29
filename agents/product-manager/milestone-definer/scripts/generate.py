#!/usr/bin/env python3
"""Generate a milestone plan from JSON parameters.

Usage:
    echo '{"product_name": "Example", "deliverable_inventory": "...", "milestone_definitions_3-6": "...", "success_criteria_per_milestone": "..."}' | python3 generate.py
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
        "skill": "milestone-definer",
        "output_type": "milestone-plan",
        "product": params["product_name"],
        "generated_date": date.today().isoformat(),
        "sections": {},
    }

    sections = ['Deliverable Inventory', 'Milestone Definitions (3-6)', 'Success Criteria per Milestone', 'Timeline with Target Dates']
    for section in sections:
        key = section.lower().replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "")
        result["sections"][key] = params.get(key, f"[Pending: {section}]")

    result["status"] = "draft"
    json.dump(result, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
