# Framework: Support Pre-Briefing

## Core Model

A structured handoff from product to support that translates release information into support-ready materials before the feature goes live.

## Brief Structure

1. **Release Summary**: What changed, who it affects, release date
2. **FAQ**: Top 5-10 anticipated customer questions with answers
3. **Troubleshooting Steps**: Known issues with step-by-step workarounds
4. **Escalation Guide**: When to escalate, to whom, with what information

## Timing Protocol

| Milestone | Action | Owner |
|-----------|--------|-------|
| T-7 days | Brief drafted | Product Manager |
| T-5 days | Support lead reviews and flags gaps | Support Lead |
| T-3 days | Brief finalised, FAQ and escalation guide complete | Product Manager |
| T-1 day | Support team briefed (live walkthrough if major change) | Support Lead |

## FAQ Template

| # | Question | Answer | Applies To |
|---|----------|--------|-----------|
| 1 | "Why does X look different now?" | [Explain the change and benefit in customer language] | All users |
| 2 | "How do I do Y with the new feature?" | [Step-by-step instructions] | Users of feature Y |

## Escalation Decision Tree

1. Customer reports data loss or corruption → **Escalate immediately** to engineering on-call
2. Customer reports feature not working as documented → **Check known issues list** → if matches, provide workaround → if not, escalate to product ops
3. Customer asks about undocumented behaviour → **Log as feedback** and provide current documentation link

## Quality Checklist

- [ ] Brief uses customer-facing language, not engineering terminology
- [ ] Known issues and workarounds are documented
- [ ] Escalation paths are specific (named team or channel, not "engineering")
- [ ] Support lead has acknowledged receipt and confirmed readiness
