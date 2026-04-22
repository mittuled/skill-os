#!/usr/bin/env python3
"""
Skill OS — Automated Skill Test Harness

Two modes:
  Structural (no API key needed) — validates SKILL.md format and assets/ templates
  Live (requires ANTHROPIC_API_KEY) — calls Claude with a synthetic input and
    checks the output matches the assets/ template shape

Usage:
    python3 scripts/test_skill.py agents/product/product-manager/requirements-extractor/SKILL.md
    python3 scripts/test_skill.py agents/engineering/sr-backend-developer/builder/SKILL.md --live
    python3 scripts/test_skill.py agents/engineering/                         # whole agent
    python3 scripts/test_skill.py                                              # whole repo
    python3 scripts/test_skill.py --live --model claude-haiku-4-5-20251001    # cheaper model
    python3 scripts/test_skill.py --json                                       # machine-readable
"""

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

REQUIRED_SECTIONS = [
    "Agent:",
    "Skill Description",
    "When to Use",
    "Workflow",
    "Anti-Patterns",
    "Output",
    "Related Skills",
]
WORD_LIMITS = {"simple": 500, "medium": 1000, "complex": 1500}
PLACEHOLDER_RE = re.compile(r"\[(?!GATE\])[A-Z][A-Z0-9 _/-]{2,}\]")
DEFAULT_MODEL = "claude-haiku-4-5-20251001"


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class Check:
    name: str
    passed: bool
    detail: str = ""


@dataclass
class SkillResult:
    path: str
    checks: list[Check] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return all(c.passed for c in self.checks)

    @property
    def n_passed(self) -> int:
        return sum(1 for c in self.checks if c.passed)

    @property
    def n_total(self) -> int:
        return len(self.checks)

    def add(self, name: str, passed: bool, detail: str = "") -> None:
        self.checks.append(Check(name, passed, detail))


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

def read_skill(path: Path) -> tuple[dict, str]:
    """Return (frontmatter_dict, body_text). Returns ({}, '') on failure."""
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

    for field_name in ("name", "department", "agent", "version", "complexity"):
        m = re.search(rf"^{field_name}:\s*(.+)$", fm_text, re.MULTILINE)
        if m:
            result[field_name] = m.group(1).strip()

    m = re.search(r"^description:\s*>?\s*\n?(.*?)(?=\n\w|\Z)", fm_text, re.MULTILINE | re.DOTALL)
    if m:
        result["description"] = re.sub(r"\s+", " ", m.group(1)).strip()

    for list_field in ("related-skills", "triggers"):
        # Inline empty list: `field: []`
        if re.search(rf"^{list_field}:\s*\[\]\s*$", fm_text, re.MULTILINE):
            result[list_field] = []
            continue
        lm = re.search(rf"^{list_field}:\s*\n((?:\s+-\s+.+\n?)+)", fm_text, re.MULTILINE)
        if lm:
            result[list_field] = [
                re.sub(r'^["\']|["\']$', "", item.strip().lstrip("- ").strip())
                for item in lm.group(1).strip().splitlines()
                if item.strip().startswith("-")
            ]
        else:
            result[list_field] = []

    return result, body


def extract_section(body: str, section_name: str) -> str:
    """Extract body of a ## section. Returns '' if not found."""
    pattern = rf"## {re.escape(section_name)}\s*\n(.*?)(?=\n## |\Z)"
    m = re.search(pattern, body, re.DOTALL)
    return m.group(1).strip() if m else ""


def template_sections(template_path: Path) -> list[str]:
    """Return list of ## section headers found in a template file."""
    try:
        text = template_path.read_text(encoding="utf-8")
    except OSError:
        return []
    return re.findall(r"^## (.+)$", text, re.MULTILINE)


# ---------------------------------------------------------------------------
# Structural checks
# ---------------------------------------------------------------------------

