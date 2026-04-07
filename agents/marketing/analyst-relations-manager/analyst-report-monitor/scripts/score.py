#!/usr/bin/env python3
"""
score.py — Score and classify analyst report mentions by sentiment, positioning impact, and competitive intelligence value.

Usage:
    echo '<json>' | python3 score.py
    python3 score.py < input.json
    python3 score.py < input.json -o output.json

Dependencies: Python 3.10+ standard library only.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

MENTION_SENTIMENTS = ["positive", "neutral", "negative", "mixed"]
MENTION_TYPES = ["category_leader", "challenger", "niche_player", "not_mentioned", "negative_mention", "competitive_reference"]
DISTRIBUTION_PRIORITY = {
    "category_leader": ["sales_enablement", "marketing", "leadership"],
    "negative_mention": ["leadership", "product", "marketing"],
    "competitive_reference": ["sales_enablement", "product"],
    "challenger": ["marketing", "sales_enablement"],
    "niche_player": ["marketing"],
    "not_mentioned": ["ar_manager"],
}

REQUIRED_FIELDS = ["report_title", "analyst_firm", "publication_date", "mentions"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "mentions" in data:
        for i, mention in enumerate(data["mentions"]):
            for field in ["mention_type", "excerpt"]:
                if field not in mention:
                    errors.append(f"Mention {i}: missing field '{field}'")
    return errors


def score_report(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    mentions = data["mentions"]
    classified = []
    overall_sentiment_score = 0.0
    sentiment_weights = {"positive": 10, "neutral": 5, "mixed": 4, "negative": 1}

    for mention in mentions:
        mention_type = mention["mention_type"]
        sentiment = mention.get("sentiment", "neutral")
        sentiment_score = sentiment_weights.get(sentiment, 5)
        overall_sentiment_score += sentiment_score

        distribution = DISTRIBUTION_PRIORITY.get(mention_type, ["ar_manager"])
        action_required = mention_type in ["negative_mention", "not_mentioned"]

        classified.append({
            "mention_type": mention_type,
            "sentiment": sentiment,
            "sentiment_score": sentiment_score,
            "excerpt": mention["excerpt"][:300],
            "distribute_to": distribution,
            "action_required": action_required,
            "recommended_action": "Brief leadership and develop response messaging" if mention_type == "negative_mention" else
                                  ("Update AR strategy for next briefing cycle" if mention_type == "not_mentioned" else
                                   "Create sales enablement snippet from this excerpt"),
        })

    avg_sentiment = overall_sentiment_score / max(len(mentions), 1)
    positive_count = sum(1 for m in classified if m["sentiment"] == "positive")
    negative_count = sum(1 for m in classified if m["sentiment"] == "negative")

    if avg_sentiment >= 8:
        report_verdict = "STRONG POSITIVE — share widely with sales and marketing"
    elif avg_sentiment >= 5:
        report_verdict = "NEUTRAL — selective sharing; extract any positive snippets"
    else:
        report_verdict = "NEGATIVE — limit distribution; prepare response strategy"

    return {
        "error": None,
        "result": {
            "report_title": data["report_title"],
            "analyst_firm": data["analyst_firm"],
            "publication_date": data["publication_date"],
            "total_mentions": len(mentions),
            "positive_mentions": positive_count,
            "negative_mentions": negative_count,
            "average_sentiment_score": round(avg_sentiment, 1),
            "report_verdict": report_verdict,
            "classified_mentions": classified,
            "priority_actions": [m["recommended_action"] for m in classified if m["action_required"]],
            "competitive_intelligence": [m["excerpt"] for m in classified if m["mention_type"] == "competitive_reference"],
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = score_report(data)
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
