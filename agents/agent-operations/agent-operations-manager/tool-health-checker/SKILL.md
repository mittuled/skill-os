---
name: tool-health-checker
description: >
  This skill checks the health and connectivity status of all tools registered
  in allowed-tools.yaml. Use when asked to verify tool connections, diagnose
  tool failures, or generate a fleet health report. Also consider when agents
  report tool timeouts or authentication errors. Suggest when the user deploys
  a new tool without verifying it is reachable.
department: agent-operations
agent: agent-operations-manager
version: 1.0.0
complexity: medium
triggers:
  - check tool health
  - are our tools working
  - tool connectivity status
  - verify tool connections
related-skills:
  - ../../../agent-operations/agent-configuration-manager/tool-policy-manager/SKILL.md
  - ../../../agent-operations/skill-builder/mcp-server-builder/SKILL.md
---

# tool-health-checker

## Agent: Agent Operations Manager

L2 Agent Operations Manager (1x) responsible for message passing infrastructure, context sharing protocols, inter-agent coordination, and agent health monitoring.

Department ethos: [ideal-agent-operations.md](../../../../departments/agent-operations/ideal-agent-operations.md)

Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Probes all tools registered in the fleet's tool policy file to assess connectivity, authentication validity, and response latency, producing a structured health report.

## When to Use

- When a routine health check is needed to verify all registered tools are operational.
- When agents report tool errors or timeouts and the root cause is unclear.
- When a new tool has been added to allowed-tools.yaml and needs connectivity verification.
- When preparing for a deployment and tool dependencies must be confirmed healthy.

## Workflow

1. **Load policy**: Read `allowed-tools.yaml` from the repository root and parse all tool entries across every level (company-wide, department, agent, skill). Deliverable: deduplicated list of tools with their scopes and MCP status.
2. **Probe each tool**: For each tool, run `scripts/check-health.py` to perform a lightweight connectivity test. For MCP tools, attempt a protocol handshake. For non-MCP tools, issue an HTTP HEAD or GET to the health endpoint. Deliverable: raw probe results (status code, latency, error message if any).
3. **Classify status**: Assign each tool a health status based on probe results:
   - **Healthy**: responded within 2 seconds, valid auth, expected status code.
   - **Degraded**: responded but with high latency (>2s) or partial errors.
   - **Unreachable**: no response, connection refused, or authentication failure.
   Deliverable: classified health status per tool.
4. **Generate report**: Render results using `assets/health-report-template.md`. Include tool name, status, latency, last checked timestamp, and remediation suggestions for non-healthy tools. Deliverable: markdown health report.
5. **Alert on critical**: If any tool is unreachable, flag it as a critical finding requiring immediate attention. Deliverable: critical alert list (may be empty).

## Anti-Patterns

- **Deep integration tests**: Running full API workflows instead of lightweight probes. *Why*: Health checks should be fast and non-destructive; deep tests risk side effects and take too long for routine monitoring.
- **Ignoring auth expiry**: Checking connectivity but not validating that credentials are still accepted. *Why*: A reachable tool with expired credentials is effectively unreachable to agents.
- **Stale reports**: Running health checks once and caching results indefinitely. *Why*: Tool health changes; reports must reflect current state to be actionable.
- **Alert fatigue**: Flagging every minor latency spike as critical. *Why*: Over-alerting causes operators to ignore real failures; reserve critical for genuinely unreachable tools.

## Output

**On success**: Produces a markdown health report (using `assets/health-report-template.md`) listing every registered tool with its status, latency, and any remediation notes. Delivered as a file or inline summary.

**On failure**: Report which tools could not be probed and why (network error, missing config, invalid policy file), what was attempted, and the next steps to resolve. Every error must be actionable.

## Related Skills

- [`tool-policy-manager`](../../../agent-operations/agent-configuration-manager/tool-policy-manager/SKILL.md) — Health checks depend on the policy file being valid; policy changes should trigger a health check.
- [`mcp-server-builder`](../../../agent-operations/skill-builder/mcp-server-builder/SKILL.md) — Newly built MCP servers should be health-checked before being considered operational.