def check_structure(skill_path: Path) -> SkillResult:
    result = SkillResult(path=str(skill_path))
    fm, body = read_skill(skill_path)

    # 1. Frontmatter present
    result.add("frontmatter-present", bool(fm), "No YAML frontmatter found" if not fm else "")

    # 2. Required frontmatter fields
    required_fields = {"name", "description", "department", "agent", "version", "complexity"}
    missing = required_fields - fm.keys()
    result.add("frontmatter-fields", not missing,
               f"Missing: {', '.join(sorted(missing))}" if missing else "")

    # 3. Description is pushy
    desc = fm.get("description", "").lower()
    pushy = any(kw in desc for kw in ("use when", "suggest when", "also consider when"))
    result.add("description-pushy", pushy, "" if pushy else "Missing 'Use when/Suggest when/Also consider when'")

    # 4. Triggers populated
    triggers = fm.get("triggers", [])
    result.add("triggers-present", len(triggers) >= 3,
               f"Only {len(triggers)} trigger(s); recommend ≥3" if len(triggers) < 3 else "")

    # 5. Required sections
    for section in REQUIRED_SECTIONS:
        present = any(f"## {section}" in line for line in body.splitlines())
        result.add(f"section:{section.rstrip(':').lower().replace(' ', '-')}",
                   present, f"Missing '## {section}'" if not present else "")

    # 6. Workflow has numbered steps
    workflow = extract_section(body, "Workflow")
    has_steps = bool(re.search(r"^\d+\.", workflow, re.MULTILINE))
    result.add("workflow-numbered", has_steps,
               "Workflow steps should be numbered (1. ...)" if not has_steps else "")

    # 7. Word count vs complexity
    complexity = fm.get("complexity", "medium")
    limit = WORD_LIMITS.get(complexity, 1000)
    wc = len(body.split())
    over = wc > limit * 1.2
    under = wc < limit * 0.3
    if over:
        result.add("word-count", False, f"{wc} words exceeds {limit} limit by >20%")
    elif under:
        result.add("word-count", False, f"{wc} words is <30% of {limit} limit — underdeveloped")
    else:
        result.add("word-count", True, f"{wc}/{limit} words")

    # 8. references/ directory exists and has content
    refs_dir = skill_path.parent / "references"
    refs_files = list(refs_dir.glob("*.md")) if refs_dir.exists() else []
    result.add("references-dir", len(refs_files) >= 1,
               "No references/*.md files found" if not refs_files else f"{len(refs_files)} file(s)")

    # 9. assets/ directory exists and has content
    assets_dir = skill_path.parent / "assets"
    assets_files = list(assets_dir.glob("*.md")) if assets_dir.exists() else []
    result.add("assets-dir", len(assets_files) >= 1,
               "No assets/*.md files found" if not assets_files else f"{len(assets_files)} file(s)")

    # 10. Asset templates have valid section structure (no empty ##)
    for af in assets_files:
        sections = template_sections(af)
        result.add(f"template-structure:{af.name}", len(sections) >= 2,
                   f"Template has <2 sections" if len(sections) < 2 else f"{len(sections)} sections")

    # 11. Related skills bidirectional (basic: at least 1 related skill)
    related = fm.get("related-skills", [])
    result.add("related-skills-present", len(related) >= 1,
               "No related-skills listed" if not related else f"{len(related)} related skill(s)")

    return result


# ---------------------------------------------------------------------------
# Live checks (requires anthropic SDK + API key)
# ---------------------------------------------------------------------------

def build_system_prompt(fm: dict, body: str) -> str:
    return f"""You are an AI agent executing the following skill from the Skill OS framework.

---
{body}
---

Execute the skill workflow step by step against the user's input.
Produce output that matches the structure described in the Output section.
Be concrete and specific — fill in real details, not placeholder text like [INSERT X].
"""


