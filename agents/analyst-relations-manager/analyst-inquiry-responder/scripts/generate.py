#!/usr/bin/env python3
"""
generate.py — Generate a structured analyst inquiry response with positioning-aligned answers.

Usage:
    echo '<json>' | python3 generate.py
    python3 generate.py < input.json
    python3 generate.py < input.json -o output.json

Dependencies: Python 3.10+ standard library only.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

INQUIRY_CATEGORIES = ["competitive_positioning", "product_capability", "market_sizing", "customer_references", "pricing_model", "roadmap", "security_compliance"]

RESPONSE_GUIDELINES = {
    "competitive_positioning": "Lead with differentiation; avoid disparaging competitors by name; use third-party validation",
    "product_capability": "Be specific with metrics and customer evidence; do not overpromise; reference GA features only unless roadmap is pre-approved for disclosure",
    "market_sizing": "Anchor to industry reports where available; provide our own bottom-up estimate with assumptions",
    "customer_references": "Provide 3 referenceable accounts by segment; include one publicly named if approved",
    "pricing_model": "Explain model conceptually; do not share actual prices without marketing approval",
    "roadmap": "Only disclose items approved for external sharing; mark as direction not commitment",
    "security_compliance": "Reference certifications held (SOC 2, ISO 27001, etc.); do not speculate on future certifications",
}

REQUIRED_FIELDS = ["inquiry_category", "inquiry_question", "company_position"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "inquiry_category" in data and data["inquiry_category"] not in INQUIRY_CATEGORIES:
        errors.append(f"inquiry_category must be one of {INQUIRY_CATEGORIES}")
    return errors


def generate_response(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    category = data["inquiry_category"]
    guideline = RESPONSE_GUIDELINES[category]
    evidence = data.get("supporting_evidence", [])

    response_structure = {
        "opening": f"Thank you for the inquiry. Here is our position on {category.replace('_', ' ')}.",
        "core_answer": data["company_position"],
        "supporting_evidence": evidence,
        "third_party_validation": data.get("third_party_sources", []),
        "messaging_guideline_applied": guideline,
        "caveats": data.get("caveats", []),
    }

    review_flags = []
    if category == "roadmap" and not data.get("roadmap_disclosure_approved"):
        review_flags.append("REVIEW REQUIRED: Roadmap items must be pre-approved for external analyst disclosure before sending")
    if category == "pricing_model" and not data.get("pricing_disclosure_approved"):
        review_flags.append("REVIEW REQUIRED: Pricing details require marketing approval before sharing with analysts")
    if not evidence:
        review_flags.append("WEAK RESPONSE: No supporting evidence provided — response is assertion-only; add customer data or metrics")

    return {
        "error": None,
        "result": {
            "inquiry_summary": data["inquiry_question"][:200],
            "category": category,
            "response_structure": response_structure,
            "review_flags": review_flags,
            "ready_to_send": len(review_flags) == 0,
            "recommended_follow_up": "Offer to schedule a 30-minute follow-up call to provide live demonstrations or customer introductions",
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_response(data)
    output = json.dumps(result, indent=2)
    args = sys.argv[1:]
    if "-o" in args:
        idx = args.index("-o") + 1
        if idx < len(args):
            Path(args[idx]).write_text(output + "\n", encoding="utf-8")
        else:
            sys.exit(1)
    else:
        print(output)


if __name__ == "__main__":
    main()
