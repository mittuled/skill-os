---
name: session-analysis
description: >
  This skill analyses user session recordings to identify usability friction and design
  improvement opportunities. Use when asked to review session replays, identify UX pain
  points from recordings, or extract design insights from behavioural data. Also consider
  when post-launch metrics show unexpected user behaviour patterns. Suggest when a feature
  has been live for a sprint without any session review.
department: design
agent: visual-interaction-designer
version: 1.0.0
complexity: medium
related-skills: []
---

# session-analysis

## Agent: Visual Interaction Designer

L3 visual and interaction designer (Nx) responsible for session analysis and design iteration in the production phase.

Department ethos: [ideal-design.md](../../../../departments/design/ideal-design.md)

## Skill Description

Analyses user session recordings to identify usability friction, interaction dead ends, and design improvement opportunities through systematic observation of real user behaviour.

## When to Use

- When a feature has shipped and session recordings are available for post-launch behavioural review.
- When quantitative analytics show anomalies (high bounce, unexpected navigation paths, low conversion) that need qualitative explanation.
- When the team needs to prioritize design iterations and requires evidence of where users struggle most.
- When a usability test was not conducted pre-launch and session recordings serve as the post-hoc evaluation method.

## Workflow

1. **Define analysis scope**: Identify the feature, user flow, or interaction to focus on. Set the session sample criteria -- user segment, date range, device type, completion status (completed vs. abandoned). Deliverable: analysis scope document with sampling criteria.
2. **Sample and watch sessions**: Select a representative sample of sessions (minimum 15-20 for pattern reliability). Watch each session end to end for the scoped flow, noting timestamps of friction events. Deliverable: session observation log with timestamped notes per session.
3. **Code friction events**: Categorize observed friction into types -- rage clicks, hesitation (cursor drift without action), backtracking, form abandonment, missed affordances, misclicks on non-interactive elements, scroll bounce. Deliverable: coded friction event matrix with frequency counts.
4. **Identify patterns**: Aggregate coded events across sessions. Identify recurring friction points (same element, same step, same confusion). Distinguish systematic design issues from individual user variability. Deliverable: pattern summary with severity ranking (frequency x impact).
5. **Generate design hypotheses**: For each significant pattern, propose a design hypothesis: what change would reduce the observed friction. Link each hypothesis to the specific friction evidence. Deliverable: hypothesis register with evidence citations.
6. **Compile analysis report**: Assemble findings into a structured report with video clips or screenshots illustrating key friction moments. Include prioritized recommendations. Deliverable: session analysis report.

## Anti-Patterns

- **Cherry-picking sessions**: Selecting only sessions that confirm a pre-existing belief about where the problem is. *Why*: confirmation bias produces inaccurate findings; representative sampling is required for reliable pattern identification.
- **Counting without context**: Reporting friction event counts without explaining the user's intent, the task context, or the severity of the interruption. *Why*: a rage click on a primary CTA is far more severe than hesitation on an optional tooltip; raw counts obscure this difference.
- **Prescribing solutions in analysis**: Jumping to specific design solutions within the analysis report instead of presenting evidence and hypotheses. *Why*: analysis should inform design decisions, not make them; premature solutions skip the exploration phase where better alternatives may emerge.

## Output

**On success**: Produces a session analysis report containing the friction event matrix, pattern summary with severity ranking, design hypotheses with evidence citations, and prioritized recommendations with supporting video clips or screenshots. Delivered to the design team, product manager, and iteration prioritiser.

**On failure**: Report which sessions could not be analysed (recording tool limitations, insufficient sample size, missing user segment data), what partial analysis was completed, and what data collection changes are needed for future analysis.

## Related Skills

- [`iteration-design-p`](../iteration-design-p/SKILL.md) -- Session analysis findings directly feed the iteration design process.
- [`iteration-prioritiser-design`](../../../design/head-of-design/iteration-prioritiser-design/SKILL.md) -- Analysis severity rankings inform backlog prioritization.
- [`accessibility-auditor-design`](../../../design/head-of-design/accessibility-auditor-design/SKILL.md) -- Session recordings may reveal accessibility barriers that warrant a formal audit.
