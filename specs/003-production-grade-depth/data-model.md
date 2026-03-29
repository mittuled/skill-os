# Data Model: Production-Grade Skill Depth

**Branch**: `003-production-grade-depth` | **Date**: 2026-03-28

## Entities

### Scoring Rubric

**Location**: `<skill>/references/scoring-rubric.md`
**Required for**: All assessment/evaluation skills (~125 skills)

| Field | Type | Constraints |
|-------|------|------------|
| Title | string | `# Scoring Rubric: <skill-name>` |
| Purpose | string | One-sentence description of what is being scored |
| Criteria | list[Criterion] | 3-6 items, weights sum to 100% |
| Scale | enum | `0-10` (default) or `0-100` for composite scores |
| Grade Bands | list[GradeBand] | 7 bands: A+ through F |
| Signal Tables | list[SignalTable] | One per criterion |

**Criterion**:
| Field | Type | Constraints |
|-------|------|------------|
| Name | string | Descriptive, domain-specific |
| Weight | integer | Percentage, all criteria sum to 100% |
| Description | string | What this criterion measures |

**GradeBand**:
| Field | Type | Constraints |
|-------|------|------------|
| Grade | enum | A+, A, B, C, D, F |
| Score Range | string | e.g., "9.0-10.0", "8.0-8.9" |
| Label | string | e.g., "Exceptional", "Strong", "Adequate" |
| Description | string | What performance at this level looks like |
| Action | string | Recommended next step for this grade |

**SignalTable**:
| Field | Type | Constraints |
|-------|------|------------|
| Criterion | string | Must match a Criterion.Name |
| Signals | list[Signal] | 4-6 rows covering the full 0-10 range |

**Signal**:
| Field | Type | Constraints |
|-------|------|------------|
| Score Range | string | e.g., "9-10", "7-8", "5-6", "3-4", "0-2" |
| Evidence | string | Observable, verifiable evidence that maps to this score |

---

### Output Template

**Location**: `<skill>/assets/<output-name>-template.md`
**Required for**: All output-producing skills (~136 skills)

| Field | Type | Constraints |
|-------|------|------------|
| Title | string | `# <Output Name> Template` |
| Metadata Block | object | Date, Author, Version, Status placeholders |
| Executive Summary | section | 2-3 sentence placeholder with guidance |
| Content Sections | list[Section] | Domain-specific, pre-defined headings |
| Appendices | section | Optional supporting materials |

**Section**:
| Field | Type | Constraints |
|-------|------|------------|
| Heading | string | Descriptive section name |
| Purpose | string | What this section communicates |
| Placeholder | string | Example content showing expected format |
| Guidance | string | What good vs. bad content looks like |

---

### Signal Table (standalone)

**Location**: `<skill>/references/signal-table.md` or embedded in scoring rubric
**Required for**: Skills with complex decision logic that aren't full assessments

| Field | Type | Constraints |
|-------|------|------------|
| Title | string | `# Signal Table: <decision-name>` |
| Context | string | When to use this table |
| Dimensions | list[Dimension] | 2-8 scoring dimensions |

**Dimension**:
| Field | Type | Constraints |
|-------|------|------------|
| Name | string | What is being evaluated |
| Signals | list[Signal] | Same structure as rubric signals |

---

### Domain Checklist

**Location**: `<skill>/references/checklist.md`
**Required for**: Workflow-only skills that verify or audit

| Field | Type | Constraints |
|-------|------|------------|
| Title | string | `# <Domain> Checklist` |
| Framework | string | Which standard/framework this derives from |
| Categories | list[Category] | Grouped checklist items |

**Category**:
| Field | Type | Constraints |
|-------|------|------------|
| Name | string | Category heading |
| Items | list[ChecklistItem] | 3-15 items per category |

**ChecklistItem**:
| Field | Type | Constraints |
|-------|------|------------|
| Item | string | What to check |
| Severity | enum | Critical, Major, Minor |
| Evidence | string | How to verify this item |

---

### Framework Detail

**Location**: `<skill>/references/framework.md`
**Required for**: Workflow-only skills that apply a named methodology

| Field | Type | Constraints |
|-------|------|------------|
| Title | string | `# <Framework Name> Reference` |
| Overview | string | What the framework is and when to apply it |
| Components | list[Component] | Framework elements with application guidance |
| Application | string | How to apply within the skill's workflow |

---

## Relationships

```
Skill (SKILL.md)
├── has 0..1 Scoring Rubric (assessment skills)
├── has 0..n Output Templates (output-producing skills)
├── has 0..n Signal Tables (decision-heavy skills)
├── has 0..n Domain Checklists (audit/verification skills)
└── has 0..n Framework Details (methodology-driven skills)
```

Every skill gets at minimum one `references/` file. The type depends on skill classification:
- Assessment → scoring-rubric.md (required) + output template (if produces report)
- Output → output template (required) + framework or checklist in references/
- Workflow → framework, checklist, or signal table in references/ (at least one)

## State Transitions

Skills progress through one state change:

```
[Shallow] → [Production-Grade]
  body only    body + references/ + assets/
```

No intermediate states. Each skill is either shallow (current state) or production-grade (target state). The transition is atomic per commit.
