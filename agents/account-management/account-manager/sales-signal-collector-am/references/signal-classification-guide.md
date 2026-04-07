# Account Signal Classification Guide

Reference for the `sales-signal-collector-am` skill.

---

## 1. Signal Type Taxonomy

| Signal Type | Definition | Example |
|-------------|-----------|---------|
| **Expansion Opportunity** | Customer says something that indicates readiness or intent to buy more | "We're planning to hire 20 more people this quarter" |
| **Churn Risk** | Customer says something suggesting they may not renew | "Our budget is being cut significantly next year" |
| **Competitive Threat** | Customer mentions an alternative product or vendor | "We're evaluating [Competitor] at the moment" |
| **Product Feedback** | Customer shares a reaction to the product — positive or negative | "The reporting feature doesn't give us what we need" |
| **Feature Request** | Customer asks for a specific capability | "Can you add an integration with [Tool]?" |
| **Relationship Health** | Signal about the quality of the human relationship | "I'm moving to a new role, let me introduce my replacement" |
| **Strategic Signal** | Information about the customer's business direction | "We're being acquired by [Company]" |
| **Advocacy Signal** | Customer expresses willingness to refer or advocate | "We'd be happy to be a reference customer" |

---

## 2. Signal Confidence Levels

| Confidence Level | Definition | How to Record |
|-----------------|-----------|--------------|
| **Confirmed** | Customer explicitly stated it; no interpretation needed | Direct quote if possible |
| **Inferred** | Reasonable conclusion from what was said; not explicit | Note the inference and the evidence |
| **Speculative** | Gut feeling or weak signal; needs confirmation | Flag as speculative; set a follow-up to validate |

---

## 3. Signal Urgency Indicators

Urgency determines how quickly the signal should escalate to the AM Lead:

| Urgency | Criteria | Action |
|---------|----------|--------|
| **Immediate (24h)** | Active churn risk expressed, competitor evaluation confirmed, M&A announced | Log immediately + notify AM Lead same day |
| **High (48h)** | Budget cut mentioned, key champion leaving, renewal at risk | Log within 24 hours + flag for AM Lead review |
| **Standard (1 week)** | Expansion signal, positive feedback, feature request | Log within 48 hours; surface at next 1:1 |
| **Informational** | Neutral update, general market context | Log within 1 week; no escalation needed |

---

## 4. Signal Collection Checklist

After every substantive customer interaction:

- [ ] Identify all signals from the conversation (do not filter — log everything)
- [ ] Classify each signal by type (from the taxonomy above)
- [ ] Assign a confidence level (confirmed / inferred / speculative)
- [ ] Assess urgency and flag if immediate or high
- [ ] Record the signal in the CRM within the required timeframe
- [ ] Link the signal to the correct account and contact record
- [ ] If urgent: notify AM Lead directly (don't wait for CRM review)

---

## 5. CRM Signal Entry Standards

Every signal log entry must include:

| Field | What to Record |
|-------|---------------|
| Account | Link to the correct CRM account |
| Contact | Specific person who said it |
| Signal Type | One of the 8 types from the taxonomy |
| Confidence | Confirmed / Inferred / Speculative |
| Source Interaction | Call / Email / QBR / Support Escalation / Event |
| Date | When the signal was received |
| Raw Note | What was actually said (as close to verbatim as possible) |
| Interpretation | What you believe this means for the account |
| Urgency Flag | Immediate / High / Standard / Informational |

---

## 6. Signal Patterns That Predict Account Risk or Growth

### Churn Risk Escalation Signals

| Pattern | Risk Level | Response |
|---------|-----------|---------|
| Budget cut + usage decline in same period | High | Immediate escalation to AM Lead |
| Champion departs + no successor introduced | High | Schedule introduction meeting within 2 weeks |
| 3+ feature requests unanswered over 6 months | Medium | Escalate to product team; acknowledge to customer |
| No login activity for 30+ days | Medium | CS check-in; surface to AM |
| Competitor mentioned twice in 90 days | High | Competitive intelligence brief; renewal risk review |

### Expansion Trigger Signals

| Signal | Expansion Type | Suggested Next Action |
|--------|--------------|----------------------|
| "We're growing headcount fast" | Seat expansion | Surface to AM Lead for opportunity framing |
| "Other teams are asking about this" | Cross-sell / seat expansion | Facilitate multi-stakeholder intro |
| "We're hitting limits on the current plan" | Upsell | Surface usage data; frame upgrade |
| "We renew next quarter" | Multi-year renewal | Proactive renewal motion 90 days out |
| "We'd recommend you to others" | Advocacy → referral pipeline | Activate referral program; introduce to community |

---

*Reference version 1.0 — Account Management / Account Manager*