def derive_synthetic_input(fm: dict, body: str) -> str:
    """Create a realistic test input from the skill's 'When to Use' scenarios."""
    skill_name = fm.get("name", "this skill")
    dept = fm.get("department", "")
    when_to_use = extract_section(body, "When to Use")

    # Pick the first bullet point as the scenario
    scenarios = [
        line.lstrip("- •*").strip()
        for line in when_to_use.splitlines()
        if line.strip().startswith("-") or line.strip().startswith("•")
    ]
    scenario = scenarios[0] if scenarios else when_to_use[:200]

    return (
        f"Please execute the '{skill_name}' skill for the following scenario:\n\n"
        f"Context: {scenario}\n\n"
        f"Company: Acme Corp (B2B SaaS, 50-person startup, Series A)\n"
        f"Request: Produce a complete, ready-to-use output as defined by this skill."
    )


def check_output_against_template(output: str, template_path: Path) -> list[Check]:
    """Validate LLM output against the expected template structure."""
    checks: list[Check] = []
    expected_sections = template_sections(template_path)

    if not expected_sections:
        return checks

    for section in expected_sections:
        present = section.lower() in output.lower()
        checks.append(Check(
            name=f"output-section:{section.lower().replace(' ', '-')}",
            passed=present,
            detail="" if present else f"Output missing '## {section}'"
        ))

    # Placeholders should be filled in
    unfilled = PLACEHOLDER_RE.findall(output)
    checks.append(Check(
        name="output-placeholders-filled",
        passed=len(unfilled) == 0,
        detail=f"Unfilled placeholders: {unfilled[:5]}" if unfilled else ""
    ))

    # Output should be substantive
    wc = len(output.split())
    checks.append(Check(
        name="output-length",
        passed=wc >= 100,
        detail=f"Output only {wc} words — likely too short" if wc < 100 else f"{wc} words"
    ))

    return checks


def run_live_check(skill_path: Path, model: str) -> SkillResult:
    result = SkillResult(path=str(skill_path))
    fm, body = read_skill(skill_path)

    if not fm:
        result.add("skill-readable", False, "Cannot parse SKILL.md")
        return result

    try:
        import anthropic
    except ImportError:
        result.add("anthropic-sdk", False, "pip install anthropic")
        return result

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        result.add("api-key", False, "ANTHROPIC_API_KEY not set")
        return result

    result.add("anthropic-sdk", True)
    result.add("api-key", True)

    system = build_system_prompt(fm, body)
    user_input = derive_synthetic_input(fm, body)

    print(f"  → Calling {model} with synthetic input...")
    try:
        client = anthropic.Anthropic(api_key=api_key)
        message = client.messages.create(
            model=model,
            max_tokens=2048,
            system=system,
            messages=[{"role": "user", "content": user_input}],
        )
        output = message.content[0].text
        result.add("api-call", True, f"{message.usage.output_tokens} output tokens")
    except Exception as e:
        result.add("api-call", False, str(e))
        return result

    # Validate output against each assets/ template
    assets_dir = skill_path.parent / "assets"
    templates = list(assets_dir.glob("*.md")) if assets_dir.exists() else []

    if not templates:
        result.add("output-template-exists", False, "No assets/ template to validate against")
    else:
        result.add("output-template-exists", True, f"{len(templates)} template(s)")
        # Use the first template (most skills have one primary output)
        template = templates[0]
        for check in check_output_against_template(output, template):
            result.checks.append(check)

    return result


# ---------------------------------------------------------------------------
# Formatting
# ---------------------------------------------------------------------------

PASS = "\033[32m✓\033[0m"
FAIL = "\033[31m✗\033[0m"
BOLD = "\033[1m"
RESET = "\033[0m"


