#!/usr/bin/env python3
"""Generate a in app announcement from JSON parameters.

Usage:
    echo '{"product_name": "Example", "feature_context": "...", "headline_and_body_copy_<40_words": "...", "cta_and_destination": "..."}' | python3 generate.py
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
        "skill": "in-app-announcement-writer",
        "output_type": "in-app-announcement",
        "product": params["product_name"],
        "generated_date": date.today().isoformat(),
        "sections": {},
    }

    sections = ['Feature Context', 'Headline and Body Copy (<40 words)', 'CTA and Destination', 'Publish and Expiration Rules']
    for section in sections:
        key = section.lower().replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "")
        result["sections"][key] = params.get(key, f"[Pending: {section}]")

    result["status"] = "draft"
    json.dump(result, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
