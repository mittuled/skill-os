#!/usr/bin/env python3
"""
discover-tools.py — Interactive tool discovery for company-tooling-onboarder.

Purpose:
    Presents tool categories and known tools per category, accepts user
    selections, and outputs a JSON manifest of selected tools with MCP
    availability status.

Dependencies: None (Python 3.10+ standard library only)

Usage:
    python3 discover-tools.py
    python3 discover-tools.py --non-interactive  # select all tools, useful for CI
"""

import json
import sys
from dataclasses import dataclass, asdict

TOOL_REGISTRY: dict[str, list[dict]] = {
    "communication": [
        {"name": "Slack", "mcp_available": True, "mcp_type": "official"},
        {"name": "Microsoft Teams", "mcp_available": True, "mcp_type": "community"},
        {"name": "Discord", "mcp_available": True, "mcp_type": "community"},
        {"name": "Zoom", "mcp_available": False, "mcp_type": None},
        {"name": "Google Chat", "mcp_available": False, "mcp_type": None},
    ],
    "source_control": [
        {"name": "GitHub", "mcp_available": True, "mcp_type": "official"},
        {"name": "GitLab", "mcp_available": True, "mcp_type": "community"},
        {"name": "Bitbucket", "mcp_available": True, "mcp_type": "community"},
        {"name": "Azure DevOps", "mcp_available": False, "mcp_type": None},
    ],
    "project_management": [
        {"name": "Linear", "mcp_available": True, "mcp_type": "official"},
        {"name": "Jira", "mcp_available": True, "mcp_type": "community"},
        {"name": "Asana", "mcp_available": True, "mcp_type": "community"},
        {"name": "Shortcut", "mcp_available": False, "mcp_type": None},
    ],
    "observability": [
        {"name": "Datadog", "mcp_available": True, "mcp_type": "community"},
        {"name": "Grafana", "mcp_available": True, "mcp_type": "community"},
        {"name": "PagerDuty", "mcp_available": False, "mcp_type": None},
        {"name": "Sentry", "mcp_available": True, "mcp_type": "community"},
    ],
    "crm": [
        {"name": "Salesforce", "mcp_available": True, "mcp_type": "community"},
        {"name": "HubSpot", "mcp_available": True, "mcp_type": "community"},
        {"name": "Pipedrive", "mcp_available": False, "mcp_type": None},
    ],
    "documentation": [
        {"name": "Notion", "mcp_available": True, "mcp_type": "community"},
        {"name": "Confluence", "mcp_available": True, "mcp_type": "community"},
        {"name": "Google Docs", "mcp_available": True, "mcp_type": "community"},
    ],
    "finance": [
        {"name": "Stripe", "mcp_available": True, "mcp_type": "community"},
        {"name": "QuickBooks", "mcp_available": False, "mcp_type": None},
        {"name": "Brex", "mcp_available": False, "mcp_type": None},
    ],
    "legal": [
        {"name": "DocuSign", "mcp_available": False, "mcp_type": None},
        {"name": "Ironclad", "mcp_available": False, "mcp_type": None},
    ],
    "design": [
        {"name": "Figma", "mcp_available": True, "mcp_type": "official"},
        {"name": "Canva", "mcp_available": False, "mcp_type": None},
        {"name": "Miro", "mcp_available": True, "mcp_type": "community"},
    ],
}


def display_category(category: str, tools: list[dict]) -> None:
    """Print a category and its tools with indices."""
    label = category.replace("_", " ").title()
    print(f"\n{'=' * 40}")
    print(f"  {label}")
    print(f"{'=' * 40}")
    for i, tool in enumerate(tools, 1):
        mcp_status = "MCP" if tool["mcp_available"] else "API-only"
        print(f"  {i}. {tool['name']} [{mcp_status}]")


def prompt_selections(category: str, tools: list[dict]) -> list[dict]:
    """Prompt the user to select tools from a category. Returns selected tools."""
    display_category(category, tools)
    print(f"\n  Enter tool numbers (comma-separated), 'all', or 'none':")
    raw = input(f"  [{category}] > ").strip().lower()

    if raw in ("none", "n", ""):
        return []
    if raw in ("all", "a"):
        return tools

    selected = []
    for part in raw.split(","):
        part = part.strip()
        if part.isdigit():
            idx = int(part) - 1
            if 0 <= idx < len(tools):
                selected.append(tools[idx])
            else:
                print(f"  Warning: index {part} out of range, skipping")
    return selected


def run_interactive() -> dict:
    """Run interactive tool discovery."""
    print("=" * 50)
    print("  Company Tooling Discovery")
    print("  Select the tools your organization uses.")
    print("=" * 50)

    manifest: dict[str, list[dict]] = {}
    for category, tools in TOOL_REGISTRY.items():
        selected = prompt_selections(category, tools)
        if selected:
            manifest[category] = selected

    return manifest


def run_non_interactive() -> dict:
    """Select all tools (for CI/automation)."""
    return {cat: list(tools) for cat, tools in TOOL_REGISTRY.items()}


def main() -> None:
    non_interactive = "--non-interactive" in sys.argv

    if non_interactive:
        manifest = run_non_interactive()
    else:
        manifest = run_interactive()

    # Summary
    total = sum(len(tools) for tools in manifest.values())
    mcp_count = sum(
        1 for tools in manifest.values() for t in tools if t["mcp_available"]
    )

    output = {
        "version": "1.0.0",
        "total_tools": total,
        "mcp_available": mcp_count,
        "api_only": total - mcp_count,
        "categories": manifest,
    }

    print("\n" + json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
