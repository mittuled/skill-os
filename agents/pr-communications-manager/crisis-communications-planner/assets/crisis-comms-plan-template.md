# Crisis Communications Plan

## Metadata
| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [PR Manager / Communications Lead] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Last Reviewed | [YYYY-MM-DD] |
| Next Review Due | [YYYY-MM-DD] |
| Skill | crisis-communications-planner |

---

## Executive Summary
[2-3 sentences: which scenario this plan covers, who it is designed to protect, and what the primary response objective is. GUIDANCE: Lead with the business impact, not the communications mechanics. Example: "This plan addresses a confirmed customer data breach affecting up to [N] accounts. The primary objective is to preserve customer trust by communicating transparently within 2 hours and outlining remediation steps within 24 hours."]

---

## 1. Crisis Scenario Matrix

| Scenario | Probability | Impact | Severity Tier | Response Owner |
|----------|------------|--------|--------------|----------------|
| [e.g., Customer data breach] | [H/M/L] | [H/M/L] | [1/2/3/4] | [Name / Role] |
| [e.g., Product outage >4 hours] | | | | |
| [e.g., Executive misconduct allegation] | | | | |
| [e.g., Regulatory inquiry] | | | | |
| [e.g., Mass layoffs leaked to press] | | | | |

GUIDANCE: List at minimum 5 scenarios. Tier 1 = Critical (30-min response window), Tier 2 = High (2-hour), Tier 3 = Moderate (4-hour), Tier 4 = Low (24-hour). Probability and Impact rated H/M/L.

---

## 2. Escalation Protocol

### Notification Chain

| Step | Trigger | Notifies | Method | Timeframe |
|------|---------|----------|--------|-----------|
| 1 | Crisis confirmed by [role] | PR Manager | Call + Slack | Immediate |
| 2 | Severity Tier 1 or 2 confirmed | CEO, Legal, Head of CS | Call | Within 15 min |
| 3 | Legal notified | Legal team | Secure email | Within 30 min |
| 4 | Response team assembled | All response team | Group call | Within 45 min |
| 5 | Statement approved | PR Manager confirms | Email + Slack | Before publish |

GUIDANCE: Adapt steps to company size. For Tier 3/4 events, steps 1 and 3 may be sufficient before response.

### Decision Authority

| Decision | Authority |
|----------|-----------|
| Issue holding statement | PR Manager (pre-approved templates) |
| Issue full press statement | PR Manager + Legal sign-off |
| Grant media interview | PR Manager + CEO approval |
| Activate dark site | PR Manager + Engineering on-call |
| Disclose to investors/board | CEO + CFO + Legal |
| Initiate regulatory notification | Legal + CEO |

---

## 3. Spokesperson Roster

| Scenario Category | Primary Spokesperson | Backup Spokesperson | Media Training Last Updated |
|-------------------|---------------------|--------------------|-----------------------------|
| Data / Security | [Name, Role] | [Name, Role] | [YYYY-MM-DD] |
| Product / Operations | [Name, Role] | [Name, Role] | [YYYY-MM-DD] |
| HR / Personnel | [Name, Role] | [Name, Role] | [YYYY-MM-DD] |
| Financial / Legal | [Name, Role] | [Name, Role] | [YYYY-MM-DD] |
| Executive / Strategic | [Name, Role] | [Name, Role] | [YYYY-MM-DD] |

GUIDANCE: All spokespersons should have completed media training within the last 12 months. Update immediately following any leadership change.

---

## 4. Messaging Template Library

### 4.1 Holding Statements

**Template A — Acknowledgement + Action (Tier 1/2 default)**
> We are aware of [describe situation]. We are taking immediate steps to [describe action]. We will provide an update by [specific time]. We apologise for any concern this has caused.

**Template B — Empathy + Investigation (Customer impact events)**
> We understand the impact this situation may have on [affected parties]. We are actively investigating [the cause / scope / details] and our team is working urgently to resolve it. Customer [safety / trust / data security] is our highest priority.

