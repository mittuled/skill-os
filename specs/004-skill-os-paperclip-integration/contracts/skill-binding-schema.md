# Contract: Skill Binding Schema

**Version**: 1.0 | **Date**: 2026-04-08

---

## Overview

The skill routing table is a YAML file that maps Paperclip agent roles + issue labels to Skill OS skill paths. Paperclip operators create this file in their company repo and reference it from their agent `adapterConfig.instructionsFilePath` setup.

---

## Schema

```yaml
# skill-routing-table.yaml
version: "1.0"
skill_os_root: "./skill-os"          # Path to Skill OS repo, absolute or relative to this file
default_fallback: null               # Optional: global fallback ethos path

bindings:
  - role: engineer                   # Paperclip role (required)
    label: backend-api               # IssueLabel.name (required)
    skill_path: agents/engineering/sr-backend-developer/builder/SKILL.md
    fallback_ethos: departments/engineering/ideal-engineering.md
    model_override: null             # Optional: claude-opus-4-6 for complex skills

  - role: engineer
    label: threat-model
    skill_path: agents/engineering/security-engineer/threat-modelling/SKILL.md
    model_override: claude-opus-4-6  # L3 complex skill — use strongest model

  - role: pm
    label: prd
    skill_path: agents/product/product-manager/prd-author/SKILL.md
    fallback_ethos: departments/product/ideal-product.md

  - role: pm
    label: experiment
    skill_path: agents/product/product-manager/experiment-designer/SKILL.md

  - role: designer
    label: usability-review
    skill_path: agents/design/ux-ui-designer/usability-heuristic-reviewer/SKILL.md

  - role: cto
    label: architecture-review
    skill_path: agents/engineering/tech-architect/system-design-author/SKILL.md
    model_override: claude-opus-4-6

  - role: cmo
    label: gtm
    skill_path: agents/marketing/vp-marketing/gtm-planner-marketing/SKILL.md

  - role: researcher
    label: data-analysis
    skill_path: agents/data-growth/data-analyst/sql-query-author/SKILL.md
```

---

## Field Reference

| Field | Type | Required | Values |
|-------|------|----------|--------|
| `version` | string | Yes | `"1.0"` |
| `skill_os_root` | string | Yes | Relative or absolute path to Skill OS repo root |
| `default_fallback` | string or null | No | Path to a `ideal-<dept>.md` file |
| `bindings[].role` | string | Yes | `ceo` `cto` `cmo` `cfo` `engineer` `designer` `pm` `qa` `devops` `researcher` `general` |
| `bindings[].label` | string | Yes | Matches `IssueLabel.name` in Paperclip — kebab-case recommended |
| `bindings[].skill_path` | string | Yes | Relative path from `skill_os_root` to a `SKILL.md` file |
| `bindings[].fallback_ethos` | string or null | No | Path to department ethos profile |
| `bindings[].model_override` | string or null | No | Claude model ID; omit to inherit agent default |

---

## Matching Logic

1. On task dispatch, Paperclip provides `agent.role` and `issue.labels[]`
2. For each label on the issue, look for a binding where `role == agent.role AND label == issueLabel.name`
3. First match wins; load `skill_path` as `instructionsFilePath`
4. If no match: use `fallback_ethos` (binding-level, then `default_fallback`, then nothing)
5. Multiple labels on one issue: first label in the list that matches a binding wins

---

## Paperclip Agent Configuration

To wire a skill to a Paperclip agent, set `instructionsFilePath` in the agent's adapter config:

```json
{
  "adapterType": "claude_local",
  "adapterConfig": {
    "cwd": "/path/to/company-repo",
    "model": "claude-sonnet-4-6",
    "instructionsFilePath": "/path/to/skill-os/agents/engineering/sr-backend-developer/builder/SKILL.md",
    "promptTemplate": "You are {{agent.title}}, a {{agent.role}} at {{company.name}}. Your current task: {{issue.title}}.\n\nFetch full context: GET /api/issues/{{issue.id}}/heartbeat-context before beginning your workflow."
  }
}
```

For dynamic routing (label-based), the `instructionsFilePath` must be resolved at dispatch time by the routing table — this requires a thin adapter script or Paperclip plugin (out of scope for v1; v1 uses static per-agent `instructionsFilePath`).

---

## Versioning

- `version: "1.0"` — initial schema (static per-agent bindings)
- Future: `version: "2.0"` — dynamic label-based routing (requires Paperclip adapter support)
