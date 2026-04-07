# Scoring Rubric: privacy-impact-assessor

Evaluates the completeness and rigour of a privacy impact assessment covering data flow mapping, legal basis, necessity/proportionality, risk identification, and mitigation design.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Data Flow Mapping | 20% | Completeness of the data lifecycle mapping including collection, processing, storage, sharing, and deletion |
| 2 | Legal Basis Assessment | 20% | Rigour of legal basis determination per processing activity (consent, legitimate interest, contractual necessity) |
| 3 | Necessity and Proportionality | 20% | Quality of data minimization analysis and evaluation of less privacy-invasive alternatives |
| 4 | Risk Identification | 20% | Comprehensiveness of privacy risk identification across all dimensions with likelihood/severity ratings |
| 5 | Mitigation Design | 20% | Specificity and implementability of recommended technical, organizational, and legal mitigations |

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
| A+ | 9.0 – 10.0 | Exceptional | Complete data flow maps, legal basis justified per activity, all risks identified with specific mitigations, DPO consultation documented | Approve processing with standard monitoring |
| A | 8.0 – 8.9 | Strong | Data flows mapped, legal basis sound, major risks identified and mitigated | Approve with minor mitigation enhancements |
| B | 7.0 – 7.9 | Good | Data flows mostly mapped, legal basis assessed, risks identified but some mitigations need specificity | Approve with conditions: complete mitigations within 30 days |
| C | 5.0 – 6.9 | Adequate | Data flows partially mapped, legal basis determined for primary activities, risk assessment incomplete | Hold: complete data flow mapping and risk assessment before launch |
| D | 3.0 – 4.9 | Weak | Significant gaps in data flow mapping, legal basis unclear, risks unidentified | Block: major PIA revision required |
| F | 0.0 – 2.9 | Failing | No systematic privacy impact assessment performed | Block: full PIA required before any processing |

## Signal Tables

### Data Flow Mapping

| Score | Evidence |
|-------|----------|
| 9-10 | Complete data lifecycle documented: collection points, processing activities, storage locations with retention periods, all third-party recipients, deletion mechanisms. Data flow diagram produced. Processing inventory linked to ROPA. |
| 7-8 | Data flows mapped for primary processing activities, most third-party sharing documented, retention periods defined |
| 5-6 | Collection and primary processing documented, third-party sharing partially mapped, retention periods incomplete |
| 3-4 | High-level data categories listed without flow mapping or lifecycle documentation |
| 0-2 | No data flow mapping performed |

### Legal Basis Assessment

| Score | Evidence |
|-------|----------|
| 9-10 | Legal basis determined per processing activity per GDPR Article 6. Consent-based processing verified for GDPR requirements (freely given, specific, informed, unambiguous). Legitimate interest balancing tests documented. CCPA sale/sharing opt-out rights assessed. |
| 7-8 | Legal basis assigned per activity, consent mechanisms reviewed, legitimate interest tests performed for primary activities |
| 5-6 | Legal basis identified at feature level but not per individual processing activity |
| 3-4 | Generic legal basis claimed ("consent") without per-activity analysis |
| 0-2 | No legal basis assessment performed |

### Necessity and Proportionality

| Score | Evidence |
|-------|----------|
| 9-10 | Each data element justified as necessary for stated purpose. Less invasive alternatives evaluated and documented. Data minimization applied: unnecessary fields removed, anonymization/pseudonymization considered, retention minimized. |
| 7-8 | Major data elements justified, alternatives considered for high-risk processing |
| 5-6 | Necessity claimed but alternatives not systematically evaluated |
| 3-4 | Data collection accepted as given without necessity analysis |
| 0-2 | No necessity or proportionality assessment performed |

### Risk Identification

| Score | Evidence |
|-------|----------|
| 9-10 | Risks identified across all dimensions: unauthorized access, function creep, re-identification, cross-border transfer, data subject rights compliance, processor chain. Each risk rated by likelihood and severity. Risk register produced. |
| 7-8 | Major risk dimensions covered with likelihood/severity ratings |
| 5-6 | Some risks identified but missing dimensions (e.g., re-identification risk, function creep) |
| 3-4 | Generic privacy risks noted without specific analysis |
| 0-2 | No risk identification performed |

### Mitigation Design

| Score | Evidence |
|-------|----------|
| 9-10 | Each risk has specific mitigations spanning technical (encryption, pseudonymization, access controls), organizational (policies, training, DPO oversight), and legal measures (consent mechanisms, privacy notices, DPAs). Implementation owners and timelines assigned. |
| 7-8 | Mitigations specified for high-priority risks, most control types covered |
| 5-6 | Mitigations listed but lack implementation detail or owner assignment |
| 3-4 | Generic mitigation recommendations without specificity |
| 0-2 | No mitigations designed |
