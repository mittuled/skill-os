# Cold Outreach Builder — Example Input

## Scenario

An SDR is building a 5-touch cold outreach sequence targeting Sarah Kim, the new VP of Operations at Deel (recently joined from Stripe). Sarah is problem-aware — she acknowledges the challenge of compliance tooling at scale but hasn't actively evaluated solutions. The campaign targets APAC expansion compliance needs.

## Input JSON

```json
{
  "prospect_name": "Sarah Kim",
  "company": "Deel",
  "persona_role": "VP of Operations",
  "buying_stage": "problem_aware",
  "seniority_level": "vp_director",
  "personalization_tokens": {
    "company_name": "Deel",
    "first_name": "Sarah",
    "pain_point": "APAC expansion compliance at scale",
    "trigger_event": "Assemble acquisition in Feb 2024",
    "mutual_connection": "James Liu (Stripe alumni network)",
    "competitor_reference": "Remote.com"
  },
  "ab_test_hypothesis": "Pain framing (APAC compliance risk) vs. aspiration framing (fastest APAC expansion)",
  "email_drafts": [
    {
      "subject": "Deel's APAC expansion — the compliance gap most teams miss",
      "body_preview": "Sarah — expanding into APAC compresses timelines on compliance in ways that catch even experienced ops teams off guard. Three weeks ago one of Deel's peers had to delay Singapore launch by 6 weeks because their payroll stack couldn't handle CPF contributions.",
      "cta": "Worth a 15-minute call to share what we've seen?"
    },
    {
      "subject": "The Assemble integration and what it means for compliance workflows",
      "body_preview": "Two acquisitions in 6 months means two sets of workflows to reconcile. The compliance surface area compounds quickly — especially when employee classifications differ by entity.",
      "cta": "Happy to share how similar companies solved this. 15 minutes?"
    },
    {
      "subject": "How Stripe's ops team handled 10-country expansion",
      "body_preview": "Given your background at Stripe, you've probably seen the compliance debt that builds up during rapid international expansion firsthand. Here's what worked for them...",
      "cta": "Want to compare notes on the APAC stack?"
    },
    {
      "subject": "One resource before you finalize the APAC compliance stack",
      "body_preview": "Sharing our 2024 APAC Payroll Compliance Benchmark — it covers CPF/EPF regulatory changes and the tooling gaps we see most commonly in companies at Deel's growth stage.",
      "cta": "Can I send it over? Or 15 minutes to walk through it together?"
    },
    {
      "subject": "Moving on — but leaving the door open",
      "body_preview": "I've reached out a few times but clearly the timing isn't right. No hard feelings — I'll stop here. If APAC compliance complexity surfaces as a priority, I'm a quick message away.",
      "cta": "No action needed."
    }
  ],
  "ab_variants": {
    "email_1_subject_a": "Deel's APAC expansion — the compliance gap most teams miss",
    "email_1_subject_b": "How fast-growing companies close their APAC expansion in half the time",
    "email_3_subject_a": "How Stripe's ops team handled 10-country expansion",
    "email_3_subject_b": "The APAC compliance debt most VP Ops discover too late"
  }
}
```
