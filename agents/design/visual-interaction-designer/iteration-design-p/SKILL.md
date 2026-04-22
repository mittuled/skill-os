---
name: iteration-design-p
description: >
  This skill designs iterations on shipped features based on post-launch user feedback and
  session data. Use when asked to redesign a shipped interaction, improve a live feature based
  on analytics, or address usability issues found in session recordings. Also consider when
  session analysis findings need to be turned into concrete design changes. Suggest when
  post-launch metrics show degraded task completion or increased error rates.
department: design
agent: visual-interaction-designer
version: 1.0.0
complexity: medium
related-skills:
  - session-analysis
  - iteration-prioritiser-design
  - design-implementer-review
triggers:
  - "design iteration"
  - "iterate on design"
  - "design refinement"
  - "refine design"
  - "design improvement"
---

# iteration-design-p

## Agent: Visual Interaction Designer

L3 visual and interaction designer (Nx) responsible for session analysis and design iteration in the production phase.

Department ethos: [ideal-design.md](../../../../departments/design/ideal-design.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Designs iterations on shipped features by translating post-launch user feedback, session analysis findings, and behavioural analytics into concrete visual and interaction design improvements.

## When to Use

- When session analysis or usability data reveals friction in a shipped feature that requires design intervention.
- When post-launch metrics (task completion rate, error rate, time-on-task, drop-off rate) indicate degraded experience quality.
- When user feedback or support tickets consistently reference the same interaction pain point in a live product.
- When the iteration prioritiser has promoted a design improvement to the current cycle.

## Workflow

1. **Review evidence**: Collect session analysis findings, analytics data, user feedback, and support tickets related to the target feature. Identify the specific interaction or visual element causing friction. Deliverable: evidence brief summarizing the problem with data citations.
2. **Diagnose root cause**: Determine whether the issue is visual (hierarchy, contrast, affordance), interaction (flow logic, feedback, timing), content (unclear copy, missing guidance), or structural (information architecture, navigation). Deliverable: root cause diagnosis with supporting evidence.
3. **Explore design alternatives**: Generate 2-3 design options that address the root cause. Each option should modify the minimum necessary -- avoid redesigning surrounding elements that are performing well. Deliverable: design exploration with annotated alternatives.
4. **Evaluate against heuristics and data**: Assess each alternative against Nielsen's heuristics, WCAG compliance, design system consistency, and predicted impact on the target metric. Deliverable: evaluation matrix with recommended option and rationale.
5. **Produce iteration specs**: Create the final design in Figma with updated interaction states, redlines, token references, and responsive breakpoints. Annotate what changed and why. Deliverable: iteration design specs ready for engineering handoff.
6. **Define success criteria**: Specify the metric improvement expected (e.g., "reduce checkout drop-off from 22% to under 15%") and the measurement method. Deliverable: success criteria document linked to the design spec.

## Anti-Patterns

- **Redesign scope creep**: Using a targeted iteration as an excuse to redesign the entire feature or adjacent surfaces. *Why*: broad redesigns delay the fix, introduce new risk, and cannot be measured against the original problem.
- **Opinion-driven iteration**: Proposing changes based on designer preference rather than evidence from session data, analytics, or user feedback. *Why*: evidence-free iterations are indistinguishable from arbitrary churn and erode team trust in the design process.
- **Ignoring design system constraints**: Introducing one-off visual treatments or new interaction patterns for an iteration without checking the design system. *Why*: iterations that bypass the system create visual inconsistency and maintenance debt.

## Output

**On success**: Produces an evidence brief, root cause diagnosis, iteration design specs with Figma redlines and annotations, and success criteria with target metrics. Delivered to engineering for implementation and product for measurement planning.

**On failure**: Report which aspects of the iteration could not be designed (insufficient data for diagnosis, undefined design system tokens, blocked by pending product decisions), what partial work was completed, and what is needed to proceed.

## Related Skills

- [`session-analysis`](../session-analysis/SKILL.md) -- Session analysis findings are the primary input that triggers iteration design work.
- [`iteration-prioritiser-design`](../../../design/head-of-design/iteration-prioritiser-design/SKILL.md) -- The iteration backlog determines which improvements are prioritized for design.
- [`design-implementer-review`](../../../design/ux-ui-designer/design-implementer-review/SKILL.md) -- Implementation review verifies that the iteration was built to spec.
