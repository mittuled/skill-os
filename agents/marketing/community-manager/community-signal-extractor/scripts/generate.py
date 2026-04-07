#!/usr/bin/env python3
"""
community-signal-extractor — Extract and prioritize signals from community conversations.
Input (JSON via stdin or -i):
  {
    "community": str,
    "product": str,
    "period": str,           # e.g. "March 2026"
    "signals": [
      {
        "text": str,         # raw signal or paraphrase of conversation
        "source": str,       # channel/thread/forum name
        "author_type": str,  # "power_user", "new_member", "churned", "prospect"
        "frequency": int     # how many times similar signal appeared
      }
    ]
  }
Output: Prioritized signal report as Markdown.
"""

import json
import sys
import argparse

# Signal taxonomy with routing targets
SIGNAL_CATEGORIES = {
    "feature_request": {
        "label": "Feature Request",
        "keywords": ["wish", "would be great", "add", "feature", "support", "request", "need", "want", "missing"],
        "route_to": "Product",
        "severity_base": 5,
    },
    "pain_point": {
        "label": "Pain Point / Bug",
        "keywords": ["broken", "bug", "error", "crash", "slow", "frustrating", "annoying", "fails", "doesn't work", "hate"],
        "route_to": "Engineering",
        "severity_base": 8,
    },
    "praise": {
        "label": "Praise / Win",
        "keywords": ["love", "amazing", "great", "awesome", "best", "thank", "helped", "works perfectly", "fast"],
        "route_to": "Marketing",
        "severity_base": 3,
    },
    "competitor_mention": {
        "label": "Competitor Mention",
        "keywords": ["vs", "compared to", "switched from", "better than", "worse than", "alternative", "competitor"],
        "route_to": "Marketing / Product",
        "severity_base": 7,
    },
    "churn_indicator": {
        "label": "Churn Indicator",
        "keywords": ["cancel", "leaving", "switching", "unsubscribe", "quit", "too expensive", "not worth"],
        "route_to": "Customer Success",
        "severity_base": 10,
    },
    "use_case_discovery": {
        "label": "Use Case Discovery",
        "keywords": ["using it for", "we use", "our team uses", "built with", "workflow"],
        "route_to": "Product / Marketing",
        "severity_base": 4,
    },
}

AUTHOR_WEIGHT = {
    "power_user": 2.0,
    "new_member": 0.8,
    "churned": 1.5,
    "prospect": 1.2,
}


def validate_input(data: dict) -> list[str]:
    required = ["community", "product", "period", "signals"]
    errors = []
    for field in required:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "signals" in data and len(data["signals"]) == 0:
        errors.append("signals list is empty")
    return errors


def classify_signal(signal: dict) -> str:
    text_lower = signal["text"].lower()
    scores = {}
    for cat_key, cat in SIGNAL_CATEGORIES.items():
        hit_count = sum(1 for kw in cat["keywords"] if kw in text_lower)
        if hit_count > 0:
            scores[cat_key] = hit_count
    if not scores:
        return "use_case_discovery"  # default fallback
    return max(scores, key=lambda k: scores[k])


def compute_priority_score(signal: dict, category_key: str) -> float:
    base = SIGNAL_CATEGORIES[category_key]["severity_base"]
    author_weight = AUTHOR_WEIGHT.get(signal.get("author_type", "new_member"), 1.0)
    freq = signal.get("frequency", 1)
    return base * author_weight * min(freq, 10) / 10 * 10


