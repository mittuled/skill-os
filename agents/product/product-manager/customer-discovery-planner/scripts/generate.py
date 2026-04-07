#!/usr/bin/env python3
"""Generate a discovery plan from JSON parameters.

Usage:
    echo '{"product_name": "Example", "falsifiable_hypothesis": "...", "learning_objectives": "...", "participant_profile": "..."}' | python3 generate.py
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
        "skill": "customer-discovery-planner",
        "output_type": "discovery-plan",
        "product": params["product_name"],
        "generated_date": date.today().isoformat(),
        "sections": {},
    }

    sections = ['Falsifiable Hypothesis', 'Learning Objectives', 'Participant Profile', 'Discussion Guide (3-Act)', 'Recruitment Plan', 'Synthesis Methodology', 'Bias Mitigation Controls', 'Timeline']
    for section in sections:
        key = section.lower().replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "")
        result["sections"][key] = params.get(key, f"[Pending: {section}]")

    result["status"] = "draft"
    json.dump(result, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
