# Implementation Plan: Skill Quality Improvements

**Branch**: `002-skill-quality-improvements` | **Date**: 2026-03-27 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/002-skill-quality-improvements/spec.md`

## Summary

Add tooling infrastructure (company onboarding, tool policy management, MCP server builder, health checker) and platform enhancements (triggers, checkpoint gates, scoring rubrics, code examples) to skill-os. Creates 4 new executable skills with helper scripts, a structured `allowed-tools.yaml` policy file, and enhances the frontmatter schema and validation script.

## Technical Context

**Language/Version**: Python 3.10+ for executable scripts, Bash for shell helpers. Markdown + YAML for skill files and policy files.
**Primary Dependencies**: None beyond stdlib — scripts must be zero-dependency (per existing convention from `scripts/validate.py`).
**Storage**: Git-managed filesystem. `allowed-tools.yaml` at repo root. Credentials in platform-native secret stores (never in repo).
**Testing**: Manual validation via `scripts/validate.py` (extended for new fields). Skill effectiveness tested via Anthropic's eval pattern.
**Target Platform**: GitHub (consumed by Claude, Codex, Cursor, and other AI agent runtimes).
**Project Type**: Documentation repository + executable skill library.
**Performance Goals**: N/A — documentation repo with lightweight scripts.
**Constraints**: Platform-agnostic format. Zero external dependencies for scripts. Backward-compatible with existing 495 skills.
**Scale/Scope**: 4 new skills + updates to validation script, schema, constitution, enrichment template. ~50 skills get `triggers`, ~20 get `[GATE]` markers, ~10 get scoring rubrics, ~20 get code examples.

## Constitution Check

*Verified against constitution v2.0.0.*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Template Fidelity | **PASS** | 4 new skills follow the enriched 9-section format with YAML frontmatter. Additionally include `scripts/` per the hybrid model (FR-003b). |
| II. Single Responsibility | **PASS** | Each of the 4 tooling skills has a distinct responsibility: onboarding ≠ policy management ≠ MCP building ≠ health checking. |
| III. Org Chart Consistency | **PASS** | New skills are added under existing agents (Agent Configuration Manager, Skill Builder, Agent Operations Manager). Org chart updated. |
| IV. Canonical Naming | **PASS** | All new skill directories use kebab-case. |
| V. Atomic Commits | **PASS** | Each new skill = 1 commit. Schema/validation updates = separate commits. |
| VI. Progressive Disclosure | **PASS** | New skills follow word limits. Executable logic lives in `scripts/`, not in the SKILL.md body. |
| VII. Department Ethos | **PASS** | New skills reference the Agent Operations ethos profile. |

**Constitutional amendment required**: MINOR bump to v2.1.0 to document `triggers`, `[GATE]`, `allowed-tools.yaml`, and the 4 new skills. Tracked as a Phase 1 deliverable.

## Project Structure

### Repository Changes

```text
skill-os/
├── allowed-tools.yaml                    # NEW — tool access policy (FR-004)
├── scripts/
│   └── validate.py                       # UPDATED — triggers, [GATE], allowed-tools validation
│
├── agents/
│   ├── agent-configuration-manager/
│   │   ├── company-tooling-onboarder/    # NEW — US1
│   │   │   ├── SKILL.md
│   │   │   ├── scripts/
│   │   │   │   ├── discover-tools.py     # Tool category interviewer
│   │   │   │   ├── connect-mcp.py        # MCP server connector
│   │   │   │   └── configure-secrets.py  # Platform secret store setup
│   │   │   └── references/
│   │   │       └── tool-categories.md    # Standard tool categories checklist
│   │   └── tool-policy-manager/          # NEW — US2
│   │       ├── SKILL.md
│   │       ├── scripts/
│   │       │   └── validate-policy.py    # YAML schema validation
│   │       └── assets/
│   │           └── allowed-tools-template.yaml
│   │
│   ├── skill-builder/
│   │   └── mcp-server-builder/           # NEW — US3
│   │       ├── SKILL.md
│   │       ├── scripts/
│   │       │   ├── parse-openapi.py      # OpenAPI spec parser
│   │       │   └── scaffold-mcp.py       # MCP server scaffolding
│   │       └── references/
│   │           └── mcp-protocol.md       # MCP protocol reference
│   │
│   └── agent-operations-manager/
│       └── tool-health-checker/          # NEW — US4
│           ├── SKILL.md
│           ├── scripts/
│           │   └── check-health.py       # Connectivity + auth checker
│           └── assets/
│               └── health-report-template.md
│
├── specs/002-skill-quality-improvements/
│   ├── contracts/
│   │   ├── allowed-tools-schema.yaml     # Policy file schema
│   │   └── triggers-schema.yaml          # Triggers frontmatter schema
│   └── ...
│
└── .specify/memory/constitution.md       # UPDATED — v2.1.0
```

**Structure Decision**: Documentation repo with hybrid executable skills. New skills follow the standard `<skill>/SKILL.md` + `scripts/` pattern. No new top-level directories beyond `allowed-tools.yaml` at root.

## Complexity Tracking

No constitutional violations — all principles pass.

---

## Phase Overview

| Phase | Scope | Deliverables |
|-------|-------|-------------|
| 0 | Research | MCP protocol patterns, open-source converters, tool category inventory |
| 1 | Design | `allowed-tools-schema.yaml`, `triggers-schema.yaml`, data model, quickstart |
| 2 | Tooling Skills (P1-P4) | 4 new skills with scripts |
| 3 | Platform Enhancements (P5-P8) | Triggers, gates, rubrics, code examples across existing skills |
| 4 | Quality Fixes (P9) | Engineering + Legal skill rewrites |
| 5 | Validation & Finalize | Schema updates, constitution amendment, validation script |

---

## Phase 0: Research

No NEEDS CLARIFICATION items remain — all resolved during `/speckit.clarify`. Research is needed for:

1. **MCP protocol best practices**: How existing MCP servers are structured (FastMCP, MCP SDK), what makes a good MCP tool interface, error handling patterns.
2. **Open-source MCP converters**: Which tools exist for REST-to-MCP, OpenAPI-to-MCP conversion. Evaluate: FastMCP (Python), MCP SDK (TypeScript).
3. **Tool category inventory**: Standard SaaS tool categories and the most popular tools per category (for the onboarding skill's interview flow).

---

## Phase 1: Design & Contracts

### Deliverables

1. **`contracts/allowed-tools-schema.yaml`** — machine-readable schema for the policy file
2. **`contracts/triggers-schema.yaml`** — frontmatter schema extension for triggers
3. **`data-model.md`** — entities, relationships, validation rules
4. **`quickstart.md`** — how to onboard tools, add triggers, use gates
5. **Constitutional amendment** — v2.1.0 draft

### `allowed-tools.yaml` Schema

```yaml
schema_version: 1

