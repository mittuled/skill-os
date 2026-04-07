# Framework: Nurture Campaign Builder

Defines the structural framework for building MQL nurture sequences that advance leads through the buyer journey.

## Nurture Architecture

### Entry Criteria
- Lead score threshold met (MQL definition)
- Specific form submission or content engagement trigger
- Sales-rejected lead recycled back to marketing

### Exit Criteria
- Lead requests demo or meeting (hand to sales)
- Lead score reaches SQL threshold
- Lead has been in nurture > 90 days without engagement progression
- Lead unsubscribes or marks as spam

### Stage Model

| Stage | Goal | Content Type | Cadence | Exit Signal |
|-------|------|-------------|---------|-------------|
| Awareness | Educate on problem space | Blog posts, industry reports, trend pieces | 1 email / 5 days | Clicks on consideration-stage content |
| Consideration | Differentiate solution | Comparison guides, webinars, analyst reports | 1 email / 4 days | Downloads decision-stage asset |
| Decision | Drive action | Case studies, ROI calculators, free trial offers | 1 email / 3 days | Books demo or starts trial |

### Branch Logic

| Signal | Action |
|--------|--------|
| Opens all emails, no clicks | Switch to shorter, CTA-focused format |
| Clicks content but ignores CTAs | Extend consideration stage with deeper content |
| High engagement burst | Accelerate to decision stage; alert sales for parallel outreach |
| No engagement for 3 sends | Move to re-engagement sequence; reduce frequency |
| Visits pricing page | Skip to decision stage immediately |

## Email Design Principles

1. **One CTA per email**: Every email drives a single action aligned to the current stage
2. **Progressive disclosure**: Each email reveals one new insight; avoid information overload
3. **Segment-specific messaging**: CFO track focuses on ROI; technical track focuses on integration ease
4. **Social proof escalation**: Start with industry data, progress to peer companies, end with named case studies
