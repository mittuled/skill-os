---
name: uat-coordinator
description: >
  This skill coordinates user acceptance testing with design partners or beta customers.
  Use when a feature is functionally complete and needs real-user validation before general release.
  Also consider when a release targets a specific customer segment and their workflow must be verified.
  Suggest when engineering marks a feature as QA-passed but no external user has tested it.
department: product
agent: product-manager
version: 1.0.0
complexity: medium
related-skills: []
---

# uat-coordinator

## Agent: Product Manager
L2 product manager (multi-instance) responsible for customer discovery, requirements extraction, sprint planning, backlog management, and go-live approval. Bridges customer needs and engineering delivery.

Department ethos: [ideal-product.md](../../../departments/product/ideal-product.md)

## Skill Description
Coordinates user acceptance testing with design partners or beta customers.

## When to Use
- When a feature passes internal QA and needs validation from real users before general availability
- When a design partner has committed to testing a feature and the PM must orchestrate the logistics
- When a release changes a core workflow and the team needs confirmation that existing users can complete their tasks
- When go-live approval depends on documented UAT sign-off from at least one external participant

## Workflow
1. **Select participants and define scope**: Identify which design partners or beta customers match the target persona for the feature. Define the test scenarios, expected outcomes, and timeline. Deliverable: UAT plan listing participants, test scenarios with expected results, and schedule.
2. **Prepare the test environment**: Coordinate with engineering to provision a staging or sandbox environment with the feature enabled. Ensure test data is realistic and accounts are configured. Deliverable: environment-ready confirmation with access credentials shared to participants.
3. **Run the UAT sessions**: Guide participants through each test scenario. Capture their feedback, observed behaviour, blockers, and any deviations from expected outcomes. Record severity of each issue found. Deliverable: session log per participant with findings categorised by severity (critical / major / minor / cosmetic).
4. **Synthesise results and decide**: Aggregate findings across all participants. Determine whether the feature meets acceptance thresholds — no critical issues, no more than N major issues with documented workarounds. Deliverable: UAT summary report with pass/fail decision and issue list.
5. **Close the loop**: Share the UAT report with engineering and stakeholders. File tickets for issues found. Notify participants of the outcome and expected release timeline. Deliverable: tickets filed, participants thanked, and go-live recommendation issued.

## Anti-Patterns
- **Internal-only UAT**: Using only internal team members as UAT participants and calling it "user acceptance testing." *Why*: Internal testers carry product knowledge that real users lack, masking usability issues and workflow gaps.
- **Unstructured testing**: Asking participants to "play around with it" without defined scenarios or expected outcomes. *Why*: This produces anecdotal impressions rather than actionable, comparable data across participants.
- **Ignoring negative results**: Proceeding to release after UAT surfaces critical issues because the timeline is tight. *Why*: This ships known defects to a wider audience and damages trust with the design partners who flagged them.

## Output
**On success**: A UAT summary report containing participant feedback, categorised issue list, pass/fail decision, and a go-live recommendation — with all critical and major issues either resolved or documented with workarounds.
**On failure**: Report which UAT activities could not be completed (participant no-shows, environment issues, insufficient test coverage), what was attempted, and recommend next steps — such as rescheduling sessions, fixing environment blockers, or expanding the participant pool.

## Related Skills
- (none yet — cross-references added in Phase 1.6)
