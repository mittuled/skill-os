#!/usr/bin/env python3
"""Execute expansion-motion-sales workflow steps."""
import json
import sys

STEPS = [
    {
        "id": 1,
        "name": "Expansion Signal Review",
        "deliverables": ["expansion opportunity brief with trigger evidence"],
        "required_inputs": ["account_name", "usage_metrics"],
        "validation": "At least one expansion trigger identified with supporting data",
    },
    {
        "id": 2,
        "name": "Stakeholder Mapping",
        "deliverables": ["updated stakeholder map with expansion-specific roles"],
        "required_inputs": ["account_name", "current_contacts"],
        "validation": "Economic buyer for expansion identified (may differ from original deal)",
    },
    {
        "id": 3,
        "name": "Value Case Construction",
        "deliverables": ["account-specific expansion value case"],
        "required_inputs": ["current_roi_data", "expansion_scope"],
        "validation": "ROI projections use account's own usage data, not generic benchmarks",
    },
    {
        "id": 4,
        "name": "Proposal and Negotiation",
        "deliverables": ["expansion proposal with commercial terms"],
        "required_inputs": ["value_case", "contract_details"],
        "validation": "Pricing co-termed with existing contract; mutual action plan attached",
        "gate": True,
    },
    {
        "id": 5,
        "name": "Handoff to CS",
        "deliverables": ["expansion handoff document"],
        "required_inputs": ["expansion_scope", "new_stakeholders", "success_criteria"],
        "validation": "CS team acknowledged receipt with onboarding plan timeline",
    },
]


def run(context: dict) -> dict:
    """Validate inputs and produce workflow execution plan."""
    results = {"skill": "expansion-motion-sales", "steps": [], "status": "complete"}
    account = context.get("account_name", "[Unknown Account]")
    results["account"] = account

    for step in STEPS:
        missing = [i for i in step["required_inputs"] if i not in context]
        status = "ready" if not missing else "blocked"
        result = {
            "step": step["id"],
            "name": step["name"],
            "status": status,
            "deliverables": step["deliverables"],
            "validation": step["validation"],
        }
        if missing:
            result["missing_inputs"] = missing
            results["status"] = "blocked"
        if step.get("gate"):
            result["gate"] = True
            result["gate_note"] = "Requires explicit approval before proceeding"
        results["steps"].append(result)
    return results


if __name__ == "__main__":
    data = json.load(sys.stdin) if not sys.stdin.isatty() else json.loads(sys.argv[1])
    print(json.dumps(run(data), indent=2))
