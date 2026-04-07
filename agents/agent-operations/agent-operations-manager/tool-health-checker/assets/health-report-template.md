# Tool Health Report

**Checked at**: {{checked_at}}
**Policy file**: {{policy_path}}

## Summary

| Metric | Count |
|--------|-------|
| Total tools | {{total}} |
| Healthy | {{healthy}} |
| Degraded | {{degraded}} |
| Unreachable | {{unreachable}} |
| Unknown | {{unknown}} |

## Critical Alerts

{{#if critical}}
The following tools are **unreachable** and require immediate attention:

{{#each critical}}
- **{{tool}}**: {{message}} — {{remediation}}
{{/each}}
{{else}}
No critical alerts. All probed tools are reachable.
{{/if}}

## Detailed Results

| Tool | Status | Latency (ms) | Last Checked | Message | Remediation |
|------|--------|--------------|--------------|---------|-------------|
{{#each results}}
| {{tool}} | {{status}} | {{latency_ms}} | {{last_checked}} | {{message}} | {{remediation}} |
{{/each}}

## Status Definitions

- **Healthy**: Responded within 2 seconds with a valid status code.
- **Degraded**: Responded but with high latency (>2s) or partial errors.
- **Unreachable**: No response, connection refused, or authentication failure.
- **Unknown**: No health endpoint configured; cannot be probed.

## Next Steps

1. For **unreachable** tools: verify credentials and network connectivity.
2. For **degraded** tools: check upstream service status and rate limits.
3. For **unknown** tools: add a `health_endpoint` field to `allowed-tools.yaml`.
