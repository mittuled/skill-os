# Implementation Plan: Skill OS × Paperclip Integration

**Branch**: `004-skill-os-paperclip-integration` | **Date**: 2026-04-08 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/004-skill-os-paperclip-integration/spec.md`

## Summary

Make Skill OS's 528 skills directly consumable by Paperclip agent companies. Deliver a `paperclip/` integration directory at repo root containing a YAML skill-binding schema, a default routing table mapping Paperclip task tags to Skill OS skills, and an operator quickstart guide. No source code is required — this is a configuration and documentation project layered on top of the existing markdown skill library.

## Technical Context

**Language/Version**: Markdown + YAML (configuration project, zero code)
**Primary Dependencies**: None (static files only)
**Storage**: Git-managed filesystem — same as the rest of Skill OS
**Testing**: Manual verification + `python3 scripts/validate.py` for skill file integrity
**Target Platform**: Paperclip (Node.js + React) consuming static markdown/YAML files
**Project Type**: Configuration/documentation integration
**Performance Goals**: N/A — static files have no runtime performance requirements
**Constraints**: Skill bodies ≤1,500 words (constitution Principle VI); YAML files must be human-editable without tooling
**Scale/Scope**: 528 skills × 80 agent roles × 16 departments; initial routing table covers top 50 most-used skills

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-checked after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Template Fidelity | ✅ Pass | No new skills added in Phase 1; any future skills follow 9-section format |
| II. Single Responsibility | ✅ Pass | Integration config is a separate concern from skill definitions |
| III. Org Chart Consistency | ✅ Pass | No agent directories added; AGENTS.md unchanged |
| IV. Canonical Naming | ✅ Pass | New directory `paperclip/` at repo root — outside `agents/` tree |
| V. Atomic Commits | ✅ Pass | Each deliverable file = 1 commit |
| VI. Progressive Disclosure | ✅ Pass | Routing table references SKILL.md paths; progressive loading documented in quickstart |
| VII. Department Ethos | ✅ Pass | No new departments; existing ethos profiles referenced in routing table |
| VIII. Tool Policy | ✅ Pass | No new tool integrations; allowed-tools.yaml unchanged |
| IX–X. Optional Extensions / Gates | ✅ Pass | No new skills; [GATE] documentation included in quickstart |

**Result**: No violations. Plan may proceed.

## Project Structure

### Documentation (this feature)

```text
specs/004-skill-os-paperclip-integration/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output
│   └── skill-binding-schema.md
└── tasks.md             # Phase 2 output (/speckit.tasks)
```

### Deliverables (repository root)

```text
paperclip/
├── README.md                    # Operator quickstart: how to use Skill OS with Paperclip
├── skill-routing-table.yaml     # Default tag → skill slug mappings (top 50 skills)
├── skill-binding-schema.yaml    # Schema for operator-defined skill binding configs
└── examples/
    ├── engineering-team.yaml    # Sample: 5-person eng team config
    ├── full-company.yaml        # Sample: CEO+CTO+PM+engineer+marketer config
    └── single-agent.yaml        # Sample: simplest possible single-agent config
```

## Phases

### Phase 0: Research

Resolve open questions about Paperclip's agent configuration model.

**Research tasks:**
1. How does Paperclip deliver context to agents? (system prompt field, heartbeat payload, or config file)
2. What task tag format does Paperclip support? (free-form strings, enums, structured objects)
3. What are Paperclip's default role names in the org chart? (must map to Skill OS agent slugs)
4. Does Paperclip support file path references in agent config, or must content be inlined?

**Output**: `research.md` with decisions and rationale for each question.

### Phase 1: Design & Contracts

**Prerequisites**: `research.md` complete

1. **Skill Binding Schema** → `contracts/skill-binding-schema.md`
   - Define the YAML structure an operator uses to bind a skill to an agent role + task tag
   - Cover: agent role, task tag pattern, skill path, skill version, fallback ethos path

2. **Data Model** → `data-model.md`
   - Entities: SkillBinding, RoutingTable, AgentRoleMapping
   - Relationships and validation rules

3. **Quickstart** → `quickstart.md`
   - 5-step operator guide: browse skills → select → configure binding → attach to agent → verify output
   - Progressive loading pattern with token budget guidance
   - [GATE] marker handling instructions

**Output**: `data-model.md`, `contracts/skill-binding-schema.md`, `quickstart.md`

## Complexity Tracking

No constitution violations to justify.
