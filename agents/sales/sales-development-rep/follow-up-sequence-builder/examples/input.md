# Follow-Up Sequence Builder — Example Input

## Scenario

An AE gave a product demo to the Head of RevOps at Cloudscale Inc. two days ago. The demo went well — the prospect asked detailed questions and mentioned a Q2 budget cycle. However, they haven't responded to the AE's follow-up email sent immediately after the demo. The SDR is now tasked with building a structured follow-up sequence.

## Input JSON

```json
{
  "prospect_name": "Marcus Webb",
  "company": "Cloudscale Inc.",
  "scenario": "post_demo",
  "engagement_context": "Demo 2 days ago — high engagement (asked about API integration, pricing, and Q2 timeline). No response to AE's Day 0 follow-up email.",
  "exit_action": "Archive and flag for re-engagement in 60 days; notify AE",
  "escalation_trigger": "Marcus changes role, Cloudscale raises funding, or competitor announcement",
  "touches": [
    {
      "value_add": "Demo recap + action items",
      "body_preview": "Marcus — great conversation Tuesday. Sending over the key points we covered and the three questions you asked about API integration with Salesforce.",
      "cta": "Does Thursday or Friday work for a 20-minute follow-up to answer those?"
    },
    {
      "value_add": "Integration documentation + customer story",
      "body_preview": "Wanted to share the Salesforce integration docs you asked about, plus a quick case study from a RevOps team similar to yours who cut their reporting time by 60%.",
      "cta": "Worth a quick call to see if the same setup applies to Cloudscale?"
    },
    {
      "value_add": "Q2 timeline check-in",
      "body_preview": "You mentioned Q2 as a target for getting new tooling in place. With procurement typically taking 3-4 weeks, we'd need to start the paperwork by mid-April to hit that window.",
      "cta": "Happy to send over a draft SOW if that's useful. 15 minutes this week?"
    },
    {
      "value_add": "New product feature announcement",
      "body_preview": "Relevant update since we spoke: we just released native HubSpot integration that eliminates the manual sync you mentioned as a pain point in the demo.",
      "cta": "Want to see a quick 10-min walkthrough of the new feature?"
    },
    {
      "value_add": "Graceful close",
      "body_preview": "I've reached out a few times since the demo. I don't want to keep interrupting if the timing has shifted — I'll leave the door open. Feel free to reach out when Q2 priorities come back into focus.",
      "cta": "No action needed."
    }
  ]
}
```
