#!/usr/bin/env python3
"""
generate.py — Generate a TAM/SAM/SOM market sizing model with bottom-up data estimates.

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

REQUIRED_FIELDS = ["market_name", "tam_inputs", "sam_inputs", "som_inputs"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    for section in ["tam_inputs", "sam_inputs", "som_inputs"]:
        if section in data:
            inputs = data[section]
            if "units" not in inputs or "arpu_usd" not in inputs:
                errors.append(f"{section} requires 'units' and 'arpu_usd'")
    return errors


def generate_market_size(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    tam = data["tam_inputs"]
    sam = data["sam_inputs"]
    som = data["som_inputs"]

    tam_usd = tam["units"] * tam["arpu_usd"]
    sam_usd = sam["units"] * sam["arpu_usd"]
    som_usd = som["units"] * som["arpu_usd"]

    sam_pct_of_tam = round(sam_usd / max(tam_usd, 1) * 100, 1)
    som_pct_of_sam = round(som_usd / max(sam_usd, 1) * 100, 1)

    def format_usd(value: float) -> str:
        if value >= 1_000_000_000:
            return f"${value/1_000_000_000:.1f}B"
        elif value >= 1_000_000:
            return f"${value/1_000_000:.1f}M"
        else:
            return f"${value:,.0f}"

    return {
        "error": None,
        "result": {
            "market_name": data["market_name"],
            "sizing_date": data.get("sizing_date", "2026-03-31"),
            "methodology": "Bottom-up: units × ARPU",
            "tam": {
                "description": tam.get("description", "Total Addressable Market"),
                "units": tam["units"],
                "arpu_usd": tam["arpu_usd"],
                "total_usd": tam_usd,
                "formatted": format_usd(tam_usd),
                "sources": tam.get("sources", []),
            },
            "sam": {
                "description": sam.get("description", "Serviceable Addressable Market — geographies and segments we can serve today"),
                "units": sam["units"],
                "arpu_usd": sam["arpu_usd"],
                "total_usd": sam_usd,
                "formatted": format_usd(sam_usd),
                "pct_of_tam": sam_pct_of_tam,
                "sources": sam.get("sources", []),
            },
            "som": {
                "description": som.get("description", "Serviceable Obtainable Market — realistic 3-year capture"),
                "units": som["units"],
                "arpu_usd": som["arpu_usd"],
                "total_usd": som_usd,
                "formatted": format_usd(som_usd),
                "pct_of_sam": som_pct_of_sam,
                "sources": som.get("sources", []),
            },
            "key_assumptions": data.get("assumptions", []),
            "confidence": data.get("confidence", "medium"),
            "investment_threshold": "SOM > $10M typically justifies dedicated team investment; > $50M justifies Series A raise",
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_market_size(data)
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
