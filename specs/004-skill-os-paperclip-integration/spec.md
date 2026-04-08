# Feature Specification: Skill OS × Paperclip Integration

**Feature Branch**: `004-skill-os-paperclip-integration`
**Created**: 2026-04-08
**Status**: Draft
**Input**: Learn from https://github.com/paperclipai/paperclip and think about how we can use the skills we have created for it.

---

## Background

Paperclip is an open-source orchestration platform for running AI agent companies. It provides an org chart, task queue, goal hierarchy, budget controls, and governance layer on top of AI agents. Each agent in Paperclip operates in a named role (CEO, CTO, engineer, marketer), receives tasks on a heartbeat schedule, and checks out work atomically.

Skill OS has 528 skills across 80 agent roles and 16 departments — each with executable workflows, scoring rubrics, output templates, and anti-patterns. These skills tell agents *how the best practitioners actually do their job*, not just what their role is called.

The integration opportunity: Paperclip gives agents a role title and a task. Skill OS gives those agents the domain expertise to execute that task the way the best human in that role would.

---

## User Scenarios & Testing *(mandatory)*

### User Story 1 — Attach a Skill OS skill to a Paperclip agent role (Priority: P1)

A Paperclip operator configures their AI company and wants the `account-executive` agent to use the `meeting-prep-builder` skill when it receives a meeting preparation task. They attach the skill's `SKILL.md` content to the agent's system prompt or context, so the agent executes the structured workflow rather than improvising.

**Why this priority**: This is the core value — grounding a Paperclip agent in domain expertise from Skill OS. All other stories build on this.

**Independent Test**: Configure a single Paperclip agent with one Skill OS skill and verify the agent's output follows the skill's workflow and produces the expected artifact.

**Acceptance Scenarios**:

1. **Given** a Paperclip agent assigned the `account-executive` role, **When** a meeting preparation task is dispatched, **Then** the agent produces a meeting brief that matches the structure defined in `assets/meeting-brief-template.md`
2. **Given** a skill is attached to an agent, **When** the agent encounters an anti-pattern scenario, **Then** the agent avoids it and explains why per the anti-patterns section
3. **Given** a Skill OS skill with a `[GATE]` marker, **When** the agent reaches that step, **Then** the agent pauses and requests human approval before proceeding

---

### User Story 2 — Skill routing: Paperclip dispatches the right skill for each task type (Priority: P2)

A Paperclip operator wants the platform to automatically select the appropriate Skill OS skill based on the task type being dispatched to an agent. For example, when a `product-manager` agent receives a task tagged `prd`, it automatically loads the `prd-author` skill. When it receives a task tagged `experiment`, it loads `experiment-designer`.

**Why this priority**: Manual skill attachment per task is feasible but slow. Automatic routing unlocks the full 528-skill library without operator overhead.

**Independent Test**: Create a routing table mapping task tags to skill paths and verify that tasks arrive in agent context pre-loaded with the correct skill.

**Acceptance Scenarios**:

1. **Given** a task tagged `prd` assigned to a `product-manager` agent, **When** the agent receives the heartbeat, **Then** the `prd-author` skill is present in the agent's context
2. **Given** a task with no matching skill tag, **When** dispatched, **Then** the agent proceeds without a skill (graceful fallback, no error)
3. **Given** a routing table, **When** a new skill is added to Skill OS, **Then** an operator can add it to the routing table without modifying agent code

---

### User Story 3 — Skill OS as the agent knowledge base for Paperclip's org chart (Priority: P2)

When a Paperclip operator defines their org chart, the Skill OS directory is the canonical source of what each role can do. The operator browses 528 skills across 80 roles, organized by department, and selects which capabilities to activate per agent — replacing manually written system prompts with structured, validated skill definitions.

**Why this priority**: High leverage — replaces the most time-consuming part of setting up a Paperclip company (writing per-agent instructions) with a curated library.

**Independent Test**: Replace a handwritten system prompt with Skill OS `SKILL.md` content and compare agent output quality across 5 tasks.

**Acceptance Scenarios**:

1. **Given** Skill OS skill files, **When** a Paperclip operator browses the `agents/` directory by department, **Then** they can identify and select skills matching their org chart roles
2. **Given** a selected skill, **When** the operator configures an agent, **Then** the skill's `when-to-use` triggers map to Paperclip task tag conditions
3. **Given** a department (e.g., `engineering/`), **When** an operator sets up their engineering agents, **Then** all 100 engineering skills are available for assignment

---

### User Story 4 — Progressive skill loading within Paperclip token budgets (Priority: P3)

A Paperclip agent operates with a token budget. Rather than loading the full skill (SKILL.md + references + assets) into every heartbeat context, the agent first receives only `SKILL.md` (≤1,500 words). When executing a step that requires a scoring rubric or output template, it fetches the relevant file on demand.

