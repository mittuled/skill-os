# Scoring Rubric: contract-review-orchestrator

Evaluates the overall safety and favorability of a contract from the company's perspective using five weighted criteria.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Liability Exposure | 25% | Degree to which the contract limits the company's financial and legal liability through caps, carve-outs, and indemnification balance |
| 2 | IP Protection | 20% | Strength of intellectual property protections including ownership, licensing scope, non-compete/non-solicit, and trade secret safeguards |
| 3 | Termination Rights | 20% | Favorability of termination provisions including for-cause triggers, convenience rights, cure periods, and post-termination obligations |
| 4 | Data & Privacy | 20% | Adequacy of data protection provisions including processing restrictions, breach notification, sub-processor controls, and regulatory compliance |
| 5 | Financial Terms | 15% | Clarity and favorability of payment terms, pricing mechanisms, audit rights, and financial risk allocation |
| **Total** | | **100%** | |

## Scale

Each criterion is scored **0-10**:
- **0**: No evidence / completely absent
- **5**: Partially present with significant gaps
- **10**: Fully present, comprehensive, no gaps

**Composite Score** = Σ (criterion score x weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 - 10.0 | Safe to Sign | All protections present, terms favor or equally balance the company's position | Approve with minor cosmetic edits only |
| A | 8.0 - 8.9 | Low Risk | Strong protections with minor gaps that do not materially increase exposure | Approve with noted should-change items |
| B | 7.0 - 7.9 | Moderate Risk | Adequate protections but several clauses deviate from standard terms | Negotiate should-change items before signing |
| C | 5.0 - 6.9 | Elevated Risk | Multiple material gaps or unfavorable terms that increase company exposure | Negotiate must-change items; escalate to General Counsel |
| D | 3.0 - 4.9 | High Risk | Significant liability exposure, missing critical protections, or heavily one-sided terms | Do not sign without substantial renegotiation; GC review required |
| F | 0.0 - 2.9 | Unacceptable | Fundamental protections missing, unlimited liability, or terms that create existential risk | Reject or propose company standard terms as counter |

## Signal Tables

### Liability Exposure

| Score | Evidence |
|-------|----------|
| 9-10 | Liability capped at 12 months fees or less, mutual indemnification with reasonable carve-outs, consequential damages excluded bilaterally, insurance requirements specified |
| 7-8 | Liability capped at contract value, indemnification mostly mutual with minor asymmetry, consequential damages excluded with standard carve-outs |
| 5-6 | Liability capped but at elevated level (2-3x contract value), indemnification tilted toward counterparty, some consequential damages included |
| 3-4 | Liability cap missing for some obligation categories, one-sided indemnification, broad consequential damages exposure |
| 0-2 | Unlimited liability with no cap, fully one-sided indemnification favoring counterparty, no consequential damages exclusion, penalty clauses present |

### IP Protection

| Score | Evidence |
|-------|----------|
| 9-10 | Company retains all pre-existing IP, work product ownership clearly assigned, license scope narrowly defined, non-compete and non-solicit provisions present, trade secret protections explicit |
| 7-8 | IP ownership clear with minor ambiguity in derivative works, license scope reasonable, confidentiality obligations cover trade secrets |
| 5-6 | IP ownership clause present but vague on edge cases (joint development, customizations), license scope broader than necessary, no non-compete |
| 3-4 | IP ownership unclear or partially assigned to counterparty, broad license grants, weak confidentiality provisions |
| 0-2 | No IP ownership clause, counterparty claims ownership of deliverables or derivative works, unlimited license grant, no trade secret protections |

### Termination Rights

| Score | Evidence |
|-------|----------|
| 9-10 | Mutual termination for convenience with 30-day notice or less, for-cause termination with reasonable cure period, clear post-termination data return/destruction obligations, no lock-in penalties |
| 7-8 | Termination for convenience available but with 60-90 day notice, for-cause triggers clearly defined, post-termination obligations specified |
| 5-6 | Termination for convenience restricted to annual renewal windows, cure period asymmetric, some post-termination obligations unclear |
| 3-4 | No termination for convenience, limited for-cause triggers, auto-renewal with price escalation, unclear data return obligations |
| 0-2 | No termination rights, mandatory multi-year commitment with penalty for early exit, counterparty retains data post-termination, one-sided termination favoring counterparty only |

### Data & Privacy

| Score | Evidence |
|-------|----------|
| 9-10 | GDPR/CCPA-compliant DPA included, data processing limited to specified purposes, 24-48hr breach notification, sub-processor approval rights, data localization honored, audit rights granted |
| 7-8 | DPA present with standard terms, breach notification within 72hrs, sub-processor list provided with notification of changes, reasonable audit provisions |
| 5-6 | Basic data protection clause but no formal DPA, breach notification timeframe vague, sub-processor controls limited to notification only |
| 3-4 | Minimal data protection language, no breach notification requirement, unlimited sub-processor delegation, no audit rights |
| 0-2 | No data protection provisions, counterparty claims broad rights to use/share company data, no breach notification, no compliance commitments |

### Financial Terms

| Score | Evidence |
|-------|----------|
| 9-10 | Fixed pricing with caps on increases, net-60 or better payment terms, audit rights for usage-based billing, clear SOW with change order process, no hidden fees |
| 7-8 | Pricing clear with annual increase cap (CPI or fixed %), net-30 payment terms, billing disputes process defined |
| 5-6 | Pricing clear but uncapped annual increases, payment terms at net-15 or prepayment required, limited dispute mechanism |
| 3-4 | Pricing ambiguous or subject to unilateral change, prepayment required with limited refund rights, no audit rights for variable charges |
| 0-2 | No pricing cap or transparency, full prepayment with no refund, auto-renewal with uncapped price escalation, penalty fees for underutilization |
