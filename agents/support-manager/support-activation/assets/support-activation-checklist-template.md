# Support Activation Checklist

**Company**: [Company Name]
**Launch Date**: [YYYY-MM-DD]
**Support Manager**: [Name]
**Prepared By**: [Name]
**Last Updated**: [YYYY-MM-DD]

---

## Phase 1: Tooling Setup

### Support Platform
- [ ] Select support platform (Intercom / Zendesk / Freshdesk / HelpScout)
- [ ] Create workspace and configure company branding
- [ ] Set up email routing: `support@[company].com` → inbox
- [ ] Configure chat widget on product and marketing site
- [ ] Enable in-app messaging (if applicable)
- [ ] Test end-to-end message delivery

### Queue Configuration
- [ ] Create queues: `General`, `Billing`, `Technical`, `Enterprise`
- [ ] Define routing rules (keyword-based / tag-based / assignment groups)
- [ ] Set up round-robin or load-balanced assignment
- [ ] Configure out-of-hours auto-reply with expected response time
- [ ] Enable CSAT survey (send 24h after ticket resolution)

### Integrations
- [ ] Connect CRM (HubSpot / Salesforce) for customer context
- [ ] Connect Slack: alerts channel for new tickets + escalations
- [ ] Connect knowledge base platform (Notion / Confluence / Help Center)
- [ ] Connect error monitoring (Sentry / Datadog) for bug correlation
- [ ] Test all integrations end-to-end

---

## Phase 2: SLA Definition

| Tier | Criteria | First Response | Resolution Target |
|------|----------|---------------|-------------------|
| P0 — Critical | Service down, data loss, security incident | 30 min | 4 hours |
| P1 — High | Core feature broken, enterprise customer blocked | 2 hours | 8 hours |
| P2 — Medium | Feature degraded, workaround available | 8 hours | 48 hours |
| P3 — Low | General inquiry, feature request, feedback | 24 hours | 5 business days |

**SLA Clock**: Starts when ticket is received; pauses during waiting-for-customer status.

- [ ] SLA tiers documented and approved by leadership
- [ ] SLA rules configured in support platform
- [ ] SLA breach alerts routed to support manager Slack channel
- [ ] SLA reporting dashboard created

---

## Phase 3: Knowledge Base Readiness

### Required Articles at Launch
- [ ] Getting started guide
- [ ] Account setup and settings walkthrough
- [ ] Top 10 anticipated FAQs (sourced from beta feedback)
- [ ] Billing and subscription FAQ
- [ ] Troubleshooting: common error messages
- [ ] How to contact support (with expected response times)
- [ ] Escalation path for enterprise customers

### Article Quality Standards
- [ ] Each article reviewed by at least one team member outside support
- [ ] Screenshots captured from current production build
- [ ] Articles published and indexed in help center
- [ ] Search functionality tested with common query terms

---

## Phase 4: Team Readiness

### Agent Onboarding
- [ ] All agents have platform access and roles configured
- [ ] Product training completed (feature walkthroughs, known limitations)
- [ ] Triage protocol walkthrough completed
- [ ] Escalation path documented and role-played
- [ ] First response templates reviewed and approved
- [ ] Agents can locate relevant knowledge base articles for top 20 issue types

### Support Runbook
- [ ] Runbook created: [link to runbook]
- [ ] Escalation contacts documented (engineering, product, CS)
- [ ] On-call schedule set for first 30 days post-launch
- [ ] War room protocol defined for P0 incidents

---

## Phase 5: Metrics Baseline

### Tracking Setup
- [ ] CSAT tracking enabled (target: ≥ 4.2 / 5.0)
- [ ] First Contact Resolution (FCR) tracking enabled (target: ≥ 70%)
- [ ] Average First Response Time (FRT) dashboard configured
- [ ] Ticket volume by category dashboard configured
- [ ] Weekly metrics report template created

### Go / No-Go Criteria
All items below must be `PASS` before launch approval:

| Criterion | Target | Status |
|-----------|--------|--------|
| Support platform receiving test tickets | Functional | [ ] PASS / FAIL |
| SLA rules configured and tested | All tiers | [ ] PASS / FAIL |
| Knowledge base articles published | Min 10 articles | [ ] PASS / FAIL |
| All agents onboarded and trained | 100% of team | [ ] PASS / FAIL |
| Escalation path tested end-to-end | Smoke test passed | [ ] PASS / FAIL |
| CSAT survey triggering correctly | Verified in staging | [ ] PASS / FAIL |

---

## Sign-Off

| Role | Name | Approved | Date |
|------|------|----------|------|
| Support Manager | | [ ] | |
| Head of Customer Success | | [ ] | |
| CTO (for technical escalation path) | | [ ] | |
