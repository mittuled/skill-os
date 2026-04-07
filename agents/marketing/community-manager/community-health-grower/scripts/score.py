#!/usr/bin/env python3
"""
community-health-grower — Score community health and recommend interventions.
Input (JSON via stdin or -i):
  {
    "community": str,
    "platform": str,         # "Discord", "Slack", "Circle", "Discourse", etc.
    "stage": str,            # "early" (<6mo), "growing" (6-18mo), "mature" (18mo+)
    "total_members": int,
    "mau": int,              # monthly active users
    "dau": int,              # daily active users
    "posts_per_member_monthly": float,
    "median_response_time_hours": float,
    "month1_retention_pct": float,   # % of new members still active after 1 month
    "month3_retention_pct": float,
    "net_sentiment_score": float,    # -100 to +100 (NPS-style)
    "content_contributor_pct": float # % of members who have posted at least once in 30d
  }
Output: Community health scorecard as Markdown.
"""

import json
import sys
import argparse

# Benchmark targets by community stage
STAGE_BENCHMARKS = {
    "early": {
        "mau_rate_pct": 40,          # % of total members who are MAU
        "dau_mau_ratio": 0.12,
        "posts_per_member": 1.5,
        "response_time_hours": 4,
        "month1_retention_pct": 40,
        "month3_retention_pct": 25,
        "net_sentiment": 30,
        "contributor_pct": 20,
    },
    "growing": {
        "mau_rate_pct": 30,
        "dau_mau_ratio": 0.10,
        "posts_per_member": 1.0,
        "response_time_hours": 8,
        "month1_retention_pct": 35,
        "month3_retention_pct": 20,
        "net_sentiment": 20,
        "contributor_pct": 15,
    },
    "mature": {
        "mau_rate_pct": 20,
        "dau_mau_ratio": 0.08,
        "posts_per_member": 0.7,
        "response_time_hours": 12,
        "month1_retention_pct": 25,
        "month3_retention_pct": 15,
        "net_sentiment": 15,
        "contributor_pct": 10,
    },
}

HEALTH_DIMENSIONS = [
    "activity",
    "retention",
    "sentiment",
    "responsiveness",
    "contribution",
]

INTERVENTIONS = {
    "activity": [
        "Launch a weekly prompt thread to stimulate discussion",
        "Run a 30-day engagement challenge with recognition rewards",
        "Schedule a community AMA with a founder or power user",
    ],
    "retention": [
        "Implement a personalised welcome sequence for new members",
        "Create an onboarding checklist tied to first-value actions",
        "Run a win-back campaign for members inactive >30 days",
    ],
    "sentiment": [
        "Conduct a community pulse survey to identify root cause",
        "Review moderation logs for recent enforcement controversies",
        "Host a community feedback session with leadership visibility",
    ],
    "responsiveness": [
        "Assign dedicated response windows to community team members",
        "Identify and empower 3-5 power users as unofficial responders",
        "Set up auto-acknowledgment for unanswered posts >4 hours",
    ],
    "contribution": [
        "Launch a 'first post' challenge with a low barrier prompt",
        "Create a content template library for easy member contributions",
        "Give contributor recognition (badges, shoutouts) to incentivise posting",
    ],
}


def validate_input(data: dict) -> list[str]:
    required = [
        "community", "platform", "stage", "total_members", "mau", "dau",
        "posts_per_member_monthly", "median_response_time_hours",
        "month1_retention_pct", "month3_retention_pct",
        "net_sentiment_score", "content_contributor_pct"
    ]
    errors = []
    for field in required:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "stage" in data and data["stage"] not in STAGE_BENCHMARKS:
        errors.append(f"stage must be one of: {list(STAGE_BENCHMARKS.keys())}")
    return errors


def score_dimension(name: str, actual: float, benchmark: float, higher_is_better: bool = True) -> dict:
    if higher_is_better:
        ratio = actual / benchmark if benchmark > 0 else 0
    else:
        ratio = benchmark / actual if actual > 0 else 0

    if ratio >= 1.2:
        grade = "EXCELLENT"
        score = 10
    elif ratio >= 1.0:
        grade = "GOOD"
        score = 8
    elif ratio >= 0.75:
        grade = "NEEDS WORK"
        score = 5
    elif ratio >= 0.5:
        grade = "AT RISK"
        score = 3
    else:
        grade = "CRITICAL"
        score = 1

    return {
        "name": name,
        "actual": actual,
        "benchmark": benchmark,
        "score": score,
        "grade": grade,
        "ratio": ratio,
    }


