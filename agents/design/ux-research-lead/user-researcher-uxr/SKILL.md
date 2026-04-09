---
name: user-researcher-uxr
description: >
  This skill conducts in-depth user research sessions and synthesises findings. Use when
  asked to run user interviews, conduct contextual inquiries, or facilitate research
  sessions. Also consider when design decisions need direct user evidence but no recent
  research exists. Suggest when the user is about to redesign a flow without talking to
  users first.
department: design
agent: ux-research-lead
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "run user research"
  - "conduct user research"
  - "user research"
  - "research users"
  - "user study"
---

# user-researcher-uxr

## Agent: UX Research Lead

L2 UX research lead (1x) (moved from Product, now reports to Head of Design) responsible for planning and leading user research to directly inform design decisions.

Department ethos: [ideal-design.md](../../../../departments/design/ideal-design.md)

## Skill Description

Conducts in-depth user research sessions including interviews, contextual inquiries, and participatory exercises, then synthesises findings into actionable design insights.

## When to Use

- When a customer discovery plan is ready and research sessions need to be executed with recruited participants.
- When the design team needs fresh qualitative evidence on user behaviours, mental models, or pain points for an active design project.
- When quantitative metrics show a problem (e.g., drop-off at a specific step) but the team does not understand why users are struggling.

## Workflow

1. **Session Preparation**: Review the discussion guide, confirm participant schedule, test recording equipment, and prepare any stimulus materials (prototypes, card sort decks, concept boards). Deliverable: session readiness checklist.
2. **Session Facilitation**: Conduct research sessions using the planned methodology. Employ active listening, open-ended questioning, and comfortable silence to elicit authentic responses. Capture verbatim quotes and behavioural observations. Deliverable: session recordings and field notes.
3. **Debrief & Quick Insights**: After each session, write a 3-5 bullet debrief noting surprising findings, emerging patterns, and questions for subsequent sessions. Deliverable: per-session debrief notes.
4. **Thematic Analysis**: Analyse all session data using affinity diagramming or thematic coding. Group observations into themes, noting frequency and intensity. Distinguish between stated preferences and observed behaviours. Deliverable: thematic analysis with supporting evidence.
5. **Insight Articulation**: Distil themes into 5-10 research insights, each stated as a finding ("Users do X because Y") with supporting evidence (quotes, behavioural counts) and a design implication. Deliverable: research insights document.
6. **Stakeholder Share-Out**: Present insights to design, product, and engineering stakeholders. Facilitate discussion on implications and next steps. Deliverable: share-out session with documented decisions.

## Anti-Patterns

- **Confirmation-seeking facilitation**: Steering conversations toward findings that validate existing assumptions. *Why*: research that only confirms what the team already believes wastes participant time and entrenches incorrect assumptions.
- **Note-taking over listening**: Typing detailed notes during sessions instead of being present with the participant. *Why*: divided attention causes the researcher to miss non-verbal cues and fail to probe interesting responses.
- **Reporting without implications**: Presenting raw findings without translating them into design-relevant implications. *Why*: the design team needs to know what to do differently, not just what users said.
- **Recency bias in synthesis**: Over-weighting findings from the most recent sessions over earlier ones. *Why*: recency bias produces a distorted picture; systematic thematic analysis across all sessions corrects for this.

## Output

**On success**: Produces a research insights document containing 5-10 insights with evidence, thematic analysis, and design implications. Delivered as a shared document with a stakeholder share-out session.

**On failure**: Report which sessions could not be completed or produced unusable data (e.g., participant was outside the target profile, technical recording failure), what partial insights were gathered, and recommend additional sessions to fill gaps.

## Related Skills

- [`customer-discovery-planner-uxr`](../customer-discovery-planner-uxr/SKILL.md) — Plans the research that this skill executes.
- [`jtbd-mapper`](../jtbd-mapper/SKILL.md) — Research findings feed into JTBD mapping.
- [`user-feedback-synthesiser`](../../../design/ux-researcher/user-feedback-synthesiser/SKILL.md) — Complements primary research with ongoing feedback synthesis.
