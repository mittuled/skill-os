#!/usr/bin/env python3
"""
community-led-growth-designer — Design community-led growth programme.
Input (JSON via stdin or -i):
  {
    "community": str,
    "product": str,
    "stage": str,           # "growing" or "mature"
    "current_members": int,
    "mau": int,
    "month1_retention_pct": float,
    "net_sentiment_score": float,
    "primary_lever": str,   # "advocacy", "referral", "ugc", "events", "product_loop"
    "member_motivations": list[str],  # e.g. ["recognition", "learning", "networking"]
    "incentive_budget_usd": float,
    "pilot_cohort_size": int
  }
Output: Community-led growth programme design as Markdown.
"""

import json
import sys
import argparse

GROWTH_LEVERS = {
    "advocacy": {
        "name": "Ambassador / Advocacy Programme",
        "description": "Empower top members to represent the brand and recruit peers",
        "eligibility": "Members active for 3+ months, 10+ posts, positive sentiment",
        "incentives": ["Exclusive badge/role", "Early product access", "Swag kit", "Direct product team access"],
        "kpis": ["Referrals per ambassador", "Ambassador retention", "Content pieces published"],
        "health_prereq": {"retention": 30, "sentiment": 20, "mau_rate": 25},
    },
    "referral": {
        "name": "Member Referral Programme",
        "description": "Incentivise existing members to invite relevant peers",
        "eligibility": "All active members (MAU)",
        "incentives": ["Product credits", "Premium features", "Leaderboard recognition"],
        "kpis": ["Referral rate", "Referred member activation rate", "Referral CAC vs paid CAC"],
        "health_prereq": {"retention": 25, "sentiment": 15, "mau_rate": 20},
    },
    "ugc": {
        "name": "User-Generated Content Programme",
        "description": "Encourage members to create tutorials, case studies, and guides",
        "eligibility": "Members with demonstrated product expertise",
        "incentives": ["Featured content slot", "Co-marketing opportunity", "Expert badge"],
        "kpis": ["UGC pieces per month", "UGC content views", "New member sign-ups via UGC"],
        "health_prereq": {"retention": 20, "sentiment": 10, "mau_rate": 15},
    },
    "events": {
        "name": "Community Events Programme",
        "description": "Regular virtual and in-person events that attract new members",
        "eligibility": "All members; events open to non-members as pipeline",
        "incentives": ["Speaker recognition", "Event access", "Recording archive access"],
        "kpis": ["Event attendance", "Post-event new member sign-ups", "Speaker NPS"],
        "health_prereq": {"retention": 20, "sentiment": 10, "mau_rate": 15},
    },
    "product_loop": {
        "name": "Community-to-Product Loop",
        "description": "Surface community achievements inside the product to drive sharing",
        "eligibility": "All product users",
        "incentives": ["In-product recognition", "Shareable milestones"],
        "kpis": ["Share rate", "Shares-to-joins conversion", "Virality coefficient (k-factor)"],
        "health_prereq": {"retention": 25, "sentiment": 15, "mau_rate": 20},
    },
}

MOTIVATION_PROGRAMME_FIT = {
    "recognition": ["advocacy", "ugc"],
    "learning": ["events", "ugc"],
    "networking": ["events", "advocacy"],
    "influence": ["advocacy", "ugc"],
    "rewards": ["referral", "ugc"],
    "access": ["advocacy", "referral"],
}


def validate_input(data: dict) -> list[str]:
    required = [
        "community", "product", "stage", "current_members", "mau",
        "month1_retention_pct", "net_sentiment_score", "primary_lever",
        "member_motivations", "incentive_budget_usd", "pilot_cohort_size"
    ]
    errors = []
    for field in required:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "primary_lever" in data and data["primary_lever"] not in GROWTH_LEVERS:
        errors.append(f"primary_lever must be one of: {list(GROWTH_LEVERS.keys())}")
    return errors


def check_health_prereq(data: dict, lever: dict) -> tuple[bool, list[str]]:
    prereq = lever["health_prereq"]
    mau_rate = data["mau"] / data["current_members"] * 100 if data["current_members"] > 0 else 0
    warnings = []
    ready = True
    if data["month1_retention_pct"] < prereq["retention"]:
        warnings.append(
            f"M1 retention {data['month1_retention_pct']:.0f}% < required {prereq['retention']:.0f}%"
        )
        ready = False
    if data["net_sentiment_score"] < prereq["sentiment"]:
        warnings.append(
            f"Sentiment {data['net_sentiment_score']:.0f} < required {prereq['sentiment']:.0f}"
        )
        ready = False
    if mau_rate < prereq["mau_rate"]:
        warnings.append(
            f"MAU rate {mau_rate:.0f}% < required {prereq['mau_rate']:.0f}%"
        )
        ready = False
    return ready, warnings


