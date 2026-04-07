#!/usr/bin/env python3
"""Execute sales-signal-collector workflow to capture and tag deal signals."""
import json
import sys
from datetime import date

SIGNAL_TYPES = ["objection", "competitor", "trigger", "blocker", "feature_request", "timeline", "budget"]

MEDDIC_CRITERIA = ["Metrics", "Economic Buyer", "Decision Criteria", "Decision Process", "Identify Pain", "Champion"]


def run(context: dict) -> dict:
    """Process conversation signals into structured, tagged CRM entries."""
    results = {
        "skill": "sales-signal-collector",
        "date": date.today().isoformat(),
        "deal": context.get("deal_name", "[Unknown Deal]"),
        "signals": [],
        "patterns": [],
        "status": "complete",
    }

    raw_signals = context.get("signals", [])
    pattern_threshold = context.get("pattern_threshold", 3)

    for sig in raw_signals:
        processed = {
            "type": sig.get("type", "unknown"),
            "content": sig.get("content", ""),
            "context": sig.get("context", ""),
            "source": sig.get("source", "conversation"),
            "timestamp": sig.get("timestamp", date.today().isoformat()),
            "meddic_mapping": [],
            "deal_impact": sig.get("deal_impact", "neutral"),
        }
        # Validate signal type
        if processed["type"] not in SIGNAL_TYPES:
            processed["type"] = "unknown"
            processed["warning"] = f"Unrecognized signal type; valid types: {SIGNAL_TYPES}"

        # Map to MEDDIC criteria
        type_to_meddic = {
            "objection": ["Identify Pain", "Decision Criteria"],
            "competitor": ["Decision Criteria", "Decision Process"],
            "trigger": ["Metrics", "Identify Pain"],
            "blocker": ["Decision Process", "Economic Buyer"],
            "budget": ["Economic Buyer", "Metrics"],
            "timeline": ["Decision Process"],
            "feature_request": ["Decision Criteria", "Identify Pain"],
        }
        processed["meddic_mapping"] = type_to_meddic.get(processed["type"], [])
        results["signals"].append(processed)

    # Pattern detection
    type_counts = {}
    for sig in results["signals"]:
        t = sig["type"]
        type_counts[t] = type_counts.get(t, 0) + 1

    for sig_type, count in type_counts.items():
        if count >= pattern_threshold:
            results["patterns"].append({
                "type": sig_type,
                "frequency": count,
                "action": "Escalate to Sales Manager — pattern threshold met",
            })

    results["signal_count"] = len(results["signals"])
    results["pattern_count"] = len(results["patterns"])
    return results


if __name__ == "__main__":
    data = json.load(sys.stdin) if not sys.stdin.isatty() else json.loads(sys.argv[1])
    print(json.dumps(run(data), indent=2))
