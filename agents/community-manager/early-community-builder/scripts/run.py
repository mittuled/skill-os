#!/usr/bin/env python3
"""
early-community-builder — Run early community building workflow.
Input (JSON via stdin or -i):
  {
    "community": str,
    "product": str,
    "platform": str,
    "purpose": str,          # one-sentence community purpose
    "target_persona": str,   # e.g. "B2B SaaS engineers", "indie developers"
    "founding_member_target": int,  # typically 20-50
    "sourcing_channels": list[str], # e.g. ["email_list", "twitter", "linkedin", "slack"]
    "launch_date": str,      # ISO YYYY-MM-DD
    "weekly_rituals": list[str]  # proposed recurring activities
  }
Output: Early community building plan as Markdown.
"""

import json
import sys
import argparse
from datetime import datetime, timedelta

FOUNDING_MEMBER_CRITERIA = [
    "Actively uses or is evaluating the product",
    "Has relevant domain expertise to contribute",
    "Willing to engage publicly (post, share, respond)",
    "Has network influence in the target persona group",
    "Available for 30-60 min/month of structured engagement",
]

NORM_CATEGORIES = [
    ("Posting norms", "What types of posts are encouraged; what is off-topic"),
    ("Response expectations", "How quickly members should expect responses from the team"),
    ("Confidentiality", "What community content may be shared outside"),
    ("Conflict resolution", "How to handle disagreements and escalation paths"),
    ("Commercial activity", "Rules on self-promotion, job posts, and advertising"),
]

WEEK_BY_WEEK = [
    (1, "Recruit", "Send personal invitations to 2× founding target; brief founding members on community purpose"),
    (2, "Onboard", "Walk accepted members through platform; co-create initial community guidelines"),
    (3, "Seed content", "Publish all seed posts; run first founding member ritual"),
    (4, "Nurture", "Follow up with every member personally; identify early power contributors"),
    (6, "Assess", "Run first health check: response rate, post count, engagement per member"),
    (8, "Stabilise", "Resolve any moderation issues; confirm rituals are self-sustaining"),
    (12, "Hand off", "Transition to ongoing community operations with established health baselines"),
]

SEED_POST_TYPES = [
    "Introductions thread — invite everyone to introduce themselves",
    "Purpose post — explain why this community exists and what members get",
    "First question post — ask a question only this community can answer",
    "Resource post — curated links and guides for the target persona",
    "Roadmap tease — share something coming soon and ask for input",
    "Behind the scenes — founder or team story that builds trust",
    "Community norm post — share the guidelines in a conversational way",
    "Win celebration — celebrate a member achievement publicly",
    "Challenge post — invite members to share their biggest challenge",
    "Event invitation — announce the first community ritual/event",
]


def validate_input(data: dict) -> list[str]:
    required = [
        "community", "product", "platform", "purpose", "target_persona",
        "founding_member_target", "sourcing_channels", "launch_date", "weekly_rituals"
    ]
    errors = []
    for field in required:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "founding_member_target" in data:
        if data["founding_member_target"] < 10:
            errors.append("founding_member_target should be at least 10 for a viable founding cohort")
        if data["founding_member_target"] > 100:
            errors.append("founding_member_target above 100 is too large for a founding cohort — aim for 20-50")
    return errors


def build_outreach_plan(channels: list[str], target: int) -> list[dict]:
    allocations = []
    per_channel = max(1, target // len(channels)) if channels else target
    for ch in channels:
        allocations.append({
            "channel": ch,
            "target_invites": int(per_channel * 2),  # 2× for conversion buffer
            "expected_accepts": per_channel,
            "message_type": "Personal, 2-sentence invite referencing their specific work",
        })
    return allocations


def build_timeline(data: dict) -> list[tuple[str, str, str]]:
    launch = datetime.strptime(data["launch_date"], "%Y-%m-%d")
    entries = []
    for week_offset, phase, activity in WEEK_BY_WEEK:
        date = launch - timedelta(weeks=12) + timedelta(weeks=week_offset)
        entries.append((date.strftime("%Y-%m-%d"), f"Week {week_offset}: {phase}", activity))
    return entries


def run(data: dict) -> str:
    target = data["founding_member_target"]
    outreach = build_outreach_plan(data["sourcing_channels"], target)
    timeline = build_timeline(data)
    rituals_md = "\n".join(f"- {r}" for r in data["weekly_rituals"])
    seed_posts_md = "\n".join(f"- {p}" for p in SEED_POST_TYPES)
    criteria_md = "\n".join(f"- {c}" for c in FOUNDING_MEMBER_CRITERIA)
    norms_md = "\n".join(f"- **{cat}**: {desc}" for cat, desc in NORM_CATEGORIES)

    outreach_rows = "\n".join(
        f"| {o['channel']} | {o['target_invites']} invites | {o['expected_accepts']} | {o['message_type']} |"
        for o in outreach
    )

    timeline_rows = "\n".join(
        f"| {date} | {phase} | {activity} |"
        for date, phase, activity in timeline
    )

    lines = [
        f"# Early Community Building Plan: {data['community']}",
        "",
        "| Field | Value |",
        "|-------|-------|",
        f"| Community | {data['community']} |",
        f"| Product | {data['product']} |",
        f"| Platform | {data['platform']} |",
        f"| Target Persona | {data['target_persona']} |",
        f"| Founding Member Target | {target} |",
        f"| Launch Date | {data['launch_date']} |",
        f"| Skill | early-community-builder |",
        "",
        "## Community Purpose Statement",
        "",
        f"> {data['purpose']}",
        "",
        "## Founding Member Profile",
        "",
        "**Eligibility criteria:**",
        criteria_md,
        "",
        "## Outreach Plan",
        "",
        "| Channel | Volume | Expected Accepts | Message Style |",
        "|---------|--------|-----------------|---------------|",
        outreach_rows,
        "",
        f"**Total invites to send**: {sum(o['target_invites'] for o in outreach)} (targeting {target} accepted members)",
        "",
        "## Community Guidelines Framework",
        "",
        norms_md,
        "",
        "*(Co-create the actual wording with founding members in Week 2)*",
        "",
        "## Ritual Calendar",
        "",
        rituals_md,
        "",
        "## Content Seed Package (Minimum 10 posts before launch)",
        "",
        seed_posts_md,
        "",
        "## 12-Week Timeline",
        "",
        "| Date | Phase | Activity |",
        "|------|-------|----------|",
        timeline_rows,
        "",
        "## Founding Cohort Activity Targets",
        "",
        "| Week | Target |",
        "|------|--------|",
        f"| Week 1 | {target} founding members recruited |",
        f"| Week 2 | {max(1, target // 2)} members active (posted or reacted) |",
        f"| Week 4 | {max(1, int(target * 0.7))} members active; first ritual completed |",
        f"| Week 8 | {max(1, int(target * 0.5))} members active; community self-sustaining |",
        "",
        "## Monitoring Signals (Weekly)",
        "",
        "- Member response rate to posts (target: >60% in first 4 weeks)",
        "- Average posts per member per week (target: >0.5)",
        "- Member churn from founding cohort (flag if >10% leave in first 4 weeks)",
        "- Team response time to member posts (target: <4 hours in early weeks)",
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Run early community building workflow")
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

    output = run(data)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Community building plan written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
