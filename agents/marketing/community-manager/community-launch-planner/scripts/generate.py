#!/usr/bin/env python3
"""
community-launch-planner — Generate community launch plan.
Input (JSON via stdin or -i):
  {
    "community": str,
    "platform": str,
    "product": str,
    "launch_date": str,          # ISO format YYYY-MM-DD
    "soft_launch_date": str,     # ISO format, before launch_date
    "member_target_week1": int,
    "member_target_month1": int,
    "activation_rate_target_pct": float,  # % of joined who activate
    "seed_member_count": int,    # existing beta/early members
    "channels": list[str],       # announcement channels: "Email", "Twitter", "ProductHunt", etc.
    "team_coverage": {
      "moderator_count": int,
      "hours_per_day": float     # coverage hours during launch week
    }
  }
Output: Community launch plan as Markdown.
"""

import json
import sys
import argparse
from datetime import datetime, timedelta

READINESS_ITEMS = [
    ("Platform configured", "Platform setup, categories/channels created"),
    ("Welcome flow live", "New member welcome message and onboarding checklist active"),
    ("Community guidelines published", "Rules and code of conduct visible to all members"),
    ("Seed content posted", "Minimum 10 starter posts/threads live"),
    ("Moderation team briefed", "Moderators trained on escalation paths and policies"),
    ("Announcement content ready", "Launch posts, email, social copy reviewed and approved"),
    ("Support escalation path defined", "Clear handoff process from community to support team"),
    ("Analytics tracking live", "Member join, post, and retention events being captured"),
]

SOFT_LAUNCH_MILESTONES = [
    ("Invite seed members", "Send personal invitations to founding/beta cohort"),
    ("Run platform stress test", "Simulate peak load, check notification flows"),
    ("Collect soft-launch feedback", "Gather input from seed members on experience"),
    ("Fix identified bugs", "Address platform and flow issues from soft launch"),
    ("Final readiness sign-off", "Community Manager confirms all checks passed"),
]

LAUNCH_WEEK_ACTIVITIES = [
    ("Day 1", "Publish announcement across all channels, monitor join rate hourly"),
    ("Day 1", "Welcome all new members personally (or via automated welcome bot)"),
    ("Day 2", "Post first community discussion prompt to seed conversation"),
    ("Day 3", "Share a 'behind the scenes' or founder story post to build connection"),
    ("Day 4", "Run first scheduled community event (Q&A, AMA, or demo)"),
    ("Day 5", "Identify and acknowledge most active new members publicly"),
    ("Day 7", "Publish Week 1 community recap — celebrate milestones hit"),
]

CONTENT_SEED_TEMPLATES = [
    "Introductions thread — 'Tell us who you are and why you joined'",
    "Wins thread — 'Share your first win with {product}'",
    "Questions thread — 'What's your biggest question about {product}?'",
    "Resources post — 'Start here: Essential links and guides'",
    "Roadmap teaser — 'What's coming next — we want your input'",
]


def validate_input(data: dict) -> list[str]:
    required = [
        "community", "platform", "product", "launch_date", "soft_launch_date",
        "member_target_week1", "member_target_month1",
        "activation_rate_target_pct", "seed_member_count",
        "channels", "team_coverage"
    ]
    errors = []
    for field in required:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "team_coverage" in data:
        if "moderator_count" not in data["team_coverage"]:
            errors.append("Missing team_coverage.moderator_count")
        if "hours_per_day" not in data["team_coverage"]:
            errors.append("Missing team_coverage.hours_per_day")
    if "soft_launch_date" in data and "launch_date" in data:
        try:
            soft = datetime.strptime(data["soft_launch_date"], "%Y-%m-%d")
            launch = datetime.strptime(data["launch_date"], "%Y-%m-%d")
            if soft >= launch:
                errors.append("soft_launch_date must be before launch_date")
        except ValueError:
            errors.append("Dates must be in YYYY-MM-DD format")
    return errors


