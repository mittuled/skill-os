#!/usr/bin/env python3
"""
scaffold-mcp.py — Generates a FastMCP-compatible Python server from parsed API data.

Purpose: Takes the structured JSON output from parse-openapi.py and generates
         a complete MCP server skeleton with tool definitions, authentication,
         and error handling.

Dependencies: Python 3.10+ standard library only (no external packages).

Usage:
    python3 scaffold-mcp.py parsed.json                # output to stdout
    python3 scaffold-mcp.py parsed.json -o server.py   # output to file
"""

from __future__ import annotations

import json
import sys
import textwrap
from pathlib import Path


def _tool_name(endpoint: dict) -> str:
    """Generate an MCP tool name from an endpoint."""
    if endpoint.get("operation_id"):
        # Convert camelCase to snake_case
        name = endpoint["operation_id"]
        result = []
        for i, ch in enumerate(name):
            if ch.isupper() and i > 0:
                result.append("_")
            result.append(ch.lower())
        return "".join(result)
    # Fallback: method + path segments
    path = endpoint["path"].strip("/").replace("/", "_").replace("{", "").replace("}", "")
    return f"{endpoint['method'].lower()}_{path}"


def _python_type(type_str: str) -> str:
    """Map JSON/OpenAPI types to Python type hints."""
    mapping = {
        "string": "str",
        "integer": "int",
        "number": "float",
        "boolean": "bool",
        "array": "list",
        "object": "dict",
    }
    return mapping.get(type_str, "str")


def _generate_tool_params(endpoint: dict) -> list[tuple[str, str, bool, str]]:
    """Return list of (name, python_type, required, description) for tool parameters."""
    params = []
    for p in endpoint.get("parameters", []):
        if p.get("in") == "header":
            continue  # Auth headers handled separately
        params.append((
            p["name"],
            _python_type(p.get("type", "string")),
            p.get("required", False),
            p.get("description", ""),
        ))

    # Add request body fields as parameters
    body = endpoint.get("request_body")
    if body and isinstance(body, dict):
        schema = body.get("schema", {})
        for prop_name, prop_type in schema.get("properties", {}).items():
            required_fields = schema.get("required", [])
            params.append((
                prop_name,
                _python_type(prop_type),
                prop_name in required_fields,
                "",
            ))
    return params


def _generate_tool_function(endpoint: dict, base_url: str) -> str:
    """Generate a single tool function definition."""
    name = _tool_name(endpoint)
    params = _generate_tool_params(endpoint)
    summary = endpoint.get("summary") or endpoint.get("description") or f"{endpoint['method']} {endpoint['path']}"

    # Build function signature
    sig_parts = []
    for pname, ptype, required, _desc in params:
        if required:
            sig_parts.insert(0, f"{pname}: {ptype}")
        else:
            default = '""' if ptype == "str" else "None"
            sig_parts.append(f"{pname}: {ptype} | None = {default}")

    sig = ", ".join(sig_parts)

    # Build docstring params
    doc_params = ""
    if params:
        doc_lines = []
        for pname, ptype, required, desc in params:
            req_str = " (required)" if required else ""
            doc_lines.append(f"        {pname}: {desc or ptype}{req_str}")
        doc_params = "\n\n    Args:\n" + "\n".join(doc_lines)

    # Build URL construction
    path = endpoint["path"]
    url_expr = f'f"{base_url}{path}"' if "{" in path else f'"{base_url}{path}"'

    # Build request body
    method = endpoint["method"]
    body_params = [p[0] for p in params if any(
        bp.get("in") == "body" or bp.get("in") == "path" is False
        for bp in endpoint.get("parameters", [])
        if bp.get("name") == p[0]
    )]

    return textwrap.dedent(f'''\

        @mcp.tool()
        async def {name}({sig}) -> str:
            """
            {summary}{doc_params}
            """
            url = {url_expr}
            headers = {{"Authorization": f"Bearer {{API_TOKEN}}"}}

            async with httpx_or_urllib(
                method="{method}",
                url=url,
                headers=headers,
            ) as response:
                return json.dumps(response)
    ''')


