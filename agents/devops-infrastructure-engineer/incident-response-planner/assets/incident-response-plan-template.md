# Incident Response Plan

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Agent role / human name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | incident-response-planner |
| Service / System | [Service name and owning team] |
| Last Tabletop Exercise | [YYYY-MM-DD or "Pending"] |

## Executive Summary

[2-3 sentences covering the scope of this plan, the services it covers, and any critical dependencies on other teams' processes.
GUIDANCE: Lead with the most important operational constraint. Example: "This plan covers the checkout service and its payment and inventory dependencies. SEV-1 response requires coordination with the payments team on-call within 15 minutes of detection. All escalation paths use PagerDuty schedules defined in [link]."]

## Severity Definitions

[Define severity levels with service-specific criteria.

GUIDANCE:
- Good: "SEV-1: Checkout API error rate > 5% for 5+ minutes, or any payment transaction failure, or full service unavailability for any region."
- Bad: "SEV-1: Major outage."
- Format: Table with service-specific numeric thresholds for each severity]

| Severity | Label | Service-Specific Criteria | Target Response | Target Resolve |
|----------|-------|--------------------------|----------------|---------------|
| SEV-1 | Critical | [Specific thresholds for this service] | 5 minutes | 1 hour |
| SEV-2 | High | [Specific thresholds for this service] | 15 minutes | 4 hours |
| SEV-3 | Medium | [Specific thresholds for this service] | 1 hour | 24 hours |
| SEV-4 | Low | [Specific thresholds for this service] | Next business day | Next sprint |

## Incident Roles

[Assign roles with backup contacts.

GUIDANCE: Name specific people or PagerDuty schedule names — not just "senior engineer". Include backup for each role.]

| Role | Primary | Backup | Contact |
|------|---------|--------|---------|
| Incident Commander | [Name / PagerDuty schedule] | [Name] | [PagerDuty link or Slack handle] |
| Technical Lead | [Name / PagerDuty schedule] | [Name] | [PagerDuty link or Slack handle] |
| Communicator | [Name / role title] | [Name] | [Slack handle] |
| Scribe | [Any available engineer] | — | #incidents channel |

## On-Call Schedule

[Reference the on-call rotation configuration.

GUIDANCE: Link to the actual schedule. Include rotation frequency and handoff process.]

- PagerDuty service: [service link]
- Rotation frequency: [weekly / bi-weekly]
- Handoff process: [Describe or link to on-call handoff procedure]
- Off-hours coverage: [describe or link]

## Escalation Paths

[Define timeout-based escalation for each severity.

GUIDANCE: All escalation must be timeout-triggered, not judgment-triggered. Include specific contact handles and time thresholds.]

### SEV-1 Escalation Chain

| Elapsed Time | Action | Contact |
|-------------|--------|---------|
| 0 min | Alert fires → PagerDuty pages on-call engineer | [PagerDuty service name] |
| 5 min | No acknowledgment | Auto-escalate to secondary on-call |
| 15 min | No resolution progress | Page Engineering Manager: [name / handle] |
| 30 min | Still unresolved | Page VP Engineering: [name / handle] |
| 60 min | Still unresolved | Notify CTO via [channel] |

### SEV-2 Escalation Chain

| Elapsed Time | Action | Contact |
|-------------|--------|---------|
| 0 min | Alert fires → PagerDuty pages on-call | [PagerDuty service name] |
| 15 min | No acknowledgment | Auto-escalate to secondary |
| 30 min | No resolution progress | Notify Engineering Manager |

## Response Procedures by Incident Category

[Document the triage steps for each incident category this service can experience.

GUIDANCE: Each category should have 3-5 triage steps with exact commands or dashboard links. Keep concise — detailed recovery steps belong in runbooks.]

### Category: Performance Degradation

1. Check SLO burn rate dashboard: [link]
2. Check recent deployments: [deployment dashboard link]
3. Check resource saturation: [CPU/memory dashboard link]
4. If deployment within last 2 hours: consult rollback plan at [link]
5. If no deployment: proceed to runbook: [runbook link]

### Category: Full Service Outage

1. Verify scope: is this single-region or multi-region? [health check URLs by region]
2. Check infrastructure status: [cloud provider status page link]
3. Check dependent services: [dependency health dashboard]
4. Declare SEV-1 immediately; notify stakeholders
5. Open war room: [video call link]

### Category: Data Integrity Issue

1. Halt all writes immediately — consult DBA before proceeding
2. Page DBA on-call: [contact]
3. Preserve logs and state — do not remediate before scoping
4. Escalate to VP Engineering within 5 minutes

### Category: Security Incident

1. **Do not attempt to remediate without security team** — page security on-call: [contact]
2. Preserve forensic evidence — do not restart affected instances
3. Isolate affected systems from network if breach is confirmed
4. Escalate to Security Lead and VP Engineering within 5 minutes

## Communication Templates

[Service-specific communication templates for each severity.

GUIDANCE: Pre-fill the service name and common impact descriptions so templates need minimal editing during an incident.]

### Initial Alert (SEV-1)

```
🔴 [SEV-1] INCIDENT: [Service Name] is experiencing [brief impact description].
Time detected: [HH:MM UTC]
IC: [Name]
Bridge: [Video call link]
Updates every 15 minutes in #incidents
```

### Status Update

```
📊 UPDATE [HH:MM UTC] — [Service Name]
Status: [Investigating / Mitigating / Monitoring]
Impact: [Current user impact]
Progress: [What has been tried / found]
Next update: [HH:MM UTC]
```

### Resolution

```
✅ RESOLVED [HH:MM UTC] — [Service Name]
Downtime: [X minutes]
Root cause: [1-sentence]
Post-mortem: [date] — [owner]
```

## Runbook Index

[Link all runbooks for this service so on-call engineers can find them during an incident.

GUIDANCE: Organize by alert name or incident category — not by runbook creation date.]

| Scenario | Runbook Link | Last Tested |
|----------|-------------|------------|
| [Alert name or scenario] | [Link] | [YYYY-MM-DD] |

## Tabletop Exercise Log

[Record all tabletop exercises and their outcomes.

GUIDANCE: Gaps found during tabletop exercises are high-priority actions. Track them to closure.]

| Date | Scenario | Participants | Gaps Found | Action Items |
|------|----------|-------------|------------|--------------|
| [YYYY-MM-DD] | [Scenario name] | [Names] | [Gaps identified] | [Actions with owners] |

## Recommendations

- **P1**: Run tabletop exercise with full on-call team before first production go-live
- **P2**: Configure PagerDuty timeout-based escalation rules matching this document
- **P3**: Review and update this plan within 48 hours of any SEV-1 or SEV-2 incident

## Appendices

### A. Service Architecture

[Brief description or diagram of the service, its key dependencies, and its SLOs.]

### B. Access Credentials for Incident Response

[Links to emergency access procedures, break-glass credentials, and DBA contacts. Do not store credentials here — link to the secure vault.]
