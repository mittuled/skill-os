# Privacy Compliance Framework: GDPR and CCPA/CPRA

Reference framework for managing end-to-end GDPR and CCPA compliance programmes.

## GDPR vs. CCPA/CPRA Comparison

| Dimension | GDPR | CCPA/CPRA |
|-----------|------|-----------|
| Scope | Processing personal data of EU residents | Businesses meeting revenue/data thresholds processing CA residents' data |
| Legal Basis | 6 lawful bases (Art. 6) | No legal basis requirement; opt-out model |
| Consent | Opt-in required for most processing | Opt-out for sale/sharing; opt-in for under-16 |
| Right to Know | Access request (Art. 15) | Right to know categories and specific pieces |
| Right to Delete | Erasure (Art. 17) | Right to delete with 9 exceptions |
| Right to Portability | Data portability (Art. 20) | Included in right to know |
| Right to Opt-Out | No direct equivalent (withdraw consent) | Right to opt-out of sale/sharing |
| Right to Correct | Rectification (Art. 16) | Right to correct (CPRA addition) |
| Right to Limit Use | Restriction (Art. 18) | Right to limit use of sensitive PI (CPRA) |
| Response Deadline | 30 days (extendable to 90) | 45 days (extendable to 90) |
| Enforcement | Supervisory authorities, up to 4% global revenue | California AG, CPPA, up to $7,500/violation |
| DPO Requirement | Required for certain controllers/processors | No DPO requirement |
| DPIA Requirement | Required for high-risk processing (Art. 35) | Risk assessments required (CPRA) |

## Data Subject Request (DSR) Workflow

### Intake
1. Receive request via designated channel (privacy@, in-app, written)
2. Log request with timestamp, requestor identity, rights invoked
3. Acknowledge receipt within 3 business days

### Verification
1. Verify requestor identity (match to account, government ID for non-account requests)
2. For CCPA authorized agents: verify agent authorization and consumer identity
3. Document verification method and outcome

### Processing
1. Determine applicable rights and exemptions
2. For access: compile all personal data across systems
3. For deletion: identify all storage locations, assess exemptions (legal hold, contractual necessity)
4. For opt-out: suppress from sale/sharing activities, propagate to downstream recipients
5. For portability: export in machine-readable format (JSON, CSV)

### Response
1. Respond within statutory deadline (30 days GDPR / 45 days CCPA)
2. If extension needed: notify requestor before original deadline with reason
3. For denial: cite specific exemption with explanation of appeal rights

## Records of Processing Activities (ROPA) Template

| Field | Description | GDPR Article |
|-------|-------------|-------------|
| Processing Activity | Name and description | Art. 30(1)(b) |
| Controller/Processor | Role and contact details | Art. 30(1)(a) |
| Purposes | Specific processing purposes | Art. 30(1)(b) |
| Categories of Data Subjects | User types affected | Art. 30(1)(c) |
| Categories of Personal Data | Data types processed | Art. 30(1)(c) |
| Recipients | Third parties receiving data | Art. 30(1)(d) |
| International Transfers | Countries and transfer mechanism | Art. 30(1)(e) |
| Retention Period | Retention period or criteria | Art. 30(1)(f) |
| Security Measures | Technical and organisational measures | Art. 30(1)(g) |
| Legal Basis | GDPR Art. 6 lawful basis | Art. 30(1)(b) |

## Cross-Border Transfer Decision Tree

1. Is the recipient in an EU/EEA country? --> No transfer mechanism needed
2. Is there an adequacy decision for the recipient country? --> Transfer permitted
3. Are appropriate safeguards available?
   - Standard Contractual Clauses (most common) --> Execute SCCs + TIA
   - Binding Corporate Rules (intra-group) --> Apply if approved
   - Codes of Conduct / Certification --> Use if available and approved
4. Do derogations apply? (Art. 49)
   - Explicit consent (for occasional transfers)
   - Contractual necessity
   - Important public interest
   - Legal claims
5. If none apply --> Transfer not permitted; data must remain in EU/EEA

## Compliance Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| DSR response time (GDPR) | <30 days | Average days to close |
| DSR response time (CCPA) | <45 days | Average days to close |
| Consent collection rate | >95% where required | Consent records / eligible users |
| DPA coverage | 100% of processors | Executed DPAs / total processors |
| ROPA currency | Updated within 30 days of change | Last update date vs. processing changes |
| Training completion | 100% within 30 days of onboarding | LMS completion records |
