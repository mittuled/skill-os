#!/usr/bin/env python3
"""
generate.py — Generate a launch narrative visual asset plan for product and company launches.

Usage:
    echo '<json>' | python3 generate.py
    python3 generate.py < input.json
    python3 generate.py < input.json -o output.json

Dependencies: Python 3.10+ standard library only.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

LAUNCH_ASSET_TYPES = {
    "hero_visual": "Primary launch image: product screenshot, illustration, or conceptual visual",
    "social_card": "OG image for website and social sharing (1200x630px)",
    "twitter_thread_visuals": "Visual thread cards for launch thread (1080x1080px)",
    "product_hunt_thumbnail": "Product Hunt thumbnail (240x240px) and banner (1270x760px)",
    "email_header": "Launch email hero image (600px wide)",
    "press_kit": "Brand assets for journalists: logo files, screenshots, founder photos",
    "demo_gif": "Animated product demo for website and social (max 10 seconds)",
    "testimonial_cards": "Customer quote cards for social proof on launch day",
}

LAUNCH_CHANNELS = ["website", "product_hunt", "twitter_x", "linkedin", "email_list", "hacker_news", "press"]

REQUIRED_FIELDS = ["launch_name", "launch_type", "core_message", "target_channels"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    for channel in data.get("target_channels", []):
        if channel not in LAUNCH_CHANNELS:
            errors.append(f"channel must be one of {LAUNCH_CHANNELS}")
    return errors


def generate_narrative_plan(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    channels = data["target_channels"]
    asset_needs = []

    # Map channels to required assets
    if "website" in channels:
        asset_needs.extend(["hero_visual", "social_card"])
    if "product_hunt" in channels:
        asset_needs.extend(["product_hunt_thumbnail", "demo_gif"])
    if any(c in channels for c in ["twitter_x", "linkedin"]):
        asset_needs.extend(["twitter_thread_visuals", "testimonial_cards"])
    if "email_list" in channels:
        asset_needs.append("email_header")
    if "press" in channels:
        asset_needs.append("press_kit")
    if "demo_gif" not in asset_needs:
        asset_needs.append("demo_gif")

    asset_needs = list(dict.fromkeys(asset_needs))  # deduplicate preserving order

    narrative_arc = {
        "hook": data.get("hook", f"The problem with {data.get('problem_statement', 'current solutions')} is that they waste your time."),
        "tension": data.get("tension", "You've been working around this for too long. There's a better way."),
        "resolution": data["core_message"],
        "proof": data.get("proof_points", ["Customer quote", "Key metric", "Demo"]),
        "cta": data.get("cta", "Try it free — no credit card required"),
    }

    return {
        "error": None,
        "result": {
            "launch_name": data["launch_name"],
            "launch_type": data["launch_type"],
            "launch_date": data.get("launch_date"),
            "core_message": data["core_message"],
            "narrative_arc": narrative_arc,
            "visual_assets_required": [
                {"asset": a, "description": LAUNCH_ASSET_TYPES[a]} for a in asset_needs
            ],
            "total_assets": len(asset_needs),
            "channels": channels,
            "consistency_rules": [
                "Use the same hero image across website, PH, and OG/social cards",
                "Core message must appear verbatim on all high-attention surfaces",
                "Testimonials must be from real customers with permission to use name and company",
                "Demo GIF must match the live product — no aspirational features",
            ],
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_narrative_plan(data)
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
