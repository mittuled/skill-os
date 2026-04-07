#!/usr/bin/env python3
"""Generate sales proposal from deal context."""
import json
import sys
from datetime import date


def generate(params: dict) -> str:
    """Build an 11-section sales proposal."""
    sections = []
    prospect = params.get("prospect_company", "[Company]")
    prepared_by = params.get("prepared_by", "[AE Name]")
    today = date.today().isoformat()

    sections.append(f"# Sales Proposal: {prospect}")
    sections.append(f"**Prepared by**: {prepared_by}")
    sections.append(f"**Date**: {today}")

    # Executive Summary
    sections.append("## 1. Executive Summary")
    pain = params.get("primary_pain", "[Primary pain point]")
    outcome = params.get("desired_outcome", "[Desired business outcome]")
    sections.append(
        f"{prospect} is experiencing {pain}. This proposal outlines how our "
        f"solution delivers {outcome}, with a projected ROI of "
        f"{params.get('projected_roi', '[X]')}x within "
        f"{params.get('payback_months', '12')} months."
    )

    # Current Situation
    sections.append("## 2. Current Situation")
    for point in params.get("current_situation", []):
        sections.append(f"- {point}")

    # Proposed Solution
    sections.append("## 3. Proposed Solution")
    requirements = params.get("requirements", [])
    if requirements:
        sections.append("| Requirement | Capability | Business Benefit |")
        sections.append("|-------------|-----------|-----------------|")
        for r in requirements:
            sections.append(
                f"| {r.get('requirement', '')} | {r.get('capability', '')} | {r.get('benefit', '')} |"
            )

    # ROI Analysis
    sections.append("## 4. ROI Analysis")
    roi = params.get("roi", {})
    sections.append(f"- **Cost of status quo**: ${roi.get('status_quo_cost', 0):,}/year")
    sections.append(f"- **Implementation cost**: ${roi.get('implementation_cost', 0):,}")
    sections.append(f"- **Annual value delivered**: ${roi.get('annual_value', 0):,}")
    sections.append(f"- **Payback period**: {roi.get('payback_months', 'N/A')} months")
    sections.append(f"- **3-year ROI**: {roi.get('three_year_roi', 'N/A')}x")

    # Competitive Comparison
    sections.append("## 5. Why Us")
    for diff in params.get("differentiators", []):
        sections.append(f"- {diff}")

    sections.append("## 6. Why Now")
    for reason in params.get("urgency_reasons", []):
        sections.append(f"- {reason}")

    # Implementation Plan
    sections.append("## 7. Implementation Plan")
    phases = params.get("implementation_phases", [])
    if phases:
        sections.append("| Phase | Duration | Milestones |")
        sections.append("|-------|----------|-----------|")
        for p in phases:
            sections.append(
                f"| {p.get('name', '')} | {p.get('duration', '')} | {p.get('milestones', '')} |"
            )

    # Team & Support
    sections.append("## 8. Team & Support")
    sections.append(
        f"- Dedicated CSM assigned at contract signature\n"
        f"- {params.get('support_level', 'Standard')} support SLA\n"
        f"- Quarterly business reviews"
    )

    # Pricing
    sections.append("## 9. Pricing Options")
    tiers = params.get("pricing_tiers", [])
    if tiers:
        sections.append("| Option | Includes | Annual Price |")
        sections.append("|--------|----------|-------------|")
        for t in tiers:
            sections.append(
                f"| {t.get('name', '')} | {t.get('includes', '')} | ${t.get('price', 0):,} |"
            )

    # Terms
    sections.append("## 10. Terms")
    sections.append(f"- **Contract length**: {params.get('contract_length', '12 months')}")
    sections.append(f"- **Payment terms**: {params.get('payment_terms', 'Annual prepay, net-30')}")
    sections.append(f"- **Start date**: {params.get('start_date', 'Upon signature')}")

    # Next Steps
    sections.append("## 11. Next Steps")
    next_steps = params.get("next_steps", [
        "Review proposal and share feedback",
        "Schedule commercial review meeting",
        "Finalize terms and execute contract",
    ])
    for i, step in enumerate(next_steps, 1):
        sections.append(f"{i}. {step}")

    return "\n\n".join(sections)


if __name__ == "__main__":
    data = json.load(sys.stdin) if not sys.stdin.isatty() else json.loads(sys.argv[1])
    print(generate(data))
