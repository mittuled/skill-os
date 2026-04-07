#!/usr/bin/env python3
"""Generate a step execution plan for internal-demo-runner.

Reads JSON from stdin with step statuses, outputs execution plan.

Usage:
    echo '{"product_name": "Example"}' | python3 run.py
"""

import json
import sys
from datetime import date


STEPS: list[str] = [
    "Define demo scope, audience, and narrative angle",
    "Prepare and verify demo environment with realistic data",
    "Run demo with user-perspective narration and feedback capture",
    "Distribute categorised feedback within 24 hours",
]


def main() -> None:
    params = json.load(sys.stdin)
    product = params.get("product_name", "Unknown")
    step_statuses = params.get("step_statuses", {})

    plan = {
        "skill": "internal-demo-runner",
        "product": product,
        "generated_date": date.today().isoformat(),
        "total_steps": len(STEPS),
        "steps": [],
    }

    completed = 0
    for i, step in enumerate(STEPS, 1):
        status = step_statuses.get(str(i), "pending")
        is_gate = "[GATE]" in step
        plan["steps"].append({
            "step": i,
            "description": step.replace(" [GATE]", ""),
            "status": status,
            "is_gate": is_gate,
        })
        if status == "complete":
            completed += 1

    plan["progress_pct"] = round(completed / len(STEPS) * 100, 1)
    plan["next_step"] = next((s for s in plan["steps"] if s["status"] == "pending"), None)

    json.dump(plan, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
