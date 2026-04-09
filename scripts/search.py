#!/usr/bin/env python3
"""
Skill OS — Skill Search CLI

Search 527 skills by name, description, triggers, agent, or department.

Usage:
    python3 scripts/search.py "write PRD"
    python3 scripts/search.py "GTM strategy" --top 5
    python3 scripts/search.py "threat model" --json
    python3 scripts/search.py --list-departments
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path


def parse_frontmatter(path: Path) -> dict | None:
    """Parse YAML frontmatter from a SKILL.md file. Returns None on failure."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None

    if not text.startswith("---"):
        return None

    end = text.find("\n---", 3)
    if end == -1:
        return None

    fm_text = text[3:end].strip()
    result = {}

    # name
    m = re.search(r"^name:\s*(.+)$", fm_text, re.MULTILINE)
    if m:
        result["name"] = m.group(1).strip()

    # description (may be multiline >-style)
    m = re.search(r"^description:\s*>?\s*\n?(.*?)(?=\n\w|\Z)", fm_text, re.MULTILINE | re.DOTALL)
    if m:
        desc = re.sub(r"\s+", " ", m.group(1)).strip()
        result["description"] = desc

    # simple scalar fields
    for field in ("department", "agent", "version", "complexity"):
        m = re.search(rf"^{field}:\s*(.+)$", fm_text, re.MULTILINE)
        if m:
            result[field] = m.group(1).strip()

    # triggers list
    triggers_match = re.search(r"^triggers:\s*\n((?:\s+-\s+.+\n?)+)", fm_text, re.MULTILINE)
    if triggers_match:
        raw = triggers_match.group(1)
        result["triggers"] = [
            re.sub(r'^["\']|["\']$', "", item.strip().lstrip("- ").strip())
            for item in raw.strip().splitlines()
            if item.strip().startswith("-")
        ]

    result["_path"] = str(path)
    return result


def load_all_skills(repo_root: Path) -> list[dict]:
    skills = []
    agents_dir = repo_root / "agents"
    for skill_file in sorted(agents_dir.rglob("SKILL.md")):
        fm = parse_frontmatter(skill_file)
        if fm and "name" in fm:
            skills.append(fm)
    return skills


def score_match(skill: dict, query: str) -> int:
    """Return a match score (higher = better). 0 means no match."""
    q = query.lower()
    score = 0
    terms = q.split()

    name = skill.get("name", "").lower()
    description = skill.get("description", "").lower()
    triggers = [t.lower() for t in skill.get("triggers", [])]
    agent = skill.get("agent", "").lower()
    department = skill.get("department", "").lower()

    # Exact trigger match — highest signal
    for t in triggers:
        if q == t:
            score += 100
        elif q in t or t in q:
            score += 50

    # Exact name match
    if q == name:
        score += 80
    elif q in name:
        score += 40

    # All query terms in name
    if all(term in name for term in terms):
        score += 30

    # All query terms in description
    if all(term in description for term in terms):
        score += 20

    # Partial term matches in description
    for term in terms:
        if term in description:
            score += 5
        if term in agent:
            score += 8
        if term in department:
            score += 3

    return score


def format_result(skill: dict, rank: int, show_path: bool = False) -> str:
    path = skill.get("_path", "")
    # Make path relative to repo root
    try:
        rel = str(Path(path).relative_to(Path.cwd()))
    except ValueError:
        rel = path

    lines = [
        f"{rank}. [{skill.get('name', '?')}]({rel})",
        f"   {skill.get('agent', '?')} · {skill.get('department', '?')} · {skill.get('complexity', '?')}",
    ]

    desc = skill.get("description", "")
    if desc:
        # Truncate to ~100 chars
        short = desc[:100] + ("…" if len(desc) > 100 else "")
        lines.append(f"   {short}")

    triggers = skill.get("triggers", [])
    if triggers:
        lines.append(f"   triggers: {', '.join(triggers[:4])}")

    if show_path:
        lines.append(f"   path: {rel}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Search Skill OS skills by keyword",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 scripts/search.py "write PRD"
  python3 scripts/search.py "threat model" --top 3
  python3 scripts/search.py "GTM strategy" --json
  python3 scripts/search.py "backend" --department engineering
  python3 scripts/search.py --list-departments
        """,
    )
    parser.add_argument("query", nargs="?", help="Search query")
    parser.add_argument("--top", type=int, default=10, help="Max results (default: 10)")
    parser.add_argument("--json", action="store_true", dest="as_json", help="Output as JSON")
    parser.add_argument("--department", help="Filter by department slug")
    parser.add_argument("--agent", help="Filter by agent slug")
    parser.add_argument("--complexity", choices=["simple", "medium", "complex"], help="Filter by complexity")
    parser.add_argument("--list-departments", action="store_true", help="List all departments and skill counts")
    parser.add_argument("--path", action="store_true", help="Show full file path in results")

    args = parser.parse_args()

    # Find repo root (directory containing agents/)
    repo_root = Path(__file__).parent.parent
    if not (repo_root / "agents").exists():
        # Try cwd
        repo_root = Path.cwd()
    if not (repo_root / "agents").exists():
        print("ERROR: Cannot find agents/ directory. Run from skill-os repo root.", file=sys.stderr)
        sys.exit(1)

    skills = load_all_skills(repo_root)

    if args.list_departments:
        from collections import Counter
        counts = Counter(s.get("department", "unknown") for s in skills)
        print(f"{'Department':<35} {'Skills':>6}")
        print("-" * 43)
        for dept, count in sorted(counts.items()):
            print(f"{dept:<35} {count:>6}")
        print("-" * 43)
        print(f"{'TOTAL':<35} {len(skills):>6}")
        return

    if not args.query:
        parser.print_help()
        return

    # Apply filters
    filtered = skills
    if args.department:
        filtered = [s for s in filtered if args.department.lower() in s.get("department", "").lower()]
    if args.agent:
        filtered = [s for s in filtered if args.agent.lower() in s.get("agent", "").lower()]
    if args.complexity:
        filtered = [s for s in filtered if s.get("complexity", "") == args.complexity]

    # Score and rank
    scored = [(score_match(s, args.query), s) for s in filtered]
    scored = [(score, s) for score, s in scored if score > 0]
    scored.sort(key=lambda x: x[0], reverse=True)
    results = [s for _, s in scored[: args.top]]

    if args.as_json:
        output = []
        for s in results:
            entry = {k: v for k, v in s.items() if not k.startswith("_")}
            try:
                entry["path"] = str(Path(s["_path"]).relative_to(repo_root))
            except (ValueError, KeyError):
                entry["path"] = s.get("_path", "")
            output.append(entry)
        print(json.dumps(output, indent=2))
        return

    if not results:
        print(f"No skills found for: {args.query!r}")
        if args.department or args.agent or args.complexity:
            print("Try removing filters or broadening your query.")
        return

    print(f"\nTop {len(results)} skills for: {args.query!r}\n")
    for i, skill in enumerate(results, 1):
        print(format_result(skill, i, show_path=args.path))
        print()


if __name__ == "__main__":
    main()
