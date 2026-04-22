---
name: support-activation
description: >
  This skill activates the support function before launch including tooling setup, queue configuration,
  and team readiness. Use when asked to stand up customer support, configure support tooling, or prepare
  the support team for go-live. Also consider when transitioning from founder-led support to a dedicated function.
  Suggest when launch is approaching and no support infrastructure exists.
department: customer-support
agent: support-manager
version: 1.0.0
complexity: medium
related-skills:
  - support-runbook-builder
  - incident-response-planner-support
  - help-centre-builder-support
triggers:
  - "activate support"
  - "support activation"
  - "launch support function"
  - "set up support team"
  - "support team activation"
---

# support-activation

## Agent: Support Manager

L1 support manager (1x) reporting to the COO, responsible for support runbooks, help centre, incident response planning, and support activation. Owns queue management, SLA adherence, and support tooling.

Department ethos: [ideal-customer-support.md](../../../../departments/customer-support/ideal-customer-support.md)

## Skill Description

The support activation skill stands up the entire customer support function from scratch, including tooling selection, queue configuration, SLA definition, and team readiness verification so the organisation can handle customer inquiries from day one of launch.

## When to Use

- When the product is approaching its first public launch and no customer support infrastructure exists.
- When the company transitions from founder-led support to a dedicated support function.
- When a new product line requires a separate support queue with distinct SLAs and routing.
- When a post-mortem or audit reveals that the existing support setup has fundamental gaps in tooling or process.

## Workflow

1. **Select and configure tooling**: Evaluate and configure the support platform (ticketing, live chat, phone) based on expected volume and channel mix. Deliverable: configured support platform.
2. **Define queues and routing**: Create ticket queues with routing rules based on product area, customer tier, and issue type. Deliverable: queue configuration document.
3. **Set SLAs**: Define first-response and resolution SLAs by ticket priority and customer tier. Deliverable: SLA policy document.
4. **Build initial macros and templates**: Create response templates for anticipated common scenarios. Deliverable: macro library.
5. **Verify team readiness**: Confirm agents have product knowledge, tooling access, and completed onboarding. Deliverable: readiness checklist with sign-off.
6. **Run a dry run**: Process test tickets through the full workflow to validate routing, SLAs, and escalation paths. Deliverable: dry-run report with issues found and resolved.
7. **Go live**: Enable customer-facing channels and begin monitoring queue health. Deliverable: live support function with real-time dashboard.

## Anti-Patterns

- **Launching without a dry run**: Going live without processing test tickets through the system. *Why*: routing errors and misconfigured SLAs surface as customer-facing failures during the highest-pressure period.
- **Over-engineering queues**: Creating complex routing rules for a small team with low volume. *Why*: unnecessary complexity slows response time and confuses agents when simple round-robin would suffice.
- **Skipping SLA definition**: Launching support without explicit SLA targets. *Why*: without targets, there is no way to measure performance or identify when the function is under-resourced.

## Output

**On success**: A fully operational support function with configured tooling, defined queues and SLAs, a macro library, verified team readiness, and a dry-run report confirming end-to-end workflow.

**On failure**: Report which components are not ready (e.g., tooling not configured, agents not onboarded), what was completed, and provide a remediation timeline for each gap.

## Related Skills

- [`support-runbook-builder`](../support-runbook-builder/SKILL.md) -- runbooks provide the operational procedures agents follow once support is activated.
- [`incident-response-planner-support`](../incident-response-planner-support/SKILL.md) -- incident response planning complements activation by covering crisis scenarios.
- [`help-centre-builder-support`](../help-centre-builder-support/SKILL.md) -- the help centre reduces ticket volume by enabling self-service alongside the support function.
