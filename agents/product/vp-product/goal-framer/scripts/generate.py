#!/usr/bin/env python3
"""Generate a goal framework from JSON parameters.

Usage:
    echo '{"product_name": "Example", "initiative_context": "...", "north_star_metric": "...", "supporting_metrics": "..."}' | python3 generate.py
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
        "skill": "goal-framer",
        "output_type": "goal-framework",
        "product": params["product_name"],
        "generated_date": date.today().isoformat(),
        "sections": {},
    }

    sections = ['Initiative Context', 'North Star Metric', 'Supporting Metrics', 'Guardrail Metrics', 'Stakeholder Sign-off']
    for section in sections:
        key = section.lower().replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "")
        result["sections"][key] = params.get(key, f"[Pending: {section}]")

    result["status"] = "draft"
    json.dump(result, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
