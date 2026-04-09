---
name: feedback-loop-formaliser-uxr
description: >
  This skill formalises the process for incorporating research findings into design and
  product decisions. Use when asked to create a research-to-action process, set up feedback
  loops, or ensure research findings actually influence product direction. Also consider
  when research reports are being produced but not acted upon. Suggest when the user
  notices a pattern of research being ignored in planning sessions.
department: design
agent: ux-researcher
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "formalise feedback loop"
  - "feedback loop uxr"
  - "research feedback process"
  - "set up feedback loop"
  - "feedback system"
---

# feedback-loop-formaliser-uxr

## Agent: UX Researcher

L3 UX researcher (Nx) responsible for user feedback synthesis, session analysis, and feeding research findings back into the product and design cycle.

Department ethos: [ideal-design.md](../../../../departments/design/ideal-design.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Formalises the process for incorporating research findings into design and product decisions, ensuring insights travel from research outputs to design actions with accountability.

## When to Use

- When research is being conducted regularly but findings are not systematically influencing design or product decisions.
- When a team is scaling and needs a repeatable process to route research insights to the right decision-makers at the right time.
- When post-launch reviews reveal that known usability issues (identified in prior research) were not addressed, indicating a broken feedback loop.

## Workflow

1. **Current State Audit**: Map the existing path research findings take from completion to action (or inaction). Identify where insights get lost, delayed, or deprioritised. Deliverable: feedback loop gap analysis.
2. **Stakeholder Mapping**: Identify the decision-makers who need research inputs (design leads, product managers, engineering leads) and the cadences at which they make decisions (sprint planning, quarterly roadmapping). Deliverable: stakeholder-decision map.
3. **Process Design**: Design a feedback loop process specifying: how findings are formatted for consumption, where they are stored (research repository), who receives them, when in the planning cycle they are reviewed, and how action/no-action is tracked. Deliverable: feedback loop process document.
4. **Tooling & Template Setup**: Configure the research repository, create insight card templates, set up notification triggers, and build a tracking mechanism for insight-to-action status. Deliverable: configured tooling with templates.
5. **Pilot & Iterate**: Run the feedback loop for one planning cycle, collect meta-feedback from stakeholders on the process itself, and refine. Deliverable: pilot retrospective with process adjustments.

## Anti-Patterns

- **Report-and-forget**: Delivering research reports without tracking whether findings were reviewed or acted upon. *Why*: untracked insights create the illusion of a research practice while decisions continue to be made without evidence.
- **Over-formalisation**: Creating a process so heavy (mandatory reviews, sign-off gates) that teams route around it. *Why*: processes that add friction without visible value get abandoned; the feedback loop must fit within existing team rhythms.
- **Single-channel distribution**: Sharing findings only in one format (e.g., long PDF reports) without adapting to how different stakeholders consume information. *Why*: engineering leads may need a bullet-point summary while designers need annotated visuals; one format guarantees some audiences disengage.
- **No accountability mechanism**: Creating a process without tracking whether insights that were marked "will address" were actually addressed. *Why*: without closure tracking, the same issues resurface in research cycle after cycle.

## Output

**On success**: Produces a feedback loop process document, configured research repository with insight templates, stakeholder notification rules, and an insight-to-action tracking mechanism. Delivered as an operational process with tooling ready for the team to use.

**On failure**: Report which process components could not be implemented (e.g., no shared tooling access, stakeholder non-participation), what alternatives were explored, and recommend a minimal viable loop to start with.

## Related Skills

- [`user-feedback-synthesiser`](../user-feedback-synthesiser/SKILL.md) — Synthesised feedback is a primary input routed through the formalised loop.
- [`session-analysis-uxr`](../session-analysis-uxr/SKILL.md) — Session analysis findings need a formalised path to reach decision-makers.
- [`ux-flow-designer-uxr`](../../../design/ux-research-lead/ux-flow-designer-uxr/SKILL.md) — Flow redesigns should be triggered by insights routed through the feedback loop.
