<!--
SYNC IMPACT REPORT
==================
Version change: 1.0.0 → 2.0.0 (MAJOR — principles redefined for enriched skill format)

Modified principles:
- I. Template Fidelity: 3-section flat format → 9-section enriched format with YAML frontmatter
- IV. Canonical Naming: flat files (<skill>.md) → skill subdirectories (<skill>/SKILL.md)
- V. Atomic Commits: single-file → logical-unit commits

Added sections:
- Principle VI. Progressive Disclosure (three-tier loading with word limits)
- Principle VII. Department Ethos (ideal-<dept>.md profiles)
- Updated Structural Conventions for subdirectories and departments/

Removed sections: None (all principles preserved, some redefined)

Templates reviewed:
- .specify/templates/plan-template.md ✅ Constitution Check section is generic — no update required
- .specify/templates/spec-template.md ✅ No constitutional references — no update required
- .specify/templates/tasks-template.md ✅ Tests are already marked OPTIONAL — no update required
- .specify/templates/constitution-template.md ✅ Source template — no change needed

Follow-up TODOs: None
-->

# skill-os Constitution

## Core Principles

### I. Template Fidelity

Every skill file MUST live at `agents/<agent-slug>/<skill-slug>/SKILL.md` and include
these sections in order: YAML frontmatter, title (`# <skill-slug>`), Agent header
(with department ethos reference), Skill Description (third-person declarative, one
sentence), When to Use (trigger scenarios), Workflow (imperative numbered steps with
deliverables), Anti-Patterns (with rationale explaining why each is harmful), Output
(success artifacts AND failure reporting), and Related Skills.

The YAML frontmatter MUST include: `name`, `description`, `department`, `agent`,
`version`, `complexity`, and `related-skills`.

The Workflow section MUST be written in imperative voice. The Anti-Patterns section
MUST explain the *why* behind each prohibition. The Output section MUST define both
success and failure behavior.

Unenriched skills (version `0.1.0`) retain the legacy 3-section format during
migration and are considered valid but incomplete.

**Rationale**: Enriched skills are executable by AI agents — the frontmatter triggers
activation, the body provides instructions, and bundled resources supply depth. Every
section serves a specific function in the agent execution loop.

### II. Single Responsibility

Each skill file MUST describe exactly one discrete responsibility. A skill that covers
two distinct capabilities MUST be split into two separate files. The skill description
MUST be expressible as a single declarative sentence; if a conjunction ("and") is
required, that is a signal the skill should be divided.

**Rationale**: Granular, non-overlapping skills are the primary value the repo
provides. Compound skills dilute role clarity and make org chart metrics unreliable.

### III. Org Chart Consistency

The org chart at `AGENTS.md` MUST be kept in strict sync with the
filesystem at all times:

- Every agent directory under `agents/` MUST appear in the org chart.
- Every skill subdirectory MUST be listed under its agent's skills list.
- Skill counts per agent and total metrics in the summary table MUST be accurate.

Violations constitute a broken state. Any commit that adds or removes skills MUST
include a corresponding org chart update in a separate, immediately following commit.

**Rationale**: The org chart is the canonical reference document. Drift between files
and the chart makes the repo untrustworthy as a source of truth.

### IV. Canonical Naming

- Agent directories MUST use kebab-case (e.g., `vendor-risk-assessor`).
- Skill subdirectories MUST use kebab-case matching the skill name exactly
  (e.g., `contract-review/SKILL.md`).
- The `name` field in YAML frontmatter MUST match the skill subdirectory name.
- The `# <skill-slug>` heading MUST match the `name` field.
- Department directories under `departments/` MUST use kebab-case.

No PascalCase, snake_case, or mixed-case names are permitted anywhere in the
`agents/` or `departments/` trees.

**Rationale**: Consistent naming makes directory traversal, grepping, and linking
unambiguous without requiring lookup tables.

### V. Atomic Commits

Changes MUST be committed as atomic logical units. The correct sequence when adding a
new skill is:

1. Commit the skill subdirectory (`agents/<agent>/<skill>/SKILL.md` and any
   supporting context files)
2. Commit the org chart update (`AGENTS.md`)

A logical unit is one skill migration, one ethos profile, or one supporting context
addition. Bundling multiple skills or mixing skills with org chart changes in a single
commit is not permitted.

**Rationale**: Logical-unit commits produce a clean, reviewable history where each
change is attributable and revertable without collateral side-effects. Subdirectory
creation and file moves within the same skill are a single logical unit.

### VI. Progressive Disclosure

Skill files MUST follow a three-tier loading model with strict size limits:

- **Tier 1 — Metadata** (~100 words): YAML frontmatter. Always in AI agent context.
- **Tier 2 — Skill body** (by complexity class):
  - Simple: max 500 words
  - Medium: max 1,000 words
  - Complex: max 1,500 words
- **Tier 3 — Bundled resources** (unlimited): `references/`, `examples/`, `scripts/`,
  `assets/` loaded on demand.

