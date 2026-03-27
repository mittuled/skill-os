---
name: go-live-approver-eng
description: >
  This skill approves engineering readiness for go-live at the tech lead level. Use when asked
  to sign off on a release, verify engineering readiness, or approve a production deployment.
  Also consider when a release is being pushed without a formal readiness check. Suggest when
  the team is approaching a go-live date without documented approval criteria.
department: engineering
agent: tech-lead-pr-reviewer
version: 1.0.0
complexity: medium
related-skills:
  - ../../tech-lead-pr-reviewer/ga-rollout-executor-planner/SKILL.md
  - ../../tech-lead-pr-reviewer/sprint-reviewer-eng/SKILL.md
---

# go-live-approver-eng

## Agent: Tech Lead / PR Reviewer

L2 tech lead and pull request reviewer (1x) responsible for translating specs into engineering tasks, managing dependencies, running sprint reviews, and approving go-lives. Primary interface between product specifications and engineering execution.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)

## Skill Description

Approves engineering readiness for go-live by verifying that all acceptance criteria, test coverage, performance benchmarks, and operational prerequisites are met.

## When to Use

- When a feature or release has completed development and QA, and needs a formal engineering sign-off before production deployment.
- When the go-live date is approaching and stakeholders need a clear yes/no from the tech lead on engineering readiness.
- When a previous go-live was rejected and the team has addressed the blocking issues, requiring re-evaluation.

## Workflow

1. **Review acceptance criteria**: Verify that every ticket in the release has its acceptance criteria marked as met, with evidence (tests passing, screenshots, or demo recordings). Deliverable: acceptance criteria checklist.
2. **Verify test coverage**: Confirm unit, integration, and regression test suites pass. Check that critical paths have end-to-end test coverage. Deliverable: test coverage report.
3. **Validate operational readiness**: Confirm monitoring dashboards, alerts, runbooks, and rollback procedures are in place and tested. Deliverable: operational readiness checklist.
4. **Assess outstanding risks**: Review any known issues, tech debt, or deferred items. Determine whether they are acceptable for go-live or blocking. Deliverable: risk assessment with disposition.
5. **Render decision**: Issue a go/no-go decision with clear rationale. If no-go, specify exactly what must be resolved and the timeline for re-evaluation. Deliverable: signed go-live approval or rejection with action items.

## Anti-Patterns

- **Rubber-stamp approval**: Approving go-live without actually reviewing test results, coverage, or operational readiness. *Why*: skipping verification transfers risk from pre-launch to production, where the cost of failure is orders of magnitude higher.
- **Moving goalposts**: Changing approval criteria during the review to accommodate incomplete work. *Why*: weakening criteria under schedule pressure normalizes shipping unfinished work and erodes release quality over time.
- **Approval without rollback verification**: Signing off without confirming that rollback procedures exist and have been tested. *Why*: go-live without a tested rollback plan means any production issue becomes an unrecoverable incident.

## Output

**On success**: Produces a signed go-live approval document containing the acceptance criteria checklist, test coverage report, operational readiness checklist, and risk assessment. Delivered to engineering leadership and the release coordinator.

**On failure**: Report the specific blocking issues preventing approval, what must be resolved, the timeline for re-evaluation, and any interim mitigations available.

## Related Skills

- [`ga-rollout-executor-planner`](../../tech-lead-pr-reviewer/ga-rollout-executor-planner/SKILL.md) -- the GA rollout plan is executed only after go-live approval is granted.
- [`sprint-reviewer-eng`](../../tech-lead-pr-reviewer/sprint-reviewer-eng/SKILL.md) -- sprint reviews provide the evidence of completed work that go-live approval evaluates.