**Template C — Correction + Context (Factual inaccuracy in press)**
> A recent report in [outlet] contains inaccurate claims about [topic]. The facts are: [accurate statement]. We have contacted [outlet] to request a correction and are happy to provide documentation to any journalist covering this topic.

**Template D — No Comment (Legal hold)**
> We are aware of the situation. As this involves [legal proceedings / personnel matters], we are unable to provide further comment at this time. We will share information as it becomes appropriate to do so.

GUIDANCE: Fill in bracketed fields before issuing. Never issue a holding statement without legal review for Tier 1 or 2 events. Pre-approval by legal means reviewing the template at playbook creation time, not during the crisis.

---

### 4.2 Full Statement Structure

**[HEADLINE: One clear factual statement of what happened and the company's response]**

[Dateline — City, Date] — [Lead paragraph: the key facts in plain language. What happened, when, who is affected, what the company is doing about it. Max 3 sentences.]

[Second paragraph: additional context, scope of impact, and any customer or operational implications.]

[Executive quote: empathetic, action-oriented. Avoid corporate boilerplate. Example: "We take this seriously and our team has been working around the clock to address it."]

[What affected parties should do: specific action steps with links or contact information.]

[What happens next: timeline of updates and resolution steps.]

[Boilerplate: standard company description, 2-3 sentences.]

GUIDANCE: Full statements should be 300–500 words. Avoid passive voice. Avoid phrases like "we apologise for any inconvenience" — they minimise the impact.

---

### 4.3 Channel-Specific Versions

| Channel | Format | Length | Key Differences |
|---------|--------|--------|-----------------|
| Press wire / email | Full statement | 300–500 words | Full context; AP Style; includes boilerplate |
| Twitter / LinkedIn | Short acknowledgement | 280 chars / 2 sentences | Link to full statement; empathetic tone |
| Customer email | Direct communication | 200–350 words | Personal address; action steps prominent; no jargon |
| Employee Slack/email | Internal briefing | 250–400 words | Full context; what employees should/should not say |
| Investor update | Formal memo | 300–500 words | Business impact focus; mitigation plan; regulatory context |

---

## 5. Dark Site Configuration

| Element | Detail |
|---------|--------|
| URL | [e.g., incident.company.com or status.company.com] |
| Access credentials | Stored in [password manager / secure location] |
| Activation trigger | Any Tier 1 event, or at PR Manager discretion for Tier 2 |
| Update frequency | Every 2 hours during active Tier 1 event |
| Deactivation trigger | Issue fully resolved and post-incident report published |

GUIDANCE: The dark site should be pre-built, tested, and accessible without company VPN. Engineering on-call contact must be in the crisis contact list.

---

## 6. Crisis Contact Directory

| Role | Name | Mobile | Email | Backup Contact |
|------|------|--------|-------|----------------|
| PR Manager | | | | |
| CEO | | | | |
| General Counsel / Legal | | | | |
| Head of Engineering | | | | |
| Head of Customer Success | | | | |
| CFO | | | | |
| HR Lead | | | | |
| PR Agency (if retained) | | | | |
| Outside Counsel | | | | |

GUIDANCE: Store mobile numbers in a format accessible without corporate email or VPN — consider a printed copy in a secure location.

---

## 7. Tabletop Simulation Log

| Date | Scenario Tested | Participants | Gaps Identified | Remediation Actions | Status |
|------|----------------|--------------|-----------------|--------------------|----|
| [YYYY-MM-DD] | [Scenario] | [Names] | [Gap description] | [Action + Owner] | [Open/Closed] |

GUIDANCE: Conduct tabletop exercises at minimum annually. Run within 90 days of any real Tier 1 or 2 event. Tabletop findings must result in documented updates to this plan within 30 days.

---

## Appendices

### A. Methodology
Crisis scenarios identified through [process: stakeholder interviews, risk assessment workshop, industry benchmark review]. Severity tiers aligned to [RACE model / company-specific response framework — see references/framework.md]. Messaging templates reviewed by [Legal, CEO, HR] on [date].

### B. Version History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [YYYY-MM-DD] | [Name] | Initial creation |
