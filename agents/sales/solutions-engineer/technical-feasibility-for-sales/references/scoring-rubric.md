# Scoring Rubric: technical-feasibility-for-sales

Evaluates the technical feasibility of a prospect's requirements against product capabilities by scoring functional fit, integration complexity, performance requirements, security/compliance alignment, and deployment compatibility.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Functional Fit | 30% | Degree to which the product's current capabilities meet the prospect's functional requirements |
| 2 | Integration Complexity | 25% | Effort and risk associated with connecting the product to the prospect's existing systems |
| 3 | Performance Requirements | 15% | Ability to meet the prospect's scale, latency, and throughput needs |
| 4 | Security & Compliance | 20% | Alignment with the prospect's security standards, certifications, and regulatory requirements |
| 5 | Deployment Compatibility | 10% | Compatibility with the prospect's infrastructure, hosting preferences, and operational model |
| **Total** | | **100%** | |

## Scale

Each criterion is scored **0-10**:
- **0**: No capability / fundamentally incompatible
- **5**: Partially capable with significant workarounds or roadmap dependencies
- **10**: Fully capable, no gaps, production-ready

**Composite Score** = Sum (criterion score x weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 - 10.0 | Exceptional | All requirements fully supported; no gaps, workarounds, or roadmap dependencies | Proceed to POC immediately; position as a technical best-fit in the proposal |
| A | 8.0 - 8.9 | Strong | All must-have requirements met; minor nice-to-haves require configuration or workaround | Proceed to POC; document workarounds in the proposal; no deal risk |
| B | 7.0 - 7.9 | Good | Must-have requirements met with 1-2 documented workarounds; no dealbreaker gaps | Proceed with conditions; brief AE on workaround positioning; monitor prospect reaction |
| C | 5.0 - 6.9 | Adequate | 1-2 must-have requirements partially met via workaround or near-term roadmap item | Proceed cautiously; require product team confirmation on roadmap commitments; flag risk to AE |
| D | 3.0 - 4.9 | Weak | Multiple must-have gaps; workarounds are fragile or unacceptable to most enterprise buyers | Recommend deferral; escalate to product team for gap assessment; do not commit to POC |
| F | 0.0 - 2.9 | Failing | Fundamental incompatibility; dealbreaker gaps with no viable path to resolution | Disqualify the technical fit; recommend AE withdraw or pivot the conversation |

## Criterion Detail

### 1. Functional Fit (30%)

| Score | Evidence |
|-------|----------|
| 9-10 | All functional requirements are natively supported; prospect's use cases map directly to existing product workflows; no customization needed |
| 7-8 | Core functional requirements met; 1-2 edge cases require configuration or admin setup; all workarounds are standard and well-documented |
| 5-6 | Primary use case supported but secondary use cases require workarounds; some requirements met through integration rather than native capability |
| 3-4 | Core use case partially supported; multiple requirements need custom development or are on the roadmap without confirmed dates |
| 0-2 | Fundamental functional mismatch; the product does not serve the prospect's primary use case |

### 2. Integration Complexity (25%)

| Score | Evidence |
|-------|----------|
| 9-10 | Pre-built connectors exist for all required integrations; standard REST/GraphQL APIs cover all data flows; integration can be configured in hours |
| 7-8 | Pre-built connectors for most integrations; 1-2 require custom API mapping but are straightforward; integration effort is days, not weeks |
| 5-6 | Some integrations require custom middleware or ETL; data format transformations needed; integration effort is 1-3 weeks |
| 3-4 | Multiple integrations require custom development; legacy systems with poor API support; significant data mapping complexity; 4-8 week effort |
| 0-2 | No viable integration path; prospect systems use proprietary protocols with no API; or integration would require rebuilding core data flows |

### 3. Performance Requirements (15%)

| Score | Evidence |
|-------|----------|
| 9-10 | Product benchmarks exceed prospect's requirements by 2x+; architecture natively supports the required scale and latency |
| 7-8 | Product meets performance requirements at stated scale; headroom exists for 50%+ growth; standard configuration sufficient |
| 5-6 | Product meets requirements at current scale but may require optimization for growth; some tuning or infrastructure scaling needed |
| 3-4 | Product approaches limits at the prospect's stated scale; performance under peak load is uncertain; significant optimization required |
| 0-2 | Product cannot meet stated performance requirements; architectural limitations prevent scaling to the required level |

### 4. Security & Compliance (20%)

| Score | Evidence |
|-------|----------|
| 9-10 | All required certifications held (SOC 2, ISO 27001, HIPAA, etc.); encryption, audit logging, and access controls exceed requirements; compliance documentation available on request |
| 7-8 | Primary certifications held; 1-2 secondary compliance items in progress with confirmed completion dates; security architecture meets requirements |
| 5-6 | Core security features present but specific compliance certification pending or not applicable; prospect may need to accept risk for non-critical items |
| 3-4 | Significant compliance gaps; required certifications not held and not in progress; security architecture requires modifications |
| 0-2 | Fundamental security incompatibility; product cannot meet regulatory requirements for the prospect's industry (e.g., data residency, encryption standards) |

### 5. Deployment Compatibility (10%)

| Score | Evidence |
|-------|----------|
| 9-10 | Product deployment model matches exactly (SaaS/on-prem/hybrid as required); supported cloud providers align; network architecture compatible |
| 7-8 | Primary deployment model matches; minor adjustments to network configuration or cloud region selection needed |
| 5-6 | Deployment model requires adaptation (e.g., prospect wants on-prem but product is SaaS-only with VPC option); feasible but adds complexity |
| 3-4 | Deployment model mismatch requires significant effort (e.g., product is SaaS-only, prospect requires on-prem with no cloud connectivity) |
| 0-2 | Deployment model fundamentally incompatible; no viable path to meet the prospect's infrastructure requirements |

## Gap Severity Classification

| Severity | Definition | Deal Impact |
|----------|-----------|-------------|
| Dealbreaker | Must-have requirement with no workaround and no confirmed roadmap | Red flag — likely disqualify |
| Manageable | Must-have requirement with a viable workaround that meets the spirit of the requirement | Yellow flag — position proactively |
| Deferrable | Nice-to-have requirement that can be addressed post-sale or in a future release | Green — acknowledge and defer |

## Feasibility Verdict

| Verdict | Criteria | AE Guidance |
|---------|----------|-------------|
| **Green** | Composite >= 7.0, no dealbreaker gaps | Proceed confidently; highlight technical fit as a differentiator |
| **Yellow** | Composite 5.0-6.9, or has manageable gaps | Proceed with documented conditions; proactively position workarounds in proposal |
| **Red** | Composite < 5.0, or has any dealbreaker gap | Recommend disqualification or deferral; escalate to product for gap assessment |
