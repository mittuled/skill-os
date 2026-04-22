---
name: jtbd-mapper
description: >
  This skill maps jobs-to-be-done from research data to build a structured understanding of
  user motivations. Use when asked to create a JTBD framework, map user motivations, or
  structure research findings into job statements. Also consider when the team has research
  data but no systematic model of what users are trying to accomplish. Suggest when the
  user is about to prioritise features without understanding underlying user jobs.
department: design
agent: ux-research-lead
version: 1.0.0
complexity: medium
related-skills:
  - customer-discovery-planner-uxr
  - jtbd-to-stories-uxr
  - user-feedback-synthesiser
triggers:
  - "map jobs to be done"
  - "jtbd mapping"
  - "jobs to be done"
  - "map user jobs"
  - "jtbd analysis"
---

# jtbd-mapper

## Agent: UX Research Lead

L2 UX research lead (1x) (moved from Product, now reports to Head of Design) responsible for planning and leading user research to directly inform design decisions.

Department ethos: [ideal-design.md](../../../../departments/design/ideal-design.md)

## Skill Description

Maps jobs-to-be-done from research data to build a structured understanding of user motivations, desired outcomes, and the circumstances that trigger action.

## When to Use

- When customer discovery or user research sessions have been completed and raw findings need to be structured into a jobs-to-be-done framework.
- When the product team needs a shared vocabulary for discussing user needs that goes beyond feature requests to underlying motivations.
- When prioritisation discussions are stuck on competing feature ideas and reframing around user jobs can break the deadlock.

## Workflow

1. **Data Consolidation**: Gather all research inputs (interview transcripts, session notes, survey responses, support tickets) into a single repository for analysis. Deliverable: consolidated research data set.
2. **Job Statement Extraction**: Analyse the data to identify discrete jobs users are trying to accomplish. Write each as a job statement in the format: "When [situation], I want to [motivation], so I can [expected outcome]." Deliverable: raw job statement list.
3. **Job Hierarchy Construction**: Organise job statements into a hierarchy: core functional jobs, related emotional jobs, and social jobs. Group sub-jobs under parent jobs where appropriate. Deliverable: JTBD hierarchy map.
4. **Outcome Mapping**: For each core job, identify the desired outcomes users use to measure success and the pain points that indicate failure. Deliverable: job-outcome matrix.
5. **Circumstance Documentation**: Document the specific circumstances (triggers, constraints, context) under which each job becomes active. Deliverable: circumstance annotations on the JTBD map.
6. **Validation & Prioritisation**: Review the JTBD map with stakeholders, validate against quantitative data where available, and prioritise jobs by frequency, intensity, and current underservedness. Deliverable: prioritised JTBD framework.

## Anti-Patterns

- **Feature-as-job confusion**: Writing job statements that describe product features ("I want to filter by date") rather than underlying motivations ("I want to find the most recent relevant item quickly"). *Why*: feature-level jobs lock thinking into current solutions and prevent discovering better approaches.
- **Ignoring emotional and social jobs**: Focusing only on functional jobs and omitting the emotional ("I want to feel confident I chose correctly") and social ("I want my team to see me as organised") dimensions. *Why*: emotional and social jobs often drive adoption, retention, and willingness to pay more than functional ones.
- **Single-source mapping**: Building the JTBD framework from one research method or one user segment. *Why*: jobs derived from a single source reflect that source's biases; triangulation across methods and segments produces more robust frameworks.
- **Static framework**: Treating the JTBD map as a one-time deliverable that never gets updated. *Why*: user jobs evolve as markets, technology, and user expectations shift; an outdated framework misdirects product investment.

## Output

**On success**: Produces a prioritised JTBD framework containing job statements (functional, emotional, social), job hierarchy, outcome matrix, and circumstance documentation. Delivered as a structured document or visual map accessible to product, design, and engineering teams.

**On failure**: Report which jobs could not be clearly articulated (e.g., insufficient data for a segment), what additional research is needed, and recommend targeted follow-up studies to fill gaps.

## Related Skills

- [`customer-discovery-planner-uxr`](../customer-discovery-planner-uxr/SKILL.md) — Discovery research produces the raw data this skill consumes.
- [`jtbd-to-stories-uxr`](../jtbd-to-stories-uxr/SKILL.md) — Translates the JTBD framework into actionable design requirements and user stories.
- [`user-feedback-synthesiser`](../../../design/ux-researcher/user-feedback-synthesiser/SKILL.md) — Synthesised feedback themes can inform and validate job identification.