def build_timeline(data: dict) -> list[tuple[str, str, str]]:
    soft = datetime.strptime(data["soft_launch_date"], "%Y-%m-%d")
    launch = datetime.strptime(data["launch_date"], "%Y-%m-%d")

    pre_soft = soft - timedelta(days=7)
    post_launch = launch + timedelta(days=7)
    month_post = launch + timedelta(days=30)

    return [
        (pre_soft.strftime("%Y-%m-%d"), "Pre-launch", "Complete readiness checklist; brief moderation team"),
        (soft.strftime("%Y-%m-%d"), "Soft Launch", "Invite seed members; stress test platform; collect feedback"),
        ((soft + timedelta(days=3)).strftime("%Y-%m-%d"), "Soft Launch +3d", "Fix bugs; finalize launch content package"),
        (launch.strftime("%Y-%m-%d"), "Public Launch", "Announce across all channels; activate welcome flows"),
        (post_launch.strftime("%Y-%m-%d"), "Launch +7d", "Publish Week 1 recap; identify power users"),
        (month_post.strftime("%Y-%m-%d"), "Launch +30d", "Post-launch retrospective; hand off to ongoing operations"),
    ]


def generate(data: dict) -> str:
    product = data["product"]
    community = data["community"]
    channels_md = ", ".join(data["channels"])
    seed_content = "\n".join(
        f"- {t.format(product=product)}" for t in CONTENT_SEED_TEMPLATES
    )

    timeline = build_timeline(data)
    timeline_rows = "\n".join(
        f"| {date} | {phase} | {activity} |"
        for date, phase, activity in timeline
    )

    readiness_rows = "\n".join(
        f"| {item} | {desc} | [ ] |"
        for item, desc in READINESS_ITEMS
    )

    soft_milestones = "\n".join(
        f"- **{m}**: {desc}" for m, desc in SOFT_LAUNCH_MILESTONES
    )

    launch_week = "\n".join(
        f"- **{day}**: {activity}" for day, activity in LAUNCH_WEEK_ACTIVITIES
    )

    coverage = data["team_coverage"]
    coverage_gap = "WARNING: Less than 8 hours daily coverage during launch week" \
        if coverage["hours_per_day"] < 8 else "Coverage meets minimum for launch"

    lines = [
        f"# Community Launch Plan: {community}",
        "",
        "| Field | Value |",
        "|-------|-------|",
        f"| Community | {community} |",
        f"| Platform | {data['platform']} |",
        f"| Product | {product} |",
        f"| Soft Launch | {data['soft_launch_date']} |",
        f"| Public Launch | {data['launch_date']} |",
        f"| Week 1 Member Target | {data['member_target_week1']:,} |",
        f"| Month 1 Member Target | {data['member_target_month1']:,} |",
        f"| Activation Rate Target | {data['activation_rate_target_pct']:.0f}% |",
        f"| Seed Members | {data['seed_member_count']:,} |",
        f"| Announcement Channels | {channels_md} |",
        f"| Skill | community-launch-planner |",
        "",
        "## Launch Timeline",
        "",
        "| Date | Phase | Activity |",
        "|------|-------|----------|",
        timeline_rows,
        "",
        "## Readiness Checklist",
        "",
        "| Item | Description | Done |",
        "|------|-------------|------|",
        readiness_rows,
        "",
        "## Soft Launch Plan",
        "",
        soft_milestones,
        "",
        "## Launch Week Playbook",
        "",
        launch_week,
        "",
        "## Content Seed Package",
        "",
        "Minimum 10 seed posts required before launch. Starter templates:",
        "",
        seed_content,
        "",
        "## Team Coverage",
        "",
        f"- Moderators: **{coverage['moderator_count']}**",
        f"- Daily coverage hours: **{coverage['hours_per_day']}**",
        f"- Coverage assessment: **{coverage_gap}**",
        "",
        "## Success Metrics",
        "",
        "| Metric | Target | When |",
        "|--------|--------|------|",
        f"| Members joined | {data['member_target_week1']:,} | Week 1 |",
        f"| Activation rate | {data['activation_rate_target_pct']:.0f}% | Week 1 |",
        f"| Members (cumulative) | {data['member_target_month1']:,} | Month 1 |",
        "| Response time | <8 hours | Launch week |",
        "| Zero unmoderated incidents | 0 | First 72 hours |",
        "",
        "## Post-Launch Retrospective Template",
        "",
        "- Did we hit Week 1 member target? (Y/N + delta)",
        "- What was the activation rate vs target?",
        "- What content performed best?",
        "- What moderation issues arose?",
        "- What would we do differently?",
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Generate community launch plan")
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
        print(f"Launch plan written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