def format_result(result: SkillResult, verbose: bool = False) -> str:
    status = f"{PASS}" if result.passed else f"{FAIL}"
    try:
        rel = str(Path(result.path).relative_to(Path.cwd()))
    except ValueError:
        rel = result.path
    lines = [f"{status} {BOLD}{rel}{RESET}  ({result.n_passed}/{result.n_total})"]
    for check in result.checks:
        if not check.passed or verbose:
            icon = PASS if check.passed else FAIL
            detail = f"  — {check.detail}" if check.detail else ""
            lines.append(f"     {icon} {check.name}{detail}")
    return "\n".join(lines)


def print_summary(results: list[SkillResult]) -> None:
    passed = sum(1 for r in results if r.passed)
    total = len(results)
    pct = round(passed / total * 100) if total else 0
    print(f"\n{'─' * 60}")
    print(f"  {passed}/{total} skills passed ({pct}%)")
    if passed < total:
        failed = [r for r in results if not r.passed]
        print(f"\n  Failed skills:")
        for r in failed[:20]:
            try:
                rel = str(Path(r.path).relative_to(Path.cwd()))
            except ValueError:
                rel = r.path
            print(f"    {FAIL} {rel}  ({r.n_passed}/{r.n_total})")
        if len(failed) > 20:
            print(f"    ... and {len(failed) - 20} more")
    print()


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------

def find_skill_files(target: Path) -> list[Path]:
    if target.name == "SKILL.md" and target.is_file():
        return [target]
    if target.is_dir():
        return sorted(target.rglob("SKILL.md"))
    return []


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Test Skill OS SKILL.md files for quality and correctness",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 scripts/test_skill.py                          # Full repo structural check
  python3 scripts/test_skill.py agents/engineering/      # One agent
  python3 scripts/test_skill.py agents/product/product-manager/requirements-extractor/SKILL.md
  python3 scripts/test_skill.py --live                   # Live LLM validation (needs API key)
  python3 scripts/test_skill.py --live --model claude-haiku-4-5-20251001
  python3 scripts/test_skill.py --json > results.json
        """,
    )
    parser.add_argument("target", nargs="?", default="agents",
                        help="SKILL.md file, agent dir, or agents/ root (default: agents/)")
    parser.add_argument("--live", action="store_true",
                        help="Run live LLM validation (requires ANTHROPIC_API_KEY)")
    parser.add_argument("--model", default=DEFAULT_MODEL,
                        help=f"Model for live checks (default: {DEFAULT_MODEL})")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Show passing checks too")
    parser.add_argument("--json", action="store_true", dest="as_json",
                        help="Output results as JSON")
    parser.add_argument("--fail-fast", action="store_true",
                        help="Stop after first failure")

    args = parser.parse_args()

    repo_root = Path(__file__).parent.parent
    target = Path(args.target)
    if not target.is_absolute():
        # Try relative to cwd first, then repo root
        if (Path.cwd() / target).exists():
            target = Path.cwd() / target
        elif (repo_root / target).exists():
            target = repo_root / target

    skill_files = find_skill_files(target)
    if not skill_files:
        print(f"ERROR: No SKILL.md files found at '{args.target}'", file=sys.stderr)
        sys.exit(1)

    results: list[SkillResult] = []
    any_failed = False

    for skill_path in skill_files:
        # Always run structural checks
        struct = check_structure(skill_path)

        if args.live:
            live = run_live_check(skill_path, args.model)
            # Merge live checks into structural result
            struct.checks.extend(live.checks)

        results.append(struct)

        if not args.as_json:
            print(format_result(struct, verbose=args.verbose))

        if not struct.passed:
            any_failed = True
            if args.fail_fast:
                break

    if args.as_json:
        output = []
        for r in results:
            output.append({
                "path": r.path,
                "passed": r.passed,
                "n_passed": r.n_passed,
                "n_total": r.n_total,
                "checks": [
                    {"name": c.name, "passed": c.passed, "detail": c.detail}
                    for c in r.checks
                ],
            })
        print(json.dumps(output, indent=2))
    elif len(results) > 1:
        print_summary(results)

    sys.exit(1 if any_failed else 0)


if __name__ == "__main__":
    main()
