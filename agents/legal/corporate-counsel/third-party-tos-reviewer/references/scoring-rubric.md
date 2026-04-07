# Scoring Rubric: third-party-tos-reviewer

Evaluates the legal risk profile of a third-party's terms of service, vendor contract, or partner agreement before the company commits.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Liability and Indemnification | 25% | Whether liability caps, indemnification obligations, and warranty provisions are reasonable and balanced |
| 2 | Data Privacy and Security | 25% | Whether data handling, processing, breach notification, and sub-processor provisions comply with the company's privacy obligations |
| 3 | IP and Data Ownership | 20% | Whether IP ownership, data ownership, license grants, and usage rights are clearly defined and acceptable |
| 4 | Term and Exit Provisions | 15% | Whether termination rights, data portability, transition support, and auto-renewal terms are favorable |
| 5 | Modification and Governance | 15% | Whether unilateral modification rights, governing law, dispute resolution, and force majeure provisions are acceptable |
| **Total** | | **100%** | |

## Scale

Each criterion is scored **0-10**:
- **0**: No evidence / completely absent
- **5**: Partially present with significant gaps
- **10**: Fully present, comprehensive, no gaps

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 – 10.0 | Accept | Terms are balanced and favorable; no material risks | Execute as-is; log in vendor register |
| A | 8.0 – 8.9 | Accept with Notes | Terms are reasonable with minor unfavorable provisions that do not create material risk | Execute with documented risk acceptance; log accepted risks |
| B | 7.0 – 7.9 | Negotiate Minor | 1-2 moderately unfavorable clauses that should be negotiated but are not deal-breakers | Send targeted redlines; accept if vendor declines changes |
| C | 5.0 – 6.9 | Negotiate Required | Multiple unfavorable clauses creating material risk; terms must be negotiated before execution | Send comprehensive redlines with fallback positions; do not execute without changes |
| D | 3.0 – 4.9 | Reject Unless Negotiated | Significant risk clauses (unlimited liability, broad IP assignment, no data protections) | Reject current terms; negotiate or find alternative vendor |
| F | 0.0 – 2.9 | Reject | Terms create unacceptable legal exposure; non-negotiable deal-breakers present | Do not execute; recommend alternative vendors |

## Signal Tables

### Liability and Indemnification

| Score | Evidence |
|-------|----------|
| 9-10 | Mutual liability cap tied to contract value or 12-month fees; carve-outs only for willful misconduct, IP infringement, and confidentiality breach; mutual indemnification for third-party claims; consequential damages waiver is mutual |
| 7-8 | Liability cap exists but is asymmetric (vendor cap lower than company's); indemnification is mutual but vendor carve-outs are broader; consequential damages waiver present |
| 5-6 | Liability cap exists but is very low relative to potential exposure; indemnification is one-sided (company indemnifies vendor but not vice versa); no consequential damages waiver |
| 3-4 | No liability cap on company's obligations; vendor disclaims all warranties; vendor's liability limited to amounts paid in last 3 months; no indemnification from vendor |
| 0-2 | Unlimited liability for company; vendor accepts zero liability; company must indemnify vendor for all claims including vendor's own negligence |

### Data Privacy and Security

| Score | Evidence |
|-------|----------|
| 9-10 | GDPR-compliant DPA included (Article 28 requirements); sub-processor list disclosed with notification rights; breach notification within 72 hours; data deletion/return on termination; SOC 2 Type II or equivalent certification; data residency commitments |
| 7-8 | DPA available on request; sub-processors disclosed; breach notification specified (but >72 hours); data deletion on termination; security certification present |
| 5-6 | Privacy policy exists but no DPA; sub-processors not disclosed; breach notification vague ("promptly"); no data residency commitment; security measures described but not certified |
| 3-4 | Minimal privacy provisions; no DPA; vendor claims right to use customer data for analytics/improvement; no breach notification commitment; no security certification |
| 0-2 | No data privacy provisions; vendor claims ownership of customer data; no security commitments; vendor may share data with third parties without consent |

### IP and Data Ownership

| Score | Evidence |
|-------|----------|
| 9-10 | Company retains all IP in its data and content; vendor's license to company data is limited to providing the service; no broad IP assignment; vendor's pre-existing IP clearly carved out; company owns all customizations and integrations |
| 7-8 | Company retains data ownership; vendor takes limited license for service delivery and anonymized analytics; pre-existing IP boundaries clear |
| 5-6 | Data ownership stated but license grant to vendor is broad ("to improve products and services"); unclear whether company IP in configurations is retained |
| 3-4 | Vendor claims license to use company data for product development, benchmarking, or marketing; IP ownership of customizations ambiguous |
| 0-2 | Vendor claims ownership of or broad license to company data; assignment of company IP to vendor; no restrictions on vendor's use of company content |

### Term and Exit Provisions

| Score | Evidence |
|-------|----------|
| 9-10 | Termination for convenience with 30-day notice; no early termination penalty; data export in standard format within 30 days; transition assistance included; auto-renewal with 30+ day opt-out notice |
| 7-8 | Termination for convenience available but with penalty or longer notice period; data export available; auto-renewal with opt-out window |
| 5-6 | Termination only for cause or at renewal; data export available but in proprietary format; auto-renewal with short opt-out window (14 days) |
| 3-4 | No termination for convenience; multi-year commitment with penalty; data export not guaranteed; auto-renewal with no opt-out window |
| 0-2 | Locked-in term with no exit; data not returned on termination; vendor retains data indefinitely; early termination requires payment of full remaining term |

### Modification and Governance

| Score | Evidence |
|-------|----------|
| 9-10 | No unilateral modification right; amendments require mutual written consent; governing law is a neutral or company-favorable jurisdiction; standard arbitration or litigation with reasonable venue; force majeure is balanced |
| 7-8 | Vendor may modify terms with 30+ day notice and right to terminate if changes are material; governing law reasonable; dispute resolution fair |
| 5-6 | Vendor may modify terms with notice but no right to terminate on adverse changes; governing law is vendor's home state; mandatory arbitration |
| 3-4 | Vendor may modify terms at any time with minimal notice; governing law in unfavorable jurisdiction; mandatory arbitration in vendor's city; class action waiver |
| 0-2 | Vendor may modify terms unilaterally without notice; continued use constitutes acceptance; governing law in foreign jurisdiction; no dispute resolution mechanism specified |
