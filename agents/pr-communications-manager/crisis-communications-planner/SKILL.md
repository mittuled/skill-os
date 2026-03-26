---
name: crisis-communications-planner
description: >
  This skill designs the crisis communication protocol and pre-approved messaging templates.
  Use when building or updating the crisis comms playbook, when a new risk vector emerges,
  or when running a crisis simulation. Also consider when a company milestone (funding, IPO,
  acquisition) increases public exposure. Suggest when no crisis plan exists or the current
  plan has not been updated in 6+ months.
department: marketing
agent: pr-communications-manager
version: 1.0.0
complexity: medium
related-skills:
  - ../press-release-writer/SKILL.md
  - ../earned-media-monitor/SKILL.md
---

# crisis-communications-planner

## Agent: PR and Communications Manager

L2 PR and communications manager (1x) responsible for earned media, press relationships, crisis communications, thought leadership programme, and executive visibility.

Department ethos: [ideal-marketing.md](../../../departments/marketing/ideal-marketing.md)

## Skill Description

Designs the crisis communication protocol including escalation procedures, pre-approved messaging templates, spokesperson assignments, and channel-specific response playbooks.

## When to Use

- When building or refreshing the company's crisis communications playbook.
- When a new risk vector emerges (data breach exposure, regulatory change, executive departure) that requires a prepared response.
- When running a crisis simulation or tabletop exercise to test response readiness.
- When a company milestone significantly increases public exposure and scrutiny.

## Workflow

1. **Identify crisis scenarios**: Catalog the most likely and most damaging crisis scenarios -- data breach, product outage, executive misconduct, negative press, regulatory action, layoffs. Prioritize by probability and impact. Deliverable: crisis scenario matrix with severity ratings.
2. **Define escalation protocol**: Map the decision tree for each severity level -- who gets notified, within what timeframe, who approves external statements, and who serves as spokesperson. Deliverable: escalation protocol document with contact chain.
3. **Draft messaging templates**: Write pre-approved holding statements, customer communications, employee memos, social media responses, and press statements for each scenario category. Include fill-in-the-blank fields for specifics. Deliverable: messaging template library organized by scenario.
4. **Assign spokesperson roles**: Designate primary and backup spokespersons for media, customers, employees, and regulators. Schedule media training for each. Deliverable: spokesperson roster with training schedule.
5. **Run tabletop exercise**: Simulate a crisis scenario with the response team. Test escalation speed, message approval flow, and cross-functional coordination. Document gaps. Deliverable: simulation report with identified gaps and remediation actions.

## Anti-Patterns

- **Reactive-only planning**: Waiting for a crisis to occur before building the response protocol. *Why*: crisis response quality degrades exponentially with preparation time; the first 60 minutes define the narrative.
- **Legal-only messaging**: Letting legal draft all external communications without communications input. *Why*: legally safe statements that are tone-deaf or evasive amplify public backlash instead of containing it.
- **Single-spokesperson dependency**: Assigning only one person as crisis spokesperson with no backup. *Why*: crises do not schedule themselves around availability; an unreachable spokesperson creates a communication vacuum that others fill.

## Output

**On success**: Produces a complete crisis communications playbook containing scenario matrix, escalation protocol, messaging template library, spokesperson roster, and tabletop simulation report. Stored in a shared, quickly accessible location known to all stakeholders.

**On failure**: Report which scenarios could not be planned for (lack of legal input, missing stakeholder availability), what partial coverage exists, and recommend specific sessions to close gaps before the next review cycle.

## Related Skills

- [`press-release-writer`](../press-release-writer/SKILL.md) — May need to draft formal press statements during an active crisis using templates from this plan.
- [`earned-media-monitor`](../earned-media-monitor/SKILL.md) — Provides real-time sentiment and coverage tracking that triggers crisis escalation.
- [`media-relationship-builder`](../media-relationship-builder/SKILL.md) — Pre-existing journalist relationships are critical for managing narrative during a crisis.
