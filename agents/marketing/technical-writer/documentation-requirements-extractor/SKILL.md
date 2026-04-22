---
name: documentation-requirements-extractor
description: >
  This skill extracts documentation requirements from engineering specs and developer feedback.
  Use when asked to identify what needs documenting, translate specs into doc tasks, or triage documentation requests.
  Also consider when a new feature is in development and documentation planning should start early.
  Suggest when the user is about to start writing docs without a requirements analysis.
department: marketing
agent: technical-writer
version: 1.0.0
complexity: simple
related-skills:
  - documentation-writer
  - documentation-accuracy-auditor
  - developer-feedback-synthesiser
triggers:
  - "extract documentation requirements"
  - "gather docs requirements"
  - "define documentation scope"
  - "documentation needs analysis"
  - "docs requirements gathering"
---

# documentation-requirements-extractor

## Agent: Technical Writer

L3 technical writer reporting to Developer Relations Lead, responsible for API documentation, developer guides, and documentation accuracy.

Department ethos: [ideal-marketing.md](../../../../departments/marketing/ideal-marketing.md)

## Skill Description

Extracts documentation requirements from engineering specs and developer feedback to ensure all necessary content is identified before writing begins.

## When to Use

- When a new feature or API is in development and documentation planning needs to begin.
- When engineering specs have been finalized and need to be translated into documentation tasks.
- When developer feedback indicates documentation gaps that need systematic cataloguing.
- When prioritizing the documentation backlog for an upcoming sprint.

## Workflow

1. **Gather source materials**: Collect engineering specs, PRDs, API changelogs, developer feedback, and support ticket trends. Use the source analysis protocol in [framework.md](references/framework.md) to ensure all high-priority source types are covered. Deliverable: source materials inventory.
2. **Extract requirements**: Parse each source for documentation implications using the extraction focus questions from the source analysis table. Classify each requirement against the categorization taxonomy (New Content, Update, Migration Guide, Code Sample, etc.). Deliverable: raw requirements list with source attribution and category.
3. **Categorize and prioritize**: Score each requirement on Developer Impact (1–5) and Release Urgency (1–5) using the priority scoring model in the framework. Assign P1–P4 priority tiers. Deliverable: prioritized requirements backlog.
4. **Create documentation tasks**: Convert each requirement into an actionable task using the documentation task template from the framework. All fields (scope, owner, deadline, acceptance criteria, dependencies) must be complete before assignment. Deliverable: task list ready for assignment.

## Anti-Patterns

- **Waiting for code freeze**: Delaying requirements extraction until engineering is complete. *Why*: Late extraction compresses writing timelines and forces documentation to ship after the feature, leaving developers without guidance during the critical adoption window.
- **Spec-only extraction**: Extracting requirements only from engineering specs without consulting developer feedback. *Why*: Specs describe what was built, not what developers struggle with; feedback reveals the documentation gaps that specs cannot predict.

## Output

**On success**: Produces a prioritized documentation requirements backlog with tasks ready for assignment. Delivered to the technical writing team lead.

**On failure**: Report which source materials were unavailable, what coverage gaps remain, and recommend follow-up extraction. Every error must be actionable.

## Related Skills

- [`documentation-writer`](../documentation-writer/SKILL.md) — Writers consume the requirements extracted here as their task input.
- [`documentation-accuracy-auditor`](../documentation-accuracy-auditor/SKILL.md) — Accuracy audit findings generate additional documentation requirements.
- [`developer-feedback-synthesiser`](../../../marketing/developer-relations-lead/developer-feedback-synthesiser/SKILL.md) — Synthesised feedback is a key input to documentation requirements extraction.
