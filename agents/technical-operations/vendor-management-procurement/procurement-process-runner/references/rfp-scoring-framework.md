# RFP Scoring and Vendor Evaluation Framework

Reference for the `procurement-process-runner` skill.

---

## 1. Procurement Threshold Matrix

| Spend Category | Process Required | Approval Level |
|---------------|----------------|---------------|
| <$5,000/year | Self-service with manager approval | Direct manager |
| $5,000–$25,000/year | Lightweight evaluation (2+ quotes) | Department head |
| $25,000–$100,000/year | Formal RFP with 3+ vendors | COO |
| >$100,000/year | Full RFP with Legal review | CEO + board notification |
| Strategic / multi-year | Full RFP + external advisor | CEO + board approval |

---

## 2. Vendor Shortlisting Criteria

Before issuing an RFP, screen vendors against baseline requirements:

| Criterion | Disqualifying Condition |
|-----------|------------------------|
| Security certification | No SOC 2 Type II or equivalent for data-handling vendors |
| Financial stability | Company <12 months old or no verifiable customer base |
| Market presence | No verifiable customer references in the target industry |
| Data residency | Cannot meet regulatory data residency requirements |
| Integration compatibility | Cannot integrate with core systems via API or standard connector |

Minimum shortlist: 3 vendors. Maximum: 5 vendors (to keep evaluation manageable).

---

## 3. RFP Evaluation Scoring Matrix

Score each vendor response on a 1–5 scale per criterion. Multiply by weight.

| Criterion | Weight | Vendor A Score | Vendor A Weighted | Vendor B Score | Vendor B Weighted | Vendor C Score | Vendor C Weighted |
|-----------|--------|---------------|------------------|---------------|------------------|---------------|------------------|
| Functional fit | 30% | `/5` | | `/5` | | `/5` | |
| Security & compliance | 20% | `/5` | | `/5` | | `/5` | |
| Total cost of ownership | 20% | `/5` | | `/5` | | `/5` | |
| Implementation & support | 15% | `/5` | | `/5` | | `/5` | |
| Vendor stability | 10% | `/5` | | `/5` | | `/5` | |
| Integration capability | 5% | `/5` | | `/5` | | `/5` | |
| **Total** | 100% | | | | | | |

### Scoring Guide

| Score | Meaning |
|-------|---------|
| 5 | Exceeds requirements; best-in-class |
| 4 | Meets all requirements with notable strengths |
| 3 | Meets core requirements; some gaps |
| 2 | Partially meets requirements; significant gaps |
| 1 | Does not meet requirements |

---

## 4. Criterion Definitions

### Functional Fit (30%)
- Does the solution address 90%+ of documented requirements?
- Does the demo show the product working as described?
- Are missing features on a committed roadmap with dates?

### Security & Compliance (20%)
- SOC 2 Type II certification current?
- GDPR / data protection compliance (if applicable)?
- Penetration testing performed in last 12 months?
- Data encryption at rest and in transit?
- SSO / SAML support?
- Incident response and breach notification process documented?

### Total Cost of Ownership (20%)
Calculate over a 3-year period:
```
TCO = (Licence + Implementation + Training + Integration + Support) × 3 years
    + Migration cost (one-time)
    - Estimated efficiency savings
```

### Implementation & Support (15%)
- Time to deployment (standard): how many weeks?
- Dedicated implementation resources included?
- Support tier available (24/7 vs. business hours)?
- SLA for critical issue response?
- Customer success manager assigned?

### Vendor Stability (10%)
- Years in business
- Total funding raised or profitability
- Customer retention rate (ask directly or infer from references)
- Vendor concentration risk (is this vendor critical and replaceable?)

### Integration Capability (5%)
- REST API with comprehensive documentation?
- Native integration with existing stack?
- Webhooks or event streaming support?
- iPaaS connector available (Zapier, Make, Workato)?

---

## 5. Reference Check Questions

Ask each provided reference the same structured questions:

1. How long have you been using this vendor?
2. What specific use cases are you using the product for?
3. How was the implementation experience on a scale of 1–10? What went well? What didn't?
4. How responsive is the vendor's support team?
5. Have you experienced any significant outages or data issues?
6. Would you purchase this product again? Why or why not?
7. Is there anything you wish you'd known before signing?

---

## 6. Negotiation Leverage Factors

| Leverage Factor | How to Use |
|----------------|-----------|
| Competitive alternatives | Reference top-ranked alternatives by name; create urgency for the vendor |
| Utilisation commitments | Offer volume guarantee in exchange for per-unit price reduction |
| Multi-year term | Propose 2–3 year contract in exchange for 15–25% cost reduction |
| Prepayment | Annual prepay for 5–10% discount (evaluate cash flow impact) |
| Reference customer | Offer case study or reference call in exchange for discounted first year |
| Implementation inclusion | Request free or reduced implementation services bundled into contract |

---

*Reference version 1.0 — Technical Operations / Vendor Management & Procurement*