def compute_scores(data: dict, benchmarks: dict) -> dict:
    mau_rate = data["mau"] / data["total_members"] * 100 if data["total_members"] > 0 else 0
    dau_mau = data["dau"] / data["mau"] if data["mau"] > 0 else 0

    activity_score = score_dimension(
        "Activity (MAU rate)",
        mau_rate,
        benchmarks["mau_rate_pct"],
    )
    activity_score["detail"] = f"DAU/MAU ratio: {dau_mau:.2f} (benchmark: {benchmarks['dau_mau_ratio']:.2f})"

    retention_score = score_dimension(
        "Retention (M1)",
        data["month1_retention_pct"],
        benchmarks["month1_retention_pct"],
    )
    retention_score["detail"] = f"M3 retention: {data['month3_retention_pct']:.0f}% (benchmark: {benchmarks['month3_retention_pct']:.0f}%)"

    sentiment_score = score_dimension(
        "Sentiment",
        data["net_sentiment_score"],
        benchmarks["net_sentiment"],
    )
    sentiment_score["detail"] = "Net sentiment score (NPS-style, range -100 to +100)"

    responsiveness_score = score_dimension(
        "Responsiveness",
        data["median_response_time_hours"],
        benchmarks["response_time_hours"],
        higher_is_better=False,
    )
    responsiveness_score["detail"] = "Median hours to first response on posts"

    contribution_score = score_dimension(
        "Content Contribution",
        data["content_contributor_pct"],
        benchmarks["contributor_pct"],
    )
    contribution_score["detail"] = f"% members who posted at least once in 30 days"

    return {
        "activity": activity_score,
        "retention": retention_score,
        "sentiment": sentiment_score,
        "responsiveness": responsiveness_score,
        "contribution": contribution_score,
    }


def overall_health(scores: dict) -> tuple[float, str]:
    avg = sum(s["score"] for s in scores.values()) / len(scores)
    if avg >= 8.5:
        label = "THRIVING"
    elif avg >= 7.0:
        label = "HEALTHY"
    elif avg >= 5.0:
        label = "NEEDS ATTENTION"
    elif avg >= 3.0:
        label = "AT RISK"
    else:
        label = "CRITICAL"
    return avg, label


def priority_gaps(scores: dict) -> list[str]:
    return sorted(
        [k for k, v in scores.items() if v["grade"] in ("AT RISK", "CRITICAL", "NEEDS WORK")],
        key=lambda k: scores[k]["score"]
    )


def score_output(data: dict) -> str:
    benchmarks = STAGE_BENCHMARKS[data["stage"]]
    scores = compute_scores(data, benchmarks)
    avg, health_label = overall_health(scores)
    gaps = priority_gaps(scores)

    # Top 2 interventions from worst dimensions
    recommended_interventions = []
    for dim in gaps[:2]:
        for ix in INTERVENTIONS.get(dim, [])[:2]:
            recommended_interventions.append(f"[{dim.title()}] {ix}")

    score_rows = "\n".join(
        f"| {v['name']} | {v['actual']:.1f} | {v['benchmark']:.1f} | {v['score']}/10 | {v['grade']} |"
        for v in scores.values()
    )

    gaps_md = "\n".join(
        f"{i+1}. **{g.title()}** (score: {scores[g]['score']}/10, grade: {scores[g]['grade']}) — {scores[g]['detail']}"
        for i, g in enumerate(gaps)
    ) if gaps else "No critical gaps identified."

    interventions_md = "\n".join(
        f"{i+1}. {iv}" for i, iv in enumerate(recommended_interventions)
    ) if recommended_interventions else "Maintain current initiatives."

    lines = [
        f"# Community Health Scorecard: {data['community']}",
        "",
        "| Field | Value |",
        "|-------|-------|",
        f"| Community | {data['community']} |",
        f"| Platform | {data['platform']} |",
        f"| Stage | {data['stage'].title()} |",
        f"| Total Members | {data['total_members']:,} |",
        f"| Health Status | {health_label} |",
        f"| Overall Score | {avg:.1f}/10 |",
        f"| Skill | community-health-grower |",
        "",
        "## Health Dimension Scores",
        "",
        "| Dimension | Actual | Benchmark | Score | Grade |",
        "|-----------|--------|-----------|-------|-------|",
        score_rows,
        "",
        "## Prioritised Gaps",
        "",
        gaps_md,
        "",
        "## Recommended Interventions",
        "",
        interventions_md,
        "",
        "## Measurement Cadence",
        "",
        "| Metric | Frequency | Owner |",
        "|--------|-----------|-------|",
        "| Activity (MAU/DAU) | Weekly | Community Manager |",
        "| Retention cohorts | Monthly | Community Manager |",
        "| Sentiment survey | Monthly | Community Manager |",
        "| Response time | Weekly | Community Manager |",
        "| Contributor rate | Monthly | Community Manager |",
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Score community health")
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

    output = score_output(data)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Health scorecard written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
