# Framework: Crisis Communications Planner

Defines the crisis response methodology, severity tiers, and messaging architecture for building and executing a crisis communications protocol.

## RACE Model Phases

| Phase | Definition | Crisis Comms Application |
|-------|-----------|--------------------------|
| Research | Assess the situation and gather facts | Identify scope, affected parties, potential liability, and coverage timeline |
| Action | Decide on operational response | Select spokespersons, activate response team, engage legal and HR |
| Communication | Deliver coordinated messaging | Execute channel-specific responses using pre-approved templates |
| Evaluation | Measure and learn | Track sentiment, coverage, and stakeholder trust indicators post-crisis |

## Crisis Severity Tiers

| Tier | Label | Criteria | Response Window | Spokesperson Level |
|------|-------|----------|----------------|--------------------|
| 1 | Critical | Data breach, executive misconduct, mass layoffs, legal action, safety incident | 30 minutes | CEO or C-suite |
| 2 | High | Product outage >4 hours, negative tier-1 press, regulatory inquiry, customer data exposure | 2 hours | VP-level + Legal |
| 3 | Moderate | Negative social media spike, minor product issue, employee complaint goes public | 4 hours | PR Manager |
| 4 | Low | Competitor attack, minor customer complaint with media pickup, rumour correction | 24 hours | PR Manager |

## Holding Statement Patterns

Holding statements are pre-approved message scaffolds issued while full facts are gathered. Use within the first response window.

| Pattern | When to Use | Core Components |
|---------|------------|-----------------|
| Acknowledgement + Action | Any Tier 1 or 2 event | We are aware of [X]. We are taking immediate steps to [Y]. We will update by [time]. |
| Empathy + Investigation | Customer impact events | We understand [impact]. We are investigating the cause. Customer safety/trust is our priority. |
| Correction + Context | Factual inaccuracy in press | [Claim] is inaccurate. The facts are [X]. We have contacted [outlet] to correct the record. |
| No Comment Holding | Legal hold required | We are aware of the situation. As this involves [legal/personnel] matters, we cannot comment at this time. |

## Channel-Specific Response Playbook

| Channel | Audience | Format | Response Time |
|---------|----------|--------|---------------|
| Press statement | Media and public | Full formal statement, distributed via wire + email | Within response window |
| Social media | Public, customers, prospects | Short acknowledgement linking to full statement | Within 1 hour of tier 1/2 |
| Customer email | Affected customers | Direct, factual, action-oriented; avoid legal boilerplate | Within response window |
| Employee comms | Internal team | Full context, what they should and should not say externally | Before or simultaneous with external |
| Investor/board comms | Shareholders | Factual, business impact focus, mitigation plan | Within response window for tier 1 |
| Dark site page | Public (Tier 1 only) | Dedicated crisis landing page with live updates | Activate for Tier 1 events |

## Dark Site Strategy

A dark site is a pre-built, not-yet-published web page activated instantly during a Tier 1 crisis.

**Pre-build requirements:**
- Domain or subdomain reserved (e.g., status.company.com or incident.company.com)
- Template published with placeholder content
- Update mechanism that bypasses normal content approval chain
- Owned by PR Manager with engineering access on-call

**Content structure:** Statement timestamp → Situation summary → Who is affected → What we are doing → What affected parties should do → Next update commitment

## Post-Crisis Evaluation Framework

| Metric | What It Measures | Target |
|--------|-----------------|--------|
| Time to first statement | Response speed | Within response window for tier |
| Sentiment recovery time | Narrative recovery | Return to pre-crisis baseline within 30 days |
| Media narrative accuracy | Factual correctness of coverage | <10% coverage contains factual errors |
| Stakeholder trust score | Customer/employee confidence | Tracked via survey 30 and 90 days post-crisis |
| Tabletop pass rate | Team readiness | All escalation steps executed correctly |
