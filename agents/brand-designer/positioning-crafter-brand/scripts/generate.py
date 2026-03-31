#!/usr/bin/env python3
"""
generate.py — Generate brand visual direction from positioning strategy.

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

POSITIONING_ATTRIBUTES = {
    "precision": {"visual_cues": ["geometric shapes", "monospace type", "grid-based layouts", "muted tones"], "colours": "Blues, greys, blacks"},
    "speed": {"visual_cues": ["horizontal motion", "diagonal elements", "gradients", "bold weights"], "colours": "Electric blues, vibrant accent"},
    "trust": {"visual_cues": ["clean whitespace", "conservative type", "photography over illustration", "dark navy"], "colours": "Navy, white, muted tones"},
    "innovation": {"visual_cues": ["bold colour", "unconventional layouts", "abstract shapes", "experimental type"], "colours": "Gradient, neon accent, dark background"},
    "simplicity": {"visual_cues": ["generous whitespace", "limited colour", "light weights", "minimal iconography"], "colours": "White, one accent, grey"},
    "power": {"visual_cues": ["large scale type", "high contrast", "dense information", "strong grid"], "colours": "Black, strong accent colour"},
}

REQUIRED_FIELDS = ["brand_name", "positioning_statement", "key_attributes", "target_audience"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "key_attributes" in data:
        unknown = [a for a in data["key_attributes"] if a not in POSITIONING_ATTRIBUTES]
        if unknown:
            errors.append(f"Unknown attributes: {unknown}. Must be from: {list(POSITIONING_ATTRIBUTES.keys())}")
    return errors


def generate_visual_direction(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    attributes = data["key_attributes"][:3]  # max 3 to keep coherent
    visual_cues = []
    colour_families = []

    for attr in attributes:
        config = POSITIONING_ATTRIBUTES[attr]
        visual_cues.extend(config["visual_cues"])
        colour_families.append(config["colours"])

    # Deduplicate
    visual_cues = list(dict.fromkeys(visual_cues))

    direction = {
        "brand_name": data["brand_name"],
        "positioning_statement": data["positioning_statement"],
        "target_audience": data["target_audience"],
        "key_attributes": attributes,
        "visual_direction": {
            "primary_cues": visual_cues[:5],
            "colour_families": colour_families,
            "photography_style": data.get("photography_style", "Product screenshots with clean backgrounds"),
            "illustration_style": data.get("illustration_style", "Minimal line illustration if needed; default to photography"),
            "iconography": data.get("iconography", "Outlined icons; consistent 1.5px stroke weight"),
            "spacing_philosophy": "Generous whitespace to convey quality and reduce cognitive load",
        },
        "design_do": data.get("design_do", [
            "Let product screenshots be the hero",
            "Use typography hierarchy to guide the eye",
            "Maintain generous whitespace between elements",
        ]),
        "design_dont": data.get("design_dont", [
            "Use decorative elements that add no meaning",
            "Crowd the layout with too many focal points",
            "Use stock photography of people — use product visuals instead",
        ]),
        "reference_brands": data.get("reference_brands", []),
    }

    return {"error": None, "result": direction}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_visual_direction(data)
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
