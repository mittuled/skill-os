# RevOps Scaling Initiative Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [RevOps analyst name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | revenue-operations-scaler |
| Assessment Period | [YYYY-MM-DD to YYYY-MM-DD] |
| CRM / Stack | [CRM name + key tools assessed] |

## Executive Summary

[2-3 sentences covering: current RevOps capacity status, the primary bottleneck identified, and the highest-priority scaling action. Example: "The Q3 2025 RevOps assessment reveals three critical bottlenecks — manual data entry consuming 75+ minutes per rep per day, lead routing latency averaging 42 minutes, and CRM report generation timing out for pipeline reviews. The highest-impact action is automating field population via email/calendar sync, projected to recover 6+ hours per rep per week. A phased 8-week scaling roadmap is included below."]

## Capacity Assessment Summary

[Current state across all monitored processes against warning and critical thresholds.

GUIDANCE: Mark rows in bold where current state exceeds Warning or Critical threshold. Include the number of reps or deals affected.]

| Process | Current State | Threshold Status | Reps/Deals Affected |
|---------|--------------|-----------------|---------------------|
| Manual data entry | [min/day per rep] | [OK / Warning / Critical] | [N reps] |
| CRM report generation | [hours] | [OK / Warning / Critical] | [N reports/week] |
| Deal-to-cash cycle | [business days] | [OK / Warning / Critical] | [N deals/month] |
| Lead routing latency | [minutes] | [OK / Warning / Critical] | [N leads/week] |
| Attribution data freshness | [hours/days] | [OK / Warning / Critical] | [N campaigns] |
| Forecast accuracy | [± %] | [OK / Warning / Critical] | [N forecast cycles] |

## Bottleneck Analysis

[Detailed breakdown of each identified bottleneck, ranked by impact score.

GUIDANCE: Calculate impact score using the formula: Impact Score = (Revenue at Risk × 0.4) + (Rep Productivity Hours Lost/Week × 0.3) + (Data Quality Degradation Score × 0.3). Present highest-score bottleneck first.]

### Bottleneck 1: [Process Name] — Impact Score: [X]

| Field | Value |
|-------|-------|
| Current State | [Metric vs. threshold] |
| Revenue at Risk | [$ ARR or pipeline value] |
| Rep Hours Lost/Week | [N hours × N reps] |
| Data Quality Degradation | [Score 1-10; describe impact] |
| Impact Score | [(R×0.4) + (H×0.3) + (D×0.3)] |
| Root Cause | [e.g., No email-to-CRM sync; reps manually entering all activity data] |
| Proposed Solution | [e.g., Enable HubSpot/Salesforce email sync + calendar integration] |
| Implementation Complexity | [Low / Medium / High] |

### Bottleneck 2: [Process Name] — Impact Score: [X]

| Field | Value |
|-------|-------|
| Current State | [Metric vs. threshold] |
| Revenue at Risk | [$ ARR or pipeline value] |
| Rep Hours Lost/Week | [N hours × N reps] |
| Data Quality Degradation | [Score 1-10; describe impact] |
| Impact Score | [(R×0.4) + (H×0.3) + (D×0.3)] |
| Root Cause | [Root cause] |
| Proposed Solution | [Solution] |
| Implementation Complexity | [Low / Medium / High] |

## Scaling Roadmap

[Phased implementation plan following the data-quality-first sequencing principle.

GUIDANCE: Always sequence: (1) data quality, (2) high-volume manual task automation, (3) reporting infrastructure, (4) advanced forecasting, (5) territory/quota tooling. Never skip phases. Never implement forecasting before data quality is resolved.]

### Phase 1: Data Quality (Weeks 1-2)

| Action | Owner | Tool | Success Metric |
|--------|-------|------|---------------|
| [e.g., Run deduplication audit] | [Team] | [DemandTools / RingLead] | [< X duplicate rate] |
| [e.g., Enforce required fields at stage gates] | [Team] | [CRM validation rules] | [100% field completion on Opp creation] |

### Phase 2: Manual Task Automation (Weeks 3-4)

| Action | Owner | Tool | Success Metric |
|--------|-------|------|---------------|
| [e.g., Enable email/calendar sync] | [Team] | [HubSpot / Salesforce Inbox] | [< 30 min/day data entry per rep] |
| [e.g., Automate lead routing rules] | [Team] | [CRM workflows / LeanData] | [< 5 min routing latency] |

### Phase 3: Reporting Infrastructure (Weeks 5-6)

| Action | Owner | Tool | Success Metric |
|--------|-------|------|---------------|
| [e.g., Build pre-aggregated pipeline dashboards] | [Team] | [Looker / Metabase] | [< 30 sec report load time] |
| [e.g., Schedule daily data refresh] | [Team] | [BI tool + CRM connector] | [Same-day attribution freshness] |

### Phase 4: Advanced Forecasting (Weeks 7-8, if Phase 1 complete)

| Action | Owner | Tool | Success Metric |
|--------|-------|------|---------------|
| [e.g., Deploy AI forecasting layer] | [Team] | [Clari / Gong] | [Forecast accuracy ± 10%] |

## Rollback Plan

[Define rollback trigger and method for each Phase 1-2 change before implementation begins.

GUIDANCE: Do not proceed to Phase 2 without rollback triggers documented for all Phase 1 changes.]

| Change | Rollback Trigger | Rollback Method | Owner |
|--------|-----------------|-----------------|-------|
| [Automation rule] | [> 5% misrouted leads in 48h] | [Disable automation; manual routing] | [Team] |
| [CRM field change] | [Reporting breaks or data corrupted] | [Restore from backup; field audit] | [Team] |
| [Integration change] | [Sync failure > 2 hours] | [Disable integration; manual entry interim] | [Team] |

## Expected Impact Summary

[Quantified before/after projections for each scaling initiative.]

| Metric | Baseline | Target | Expected Improvement | Measurement Date |
|--------|----------|--------|---------------------|-----------------|
| Rep data-entry time/day | [min] | [min] | [time saved × N reps] | [30 days post] |
| Lead routing latency | [min] | [min] | [% reduction] | [7 days post] |
| Report generation time | [hours] | [min] | [% reduction] | [14 days post] |
| Forecast accuracy | [± %] | [± %] | [improvement in pts] | [90 days post] |
| Data quality score | [score] | [score] | [% improvement] | [60 days post] |

## Appendices

### A. Bottleneck Scoring Detail

[Show full impact score calculation for all bottlenecks assessed, including those below the threshold for action.]

### B. Tool Evaluation

[For any scaling solution requiring a net-new tool, include a brief 3-column comparison: Tool | Key Capability | Integration Effort.]

### C. Stakeholder Sign-Off

| Stakeholder | Role | Sign-Off Date | Notes |
|-------------|------|---------------|-------|
| [Name] | VP Sales / CRO | [Date] | |
| [Name] | Head of Marketing | [Date] | |
| [Name] | Finance / CFO | [Date] | |
