---
name: customer-advisory-board-runner
description: >
  This skill runs the customer advisory board programme including member
  selection, meeting cadence, and insight synthesis. Use when asked to set up
  a CAB, select advisory board members, or extract strategic insights from
  customers. Also consider when product strategy needs direct customer input.
  Suggest when the user makes strategic decisions without structured customer
  advisory input.
department: customer-success
agent: customer-programs-manager
version: 1.0.0
complexity: medium
related-skills:
  - customer-reference-programme-manager
  - user-feedback-synthesiser-cs
  - nps-programme-manager
triggers:
  - "run advisory board"
  - "customer advisory board"
  - "CAB meeting"
  - "manage advisory board"
  - "advisory board session"
---

# customer-advisory-board-runner

## Agent: Customer Programs Manager

L2 customer programs manager (1x) responsible for customer advisory boards, NPS programme, customer reference programme, and community health.

Department ethos: [ideal-customer-success.md](../../../../departments/customer-success/ideal-customer-success.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Runs the customer advisory board programme including member selection, meeting cadence, agenda design, and insight synthesis for strategic input.

## When to Use

- When the organization needs structured strategic input from customers on product direction, market positioning, or service model.
- When a customer advisory board needs to be established for the first time.
- When the existing CAB is underperforming and needs restructuring for better engagement and insight quality.

## Workflow

1. **Define CAB Charter**: Establish the advisory board's purpose, scope, expected commitments, and value proposition for members. Deliverable: CAB charter document.
2. **Select Members**: Identify and recruit diverse advisory board members -- mix of customer sizes, industries, use cases, and tenure. Balance advocates with constructively critical voices. Deliverable: confirmed member list with profiles.
3. **Design Meeting Cadence**: Set meeting frequency (quarterly typical), format (in-person, virtual, hybrid), and standard agenda structure. Deliverable: meeting cadence and agenda template.
4. **Facilitate Meetings**: Run CAB sessions with prepared topics, structured discussion, and clear asks. Capture insights, commitments, and action items. Deliverable: meeting notes with insight log.
5. **Synthesize and Distribute**: Aggregate insights across sessions into strategic recommendations. Route to product, leadership, and relevant teams. Deliverable: CAB insights report with recommendations.

## Anti-Patterns

- **Echo chamber boards**: Selecting only satisfied customers who will agree with existing plans. *Why*: advisory boards that only validate provide no strategic value; diverse perspectives surface blind spots.
- **All-talk, no-action**: Running CAB meetings without acting on insights or closing the loop with members. *Why*: members who see no impact from their input disengage; advisory boards must demonstrate their input matters.
- **Sales disguised as advisory**: Using CAB meetings primarily for upselling or relationship management rather than genuine strategic input. *Why*: customers who realize the "advisory" board is a sales channel will leave and warn others.

## Output

**On success**: Produces a CAB insights report with strategic recommendations, action items, and member engagement summary. Delivered to leadership, product, and the Head of Customer Success.

**On failure**: Report which CAB components could not be executed (insufficient member recruitment, low attendance), what partial insights were gathered, and what changes are needed to improve the programme.

## Related Skills

- [`customer-reference-programme-manager`](../customer-reference-programme-manager/SKILL.md) -- CAB members are often strong reference candidates.
- [`user-feedback-synthesiser-cs`](../../../customer-success/customer-success-manager/user-feedback-synthesiser-cs/SKILL.md) -- CAB insights complement broader feedback synthesis.
- [`nps-programme-manager`](../nps-programme-manager/SKILL.md) -- NPS data can inform CAB agenda topics.