**Why this priority**: Token budget is a first-class constraint in Paperclip. Progressive loading respects that constraint while preserving full skill depth.

**Independent Test**: Measure token usage with full vs. progressive loading and verify output quality is equivalent.

**Acceptance Scenarios**:

1. **Given** an agent with a token budget, **When** executing a complex skill, **Then** the base `SKILL.md` consumes ≤1,500 words and reference files are fetched only when that step is reached
2. **Given** an agent requesting an asset template, **When** the file is fetched, **Then** the agent fills in the template with task-specific content and returns it as the task output
3. **Given** a skill with no matching reference for a step, **When** the agent reaches that step, **Then** it proceeds using the workflow guidance in `SKILL.md` without erroring

---

### Edge Cases

- What happens when a task requires expertise spanning multiple skills (e.g., a product launch needs both `launch-plan-owner` and `sales-enablement-content-creator`)? → Multi-skill composition is out of scope for v1; operators select a primary skill per task type
- How does an agent handle a task where no Skill OS skill exists for the role? → Falls back to the department ethos profile from `departments/<dept>/ideal-<dept>.md`
- What if token budget is exhausted mid-skill execution? → Agent checkpoints progress and resumes on the next heartbeat with remaining steps
- What if a skill is updated in Skill OS while agents are mid-task? → Skill bindings are version-locked; updates apply only on explicit operator upgrade

---

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: A Paperclip agent MUST be able to receive a Skill OS `SKILL.md` file as part of its context on task dispatch
- **FR-002**: A skill routing table MUST map Paperclip task tags to Skill OS skill slugs and file paths
- **FR-003**: Agents MUST produce outputs that conform to the structure defined in the matched skill's `assets/` template
- **FR-004**: The integration MUST respect Paperclip's token budget constraints — base skill body ≤1,500 words; reference files loaded on demand
- **FR-005**: Skills with `[GATE]` markers MUST trigger a Paperclip human-approval request before the agent proceeds past that step
- **FR-006**: Skill-to-agent mappings MUST be versioned — agents on an older skill version continue working until explicitly upgraded by the operator
- **FR-007**: Operators MUST be able to activate skills at three levels: agent-wide (all tasks), task-tag level (tasks matching a tag), or single-task override
- **FR-008**: Department ethos profiles (`departments/<dept>/ideal-<dept>.md`) MUST serve as fallback agent context when no skill is matched
- **FR-009**: The Skill OS validation script (`python3 scripts/validate.py`) MUST pass before any skill version is deployed to a Paperclip instance
- **FR-010**: The integration MUST support all 16 Skill OS departments and their 80 agent roles without custom code per role

### Key Entities

- **Skill**: A `SKILL.md` file with YAML frontmatter and 9 sections, with optional `references/` and `assets/` subdirectories
- **Skill Binding**: A versioned mapping between a Paperclip agent role + task tag and a Skill OS skill slug
- **Routing Table**: A configuration document mapping task tags to skill paths, maintained by the operator
- **Agent Role**: A Paperclip agent configured with a named role corresponding to a Skill OS agent directory
- **Ethos Profile**: A department-level `ideal-<dept>.md` file used as fallback context when no skill binding matches

---

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Skill-grounded agent outputs score ≥30% higher on domain rubrics compared to ungrounded agents executing equivalent tasks
- **SC-002**: An operator can configure a 10-agent Paperclip company with Skill OS skill bindings in under 30 minutes
- **SC-003**: Progressive skill loading reduces average tokens consumed per task by ≥40% compared to loading the full skill tree upfront
- **SC-004**: All 80 Paperclip agent roles can be mapped to at least one Skill OS skill without gaps
- **SC-005**: Skill-grounded agents produce outputs matching the expected asset template structure in ≥90% of task executions
- **SC-006**: 100% of tasks with `[GATE]` markers pause for human approval; zero gates are skipped autonomously

---

## Assumptions

- Paperclip agents use Claude Code, Codex, or an HTTP adapter — all capable of processing markdown skill files in their context
- Skill OS skills are consumed as static markdown files; no runtime API or server is required
- The Paperclip task tagging system supports arbitrary string tags matchable against a routing table
- Operators can edit a YAML or JSON configuration file to define skill bindings
- Token budgets in Paperclip are configurable per agent and sufficient to accommodate a base skill (≤1,500 words) plus one reference file per heartbeat
- The `SKILL.md` format (YAML frontmatter + 9 sections) is stable — no breaking changes during integration development
- Multi-skill composition (a single task using multiple skills) is out of scope for v1; one primary skill per task type is the initial model
