#!/usr/bin/env python3
"""
connect-mcp.py — Test MCP server reachability for a given tool.

Purpose:
    Takes a tool name, looks up its known MCP server endpoint, and tests
    whether the server is reachable. Outputs connection status as JSON.

Dependencies: None (Python 3.10+ standard library only)

Usage:
    python3 connect-mcp.py <tool-name>
    python3 connect-mcp.py GitHub
    python3 connect-mcp.py Slack --timeout 10
"""

import json
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone

# Known MCP server endpoints for popular tools.
# In production, this would be loaded from a dynamic registry.
MCP_SERVERS: dict[str, dict] = {
    "github": {
        "name": "GitHub",
        "endpoint": "https://api.github.com",
        "health_path": "/",
        "auth_type": "token",
    },
    "slack": {
        "name": "Slack",
        "endpoint": "https://slack.com/api",
        "health_path": "/api.test",
        "auth_type": "oauth",
    },
    "linear": {
        "name": "Linear",
        "endpoint": "https://api.linear.app",
        "health_path": "/graphql",
        "auth_type": "token",
    },
    "notion": {
        "name": "Notion",
        "endpoint": "https://api.notion.com",
        "health_path": "/v1/users/me",
        "auth_type": "token",
    },
    "figma": {
        "name": "Figma",
        "endpoint": "https://api.figma.com",
        "health_path": "/v1/me",
        "auth_type": "token",
    },
    "gitlab": {
        "name": "GitLab",
        "endpoint": "https://gitlab.com/api/v4",
        "health_path": "/version",
        "auth_type": "token",
    },
    "jira": {
        "name": "Jira",
        "endpoint": "https://api.atlassian.com",
        "health_path": "/",
        "auth_type": "oauth",
    },
    "hubspot": {
        "name": "HubSpot",
        "endpoint": "https://api.hubapi.com",
        "health_path": "/",
        "auth_type": "token",
    },
    "stripe": {
        "name": "Stripe",
        "endpoint": "https://api.stripe.com",
        "health_path": "/v1/balance",
        "auth_type": "token",
    },
    "sentry": {
        "name": "Sentry",
        "endpoint": "https://sentry.io/api/0",
        "health_path": "/",
        "auth_type": "token",
    },
    "datadog": {
        "name": "Datadog",
        "endpoint": "https://api.datadoghq.com",
        "health_path": "/api/v1/validate",
        "auth_type": "token",
    },
    "grafana": {
        "name": "Grafana",
        "endpoint": "https://grafana.com/api",
        "health_path": "/",
        "auth_type": "token",
    },
}


def test_connection(tool_key: str, timeout: int = 5) -> dict:
    """Test if a tool's MCP server endpoint is reachable."""
    if tool_key not in MCP_SERVERS:
        return {
            "tool": tool_key,
            "status": "unknown",
            "reachable": False,
            "error": f"No known MCP server for '{tool_key}'. Available: {', '.join(sorted(MCP_SERVERS.keys()))}",
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

    server = MCP_SERVERS[tool_key]
    url = server["endpoint"] + server["health_path"]

    try:
        req = urllib.request.Request(url, method="GET")
        req.add_header("User-Agent", "skill-os-connect-mcp/1.0")
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            status_code = resp.status
            reachable = 200 <= status_code < 500  # 4xx means server is up but needs auth
            return {
                "tool": server["name"],
                "status": "reachable" if reachable else "error",
                "reachable": reachable,
                "endpoint": server["endpoint"],
                "http_status": status_code,
                "auth_type": server["auth_type"],
                "timestamp": datetime.now(timezone.utc).isoformat(),
            }
    except urllib.error.HTTPError as e:
        # 401/403 means the server is up, just needs auth
        reachable = e.code in (401, 403)
        return {
            "tool": server["name"],
            "status": "reachable (needs auth)" if reachable else "error",
            "reachable": reachable,
            "endpoint": server["endpoint"],
            "http_status": e.code,
            "auth_type": server["auth_type"],
            "error": None if reachable else str(e),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        return {
            "tool": server["name"],
            "status": "unreachable",
            "reachable": False,
            "endpoint": server["endpoint"],
            "error": str(e),
            "remediation": "Check network connectivity, firewall rules, or DNS resolution.",
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 connect-mcp.py <tool-name> [--timeout N]")
        print(f"Available tools: {', '.join(sorted(MCP_SERVERS.keys()))}")
        sys.exit(1)

    tool_name = sys.argv[1].lower().strip()

    timeout = 5
    if "--timeout" in sys.argv:
        idx = sys.argv.index("--timeout")
        if idx + 1 < len(sys.argv):
            timeout = int(sys.argv[idx + 1])

    result = test_connection(tool_name, timeout=timeout)
    print(json.dumps(result, indent=2))

    sys.exit(0 if result["reachable"] else 1)


if __name__ == "__main__":
    main()
