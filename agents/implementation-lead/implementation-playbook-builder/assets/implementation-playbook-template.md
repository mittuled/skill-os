# Implementation Playbook

**Version**: `[v1.0 Initial / v#.# — Reason for update]`
**Owner**: `[Implementation Lead]`
**Last Updated**: `YYYY-MM-DD`
**Applies To**: `[ ] All tiers  [ ] Tier 1  [ ] Tier 2  [ ] Tier 3  [ ] Tier 4 only`

---

## 1. Playbook Overview

**Purpose**: This playbook defines the standard implementation methodology for `[Product/Company Name]`. It ensures every customer deployment follows a predictable, repeatable process with clear milestones, responsibilities, and success criteria.

**Scope**: Covers all implementation phases from signed agreement through go-live and handoff to steady-state support.

---

## 2. Implementation Tiers

| Tier | Criteria | Duration | Process |
|------|----------|---------|---------|
| Tier 1 — Self-Serve | `[Criteria]` | `[Duration]` | Customer-led; support docs + async help |
| Tier 2 — Guided | `[Criteria]` | `[Duration]` | 1 implementation engineer |
| Tier 3 — Assisted | `[Criteria]` | `[Duration]` | 1 engineer + lead oversight |
| Tier 4 — Enterprise | `[Criteria]` | `[Duration]` | Full implementation team |

**Tier Assignment Process**: `[How is the tier determined? Who assigns it? When?]`

---

## 3. Phase-by-Phase Playbook

### Phase 1: Discovery

**Duration**: `[Standard duration per tier]`
**Owner**: Implementation Engineer (with Lead oversight on Tier 3/4)

| Activity | Owner | Customer Dependency | Output |
|----------|-------|---------------------|--------|
| Review sales handoff and SOW | Implementation Engineer | — | Context summary |
| Conduct discovery sessions | Implementation Engineer | Customer technical + business stakeholders | Session notes |
| Document requirements | Implementation Engineer | Customer review | Requirements document |
| Obtain sign-off | Implementation Lead | Customer approval | Signed requirements |

**Entry Gate**: Signed agreement + sales handoff complete
**Exit Gate**: Customer-signed requirements document

---

### Phase 2: Configuration

**Duration**: `[Standard duration per tier]`
**Owner**: Implementation Engineer

| Activity | Owner | Customer Dependency | Output |
|----------|-------|---------------------|--------|
| Provision environment | Implementation Engineer | None | Live environment URL |
| Configure workflows and roles | Implementation Engineer | Requirements sign-off | Configured environment |
| Apply custom settings | Implementation Engineer | Customer specification | Configured environment |
| Internal QA | Implementation Lead | — | QA sign-off |

**Entry Gate**: Signed requirements document
**Exit Gate**: Implementation Lead QA sign-off

---

### Phase 3: Integration

**Duration**: `[Standard duration per tier]`
**Owner**: Implementation Engineer

| Integration | Reference Guide | Customer Dependency | Estimated Duration |
|------------|----------------|---------------------|-------------------|
| `[Integration 1]` | `[Link to catalogue guide]` | `[What customer must provide]` | `[# days]` |
| `[Integration 2]` | `[Link to catalogue guide]` | `[What customer must provide]` | `[# days]` |

**Entry Gate**: Configuration phase complete
**Exit Gate**: All integrations passing connectivity and data-flow tests

---

### Phase 4: Data Migration *(if applicable)*

**Duration**: `[Standard duration per tier]`
**Owner**: Implementation Engineer

| Activity | Owner | Customer Dependency | Output |
|----------|-------|---------------------|--------|
| Receive customer data export | Customer | Data in agreed format | Raw data package |
| Map and validate data | Implementation Engineer | Customer review | Mapping document |
| Staging migration | Implementation Engineer | — | Staging environment with data |
| Customer validation | Customer | Customer sign-off | Validated dataset |
| Production migration | Implementation Engineer | Go-ahead from customer | Migrated production data |

**Entry Gate**: Integration phase complete; customer data export received
**Exit Gate**: Customer sign-off on production data quality

---

### Phase 5: Testing

**Duration**: `[Standard duration per tier]`
**Owner**: Implementation Engineer + Customer

| Test Type | Owner | Criteria Source | Pass Condition |
|-----------|-------|----------------|---------------|
| Functional acceptance testing | Implementation Engineer | Requirements document | All test cases pass |
| User acceptance testing | Customer | Customer workflow requirements | Customer sign-off |

**Entry Gate**: Configuration, integration, and migration complete
**Exit Gate**: All acceptance criteria passed; customer sign-off documented

---

### Phase 6: Go-Live and Hypercare

**Duration**: `[Go-live day] + [Hypercare period: # weeks]`
**Owner**: Implementation Lead

| Activity | Owner | Output |
|----------|-------|--------|
| Go-live readiness checklist | Implementation Lead | Signed checklist |
| Production go-live execution | Implementation Engineer | System live |
| User training | Implementation Engineer | Training complete |
| Hypercare monitoring | Implementation Engineer | Daily status check for first `# weeks` |
| CS handoff | Implementation Lead | Handoff document + briefing |

**Entry Gate**: Go-live readiness checklist complete; customer approval
**Exit Gate**: Hypercare period complete; customer confirms stable operation; CS team briefed

---

## 4. Standard Templates Library

| Template | Location | Used In |
|---------|---------|--------|
| Requirements document | `references/requirements-template.md` | Phase 1 |
| RACI matrix | `references/implementation-methodology.md` | All phases |
| Go-live checklist | `references/implementation-methodology.md` | Phase 6 |
| Status report | `[Link]` | Weekly during Tier 3/4 |
| Implementation handoff | `[Link]` | Phase 6 |

---

## 5. Escalation Path

| Situation | Escalate To | Response Time |
|-----------|------------|--------------|
| Customer not meeting commitments (2+ weeks delayed) | Implementation Lead | 24 hours |
| Technical blocker cannot be resolved | Engineering | 48 hours |
| Customer scope change request | Implementation Lead + Sales | 48 hours |
| Customer satisfaction at risk | Implementation Lead + CS Manager | 24 hours |

---

*Playbook version 1.0 — Implementation / Implementation Lead*
