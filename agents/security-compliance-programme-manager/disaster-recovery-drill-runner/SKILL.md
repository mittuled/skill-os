---
name: disaster-recovery-drill-runner
description: >
  This skill plans and runs disaster recovery drills to validate that recovery
  procedures work as documented. Use when asked to schedule a DR drill, test
  backup restoration, or validate RTO/RPO targets. Also consider when SOC 2
  or customer contracts require annual DR testing. Suggest when the user has
  DR procedures that have never been tested.
department: legal
agent: security-compliance-programme-manager
version: 1.0.0
complexity: medium
related-skills:
  - ../soc2-programme-manager/SKILL.md
  - ../security-awareness-training-runner/SKILL.md
---

# disaster-recovery-drill-runner

## Agent: Security & Compliance Programme Manager

L2 security and compliance programme manager (1x) responsible for SOC 2, security awareness training, disaster recovery, GDPR/CCPA compliance, and penetration test programme management.

Department ethos: [ideal-legal.md](../../../departments/legal/ideal-legal.md)

## Skill Description

Plans and executes disaster recovery drills to validate that backup restoration, failover procedures, and business continuity processes meet documented RTO and RPO targets under realistic conditions.

## When to Use

- When the annual DR testing schedule requires execution to maintain SOC 2 compliance or satisfy customer contractual commitments.
- When significant infrastructure changes (cloud migration, database upgrade, new backup provider) require validation of updated recovery procedures.
- When a near-miss incident reveals potential gaps in recovery capabilities that should be tested before a real disaster occurs.

## Workflow

1. **Drill Planning**: Define the drill scope (full failover vs. partial restoration vs. tabletop exercise), target systems, success criteria (RTO/RPO achievement), participants, and communication plan. Coordinate with engineering to select a drill window that minimizes production risk. Deliverable: drill plan document with scope, timeline, success criteria, and rollback procedures.
2. **Pre-Drill Validation**: Verify that backup systems are current, failover configurations are up to date, and all participants understand their roles. Confirm that monitoring and alerting will capture drill metrics. Deliverable: pre-drill readiness checklist with sign-off from each responsible team.
3. **Drill Execution**: Execute the drill according to the plan. Monitor backup restoration times, failover switchover duration, data integrity verification, and communication effectiveness. Document deviations from the plan and any issues encountered in real time. Deliverable: drill execution log with timestamped actions and observations.
4. **Results Analysis and Reporting**: Compare actual recovery times against RTO/RPO targets. Identify gaps where procedures failed, took longer than expected, or were unclear. Calculate actual vs. documented recovery metrics. Deliverable: DR drill results report with pass/fail per success criterion, gap analysis, and lessons learned.
5. **Remediation Tracking**: Create remediation items for each identified gap. Update DR procedures to reflect lessons learned. Schedule follow-up testing for any failed recovery scenarios. Deliverable: remediation action items with owners and deadlines, and updated DR procedures.

## Anti-Patterns

- **Tabletop-only testing**: Conducting only discussion-based exercises without actually restoring from backups or triggering failovers. *Why*: tabletop exercises validate process knowledge but not technical capability; untested backups are not backups.
- **Testing during off-hours with skeleton crew**: Running drills at 2 AM with a minimal team that does not reflect the actual on-call rotation and incident response staffing. *Why*: a drill should test the real response capability; optimistic staffing conditions produce optimistic results that do not hold during actual incidents.
- **Skipping post-drill remediation**: Documenting drill failures without following through on fixes and retesting. *Why*: an unfixed gap identified in a drill remains a gap; the drill's value is in driving improvement, not generating reports.

## Output

**On success**: Produces the DR drill results report containing execution log, RTO/RPO achievement metrics, gap analysis, lessons learned, updated DR procedures, and remediation action items. Delivered to the security team, engineering leadership, and compliance records.

**On failure**: Report which drill scenarios could not be executed (e.g., production freeze blocked failover test, backup system unavailable), what partial testing was completed, and when the drill will be rescheduled.

## Related Skills

- [`soc2-programme-manager`](../soc2-programme-manager/SKILL.md) -- SOC 2 requires evidence of regular DR testing; drill results are a key audit artifact.
- [`security-awareness-training-runner`](../security-awareness-training-runner/SKILL.md) -- DR drills test incident response communication which is reinforced through security awareness training.
