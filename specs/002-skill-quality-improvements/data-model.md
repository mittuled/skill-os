# Data Model: Skill Quality Improvements

**Date**: 2026-03-27

## New Entities

### Tool Policy File (`allowed-tools.yaml`)

**Location**: Repo root

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `schema_version` | integer | Yes | Current: 1. Incremented on format changes. |
| `company-wide` | list of Tool entries | Yes | Tools available to all agents |
| `department` | map (dept → list of Tool entries) | No | Department-restricted tools |
| `agent` | map (agent → list of Tool entries) | No | Agent-restricted tools |
| `skill` | map (skill → list of Tool entries) | No | Skill-restricted tools |

**Tool Entry**:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes | Tool identifier (kebab-case) |
| `mcp` | boolean | Yes | Whether an MCP server exists for this tool |
| `scopes` | list of strings | No | Permitted actions (e.g., `[read, write, send]`) |

**Lookup chain**: company-wide ∪ department ∪ agent ∪ skill. Union merge — most permissive wins.

**Validation rules**:
- `schema_version` must be a supported version (currently only `1`)
- Department keys must match `departments/` subdirectory names
- Agent keys must match `agents/` subdirectory names
- Skill keys must match `agents/<agent>/<skill>/` directory paths
- Duplicate tool names across levels are allowed (union merge)

### Triggers (Frontmatter Extension)

**Location**: YAML frontmatter in any SKILL.md

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `triggers` | list of strings | No | 2-10 word phrases for fuzzy matching activation |

**Validation**: Each item is a non-empty string, 5-50 chars. Empty list valid. Absent field valid.

### Checkpoint Gate (`[GATE]` Marker)

**Location**: Inline in Workflow section of any SKILL.md

**Format**: `[GATE]` appended to a workflow step line.

**Example**: `3. **Deploy to staging**: Push the build to staging environment. Deliverable: staging URL. [GATE]`

**Validation**: Accepted in any workflow step. Warning if skill complexity is `simple`.

### Scoring Rubric (`references/scoring-rubric.md`)

**Location**: `<skill>/references/scoring-rubric.md`

**Required structure**:

| Section | Description |
|---------|-------------|
| Criteria | Named dimensions being scored |
| Weights | Percentage weight per criterion (must sum to 100%) |
| Scale | Numeric range per criterion (0-10 or 0-100) |
| Grade bands | Score ranges mapped to letter grades (A+ through F) |
| Signal tables | Observable evidence mapped to score values |

## Updated Entities

### Agent Header (Extended)

Added line after ethos reference:

```
Tool policy: [allowed-tools.yaml](../../allowed-tools.yaml)
```

### Frontmatter Schema (Extended)

New optional field: `triggers` (list of strings).

### Validation Script (Extended)

New checks:
- `triggers`: list of strings when present
- `[GATE]`: accepted in workflow, warning if simple skill
- `allowed-tools.yaml`: valid YAML, schema_version supported, references resolve

## Relationships

```
allowed-tools.yaml (1) → referenced by → Agent Header (all agents)
company-tooling-onboarder → creates → allowed-tools.yaml
tool-policy-manager → updates → allowed-tools.yaml
tool-health-checker → reads → allowed-tools.yaml (to know what to check)
mcp-server-builder → called by → company-tooling-onboarder (for tools without MCP)
triggers (frontmatter) → complements → description (frontmatter)
[GATE] (workflow) → signals → AI agent runtime (pause for human approval)
scoring-rubric (references) → referenced by → Workflow section
```
