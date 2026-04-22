---
name: it-helpdesk-operator
description: >
  This skill operates the IT helpdesk by resolving hardware, software, and access issues for all users.
  Use when asked to troubleshoot IT issues, reset passwords, or resolve device problems.
  Also consider when a new employee needs first-day IT setup support.
  Suggest when IT ticket backlog is growing and users report unresolved issues.
department: technical-operations
agent: it-support-specialist
version: 1.0.0
complexity: simple
related-skills:
  - access-provisioning-manager
  - hardware-lifecycle-manager
triggers:
  - "run IT helpdesk"
  - "resolve IT tickets"
  - "IT issue triage"
  - "helpdesk support"
  - "employee IT support"
---

# it-helpdesk-operator

## Agent: IT Support Specialist

L2 IT support specialist (Nx, multi-instance) responsible for helpdesk operations.

Department ethos: [ideal-technical-operations.md](../../../../departments/technical-operations/ideal-technical-operations.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

The IT helpdesk operator receives, triages, and resolves IT support requests covering hardware issues, software problems, and access troubles to keep all employees productive with minimal downtime.

## When to Use

- When an employee submits an IT support request for hardware, software, or access issues.
- When a new hire needs first-day IT setup assistance (device login, tool access, printer setup).
- When a system outage generates a surge of user-reported IT issues.

## Workflow

1. **Receive and triage**: Accept the IT ticket, classify by category (hardware, software, access), and assign priority. Deliverable: triaged ticket with priority and category.
2. **Diagnose**: Investigate the issue using remote tools, logs, or user-provided information. Deliverable: root cause or working hypothesis.
3. **Resolve or escalate**: Apply the fix if within scope; escalate to IT Operations Manager or vendor support if not. Deliverable: resolved ticket or escalation with context.
4. **Document resolution**: Record the diagnosis, fix applied, and time to resolution in the ticket system. Deliverable: closed ticket with resolution notes.
5. **Follow up**: Confirm with the user that the issue is resolved and close the ticket. Deliverable: user confirmation and closed ticket.

## Anti-Patterns

- **Resolving without documenting**: Fixing issues via side-channel (chat, walk-up) without logging a ticket. *Why*: undocumented fixes prevent pattern detection and leave no audit trail for recurring issues.
- **Escalating without diagnosis**: Passing tickets to senior IT without attempting initial troubleshooting. *Why*: premature escalation overloads senior staff and delays resolution for issues the specialist could have solved.

## Output

**On success**: Resolved IT support tickets with documented diagnosis, fix applied, user confirmation, and resolution time within SLA targets.

**On failure**: Report what was attempted, why the issue could not be resolved at this tier, and provide a detailed escalation with all diagnostic information gathered.

## Related Skills

- [`access-provisioning-manager`](../../../technical-operations/it-operations-manager/access-provisioning-manager/SKILL.md) -- helpdesk escalates access provisioning needs to the access provisioning manager.
- [`hardware-lifecycle-manager`](../../../technical-operations/it-operations-manager/hardware-lifecycle-manager/SKILL.md) -- hardware issues that indicate device failure are escalated for lifecycle action.
