# Data Model: Skill OS × Paperclip Integration

**Phase 1 Output** | **Date**: 2026-04-08

---

## Entities

### SkillBinding

A versioned mapping between a Paperclip agent configuration and a Skill OS skill.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `role` | `PaperclipRole` | Yes | Paperclip role enum: `engineer`, `pm`, `designer`, `qa`, `devops`, `researcher`, `cto`, `cmo`, `cfo`, `ceo`, `general` |
| `label` | `string` | Yes | `IssueLabel.name` value that triggers this binding (e.g., `prd`, `threat-model`) |
| `skill_path` | `string` | Yes | Relative path to `SKILL.md` from repo root (e.g., `agents/product/product-manager/prd-author/SKILL.md`) |
| `skill_version` | `string` | No | Pin to a specific git commit SHA or semver tag; omit for latest |
| `fallback_ethos` | `string` | No | Path to department ethos profile used when no skill matches (e.g., `departments/product/ideal-product.md`) |
| `model_override` | `string` | No | Override Claude model for this skill (e.g., `claude-opus-4-6` for L3 complex skills) |

**Validation rules**:
- `skill_path` MUST resolve to an existing file
- `label` MUST be a non-empty string with no spaces (use hyphens)
- `role` MUST be one of the 11 Paperclip role values
- If `skill_version` is set, it MUST be a valid git SHA or semver string

---

### RoutingTable

The top-level operator configuration document. Contains one or more `SkillBinding` entries organized by role.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `version` | `string` | Yes | Schema version (e.g., `"1.0"`) |
| `skill_os_root` | `string` | Yes | Absolute or relative path to the Skill OS repo root |
| `bindings` | `SkillBinding[]` | Yes | List of skill bindings |
| `default_fallback` | `string` | No | Global fallback ethos path when no role+label match is found |

---

### AgentRoleMapping

A reference table mapping Paperclip's 11 roles to the relevant Skill OS departments and agent slugs. Used by operators to discover which skills apply to each Paperclip role.

| Paperclip Role | Skill OS Department(s) | Primary Agent Slugs |
|----------------|----------------------|---------------------|
| `cto` | Engineering | `vp-engineering`, `tech-architect`, `tech-lead-pr-reviewer` |
| `engineer` | Engineering | `sr-backend-developer`, `sr-frontend-developer`, `devops-infrastructure-engineer`, `security-engineer`, `ai-ml-engineer`, `platform-engineer`, `data-engineer` |
| `qa` | Engineering | `qa-test-engineer` |
| `devops` | Engineering | `devops-infrastructure-engineer`, `platform-engineer` |
| `pm` | Product | `product-manager`, `vp-product`, `product-operations-analyst` |
| `designer` | Design | `ux-ui-designer`, `ux-researcher`, `brand-designer`, `content-designer-ux-writer` |
| `cmo` | Marketing | `vp-marketing`, `demand-gen-manager`, `content-marketer` |
| `cfo` | Finance | `cfo-vp-finance`, `fpa-analyst`, `controller-accounting` |
| `researcher` | Applied Research, Data & Growth | `applied-research-lead`, `analytics-lead`, `data-analyst` |
| `ceo` | (all departments — strategic) | `vp-sales`, `vp-marketing`, `vp-engineering`, `vp-product` |
| `general` | All others | Sales, Legal, CS, Support, Revenue Ops, Account Mgmt, Implementation |

---

## Relationships

```
RoutingTable
  └── bindings: SkillBinding[]
        ├── role          → PaperclipRole (enum)
        ├── label         → IssueLabel.name (Paperclip)
        ├── skill_path    → SKILL.md (Skill OS filesystem)
        └── fallback_ethos → ideal-<dept>.md (Skill OS filesystem)

AgentRoleMapping
  ├── PaperclipRole → Skill OS departments[]
  └── Skill OS departments[] → agent slugs[]
```

---

## State Transitions

A `SkillBinding` is active when:
1. `role` matches `agent.role` in Paperclip
2. `label` matches any `IssueLabel.name` on the dispatched issue
3. `skill_path` file exists at resolution time

If neither condition matches, `fallback_ethos` is used. If no fallback is configured, the agent operates without Skill OS context.

---

## Validation Rules Summary

| Rule | Severity |
|------|----------|
| `skill_path` must resolve to existing `SKILL.md` | Error |
| `role` must be valid Paperclip role enum value | Error |
| `label` must be non-empty, no whitespace | Error |
| `version` field required in RoutingTable | Error |
| `skill_os_root` must be a valid path | Error |
| `model_override` should be a recognized Claude model ID | Warning |
| Duplicate `role+label` combinations in same RoutingTable | Warning |
