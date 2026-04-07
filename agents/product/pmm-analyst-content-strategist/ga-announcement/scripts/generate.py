#!/usr/bin/env python3
"""Generate a ga announcement package from JSON parameters.

Usage:
    echo '{"product_name": "Example", "messaging_hierarchy": "...", "blog_post_draft": "...", "email_announcement": "..."}' | python3 generate.py
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
        "skill": "ga-announcement",
        "output_type": "ga-announcement-package",
        "product": params["product_name"],
        "generated_date": date.today().isoformat(),
        "sections": {},
    }

    sections = ['Messaging Hierarchy', 'Blog Post Draft', 'Email Announcement', 'Social Media Posts', 'Distribution Schedule', 'Performance Tracking']
    for section in sections:
        key = section.lower().replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "")
        result["sections"][key] = params.get(key, f"[Pending: {section}]")

    result["status"] = "draft"
    json.dump(result, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
