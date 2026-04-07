# Unit Economics Gate Decision: SMB Self-Serve — Meridian AI

| Field | Value |
|-------|-------|
| Company | Meridian AI |
| Segment | SMB Self-Serve |
| Gate Decision | CONDITIONAL PASS |
| Runway | 18 months |
| Target Payback | 14 months |
| Primary Risk Driver | CAC +25% |
| Skill | unit-econ-viability-gate |

## Scenario Analysis

| Scenario | LTV | LTV/CAC | Payback | Gross Margin | Verdict |
|----------|-----|---------|---------|--------------|---------|
| Base | $8.5K | 2.65x | 15.1mo | 71.0% | CONDITIONAL PASS |
| Churn +2pp | $4.7K | 1.48x | 15.1mo | 71.0% | FAIL |
| CAC +25% | $8.5K | 2.12x | 18.9mo | 71.0% | CONDITIONAL PASS |
| Margin -5pp | $7.4K | 2.30x | 16.6mo | 66.0% | CONDITIONAL PASS |

## Break-Even Thresholds

- Minimum ARPU for LTV/CAC ≥ 3.0x: **$338/month**
- Maximum CAC for LTV/CAC ≥ 3.0x: **$2.8K**
- Gross margin floor: **55.0%**

## Sensitivity Matrix — LTV/CAC Impact

| Stress Variable | Change | LTV/CAC Impact | Primary Driver |
|-----------------|--------|----------------|----------------|
| Monthly churn | +2pp | -1.17x | No |
| CAC | +25% | -0.53x | Yes |
| Gross margin | -5pp | -0.35x | No |

## Gate Decision: CONDITIONAL PASS

**Conditions and required actions:**
1. [Base] LTV/CAC meets minimum but has room to improve
2. [Churn +2pp] LTV/CAC 1.48x below minimum 3.0x
3. [CAC +25%] LTV/CAC meets minimum but has room to improve
4. [Margin -5pp] LTV/CAC meets minimum but has room to improve

## Monitoring Triggers

| Trigger | Threshold | Action |
|---------|-----------|--------|
| Monthly churn exceeds | 4.5% | Re-run gate |
| CAC exceeds | $2.8K | Re-run gate |
| Gross margin falls below | 66.0% | Re-run gate |
| LTV/CAC falls below | 3.0x for 2 consecutive months | Board notification |
