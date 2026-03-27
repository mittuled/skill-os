# Tasks: Skill Quality Improvements

**Input**: Design documents from `/specs/002-skill-quality-improvements/`
**Prerequisites**: plan.md (required), spec.md (required), data-model.md, contracts/, quickstart.md

**Commit discipline**: Each skill, script, or schema update = 1 commit.

---

## Phase 1: Setup & Foundational

**Purpose**: Validation script updates and schema artifacts that all user stories depend on.

- [x] T001 Update `scripts/validate.py` to accept optional `triggers` frontmatter field (list of strings). Validation: each item is a non-empty string, 5-50 chars. No error if field absent. 1 commit.
- [x] T002 Update `scripts/validate.py` to accept `[GATE]` markers in workflow steps as valid syntax. Add warning (not error) when `[GATE]` appears in a skill with `complexity: simple`. 1 commit.
- [x] T003 Update `scripts/validate.py` to validate `allowed-tools.yaml` at repo root: check YAML syntax, `schema_version` field present and supported, department keys match `departments/` dirs, agent keys match `agents/` dirs. 1 commit.
- [x] T004 Create `allowed-tools.yaml` at repo root with `schema_version: 1` and empty `company-wide: []` placeholder. 1 commit.
- [x] T005 Update enrichment template at `specs/001-enrich-skill-directory/contracts/skill-template.md` — add `triggers` as optional frontmatter field, add `[GATE]` guidance in Workflow section comments, add `Tool policy` reference in Agent header. 1 commit.
- [x] T006 Update `specs/001-enrich-skill-directory/quickstart.md` — add sections for triggers, gates, rubrics, code examples, and tool policy reference. 1 commit.

**Checkpoint**: Validation script handles all new elements. Templates updated. Phase 2+ can begin.

---

## Phase 2: US1 — Company Tooling Onboarder

**Goal**: Create the onboarding skill that discovers, authenticates, and connects org tools.

**Independent Test**: Run in a test environment with 3 tools (GitHub, Slack, mock CRM). Verify discovery, authentication, and agent access.

- [x] T007 [US1] Create `agents/agent-configuration-manager/company-tooling-onboarder/` directory structure (SKILL.md, scripts/, references/). 1 commit.
- [x] T008 [US1] Write `agents/agent-configuration-manager/company-tooling-onboarder/SKILL.md` — enriched 9-section format (complexity: complex). 1 commit.
- [x] T009 [US1] Write `agents/agent-configuration-manager/company-tooling-onboarder/references/tool-categories.md`. 1 commit.
- [x] T010 [US1] Write `agents/agent-configuration-manager/company-tooling-onboarder/scripts/discover-tools.py`. 1 commit.
- [x] T011 [US1] Write `agents/agent-configuration-manager/company-tooling-onboarder/scripts/connect-mcp.py`. 1 commit.
- [x] T012 [US1] Write `agents/agent-configuration-manager/company-tooling-onboarder/scripts/configure-secrets.py`. 1 commit.
- [x] T013 [US1] Update `restructured-org-chart-v3.md` — add `company-tooling-onboarder` to Agent Configuration Manager's skill list. 1 commit.

---

## Phase 3: US2 — Tool Policy Manager

**Goal**: Create the skill that manages `allowed-tools.yaml` as an ongoing governance function.

**Independent Test**: Add/remove/modify tool permissions via the skill. Verify allowed-tools.yaml updates correctly and validation passes.

- [x] T014 [US2] Create `agents/agent-configuration-manager/tool-policy-manager/` directory structure. 1 commit.
- [x] T015 [US2] Write `agents/agent-configuration-manager/tool-policy-manager/SKILL.md`. 1 commit.
- [x] T016 [US2] Write `agents/agent-configuration-manager/tool-policy-manager/scripts/validate-policy.py`. 1 commit.
- [x] T017 [US2] Write `agents/agent-configuration-manager/tool-policy-manager/assets/allowed-tools-template.yaml`. 1 commit.
- [ ] T018 [US2] Add tool policy reference to all agent directories — add `Tool policy: [allowed-tools.yaml](../../allowed-tools.yaml)` line to the Agent header section of one representative skill per agent (80 agents). This is a batch update, not per-skill. 1 commit.
- [x] T019 [US2] Update `restructured-org-chart-v3.md` — add `tool-policy-manager` to Agent Configuration Manager's skill list. 1 commit.

