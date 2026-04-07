---
name: incident-response-planner
description: Prepares the team to handle production failures fast by defining clear procedures and escalation paths.
department: engineering
agent: devops-infrastructure-engineer
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "plan incident response"
  - "set up on-call procedures"
  - "define escalation paths"
  - "create an incident playbook"
---

# incident-response-planner

## Agent

L2 DevOps and infrastructure engineer responsible for CI/CD pipelines, deployment automation, cloud infrastructure, monitoring, alerting, incident response, and rollout management.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

The DevOps / Infrastructure Engineer plans incident response procedures and escalation paths for production failures.

## When to Use

- The team is launching a new service and needs incident response procedures before go-live.
- A post-incident review revealed that response was slow or uncoordinated.
- On-call rotations are being established or restructured.
- Compliance requirements mandate documented incident response plans.

## Workflow

1. Identify the categories of incidents the service can experience (outage, data loss, security breach, performance degradation).
2. Define severity levels with clear criteria for each (e.g., S1: full outage, S2: partial degradation).
3. Map escalation paths for each severity: who is notified, in what order, and through which channels.
4. Define roles during an incident: incident commander, communicator, technical responder.
5. Document the response procedures: triage steps, communication cadence, and resolution workflow.
6. Set up on-call schedules with rotation policies and escalation timeouts.
7. Create incident communication templates for internal and external stakeholders.
8. Run a tabletop exercise to validate the plan with the team.
   - **Deliverable**: An incident response plan with severity definitions, escalation paths, role assignments, communication templates, and tabletop exercise results.

## Anti-Patterns

- **Writing the incident response plan after the first major incident.** *Why*: The first incident is the worst time to figure out the process; planning must precede production exposure.
- **Defining escalation paths without timeout-based auto-escalation.** *Why*: Manual escalation depends on someone remembering to escalate; timeouts ensure no incident goes unattended.
- **Skipping tabletop exercises.** *Why*: An untested plan contains assumptions that will fail under the stress of a real incident.
- **Assigning on-call without training.** *Why*: On-call engineers who do not know the system or the procedures will be ineffective responders.

## Output

**Success**: A documented and exercised incident response plan with severity levels, escalation paths, on-call schedules, and communication templates.

**Failure**: A gap analysis listing missing procedures, untested scenarios, or unclear escalation paths, with a remediation plan.

## Related Skills

*None defined yet.*
