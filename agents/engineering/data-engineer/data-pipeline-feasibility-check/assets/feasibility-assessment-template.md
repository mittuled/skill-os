# Data Pipeline Feasibility Assessment

**Pipeline Name:** [PIPELINE NAME]
**Requested By:** [REQUESTOR NAME], [TEAM]
**Assessment Date:** [DATE]
**Assessed By:** [DATA ENGINEER NAME]
**Verdict:** [GO / NO-GO / CONDITIONAL GO]

---

## Executive Summary

[One paragraph summarising the overall feasibility outcome. State whether the pipeline can be built as specified, note the primary risk or constraint, and call out any conditions that must be satisfied before engineering begins.]

---

## 1. Source Verification Results

### Source Inventory

| Source System | Type | Auth Method | Connectivity | Status |
|---|---|---|---|---|
| [SOURCE 1] | REST API / DB / File | OAuth 2.0 / API Key / IAM | ✅ Verified / ❌ Failed | [NOTES] |
| [SOURCE 2] | REST API / DB / File | OAuth 2.0 / API Key / IAM | ✅ Verified / ❌ Failed | [NOTES] |
| [SOURCE 3] | REST API / DB / File | OAuth 2.0 / API Key / IAM | ✅ Verified / ❌ Failed | [NOTES] |

### Rate Limits and Constraints

| Source | Rate Limit | Burst Allowance | SLA Guarantee | Contractual? |
|---|---|---|---|---|
| [SOURCE 1] | [X] req/min | [Y] req/burst | [Z]% uptime | Yes / No |
| [SOURCE 2] | [X] req/min | [Y] req/burst | [Z]% uptime | Yes / No |

### Data Format Assessment

| Source | Format | Schema Stability | Version | Notes |
|---|---|---|---|---|
| [SOURCE 1] | JSON / CSV / Parquet | Stable / Unstable / Unknown | v[X] | [SCHEMA DRIFT RISK NOTE] |
| [SOURCE 2] | JSON / CSV / Parquet | Stable / Unstable / Unknown | v[X] | [SCHEMA DRIFT RISK NOTE] |

**Source verification outcome:** [All sources accessible and verified / [N] sources have unresolved issues — see blocker list]

---

## 2. Volume Forecast

### Sampling Methodology

- **Sample period:** [DATE RANGE]
- **Sample size:** [N] records / [X] GB
- **Sampling method:** [Full table scan / Random 10% sample / API pagination probe]

### Volume Estimates

| Metric | Current | 6-Month Projection | 12-Month Projection | Confidence |
|---|---|---|---|---|
| Row count (daily) | [N] rows | [N] rows | [N] rows | High / Medium / Low |
| Payload size (daily) | [X] GB | [X] GB | [X] GB | High / Medium / Low |
| Peak batch size | [X] GB | [X] GB | [X] GB | High / Medium / Low |
| Growth rate (MoM) | [X]% | [X]% | [X]% | High / Medium / Low |

### Volume Risk Notes

[Describe any assumptions or sources of uncertainty in the volume estimate. Flag if stakeholder-provided estimates differed significantly from sampled actuals.]

---

## 3. Infrastructure Gap Analysis

### Pipeline Requirements

| Resource | Required | Available | Gap |
|---|---|---|---|
| Compute (vCPU) | [X] vCPU | [Y] vCPU | [Z] vCPU shortfall / surplus |
| Memory (RAM) | [X] GB | [Y] GB | [Z] GB shortfall / surplus |
| Storage (raw) | [X] TB | [Y] TB | [Z] TB shortfall / surplus |
| Network bandwidth | [X] Gbps | [Y] Gbps | [Z] Gbps shortfall / surplus |
| Orchestrator slots | [X] worker slots | [Y] available | [Z] shortfall / surplus |

### Cost Estimates for Required Provisioning

| Resource | Action | Monthly Cost | One-Time Cost |
|---|---|---|---|
| [COMPUTE TIER] | Provision [X] additional nodes | $[METRIC]/mo | $[METRIC] |
| [STORAGE TIER] | Expand warehouse storage by [X] TB | $[METRIC]/mo | — |
| [NETWORK] | Increase egress allowance | $[METRIC]/mo | — |
| **Total additional cost** | | **$[METRIC]/mo** | **$[METRIC]** |

### Existing Infrastructure Assessment

- **Orchestrator:** [Airflow / Dagster / Prefect] — [adequate / at capacity / requires upgrade]
- **Data warehouse:** [BigQuery / Snowflake / Redshift] — [adequate / approaching limits]
- **Compute cluster:** [Spark / dbt / serverless] — [adequate / requires scaling]
- **Networking:** [VPC / public API] — [adequate / requires peering / VPN required]

---

## 4. Feasibility Verdict

### Overall Verdict: [GO / CONDITIONAL GO / NO-GO]

| Dimension | Result | Confidence | Blocker? |
|---|---|---|---|
| Source access | ✅ Pass / ❌ Fail / ⚠️ Conditional | High / Medium / Low | Yes / No |
| Volume feasibility | ✅ Pass / ❌ Fail / ⚠️ Conditional | High / Medium / Low | Yes / No |
| Infrastructure capacity | ✅ Pass / ❌ Fail / ⚠️ Conditional | High / Medium / Low | Yes / No |
| SLA achievability | ✅ Pass / ❌ Fail / ⚠️ Conditional | High / Medium / Low | Yes / No |

### Conditions (for Conditional GO)

1. [CONDITION 1] — Owner: [OWNER], Due: [DATE]
2. [CONDITION 2] — Owner: [OWNER], Due: [DATE]
3. [CONDITION 3] — Owner: [OWNER], Due: [DATE]

### Blockers (for NO-GO)

| Blocker | Dimension | Remediation | Estimated Effort |
|---|---|---|---|
| [BLOCKER 1] | Source / Volume / Infra / SLA | [REMEDIATION STEPS] | [X] days |
| [BLOCKER 2] | Source / Volume / Infra / SLA | [REMEDIATION STEPS] | [X] days |

### Risks (accepted for GO or Conditional GO)

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| [RISK 1] | High / Medium / Low | High / Medium / Low | [MITIGATION] |
| [RISK 2] | High / Medium / Low | High / Medium / Low | [MITIGATION] |

---

## 5. Recommended Next Steps

- [ ] [NEXT STEP 1] — Owner: [OWNER], Due: [DATE]
- [ ] [NEXT STEP 2] — Owner: [OWNER], Due: [DATE]
- [ ] [NEXT STEP 3] — Owner: [OWNER], Due: [DATE]

**Proceed to design:** Yes / No / Pending conditions above

---

*Assessment prepared by [DATA ENGINEER NAME] | Reviewed by [TECH LEAD / MANAGER] | [DATE]*