---

## Phase 4: US3 — MCP Server Builder

**Goal**: Create the skill that generates MCP server wrappers from API documentation.

**Independent Test**: Point at a tool with an OpenAPI spec. Verify it scaffolds a working MCP server.

- [x] T020 [US3] Create `agents/skill-builder/mcp-server-builder/` directory structure. 1 commit.
- [x] T021 [US3] Write `agents/skill-builder/mcp-server-builder/SKILL.md`. 1 commit.
- [x] T022 [US3] Write `agents/skill-builder/mcp-server-builder/scripts/parse-openapi.py`. 1 commit.
- [x] T023 [US3] Write `agents/skill-builder/mcp-server-builder/scripts/scaffold-mcp.py`. 1 commit.
- [x] T024 [US3] Write `agents/skill-builder/mcp-server-builder/references/mcp-protocol.md`. 1 commit.
- [x] T025 [US3] Update `restructured-org-chart-v3.md` — add `mcp-server-builder` to Skill Builder's skill list. 1 commit.

---

## Phase 5: US4 — Tool Health Checker

**Goal**: Create the skill that verifies tool connectivity, credentials, and MCP responsiveness.

**Independent Test**: Connect 3 tools, revoke one token. Verify health report catches the failure.

- [x] T026 [US4] Create `agents/agent-operations-manager/tool-health-checker/` directory structure. 1 commit.
- [x] T027 [US4] Write `agents/agent-operations-manager/tool-health-checker/SKILL.md`. 1 commit.
- [x] T028 [US4] Write `agents/agent-operations-manager/tool-health-checker/scripts/check-health.py`. 1 commit.
- [x] T029 [US4] Write `agents/agent-operations-manager/tool-health-checker/assets/health-report-template.md`. 1 commit.
- [x] T030 [US4] Update `restructured-org-chart-v3.md` — add `tool-health-checker` to Agent Operations Manager's skill list. 1 commit.

---

## Phase 6: US5 — Add Triggers to Skills

**Goal**: Add `triggers` frontmatter to the 50 most commonly activated skills.

**Independent Test**: Verify 5 skills with triggers activate more reliably in Claude Code.

- [x] T031 [US5] Identify the top 50 skills by cross-reference count and domain importance. Done.
- [x] T032 [US5] Add `triggers` to 10 Product skills. Done.
- [x] T033 [US5] Add `triggers` to 10 Engineering skills. Done.
- [x] T034 [US5] Add `triggers` to 10 Marketing skills. Done.
- [x] T035 [US5] Add `triggers` to 10 Sales + Legal skills. Done.
- [x] T036 [US5] Add `triggers` to 10 remaining department skills. Done.

---

## Phase 7: US6 — Add Checkpoint Gates

**Goal**: Add `[GATE]` markers to 20 complex skills with high-stakes workflow steps.

**Independent Test**: Verify `[GATE]` markers are visible in workflow and validation script accepts them.

- [x] T037 [US6] Identify 20 complex skills with high-stakes steps. Done.
- [x] T038 [US6] Add `[GATE]` markers to 10 skills (Engineering + Legal). Done.
- [x] T039 [US6] Add `[GATE]` markers to 10 skills (Product + Finance + Sales). Done.

---

## Phase 8: US7 — Add Scoring Rubrics

**Goal**: Create scoring rubrics for 10 assessment-type skills.

**Independent Test**: Run an assessment skill against two subjects. Verify identical rubric produces comparable numeric scores.

- [x] T040 [US7] Identify 10 assessment skills. Done.
- [x] T041 [US7] Create `references/scoring-rubric.md` for 10 skills + update Workflows. Done.

---

## Phase 9: US8 — Add Code Examples

**Goal**: Add working code examples to 20 engineering skills.

**Independent Test**: Verify an agent executing an engineering skill references the examples and produces correct output.

