# Scoring Rubric: legal-idea-reviewer

Evaluates the legal viability and risk profile of a new business idea or product concept before significant resource investment.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Regulatory Compliance Risk | 30% | Whether applicable regulations have been identified and the concept can comply without fundamental redesign |
| 2 | IP and Freedom-to-Operate Risk | 25% | Whether the concept faces patent infringement, trademark conflicts, or trade secret misappropriation risks |
| 3 | Data Privacy and Security Risk | 20% | Whether data collection, processing, and storage comply with applicable privacy frameworks (GDPR, CCPA, COPPA, HIPAA) |
| 4 | Liability Exposure | 15% | Whether the concept creates product liability, indemnification, or professional responsibility risks |
| 5 | Contractual Constraint Risk | 10% | Whether existing agreements (vendor contracts, licenses, non-competes) restrict or prevent the concept |
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
| A+ | 9.0 – 10.0 | Go | No material legal risks identified; concept is legally viable as designed | Proceed with development; schedule deeper review at commitment milestone |
| A | 8.0 – 8.9 | Conditional Go | Minor legal risks identified with clear mitigation paths | Proceed with development; implement mitigations in parallel |
| B | 7.0 – 7.9 | Conditional Go with Caveats | Moderate risks in 1-2 dimensions that require design modifications | Proceed with concept revisions; re-review after modifications |
| C | 5.0 – 6.9 | Pause | Significant risks in multiple dimensions; concept may be viable with substantial changes | Hold development; conduct deeper regulatory and IP analysis before investing |
| D | 3.0 – 4.9 | No-Go (Revisable) | Major legal barriers exist but concept could be restructured to avoid them | Do not proceed; provide restructuring guidance for founders to consider |
| F | 0.0 – 2.9 | No-Go | Fundamental legal barriers (regulated activity without license, clear IP infringement, prohibited data use) | Do not proceed; document reasons for concept archive |

## Signal Tables

### Regulatory Compliance Risk

| Score | Evidence |
|-------|----------|
| 9-10 | All applicable regulatory frameworks identified (federal, state, international); concept complies without modification; licensing requirements confirmed achievable |
| 7-8 | Major regulations identified; concept complies with minor adjustments (e.g., adding disclosures or consent flows); no licensing barriers |
| 5-6 | Some regulations identified but analysis incomplete; concept may require feature changes to comply; licensing feasibility unknown |
| 3-4 | Concept enters regulated industry (fintech, healthtech, edtech) without addressing licensing, permits, or compliance infrastructure |
| 0-2 | Concept requires regulatory license the company cannot obtain, or directly violates existing regulation |

### IP and Freedom-to-Operate Risk

| Score | Evidence |
|-------|----------|
| 9-10 | Prior art search conducted; no blocking patents identified; trademark clearance confirmed; no trade secret misappropriation concerns |
| 7-8 | Preliminary freedom-to-operate review shows no blocking IP; minor trademark conflicts resolvable through naming changes |
| 5-6 | No formal IP search conducted but concept uses novel approach; potential patent landscape risks not yet assessed |
| 3-4 | Concept closely mirrors existing patented technology or uses a name with known trademark conflicts |
| 0-2 | Concept directly infringes known patents, uses protected trademarks, or relies on misappropriated trade secrets |

### Data Privacy and Security Risk

| Score | Evidence |
|-------|----------|
| 9-10 | Data flows mapped; applicable privacy laws identified (GDPR, CCPA, COPPA, HIPAA); concept includes compliant consent, storage, and deletion mechanisms by design |
| 7-8 | Major data privacy requirements identified; concept can comply with standard privacy engineering (consent flows, DPA provisions) |
| 5-6 | Concept collects personal data but privacy impact assessment not conducted; unclear if special categories (health, children, biometric) apply |
| 3-4 | Concept involves sensitive data categories without addressing consent, cross-border transfer, or breach notification requirements |
| 0-2 | Concept fundamentally requires data practices prohibited by applicable law (e.g., selling children's data, processing without legal basis under GDPR) |

### Liability Exposure

| Score | Evidence |
|-------|----------|
| 9-10 | Liability vectors identified (product liability, professional responsibility, content liability); all manageable through standard terms, insurance, and disclaimers |
| 7-8 | Major liability risks assessed; most manageable through contractual protections; one area needs deeper analysis |
| 5-6 | Liability exposure acknowledged but not systematically assessed; concept may create novel liability theories (AI-generated advice, autonomous decisions) |
| 3-4 | Concept creates significant uninsurable or hard-to-limit liability exposure (e.g., health/safety recommendations without professional licensing) |
| 0-2 | Concept creates strict liability exposure or professional responsibility obligations the company cannot satisfy |

### Contractual Constraint Risk

| Score | Evidence |
|-------|----------|
| 9-10 | Existing contracts reviewed; no restrictive covenants, exclusivity clauses, or non-compete obligations conflict with concept |
| 7-8 | Most relevant contracts reviewed; minor potential conflicts identified with clear resolution paths |
| 5-6 | Contract review incomplete; key vendor or partner agreements not yet checked for restrictive clauses |
| 3-4 | Known contractual obligations may restrict concept (e.g., exclusivity with competing partner, data use limitations) |
| 0-2 | Concept directly violates existing contractual obligations (non-compete, exclusivity, IP license restrictions) |
