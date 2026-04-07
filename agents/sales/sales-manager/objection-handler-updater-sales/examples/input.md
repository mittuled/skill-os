# Objection Handler Updater — Example Input

## Scenario

After Q1 close, the Sales Manager collected objection data from 3 sources: call recordings (12 sessions), CRM loss reasons (8 closed-lost deals), and a team Slack thread. A new competitor pricing move has introduced a pricing objection that wasn't in the previous handler. One objection reveals a genuine product gap requiring Product team escalation.

## Input JSON

```json
{
  "source": "Q1 field data: call recordings, CRM loss reasons, Slack #sales-objections",
  "publish_to": "sales-playbook",
  "changelog_notes": "Q1 refresh: added Workday Prism pricing objection; updated timing objection for Q2 budget cycle; escalated data export limitation to Product",
  "objections": [
    {
      "text": "Workday Prism Analytics is now cheaper than PeopleMetrics for our volume",
      "category": "pricing",
      "frequency": 7,
      "deal_loss_correlation": true,
      "acknowledge": "Prism has been more competitively priced recently — I appreciate you flagging that directly.",
      "reframe": "The comparison breaks down on total cost of ownership — Prism requires a $50-150K SI engagement to configure and takes 4-6 months. PeopleMetrics is live in 2 weeks with zero PS cost.",
      "evidence": "Share Deel case study: Prism quote was $42K/year vs. PeopleMetrics $38K/year — but they avoided $90K in SI fees and went live 5 months earlier.",
      "escalation_needed": false
    },
    {
      "text": "We can't do this now — maybe next quarter when budget resets",
      "category": "timing",
      "frequency": 9,
      "deal_loss_correlation": true,
      "acknowledge": "Q1/Q2 budget transitions are genuinely challenging — it makes sense that timing feels off.",
      "reframe": "The risk of waiting is that manual reporting continues to cost you roughly 3 FTE-hours per week. At your scale, that's about $X/quarter in lost productivity while Q3 ramp gets delayed.",
      "evidence": "Offer: 'I can lock in Q1 pricing with a Q3 start date so you don't lose the budget window but the implementation fits your timeline.'",
      "escalation_needed": false
    },
    {
      "text": "We need to export raw workforce data to our data warehouse — your platform doesn't support bulk export",
      "category": "product_capability",
      "frequency": 6,
      "deal_loss_correlation": true,
      "acknowledge": "You're right — we don't currently support bulk raw data export to third-party warehouses.",
      "reframe": "We have a native Snowflake connector in beta and a roadmap commitment for GA in Q3 2026. In the meantime, our API can pull data programmatically.",
      "evidence": "Share API documentation; offer beta access to Snowflake connector.",
      "escalation_needed": true,
      "escalation_reason": "3 lost deals directly cited this gap in Q1. Product team should evaluate pulling Snowflake connector GA forward from Q3 to Q2."
    }
  ]
}
```
