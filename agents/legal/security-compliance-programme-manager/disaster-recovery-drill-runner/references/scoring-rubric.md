# Scoring Rubric: disaster-recovery-drill-runner

Evaluates the quality and completeness of a disaster recovery drill covering planning, execution, results analysis, and remediation follow-through.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Drill Planning | 20% | Quality of drill scope, success criteria, participant coordination, and rollback procedures |
| 2 | Execution Realism | 25% | Whether the drill tested actual recovery capabilities under realistic conditions |
| 3 | RTO/RPO Achievement | 30% | Whether actual recovery times and data loss met documented targets |
| 4 | Remediation Follow-Through | 25% | Quality of gap identification, remediation tracking, and procedure updates |

| **Total** | | **100%** | |

## Scale

Each criterion is scored **0-10**:
- **0**: No evidence / completely absent
- **5**: Partially present with significant gaps
- **10**: Fully present, comprehensive, no gaps

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 – 10.0 | Exceptional | Full failover drill with realistic conditions, RTO/RPO targets met, all gaps remediated | Document for SOC 2 evidence, schedule next drill |
| A | 8.0 – 8.9 | Strong | Realistic drill, RTO/RPO mostly met, remediation plan in progress | Complete remediation, document for compliance |
| B | 7.0 – 7.9 | Good | Drill executed with some limitations, RTO/RPO partially met, gaps identified | Schedule follow-up drill after remediation |
| C | 5.0 – 6.9 | Adequate | Tabletop + partial technical drill, RTO/RPO targets exceeded for some systems | Remediate gaps and schedule full technical drill within 90 days |
| D | 3.0 – 4.9 | Weak | Tabletop only or drill with significant scope limitations, RTO/RPO not tested | Schedule full technical drill within 60 days |
| F | 0.0 – 2.9 | Failing | No meaningful DR testing performed | Urgent: plan and execute DR drill within 30 days |

## Signal Tables

### Drill Planning

| Score | Evidence |
|-------|----------|
| 9-10 | Drill plan covers full failover scope, success criteria defined for each target system (specific RTO/RPO per system), all participants briefed, rollback procedures documented and tested, communication plan established, monitoring configured to capture drill metrics |
| 7-8 | Drill plan covers primary systems, success criteria defined, participants briefed, rollback procedures documented |
| 5-6 | Drill plan exists but scope limited to partial systems, success criteria vague, not all participants briefed |
| 3-4 | Minimal planning document, scope unclear, participants not formally coordinated |
| 0-2 | No drill plan documented |

### Execution Realism

| Score | Evidence |
|-------|----------|
| 9-10 | Full production failover executed during business hours with actual on-call rotation, backup restoration from actual backups (not pre-staged), failover to actual DR site, real-time monitoring of application availability |
| 7-8 | Technical drill with actual backup restoration and failover, executed during planned window with full team |
| 5-6 | Partial technical drill (restore subset of systems from backup) combined with tabletop for remaining scenarios |
| 3-4 | Tabletop exercise only with walk-through of procedures, no actual restoration or failover |
| 0-2 | No drill execution or only a document review |

### RTO/RPO Achievement

| Score | Evidence |
|-------|----------|
| 9-10 | All target systems restored within documented RTO. Data loss within documented RPO for every system. Metrics captured with timestamps. Application availability verified post-recovery. |
| 7-8 | Primary systems met RTO/RPO targets, minor systems exceeded targets by <20% |
| 5-6 | Some systems met targets, others exceeded by significant margin, or RPO not independently verified |
| 3-4 | RTO/RPO tested for limited systems, most targets not met |
| 0-2 | RTO/RPO not measured during drill |

### Remediation Follow-Through

| Score | Evidence |
|-------|----------|
| 9-10 | Every gap documented with root cause analysis, remediation tickets created with owners and deadlines, DR procedures updated to reflect lessons learned, follow-up drill scheduled to validate fixes |
| 7-8 | Gaps documented with remediation tickets and owners, procedures updated |
| 5-6 | Gaps documented but remediation tickets lack owners or deadlines, procedures not yet updated |
| 3-4 | Gaps noted in drill report without formal remediation tracking |
| 0-2 | No gap analysis or remediation performed |
