#!/usr/bin/env python3
"""Generate meeting prep brief from account data."""
import json
import sys
from datetime import date


def generate(params: dict) -> str:
    """Build an 11-section meeting brief with cheat sheet."""
    sections = []
    meeting_date = params.get("meeting_date", date.today().isoformat())
    prospect = params.get("prospect_company", "[Company]")
    meeting_type = params.get("meeting_type", "discovery")
    attendees = params.get("attendees", [])
    deal_stage = params.get("deal_stage", "unknown")

    sections.append(f"# Meeting Brief: {prospect}")
    sections.append(f"**Date**: {meeting_date}")
    sections.append(f"**Type**: {meeting_type.title()}")
    sections.append(f"**Deal Stage**: {deal_stage}")
    sections.append(f"**Prepared**: {date.today().isoformat()}")

    # Section 1: Company Snapshot
    company = params.get("company_snapshot", {})
    sections.append("## 1. Company Snapshot")
    sections.append(f"- **Industry**: {company.get('industry', '[Unknown]')}")
    sections.append(f"- **Size**: {company.get('employee_count', '[Unknown]')} employees")
    sections.append(f"- **Revenue**: {company.get('revenue', '[Unknown]')}")
    sections.append(f"- **Funding**: {company.get('funding', '[Unknown]')}")
    sections.append(f"- **HQ**: {company.get('headquarters', '[Unknown]')}")

    # Section 2: Attendee Profiles
    sections.append("## 2. Attendee Profiles")
    for att in attendees:
        name = att.get("name", "[Name]")
        title = att.get("title", "[Title]")
        background = att.get("background", "No background available")
        sections.append(f"### {name} — {title}")
        sections.append(f"- {background}")

    # Section 3: Deal History
    sections.append("## 3. Deal History")
    history = params.get("deal_history", "No prior deal history available.")
    sections.append(history)

    # Section 4: Competitive Landscape
    sections.append("## 4. Competitive Landscape")
    competitors = params.get("competitors", [])
    if competitors:
        for c in competitors:
            sections.append(f"- **{c.get('name', '[Competitor]')}**: {c.get('positioning', 'Unknown')}")
    else:
        sections.append("No competitive intelligence available.")

    # Section 5: Recent News
    sections.append("## 5. Recent News")
    news = params.get("recent_news", [])
    for item in news:
        sections.append(f"- {item}")
    if not news:
        sections.append("No recent news found.")

    # Section 6: Pain Points
    sections.append("## 6. Pain Points")
    pains = params.get("pain_points", [])
    for p in pains:
        sections.append(f"- {p}")
    if not pains:
        sections.append("Pain points not yet identified — prioritize discovery.")

    # Section 7: Value Propositions
    sections.append("## 7. Value Propositions")
    vps = params.get("value_propositions", [])
    for v in vps:
        sections.append(f"- {v}")

    # Section 8: Objection Prep
    sections.append("## 8. Objection Prep")
    objections = params.get("objections", [])
    for o in objections:
        sections.append(f"- **Objection**: {o.get('objection', '[Objection]')}")
        sections.append(f"  **Response**: {o.get('response', '[Response]')}")

    # Section 9: Agenda Suggestion
    sections.append("## 9. Suggested Agenda")
    agenda = params.get("agenda", [])
    for i, item in enumerate(agenda, 1):
        sections.append(f"{i}. {item}")
    if not agenda:
        depth = {"discovery": ["Introductions (5 min)", "Pain discovery (15 min)", "Solution overview (10 min)", "Q&A (10 min)", "Next steps (5 min)"],
                 "demo": ["Recap pain points (5 min)", "Tailored demo (25 min)", "Technical Q&A (15 min)", "Next steps (5 min)"],
                 "negotiation": ["Recap value case (10 min)", "Commercial terms review (20 min)", "Objection resolution (15 min)", "Mutual action plan (5 min)"]}
        for i, item in enumerate(depth.get(meeting_type, depth["discovery"]), 1):
            sections.append(f"{i}. {item}")

    # Section 10: Questions to Ask
    sections.append("## 10. Questions to Ask")
    questions = params.get("questions", [])
    for q in questions:
        sections.append(f"- {q}")

    # Section 11: Success Metrics
    sections.append("## 11. Success Metrics")
    desired_outcome = params.get("desired_outcome", "Book follow-up meeting with next step defined")
    sections.append(f"**Desired outcome**: {desired_outcome}")

    # Cheat Sheet
    sections.append("---")
    sections.append("## Cheat Sheet (1-Page Quick Reference)")
    sections.append("| Item | Detail |")
    sections.append("|------|--------|")
    if attendees:
        names = ", ".join(f"{a.get('name', '?')} ({a.get('title', '?')})" for a in attendees[:4])
        sections.append(f"| Attendees | {names} |")
    if pains:
        top_pains = "; ".join(pains[:3])
        sections.append(f"| Top 3 Pain Points | {top_pains} |")
    sections.append(f"| Key Question | {questions[0] if questions else 'What is your timeline for making a decision?'} |")
    sections.append(f"| Desired Next Step | {desired_outcome} |")

    return "\n\n".join(sections)


if __name__ == "__main__":
    data = json.load(sys.stdin) if not sys.stdin.isatty() else json.loads(sys.argv[1])
    print(generate(data))
