---
name: support-readiness-confirmer
description: >
  This skill confirms the support team is ready for an upcoming release including knowledge of new features.
  Use when asked to verify agent preparedness, run readiness checks, or sign off on support go-live.
  Also consider when previous releases had high early-ticket volumes due to agent unpreparedness.
  Suggest after a readiness briefing has been delivered and before launch.
department: customer-support
agent: support-agent
version: 1.0.0
complexity: simple
related-skills: []
triggers:
  - "confirm support readiness"
  - "is support ready"
  - "support readiness check"
  - "readiness confirmation"
  - "verify support readiness"
---

# support-readiness-confirmer

## Agent: Support Agent

L2 support agent (Nx, multi-instance) responsible for ticket triage, support readiness confirmation, and help content review.

Department ethos: [ideal-customer-support.md](../../../../departments/customer-support/ideal-customer-support.md)

## Skill Description

The support readiness confirmer verifies that the support team has the knowledge, tooling, and documentation needed to handle customer inquiries related to an upcoming release before go-live approval is granted.

## When to Use

- When a readiness briefing has been delivered and the team needs formal confirmation that agents are prepared.
- When launch approval requires a support readiness sign-off as a gate.
- When previous releases showed high early-ticket escalation rates due to agent knowledge gaps.

## Workflow

1. **Define readiness criteria**: Establish what "ready" means for this release: briefing completed, runbooks updated, macros created, test tickets processed. Deliverable: readiness checklist.
2. **Assess agent knowledge**: Verify agents can describe the change, anticipated questions, and where to find resolution steps. Deliverable: knowledge assessment results.
3. **Verify tooling and content**: Confirm runbooks are updated, macros are deployed, and help articles reflect the release. Deliverable: tooling and content verification report.
4. **Issue readiness sign-off**: Provide a go/no-go recommendation to the launch coordinator based on assessment results. Deliverable: readiness sign-off document.

## Anti-Patterns

- **Rubber-stamping readiness**: Signing off without actually testing agent knowledge. *Why*: unverified readiness leads to the same problems as no readiness process at all.
- **Binary pass/fail without remediation**: Declaring "not ready" without specifying what is missing and how to fix it. *Why*: a no-go without actionable gaps blocks the launch without a path forward.

## Output

**On success**: A readiness sign-off document confirming agents have the knowledge, tooling, and documentation to handle the release, with a go recommendation for the launch coordinator.

**On failure**: Report which readiness criteria are unmet, what remediation steps are needed, and provide an estimated timeline to achieve readiness.

## Related Skills

- [`support-readiness-briefer-support`](../support-readiness-briefer-support/SKILL.md) -- delivers the briefing that this skill validates was absorbed.
- [`support-activation`](../../../customer-support/support-manager/support-activation/SKILL.md) -- activation builds the support function; readiness confirmation validates it before each release.