def motivation_alignment(motivations: list[str], lever_key: str) -> str:
    aligned = sum(
        1 for m in motivations
        if m in MOTIVATION_PROGRAMME_FIT and lever_key in MOTIVATION_PROGRAMME_FIT[m]
    )
    total = len(motivations)
    if total == 0:
        return "Unknown"
    pct = aligned / total * 100
    if pct >= 60:
        return "HIGH"
    elif pct >= 30:
        return "MEDIUM"
    return "LOW"


def generate(data: dict) -> str:
    lever_key = data["primary_lever"]
    lever = GROWTH_LEVERS[lever_key]
    ready, warnings = check_health_prereq(data, lever)
    alignment = motivation_alignment(data["member_motivations"], lever_key)

    incentives_md = "\n".join(f"- {i}" for i in lever["incentives"])
    kpis_md = "\n".join(f"- {k}" for k in lever["kpis"])
    motivations_md = ", ".join(data["member_motivations"])

    prereq_status = "READY" if ready else "NOT READY — Address health gaps first"
    warnings_md = "\n".join(f"- {w}" for w in warnings) if warnings else "None"

    budget_per_pilot = data["incentive_budget_usd"] / max(data["pilot_cohort_size"], 1)

    lines = [
        f"# Community-Led Growth Programme: {data['community']}",
        "",
        "| Field | Value |",
        "|-------|-------|",
        f"| Community | {data['community']} |",
        f"| Product | {data['product']} |",
        f"| Stage | {data['stage'].title()} |",
        f"| Programme | {lever['name']} |",
        f"| Health Readiness | {prereq_status} |",
        f"| Motivation Alignment | {alignment} |",
        f"| Pilot Cohort Size | {data['pilot_cohort_size']} |",
        f"| Incentive Budget | ${data['incentive_budget_usd']:,.0f} |",
        f"| Skill | community-led-growth-designer |",
        "",
        "## Growth Readiness Assessment",
        "",
        f"**Status**: {prereq_status}",
        "",
        "**Health gap warnings:**",
        warnings_md,
        "",
        "## Programme Design",
        "",
        f"### {lever['name']}",
        "",
        f"**Description**: {lever['description']}",
        "",
        f"**Eligibility**: {lever['eligibility']}",
        "",
        "**Member motivations targeted:**",
        f"- Stated motivations: {motivations_md}",
        f"- Programme fit: {alignment}",
        "",
        "**Incentives:**",
        incentives_md,
        "",
        "**Success KPIs:**",
        kpis_md,
        "",
        "## Pilot Plan",
        "",
        f"| Parameter | Value |",
        "|-----------|-------|",
        f"| Pilot cohort size | {data['pilot_cohort_size']} members |",
        f"| Budget per participant | ${budget_per_pilot:,.0f} |",
        "| Pilot duration | 30 days |",
        "| Go/no-go criteria | 2+ KPIs at or above baseline |",
        "",
        "## Enablement Assets Required",
        "",
        "- [ ] Programme brief document (eligibility, rules, incentives)",
        "- [ ] Participant onboarding guide",
        "- [ ] Content templates / referral link / event scripts",
        "- [ ] Recognition system configured (badges, roles)",
        "- [ ] Tracking setup (referral codes or UTMs)",
        "",
        "## Rollout Timeline",
        "",
        "| Week | Activity |",
        "|------|----------|",
        "| Week 1 | Finalize programme design; build enablement assets |",
        "| Week 2 | Recruit pilot cohort; send invitations |",
        "| Week 3-6 | Run pilot; weekly check-ins with participants |",
        "| Week 6 | Evaluate pilot results against go/no-go criteria |",
        "| Week 8 | Full rollout if pilot successful |",
        "",
        "## Operational Playbook",
        "",
        "1. **Recruit**: Identify eligible members from platform analytics; send personal invitations",
        "2. **Onboard**: Walk participants through programme brief in a kick-off session",
        "3. **Enable**: Distribute enablement assets; answer questions in a dedicated programme channel",
        "4. **Recognise**: Celebrate participant wins publicly in the community weekly",
        "5. **Measure**: Track KPIs weekly; share results with participants to maintain momentum",
        "6. **Iterate**: Run monthly retrospective with participants; update programme based on feedback",
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Design community-led growth programme")
    parser.add_argument("-i", "--input", help="Input JSON file (default: stdin)")
    parser.add_argument("-o", "--output", help="Output Markdown file (default: stdout)")
    args = parser.parse_args()

    if args.input:
        with open(args.input) as f:
            data = json.load(f)
    else:
        data = json.load(sys.stdin)

    errors = validate_input(data)
    if errors:
        print("Input validation errors:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)

    output = generate(data)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Growth programme written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
