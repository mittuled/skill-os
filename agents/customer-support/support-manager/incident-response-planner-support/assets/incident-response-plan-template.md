# Incident Response Plan

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Support Manager name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | incident-response-planner-support |
| Review Cadence | [Quarterly / After every S1 incident] |

## Executive Summary

[2-3 sentences describing this plan's scope, validation status, and any known gaps. Example: "This incident response plan covers S1–S4 severity levels with defined escalation paths confirmed with engineering and CS leadership. It was validated in a tabletop exercise on [date] with 2 gaps identified and remediated. The plan is effective immediately and will be reviewed quarterly or after any S1 incident."]

## Severity Matrix

[Copy from the framework; customise based on actual product and customer base.

GUIDANCE: Severity definitions should reference specific product features and customer impact levels that are meaningful to your business.]

| Severity | Definition | Customer Impact | Response SLA |
|----------|-----------|-----------------|-------------|
| S1 | [Custom definition] | [Specific impact] | Acknowledge: 15 min |
| S2 | [Custom definition] | [Specific impact] | Acknowledge: 30 min |
| S3 | [Custom definition] | [Specific impact] | Acknowledge: 1 hour |
| S4 | [Custom definition] | [Specific impact] | Acknowledge: 4 hours |

## Escalation Tree

[Named contacts, not just roles. Update when team changes.

GUIDANCE: Every name must have a backup. Contacts must be confirmed willing and available.]

| Severity | Primary Contact | Backup Contact | Notification Method | Response Expectation |
|----------|----------------|----------------|--------------------|--------------------|
| S1 | [Name, Role] | [Name, Role] | PagerDuty + Slack DM | Respond within 10 min |
| S2 | [Name, Role] | [Name, Role] | Slack #incidents + DM | Respond within 20 min |
| S3 | [Name, Role] | [Name, Role] | Slack #incidents | Respond within 1 hour |

## Communication Templates

[Pre-written templates for customer communication at each severity level.

GUIDANCE:
- Templates must be personalised at send time with incident-specific details
- Avoid specifying a resolution time you cannot guarantee
- Always include the status page link]

### S1 Initial Acknowledgement

> Subject: We're aware of an issue affecting [Product]
>
> We're currently investigating an issue that may be affecting your access to [Product]. Our team is working on this as a top priority.
>
> We'll provide an update within [30 minutes / 1 hour].
>
> Current status: [Status page URL]
>
> If you need immediate assistance, reply to this email.

### Status Update (all severities)

> Subject: Update: [Product] — [Brief description]
>
> **Status**: [Investigating / Identified — working on fix / Monitoring — fix deployed]
> **Impact**: [Description of what is affected]
> **Next update**: [Time]
>
> Status page: [URL]

### Resolution

> Subject: Resolved: [Product] — [Brief description]
>
> The issue affecting [feature/area] has been resolved as of [time].
>
> **What happened**: [Brief, non-technical explanation]
> **What we did**: [Fix applied]
> **What you may need to do**: [Any customer action required, or "No action required"]
>
> We're sorry for the disruption. If you continue to experience issues, please reply to this email.

## War-Room Protocol

[Step-by-step coordination procedure for S1 and S2 incidents.

GUIDANCE: Must include Slack channel names, conference bridge details, and the decision tree for escalation.]

1. Declare in #incidents: "[INCIDENT] S[1/2] — [Brief description] — [Your name] is incident commander"
2. Open bridge: [Conference call link or Slack huddle instructions]
3. Invite: [List of roles to invite]
4. Update status page within 15 minutes
5. Provide customer update within 30 minutes (S1) or 60 minutes (S2)
6. Update every 30 minutes until resolved (S1) or 60 minutes (S2)

## Post-Mortem Requirements

[What must be produced after every S1/S2 incident.

GUIDANCE: Post-mortem template link or outline; deadline is 48 hours after resolution.]

## Recommendations

[Gaps identified during plan creation or tabletop exercise, with owners and deadlines.
- P1 gaps: Must be resolved before this plan is considered active
- P2 gaps: Remediate within 30 days
- P3 gaps: Track in backlog]

## Appendices

### A. Tabletop Exercise Results

[Date, scenario used, participants, gaps identified, and resolution status.]

### B. Status Page Access

[Who has access to update the status page and how to add emergency access.]

### C. Engineering On-Call Schedule

[Link to current on-call rotation or PagerDuty schedule.]