- [x] T042 [US8] Identify 20 engineering skills. Done.
- [x] T043 [US8] Create `examples/` for 10 DevOps + Platform skills. Done.
- [x] T044 [US8] Create `examples/` for 10 Frontend + Backend + Security + Data skills. Done.

---

## Phase 10: US9 — Quality Fixes

**Goal**: Rewrite Engineering skills scoring <5/5 and Legal skills missing anti-pattern rationale.

**Independent Test**: Re-score rewritten skills — both departments should score 5.0.

- [ ] T045 [US9] Identify all Engineering skills scoring below 5/5 in the quality assessment. Run validation to find skills missing frontmatter or with generalist content. Save list. 1 commit.
- [ ] T046 [US9] Rewrite identified Engineering skills with domain-specific patterns and terminology. 1 commit per skill.
- [ ] T047 [US9] Identify all Legal skills with anti-patterns missing *Why* rationale. 1 commit.
- [ ] T048 [US9] Update identified Legal skills — add *Why* rationale to every anti-pattern. 1 commit per skill.

---

## Phase 11: Polish & Finalize

**Purpose**: Constitution amendment, full validation, status update.

- [x] T049 Amend constitution to v2.1.0 — document `triggers`, `[GATE]`, `allowed-tools.yaml`, tool policy. Done.
- [x] T050 Update frontmatter schema at `specs/001-enrich-skill-directory/contracts/frontmatter-schema.yaml` — add `triggers` as optional field. 1 commit.
- [x] T051 Run full repo validation: `python3 scripts/validate.py` — confirm 0 errors across all 499+ skills. Fix any errors. 1 commit per fix.
- [x] T052 Update `status.md` — reflect 4 new skills, tool policy, triggers/gates/rubrics/examples counts. 1 commit.
- [x] T053 Update `CLAUDE.md` — add tool policy reference, triggers guidance, gate guidance. 1 commit.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: No dependencies — start immediately
- **Phase 2 (Onboarder)**: Depends on Phase 1 (needs allowed-tools.yaml + validation)
- **Phase 3 (Policy Manager)**: Depends on Phase 2 (manages what onboarder creates)
- **Phase 4 (MCP Builder)**: Depends on Phase 1 only (called by onboarder but independently testable)
- **Phase 5 (Health Checker)**: Depends on Phase 2 (reads allowed-tools.yaml)
- **Phase 6-9 (Enhancements)**: Depend on Phase 1 only (validation script must support new elements)
- **Phase 10 (Quality Fixes)**: Independent of tooling phases
- **Phase 11 (Finalize)**: Depends on ALL previous phases

### Parallel Opportunities

- Phases 4 + 5 can run in parallel (different agents, different skills)
- Phases 6 + 7 + 8 + 9 + 10 can ALL run in parallel (different files, no dependencies)
- Within Phase 6: T032-T036 can run in parallel (different departments)

---

## Implementation Strategy

### MVP First (Phases 1-2)

1. Phase 1: Setup (validation + schema)
2. Phase 2: Company Tooling Onboarder
3. **STOP and VALIDATE**: Test onboarding with 3 tools

### Incremental Delivery

1. Phase 1 → Foundation ready
2. Phase 2 → Onboarder works (MVP!)
3. Phase 3 → Policy management
4. Phase 4 + 5 → MCP builder + health checker (parallel)
5. Phase 6-10 → All enhancements (parallel)
6. Phase 11 → Polish, constitution, finalize

---

## Task Count

| Phase | Tasks | Description |
|-------|-------|-------------|
| 1 | 6 | Setup & foundational |
| 2 | 7 | US1: Onboarder |
| 3 | 6 | US2: Policy manager |
| 4 | 6 | US3: MCP builder |
| 5 | 5 | US4: Health checker |
| 6 | 6 | US5: Triggers (~50 skills) |
| 7 | 3 | US6: Gates (~20 skills) |
| 8 | 2 | US7: Rubrics (~10 skills) |
| 9 | 3 | US8: Code examples (~20 skills) |
| 10 | 4 | US9: Quality fixes |
| 11 | 5 | Polish & finalize |
| **Total** | **53** | |

Note: Phases 6-9 involve batch updates (1 commit per skill within each batch task), so the actual commit count is ~53 tasks + ~110 individual skill commits = ~163 total commits.
