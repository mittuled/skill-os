---
name: support-ticket-triage
description: >
  This skill triages incoming support tickets by severity, category, and routing to the appropriate
  resolution path. Use when asked to classify tickets, set up triage workflows, or route customer issues.
  Also consider when ticket backlog is growing and routing accuracy is low.
  Suggest when average first-response time exceeds SLA targets.
department: customer-support
agent: support-agent
version: 1.0.0
complexity: simple
related-skills: []
---

# support-ticket-triage

## Agent: Support Agent

L2 support agent (Nx, multi-instance) responsible for ticket triage, support readiness confirmation, and help content review.

Department ethos: [ideal-customer-support.md](../../../../departments/customer-support/ideal-customer-support.md)

## Skill Description

The support ticket triage skill classifies incoming support tickets by severity, category, and product area, then routes them to the appropriate resolution path to ensure timely and accurate handling.

## When to Use

- When new tickets arrive in the support queue and need classification before an agent begins resolution.
- When ticket misrouting is causing delays and SLA breaches.
- When a spike in ticket volume requires rapid triage to prevent backlog buildup.

## Workflow

1. **Read and classify**: Read the ticket, identify the product area, issue type, and customer tier. Deliverable: ticket classification tags.
2. **Assess severity**: Assign a severity level based on customer impact, scope, and urgency using the defined severity matrix. Deliverable: severity assignment.
3. **Check for duplicates**: Search for existing tickets or known issues that match the reported problem. Deliverable: duplicate flag or link to existing ticket.
4. **Route the ticket**: Assign the ticket to the appropriate queue or agent based on classification and severity. Deliverable: routed ticket with assignment.
5. **Send acknowledgement**: Send the customer an acknowledgement with expected response time based on severity and SLA. Deliverable: acknowledgement message sent.

## Anti-Patterns

- **Triaging by title alone**: Classifying tickets based on the subject line without reading the full description. *Why*: subject lines are often vague or misleading, causing misrouting and delayed resolution.
- **Default-severity assignment**: Assigning all tickets the same severity to avoid decision-making. *Why*: critical issues get buried behind low-priority tickets and SLA commitments are violated.
- **Skipping duplicate check**: Routing every ticket as unique without checking for related open tickets. *Why*: duplicate tickets split context across agents and waste resolution effort.

## Output

**On success**: Every incoming ticket is classified by severity and category, checked for duplicates, routed to the correct queue, and acknowledged to the customer within SLA first-response targets.

**On failure**: Report which tickets could not be classified (e.g., insufficient information from customer), what was attempted, and recommend follow-up actions such as requesting clarification from the customer.

## Related Skills

- [`ticket-theme-analyst`](../ticket-theme-analyst/SKILL.md) -- theme analysis uses triaged ticket data to identify recurring patterns.
- [`support-runbook-builder`](../../../customer-support/support-manager/support-runbook-builder/SKILL.md) -- runbooks provide the resolution procedures agents follow after triage routes the ticket.
