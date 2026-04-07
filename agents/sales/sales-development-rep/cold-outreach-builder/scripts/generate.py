#!/usr/bin/env python3
"""
generate.py — Generate a multi-touch cold outreach sequence with A/B variants.

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

# Outreach frameworks by buying stage
FRAMEWORKS = {
    "unaware": "AIDA",
    "problem_aware": "PAS",
    "solution_aware": "BAB",
    "vendor_aware": "BAB",
}

FRAMEWORK_DESCRIPTIONS = {
    "AIDA": "Attention → Interest → Desire → Action — for prospects unaware of the problem",
    "PAS": "Problem → Agitate → Solve — for prospects who acknowledge the pain",
    "BAB": "Before → After → Bridge — for prospects who know solutions exist",
}

# Standard cadence in days per seniority level
CADENCE_BY_SENIORITY = {
    "c_suite": [1, 6, 12, 22, 32],   # 2x spacing for C-suite
    "vp_director": [1, 4, 8, 14, 22],
    "manager_ic": [1, 3, 6, 11, 16],
}

# Channel rotation per touch index (0-based)
CHANNEL_ROTATION = {
    0: "email",
    1: "linkedin_connection",
    2: "email",
    3: "linkedin_message",
    4: "email",
    5: "phone",
    6: "email",
    7: "email_breakup",
}


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    for f in ["prospect_name", "company", "persona_role", "buying_stage", "seniority_level"]:
        if f not in data:
            errors.append(f"Missing required field: {f}")
    if "buying_stage" in data and data["buying_stage"] not in FRAMEWORKS:
        errors.append(f"buying_stage must be one of: {list(FRAMEWORKS.keys())}")
    if "seniority_level" in data and data["seniority_level"] not in CADENCE_BY_SENIORITY:
        errors.append(f"seniority_level must be one of: {list(CADENCE_BY_SENIORITY.keys())}")
    return errors


def build_sequence(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    framework = FRAMEWORKS[data["buying_stage"]]
    cadence = CADENCE_BY_SENIORITY[data["seniority_level"]]
    emails = data.get("email_drafts", [])
    ab_variants = data.get("ab_variants", {})
    tokens = data.get("personalization_tokens", {})

    # Build touch sequence
    touches = []
    for i, day in enumerate(cadence):
        channel = CHANNEL_ROTATION.get(i, "email")
        email_data = emails[i] if i < len(emails) else {}
        variant_a = ab_variants.get(f"email_{i + 1}_subject_a", email_data.get("subject", ""))
        variant_b = ab_variants.get(f"email_{i + 1}_subject_b", "")
        touch = {
            "touch_number": i + 1,
            "day": day,
            "channel": channel,
            "subject_line_a": variant_a,
            "subject_line_b": variant_b if variant_b else None,
            "body_preview": email_data.get("body_preview", ""),
            "cta": email_data.get("cta", ""),
        }
        touches.append(touch)

    # Identify missing personalization tokens
    required_tokens = ["company_name", "first_name", "pain_point", "trigger_event"]
    missing_tokens = [t for t in required_tokens if t not in tokens]

    result = {
        "prospect": data["prospect_name"],
        "company": data["company"],
        "persona_role": data["persona_role"],
        "buying_stage": data["buying_stage"],
        "framework": framework,
        "framework_rationale": FRAMEWORK_DESCRIPTIONS[framework],
        "seniority_level": data["seniority_level"],
        "sequence_length": len(touches),
        "touches": touches,
        "personalization_tokens": tokens,
        "missing_tokens": missing_tokens,
        "ab_test_hypothesis": data.get("ab_test_hypothesis", ""),
        "performance_targets": {
            "open_rate_target_pct": 35,
            "reply_rate_target_pct": 3,
            "meeting_set_rate_target_pct": 0.8,
        },
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = build_sequence(data)
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