def generate(data: dict) -> str:
    signals = data["signals"]

    # Classify and score
    enriched = []
    for s in signals:
        cat_key = classify_signal(s)
        cat = SIGNAL_CATEGORIES[cat_key]
        priority = compute_priority_score(s, cat_key)
        enriched.append({
            **s,
            "category_key": cat_key,
            "category_label": cat["label"],
            "route_to": cat["route_to"],
            "priority_score": priority,
        })

    # Sort by priority
    enriched.sort(key=lambda x: x["priority_score"], reverse=True)

    # Cluster by category
    clusters: dict[str, list] = {}
    for s in enriched:
        key = s["category_key"]
        clusters.setdefault(key, []).append(s)

    # Signal table rows
    signal_rows = "\n".join(
        f"| {s['category_label']} | {s['text'][:60]}{'...' if len(s['text']) > 60 else ''} | "
        f"{s['source']} | {s['author_type']} | {s['frequency']}x | "
        f"{s['priority_score']:.0f} | {s['route_to']} |"
        for s in enriched[:20]  # top 20
    )

    # Theme clusters
    cluster_section = []
    for cat_key, sigs in sorted(clusters.items(), key=lambda x: -max(s["priority_score"] for s in x[1])):
        cat = SIGNAL_CATEGORIES[cat_key]
        total_freq = sum(s["frequency"] for s in sigs)
        top_signal = max(sigs, key=lambda s: s["priority_score"])
        cluster_section.append(
            f"### {cat['label']} ({len(sigs)} signals, {total_freq} mentions)\n\n"
            f"- Route to: **{cat['route_to']}**\n"
            f"- Top signal: _{top_signal['text'][:80]}_\n"
            f"- Source: {top_signal['source']} ({top_signal['author_type']})\n"
        )

    cluster_md = "\n".join(cluster_section)

    # Strategic implications
    implications = []
    if "churn_indicator" in clusters:
        implications.append(
            f"**Retention risk**: {len(clusters['churn_indicator'])} churn signals detected — "
            "escalate to Customer Success immediately"
        )
    if "pain_point" in clusters:
        implications.append(
            f"**Product quality**: {len(clusters['pain_point'])} pain point signals — "
            "file bug reports and prioritize in next sprint"
        )
    if "feature_request" in clusters:
        top_req = max(clusters["feature_request"], key=lambda s: s["frequency"])
        implications.append(
            f"**Product direction**: Most requested feature: '{top_req['text'][:60]}' "
            f"({top_req['frequency']} mentions) — add to product backlog"
        )
    if "competitor_mention" in clusters:
        implications.append(
            f"**Competitive intelligence**: {len(clusters['competitor_mention'])} competitor mentions — "
            "review for battlecard updates"
        )

    implications_md = "\n".join(f"{i+1}. {imp}" for i, imp in enumerate(implications)) \
        if implications else "No material strategic implications from this signal set."

    category_counts = {k: len(v) for k, v in clusters.items()}
    top_category = max(category_counts, key=category_counts.get) if category_counts else "—"

    lines = [
        f"# Community Signal Report: {data['community']} — {data['period']}",
        "",
        "| Field | Value |",
        "|-------|-------|",
        f"| Community | {data['community']} |",
        f"| Product | {data['product']} |",
        f"| Period | {data['period']} |",
        f"| Total Signals | {len(signals)} |",
        f"| Dominant Category | {SIGNAL_CATEGORIES.get(top_category, {}).get('label', top_category)} |",
        f"| Skill | community-signal-extractor |",
        "",
        "## Signal Distribution",
        "",
        "| Category | Count |",
        "|----------|-------|",
    ] + [
        f"| {SIGNAL_CATEGORIES[k]['label']} | {v} |"
        for k, v in sorted(category_counts.items(), key=lambda x: -x[1])
    ] + [
        "",
        "## Tagged Signal Database (Top 20 by Priority)",
        "",
        "| Category | Signal | Source | Author | Frequency | Priority | Route To |",
        "|----------|--------|--------|--------|-----------|----------|----------|",
        signal_rows,
        "",
        "## Theme Clusters",
        "",
        cluster_md,
        "## Strategic Implications",
        "",
        implications_md,
        "",
        "## Distribution Plan",
        "",
        "| Stakeholder | Signal Categories | Format |",
        "|------------|-------------------|--------|",
        "| Product team | Feature requests, Pain points | Weekly signal digest |",
        "| Engineering | Pain points / Bugs | Jira tickets |",
        "| Marketing | Praise, Competitor mentions | Monthly insight memo |",
        "| Customer Success | Churn indicators | Immediate escalation |",
        "| Leadership | All | Monthly community insights report |",
    ]

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Extract community signals")
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
        print(f"Signal report written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
