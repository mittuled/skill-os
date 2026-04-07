# Vendor Contract Management Framework

Reference for the `vendor-contract-manager` skill.

---

## 1. Contract Lifecycle Stages

```
Negotiation → Execution → Obligation Tracking → Renewal Review → Renew / Renegotiate / Terminate
```

| Stage | Key Activities | Output |
|-------|--------------|--------|
| **Negotiation** | Red-line review, counter-proposals, SLA negotiation | Agreed term sheet / redlined contract |
| **Execution** | Signature collection, countersigning, filing | Fully executed contract on file |
| **Obligation Tracking** | Monitor payment, SLA compliance, key dates | Active obligation tracker |
| **Renewal Review** | Performance review, pricing comparison, decision | Renewal recommendation |
| **Renewal / Renegotiate** | Terms update, pricing negotiation | New executed agreement |
| **Termination** | Notice submission, data offboarding, final invoice | Termination confirmation |

---

## 2. Standard Contract Review Checklist

Before executing any vendor agreement, verify:

### Commercial Terms
- [ ] Total contract value and annual value clearly stated
- [ ] Payment terms specified (net-30, annual prepay, etc.)
- [ ] Price increase cap defined (e.g., CPI + 3% annual maximum)
- [ ] Discount and credit conditions documented
- [ ] Overage pricing defined if usage-based

### SLA and Performance
- [ ] Uptime SLA stated with minimum acceptable percentage
- [ ] Support response times by severity tier defined
- [ ] Service credit mechanism for SLA breaches included
- [ ] Escalation path for unresolved issues documented

### Data and Security
- [ ] Data ownership clearly assigned to the customer
- [ ] Data deletion timeline upon termination specified (e.g., 30 days)
- [ ] Subprocessor disclosure and consent requirements stated
- [ ] Security incident notification timeframe specified (e.g., 72 hours)
- [ ] Right-to-audit clause included (or waived with documented rationale)

### Legal Protections
- [ ] Limitation of liability capped at 12 months of fees or higher
- [ ] Mutual indemnification for IP infringement included
- [ ] Governing law and dispute resolution forum specified
- [ ] Termination for cause provisions defined
- [ ] Termination for convenience provisions defined (with notice period)
- [ ] Auto-renewal clause reviewed (acceptable notice period to cancel)

### Exit / Termination
- [ ] Termination notice period specified
- [ ] Transition assistance obligations defined
- [ ] Data export format and timeline agreed
- [ ] Post-termination obligations documented

---

## 3. Auto-Renewal Risk Matrix

| Renewal Notice Period | Risk Level | Recommended Action |
|----------------------|-----------|-------------------|
| >90 days | High | Set calendar reminder 120 days before renewal; initiate review |
| 60–90 days | Medium | Set calendar reminder 90 days before renewal |
| 30–60 days | Low | Set calendar reminder 60 days before renewal |
| <30 days | Critical | Flag at execution; negotiate to extend or remove auto-renewal |

---

## 4. Contract Key Dates Tracker

Every executed contract must have these dates logged in the contract management system:

| Date Type | Description | Alert Lead Time |
|-----------|-------------|----------------|
| Execution date | When the contract was signed | None |
| Effective date | When obligations begin | None |
| First invoice date | When first payment is due | 5 business days |
| Renewal date | When contract automatically renews | 90 days |
| Termination notice deadline | Latest date to send termination notice | 90 days + notice period |
| Contract expiry | When contract ends if not renewed | 90 days |
| Review date | Scheduled internal review | 90 days before renewal |

---

## 5. SLA Performance Tracking

### SLA Tiers for Vendor Agreements

| Tier | Uptime SLA | Critical Issue Response | Resolution |
|------|-----------|------------------------|-----------|
| **Enterprise** | 99.99% | 30 minutes | 4 hours |
| **Business** | 99.9% | 1 hour | 8 hours |
| **Standard** | 99.5% | 4 hours | 24 hours |
| **Basic** | 99.0% | 1 business day | 3 business days |

### Monthly SLA Calculation

```
Uptime % = ((Total minutes in period - Downtime minutes) / Total minutes in period) × 100

Example: 30 days = 43,200 minutes
If 65 minutes downtime: (43,200 - 65) / 43,200 × 100 = 99.85% uptime
```

### Service Credit Trigger

If vendor falls below contracted SLA, initiate credit claim:
1. Document downtime with timestamps from vendor status page or internal monitoring
2. Calculate credit owed per contract credit schedule
3. Submit credit request to vendor in writing within 30 days of the incident
4. Log credit applied to next invoice

---

## 6. Renewal Recommendation Framework

Review 90 days before renewal date:

| Assessment Area | Questions |
|----------------|-----------|
| **Value delivered** | Did the vendor deliver on the core use case? What measurable outcomes? |
| **SLA compliance** | How many SLA breaches occurred? Were credits applied? |
| **Support quality** | Ticket volume, resolution times, satisfaction of internal users |
| **Utilisation** | What % of licences/capacity are actively used? |
| **Market landscape** | Are better or cheaper alternatives available now? |
| **Relationship quality** | Is the vendor proactive, communicative, and responsive to feedback? |
| **Roadmap alignment** | Does the vendor's roadmap align with our needs for the next contract term? |

### Renewal Outcome Options

| Outcome | When to Choose | Action |
|---------|---------------|--------|
| **Renew same terms** | High value, fair price, no alternatives | Auto-renew or confirm |
| **Renegotiate** | Value delivered, but price or terms can be improved | Initiate renegotiation 90 days out |
| **Downsize** | Good product, but utilisation is low | Negotiate down to lower tier or fewer seats |
| **Terminate** | Poor value, better alternative exists, or low utilisation | Send notice per contract terms |
| **Replace** | Terminating; replacement vendor already selected | Coordinate termination with new vendor go-live |

---

*Reference version 1.0 — Technical Operations / Vendor Management & Procurement*
