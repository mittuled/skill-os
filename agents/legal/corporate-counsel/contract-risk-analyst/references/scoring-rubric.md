# Scoring Rubric: contract-risk-analyst

Evaluates individual contract clauses across four risk dimensions to quantify clause-level risk exposure.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Financial Exposure | 30% | Degree to which the clause creates direct or contingent financial liability, cost uncertainty, or payment risk for the company |
| 2 | Legal Liability | 30% | Extent to which the clause expands the company's legal obligations, litigation exposure, or regulatory liability |
| 3 | Operational Burden | 20% | Level of operational effort, process changes, or resource commitment required to comply with the clause |
| 4 | Compliance Risk | 20% | Degree to which the clause creates regulatory compliance obligations or conflicts with existing compliance frameworks |
| **Total** | | **100%** | |

## Scale

Each criterion is scored **0-10**:
- **0**: No evidence / completely absent
- **5**: Partially present with significant gaps
- **10**: Fully present, comprehensive, no gaps

Note: For risk scoring, **10 = lowest risk** (most favorable to the company) and **0 = highest risk** (most unfavorable).

**Composite Score** = Σ (criterion score x weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 - 10.0 | Minimal Risk | Clause fully protects company interests with no material exposure | Accept as-is |
| A | 8.0 - 8.9 | Low Risk | Clause provides strong protections with minor gaps that do not create material exposure | Accept with optional improvements noted |
| B | 7.0 - 7.9 | Moderate Risk | Clause provides adequate protection but contains terms that could be more favorable | Flag for negotiation if deal size warrants |
| C | 5.0 - 6.9 | Elevated Risk | Clause contains terms that create measurable exposure or impose significant obligations | Negotiate specific changes before signing |
| D | 3.0 - 4.9 | High Risk | Clause creates substantial liability, operational burden, or compliance gaps | Require revision; escalate to General Counsel |
| F | 0.0 - 2.9 | Critical Risk | Clause creates unacceptable exposure that could threaten business operations or financial stability | Block signing until clause is rewritten or removed |

## Signal Tables

### Financial Exposure

| Score | Evidence |
|-------|----------|
| 9-10 | No financial exposure beyond agreed fees, capped liability proportional to contract value, favorable payment terms (net-60+), no penalty clauses, audit rights for variable charges |
| 7-8 | Financial exposure limited and quantifiable, liability capped at contract value, standard payment terms (net-30), minor penalty provisions with reasonable triggers |
| 5-6 | Financial exposure present but bounded, liability cap at 2x contract value, prepayment required for some components, moderate penalty clauses |
| 3-4 | Significant financial exposure, liability cap missing for some categories, unfavorable payment terms, penalty clauses with broad triggers, auto-renewal with price escalation |
| 0-2 | Unlimited financial exposure, no liability cap, penalty clauses with automatic triggers, full prepayment with no refund rights, uncapped price escalation, personal guarantees required |

### Legal Liability

| Score | Evidence |
|-------|----------|
| 9-10 | Mutual and balanced obligations, liability limited to direct damages, bilateral indemnification with standard carve-outs, clear dispute resolution with favorable venue, no waiver of rights |
| 7-8 | Mostly balanced obligations with minor asymmetry, liability includes limited consequential damages carve-outs, indemnification slightly favors counterparty on 1-2 items |
| 5-6 | Noticeable obligation asymmetry, consequential damages exposure in some categories, indemnification tilted toward counterparty, arbitration in neutral venue |
| 3-4 | Significant obligation imbalance, broad consequential damages exposure, one-sided indemnification, unfavorable dispute venue, representations that are difficult to verify |
| 0-2 | Fully one-sided obligations, unlimited consequential damages, indemnification only from company to counterparty, mandatory arbitration in counterparty's home jurisdiction, broad representations and warranties |

### Operational Burden

| Score | Evidence |
|-------|----------|
| 9-10 | No additional operational requirements beyond standard business practices, flexible compliance timelines, change management process is bilateral |
| 7-8 | Minor additional operational requirements (e.g., periodic reporting), reasonable compliance timelines (30+ days), standard change management |
| 5-6 | Moderate operational requirements (new processes or tools needed), tight but achievable timelines (14-30 days), change management favors counterparty |
| 3-4 | Significant operational requirements (dedicated resources, system changes), aggressive timelines (under 14 days), unilateral change rights for counterparty |
| 0-2 | Extensive operational overhaul required, immediate compliance deadlines, counterparty can unilaterally change requirements, audit obligations with unrestricted scope and frequency |

### Compliance Risk

| Score | Evidence |
|-------|----------|
| 9-10 | Clause aligns with existing compliance frameworks (GDPR, SOC 2, etc.), no new regulatory obligations created, counterparty shares compliance burden |
| 7-8 | Minor additional compliance requirements that align with planned initiatives, counterparty provides reasonable compliance support |
| 5-6 | Creates new compliance obligations requiring policy updates or process changes, timeframe achievable but requires planning |
| 3-4 | Creates compliance obligations that may conflict with existing frameworks, requires significant investment to achieve, potential regulatory exposure during transition |
| 0-2 | Creates compliance obligations that directly conflict with existing regulations (e.g., data localization requirements incompatible with current architecture), impossible to fully comply without fundamental business changes |
