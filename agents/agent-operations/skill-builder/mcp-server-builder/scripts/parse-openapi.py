#!/usr/bin/env python3
"""
parse-openapi.py — Parses an OpenAPI/Swagger spec and extracts endpoint metadata.

Purpose: Reads an OpenAPI 3.x or Swagger 2.0 JSON spec file and outputs a
         structured JSON summary of all endpoints, methods, parameters, and
         response schemas for use by scaffold-mcp.py.

Dependencies: Python 3.10+ standard library only (no external packages).

Usage:
    python3 parse-openapi.py spec.json                # output to stdout
    python3 parse-openapi.py spec.json -o parsed.json # output to file
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


def resolve_ref(spec: dict, ref: str) -> dict:
    """Resolve a $ref pointer within the spec. Supports #/components/schemas/... paths."""
    parts = ref.lstrip("#/").split("/")
    node = spec
    for part in parts:
        node = node.get(part, {})
    return node if isinstance(node, dict) else {}


def extract_parameters(spec: dict, params: list[dict]) -> list[dict]:
    """Extract parameter metadata from a list of OpenAPI parameter objects."""
    result = []
    for param in params:
        if "$ref" in param:
            param = resolve_ref(spec, param["$ref"])
        entry = {
            "name": param.get("name", "unknown"),
            "in": param.get("in", "query"),
            "required": param.get("required", False),
            "type": _extract_type(spec, param.get("schema", param)),
        }
        if "description" in param:
            entry["description"] = param["description"]
        result.append(entry)
    return result


def extract_request_body(spec: dict, body: dict) -> dict | None:
    """Extract request body schema from OpenAPI 3.x requestBody object."""
    if not body:
        return None
    if "$ref" in body:
        body = resolve_ref(spec, body["$ref"])
    content = body.get("content", {})
    json_content = content.get("application/json", {})
    schema = json_content.get("schema", {})
    if "$ref" in schema:
        schema = resolve_ref(spec, schema["$ref"])
    return {
        "required": body.get("required", False),
        "schema": _simplify_schema(spec, schema),
    }


def _extract_type(spec: dict, schema: dict) -> str:
    """Extract a human-readable type string from a schema object."""
    if "$ref" in schema:
        ref_name = schema["$ref"].split("/")[-1]
        return ref_name
    return schema.get("type", "object")


def _simplify_schema(spec: dict, schema: dict) -> dict:
    """Simplify a schema for output, resolving top-level refs."""
    if "$ref" in schema:
        schema = resolve_ref(spec, schema["$ref"])
    result: dict = {"type": schema.get("type", "object")}
    if "properties" in schema:
        result["properties"] = {
            k: _extract_type(spec, v) for k, v in schema["properties"].items()
        }
    if "required" in schema:
        result["required"] = schema["required"]
    if schema.get("type") == "array" and "items" in schema:
        result["items"] = _extract_type(spec, schema["items"])
    return result


def extract_response(spec: dict, responses: dict) -> dict:
    """Extract the success response schema (200 or 201)."""
    for code in ("200", "201", 200, 201):
        if str(code) in responses:
            resp = responses[str(code)]
            if "$ref" in resp:
                resp = resolve_ref(spec, resp["$ref"])
            content = resp.get("content", {})
            json_content = content.get("application/json", {})
            schema = json_content.get("schema", {})
            if "$ref" in schema:
                schema = resolve_ref(spec, schema["$ref"])
            return {
                "status": str(code),
                "schema": _simplify_schema(spec, schema) if schema else None,
            }
    return {"status": "unknown", "schema": None}


def extract_auth(spec: dict) -> list[dict]:
    """Extract authentication schemes from the spec."""
    schemes = []
    # OpenAPI 3.x
    components = spec.get("components", {}).get("securitySchemes", {})
    # Swagger 2.x
    if not components:
        components = spec.get("securityDefinitions", {})
    for name, scheme in components.items():
        schemes.append({
            "name": name,
            "type": scheme.get("type", "unknown"),
            "scheme": scheme.get("scheme"),
            "in": scheme.get("in"),
        })
    return schemes


def parse_spec(spec: dict) -> dict:
    """Parse an OpenAPI/Swagger spec into structured endpoint data."""
    # Determine version
    version = spec.get("openapi", spec.get("swagger", "unknown"))
    info = spec.get("info", {})

    endpoints = []
    paths = spec.get("paths", {})

    for path, path_item in paths.items():
        if not isinstance(path_item, dict):
            continue
        # Path-level parameters
        path_params = path_item.get("parameters", [])

        for method in ("get", "post", "put", "patch", "delete", "head", "options"):
            if method not in path_item:
                continue
            operation = path_item[method]
            # Merge path-level and operation-level parameters
            op_params = operation.get("parameters", [])
            all_params = path_params + op_params

            endpoint = {
                "path": path,
                "method": method.upper(),
                "operation_id": operation.get("operationId"),
                "summary": operation.get("summary", ""),
                "description": operation.get("description", ""),
                "parameters": extract_parameters(spec, all_params),
                "response": extract_response(spec, operation.get("responses", {})),
            }

            # OpenAPI 3.x request body
            if "requestBody" in operation:
                endpoint["request_body"] = extract_request_body(spec, operation["requestBody"])

            # Swagger 2.x body parameter
            body_params = [p for p in all_params if isinstance(p, dict) and p.get("in") == "body"]
            if body_params and "request_body" not in endpoint:
                schema = body_params[0].get("schema", {})
                if "$ref" in schema:
                    schema = resolve_ref(spec, schema["$ref"])
                endpoint["request_body"] = {
                    "required": body_params[0].get("required", False),
                    "schema": _simplify_schema(spec, schema),
                }

            endpoints.append(endpoint)

    return {
        "api_name": info.get("title", "Unknown API"),
        "api_version": info.get("version", "0.0.0"),
        "spec_version": version,
        "base_url": _extract_base_url(spec),
        "auth": extract_auth(spec),
        "endpoints": endpoints,
    }


def _extract_base_url(spec: dict) -> str:
    """Extract the base URL from the spec."""
    # OpenAPI 3.x
    servers = spec.get("servers", [])
    if servers and isinstance(servers[0], dict):
        return servers[0].get("url", "")
    # Swagger 2.x
    host = spec.get("host", "")
    base_path = spec.get("basePath", "")
    scheme = (spec.get("schemes") or ["https"])[0]
    if host:
        return f"{scheme}://{host}{base_path}"
    return ""


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: parse-openapi.py <spec.json> [-o output.json]", file=sys.stderr)
        sys.exit(1)

    spec_path = Path(sys.argv[1])
    if not spec_path.exists():
        print(f"Error: File not found: {spec_path}", file=sys.stderr)
        sys.exit(1)

    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    result = parse_spec(spec)

    output = json.dumps(result, indent=2)

    if "-o" in sys.argv:
        out_index = sys.argv.index("-o") + 1
        if out_index < len(sys.argv):
            Path(sys.argv[out_index]).write_text(output + "\n", encoding="utf-8")
            print(f"Written to {sys.argv[out_index]}")
        else:
            print("Error: -o requires a filename", file=sys.stderr)
            sys.exit(1)
    else:
        print(output)


if __name__ == "__main__":
    main()
