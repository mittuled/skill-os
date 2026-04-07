# First Sales Process — Mid-Market Motion v1.0

| Field | Value |
|---|---|
| Date | 2026-03-31 |
| Author | Sales Manager |
| Motion Type | Mid-Market |
| Qualification Framework | MEDDIC |
| Pipeline Stages | 6 |
| Stage Count Valid | Yes (6 within 5-7 range) |
| Skill | first-sales-process-builder |

## Validation

**Stage count:** 6 — within recommended 5-7 range for mid-market motion.

**Seller-centric stages detected:** None — all stages are buyer-milestone oriented.

**Handoff protocols:** Complete — SDR→AE, AE→SE, AE→CS all defined.

**Missing handoffs:** None.

---

## Pipeline Stage Definitions

| # | Stage | Entry Criterion | Exit Criterion | Probability | Target Days |
|---|---|---|---|---|---|
| 1 | Lead Qualified | BANT/MEDDIC ≥ 6.0 or inbound demo | Discovery call scheduled; pain acknowledged | 10% | 3 |
| 2 | Discovery | Discovery call completed | Pain quantified; economic buyer identified | 20% | 7 |
| 3 | Technical Evaluation | Discovery complete; AE confirmed fit | Technical sign-off; no blocking objections | 40% | 14 |
| 4 | Proposal | Technical sign-off; pricing approved | Verbal agreement from economic buyer | 65% | 10 |
| 5 | Negotiation | Verbal agreement; legal initiated | Contract signed | 85% | 14 |
| 6 | Closed Won | Contract signed | N/A — CS handoff triggered | 100% | 1 |

**Total average deal cycle (Discovery to Close):** 46 days

---

## Qualification Gates by Stage

| Stage | Required Before Advancement |
|---|---|
| Lead Qualified | ICP fit confirmed, champion/decision-maker identified |
| Discovery | Pain quantified, decision timeline confirmed |
| Technical Evaluation | Decision criteria confirmed, champion active |
| Proposal | Economic buyer engaged, decision process mapped, timeline confirmed |
| Negotiation | Procurement requirements met, legal review complete |

---

## Handoff Protocols

**SDR → AE:** SDR books discovery; transfers BANT notes, company research, and stakeholder map to AE in CRM before meeting.

**AE → SE:** AE completes discovery; creates SE brief with use case, technical requirements, and integration needs.

**AE → CS:** AE creates CS handoff note: deal context, champion contact, use case, success metrics, and known risks.

---

## CRM Configuration Requirements

**Required deal fields:** deal_value, close_date, lead_source, product_line, deal_owner, contract_term, champion_name

**Automation rules:**
1. Stage transition → notify AE manager
2. Close date T-7 days → overdue deal alert
3. Closed Won → create CS onboarding task

---

## 90-Day Rollout Plan

| Phase | Duration | Description |
|---|---|---|
| Pilot | Weeks 1-4 | 2 senior AEs run process; weekly 30-min review |
| Feedback loop | Weekly | Collect friction points; iterate stage definitions |
| Full rollout | Week 5 | All AEs onboarded; process documentation published |
| Review | Week 13 | 90-day retrospective; update based on conversion data |

**Success metrics:** 80%+ CRM stage compliance by Week 8; deal cycle variance <20% vs. targets by Week 12.
