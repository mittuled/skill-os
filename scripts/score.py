#!/usr/bin/env python3
"""
Skill OS — Skill Quality Scorer

Rates every SKILL.md on 7 dimensions and produces a quality leaderboard.

Usage:
    python3 scripts/score.py                          # Full repo leaderboard
    python3 scripts/score.py --bottom 20              # Worst skills (contributor targets)
    python3 scripts/score.py --department engineering # Filter by department
    python3 scripts/score.py --agent sr-backend-developer
    python3 scripts/score.py --min-score 60           # Only skills scoring ≥60%
    python3 scripts/score.py --json                   # Machine-readable output
    python3 scripts/score.py --summary                # Department summary table
"""

import argparse
import json
import re
import sys
from pathlib import Path


# Scoring dimensions and their max points
DIMENSIONS = {
    "triggers":    10,  # Trigger phrase coverage
    "description": 10,  # Description pushiness
    "references":  10,  # references/ directory depth
    "assets":      10,  # assets/ directory depth
    "related":     10,  # Related-skills count
    "depth":       10,  # Word count vs complexity limit
    "sections":    10,  # Required section completeness
}
MAX_SCORE = sum(DIMENSIONS.values())  # 70

WORD_LIMITS = {"simple": 500, "medium": 1000, "complex": 1500}
PUSHY_KEYWORDS = ("use when", "suggest when", "also consider when")
REQUIRED_SECTIONS = [
    "## Agent:",
    "## Skill Description",
    "## When to Use",
    "## Workflow",
    "## Anti-Patterns",
    "## Output",
    "## Related Skills",
]


