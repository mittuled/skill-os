#!/usr/bin/env python3
"""
generate.py — Generate a brand foundation document including values, personality, tone, and visual principles.

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

PERSONALITY_ARCHETYPES = {
    "creator": {"traits": ["innovative", "expressive", "imaginative"], "tone": "Inspiring, visionary, creative"},
    "hero": {"traits": ["confident", "courageous", "determined"], "tone": "Bold, direct, empowering"},
    "sage": {"traits": ["knowledgeable", "trustworthy", "analytical"], "tone": "Authoritative, clear, precise"},
    "explorer": {"traits": ["adventurous", "curious", "independent"], "tone": "Energetic, open, pioneering"},
    "caregiver": {"traits": ["nurturing", "supportive", "reliable"], "tone": "Warm, helpful, reassuring"},
    "magician": {"traits": ["transformative", "visionary", "charismatic"], "tone": "Inspiring, transformative, sophisticated"},
}

REQUIRED_FIELDS = ["company_name", "mission", "target_audience", "personality_archetype"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "personality_archetype" in data and data["personality_archetype"] not in PERSONALITY_ARCHETYPES:
        errors.append(f"personality_archetype must be one of {list(PERSONALITY_ARCHETYPES.keys())}")
    return errors


def generate_brand_foundation(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    archetype = PERSONALITY_ARCHETYPES[data["personality_archetype"]]

    foundation = {
        "company_name": data["company_name"],
        "mission": data["mission"],
        "vision": data.get("vision", f"A world where {data['target_audience']} can {data['mission'].lower()}"),
        "target_audience": data["target_audience"],
        "brand_values": data.get("brand_values", ["Innovation", "Transparency", "Customer obsession"]),
        "personality": {
            "archetype": data["personality_archetype"],
            "traits": archetype["traits"] + data.get("additional_traits", []),
            "anti_traits": data.get("anti_traits", ["Generic", "Corporate", "Passive"]),
        },
        "tone_of_voice": {
            "primary_tone": archetype["tone"],
            "do": data.get("tone_do", [
                "Use active voice",
                "Be specific — avoid vague claims",
                "Address the reader directly (you, your)",
                "Lead with the customer's problem",
            ]),
            "dont": data.get("tone_dont", [
                "Use jargon without explanation",
                "Make unsubstantiated superlatives (world's best, #1)",
                "Use passive voice",
                "Write longer than needed",
            ]),
        },
        "visual_direction": {
            "personality_cues": f"{archetype['traits'][0].title()}, {archetype['traits'][1].title()}",
            "emotional_response": data.get("desired_emotional_response", "Confidence and clarity"),
            "design_principles": data.get("design_principles", ["Clarity over complexity", "Functional beauty", "Consistent but not rigid"]),
        },
        "brand_promise": data.get("brand_promise", f"{data['company_name']} helps {data['target_audience']} {data['mission'].lower()}"),
    }

    return {"error": None, "result": foundation}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_brand_foundation(data)
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
