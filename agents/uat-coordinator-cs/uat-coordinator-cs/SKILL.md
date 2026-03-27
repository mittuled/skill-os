---
name: uat-coordinator-cs
description: >
  This skill coordinates user acceptance testing with customers including
  participant selection, session facilitation, and feedback synthesis. Use when
  asked to run UAT sessions, recruit test participants, or validate features
  with customers. Also consider when a release needs customer validation before
  GA. Suggest when the user ships features without customer acceptance testing.
department: customer-success
agent: uat-coordinator-cs
version: 1.0.0
complexity: medium
related-skills: []
---

# uat-coordinator-cs

## Agent: UAT Coordinator (CS)

L3 UAT coordinator within Customer Success (1x) responsible for coordinating user acceptance testing with customers.

Department ethos: [ideal-customer-success.md](../../../departments/customer-success/ideal-customer-success.md)

## Skill Description

Coordinates user acceptance testing with customers including participant selection, session facilitation, and feedback synthesis for product validation.

## When to Use

- When a product release needs customer validation before general availability.
- When a new feature requires real-world testing with actual customer workflows.
- When product or engineering requests structured customer feedback on a pre-release build.

## Workflow

1. **Define UAT Scope**: Work with product to define what is being tested, acceptance criteria, and the test scenarios customers should execute. Deliverable: UAT plan with scope, criteria, and scenarios.
2. **Select Participants**: Coordinate with CS Manager to select appropriate customer participants based on use case fit, technical readiness, and willingness. Deliverable: confirmed participant list with contact details.
3. **Prepare Environment**: Ensure the test environment is ready, participants have access, and test data is available. Provide participants with test guides and expectations. Deliverable: UAT environment with participant access and guides.
4. **Facilitate Sessions**: Run UAT sessions with participants. Guide them through test scenarios, observe their behavior, capture feedback in real time, and document issues encountered. Deliverable: session recordings and real-time notes.
5. **Synthesize and Report**: Aggregate feedback across all sessions. Classify issues by severity (blocker, major, minor, cosmetic). Produce a UAT report with go/no-go recommendation. Deliverable: UAT results report with issue list and recommendation.

## Anti-Patterns

- **Scripted-only testing**: Having participants follow scripts exactly without allowing exploratory testing. *Why*: scripted tests validate expected behavior but miss the unexpected interactions that reveal real usability issues.
- **UAT as demo**: Treating UAT sessions as product demonstrations rather than genuine testing. *Why*: demos collect impressions, not bugs; UAT must put features under stress with real customer workflows.
- **Ignoring UAT findings**: Collecting UAT feedback but proceeding with release regardless of critical findings. *Why*: UAT that does not influence release decisions is wasted customer time that damages trust.

## Output

**On success**: Produces a UAT results report containing session findings, classified issue list, participant feedback, and go/no-go recommendation. Delivered to product, engineering, and the CS Manager.

**On failure**: Report which UAT components could not be completed (insufficient participants, environment issues), what partial testing was accomplished, and what is needed to complete validation.

## Related Skills

- [`cohort-selector-cs`](../../cs-manager/cohort-selector-cs/SKILL.md) -- Cohort selection provides the participant pool for UAT.
- [`cs-release-readiness`](../../cs-manager/cs-release-readiness/SKILL.md) -- UAT results feed into release readiness decisions.
- [`user-feedback-synthesiser-cs`](../../customer-success-manager/user-feedback-synthesiser-cs/SKILL.md) -- UAT feedback contributes to broader feedback synthesis.
