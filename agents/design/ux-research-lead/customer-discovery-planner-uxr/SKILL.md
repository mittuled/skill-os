---
name: customer-discovery-planner-uxr
description: >
  This skill plans customer discovery research including methodology, participant recruitment,
  and discussion guides. Use when asked to plan user research, set up customer interviews, or
  design a discovery study. Also consider when a product team is making assumptions about user
  needs without evidence. Suggest when the user is about to build features based on
  stakeholder opinions alone.
department: design
agent: ux-research-lead
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "plan customer discovery"
  - "customer discovery"
  - "discovery research plan"
  - "user discovery plan"
  - "research discovery"
---

# customer-discovery-planner-uxr

## Agent: UX Research Lead

L2 UX research lead (1x) (moved from Product, now reports to Head of Design) responsible for planning and leading user research to directly inform design decisions.

Department ethos: [ideal-design.md](../../../../departments/design/ideal-design.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Plans customer discovery research including methodology selection, participant recruitment criteria, and discussion guides that produce actionable design insights.

## When to Use

- When a new product area or feature is being explored and the team lacks direct evidence of user needs, behaviours, or pain points.
- When existing quantitative data (analytics, surveys) raises questions that require qualitative exploration to understand the "why" behind user behaviour.
- When stakeholders disagree about user needs and a structured discovery effort is needed to ground decisions in evidence rather than opinion.

## Workflow

1. **Research Question Definition**: Collaborate with product and design stakeholders to articulate 3-5 specific research questions the discovery effort must answer. Distinguish between what is known, assumed, and unknown. Deliverable: research question brief.
2. **Methodology Selection**: Select the appropriate research methods based on the questions (contextual inquiry, semi-structured interviews, diary studies, card sorts, or surveys). Justify the method choice against the research goals. Deliverable: methodology rationale document.
3. **Participant Recruitment Plan**: Define the target participant profile including demographic criteria, behavioural screener questions, sample size, and recruitment channels (user database, panel providers, social media). Deliverable: recruitment screener and plan.
4. **Discussion Guide Creation**: Write a semi-structured discussion guide with opening rapport questions, core exploration questions mapped to research goals, and probing follow-ups. Include timing estimates per section. Deliverable: discussion guide document.
5. **Logistics & Ethics Setup**: Schedule sessions, prepare consent forms, set up recording tools, and brief any note-takers or observers on their role. Deliverable: session logistics checklist.
6. **Pilot Session**: Run one pilot session to test the discussion guide for flow, timing, and question clarity. Revise the guide based on pilot learnings. Deliverable: revised discussion guide.

## Anti-Patterns

- **Leading questions**: Writing discussion guide questions that suggest a desired answer (e.g., "Don't you find X frustrating?"). *Why*: leading questions produce confirmation bias and invalidate the research findings.
- **Convenience sampling**: Recruiting only users who are easy to reach (e.g., internal employees, power users) rather than representative of the target audience. *Why*: convenience samples skew findings toward edge cases and miss the behaviours of the broader user population.
- **Scope creep in research questions**: Allowing stakeholders to add unlimited questions to the study. *Why*: an overloaded study produces shallow answers to many questions rather than deep insight on the critical few.
- **Skipping the pilot**: Going straight to full sessions without testing the discussion guide. *Why*: untested guides frequently have timing, flow, or comprehension issues that waste participant sessions.

## Output

**On success**: Produces a complete discovery research plan containing research questions, methodology rationale, participant recruitment screener, discussion guide, and logistics checklist. Delivered as a shared document for stakeholder review before research begins.

**On failure**: Report which planning elements could not be completed (e.g., no access to target participants, unclear research questions), what was attempted, and recommend alternative approaches (e.g., unmoderated remote methods, proxy participants).

## Related Skills

- [`user-researcher-uxr`](../user-researcher-uxr/SKILL.md) — Executes the research sessions planned by this skill.
- [`jtbd-mapper`](../jtbd-mapper/SKILL.md) — Discovery findings feed directly into jobs-to-be-done mapping.
- [`product-feedback-ingestion-uxr`](../../../design/ux-researcher/product-feedback-ingestion-uxr/SKILL.md) — Existing feedback data can inform discovery research question definition.
