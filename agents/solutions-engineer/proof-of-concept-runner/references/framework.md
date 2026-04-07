# Framework: proof-of-concept-runner

Defines the POC methodology including qualification gates, execution phases, and evaluation criteria for structured proof-of-concept engagements.

## POC Qualification Gate

A POC should only proceed when **all** of the following criteria are met:

| Criterion | Threshold | Evidence Required |
|-----------|-----------|-------------------|
| Deal ACV | >= $25K ARR (or company-defined minimum) | CRM opportunity record with ACV estimate |
| MEDDIC Score | >= 6.0 composite | Completed MEDDIC scorecard from lead-qualifier |
| Executive Sponsor | Named and engaged | At least 1 direct interaction (meeting, email exchange) with VP+ sponsor |
| Decision Timeline | Committed post-POC decision date | Written confirmation from economic buyer or champion |
| Technical Evaluator | Named and available | Identified individual who will conduct the hands-on evaluation |
| Success Criteria | Agreed in writing | Signed scope document with measurable pass/fail metrics |

### Decline Criteria

Decline or defer POCs when:
- Deal ACV is below threshold (offer a self-serve trial instead)
- No executive sponsor identified (sales team must multi-thread before POC)
- Prospect wants an "open-ended evaluation" without defined success criteria
- Technical evaluator is unavailable during the proposed evaluation window
- Requirements fall into the "red" zone on the feasibility assessment

## POC Phases

### Phase 1: Scoping (Days 1-3)

**Objective**: Define what will be evaluated and how success is measured.

| Activity | Owner | Deliverable |
|----------|-------|-------------|
| Requirements workshop | SE + prospect tech team | Use case list (max 3) with priority ranking |
| Success criteria definition | SE + prospect + AE | Measurable pass/fail thresholds per use case |
| Environment specification | SE | Infrastructure requirements, data needs, integration points |
| Timeline agreement | AE + prospect EB | Start date, end date, decision date, touchpoint schedule |
| Scope document sign-off | All parties | Signed POC scope document |

### Phase 2: Provisioning (Days 4-5)

**Objective**: Set up the evaluation environment so the prospect can start on Day 6.

| Activity | Owner | Deliverable |
|----------|-------|-------------|
| Instance provisioning | SE / DevOps | Dedicated sandbox or demo environment |
| Data loading | SE + prospect | Sample datasets that mirror production scenarios |
| Integration configuration | SE | API connections, SSO setup, third-party tool links |
| Access distribution | SE | Credentials for all prospect evaluators |
| Smoke test | SE | Environment validation checklist (all green) |

### Phase 3: Guided Evaluation (Days 6-20)

**Objective**: Prospect evaluates the product with structured support touchpoints.

| Touchpoint | Timing | Format | Agenda |
|------------|--------|--------|--------|
| Kickoff session | Day 6 | 60-min video call | Orient team, walk through use cases, confirm schedule |
| Async check-in | Day 9 | Slack/email | "Any blockers? Anything surprising?" |
| Mid-point review | Day 13 | 45-min video call | Progress against success criteria, blocker resolution |
| Async check-in | Day 16 | Slack/email | Prep for final review, gather preliminary feedback |
| Final review | Day 20 | 60-min video call | Results presentation, gap discussion, next steps |

### Phase 4: Results & Decision (Days 21-25)

**Objective**: Document outcomes and drive a go/no-go decision.

| Activity | Owner | Deliverable |
|----------|-------|-------------|
| Results documentation | SE | Per-metric results vs. success criteria |
| Business value mapping | SE + AE | Technical outcomes translated to business impact |
| Gap documentation | SE | Any unmet criteria with mitigation paths |
| Joint results presentation | SE + AE | Combined presentation to tech team + EB |
| Decision facilitation | AE | Go/no-go with next steps documented |

## Success Criteria Framework

### Criteria Categories

| Category | Example Metrics | Measurement Method |
|----------|-----------------|-------------------|
| Functional | "Process 1,000 records with <1% error rate" | Automated test run on sample data |
| Performance | "API response time <200ms at P95 under load" | Load test with defined traffic pattern |
| Integration | "Bi-directional sync with Salesforce within 5 minutes" | End-to-end integration test |
| Usability | "New user completes core workflow in <10 minutes" | Timed user walkthrough |
| Security | "Passes SSO authentication; audit log captures all actions" | Security checklist verification |

### Pass/Fail Determination

- **Pass**: Metric meets or exceeds the defined threshold
- **Partial Pass**: Metric is within 80% of threshold with a documented workaround
- **Fail**: Metric falls below 80% of threshold with no viable workaround

### Overall POC Verdict

| Verdict | Criteria |
|---------|----------|
| **Green** (Proceed) | All must-have criteria Pass; nice-to-have criteria are Pass or Partial Pass |
| **Yellow** (Proceed with conditions) | All must-have criteria Pass or Partial Pass; gaps have documented mitigation timeline |
| **Red** (Do not proceed) | Any must-have criterion Fails with no workaround or mitigation path |

## Scope Management

### In-Scope Boundaries

- Maximum 3 use cases per POC
- Maximum 21 calendar days for evaluation
- Pre-defined data sets only (no production data migration)
- Named evaluator team (max 5 users)

### Scope Change Protocol

1. Prospect requests additional use case or integration
2. SE documents the request and estimates additional time/effort
3. AE assesses commercial impact (does this expand the deal or delay it?)
4. Joint decision: accept (with timeline extension), defer to post-sale, or decline
5. Any scope change requires written re-confirmation from the executive sponsor

### Common Scope Creep Patterns to Block

| Pattern | Response |
|---------|----------|
| "Can we also test [unrelated feature]?" | "We can add that to Phase 2 post-purchase. Let's keep this POC focused on your top 3 priorities." |
| "Our security team wants a full audit" | "We will schedule a dedicated security review session outside the POC timeline." |
| "Can we extend by 2 more weeks?" | "What specifically is not resolved? Let's address the blocker rather than extending the timeline." |
| "We want to add 10 more users" | "For the POC, 5 evaluators keeps feedback focused. We will expand access during implementation." |
