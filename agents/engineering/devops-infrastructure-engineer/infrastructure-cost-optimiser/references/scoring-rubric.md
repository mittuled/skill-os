# Scoring Rubric: Infrastructure Cost Optimisation

Evaluates the thoroughness and impact of infrastructure cost optimisation analysis and implementation.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Cost Visibility | 20% | Completeness of cost breakdown by service, team, environment, and resource type |
| 2 | Waste Identification | 25% | Coverage of orphaned resources, idle capacity, and underutilised infrastructure |
| 3 | Right-Sizing Quality | 25% | Accuracy of sizing recommendations with performance risk assessment |
| 4 | Savings Validation | 15% | Post-implementation verification that savings materialised without performance impact |
| 5 | Sustainability | 15% | Recurring process, automated detection, and ongoing optimisation backlog |
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
| A+ | 9.0 – 10.0 | Exceptional | Comprehensive analysis with validated savings and automated ongoing detection | Publish report; schedule next review in 90 days |
| A | 8.0 – 8.9 | Strong | Thorough analysis with implemented savings; minor gaps in ongoing automation | Approve; implement automated waste detection within 30 days |
| B | 7.0 – 7.9 | Good | Solid analysis but savings not fully validated or some resource types missed | Complete validation; extend analysis to missing resource types |
| C | 5.0 – 6.9 | Adequate | Basic analysis covering compute only; data transfer and storage not analysed | Extend scope; compute-only optimisation misses 30-40% of spend |
| D | 3.0 – 4.9 | Weak | Superficial analysis; recommendations lack performance risk assessment | Redo with resource utilisation data and performance baselines |
| F | 0.0 – 2.9 | Failing | No cost analysis performed or recommendations are generic without data | Start with cost visibility tooling setup |

## Signal Tables

### Cost Visibility

| Score | Evidence |
|-------|----------|
| 9-10 | Cost breakdown by service, team, environment, and resource type with tagging compliance >95%; month-over-month trends analysed |
| 7-8 | Cost breakdown by service and environment; tagging compliance >80%; trends available |
| 5-6 | Account-level cost data only; partial tagging; no per-service attribution |
| 3-4 | Only total cloud bill reviewed; no tagging; no breakdown |
| 0-2 | No cost data collected or reviewed |

### Waste Identification

| Score | Evidence |
|-------|----------|
| 9-10 | Orphaned resources, unattached volumes, idle load balancers, unused IPs, over-provisioned databases all identified with dollar impact |
| 7-8 | Most waste categories covered; dollar impact calculated for major items |
| 5-6 | Only obvious waste (stopped instances, unattached volumes) identified |
| 3-4 | Anecdotal waste identification without systematic scan |
| 0-2 | No waste identification performed |

### Right-Sizing Quality

| Score | Evidence |
|-------|----------|
| 9-10 | Utilisation data over 30+ days; recommendations with projected savings and performance risk rating; reserved instance analysis included |
| 7-8 | Utilisation data over 14+ days; recommendations with savings estimates; performance risk noted |
| 5-6 | Utilisation data limited; recommendations based on instance type only; no performance risk assessment |
| 3-4 | Recommendations without utilisation data; "downsize everything" approach |
| 0-2 | No right-sizing analysis |

### Savings Validation

| Score | Evidence |
|-------|----------|
| 9-10 | Post-implementation cost comparison confirming savings; performance dashboards showing no degradation; savings tracked monthly |
| 7-8 | Savings confirmed via billing; performance spot-checked |
| 5-6 | Savings estimated but not yet confirmed post-implementation |
| 3-4 | Changes implemented without follow-up measurement |
| 0-2 | No validation performed |

### Sustainability

| Score | Evidence |
|-------|----------|
| 9-10 | Automated waste detection alerts; recurring review cadence scheduled; cost anomaly detection active; team ownership assigned |
| 7-8 | Recurring review scheduled; some automated detection; ownership assigned |
| 5-6 | Manual review planned; no automation; ownership unclear |
| 3-4 | One-time analysis with no follow-up plan |
| 0-2 | No sustainability plan |