company-wide:
  - name: slack
    mcp: true
    scopes: [read, send]
  - name: github
    mcp: true
    scopes: [read, write, pr]

department:
  engineering:
    - name: datadog
      mcp: true
      scopes: [read]
    - name: pagerduty
      mcp: true
  legal:
    - name: docusign
      mcp: true
      scopes: [read, send]

agent:
  security-engineer:
    - name: burpsuite
      mcp: false

skill:
  contract-review-orchestrator:
    - name: docusign
      scopes: [read]
```

### Context Lookup for Tools

When an agent needs to know its available tools:
1. Load `allowed-tools.yaml` from repo root
2. Collect `company-wide` tools (available to all)
3. Add `department/<agent's-department>` tools
4. Add `agent/<agent-slug>` tools (if any)
5. Add `skill/<skill-slug>` tools (if any, for the active skill)
6. The union of all levels = the agent's tool set

---

## Execution Strategy

### Phase 2: Tooling Skills (4 new skills)

Create sequentially — each depends on the previous for cross-referencing:

1. **company-tooling-onboarder** (complex) — the entry point
2. **tool-policy-manager** (medium) — manages the policy file the onboarder creates
3. **mcp-server-builder** (complex) — called by the onboarder for tools without MCP
4. **tool-health-checker** (medium) — verifies everything the onboarder connected

Each skill = SKILL.md + `scripts/` + `references/` or `assets/`. One commit per skill.

### Phase 3: Platform Enhancements

Can run in parallel — independent changes to different files:

1. **Triggers** (US5): Update validation script + add `triggers` to ~50 skills
2. **Gates** (US6): Update validation script + add `[GATE]` to ~20 complex skills
3. **Rubrics** (US7): Create scoring rubrics for ~10 assessment skills
4. **Code examples** (US8): Add code examples to ~20 engineering skills

### Phase 4: Quality Fixes (US9)

Rewrite Engineering skills scoring below 5/5 and Legal skills missing anti-pattern rationale. Cross-references with `003-production-grade-depth` — fixes here are targeted rewrites, not the full depth pass.

### Phase 5: Validation & Finalize

1. Update `scripts/validate.py` for `triggers`, `[GATE]`, `allowed-tools.yaml`
2. Amend constitution to v2.1.0
3. Update `CLAUDE.md`, enrichment template, quickstart
4. Full repo validation — 0 errors
5. Update `status.md`
