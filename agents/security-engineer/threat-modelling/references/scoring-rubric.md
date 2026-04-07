# Scoring Rubric: Threat Modelling

Evaluates the rigour and completeness of a threat model across decomposition, enumeration, prioritization, mitigation, and attack path validation.

## Criteria

| Criterion | Weight | Scale | Description |
|-----------|--------|-------|-------------|
| Decomposition Completeness | 20% | 0-10 | Quality and coverage of system decomposition: DFD accuracy, trust boundary identification |
| Threat Enumeration Coverage | 25% | 0-10 | Thoroughness of STRIDE application across all elements and threat categories |
| Prioritization Rigour | 20% | 0-10 | Quality of threat scoring: consistent methodology, defensible rankings |
| Mitigation Specificity | 20% | 0-10 | Actionability of mitigations: specific controls mapped, residual risk assessed |
| Attack Tree Validation | 15% | 0-10 | Depth of attack path analysis: multi-step chains verified, mitigations validated against paths |
| **Total** | **100%** | | |

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 – 10.0 | Exceptional | Threat model covers all attack surfaces with validated mitigations and complete attack tree verification | Approve and schedule periodic re-assessment |
| A | 8.0 – 8.9 | Strong | Comprehensive STRIDE coverage with minor gaps in attack tree depth or residual risk documentation | Approve with follow-up on flagged gaps within next sprint |
| B | 7.0 – 7.9 | Good | Solid decomposition and enumeration but mitigation specificity or attack path validation needs strengthening | Approve conditionally; remediate mitigation gaps before implementation |
| C | 5.0 – 6.9 | Adequate | Core threats identified but decomposition is shallow, prioritization inconsistent, or mitigations are generic | Revise threat model; do not proceed to implementation until gaps closed |
| D | 3.0 – 4.9 | Weak | Significant blind spots in threat coverage; no systematic prioritization; mitigations are copy-paste | Rework from decomposition stage with security engineering support |
| F | 0.0 – 2.9 | Failing | No meaningful threat analysis; system risks are unknown and unmitigated | Halt and commission a full threat modelling engagement |

## Signal Tables

### Decomposition Completeness
| Score | Evidence |
|-------|----------|
| 9-10 | Multi-level DFDs (L0-L2) with all processes, stores, flows, and external entities identified; trust boundaries clearly annotated at every privilege transition |
| 7-8 | L0-L1 DFDs complete with most trust boundaries identified; minor gaps in data store or external entity enumeration |
| 5-6 | Single-level DFD exists but missing some components; trust boundaries partially identified |
| 3-4 | Informal or incomplete diagram; significant components missing; trust boundaries not explicitly marked |
| 1-2 | No DFD or only a high-level block diagram with no data flow or trust boundary information |

### Threat Enumeration Coverage
| Score | Evidence |
|-------|----------|
| 9-10 | STRIDE applied per-element with correct category-to-element mapping; every DFD element has at least one threat identified; no categories systematically skipped |
| 7-8 | STRIDE applied to most elements; one or two low-risk elements or categories may be lightly covered with justification |
| 5-6 | STRIDE applied at system level rather than per-element; some threat categories (e.g., Repudiation, Elevation) underrepresented |
| 3-4 | Only 2-3 STRIDE categories addressed; many elements not analyzed; enumeration is ad-hoc |
| 1-2 | No systematic threat enumeration; threats listed are anecdotal or copied from a generic template without system-specific analysis |

### Prioritization Rigour
| Score | Evidence |
|-------|----------|
| 9-10 | Consistent DREAD or risk-matrix scoring for every threat; scores are justified with evidence; ranking produces a clear priority order with no ties left unresolved |
| 7-8 | Scoring methodology applied consistently; most scores justified; minor inconsistencies between similar threats |
| 5-6 | Scoring exists but methodology applied unevenly; some threats lack justification; high/medium/low used instead of numeric scores |
| 3-4 | Threats listed without consistent scoring; priority is based on gut feeling; no reproducible methodology |
| 1-2 | No prioritization; threats presented as a flat list with no severity or likelihood assessment |

### Mitigation Specificity
| Score | Evidence |
|-------|----------|
| 9-10 | Every high/critical threat has a named control, implementation approach, owner, and residual risk rating; mitigations mapped to security frameworks (NIST, CIS) |
| 7-8 | Mitigations specified for most threats with control names and risk treatment type (eliminate/reduce/transfer/accept); residual risk noted |
| 5-6 | Mitigations described in general terms ("add encryption", "use WAF") without specific implementation guidance; residual risk not consistently assessed |
| 3-4 | Generic mitigations copied from templates; no mapping to specific system controls; residual risk ignored |
| 1-2 | No mitigations proposed, or mitigations are vague ("improve security") with no actionable detail |

### Attack Tree Validation
| Score | Evidence |
|-------|----------|
| 9-10 | Attack trees built for top 5+ threats; multi-step exploitation chains documented; every viable path verified to be broken by at least one proposed mitigation |
| 7-8 | Attack trees for top 3-4 threats; most paths validated against mitigations; minor gaps in chain coverage |
| 5-6 | Attack trees for 1-2 threats only; paths identified but mitigation overlay is incomplete |
| 3-4 | No formal attack trees; some attack scenarios described narratively but not structured or validated |
| 1-2 | No attack path analysis performed |
