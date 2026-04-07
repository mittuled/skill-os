#!/usr/bin/env python3
"""Generate a backlog population report from JSON parameters.

Usage:
    echo '{"product_name": "Example", "input_sources": "...", "backlog_items_epics_stories_enablers": "...", "rice_scores": "..."}' | python3 generate.py
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
        "skill": "backlog-populator",
        "output_type": "backlog-population-report",
        "product": params["product_name"],
        "generated_date": date.today().isoformat(),
        "sections": {},
    }

    sections = ['Input Sources', 'Backlog Items (Epics/Stories/Enablers)', 'RICE Scores', 'Deduplication Log', 'Traceability Links']
    for section in sections:
        key = section.lower().replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "")
        result["sections"][key] = params.get(key, f"[Pending: {section}]")

    result["status"] = "draft"
    json.dump(result, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
