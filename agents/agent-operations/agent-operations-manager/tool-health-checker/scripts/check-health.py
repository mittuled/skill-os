#!/usr/bin/env python3
"""
check-health.py — Probes tools registered in allowed-tools.yaml and reports health status.

Purpose: Reads allowed-tools.yaml, attempts a lightweight HTTP probe for each
         tool's health endpoint, and outputs a JSON health report with status,
         latency, and remediation suggestions.

Dependencies: Python 3.10+ standard library only (no external packages).

Usage:
    python3 check-health.py                              # uses ./allowed-tools.yaml
    python3 check-health.py path/to/allowed-tools.yaml   # custom path
    python3 check-health.py --json                       # JSON output to stdout
    python3 check-health.py -o report.json               # write JSON to file
"""

from __future__ import annotations

import json
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore[assignment]


# Default health endpoints for well-known tools (used when none specified).
KNOWN_HEALTH_ENDPOINTS: dict[str, str] = {
    "github": "https://api.github.com",
    "slack": "https://slack.com/api/api.test",
    "datadog": "https://api.datadoghq.com/api/v1/validate",
    "sentry": "https://sentry.io/api/0/",
    "linear": "https://api.linear.app/graphql",
    "salesforce": "https://login.salesforce.com/.well-known/openid-configuration",
}

HEALTHY_THRESHOLD_MS = 2000
DEGRADED_THRESHOLD_MS = 5000


def load_policy(path: Path) -> dict | None:
    """Load and parse allowed-tools.yaml."""
    if not path.exists():
        print(f"Error: Policy file not found: {path}", file=sys.stderr)
        return None

    text = path.read_text(encoding="utf-8")
    if yaml is not None:
        try:
            return yaml.safe_load(text)
        except yaml.YAMLError as exc:
            print(f"Error: YAML parse error: {exc}", file=sys.stderr)
            return None
    else:
        print("Warning: PyYAML not available. Install with: pip install pyyaml", file=sys.stderr)
        return None


def collect_tools(policy: dict) -> list[dict]:
    """Collect all unique tools from every policy level."""
    seen: set[str] = set()
    tools: list[dict] = []

    def add_entries(entries: list, level: str) -> None:
        for entry in entries:
            if not isinstance(entry, dict):
                continue
            name = entry.get("name", "")
            if name and name not in seen:
                seen.add(name)
                tools.append({**entry, "_level": level})

    # Company-wide
    cw = policy.get("company-wide")
    if isinstance(cw, list):
        add_entries(cw, "company-wide")

    # Department, agent, skill levels
    for level in ("department", "agent", "skill"):
        level_data = policy.get(level)
        if isinstance(level_data, dict):
            for _key, entries in level_data.items():
                if isinstance(entries, list):
                    add_entries(entries, level)

    return tools


def probe_tool(tool: dict) -> dict:
    """Probe a single tool and return health result."""
    name = tool.get("name", "unknown")
    health_url = tool.get("health_endpoint") or KNOWN_HEALTH_ENDPOINTS.get(name)
    now = datetime.now(timezone.utc).isoformat()

    if not health_url:
        return {
            "tool": name,
            "status": "unknown",
            "latency_ms": None,
            "last_checked": now,
            "message": "No health endpoint configured or known.",
            "remediation": f"Add 'health_endpoint' to the {name} entry in allowed-tools.yaml.",
        }

    start = time.monotonic()
    try:
        req = urllib.request.Request(health_url, method="HEAD")
        req.add_header("User-Agent", "skill-os-health-checker/1.0")
        with urllib.request.urlopen(req, timeout=10) as resp:
            latency_ms = int((time.monotonic() - start) * 1000)
            status_code = resp.status

        if latency_ms <= HEALTHY_THRESHOLD_MS and 200 <= status_code < 400:
            status = "healthy"
            message = f"Responded with HTTP {status_code} in {latency_ms}ms."
            remediation = None
        elif latency_ms <= DEGRADED_THRESHOLD_MS:
            status = "degraded"
            message = f"Responded with HTTP {status_code} in {latency_ms}ms (high latency)."
            remediation = "Investigate network latency or upstream performance."
        else:
            status = "degraded"
            message = f"Responded with HTTP {status_code} in {latency_ms}ms (very high latency)."
            remediation = "Check for rate limiting, network issues, or service degradation."

    except urllib.error.HTTPError as exc:
        latency_ms = int((time.monotonic() - start) * 1000)
        if exc.code in (401, 403):
            status = "unreachable"
            message = f"Authentication failed: HTTP {exc.code}."
            remediation = f"Verify credentials for {name}. Check API key or token expiry."
        else:
            status = "degraded"
            message = f"HTTP error {exc.code}: {exc.reason}."
            remediation = f"Check {name} API status page or configuration."

    except urllib.error.URLError as exc:
        latency_ms = int((time.monotonic() - start) * 1000)
        status = "unreachable"
        message = f"Connection failed: {exc.reason}."
        remediation = f"Verify {name} health endpoint URL and network connectivity."

    except TimeoutError:
        latency_ms = 10000
        status = "unreachable"
        message = "Request timed out after 10 seconds."
        remediation = f"Check if {name} service is running and reachable."

    return {
        "tool": name,
        "status": status,
        "latency_ms": latency_ms,
        "last_checked": now,
        "message": message,
        "remediation": remediation,
    }


def run_checks(policy_path: Path) -> dict:
    """Run health checks on all tools and return the report."""
    policy = load_policy(policy_path)
    if policy is None:
        return {"error": "Failed to load policy file.", "results": []}

    tools = collect_tools(policy)
    if not tools:
        return {"error": None, "results": [], "summary": "No tools found in policy file."}

    results = []
    for tool in tools:
        result = probe_tool(tool)
        results.append(result)

    # Summary
    total = len(results)
    healthy = sum(1 for r in results if r["status"] == "healthy")
    degraded = sum(1 for r in results if r["status"] == "degraded")
    unreachable = sum(1 for r in results if r["status"] == "unreachable")
    unknown = sum(1 for r in results if r["status"] == "unknown")

    return {
        "error": None,
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "summary": {
            "total": total,
            "healthy": healthy,
            "degraded": degraded,
            "unreachable": unreachable,
            "unknown": unknown,
        },
        "critical": [r["tool"] for r in results if r["status"] == "unreachable"],
        "results": results,
    }


def main() -> None:
    args = sys.argv[1:]

    # Find policy path
    policy_path = Path("allowed-tools.yaml")
    for arg in args:
        if not arg.startswith("-"):
            policy_path = Path(arg)
            break

    report = run_checks(policy_path)

    output = json.dumps(report, indent=2)

    if "-o" in args:
        out_index = args.index("-o") + 1
        if out_index < len(args):
            Path(args[out_index]).write_text(output + "\n", encoding="utf-8")
            print(f"Report written to {args[out_index]}")
        else:
            print("Error: -o requires a filename", file=sys.stderr)
            sys.exit(1)
    else:
        print(output)


if __name__ == "__main__":
    main()
