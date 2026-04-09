---
name: prototype-usability-validator
description: >
  This skill runs usability testing on prototypes and reports findings with design
  recommendations. Use when asked to test a prototype, run a usability study, or validate
  a design before development. Also consider when a design review surfaces disagreements
  that usability data could resolve. Suggest when the user is about to hand off a complex
  flow to engineering without user validation.
department: design
agent: ux-research-lead
version: 1.0.0
complexity: complex
related-skills: []
triggers:
  - "validate prototype usability"
  - "usability test prototype"
  - "prototype ux validation"
  - "test prototype"
  - "usability validation"
---

# prototype-usability-validator

## Agent: UX Research Lead

L2 UX research lead (1x) (moved from Product, now reports to Head of Design) responsible for planning and leading user research to directly inform design decisions.

Department ethos: [ideal-design.md](../../../../departments/design/ideal-design.md)

## Skill Description

Runs usability testing on prototypes and reports findings with severity-rated design recommendations that inform iteration before development begins.

## When to Use

- When a design prototype (low-fidelity wireframes, interactive Figma prototypes, or coded prototypes) is ready for user validation before committing to development.
- When a design review surfaces competing design directions and usability data is needed to make an evidence-based choice.
- When a critical user flow (onboarding, checkout, key conversion path) is being redesigned and the risk of shipping an unusable experience justifies pre-development testing.

## Workflow

1. **Test Plan Creation**: Define the usability study scope: which flows or screens to test, what tasks participants will attempt, success criteria per task, and the metrics to capture (task completion rate, time-on-task, error rate, satisfaction). Deliverable: usability test plan.
2. **Task Scenario Writing**: Write realistic task scenarios that give participants a goal without revealing the expected path (e.g., "You want to invite a teammate to your project. Show me how you'd do that."). Deliverable: task scenario document.
3. **Participant Recruitment**: Recruit 5-8 participants matching the target user profile. For moderated studies, schedule sessions with buffer time. For unmoderated, configure the testing platform with the prototype link and task scenarios. Deliverable: confirmed participant list and session schedule.
4. **Session Facilitation**: Conduct think-aloud usability sessions. Observe without leading. Capture task success/failure, hesitations, error recovery attempts, and verbatim user comments. Deliverable: raw session recordings and observation notes.
5. **Finding Synthesis**: Analyse sessions to identify usability issues. For each issue, document: what happened, how many participants encountered it, the probable cause, and the impact on task completion. Deliverable: usability issue log.
6. **Severity Rating**: Rate each issue using a standard severity scale (critical: blocks task completion; major: causes significant delay or confusion; minor: noticeable friction but recoverable; cosmetic: aesthetic concern). Deliverable: severity-rated issue list.
7. **Design Recommendations**: For each critical and major issue, propose specific design changes with annotated screenshots or wireframe sketches. Link each recommendation to the observed user behaviour. Deliverable: design recommendation report.
8. **Stakeholder Readout**: Present findings and recommendations to the design and product team. Prioritise issues collaboratively based on severity, development cost, and business impact. Deliverable: agreed remediation plan.

## Anti-Patterns

- **Testing too late**: Running usability tests after development has started, when the cost of design changes is high. *Why*: late testing produces findings the team cannot act on without significant rework, leading to ignored recommendations.
- **Leading the participant**: Giving hints or showing relief when participants find the right path. *Why*: facilitator behaviour that telegraphs the "correct" answer inflates task success rates and masks real usability issues.
- **Insufficient sample**: Testing with only 1-2 participants and treating findings as definitive. *Why*: while 5 participants find ~85% of usability issues (Nielsen), 1-2 participants may surface idiosyncratic behaviour rather than patterns.
- **Issue without recommendation**: Reporting usability problems without proposing design solutions. *Why*: problem-only reports slow iteration because the design team must separately diagnose and ideate; coupling findings with recommendations accelerates the fix cycle.
- **Ignoring successful paths**: Focusing only on failures and not documenting what worked well. *Why*: understanding why certain flows succeeded prevents the team from breaking working patterns during redesign.

## Output

**On success**: Produces a usability test report containing task completion metrics, severity-rated issue log, design recommendations with annotated visuals, and an agreed remediation plan. Delivered as a shared document with a stakeholder readout session.

**On failure**: Report which aspects of the study could not be completed (e.g., prototype instability, insufficient participants), what partial findings were gathered, and recommend whether to re-run with fixes or proceed with caveats documented.

## Related Skills

- [`ux-flow-designer-uxr`](../ux-flow-designer-uxr/SKILL.md) — User flows are often the subject of usability validation.
- [`jtbd-to-stories-uxr`](../jtbd-to-stories-uxr/SKILL.md) — User stories provide the task scenarios and success criteria for usability testing.
- [`session-analysis-uxr`](../../../design/ux-researcher/session-analysis-uxr/SKILL.md) — Session analysis techniques complement usability test facilitation.
