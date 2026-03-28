# Framework: Solutions Engineering Playbook Construction

## Purpose

Provides the methodology for building an SE playbook that drives consistent technical engagement quality across the team.

## Technical Discovery Design

### Three-Phase Discovery Model

| Phase | Purpose | Timing | Key Questions |
|-------|---------|--------|---------------|
| Environment Assessment | Understand the prospect's current stack, constraints, and integration landscape | First SE call | Current tools, data flows, security requirements, deployment preferences |
| Use Case Validation | Validate that the product addresses the prospect's primary workflows and edge cases | Second SE call or within demo | Primary use case, secondary use cases, scale requirements, edge cases |
| Decision Criteria Mapping | Map the prospect's must-haves, nice-to-haves, and dealbreakers | Throughout evaluation | Evaluation criteria, weighting, comparison methodology, timeline |

### Question Design Principles

1. **Start broad, then narrow**: "Tell me about your current workflow" before "What API do you use for X?"
2. **Technical credibility first**: Demonstrate understanding of their stack before asking about limitations
3. **Uncover constraints, not just requirements**: "What can't you change?" is more revealing than "What do you need?"
4. **Map to architecture**: Every answer should update your mental model of their technical environment
5. **Listen for unstated requirements**: Security, compliance, and performance requirements are often assumed, not stated

### Red Flag Indicators

| Red Flag | What It Means | Recommended Action |
|----------|--------------|-------------------|
| "We need this to work exactly like [competitor]" | Evaluation biased toward incumbent; may be a validation exercise | Probe: "What specifically about that approach works for you?" Redirect to outcomes |
| "Can you just send us a sandbox?" | Prospect wants to self-evaluate without SE guidance | Insist on guided evaluation: "We find prospects get 3x more value from our guided approach" |
| "Our security team will review later" | Security may kill the deal late-stage | Engage security early: "Let's involve them now so there are no surprises" |
| Cannot articulate success criteria | Prospect not serious or too early in evaluation | Pause POC discussion; return to discovery |

## POC Design Standards

### Entry Criteria Matrix

| Criterion | Minimum Threshold | Rationale |
|-----------|------------------|-----------|
| Deal ACV | Company-defined minimum (typically $25K+) | SE time investment must be proportional to deal value |
| MEDDIC Score | 12/18 minimum | Deal must be qualified before investing SE capacity |
| Executive Sponsor | Named and confirmed by AE | Without sponsor, POC results may not drive decision |
| Decision Timeline | Committed date within 30 days of POC end | Open-ended POCs become free consulting |
| Technical Champion | Identified and engaged | Someone must actively participate in evaluation |

### Scope Control Method

| Element | Boundary | Enforcement |
|---------|----------|-------------|
| Use cases | Maximum 3 | Written in scope document; additional requests deferred to post-sale |
| Duration | Maximum 14 business days (standard), 21 (complex) | End date in scope document; extensions require Sales Manager approval |
| Data | Sample data only; no production data during POC | Pre-defined dataset; production migration is post-sale |
| Integrations | Primary integration only; secondary integrations post-sale | One integration in scope; others documented as "validated feasible" |
| Support | Business-hours support; SLA: 4-hour response | Documented in scope; after-hours requests escalated |

### Success Criteria Design

Every POC success criterion must be:
- **Measurable**: Quantified (e.g., "process 1,000 records in <5 minutes" not "handles data well")
- **Pre-agreed**: Written in scope document before POC starts; signed by both sides
- **Binary**: Pass or fail; no "partially met"
- **Achievable**: Validated as technically feasible before POC begins
- **Buyer-defined**: Criteria come from the buyer, not suggested by the seller

## Demo Framework Design

### Persona-Specific Demo Architecture

| Persona | Duration | Focus | Demo Style | Avoid |
|---------|----------|-------|------------|-------|
| Technical Evaluator | 45-60 min | Architecture, APIs, integration, security | Live, interactive, allow them to drive | High-level marketing slides |
| Business Buyer | 20-30 min | Outcomes, ROI, workflow transformation | Polished, narrative-driven, data-heavy | Deep technical details, jargon |
| End User | 30-45 min | Daily workflow, UX, time savings | Hands-on, scenario-based, relatable | Architecture diagrams, pricing |

### Demo Environment Standards

| Requirement | Standard |
|-------------|----------|
| Availability | 99.9% uptime during business hours; tested 1 hour before every demo |
| Data | Realistic sample data matching the prospect's industry when possible |
| Configuration | Pre-configured for the prospect's primary use case |
| Branding | Neutral branding (not another customer's data) |
| Backup | Recorded backup demo available in case of environment failure |

## Competitive Technical Analysis Method

### Comparison Dimensions

| Dimension | What to Compare | Data Sources |
|-----------|----------------|-------------|
| Architecture | Cloud-native vs. legacy, multi-tenant vs. single-tenant, API-first vs. UI-first | Product documentation, technical blog posts, SE evaluation |
| Performance | Throughput, latency, concurrent users, data volume limits | Published benchmarks, POC results, third-party tests |
| Integration Ecosystem | API coverage, pre-built connectors, webhook support, SDK availability | API documentation, marketplace listings, integration guides |
| Security Posture | Certifications (SOC2, ISO, HIPAA), encryption, access controls, audit logging | Security whitepapers, compliance pages, third-party audits |
| Deployment Model | SaaS, self-hosted, hybrid options, data residency options | Product documentation, pricing pages |

### Trap Question Design

For each competitor weakness:
1. Identify a specific limitation (verified, not assumed)
2. Frame a question the prospect should ask the competitor
3. Ensure the question sounds natural (not leading)
4. Prepare our response to the same question (we must pass our own trap)

## SE Engagement Model

### Time Allocation by Deal Tier

| Tier | ACV Range | Max SE Hours | Engagement Type | Approval |
|------|-----------|-------------|-----------------|----------|
| 1 | $100K+ | 40 hours | Full POC + dedicated SE | SE Manager |
| 2 | $50K-$99K | 20 hours | Guided demo + light POC | SE Manager |
| 3 | $25K-$49K | 8 hours | Standard demo + async technical review | Self-serve |
| Below threshold | <$25K | 2 hours | Recorded demo + FAQ document | None (self-serve) |
