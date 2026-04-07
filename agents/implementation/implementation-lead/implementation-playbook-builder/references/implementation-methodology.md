# Implementation Methodology Reference

Reference for the `implementation-playbook-builder` skill.

---

## 1. Implementation Complexity Tiers

Define the implementation tier at deal signature based on scope indicators.

| Tier | Indicators | Typical Duration | Staffing |
|------|-----------|-----------------|---------|
| **Tier 1 — Self-Serve** | SMB, standard config, no integrations, <5 users | 1–3 days | Customer-led; support docs |
| **Tier 2 — Guided** | SMB/Mid-market, 1–2 integrations, 5–50 users | 1–4 weeks | 1 implementation engineer |
| **Tier 3 — Assisted** | Mid-market, 3–5 integrations, data migration, 50–200 users | 4–12 weeks | 1 engineer + lead oversight |
| **Tier 4 — Enterprise** | Enterprise, complex integrations, custom config, >200 users | 8–24 weeks | Lead + 2 engineers + PM |

---

## 2. Standard Phase Definitions

### Phase 1: Discovery

**Purpose**: Understand the customer's technical environment, workflows, and success criteria before any configuration begins.

**Duration**: 1–2 weeks (Tier 3/4); 1–3 days (Tier 2)

**Entry Criteria**: Signed agreement; sales handoff completed

**Activities**:
- Review sales handoff notes and SOW
- Conduct discovery sessions with technical and business stakeholders
- Document requirements: functional, technical, integration, data migration
- Identify risks and dependencies
- Obtain customer sign-off on requirements document

**Exit Criteria**: Signed requirements document; implementation plan agreed

---

### Phase 2: Configuration

**Purpose**: Configure the product environment to match the customer's documented requirements.

**Duration**: 1–4 weeks depending on complexity tier

**Entry Criteria**: Signed requirements document

**Activities**:
- Provision customer environment
- Configure workflows, roles, and permissions per requirements
- Set up branding and white-labelling (if applicable)
- Apply custom configurations documented in requirements

**Exit Criteria**: Configured environment ready for integration and testing

---

### Phase 3: Integration

**Purpose**: Connect the product to the customer's existing systems.

**Duration**: 1–6 weeks depending on integration count and complexity

**Entry Criteria**: Configured environment from Phase 2

**Activities**:
- Set up each integration using the integration catalogue guides
- Validate data flow and field mapping
- Test authentication and permission scopes
- Document any limitations or workarounds

**Exit Criteria**: All integrations connected and passing data correctly

---

### Phase 4: Data Migration

**Purpose**: Move existing customer data into the product environment.

**Duration**: 1–4 weeks (if applicable)

**Entry Criteria**: Integration phase complete; customer data export provided

**Activities**:
- Map customer data fields to product data schema
- Clean and transform data per mapping document
- Run migration in staging environment
- Validate data quality and completeness
- Run migration in production with customer sign-off

**Exit Criteria**: Production data migration complete with customer validation sign-off

---

### Phase 5: Testing

**Purpose**: Validate the full implementation against the acceptance criteria defined in requirements.

**Duration**: 1–2 weeks

**Entry Criteria**: Configuration, integration, and migration complete

**Activities**:
- Execute acceptance test cases from requirements document
- Conduct user acceptance testing with customer team
- Resolve any issues blocking go-live
- Obtain customer sign-off on test results

**Exit Criteria**: All acceptance criteria passed; customer sign-off on go-live readiness

---

### Phase 6: Go-Live

**Purpose**: Transition the customer to production usage.

**Duration**: 1 day (event) + 2–4 weeks (hypercare period)

**Entry Criteria**: Testing phase complete; all acceptance criteria passed; go-live checklist cleared

**Activities**:
- Execute go-live (switch from staging to production or enable for all users)
- Confirm all systems operational
- Conduct kickoff training for end users
- Enter hypercare period (heightened monitoring and support)

**Exit Criteria**: Customer confirms production system operational; hypercare period ends

---

## 3. RACI Matrix (Standard)

| Deliverable | Implementation Engineer | Implementation Lead | Customer Technical | Customer Business |
|-------------|------------------------|---------------------|-------------------|------------------|
| Requirements document | Responsible | Accountable | Consulted | Consulted |
| Implementation plan | Consulted | Responsible | Informed | Informed |
| Environment configuration | Responsible | Accountable | Informed | — |
| Integration setup | Responsible | Accountable | Consulted | — |
| Data mapping document | Responsible | Accountable | Responsible | Informed |
| Acceptance test execution | Responsible | Accountable | Responsible | Consulted |
| Go-live decision | Consulted | Responsible | Accountable | Accountable |
| Training delivery | Responsible | Consulted | Informed | Accountable |

---

## 4. Implementation Risk Matrix

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|-----------|
| Customer cannot provide data schema on time | High | High | Require data sample within 5 days of kickoff; block migration phase if delayed |
| Integration with legacy system not documented | Medium | High | Conduct technical pre-discovery before project start |
| Key customer stakeholder unavailable | Medium | Medium | Identify backup contacts at kickoff |
| Scope creep from undocumented requirements | High | High | Require sign-off before each phase starts; document change requests formally |
| Go-live deadline driven by external event | Medium | High | Flag early; build buffer into timeline; define descope criteria |
| Customer data quality issues | High | Medium | Validate data sample in discovery; budget 20% time buffer for cleaning |

---

## 5. Go-Live Readiness Checklist

Before declaring go-live:

**Technical**
- [ ] All acceptance criteria from requirements document passed
- [ ] All integrations tested and data flowing correctly
- [ ] Production data migration complete and validated
- [ ] Security configuration reviewed (SSO, MFA, data access)
- [ ] Monitoring and alerting configured

**Customer Readiness**
- [ ] Customer technical team trained
- [ ] End user training completed
- [ ] Customer support escalation path documented
- [ ] Customer has confirmed readiness in writing

**Handoff**
- [ ] Customer success team briefed on account context
- [ ] Implementation notes and configurations documented
- [ ] Hypercare plan agreed with customer
- [ ] Transition to steady-state support communicated to customer

---

*Reference version 1.0 — Implementation / Implementation Lead*
