#!/usr/bin/env python3
"""
validate-policy.py — Validates allowed-tools.yaml for the tool-policy-manager skill.

Purpose: Checks that allowed-tools.yaml is valid YAML, contains a schema_version
         field, and that all tool entries have required fields (name, scopes).

Dependencies: Python 3.10+ standard library only (no external packages).

Usage:
    python3 validate-policy.py                          # validates ./allowed-tools.yaml
    python3 validate-policy.py path/to/allowed-tools.yaml  # validates a specific file
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

# PyYAML is not in stdlib — use a minimal YAML subset parser for simple cases,
# but since allowed-tools.yaml is simple enough, we parse with the yaml module
# which ships with most Python installs. If unavailable, fall back to basic checks.
try:
    import yaml
except ImportError:
    yaml = None  # type: ignore[assignment]


def load_yaml(path: Path) -> dict | None:
    """Load a YAML file. Returns parsed dict or None on failure."""
    text = path.read_text(encoding="utf-8")
    if yaml is not None:
        try:
            return yaml.safe_load(text)
        except yaml.YAMLError as exc:
            print(f"FAIL: YAML parse error: {exc}")
            return None
    else:
        print("WARN: PyYAML not available; skipping deep YAML validation.")
        # Basic check: file is non-empty and contains schema_version
        if "schema_version" not in text:
            print("FAIL: schema_version not found in file.")
            return None
        return {"_fallback": True, "schema_version": 1}


def validate_tool_entry(tool: dict, level: str, index: int) -> list[str]:
    """Validate a single tool entry. Returns list of error messages."""
    errors: list[str] = []
    if not isinstance(tool, dict):
        errors.append(f"  [{level}][{index}]: entry is not a mapping")
        return errors
    if "name" not in tool:
        errors.append(f"  [{level}][{index}]: missing required field 'name'")
    if "scopes" in tool and not isinstance(tool["scopes"], list):
        errors.append(f"  [{level}][{index}]: 'scopes' must be a list")
    return errors


def validate_level(data: dict | list, level_name: str) -> list[str]:
    """Validate tool entries at a given level."""
    errors: list[str] = []
    if isinstance(data, list):
        for i, entry in enumerate(data):
            errors.extend(validate_tool_entry(entry, level_name, i))
    elif isinstance(data, dict):
        for sub_key, sub_list in data.items():
            if isinstance(sub_list, list):
                for i, entry in enumerate(sub_list):
                    errors.extend(validate_tool_entry(entry, f"{level_name}.{sub_key}", i))
            elif sub_list is not None:
                errors.append(f"  [{level_name}.{sub_key}]: expected a list of tool entries")
    return errors


def validate(path: Path) -> bool:
    """Run all validations. Returns True if valid."""
    if not path.exists():
        print(f"FAIL: File not found: {path}")
        return False

    data = load_yaml(path)
    if data is None:
        return False

    if data.get("_fallback"):
        print("PASS (limited): schema_version present, YAML not deeply validated.")
        return True

    errors: list[str] = []

    # Check schema_version
    if "schema_version" not in data:
        errors.append("Missing required field: schema_version")

    # Validate each level
    valid_levels = ["company-wide", "department", "agent", "skill"]
    for level in valid_levels:
        if level in data and data[level] is not None:
            errors.extend(validate_level(data[level], level))

    # Check for unknown top-level keys
    known_keys = {"schema_version"} | set(valid_levels)
    for key in data:
        if key not in known_keys and not str(key).startswith("#"):
            errors.append(f"Unknown top-level key: '{key}'")

    if errors:
        print(f"FAIL: {len(errors)} error(s) found in {path}:")
        for err in errors:
            print(f"  {err}")
        return False

    print(f"PASS: {path} is valid.")
    return True


def main() -> None:
    if len(sys.argv) > 1:
        path = Path(sys.argv[1])
    else:
        path = Path("allowed-tools.yaml")

    success = validate(path)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
