# Data Model: Enrich Skill Directory

**Date**: 2026-03-26

## Entities

### Skill File (`SKILL.md`)

**Location**: `agents/<agent-slug>/<skill-slug>/SKILL.md`

**YAML Frontmatter Schema**:

| Field | Type | Required | Constraints | Description |
|-------|------|----------|-------------|-------------|
| `name` | string | Yes | kebab-case, max 64 chars, `[a-z0-9-]+` | Must match parent directory name |
| `description` | string | Yes | 50–1024 chars, third-person, no angle brackets | Pushy trigger description for AI agent discovery |
| `department` | string | Yes | Must match a `departments/` subdirectory name | Organizational department |
| `agent` | string | Yes | Must match parent agent directory name | Owning agent role |
| `version` | string | Yes | Semver format `X.Y.Z` | `0.1.0` = unenriched, `1.0.0`+ = enriched |
| `complexity` | enum | Yes | `simple` \| `medium` \| `complex` | Determines word limit (500/1,000/1,500) |
| `related-skills` | list | Yes | List of relative paths to related `SKILL.md` files, may be empty `[]` | Cross-references to related skills |

**Body Sections** (in order):

| Section | Heading | Voice | Required | Purpose |
|---------|---------|-------|----------|---------|
| Title | `# <skill-slug>` | — | Yes | Must match `name` in frontmatter |
| Agent Header | `## Agent: <Role Name>` | Declarative | Yes | Seniority, description, instance type. Includes ethos reference: `Department ethos: [ideal-<dept>.md](../../../departments/<dept>/ideal-<dept>.md)` |
| Skill Description | `## Skill Description` | Third-person declarative | Yes | One sentence. Same as current format. |
| When to Use | `## When to Use` | Scenario-based | Yes | Concrete trigger conditions. Min 1 scenario. |
| Workflow | `## Workflow` | Imperative | Yes | Numbered steps with deliverables per step. |
| Anti-Patterns | `## Anti-Patterns` | Rationale-driven | Yes | What to avoid + why. "None identified" if N/A. |
| Output | `## Output` | Declarative | Yes | Success artifacts (format, content) + failure reporting (what went wrong, what to try next). |
| Related Skills | `## Related Skills` | Reference list | Yes | Links to related skills with brief rationale. Empty section if none. |

**Word Limits by Complexity**:

| Complexity | Frontmatter (Tier 1) | Body (Tier 2) | Bundled Resources (Tier 3) |
|------------|---------------------|---------------|---------------------------|
| Simple | ~100 words | Max 500 words | Unlimited, on demand |
| Medium | ~100 words | Max 1,000 words | Unlimited, on demand |
| Complex | ~100 words | Max 1,500 words | Unlimited, on demand |

**Lifecycle**:

```
Unenriched (v0.1.0) → Enriched (v1.0.0) → Refined (v1.x.y) → Scope Change (v2.0.0)
```

- `0.1.0`: Original 3-section format, awaiting enrichment
- `1.0.0`: First enriched version with all 9 sections populated
- `1.x.y`: Iterative improvements (MINOR = new content, PATCH = clarifications)
- `2.0.0`: Scope or responsibility fundamentally changed

### Skill Subdirectory

**Location**: `agents/<agent-slug>/<skill-slug>/`

| Contents | Required | Purpose |
|----------|----------|---------|
| `SKILL.md` | Yes | The skill definition file |
| `references/` | No | Domain docs loaded into context on demand |
| `examples/` | No | Working input/output pairs |
| `scripts/` | No | Executable code for deterministic tasks |
| `assets/` | No | Output templates, NOT loaded into context |
| `evals/` | No | Test prompts for skill evaluation |

### Agent Directory

**Location**: `agents/<agent-slug>/`

| Contents | Required | Purpose |
|----------|----------|---------|
| `<skill-slug>/` | Yes (1+) | Skill subdirectories |
| `references/` | No | Resources shared across all agent's skills |
| `examples/` | No | Agent-wide examples |
| `scripts/` | No | Agent-wide executable tools |
| `assets/` | No | Agent-wide output templates |

### Department

**Location**: `departments/<dept-slug>/`

| Contents | Required | Purpose |
|----------|----------|---------|
| `ideal-<dept>.md` | Yes | Ethos profile (max 500 words) |
| `references/` | No | Resources shared across all agents in department |
| `examples/` | No | Department-wide examples |
| `scripts/` | No | Department-wide executable tools |
| `assets/` | No | Department-wide output templates |

### Department Ethos Profile (`ideal-<dept>.md`)

**Location**: `departments/<dept-slug>/ideal-<dept>.md`

**Format**: Plain markdown, no frontmatter. Max 500 words.

| Section | Required | Purpose |
|---------|----------|---------|
| Title | Yes | `# Ideal <Department Name> Practitioner` |
| Philosophy | Yes | 2-3 sentences on the department's core belief |
| Principles | Yes | 5-7 opinionated principles with rationale |
| Decision Framework | No | How to resolve tradeoffs specific to this domain |

### Global Shared Context

**Location**: `_shared/`

| Contents | Required | Purpose |
|----------|----------|---------|
| `references/` | No | Cross-department domain docs |
| `scripts/` | No | Cross-department executable tools |
| `assets/` | No | Cross-department output templates |

### ETHOS.md

**Location**: Root (`ETHOS.md`)

**Format**: Plain markdown, no frontmatter. No word limit (but should be concise).

Defines the operating philosophy of the entire Skill OS. Referenced by ethos profiles but not duplicated into them.

## Relationships

```
ETHOS.md (1) ← references ← Department Ethos Profile (15)
Department (1) → contains → Agent (many)
Agent (1) → contains → Skill (many)
Skill (many) ← related-skills → Skill (many)  [bidirectional]
Skill (1) → produces → Artifact → consumed by → Skill (1)  [handoff]

Context Lookup Chain:
  Skill/references/ → Agent/references/ → Department/references/ → _shared/references/
```

## Validation Rules

| Rule | Check | Error Level |
|------|-------|-------------|
| Frontmatter `name` matches directory name | `name` == parent dir basename | ERROR |
| Frontmatter `description` length | 50 ≤ len ≤ 1024 | ERROR |
| Frontmatter `description` third-person | Does not start with "You", "I", "We" | WARNING |
| Frontmatter `version` format | Matches `\d+\.\d+\.\d+` | ERROR |
| Frontmatter `complexity` valid | In `{simple, medium, complex}` | ERROR |
| Body word count | ≤ limit for complexity class | ERROR |
| Ethos reference valid | Path in Agent header resolves to real file | ERROR |
| Related skills resolve | All paths in `related-skills` list point to existing `SKILL.md` | WARNING |
| Cross-reference files exist | All `references/`, `scripts/`, etc. paths in body resolve | WARNING |
| Department directory exists | `departments/<dept>/` exists with `ideal-<dept>.md` | ERROR |
