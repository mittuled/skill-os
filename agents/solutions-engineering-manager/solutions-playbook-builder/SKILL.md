---
name: solutions-playbook-builder
description: >
  This skill builds the solutions engineering playbook including technical
  discovery questions and POC criteria. Use when asked to create SE enablement
  materials, define POC standards, or document technical qualification criteria.
  Also consider when SEs lack standardized technical discovery frameworks.
  Suggest when SE win rates diverge significantly across the team.
department: sales
agent: solutions-engineering-manager
version: 1.0.0
complexity: complex
related-skills:
  - ../technical-buyer-signal-extractor/SKILL.md
  - ../../sales-manager/sales-playbook-builder/SKILL.md
  - ../../solutions-engineer/proof-of-concept-runner/SKILL.md
---

# solutions-playbook-builder

## Agent: Solutions Engineering Manager

L2 solutions engineering manager (1x) responsible for technical buyer signal extraction and solutions playbook development.

Department ethos: [ideal-sales.md](../../../departments/sales/ideal-sales.md)

## Skill Description

Builds the solutions engineering playbook including technical discovery questions, POC criteria, demo frameworks, and technical qualification standards that SEs execute consistently.

## When to Use

- When the SE team has no standardized playbook and technical discovery quality varies across reps.
- When onboarding new SEs who need a structured framework for technical engagement.
- When POC win rates are low or POC scope creep is consuming SE capacity without proportional deal closure.

## Workflow

1. **Technical Discovery Framework**: Build a structured technical discovery question bank organized by evaluation phase: environment assessment (current stack, integration requirements, security constraints), use case validation (primary workflows, edge cases, scale requirements), and decision criteria mapping (must-haves, nice-to-haves, dealbreakers). Deliverable: technical discovery question bank with phase tags.
2. **POC Criteria Definition**: Define POC entry criteria (minimum deal size, qualification score, executive sponsor confirmed), scope boundaries (maximum duration, feature set, success metrics), and exit criteria (pass/fail thresholds, decision timeline commitment). Deliverable: POC qualification and scoping framework.
3. **Demo Framework**: Build demo frameworks for each buyer persona: technical evaluator (architecture, APIs, integration), business buyer (outcomes, ROI, workflow), and end user (UX, daily workflow). Define demo environment requirements and setup procedures. Deliverable: persona-specific demo frameworks with environment specs.
4. **Technical Objection Library**: Document common technical objections with evidence-based responses: security concerns (certifications, architecture), scalability questions (benchmarks, reference architectures), and integration complexity (API documentation, pre-built connectors). Deliverable: technical objection library with proof points.
5. **Competitive Technical Analysis**: Create technical comparison matrices against the top 3 competitors covering architecture, performance, integration ecosystem, security posture, and deployment model. Include "trap questions" SEs can use to expose competitor weaknesses. Deliverable: competitive technical matrices with trap questions.
6. **SE Engagement Model**: Define when and how SEs engage in the deal cycle: stage-gate entry points, time allocation per deal tier, and escalation criteria for complex technical requirements. Deliverable: SE engagement model with capacity guidelines.
7. **Assembly and Review**: Assemble all components into a navigable playbook. Review with VP Sales and 2 senior SEs. Incorporate feedback and publish with a quarterly update cadence. Deliverable: complete solutions engineering playbook v1.0.

## Anti-Patterns

- **Demo-first engagement**: Allowing SEs to jump into demos before technical discovery. *Why*: demos without discovery produce generic presentations that do not address the prospect's specific technical concerns; this wastes SE time and fails to differentiate.
- **Unbounded POCs**: Running POCs without predefined scope, success criteria, or time limits. *Why*: unbounded POCs become free consulting engagements that consume SE capacity without correlating to deal progression; prospects use them to delay decisions.
- **One-size-fits-all demos**: Using the same demo for technical evaluators, business buyers, and end users. *Why*: each persona cares about different things; a deep API demo alienates business buyers while a high-level overview fails to satisfy technical evaluators.
- **Building without SE input**: Creating the playbook from management perspective without incorporating what top-performing SEs actually do in technical engagements. *Why*: SE workflows have nuances (deal room dynamics, live troubleshooting, technical credibility building) that management prescriptions miss.

## Output

**On success**: Produces a complete solutions engineering playbook containing technical discovery framework, POC criteria, demo frameworks, technical objection library, competitive technical matrices, and SE engagement model. Delivered to the SE team with an enablement session scheduled.

**On failure**: Report which playbook section could not be completed (e.g., insufficient competitive technical data, no POC outcome data to inform criteria), what was attempted, and what inputs are needed.

## Related Skills

- [`technical-buyer-signal-extractor`](../technical-buyer-signal-extractor/SKILL.md) -- Provides technical buyer signal data that informs playbook content.
- [`sales-playbook-builder`](../../sales-manager/sales-playbook-builder/SKILL.md) -- The sales counterpart playbook that aligns with the SE playbook on qualification and process.
- [`proof-of-concept-runner`](../../solutions-engineer/proof-of-concept-runner/SKILL.md) -- Executes POCs using the criteria and frameworks defined in this playbook.
