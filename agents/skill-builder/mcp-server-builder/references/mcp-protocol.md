# MCP Protocol Reference

Reference guide for the Model Context Protocol (MCP) as used by the mcp-server-builder skill.

## Overview

MCP is a standardized protocol for connecting AI agents to external tools. It defines how tools are discovered, invoked, and how results are returned.

## Tool Definition Format

Every MCP tool must declare:

```json
{
  "name": "resource_action",
  "description": "Human-readable description of what this tool does.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "param_name": {
        "type": "string",
        "description": "What this parameter controls."
      }
    },
    "required": ["param_name"]
  }
}
```

### Naming Conventions

- Use `snake_case` for tool names.
- Follow `resource_action` pattern: `issues_list`, `issue_create`, `issue_update`.
- For nested resources: `repo_issues_list`, `org_members_add`.
- Avoid generic names like `do_thing` or `execute`.
- Keep names under 64 characters.

### Description Best Practices

- Start with a verb: "Lists all...", "Creates a new...", "Retrieves the...".
- Include what the tool returns, not just what it does.
- Mention required context (e.g., "Requires a project ID").

## Transport

MCP supports two transport mechanisms:

### stdio (default)

- Server communicates via stdin/stdout.
- Best for local tools and CLI integrations.
- No network configuration needed.

### SSE (Server-Sent Events)

- Server runs as an HTTP endpoint.
- Best for remote tools and shared servers.
- Requires host and port configuration.

## Error Handling Patterns

### Structured Errors

Always return errors as structured objects, never raw strings:

```json
{
  "error": true,
  "code": "NOT_FOUND",
  "message": "Issue #42 not found in repository.",
  "retry": false
}
```

### Error Codes

| Code | Meaning | Retryable |
|------|---------|-----------|
| `AUTH_FAILED` | Invalid or expired credentials | No |
| `NOT_FOUND` | Resource does not exist | No |
| `RATE_LIMITED` | Too many requests | Yes |
| `TIMEOUT` | Request timed out | Yes |
| `VALIDATION` | Invalid input parameters | No |
| `SERVER_ERROR` | Upstream API error | Yes |

### Retry Policy

- Retryable errors should include a `retry_after` field (seconds).
- Maximum 3 retries with exponential backoff.
- Non-retryable errors should fail immediately with actionable messages.

## Authentication Patterns

### API Key

```python
headers = {"X-API-Key": os.environ["SERVICE_API_KEY"]}
```

### Bearer Token

```python
headers = {"Authorization": f"Bearer {os.environ['SERVICE_TOKEN']}"}
```

### OAuth2 Client Credentials

```python
# Exchange client_id + client_secret for access token, then use as Bearer.
```

### Rules

- Never hardcode credentials in server code.
- Always read from environment variables.
- Name env vars consistently: `SERVICE_NAME_API_KEY` or `SERVICE_NAME_TOKEN`.
- Validate credentials at server startup, not at first tool call.

## Input Schema Guidelines

- Use JSON Schema types: `string`, `number`, `integer`, `boolean`, `array`, `object`.
- Mark parameters as `required` only when the tool cannot function without them.
- Provide `default` values for optional parameters where sensible.
- Use `enum` to constrain values when the set is known and small.
- Add `description` to every parameter — agents use these to decide what to pass.

## Output Guidelines

- Return JSON objects, not raw strings.
- Include a top-level `success` or `error` boolean for easy status checking.
- Paginate large result sets: include `next_cursor` or `has_more` fields.
- Keep responses under 4KB when possible to preserve agent context window.
