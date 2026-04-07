# Framework: Revenue Operations Scaling

Defines the capacity assessment model, bottleneck prioritisation criteria, and scaling solution patterns for RevOps infrastructure.

## Capacity Assessment Model

### Volume Stress Thresholds

| Process | Current State | Warning Threshold | Critical Threshold |
|---------|--------------|-------------------|--------------------|
| Manual data entry | < 30 min/day per rep | 30-60 min/day | > 60 min/day |
| CRM report generation | < 2 hours | 2-4 hours | > 4 hours or timeout |
| Deal-to-cash cycle | < 5 business days | 5-10 days | > 10 days |
| Lead routing latency | < 5 minutes | 5-30 minutes | > 30 minutes |
| Attribution data freshness | Same day | Next day | > 2 days |
| Forecast accuracy | ± 10% vs. actuals | ± 15% | > ± 20% |

### Bottleneck Impact Scoring

**Impact Score** = (Revenue at Risk × 0.4) + (Rep Productivity Hours Lost/Week × 0.3) + (Data Quality Degradation Score × 0.3)

Prioritise bottlenecks with the highest impact scores first.

## Scaling Solution Patterns

| Bottleneck Type | Scaling Solution | Implementation Complexity |
|----------------|------------------|--------------------------|
| Manual data entry | Field auto-population from email/calendar sync; Zapier/n8n automation | Low |
| Slow reporting | Pre-built dashboard with scheduled data refresh; BI layer (Looker/Metabase) | Medium |
| Lead routing lag | Rules-based auto-assignment; CRM workflow with tiered logic | Low |
| Forecast inaccuracy | AI forecasting add-on (Clari/Gong); stage-weighted probability recalibration | Medium-High |
| Duplicate records | Automated deduplication tool (DemandTools / RingLead); merge workflows | Medium |
| Integration data lag | Replace nightly batch sync with real-time webhook integration | High |
| Territory management | Territory planning tool (Varicent / Xactly); automated account routing | High |

## Scaling Implementation Sequencing

Implement scaling solutions in this order to maximise value and minimise disruption:

1. **Data quality first**: Clean and deduplicate existing data before building automation on top of it
2. **Automate highest-volume manual tasks**: Quick wins that free up rep time immediately
3. **Improve reporting infrastructure**: Ensure decisions are based on accurate, timely data
4. **Add advanced forecasting**: Only valuable after data quality and pipeline hygiene are established
5. **Territory and quota tooling**: Complex; implement during annual planning cycle, not mid-year

## Rollback Protocol

For each scaling change, define a rollback trigger before implementation:

| Change | Rollback Trigger | Rollback Method |
|--------|-----------------|-----------------|
| New automation rule | > 5% of leads misrouted in first 48h | Disable automation; revert to manual routing |
| CRM field change | Reporting breaks or field values corrupted | Restore from backup; field audit |
| Integration change | Data sync failure > 2 hours | Disable integration; manual data entry as interim |
| New forecasting model | Forecast error > previous model for 2+ weeks | Revert to previous model; keep new as parallel track |

## Post-Implementation Metrics

Capture before/after metrics for every scaling initiative:

| Metric | Capture Timing | Purpose |
|--------|---------------|---------|
| Rep data-entry time per day | Before + 30 days after | Quantify time savings |
| Lead routing latency | Before + 7 days after | Verify routing improvement |
| Report generation time | Before + 14 days after | Confirm BI performance gain |
| Forecast accuracy | Before + 90 days after | Allow sufficient deal cycles for measurement |
| Data quality score | Before + 60 days after | Confirm deduplication impact |
