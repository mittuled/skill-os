#!/usr/bin/env python3
"""
generate.py — Generate the first repeatable sales process with pipeline stages and qualification gates.

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

# Stage count recommendations by motion type
STAGE_COUNT_BY_MOTION = {
    "enterprise": {"min": 6, "max": 8, "recommended": 7},
    "mid_market": {"min": 5, "max": 7, "recommended": 6},
    "velocity": {"min": 4, "max": 6, "recommended": 5},
    "plg": {"min": 3, "max": 5, "recommended": 4},
}

# Default MEDDIC qualification checklist
MEDDIC_QUALIFICATION = [
    "metrics_quantified",
    "economic_buyer_identified",
    "decision_criteria_confirmed",
    "decision_process_mapped",
    "pain_identified",
    "champion_identified",
]

# Required handoff types
REQUIRED_HANDOFFS = ["sdr_to_ae", "ae_to_se", "ae_to_cs"]


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    for f in ["motion_type", "pipeline_stages"]:
        if f not in data:
            errors.append(f"Missing required field: {f}")
    if "motion_type" in data and data["motion_type"] not in STAGE_COUNT_BY_MOTION:
        errors.append(f"motion_type must be one of: {list(STAGE_COUNT_BY_MOTION.keys())}")
    if "pipeline_stages" in data:
        if len(data["pipeline_stages"]) < 3:
            errors.append("pipeline_stages must have at least 3 stages")
        for i, s in enumerate(data["pipeline_stages"]):
            for f in ["name", "entry_criterion", "exit_criterion"]:
                if f not in s:
                    errors.append(f"pipeline_stages[{i}] missing field: {f}")
    return errors


def build_process(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    motion = data["motion_type"]
    motion_config = STAGE_COUNT_BY_MOTION[motion]
    stages = data["pipeline_stages"]

    stage_count_valid = motion_config["min"] <= len(stages) <= motion_config["max"]
    stage_count_warning = None if stage_count_valid else (
        f"Stage count {len(stages)} is outside recommended range {motion_config['min']}-{motion_config['max']} for {motion} motion"
    )

    # Check for buyer-centric stage names (anti-pattern detection)
    seller_centric_keywords = ["sent", "scheduled", "submitted", "called", "emailed"]
    seller_centric_stages = [
        s["name"] for s in stages
        if any(kw in s["name"].lower() for kw in seller_centric_keywords)
    ]

    # Build stage definitions
    stage_defs = []
    for i, s in enumerate(stages):
        stage_defs.append({
            "stage_number": i + 1,
            "stage_name": s["name"],
            "entry_criterion": s["entry_criterion"],
            "exit_criterion": s["exit_criterion"],
            "probability_pct": s.get("probability_pct", (i + 1) * (100 // len(stages))),
            "required_activities": s.get("required_activities", []),
            "qualification_gates": s.get("qualification_gates", []),
            "avg_days_target": s.get("avg_days_target", None),
        })

    # Handoff protocols
    handoffs_provided = set(data.get("handoff_protocols", {}).keys())
    missing_handoffs = [h for h in REQUIRED_HANDOFFS if h not in handoffs_provided]

    result = {
        "motion_type": motion,
        "stage_count": len(stages),
        "stage_count_valid": stage_count_valid,
        "stage_count_warning": stage_count_warning,
        "seller_centric_stages": seller_centric_stages,
        "qualification_framework": data.get("qualification_framework", "MEDDIC"),
        "stages": stage_defs,
        "handoff_protocols": data.get("handoff_protocols", {}),
        "missing_handoffs": missing_handoffs,
        "crm_requirements": {
            "stage_picklist_values": [s["stage_name"] for s in stages],
            "required_fields": data.get("required_crm_fields", []),
            "automation_rules": data.get("automation_rules", []),
        },
        "rollout_plan": data.get("rollout_plan", {}),
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = build_process(data)
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
