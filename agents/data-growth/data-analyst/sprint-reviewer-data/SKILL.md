---
name: sprint-reviewer-data
description: >
  This skill reviews data deliverables in sprint to confirm instrumentation and dashboards meet requirements. Use when asked to QA analytics deliverables, review sprint data work, or sign off on instrumentation and dashboard completeness. Also consider at sprint end when data work items are marked done. Suggest when data tasks close without explicit review.
department: data-growth
agent: data-analyst
version: 1.0.0
complexity: simple
related-skills:
  - instrumentation-verifier-data
  - metrics-dashboard-builder
  - sprint-reviewer
triggers:
  - "review data sprint"
  - "analytics sprint review"
  - "data team sprint retrospective"
  - "sprint output review data"
  - "data sprint retrospective"
---

# sprint-reviewer-data

## Agent: Data Analyst

L2 data analyst (Nx) responsible for data modelling, instrumentation implementation, metrics dashboards, funnel analysis, and signal synthesis.

Department ethos: [ideal-data-growth.md](../../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The sprint reviewer audits all data deliverables completed in the current sprint — instrumentation implementations, dashboard builds, data model changes, and analysis reports — to confirm each meets the acceptance criteria defined in the ticket and the standards defined in the instrumentation spec.

## When to Use

- When the sprint approaches completion and data work items need sign-off before the sprint review meeting.
- When multiple data tasks complete in parallel and need consolidated quality review.
- When a prior sprint had data quality issues escape review, and the team wants to prevent recurrence.

## Workflow

1. **List deliverables**: Pull all data-related tickets marked "done" or "in review" in the current sprint. Categorize by type (instrumentation, dashboard, analysis, data model).
2. **Review instrumentation**: For each instrumentation ticket, confirm the verification report exists, events pass spec validation, and production deployment is scheduled or complete.
3. **Review dashboards**: For each dashboard ticket, verify metric accuracy against raw queries, confirm layout matches the design spec, and check that documentation exists.
4. **Review analyses**: For each analysis ticket, validate methodology, check data sources, and confirm the output addresses the question posed in the ticket.
5. **Compile review summary**: Produce a sprint data review summary listing each deliverable, its status (approved / needs rework), and specific feedback for any rework items.

## Anti-Patterns

- **Rubber-stamping done tickets**: Marking deliverables as reviewed without checking the output produces a false sense of quality. *Why*: unreviewed instrumentation ships bugs to production; unreviewed dashboards display wrong numbers.
- **Reviewing in isolation**: Checking each deliverable without considering cross-deliverable dependencies misses integration issues. *Why*: a dashboard built on a data model that changed in the same sprint may reference deprecated columns.

## Output

**Success:**
- A sprint data review summary with pass/rework status per deliverable and specific feedback for any items requiring rework, delivered before the sprint review meeting.

**Failure:**
- Data deliverables ship without review and quality issues are discovered post-sprint. Report the escaped issue, its impact, and the review process gap that allowed it.

## Related Skills

- [`instrumentation-verifier-data`](../instrumentation-verifier-data/SKILL.md) -- instrumentation verification is a key input to the sprint review.
- [`metrics-dashboard-builder`](../metrics-dashboard-builder/SKILL.md) -- dashboards are a primary deliverable reviewed in sprint.
- [`sprint-reviewer`](../../../product/product-manager/sprint-reviewer/SKILL.md) -- the PM sprint reviewer covers product deliverables; this skill focuses on data deliverables.
