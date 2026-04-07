# Framework: Help Centre Builder

Defines the architecture and content strategy for building a customer-facing help centre that deflects support tickets and enables self-service.

## Help Centre Architecture

### Information Architecture Principles

1. **Customer journey over product structure**: Organise by what customers are trying to do, not by how the product is built internally
2. **Three-level taxonomy max**: Category → Subcategory → Article (deeper nesting hides content)
3. **Progressive disclosure**: Start with the most common use case; link to advanced topics at the bottom of each article

### Taxonomy Model

| Level | Examples | Max Count |
|-------|----------|-----------|
| Category | Getting Started, Managing Your Account, Integrations, Billing, Troubleshooting | 5-8 |
| Subcategory | Getting Started → Initial Setup, Inviting Teammates, First Steps | 3-6 per category |
| Article | Initial Setup → Connect your first integration | Unlimited |

### Article Template

Every article follows this structure:
1. **Title**: Action-oriented (e.g., "Connect Slack to [Product]", not "Slack Integration")
2. **Problem statement**: One sentence stating when a customer reads this article
3. **Prerequisites**: What the customer needs before starting (access level, existing configuration)
4. **Step-by-step instructions**: Numbered; each step has one action
5. **Expected result**: What the customer should see when the task is complete
6. **Troubleshooting**: 2-3 common errors and fixes
7. **Related articles**: 2-4 cross-links to logically connected articles

### Ticket Deflection Targeting

| Article Priority Tier | Target Ticket Deflection | Criteria |
|----------------------|-------------------------|----------|
| P1 — High deflection | > 30 tickets / month | Answers the most-asked questions |
| P2 — Medium deflection | 10-29 tickets / month | Common use cases, not obvious from UI |
| P3 — Low deflection but required | < 10 tickets / month | Compliance, billing terms, policy articles |

## Maintenance Cadence

| Trigger | Action |
|---------|--------|
| Product release | Review all articles in affected product areas within 48h of launch |
| Ticket mentions article as unhelpful | Review and update within 5 business days |
| Article has > 20% "Not helpful" feedback | Flag for rewrite; escalate to content owner |
| Quarterly review | Full taxonomy review; deprecate stale articles |
| Search query with no results > 20 times | Create new article or update taxonomy to surface existing content |

## Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Ticket deflection rate | ≥ 20% of total ticket volume | (Article views that did not result in a ticket) / (Total article views) |
| Search success rate | ≥ 70% | Searches resulting in an article click / Total searches |
| CSAT on article | ≥ 75% "helpful" rating | Help centre feedback widget |
| Stale article rate | < 10% | Articles not updated in > 90 days |
