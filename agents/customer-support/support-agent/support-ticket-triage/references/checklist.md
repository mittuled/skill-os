# Triage Checklist: support-ticket-triage

Use this checklist on every incoming ticket before routing.

## Step 1 — Read and Classify

- [ ] Read the full ticket body (not just the subject line)
- [ ] Identify the product area (e.g., billing, authentication, integrations, core product)
- [ ] Identify the issue type (bug report, how-to question, feature request, account issue)
- [ ] Identify the customer tier from the CRM (Free, Pro, Enterprise)
- [ ] Apply classification tags in Zendesk/Intercom

## Step 2 — Assign Severity

Use the severity matrix below. Assign the highest severity that applies.

| Priority | Criteria | First-Response SLA | Resolution SLA |
|----------|----------|--------------------|----------------|
| P0 | Full outage or data loss affecting the customer in production | 1 hour | 4 hours |
| P1 | Core feature broken, no workaround available | 4 hours | 8 hours |
| P2 | Degraded functionality, workaround exists | 8 hours | 24 hours |
| P3 | Question, cosmetic issue, feature request | 24 hours | 72 hours |

- [ ] Severity assigned (P0 / P1 / P2 / P3)
- [ ] P0 or P1: escalation path notified immediately

## Step 3 — Duplicate Check

- [ ] Search open tickets for the same error message or symptom
- [ ] Check the known issues board for matching incidents
- [ ] If duplicate found: link to parent ticket and close as duplicate with explanation to customer
- [ ] If known issue: link to status page or incident ticket; notify customer of status

## Step 4 — Route the Ticket

| Condition | Destination Queue |
|-----------|------------------|
| P0 / P1 — production incident | Escalation queue → on-call engineer notified |
| Billing or subscription issue | Billing specialist queue |
| API / integration technical issue | Technical support queue |
| General how-to question | Tier-1 queue |
| Enterprise customer, any priority | Named CSM notified in addition to queue |

- [ ] Ticket assigned to correct queue
- [ ] For P0/P1: on-call engineer paged (PagerDuty / Slack #incidents)

## Step 5 — Send Acknowledgement

- [ ] Acknowledgement message sent within SLA window (see Step 2 table)
- [ ] Message includes: ticket reference number, severity, expected first-response time
- [ ] Enterprise customers: personal acknowledgement from named CSM copied

## Quality Gate

Before marking triage complete, confirm:

- [ ] All five steps completed
- [ ] Severity matches the actual impact described in the ticket
- [ ] No duplicate ticket was created for an existing known issue
- [ ] SLA clock started from ticket creation timestamp, not triage completion
