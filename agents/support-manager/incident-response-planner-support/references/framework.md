# Framework: Incident Response Planning

Defines the support team's incident response model, severity classification, escalation structure, and communication protocol for customer-impacting outages.

## Severity Classification

| Severity | Definition | Customer Impact | Examples |
|----------|-----------|-----------------|---------|
| S1 — Critical | Full product outage or data loss | All customers or all customers in a region; revenue-generating workflows blocked | Login broken for all users; data export producing corrupt files |
| S2 — High | Core feature unavailable, no workaround | Significant subset of customers; primary use case blocked | API returning 500 errors; integrations disconnected for all customers |
| S3 — Medium | Feature degraded with workaround | Some customers; primary use case slow or limited | Reporting lag > 30 min; bulk import timing out for large files |
| S4 — Low | Minor issue or edge case | Small subset; non-critical workflow affected | UI bug on non-default browser; export formatting issue |

## Response Time Targets

| Severity | Customer Acknowledgement | First Status Update | Escalation Notification | Resolution Target |
|----------|--------------------------|--------------------|-----------------------|-------------------|
| S1 | 15 minutes | 30 minutes | Immediate | 4 hours |
| S2 | 30 minutes | 1 hour | Within 30 minutes | 8 hours |
| S3 | 1 hour | 4 hours | If not resolved in 4h | 24 hours |
| S4 | 4 hours | 24 hours | Not required | 72 hours |

## Escalation Tree

| Severity | Primary Escalation | Secondary Escalation | Executive Notification |
|----------|-------------------|---------------------|------------------------|
| S1 | On-call engineer (PagerDuty) + Support Manager | VP Engineering + VP Customer Success | CEO, CTO within 30 minutes |
| S2 | On-call engineer + Support Manager | VP Engineering if not resolved in 2h | VP CS at 2h if not resolved |
| S3 | Engineering queue ticket (non-urgent) | Support Manager if not responded in 4h | None |
| S4 | Standard engineering backlog | None | None |

## War-Room Protocol

For S1 and S2 incidents:

1. **Declare incident**: Post in #incidents Slack channel with severity, description, and known customer impact
2. **Assign incident commander**: Support Manager or most senior available person owns coordination
3. **Open war room**: Create dedicated incident thread or conference call; invite engineering, CS, and support leads
4. **Communication cadence**: Customer status update every 30 minutes (S1) or 60 minutes (S2) until resolved
5. **Resolution**: Incident commander declares resolution; send final customer communication; schedule post-mortem within 48 hours

## Status Page Policy

| Event Type | Status Page Update Required | Timing |
|-----------|----------------------------|--------|
| S1 | Yes — "Investigating" → "Identified" → "Monitoring" → "Resolved" | Within 15 minutes of declaration |
| S2 | Yes — "Investigating" + updates | Within 30 minutes |
| S3 | Optional — at Support Manager discretion | If customer-facing for > 4h |
| S4 | No | N/A |

## Post-Mortem Requirements

Every S1 and S2 incident requires a post-mortem within 48 hours containing:
- Timeline of events (detection → declaration → resolution)
- Root cause
- Customer impact (number of customers, duration)
- What went well
- What went poorly
- Action items with owners and deadlines (prevent recurrence, improve detection, improve response)