Content exceeding the Tier 2 limit MUST be moved to `references/` files with clear
pointers from the body. Individual reference files over 300 lines MUST include a
table of contents.

**Rationale**: Not every consumer runs large models. Skill bodies must fit comfortably
in smaller context windows. Combined with the department ethos profile (max 500 words),
total context per invocation stays within 1,000–2,000 words.

### VII. Department Ethos

Each of the 15 departments MUST have an `ideal-<department>.md` file at
`departments/<department>/ideal-<department>.md` defining the mindset, priorities,
and quality standards of an ideal practitioner. Max 500 words.

Every skill file MUST reference its department's ethos profile in the Agent header
section.

Ethos profiles MUST be opinionated and specific — actionable principles that
distinguish excellent practitioners from average ones, not generic platitudes.

**Rationale**: Skills tell agents what to do. Ethos profiles tell agents who to be.
Without them, skills produce technically correct but soulless output. With them,
agents embody the judgment and values that make work excellent.

### VIII. Tool Policy

A structured `allowed-tools.yaml` file at the repo root defines which tools are
available to agents at four levels: company-wide, department, agent, and skill.
Each agent directory's Agent header MUST include a tool policy reference:
`Tool policy: [allowed-tools.yaml](../../allowed-tools.yaml)`.

The file MUST include a `schema_version` field. Credentials MUST be stored in
the consuming AI platform's native secret store — never in the repo.

**Rationale**: Connecting tools without access control is a security risk. The
policy file is the guardrail that makes tool connectivity safe at scale.

### IX. Optional Frontmatter Extensions

Skill frontmatter MAY include optional fields beyond the 7 required fields:

- `triggers`: A list of short phrases (2-10 words) for machine-optimized skill
  activation. Complements the pushy `description` field.

Additional optional fields are permitted but not validated — this allows future
extensibility without breaking existing skills.

**Rationale**: Triggers improve activation accuracy. Optional fields enable
platform-specific enhancements without imposing them on all consumers.

### X. Checkpoint Gates

Complex skill workflows MAY include `[GATE]` markers on steps that require human
approval before the agent proceeds. Format: `[GATE]` appended to the workflow
step text. The validation script SHOULD warn when `[GATE]` appears in a
simple-complexity skill.

**Rationale**: Prevents autonomous execution of high-stakes decisions — deploys,
legal filings, budget approvals, security exceptions. Gates are advisory;
enforcement depends on the agent runtime.

## Structural Conventions

- Each skill MUST live in its own subdirectory: `agents/<agent>/<skill>/SKILL.md`.
- Skill subdirectories MAY contain `references/`, `examples/`, `scripts/`, `assets/`,
  and `evals/` directories for supporting context.
- Agent directories MAY contain agent-level `references/`, `examples/`, `scripts/`,
  and `assets/` directories for resources shared across all the agent's skills.
- Department directories at `departments/<dept>/` MUST contain the ethos profile and
  MAY contain `references/`, `examples/`, `scripts/`, and `assets/` directories.
- A global `_shared/` directory at repo root holds cross-cutting resources.
- Context lookup follows: skill → agent → department → `_shared/`. Most specific wins.
- The `agents/` directory holds skill content. The `departments/` directory holds
  ethos profiles and department-wide context. The `_shared/` directory holds
  cross-cutting resources. No skill-like content belongs in the repo root or `docs/`.
- Agent descriptions in skill files MUST accurately reflect the current org chart
  definition. If an agent's definition changes, all skill files for that agent MUST
  be updated in the same change batch.
- The summary table at the top of `AGENTS.md` MUST include:
  total roles, total skills, department count, and last-updated date.

## Amendment Procedure

To propose a change to this constitution:

1. Draft the amendment as a concrete diff against this file.
2. Identify which principles change in semantics — MUST vs. SHOULD distinctions
   count as semantic changes.
3. Apply semantic versioning:
   - **MAJOR**: A principle is removed, redefined, or its normative language is
     weakened (e.g., MUST → SHOULD).
   - **MINOR**: A new principle or section is added, or normative language is
     strengthened.
   - **PATCH**: Wording clarifications, formatting fixes, non-semantic rewording.
4. Update `LAST_AMENDED_DATE` to the date of the change.
5. Commit the updated constitution as a single-file commit with message:
   `docs: amend constitution to vX.Y.Z (<summary>)`

## Governance

This constitution supersedes CLAUDE.md on any matter of org structure, skill file
format, naming, or commit discipline. CLAUDE.md continues to govern tooling choices,
workflow shortcuts, and project-startup checklists.

All speckit plan and task generation commands MUST verify compliance with Principles
I–X before proceeding. Any detected violation MUST be reported in the Constitution
Check section of the relevant plan.md before the plan advances.

Complexity or deviation from these principles MUST be justified explicitly in a
Complexity Tracking table in the relevant plan.md — not in commit messages or
conversation.

**Version**: 2.1.0 | **Ratified**: 2026-03-26 | **Last Amended**: 2026-03-27
