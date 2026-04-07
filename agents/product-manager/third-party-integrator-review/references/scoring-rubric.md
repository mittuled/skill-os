# Scoring Rubric: third-party-integrator-review

Evaluates the rigour of a third-party integration review covering product fit, technical risk, compliance, cost analysis, and decision quality.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Product Fit Assessment | 25% | Quality of alignment analysis between integration and product goals/user needs |
| 2 | Technical Risk Evaluation | 25% | Depth of API reliability, failure mode, and performance impact analysis |
| 3 | Compliance and Data Review | 25% | Completeness of regulatory, data handling, and privacy assessment |
| 4 | Cost and Lock-In Analysis | 15% | Accuracy of pricing projections and switching cost evaluation |
| 5 | Decision Quality | 10% | Clarity and actionability of the approve/conditional/reject recommendation |

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
| A+ | 9.0 – 10.0 | Exceptional | All five dimensions thoroughly assessed, decision backed by complete evidence, mitigations specified for conditional approvals | Proceed with integration decision |
| A | 8.0 – 8.9 | Strong | Product fit validated, technical and compliance risks assessed, cost modelled, clear decision | Proceed with minor documentation additions |
| B | 7.0 – 7.9 | Good | Most dimensions covered, some gaps in cost or lock-in analysis | Complete cost analysis before finalising decision |
| C | 5.0 – 6.9 | Adequate | Product fit and technical risk assessed but compliance or cost review incomplete | Request compliance review and cost modelling before approval |
| D | 3.0 – 4.9 | Weak | Superficial review, multiple dimensions missing or poorly assessed | Re-conduct review with structured checklist |
| F | 0.0 – 2.9 | Failing | No meaningful integration review performed | Block integration until complete review is conducted |

## Signal Tables

### Product Fit Assessment

| Score | Evidence |
|-------|----------|
| 9-10 | Integration mapped to specific validated user need with evidence (discovery findings, support tickets, usage data). Alignment with roadmap priorities documented. Alternative solutions considered and compared. |
| 7-8 | User need identified and linked to product goals, alternatives noted |
| 5-6 | General alignment with product direction stated but no specific user need validation |
| 3-4 | Integration justified by engineering preference without product fit analysis |
| 0-2 | No product fit assessment performed |

### Technical Risk Evaluation

| Score | Evidence |
|-------|----------|
| 9-10 | Vendor SLA reviewed with uptime history. Latency impact modelled. Failure modes documented with fallback behaviour. Data flow mapped. Load testing results or capacity projections included. |
| 7-8 | SLA reviewed, failure modes considered, basic performance impact assessed |
| 5-6 | SLA noted but not reviewed in depth; failure modes acknowledged but fallbacks not designed |
| 3-4 | Technical risk mentioned generically without specific analysis |
| 0-2 | No technical risk evaluation performed |

### Compliance and Data Review

| Score | Evidence |
|-------|----------|
| 9-10 | GDPR/SOC 2/HIPAA compliance verified as applicable. Data residency confirmed. Encryption at rest and in transit verified. Deletion and retention policies reviewed. DPA executed or required. |
| 7-8 | Primary compliance certifications verified, data handling reviewed |
| 5-6 | Certifications noted at face value without scope review; data handling partially assessed |
| 3-4 | Compliance assumed based on vendor reputation |
| 0-2 | No compliance or data review performed |

### Cost and Lock-In Analysis

| Score | Evidence |
|-------|----------|
| 9-10 | Pricing modelled at current usage and 3x scale. Lock-in clauses identified. Switching costs estimated including migration effort and data portability. Contract terms reviewed. |
| 7-8 | Pricing modelled at current usage, switching costs acknowledged |
| 5-6 | Current pricing documented but no scale projection or switching cost estimate |
| 3-4 | Pricing noted but no analysis of terms or lock-in |
| 0-2 | No cost analysis performed |

### Decision Quality

| Score | Evidence |
|-------|----------|
| 9-10 | Clear approve/conditional/reject with rationale linking to each assessment dimension. Conditions have specific deadlines and owners. Decision distributed to all stakeholders. |
| 7-8 | Clear decision with rationale, conditions specified |
| 5-6 | Decision made but rationale incomplete or conditions vague |
| 3-4 | Informal recommendation without documented rationale |
| 0-2 | No decision rendered |