def _generate_auth_section(auth_schemes: list[dict]) -> str:
    """Generate authentication configuration code."""
    if not auth_schemes:
        return textwrap.dedent('''\
            # Authentication — configure via environment variables.
            API_TOKEN = os.environ.get("API_TOKEN", "")
        ''')

    lines = ["# Authentication — configure via environment variables."]
    for scheme in auth_schemes:
        env_var = f"{scheme['name'].upper().replace('-', '_')}_TOKEN"
        lines.append(f'{env_var} = os.environ.get("{env_var}", "")')

    # Use the first scheme's var as the default API_TOKEN
    first_var = f"{auth_schemes[0]['name'].upper().replace('-', '_')}_TOKEN"
    lines.append(f"API_TOKEN = {first_var}")
    return "\n".join(lines)


def generate_server(parsed: dict) -> str:
    """Generate the complete MCP server Python file."""
    api_name = parsed.get("api_name", "Unknown API")
    base_url = parsed.get("base_url", "https://api.example.com")
    auth_schemes = parsed.get("auth", [])
    endpoints = parsed.get("endpoints", [])

    auth_code = _generate_auth_section(auth_schemes)

    tool_functions = ""
    for ep in endpoints:
        tool_functions += _generate_tool_function(ep, base_url)

    return textwrap.dedent(f'''\
        #!/usr/bin/env python3
        """
        MCP Server: {api_name}

        Auto-generated by scaffold-mcp.py from the skill-os mcp-server-builder skill.
        Provides MCP tool definitions for the {api_name} API.

        Usage:
            python3 server.py          # stdio transport (default)
            python3 server.py --sse    # SSE transport
        """

        from __future__ import annotations

        import json
        import os
        import sys
        import urllib.request
        import urllib.error
        from contextlib import asynccontextmanager

        try:
            from mcp.server.fastmcp import FastMCP
        except ImportError:
            print("Error: FastMCP not installed. Run: pip install mcp", file=sys.stderr)
            sys.exit(1)


        {auth_code}

        mcp = FastMCP("{api_name}")


        # --- HTTP helper (stdlib only, no external deps required) ---

        @asynccontextmanager
        async def httpx_or_urllib(method: str, url: str, headers: dict | None = None, body: dict | None = None):
            """Lightweight HTTP request using urllib. Yields parsed response dict."""
            data = json.dumps(body).encode() if body else None
            req = urllib.request.Request(url, data=data, headers=headers or {{}}, method=method)
            try:
                with urllib.request.urlopen(req, timeout=30) as resp:
                    content = resp.read().decode()
                    try:
                        yield json.loads(content)
                    except json.JSONDecodeError:
                        yield {{"status": resp.status, "body": content}}
            except urllib.error.HTTPError as exc:
                yield {{"error": True, "status": exc.code, "reason": exc.reason}}
            except urllib.error.URLError as exc:
                yield {{"error": True, "status": 0, "reason": str(exc.reason)}}

        {tool_functions}

        # --- Entry point ---

        def main() -> None:
            transport = "sse" if "--sse" in sys.argv else "stdio"
            mcp.run(transport=transport)


        if __name__ == "__main__":
            main()
    ''')


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: scaffold-mcp.py <parsed.json> [-o server.py]", file=sys.stderr)
        sys.exit(1)

    parsed_path = Path(sys.argv[1])
    if not parsed_path.exists():
        print(f"Error: File not found: {parsed_path}", file=sys.stderr)
        sys.exit(1)

    parsed = json.loads(parsed_path.read_text(encoding="utf-8"))
    server_code = generate_server(parsed)

    if "-o" in sys.argv:
        out_index = sys.argv.index("-o") + 1
        if out_index < len(sys.argv):
            Path(sys.argv[out_index]).write_text(server_code, encoding="utf-8")
            print(f"Written to {sys.argv[out_index]}")
        else:
            print("Error: -o requires a filename", file=sys.stderr)
            sys.exit(1)
    else:
        print(server_code)


if __name__ == "__main__":
    main()
