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

Department ethos: [ideal-legal.md](../../../../departments/legal/ideal-legal.md)

## Skill Description

Plans and executes disaster recovery drills to validate that backup restoration, failover procedures, and business continuity processes meet documented RTO and RPO targets under realistic conditions.

## When to Use

- When the annual DR testing schedule requires execution to maintain SOC 2 compliance or satisfy customer contractual commitments.
- When significant infrastructure changes (cloud migration, database upgrade, new backup provider) require validation of updated recovery procedures.
- When a near-miss incident reveals potential gaps in recovery capabilities that should be tested before a real disaster occurs.

## Workflow

1. **Drill Planning**: Define drill scope (full failover, partial restoration, or tabletop), target systems with per-system RTO/RPO targets, participants, communication plan, and rollback procedures. Coordinate drill window with engineering. Deliverable: drill plan document.
2. **Pre-Drill Validation**: Verify backups current, failover configurations up to date, participants briefed on roles. Confirm monitoring will capture drill metrics (restoration times, failover duration, data integrity). Deliverable: pre-drill readiness checklist with team sign-offs.
3. **Drill Execution**: Execute per plan. Capture timestamped actions: backup restoration, replica promotion, application reconnection, health check confirmation. Document all deviations and issues in real time. Deliverable: drill execution log.
4. **Scoring and Reporting**: Apply scoring rubric at `references/scoring-rubric.md` to evaluate drill quality across planning, realism, RTO/RPO achievement, and remediation. Produce report using template at `assets/dr-drill-report-template.md`. Compare actual vs. target metrics per system. Deliverable: scored DR drill results report per SOC 2 A1.3 and ISO 27001 A.17.1.3.
5. **Remediation Tracking**: Create remediation items for each gap with root cause analysis. Update DR procedures for lessons learned. Schedule follow-up drill to validate fixes. Deliverable: remediation action items with owners and deadlines.

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
