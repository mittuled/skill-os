---
name: sla-definer
description: >
  This skill defines the service-level agreements that the product will commit
  to for customers, covering uptime, latency, support response times, and
  remediation policies. Use when preparing a product for GA or enterprise sales
  that require contractual SLAs. Also consider when renegotiating existing SLAs
  after architecture changes or incident post-mortems. Suggest when deal-desk
  escalations cite missing or unclear SLA language as a blocker.
department: product
agent: vp-product
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "define sla"
  - "sla definition"
  - "service level agreement"
  - "set slas"
  - "sla setting"
---

# sla-definer

## Agent: VP Product
L1 product leader responsible for opportunity framing, MVP definition, PRD assembly, go-live coordination, and post-launch monitoring. Owns the product strategy and roadmap from idea through GA.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Defines the service-level agreements that the product will commit to for customers.

## When to Use
- When a product is approaching GA and enterprise buyers require contractual SLA commitments
- When entering a new market segment (e.g., healthcare, financial services) with regulatory SLA expectations
- When post-incident reviews reveal that existing SLAs are misaligned with actual system capabilities
- When Sales escalations indicate that missing or vague SLA terms are stalling deal closure

## Workflow
1. **Audit current capabilities**: Gather historical data on uptime, p50/p95/p99 latency, incident frequency, MTTR, and support response times from engineering and ops. Deliverable: system performance baseline report.
2. **Benchmark against market**: Research SLA terms offered by direct competitors and adjacent products in the same buyer segment. Note where the market floor and ceiling sit for each metric. Deliverable: competitive SLA benchmark.
3. **Define SLA metrics**: Select the specific metrics to include — availability percentage, response-time percentiles, support-tier response windows, RTO/RPO for disaster recovery, and data-processing throughput guarantees. Deliverable: SLA metric definitions.
4. **Set target thresholds**: Propose numeric targets for each metric that are achievable with current architecture and headroom for growth. Stress-test targets against worst-case scenarios from the incident history. Deliverable: proposed SLA targets with confidence intervals.
5. **Design remediation and credit policies**: Define what happens when an SLA is breached — service credits, escalation paths, root-cause disclosure timelines, and customer notification protocols. Deliverable: SLA remediation policy.
6. **Review with Engineering and Legal**: Validate that Engineering can instrument, measure, and alert on every SLA metric. Confirm that Legal approves the contractual language and liability exposure. Deliverable: engineering feasibility sign-off and legal review.
7. **Publish the SLA document**: Finalize the SLA in both customer-facing and internal versions. The customer-facing version goes into contract templates; the internal version includes monitoring runbooks and escalation procedures. Deliverable: published SLA document (external + internal).

## Anti-Patterns
- **Aspirational SLAs**: Committing to targets the system cannot currently meet, hoping infrastructure improvements will close the gap before a breach. *Why*: Breached SLAs erode customer trust and trigger financial credits that compound quickly.
- **Copy-paste SLAs**: Adopting a competitor's SLA verbatim without validating against your own architecture and ops maturity. *Why*: Your system characteristics differ; borrowed targets may be unachievable or too conservative.
- **Metric-free SLAs**: Using vague language like "high availability" or "best-effort response" without numeric commitments. *Why*: Ambiguous SLAs create disputes during incidents and undermine the credibility of the product in enterprise procurement.
- **SLAs without monitoring**: Publishing SLA targets without instrumented dashboards and alerting to detect breaches proactively. *Why*: If you cannot measure it, you cannot manage it, and customers will discover breaches before you do.

## Output
**On success**: A published SLA document (customer-facing and internal) containing metric definitions, numeric targets, measurement methodology, remediation and credit policies, and monitoring runbook references — approved by Engineering, Legal, and Product.
**On failure**: Report which metrics lack sufficient historical data, what architectural gaps prevent commitment, the best available interim SLA (e.g., best-effort with transparency commitments), and a roadmap to close gaps for a full SLA in a defined timeframe.

## Related Skills
- (none yet — cross-references added in Phase 1.6)
