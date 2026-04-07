# Framework: Incident Response Planner

Defines severity levels, role assignments, escalation paths, and communication cadence for production incident response.

## Severity Level Definitions

| Level | Label | Criteria | Target Response Time | Target Resolution Time |
|-------|-------|----------|---------------------|----------------------|
| SEV-1 | Critical | Full service outage; data loss; security breach affecting users; revenue-blocking failure | 5 minutes | 1 hour |
| SEV-2 | High | Significant degradation (> 10% error rate or > 2× SLO latency); subset of users impacted | 15 minutes | 4 hours |
| SEV-3 | Medium | Minor degradation; no user-visible impact; approaching SLO threshold | 1 hour | 24 hours |
| SEV-4 | Low | Cosmetic issue; non-functional bug; no performance impact | Next business day | Next sprint |

## Incident Roles

| Role | Responsibilities | Assigned To |
|------|-----------------|-------------|
| Incident Commander | Owns the incident; coordinates all responders; makes final decisions; declares resolution | On-call senior engineer or manager |
| Technical Lead | Investigates root cause; executes fixes; owns technical decisions | Subject matter expert for affected system |
| Communicator | Manages stakeholder communication; writes status page updates; sends internal briefings | Product or engineering manager |
| Scribe | Documents the timeline in real time; captures decisions, actions, and findings | Any available engineer |

For SEV-3 and SEV-4, the incident commander and technical lead may be the same person.

## Escalation Path (Timeout-Based)

Escalation must be automated or triggered by timeout — do not rely on human memory.

| Time Since Detection | SEV-1 Action | SEV-2 Action |
|---------------------|-------------|-------------|
| 0 minutes | Page on-call engineer via PagerDuty | Page on-call engineer |
| 5 minutes (SEV-1) / 15 minutes (SEV-2) | No response → auto-escalate to secondary on-call | No response → escalate to secondary |
| 15 minutes (SEV-1) / 30 minutes (SEV-2) | Still unresolved → page Engineering Manager | Still unresolved → notify Engineering Manager |
| 30 minutes (SEV-1) | Still unresolved → page VP Engineering | — |
| 60 minutes (SEV-1) | Still unresolved → CEO / CTO briefing | — |

## Communication Cadence

| Audience | Format | Frequency | Channel |
|----------|--------|-----------|---------|
| Engineering team | Slack update with current status | Every 15 minutes (SEV-1), 30 min (SEV-2) | #incidents channel |
| Customer-facing teams | Summary of user impact and ETA | Every 30 minutes (SEV-1) | #customer-impact |
| External customers | Status page update | On detection, every 30 min, on resolution | status.company.com |
| Executive team | Briefing note | On detection and resolution (SEV-1) | Direct message or email |

## Communication Templates

### Initial Detection Template

```
🔴 [SEV-1] INCIDENT DECLARED — [Service Name]
Time: [HH:MM UTC]
Impact: [User-visible impact description]
Incident Commander: [Name]
Bridge: [Link to video call or war room]
Ticket: [Incident management link]
Next update: [HH:MM UTC]
```

### Status Update Template

```
📊 INCIDENT UPDATE — [Service Name] — [Time UTC]
Status: Investigating / Mitigating / Monitoring
Current impact: [Current user impact]
Last action taken: [What was done]
Next action: [What is being tried]
ETA to resolution: [Time or "Unknown"]
```

### Resolution Template

```
✅ INCIDENT RESOLVED — [Service Name]
Resolved at: [HH:MM UTC]
Duration: [X hours Y minutes]
Root cause: [1-sentence description]
Actions taken: [Bullet list]
Post-mortem: Scheduled for [date/time]
```

## Post-Incident Review (PIR) Requirements

| Severity | PIR Required | Deadline | Format |
|----------|-------------|----------|--------|
| SEV-1 | Yes — mandatory | Within 48 hours | Full blameless post-mortem |
| SEV-2 | Yes | Within 1 week | Abbreviated post-mortem |
| SEV-3 | Optional | Within 2 weeks | Short incident summary |
| SEV-4 | No | — | Bug ticket sufficient |

### Post-Mortem Structure

1. **Incident summary** — What happened, when, impact
2. **Timeline** — Minute-by-minute sequence of events
3. **Root cause analysis** — 5 Whys or fault tree
4. **Contributing factors** — System, process, and human factors
5. **Action items** — Specific, assigned, time-bounded preventive measures
6. **What went well** — Detection, response, or mitigation steps that worked

## Tabletop Exercise Protocol

Before going live, run a tabletop exercise with the team:

1. Present a realistic failure scenario without revealing the answer
2. Walk through the incident response plan step-by-step
3. Note any steps where the team hesitates, disagrees, or cannot find the referenced resource
4. Record gaps and update the plan before the next sprint
5. Target: all P1 runbooks exercised before first production deployment
