# Revenue Model Operationalisation — Subscription Pipeline

| Field | Value |
|---|---|
| Date | 2026-03-31 |
| Author | Revenue Operations |
| Model Type | Subscription |
| Recognition Method | Ratable |
| Pipeline Stages | 6 |
| Probability Progression Valid | Yes |
| Finance Validation Required | Yes |
| Skill | revenue-model-operationaliser |

## Revenue Model Summary

**Type:** Subscription — Recurring monthly/annual revenue; recognised ratably over contract term

**Recognition Method:** Ratable — Revenue spread evenly over contract period (e.g., $54K/year Enterprise = $4,500/month recognised)

---

## Pricing Tiers

| Tier | Monthly | Annual ARR | Seats |
|---|---|---|---|
| Starter | $500/mo | $5,400 | 5 |
| Growth | $1,500/mo | $16,200 | 20 |
| Enterprise | $5,000/mo | $54,000 | Unlimited |

---

## Pipeline Stage Definitions

| Stage | Probability | Forecast Category | Key Exit Criteria |
|---|---|---|---|
| Lead Qualified | 10% | Pipeline | Discovery call done; ICP confirmed |
| Discovery | 20% | Pipeline | Pain confirmed; champion identified |
| Technical Evaluation | 40% | Pipeline | Technical sign-off; no blocking objections |
| Proposal Sent | 60% | Best Case | Verbal agreement on pricing |
| Negotiation | 80% | Commit | Contract signed by all parties |
| Closed Won | 100% | Closed | N/A |

**Probability progression:** Valid — monotonically increasing from 10% to 100%.

---

## Required Deal Fields by Stage

| Stage | Required Fields |
|---|---|
| Lead Qualified | company_name, deal_owner, lead_source |
| Discovery | deal_value, close_date, product_line |
| Technical Evaluation | contract_term, seats_requested |
| Proposal Sent | proposed_arr, discount_pct |
| Negotiation | legal_review_status |
| Closed Won | signed_arr, subscription_start_date, billing_frequency |

---

## Finance Validation Required

Before going live, walk through these test scenarios with the finance team:

1. **Starter monthly**: $500 MRR × 12 = $6,000 annual — verify CRM shows $500/month recognised, not $6K upfront
2. **Enterprise annual prepaid**: $54,000 upfront → $4,500/month recognised — verify deferred revenue ledger entry
3. **Mid-contract upgrade**: Starter → Growth at Month 6 — verify CRM handles partial-period proration

Finance sign-off required before the subscription pipeline goes live.

---

## Notes

Separate pipeline from one-time implementation model. Finance requires subscription_start_date field for ratable recognition calculations. Do not merge subscription and implementation deals in the same pipeline — recognition methods differ.
