#!/usr/bin/env python3
"""Generate a step execution plan for dependency-resolver.

Reads JSON from stdin with step statuses, outputs execution plan.

Usage:
    echo '{"product_name": "Example"}' | python3 run.py
"""

import json
import sys
from datetime import date


STEPS: list[str] = [
    "Review dependency map and identify unresolved blocking items",
    "Contact owning team PM/tech lead for capacity and delivery date",
    "Assess resolution options: direct, re-sequence, scope reduction, workaround, escalation",
    "Select resolution path and document action, owner, committed date, fallback",
    "Update dependency map with resolution status",
    "Communicate resolution plan to both teams",
    "Set midpoint follow-up checkpoint",
    "Close dependency item when deliverable confirmed complete",
]


def main() -> None:
    params = json.load(sys.stdin)
    product = params.get("product_name", "Unknown")
    step_statuses = params.get("step_statuses", {})

    plan = {
        "skill": "dependency-resolver",
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
