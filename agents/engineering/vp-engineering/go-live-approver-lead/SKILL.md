---
name: go-live-approver-lead
description: >
  This skill provides final engineering leadership sign-off before production go-live. Use when
  asked to approve a release for production, give go/no-go for a launch, or validate release
  readiness at the VP level. Also consider when the tech lead go-live approval is complete and
  leadership sign-off is the remaining gate. Suggest when a release is being pushed to production
  without executive engineering review.
department: engineering
agent: vp-engineering
version: 1.0.0
complexity: medium
related-skills:
  - ../../../engineering/tech-lead-pr-reviewer/go-live-approver-eng/SKILL.md
  - ../../../engineering/vp-engineering/risk-register-builder-eng/SKILL.md
triggers:
  - "approve go-live as lead"
  - "VP go-live sign-off"
  - "exec launch approval"
  - "final go-live approval"
  - "lead release sign-off"
---

# go-live-approver-lead

## Agent: VP Engineering

L1 engineering leader (1x) responsible for spec intake review, team allocation, architecture oversight, velocity monitoring, and go-live approvals. Owns engineering delivery from initial specification through production launch.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Provides final engineering leadership sign-off before production go-live by validating readiness across quality, observability, security, and operational preparedness.

## When to Use

- When the tech lead has approved engineering readiness and VP-level sign-off is the final gate.
- When a high-severity release requires leadership review due to blast radius or customer impact.
- When a go-live has been previously blocked and the team is requesting re-evaluation after remediation.

## Workflow

1. **Review tech lead approval**: Confirm the tech lead go-live approval is complete and all action items are resolved. Deliverable: verified prerequisite checklist.
2. **Validate quality gates**: Verify test coverage meets thresholds, CI/CD pipeline is green, no P0/P1 bugs are open, and regression suite has passed. Deliverable: quality gate status report.
3. **Assess operational readiness**: Confirm runbooks exist, alerting is configured against SLOs, rollback procedure is documented and tested, and on-call rotation is staffed. Deliverable: operational readiness checklist.
4. **Review risk register**: Check the risk register for any open high-severity items. Verify mitigations are in place or accepted with documented rationale. Deliverable: risk acceptance memo.
5. **Render go/no-go decision**: Approve, conditionally approve (with required follow-ups), or block with explicit criteria that must be met. Deliverable: signed go-live decision with rationale. [GATE]

## Anti-Patterns

- **Ceremony without scrutiny**: Treating go-live approval as a formality rather than a genuine quality gate. *Why*: rubber-stamp approvals negate the purpose of the gate and allow preventable incidents.
- **Blocking without criteria**: Issuing a no-go without specifying what must change. *Why*: vague blocks stall delivery without giving the team a path to resolution.
- **Skipping operational checks**: Approving based on feature completeness while ignoring observability, rollback, and on-call readiness. *Why*: feature-complete does not mean production-ready; missing operational safeguards cause extended outages.

## Output

**On success**: Produces a go-live decision document containing the verdict (approved / conditionally approved / blocked), quality gate status, operational readiness status, risk acceptance notes, and any required post-launch follow-ups. Delivered to the release coordination channel.

**On failure**: Report which readiness criteria could not be verified, what information or artifacts are missing, and a concrete remediation path with estimated timeline.

## Related Skills

- [`go-live-approver-eng`](../../../engineering/tech-lead-pr-reviewer/go-live-approver-eng/SKILL.md) -- tech lead level approval that precedes this leadership sign-off.
- [`risk-register-builder-eng`](../../../engineering/vp-engineering/risk-register-builder-eng/SKILL.md) -- the risk register reviewed during go-live approval.