def parse_frontmatter(path: Path) -> tuple[dict, str]:
    """Parse YAML frontmatter and return (fm_dict, body). Returns ({}, '') on failure."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return {}, ""

    if not text.startswith("---"):
        return {}, text

    end = text.find("\n---", 3)
    if end == -1:
        return {}, text

    fm_text = text[3:end].strip()
    body = text[end + 4:].strip()
    result: dict = {}

    m = re.search(r"^name:\s*(.+)$", fm_text, re.MULTILINE)
    if m:
        result["name"] = m.group(1).strip()

    m = re.search(r"^description:\s*>?\s*\n?(.*?)(?=\n\w|\Z)", fm_text, re.MULTILINE | re.DOTALL)
    if m:
        result["description"] = re.sub(r"\s+", " ", m.group(1)).strip()

    for field in ("department", "agent", "version", "complexity"):
        m = re.search(rf"^{field}:\s*(.+)$", fm_text, re.MULTILINE)
        if m:
            result[field] = m.group(1).strip()

    # related-skills list
    rs_match = re.search(r"^related-skills:\s*\n((?:\s+-\s+.+\n?)+)", fm_text, re.MULTILINE)
    if rs_match:
        raw = rs_match.group(1)
        result["related-skills"] = [
            item.strip().lstrip("- ").strip()
            for item in raw.strip().splitlines()
            if item.strip().startswith("-")
        ]
    else:
        result["related-skills"] = []

    # triggers list
    tr_match = re.search(r"^triggers:\s*\n((?:\s+-\s+.+\n?)+)", fm_text, re.MULTILINE)
    if tr_match:
        raw = tr_match.group(1)
        result["triggers"] = [
            re.sub(r'^["\']|["\']$', "", item.strip().lstrip("- ").strip())
            for item in raw.strip().splitlines()
            if item.strip().startswith("-")
        ]
    else:
        result["triggers"] = []

    return result, body


def score_skill(path: Path) -> dict | None:
    """Score a single SKILL.md. Returns None if not a valid skill file."""
    fm, body = parse_frontmatter(path)
    if not fm.get("name"):
        return None

    scores: dict[str, int] = {}

    # 1. Trigger coverage (0-10)
    n_triggers = len(fm.get("triggers", []))
    if n_triggers == 0:
        scores["triggers"] = 0
    elif n_triggers <= 2:
        scores["triggers"] = 5
    elif n_triggers <= 4:
        scores["triggers"] = 8
    else:
        scores["triggers"] = 10

    # 2. Description pushiness (0-10)
    desc = fm.get("description", "").lower()
    scores["description"] = 10 if any(kw in desc for kw in PUSHY_KEYWORDS) else 0

    # 3. References/ depth (0-10)
    refs_dir = path.parent / "references"
    refs_files = list(refs_dir.glob("*.md")) if refs_dir.exists() else []
    if len(refs_files) == 0:
        scores["references"] = 0
    elif len(refs_files) == 1:
        scores["references"] = 7
    else:
        scores["references"] = 10

    # 4. Assets/ depth (0-10)
    assets_dir = path.parent / "assets"
    assets_files = list(assets_dir.glob("*.md")) if assets_dir.exists() else []
    if len(assets_files) == 0:
        scores["assets"] = 0
    elif len(assets_files) == 1:
        scores["assets"] = 7
    else:
        scores["assets"] = 10

    # 5. Related-skills count (0-10)
    n_related = len(fm.get("related-skills", []))
    if n_related == 0:
        scores["related"] = 0
    elif n_related <= 2:
        scores["related"] = 5
    elif n_related <= 4:
        scores["related"] = 8
    else:
        scores["related"] = 10

    # 6. Body depth vs complexity limit (0-10)
    complexity = fm.get("complexity", "medium")
    limit = WORD_LIMITS.get(complexity, 1000)
    word_count = len(body.split()) if body else 0
    ratio = word_count / limit if limit else 0
    if ratio >= 0.85:
        scores["depth"] = 10
    elif ratio >= 0.55:
        scores["depth"] = 7
    elif ratio >= 0.30:
        scores["depth"] = 4
    elif ratio > 0:
        scores["depth"] = 2
    else:
        scores["depth"] = 0

    # 7. Section completeness (0-10)
    present = sum(1 for s in REQUIRED_SECTIONS if s in body)
    scores["sections"] = round(present / len(REQUIRED_SECTIONS) * 10)

    total = sum(scores.values())
    pct = round(total / MAX_SCORE * 100)

    return {
        "name": fm.get("name", "?"),
        "agent": fm.get("agent", "?"),
        "department": fm.get("department", "?"),
        "complexity": fm.get("complexity", "?"),
        "scores": scores,
        "total": total,
        "pct": pct,
        "_path": str(path),
    }


def grade(pct: int) -> str:
    if pct >= 90: return "A"
    if pct >= 75: return "B"
    if pct >= 55: return "C"
    if pct >= 35: return "D"
    return "F"


def load_all_skills(repo_root: Path) -> list[dict]:
    results = []
    for skill_file in sorted((repo_root / "agents").rglob("SKILL.md")):
        s = score_skill(skill_file)
        if s:
            results.append(s)
    return results


def format_bar(pct: int, width: int = 20) -> str:
    filled = round(pct / 100 * width)
    return "█" * filled + "░" * (width - filled)


def format_row(rank: int, skill: dict, show_path: bool = False) -> str:
    g = grade(skill["pct"])
    bar = format_bar(skill["pct"], 15)
    path = skill["_path"]
    try:
        rel = str(Path(path).relative_to(Path.cwd()))
    except ValueError:
        rel = path

    name_link = f"[{skill['name']}]({rel})" if show_path else skill["name"]
    line = (
        f"{rank:>4}. {g} {bar} {skill['pct']:>3}%  "
        f"{name_link:<45}  "
        f"{skill['agent']:<35}  "
        f"{skill['department']}"
    )
    return line


def print_dimension_breakdown(skill: dict) -> None:
    scores = skill["scores"]
    print(f"\n  Breakdown for: {skill['name']}")
    for dim, max_pts in DIMENSIONS.items():
        pts = scores.get(dim, 0)
        bar = format_bar(round(pts / max_pts * 100), 10)
        print(f"    {dim:<12} {bar} {pts:>2}/{max_pts}")


def summary_by_department(skills: list[dict]) -> None:
    from collections import defaultdict
    dept_data: dict[str, list[int]] = defaultdict(list)
    for s in skills:
        dept_data[s["department"]].append(s["pct"])

    print(f"\n{'Department':<35} {'Skills':>6}  {'Avg%':>5}  {'A':>3}  {'B':>3}  {'C':>3}  {'D/F':>4}")
    print("-" * 70)
    for dept in sorted(dept_data):
        pcts = dept_data[dept]
        avg = round(sum(pcts) / len(pcts))
        grades = [grade(p) for p in pcts]
        a = grades.count("A")
        b = grades.count("B")
        c = grades.count("C")
        df = grades.count("D") + grades.count("F")
        bar = format_bar(avg, 10)
        print(f"{dept:<35} {len(pcts):>6}  {bar} {avg:>3}%  {a:>3}  {b:>3}  {c:>3}  {df:>4}")
    print("-" * 70)
    overall = round(sum(s["pct"] for s in skills) / len(skills)) if skills else 0
    g_counts = [grade(s["pct"]) for s in skills]
    print(
        f"{'TOTAL':<35} {len(skills):>6}  {format_bar(overall, 10)} {overall:>3}%"
        f"  {g_counts.count('A'):>3}  {g_counts.count('B'):>3}"
        f"  {g_counts.count('C'):>3}  {g_counts.count('D') + g_counts.count('F'):>4}"
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Score Skill OS skills on quality dimensions",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 scripts/score.py                          # Top 20 leaderboard
  python3 scripts/score.py --top 50                 # Top 50
  python3 scripts/score.py --bottom 20              # Worst 20 (contributor targets)
  python3 scripts/score.py --summary                # Department averages
  python3 scripts/score.py --department engineering # Filter by department
  python3 scripts/score.py --min-score 80           # Only high-quality skills
  python3 scripts/score.py --json > quality.json    # Export for tooling
        """,
    )
    parser.add_argument("--top", type=int, default=20, help="Show top N skills (default: 20)")
    parser.add_argument("--bottom", type=int, help="Show bottom N skills instead of top")
    parser.add_argument("--all", action="store_true", help="Show all skills")
    parser.add_argument("--summary", action="store_true", help="Show department summary table")
    parser.add_argument("--department", help="Filter by department slug")
    parser.add_argument("--agent", help="Filter by agent slug")
    parser.add_argument("--complexity", choices=["simple", "medium", "complex"], help="Filter by complexity")
    parser.add_argument("--min-score", type=int, default=0, help="Only show skills scoring >= N%%")
    parser.add_argument("--max-score", type=int, default=100, help="Only show skills scoring <= N%%")
    parser.add_argument("--json", action="store_true", dest="as_json", help="Output as JSON")
    parser.add_argument("--path", action="store_true", help="Show file paths in results")
    parser.add_argument("--breakdown", action="store_true", help="Show per-dimension breakdown")

    args = parser.parse_args()

    repo_root = Path(__file__).parent.parent
    if not (repo_root / "agents").exists():
        repo_root = Path.cwd()
    if not (repo_root / "agents").exists():
        print("ERROR: Cannot find agents/ directory. Run from skill-os repo root.", file=sys.stderr)
        sys.exit(1)

    skills = load_all_skills(repo_root)

    # Apply filters
    filtered = skills
    if args.department:
        filtered = [s for s in filtered if args.department.lower() in s["department"].lower()]
    if args.agent:
        filtered = [s for s in filtered if args.agent.lower() in s["agent"].lower()]
    if args.complexity:
        filtered = [s for s in filtered if s["complexity"] == args.complexity]
    filtered = [s for s in filtered if args.min_score <= s["pct"] <= args.max_score]

    # Sort by score descending
    filtered.sort(key=lambda x: x["total"], reverse=True)

    if args.summary:
        summary_by_department(filtered)
        return

    if args.as_json:
        output = []
        for s in filtered:
            entry = {k: v for k, v in s.items() if not k.startswith("_")}
            try:
                entry["path"] = str(Path(s["_path"]).relative_to(repo_root))
            except (ValueError, KeyError):
                entry["path"] = s.get("_path", "")
            output.append(entry)
        print(json.dumps(output, indent=2))
        return

    if not filtered:
        print("No skills match the given filters.")
        return

    # Determine slice
    if args.bottom:
        display = list(reversed(filtered))[:args.bottom]
        total_shown = args.bottom
        label = f"Bottom {min(args.bottom, len(filtered))} skills"
    elif args.all:
        display = filtered
        total_shown = len(filtered)
        label = f"All {len(filtered)} skills"
    else:
        display = filtered[: args.top]
        total_shown = args.top
        label = f"Top {min(args.top, len(filtered))} skills"

    avg = round(sum(s["pct"] for s in filtered) / len(filtered)) if filtered else 0
    g_counts = [grade(s["pct"]) for s in filtered]

    print(f"\n{label} by quality score  (total: {len(filtered)} matching)\n")
    print(f"{'Rank':<6} {'Gr':<3} {'Score':<20} {'%':>4}  {'Skill':<45}  {'Agent':<35}  Dept")
    print("-" * 130)

    for i, skill in enumerate(display, 1):
        # When --bottom, display rank from end of full list
        if args.bottom:
            rank = len(filtered) - args.bottom + i
        else:
            rank = i
        print(format_row(rank, skill, show_path=args.path))
        if args.breakdown:
            print_dimension_breakdown(skill)

    print("-" * 130)
    print(
        f"\nRepo avg: {format_bar(avg, 15)} {avg}%   "
        f"A:{g_counts.count('A')}  B:{g_counts.count('B')}  "
        f"C:{g_counts.count('C')}  D:{g_counts.count('D')}  F:{g_counts.count('F')}"
    )

    # Surface quick wins if showing top
    if not args.bottom and not args.all:
        no_refs = sum(1 for s in filtered if s["scores"]["references"] == 0)
        no_assets = sum(1 for s in filtered if s["scores"]["assets"] == 0)
        low_triggers = sum(1 for s in filtered if s["scores"]["triggers"] < 8)
        print(f"\nContributor targets across {len(filtered)} skills:")
        print(f"  {no_refs:>4} skills missing references/  (10 pts each)")
        print(f"  {no_assets:>4} skills missing assets/     (10 pts each)")
        print(f"  {low_triggers:>4} skills with <5 triggers      (up to 10 pts each)")


if __name__ == "__main__":
    main()
