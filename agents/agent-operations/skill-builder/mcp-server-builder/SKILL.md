---
name: mcp-server-builder
description: >
  This skill scaffolds a Model Context Protocol (MCP) server from API
  documentation. Use when asked to build an MCP server, create an MCP wrapper
  for an existing API, or generate MCP tool definitions from OpenAPI specs.
  Also consider when a tool lacks native MCP support and needs a bridge.
  Suggest when the user connects to an API manually instead of through MCP.
department: agent-operations
agent: skill-builder
version: 1.0.0
complexity: complex
triggers:
  - build an MCP server
  - create MCP wrapper
  - connect a tool without MCP
  - generate MCP from API
related-skills:
  - ../../../agent-operations/agent-configuration-manager/tool-policy-manager/SKILL.md
  - ../../../agent-operations/agent-operations-manager/tool-health-checker/SKILL.md
---

# mcp-server-builder

## Agent: Skill Builder

L3 Skill Builder (Nx) responsible for building and testing individual SKILL.md files. Multiple Skill Builders can work across different domains simultaneously.

Department ethos: [ideal-agent-operations.md](../../../../departments/agent-operations/ideal-agent-operations.md)

Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Scaffolds a fully functional MCP server from API documentation, transforming REST endpoints into MCP-compatible tool definitions with transport, error handling, and authentication.

## When to Use

- When an external API needs to be exposed as MCP tools for the agent fleet.
- When an OpenAPI/Swagger spec is available and needs to be converted to an MCP server.
- When a tool vendor does not provide native MCP support and a bridge server is required.
- When migrating from direct API calls to MCP-based tool access for better observability.
- When prototyping a new integration and a working MCP skeleton is needed quickly.

## Workflow

1. **Receive API documentation**: Accept an OpenAPI/Swagger spec (JSON or YAML) or structured API docs. Validate the input contains at least one endpoint with method, path, and parameters. Deliverable: validated API specification.

2. **Parse endpoints**: Run `scripts/parse-openapi.py` to extract all endpoints, HTTP methods, parameters (path, query, body), response schemas, and authentication requirements. Deliverable: structured JSON describing every endpoint.

3. **Map to MCP tools**: Transform each API endpoint into an MCP tool definition following the naming conventions in `references/mcp-protocol.md`. Apply these rules:
   - One tool per endpoint (unless CRUD operations should be grouped).
   - Tool names follow `resource_action` pattern (e.g., `issues_list`, `issue_create`).
   - Input schemas derived from request parameters; output schemas from response bodies.
   - Mark required vs optional parameters.
   Deliverable: MCP tool mapping document.

4. **Scaffold server**: Run `scripts/scaffold-mcp.py` with the parsed API structure to generate a FastMCP-compatible Python server. The generated server includes:
   - Tool definitions with type-annotated parameters.
   - Placeholder authentication (API key, OAuth, or bearer token).
   - Error handling wrappers for HTTP status codes.
   - Transport configuration (stdio by default, SSE optional).
   Deliverable: complete Python server file ready for customization.

5. **Add authentication layer**: Configure the authentication mechanism based on the API spec. Support API key (header/query), Bearer token, and OAuth2 client credentials. Deliverable: auth configuration in the server skeleton.

6. **Validate server**: Verify the generated server:
   - Python syntax check (compile without errors).
   - All tools have descriptions and input schemas.
   - No duplicate tool names.
   - Transport initializes without runtime errors.
   Deliverable: validation report with pass/fail per check.

7. **Generate policy entry**: Produce an `allowed-tools.yaml` entry for the new MCP server, including name, `mcp: true`, and recommended scopes. Deliverable: YAML snippet ready for the tool-policy-manager.

8. **Report**: Summarize the server: number of tools generated, endpoints covered, auth method, transport, and any endpoints that were skipped with reasons. Deliverable: build report.

## Anti-Patterns

- **One-giant-tool**: Mapping an entire API to a single MCP tool with a "do anything" parameter. *Why*: Agents cannot reason about tool selection when one tool does everything; granular tools enable better planning.
- **Ignoring pagination**: Generating tools that return unbounded result sets. *Why*: Large responses blow context windows and degrade agent performance.
- **Hardcoded credentials**: Embedding API keys directly in the generated server code. *Why*: Credentials leak into version control; always use environment variables.
- **Skipping error mapping**: Returning raw HTTP errors without MCP-compatible error codes. *Why*: Agents need structured error responses to retry or escalate; raw HTML error pages are unparseable.
- **Over-grouping endpoints**: Merging unrelated endpoints into one tool for "convenience." *Why*: Violates single-responsibility; agents pick the wrong tool when boundaries are fuzzy.

## Output

**On success**: Produces a directory containing:
- A FastMCP-compatible Python server file with all tool definitions.
- An `allowed-tools.yaml` snippet for policy registration.
- A build report summarizing tools generated, auth method, and coverage.

Delivered as a ready-to-run server that can be tested with `python server.py` or registered via MCP configuration.

**On failure**: Report which step failed (parse, scaffold, or validate), the specific error (malformed spec, unsupported auth, invalid endpoint), and the remediation steps. Every error must be actionable.

## Related Skills

- [`tool-policy-manager`](../../../agent-operations/agent-configuration-manager/tool-policy-manager/SKILL.md) — Register the newly built MCP server in allowed-tools.yaml after scaffolding.
- [`tool-health-checker`](../../../agent-operations/agent-operations-manager/tool-health-checker/SKILL.md) — Verify the MCP server is healthy and reachable after deployment.
