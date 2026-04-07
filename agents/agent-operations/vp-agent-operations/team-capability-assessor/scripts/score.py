#!/usr/bin/env python3
"""
score.py — Scores a capability assessment report against the quality rubric

Usage:
    python3 score.py <document.md>
    python3 score.py <document.md> --json
    python3 score.py <document.md> -o scores.json

Dependencies: Python 3.10+ standard library only.
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

RUBRIC = {
    "Requirements Decomposition": {"weight": 0.25, "description": "Granularity of initiative-to-capability mapping"},
    "Coverage Accuracy": {"weight": 0.25, "description": "Correctness of capability-to-agent matching with skill verification"},
    "Gap Severity Assessment": {"weight": 0.25, "description": "Appropriateness of blocker/degrader/nice-to-have classification"},
    "Remediation Quality": {"weight": 0.25, "description": "Specificity and feasibility of recommendations with effort estimates"},
}

GRADE_BANDS = [
    (9.0, 10.0, "A+", "Exceptional"),
    (8.0, 8.9, "A", "Strong"),
    (7.0, 7.9, "B", "Good"),
    (5.0, 6.9, "C", "Adequate"),
    (3.0, 4.9, "D", "Weak"),
    (0.0, 2.9, "F", "Failing"),
]


def load_document(path: Path) -> str:
    """Load the document to be scored."""
    if not path.exists():
        print(f"Error: File not found: {path}", file=sys.stderr)
        sys.exit(1)
    return path.read_text(encoding="utf-8")


def count_sections(text: str) -> int:
    """Count markdown H2 sections."""
    return len(re.findall(r"^## ", text, re.MULTILINE))


def has_table(text: str) -> bool:
    """Check if document contains markdown tables."""
    return bool(re.search(r"\|.*\|.*\|", text))


def has_metadata(text: str) -> bool:
    """Check for metadata section with required fields."""
    required = ["Date", "Author", "Version", "Status", "Skill"]
    return all(field in text for field in required)


def score_criterion(name: str, text: str) -> tuple[int, str]:
    """Score a single criterion based on document content analysis.
    
    Returns (score, evidence) tuple.
    """
    sections = count_sections(text)
    word_count = len(text.split())
    has_tables = has_table(text)
    has_meta = has_metadata(text)
    has_exec_summary = "Executive Summary" in text or "executive summary" in text.lower()
    has_recommendations = "Recommend" in text or "Action" in text
    has_quantitative = bool(re.search(r"\d+%|\d+\.\d+|\d+/\d+", text))
    
    # Base score from document quality signals
    score = 5  # Start at adequate
    evidence_parts = []
    
    if has_meta:
        score += 1
        evidence_parts.append("metadata present")
    if has_exec_summary:
        score += 1
        evidence_parts.append("executive summary found")
    if has_tables:
        score += 1
        evidence_parts.append("structured tables present")
    if has_quantitative:
        score += 1
        evidence_parts.append("quantitative data included")
    if has_recommendations:
        score += 1
        evidence_parts.append("recommendations/actions included")
    if sections >= 5:
        score += 1
        evidence_parts.append(f"{sections} sections (comprehensive)")
    if word_count >= 500:
        evidence_parts.append(f"{word_count} words (sufficient depth)")
    else:
        score -= 1
        evidence_parts.append(f"{word_count} words (may lack depth)")
    
    score = max(0, min(10, score))
    evidence = "; ".join(evidence_parts) if evidence_parts else "basic analysis"
    return score, evidence


def compute_grade(composite: float) -> tuple[str, str]:
    """Map composite score to grade band."""
    for low, high, grade, label in GRADE_BANDS:
        if low <= composite <= high:
            return grade, label
    return "F", "Failing"


def score_document(text: str) -> dict:
    """Score the document against all rubric criteria."""
    results = {}
    composite = 0.0
    
    for criterion, meta in RUBRIC.items():
        score, evidence = score_criterion(criterion, text)
        weighted = score * meta["weight"]
        composite += weighted
        results[criterion] = {
            "score": score,
            "weight": meta["weight"],
            "weighted_score": round(weighted, 2),
            "evidence": evidence,
        }
    
    grade, label = compute_grade(composite)
    
    return {
        "skill": "team-capability-assessor",
        "scored_at": datetime.now(timezone.utc).isoformat(),
        "criteria": results,
        "composite_score": round(composite, 2),
        "grade": grade,
        "grade_label": label,
    }


def format_text_report(report: dict) -> str:
    """Format the score report as readable text."""
    lines = [
        f"Score Report: {report['skill']}",
        f"Scored at: {report['scored_at']}",
        f"",
        f"Criteria Scores:",
    ]
    for name, data in report["criteria"].items():
        lines.append(f"  {name}: {data['score']}/10 (weight: {data['weight']:.0%}, weighted: {data['weighted_score']:.2f})")
        lines.append(f"    Evidence: {data['evidence']}")
    lines.append(f"")
    lines.append(f"Composite Score: {report['composite_score']:.2f}/10.00")
    lines.append(f"Grade: {report['grade']} ({report['grade_label']})")
    return "\n".join(lines)


def main() -> None:
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print("Usage: python3 score.py <document.md> [--json] [-o output.json]")
        sys.exit(0)
    
    doc_path = Path(args[0])
    text = load_document(doc_path)
    report = score_document(text)
    
    if "--json" in args or "-o" in args:
        output = json.dumps(report, indent=2)
        if "-o" in args:
            idx = args.index("-o") + 1
            if idx < len(args):
                Path(args[idx]).write_text(output + "\n", encoding="utf-8")
                print(f"Report written to {args[idx]}")
            else:
                print("Error: -o requires a filename", file=sys.stderr)
                sys.exit(1)
        else:
            print(output)
    else:
        print(format_text_report(report))


if __name__ == "__main__":
    main()
