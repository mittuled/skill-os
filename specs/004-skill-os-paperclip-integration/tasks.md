# Tasks: Skill OS × Paperclip Integration

**Input**: Design documents from `/specs/004-skill-os-paperclip-integration/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/skill-binding-schema.md, quickstart.md

**Note**: This is a configuration/documentation project — no source code. All tasks produce markdown, YAML, or example files. Tests are not applicable (validation is done via `python3 scripts/validate.py` and manual operator verification).

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1–US4)

---

## Phase 1: Setup

**Purpose**: Create the `paperclip/` integration directory and shared structure.

- [x] T001 Create directory structure: `paperclip/`, `paperclip/examples/` at repo root
- [x] T002 [P] Create `paperclip/README.md` — top-level index with one-paragraph description of the integration, links to `QUICKSTART.md`, `skill-routing-table.yaml`, `skill-binding-schema.yaml`, and `examples/`; also defines the section outline for `QUICKSTART.md` (sections: Setup, Find a Skill, Configure an Agent, Routing via Labels, Activation Levels, Progressive Loading, [GATE] Handling, Troubleshooting) so parallel QUICKSTART tasks know where their content lands

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core schema and role-mapping reference that all user stories depend on.

**⚠️ CRITICAL**: US1–US4 all depend on the skill-binding schema and role mapping table.

- [x] T003 Create `paperclip/skill-binding-schema.yaml` — machine-readable YAML schema defining the SkillBinding and RoutingTable structure (based on `contracts/skill-binding-schema.md`); must include the optional `skill_version` field with an inline comment explaining: (a) omit for always-latest, (b) set to a git SHA for stable production configs (e.g., `skill_version: "a1b2c3d"`), (c) set to a semver tag if the operator tags releases — this covers FR-006 versioned binding requirement
- [x] T004 [P] Create `paperclip/role-mapping.md` — reference table mapping all 11 Paperclip roles to their best-fit Skill OS departments and agent slugs (from `data-model.md` AgentRoleMapping entity); verify all 16 Skill OS departments appear at least once across the 11 role rows so FR-010 (no gaps in coverage) is provably satisfied

**Checkpoint**: Schema + role mapping complete. US1–US4 can now proceed.

---

## Phase 3: User Story 1 — Attach a Skill OS skill to a Paperclip agent role (Priority: P1) 🎯 MVP

**Goal**: An operator can configure a Paperclip agent with a single Skill OS skill via `instructionsFilePath` and the agent produces output following the skill's workflow.

**Independent Test**: Configure the sample `pm` agent in `examples/single-agent.yaml` with `agents/product/product-manager/prd-author/SKILL.md` as `instructionsFilePath`. Dispatch a task labeled `prd`. Verify the agent output follows the 9-section workflow and references the asset template structure.

### Implementation for User Story 1

- [x] T005 [US1] Create `paperclip/examples/single-agent.yaml` — minimal single-agent config showing a `pm` agent with `prd-author` skill attached via `instructionsFilePath`, with `promptTemplate` that fetches heartbeat-context and follows the skill workflow
- [x] T006 [P] [US1] Create `paperclip/QUICKSTART.md` — operator quickstart (condensed from `specs/004-skill-os-paperclip-integration/quickstart.md`) covering: clone Skill OS, find a skill, set `instructionsFilePath`, handle `[GATE]` markers; includes the `promptTemplate` snippet for heartbeat-context fetching
- [x] T007 [P] [US1] Add `[GATE]` handling documentation to `paperclip/QUICKSTART.md` — how agents should create Paperclip approval requests when a `[GATE]` step is reached (POST to `/api/approvals`, set status to `blocked`)

**Checkpoint**: US1 complete. An operator can follow `QUICKSTART.md` to attach any Skill OS skill to any Paperclip agent.

---

## Phase 4: User Story 2 — Skill routing via issue labels (Priority: P2)

**Goal**: Operators can configure a routing table so the right Skill OS skill loads automatically based on the Paperclip issue label, without changing `instructionsFilePath` per task.

**Independent Test**: Review `skill-routing-table.yaml` against the binding schema. Verify all `skill_path` values resolve to real `SKILL.md` files. Verify all `role` values are valid Paperclip role enums. Verify all `label` values are kebab-case strings.

### Implementation for User Story 2

- [x] T008 [US2] Create `paperclip/skill-routing-table.yaml` — default routing table covering the top 40 most-used Skill OS skills, organized by Paperclip role, with one binding per common label (e.g., `pm:prd`, `pm:experiment`, `engineer:backend-api`, `engineer:threat-model`, `designer:usability-review`, `qa:test-plan`, etc.)
- [x] T009 [P] [US2] Add routing table usage section to `paperclip/QUICKSTART.md` — explains IssueLabel.name matching, how to create labels in Paperclip Settings, and v1 limitation (static per-agent `instructionsFilePath`; dynamic label routing is v2)
- [x] T009b [P] [US2] Add "Activation Levels" section to `paperclip/QUICKSTART.md` — documents all three FR-007 activation levels: (1) agent-wide (set `instructionsFilePath` in agent `adapterConfig` — applies to all tasks), (2) task-tag level (routing table `label` matching — applies per `IssueLabel`), (3) single-task override (temporarily set `adapterConfig.instructionsFilePath` on an individual agent run via the Paperclip UI or PATCH `/api/agents/{id}` before dispatching the task, reset after)
- [x] T010 [P] [US2] Create validation note in `paperclip/skill-routing-table.yaml` header — inline comment block explaining how to verify all `skill_path` values are valid (using `python3 scripts/validate.py` + `ls` check)

**Checkpoint**: US2 complete. Operators have a default routing table covering 40 common task types across all major Paperclip roles.

---

## Phase 5: User Story 3 — Skill OS as the org chart knowledge base (Priority: P2)

**Goal**: Paperclip operators can browse Skill OS by department to discover and select skills that match their org chart roles, replacing hand-written system prompts.

**Independent Test**: A new operator can open `paperclip/role-mapping.md`, find their Paperclip role (e.g., `engineer`), navigate to the suggested Skill OS agent (e.g., `sr-backend-developer`), browse available skills, and select one — all without reading the Skill OS README or CLAUDE.md.

### Implementation for User Story 3

- [x] T011 [US3] Create `paperclip/examples/engineering-team.yaml` — sample config for a 5-person engineering team: `cto` (tech-architect/system-design-author), `engineer` ×3 (sr-backend-developer/builder, security-engineer/threat-modelling, devops-infrastructure-engineer/ci-pipeline-builder), `qa` (qa-test-engineer/test-plan-author)
- [x] T012 [P] [US3] Create `paperclip/examples/full-company.yaml` — sample config for a 7-agent company: CEO (general), CTO (tech-architect), CMO (vp-marketing/gtm-planner-marketing), CFO (fpa-analyst/unit-economics-tracker), PM (product-manager/prd-author), Engineer (sr-backend-developer/builder), Designer (ux-ui-designer/wireframe-creator)
- [x] T013 [P] [US3] Update `paperclip/role-mapping.md` — add a "Which skill to start with" column recommending the single most-used skill per Paperclip role (the P1 skill for that role type)

**Checkpoint**: US3 complete. An operator setting up any Paperclip company can find the right Skill OS skill for each role within 5 minutes.

---

## Phase 6: User Story 4 — Progressive skill loading (Priority: P3)

**Goal**: Operators understand the token budget implications of Skill OS and know how to use progressive loading (base SKILL.md only, references on demand) to stay within budget.

**Independent Test**: The progressive loading section of `QUICKSTART.md` correctly describes the three-tier loading model (Tier 1: YAML frontmatter ~100 words, Tier 2: skill body ≤1,500 words, Tier 3: references on demand) and shows a concrete `promptTemplate` that instructs the agent to read reference files only at the relevant workflow step.

### Implementation for User Story 4

- [x] T014 [US4] Add progressive loading section to `paperclip/QUICKSTART.md` — explains three-tier model, per-skill word count guidance (simple ≤500, medium ≤1,000, complex ≤1,500), and recommended `budgetMonthlyCents` ranges for different agent types
- [x] T015 [P] [US4] Add model selection guidance to `paperclip/QUICKSTART.md` — when to use `claude-sonnet-4-6` (L1/L2 skills) vs `claude-opus-4-6` (L3/complex skills like `system-design-author`, `threat-modelling`, `contract-review-orchestrator`)
- [x] T016 [P] [US4] Add reference-file loading example to `paperclip/QUICKSTART.md` — concrete `promptTemplate` snippet showing agent instructed to `Read: path/to/references/scoring-rubric.md` only when reaching the assessment step, not upfront

**Checkpoint**: US4 complete. Operators can configure token-efficient agents that use full Skill OS depth without exceeding budget.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Final quality pass across all deliverables.

- [x] T017 [P] Verify all `skill_path` values in `paperclip/skill-routing-table.yaml` resolve to existing files: run `ls` on each path referenced in the routing table
- [x] T018 [P] Verify all `instructionsFilePath` values in `paperclip/examples/*.yaml` resolve to existing `SKILL.md` files
- [x] T019 Run `python3 scripts/validate.py` — confirm 0 errors across repo (no new SKILL.md files added, but confirm nothing broken)
- [x] T020 [P] Add `paperclip/` section to root `README.md` — one paragraph with a link to `paperclip/QUICKSTART.md` under a new "## Integrations" heading
- [x] T021 [P] Update `AGENTS.md` last-updated date if modified
- [x] T022 Commit all deliverables in separate logical-unit commits per constitution Principle V — one commit per file group: (1) `paperclip/` directory + `README.md`, (2) `skill-binding-schema.yaml` + `role-mapping.md`, (3) `skill-routing-table.yaml`, (4) `examples/single-agent.yaml`, (5) `examples/engineering-team.yaml` + `examples/full-company.yaml`, (6) `QUICKSTART.md`, (7) root `README.md` integrations section

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: No dependencies — start immediately
- **Phase 2 (Foundational)**: Depends on Phase 1 — BLOCKS Phase 3–6
- **Phases 3–6 (User Stories)**: All depend on Phase 2 completion; can proceed in priority order
- **Phase 7 (Polish)**: Depends on all desired user stories being complete

### User Story Dependencies

- **US1 (P1)**: Can start after Phase 2 — no dependencies on other stories
- **US2 (P2)**: Can start after Phase 2 — independent of US1; routing table references skills validated by US1's quickstart
- **US3 (P2)**: Can start after Phase 2 — independent of US1/US2; examples build on same schema
- **US4 (P3)**: Can start after US1 — adds to QUICKSTART.md sections established in US1

### Parallel Opportunities

- T003 and T004 (Phase 2) can run in parallel
- T006 and T007 (US1 quickstart sections) can run in parallel
- T009, T010 (US2 additions) can run in parallel after T008
- T011, T012, T013 (US3 examples) can run in parallel
- T014, T015, T016 (US4 additions) can run in parallel
- T017, T018, T020, T021 (Phase 7 checks) can all run in parallel

---

## Parallel Example: Phase 2

```bash
# Both foundational tasks can run simultaneously (different files):
Task A: "Create paperclip/skill-binding-schema.yaml"
Task B: "Create paperclip/role-mapping.md"
```

## Parallel Example: User Story 3

```bash
# All three example configs are independent files:
Task A: "Create paperclip/examples/engineering-team.yaml"
Task B: "Create paperclip/examples/full-company.yaml"
Task C: "Update paperclip/role-mapping.md — add 'which skill to start with' column"
```

---

## Implementation Strategy

### MVP (US1 Only — 4 tasks)

1. Phase 1: T001, T002 — create directory structure
2. Phase 2: T003, T004 — schema + role mapping
3. Phase 3: T005, T006, T007 — single-agent example + QUICKSTART.md
4. **Validate**: Follow QUICKSTART.md yourself with a real Paperclip instance

### Full Delivery

Complete all phases in order: Setup → Foundation → US1 → US2 → US3 → US4 → Polish.
Each user story adds a complete, independently usable layer of operator tooling.
