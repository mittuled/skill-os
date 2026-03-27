---
name: tool-policy-manager
description: >
  This skill manages the tool access policy file (allowed-tools.yaml) for the
  agent fleet. Use when asked to add a tool, remove tool access, update tool
  permissions, or modify scopes at any level. Also consider when onboarding a
  new MCP server that needs policy entries. Suggest when the user grants tool
  access without updating the canonical policy file.
department: agent-operations
agent: agent-configuration-manager
version: 1.0.0
complexity: medium
triggers:
  - manage tool access
  - update tool permissions
  - add a tool
  - remove tool access
related-skills:
  - ../../agent-operations-manager/tool-health-checker/SKILL.md
  - ../../skill-builder/mcp-server-builder/SKILL.md
---

# tool-policy-manager

## Agent: Agent Configuration Manager

L2 Agent Configuration Manager (1x) responsible for model selection per agent, compute budget allocation, context window sizing, tool access policies, and API key management.

Department ethos: [ideal-agent-operations.md](../../../departments/agent-operations/ideal-agent-operations.md)

Tool policy: [allowed-tools.yaml](../../../allowed-tools.yaml)

## Skill Description

Manages the canonical tool access policy file by validating, applying, and auditing changes to tool permissions at company, department, agent, and skill levels.

## When to Use

- When a new tool or MCP server needs to be added to the fleet's allowed tools.
- When tool permissions or scopes need to be modified for a department, agent, or skill.
- When revoking tool access after a security review or deprecation.
- When onboarding a new department and its baseline tooling must be declared.

## Workflow

1. **Read current policy**: Load `allowed-tools.yaml` from the repository root. Deliverable: parsed policy object with all levels (company-wide, department, agent, skill).
2. **Validate request**: Confirm the requested change specifies a tool name, target level, action (add/remove/modify), and scopes. Reject ambiguous requests. Deliverable: validated change request.
3. **Check conflicts**: Verify the change does not create conflicting permissions (e.g., removing a company-wide tool that a skill explicitly requires). Deliverable: conflict report or clean signal.
4. **Apply change**: Insert, update, or remove the tool entry at the specified level. Preserve YAML comments and formatting. Deliverable: modified policy object.
5. **Validate schema**: Run `scripts/validate-policy.py` against the modified file to confirm schema compliance. Deliverable: validation pass/fail with diagnostics.
6. **Report result**: Summarize what changed, at which level, and any downstream impacts. Deliverable: change summary with before/after diff.

## Anti-Patterns

- **Blanket company-wide grants**: Adding tools at company-wide level when only one agent needs them. *Why*: Violates least-privilege; every agent inherits access, expanding the attack surface unnecessarily.
- **Scope inflation**: Granting write scopes when only read is needed. *Why*: Excess permissions increase blast radius of misconfigured agents.
- **Silent removals**: Removing a tool entry without checking which skills depend on it. *Why*: Downstream skills will fail at runtime with no diagnostic trace.
- **Skipping validation**: Editing allowed-tools.yaml by hand without running the schema validator. *Why*: Malformed YAML or missing fields cause silent policy failures.

## Output

**On success**: Produces an updated `allowed-tools.yaml` file and a change summary listing the tool name, level, action taken, and resulting scopes. Delivered as a commit-ready file change.

**On failure**: Report the rejected change reason (conflict, schema violation, or missing fields), the attempted modification, and the corrective action required. Every error must be actionable.

## Related Skills

- [`tool-health-checker`](../../agent-operations-manager/tool-health-checker/SKILL.md) — After policy changes, verify the newly added or modified tool is reachable and healthy.
- [`mcp-server-builder`](../../skill-builder/mcp-server-builder/SKILL.md) — When adding an MCP-based tool, the server must be built before the policy entry is meaningful.
