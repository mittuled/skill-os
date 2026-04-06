# Checklist: unit-economics-monitor

Covers the recurring steps required to complete a unit economics monitoring cycle without gaps.

## Pre-Monitoring Setup

- [ ] Confirm close is complete and actuals are finalized for the period
- [ ] Verify marketing spend is attributed by channel (inbound, outbound, partner) in the source system
- [ ] Confirm sales compensation data is available including commissions, bonuses, and OTE
- [ ] Verify customer-level revenue data is available segmented by SMB, mid-market, and enterprise
- [ ] Confirm current churn rate data is available from the subscription system

## CAC Calculation

- [ ] Sum all sales and marketing spend for the period by channel
- [ ] Include: media spend, agency fees, sales salaries, commissions, sales tools, allocated overhead
- [ ] Divide total channel spend by new customers acquired through that channel
- [ ] Break out CAC by segment (SMB, mid-market, enterprise)
- [ ] Compare CAC to prior period — flag if any channel increased >15% month-over-month
- [ ] Document the CAC methodology including any cost allocation decisions

## LTV Calculation

- [ ] Calculate average revenue per customer by segment using gross-margin-weighted ACV
- [ ] Pull current gross margin percentage by segment from the GL
- [ ] Calculate gross-margin LTV = (ARPU × gross margin) / monthly churn rate
- [ ] Calculate contribution-margin LTV using contribution margin in place of gross margin
- [ ] Document any churn rate source — ensure it is current, not a historical assumption
- [ ] Flag if gross-margin LTV and contribution-margin LTV diverge by >20%

## Ratio and Payback Analysis

- [ ] Calculate LTV/CAC ratio per segment and channel
- [ ] Compare against target thresholds: LTV/CAC >3x, CAC payback <18 months
- [ ] Calculate CAC payback period = CAC / (ARPU × gross margin %)
- [ ] Flag any segment or channel below LTV/CAC 3x
- [ ] Flag any segment or channel with payback >18 months
- [ ] Compare ratios to prior 3 periods to identify direction of change

## Trend Analysis

- [ ] Plot 6-month trend for: blended CAC, CAC by channel, LTV, LTV/CAC ratio, payback period
- [ ] Calculate rate of change for each metric (month-over-month percentage change)
- [ ] Distinguish inflection points from noise — require ≥2 consecutive periods of movement before flagging as trend
- [ ] Identify any metric trending toward threshold breach within 2 months

## Alert and Escalation

- [ ] List every metric that has breached its threshold this period
- [ ] List every metric trending toward breach within 2 months
- [ ] For each alert: identify root cause, affected channels/segments, and recommended action
- [ ] Route alert memo to CFO and growth leadership with 48-hour response requested
- [ ] Update the rolling forecast with any CAC or churn assumption changes implied by the analysis

## Output Quality Check

- [ ] All CAC figures are fully-loaded (no partial cost exclusions)
- [ ] All LTV figures use current churn rates, not stale assumptions
- [ ] Channel-level CAC is reported (no blended-only reporting)
- [ ] Trend charts cover at least 6 months
- [ ] Alert memo includes specific action items (not generic recommendations)
- [ ] Report is consistent with prior-period methodology or differences are documented
