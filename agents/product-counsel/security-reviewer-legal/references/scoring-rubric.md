# Scoring Rubric: security-reviewer-legal

Evaluates the completeness of a legal security architecture review covering requirements mapping, architecture assessment, contractual verification, and remediation planning.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Requirements Mapping | 25% | Completeness of compiling legal and contractual security requirements from all applicable sources |
| 2 | Architecture Assessment | 30% | Rigour of reviewing security architecture against the requirements register with gap identification |
| 3 | Contractual Representation Verification | 25% | Accuracy of verifying security claims in contracts, DPAs, and marketing against actual posture |
| 4 | Remediation Roadmap | 20% | Quality of prioritized remediation plan based on regulatory exposure and contractual breach risk |

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
| A+ | 9.0 – 10.0 | Exceptional | All requirements mapped, architecture fully assessed, representations verified accurate, no material gaps | Confirm compliance status to stakeholders |
| A | 8.0 – 8.9 | Strong | Requirements mapped, architecture assessed with minor gaps, representations mostly accurate | Address minor gaps within quarterly cycle |
| B | 7.0 – 7.9 | Good | Major requirements mapped, architecture assessed, some representation accuracy gaps found | Remediate representation gaps within 60 days |
| C | 5.0 – 6.9 | Adequate | Core requirements identified but architecture assessment incomplete | Hold: complete architecture assessment before customer commitments |
| D | 3.0 – 4.9 | Weak | Significant requirements gaps, architecture assessment superficial | Block new security representations: major review needed |
| F | 0.0 – 2.9 | Failing | No security legal review performed | Block: engage security and legal for comprehensive review |

## Signal Tables

### Requirements Mapping

| Score | Evidence |
|-------|----------|
| 9-10 | All sources compiled: GDPR Article 32 (appropriate measures), SOC 2 Trust Services Criteria, customer DPA security schedules, cyber insurance requirements, PCI-DSS (if applicable), HIPAA Security Rule (if applicable). Each requirement linked to legal source with specific clause reference. |
| 7-8 | Major regulatory and contractual sources compiled, most requirements traced to legal source |
| 5-6 | Primary regulatory requirements identified, contractual requirements partially compiled |
| 3-4 | Generic security requirements listed without legal source traceability |
| 0-2 | No requirements mapping performed |

### Architecture Assessment

| Score | Evidence |
|-------|----------|
| 9-10 | Encryption (at rest, in transit, key management), access controls (RBAC, MFA, least privilege), data residency, cross-border transfers (SCCs, adequacy), logging/monitoring, incident response, and vendor security all assessed against requirements register. Gap analysis produced. |
| 7-8 | Major security domains assessed against requirements, gap analysis produced with minor omissions |
| 5-6 | Core security controls reviewed but not systematically mapped to legal requirements |
| 3-4 | High-level architecture review without requirement-by-requirement assessment |
| 0-2 | No architecture assessment performed |

### Contractual Representation Verification

| Score | Evidence |
|-------|----------|
| 9-10 | Every security representation in customer contracts, DPAs, and marketing verified against actual implementation. Overstatements flagged with specific contract reference and remediation recommendation. Accuracy report produced. |
| 7-8 | Major representations verified, most overstatements identified |
| 5-6 | Some representations checked but not systematically verified across all contracts |
| 3-4 | Representations noted but not verified against actual security posture |
| 0-2 | No representation verification performed |

### Remediation Roadmap

| Score | Evidence |
|-------|----------|
| 9-10 | Gaps prioritized by regulatory exposure and contractual breach risk. Remediation plan with specific actions, owners, deadlines, and success criteria. Quick wins distinguished from long-term improvements. |
| 7-8 | Gaps prioritized, remediation actions identified with owners and deadlines |
| 5-6 | Gaps identified with generic remediation guidance but lacking prioritization |
| 3-4 | Gaps listed without remediation planning |
| 0-2 | No remediation roadmap produced |
