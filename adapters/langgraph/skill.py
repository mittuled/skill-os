"""
skill.py — Skill dataclass parsed from a SKILL.md file.

Parses YAML frontmatter and body using stdlib regex only,
consistent with scripts/search.py and scripts/score.py patterns.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Skill:
    """Represents a parsed SKILL.md file."""

    name: str
    description: str
    department: str
    agent: str
    version: str
    complexity: str  # simple | medium | complex
    related_skills: list[str]
    triggers: list[str]
    body: str  # full markdown body after frontmatter
    path: Path | None = field(default=None, repr=False)

    @property
    def system_prompt(self) -> str:
        """Return the full skill content as a system prompt string."""
        return self.body.strip()


def _parse_frontmatter_text(fm_text: str) -> dict:
    """Parse a YAML frontmatter block (text between the --- delimiters)."""
    result: dict = {}

    # name
    m = re.search(r"^name:\s*(.+)$", fm_text, re.MULTILINE)
    if m:
        result["name"] = m.group(1).strip()

    # description (may be multiline >-style or >)
    m = re.search(
        r"^description:\s*>-?\s*\n((?:[ \t]+.+\n?)+)",
        fm_text,
        re.MULTILINE,
    )
    if m:
        desc = re.sub(r"\s+", " ", m.group(1)).strip()
        result["description"] = desc
    else:
        m = re.search(r"^description:\s*(.+)$", fm_text, re.MULTILINE)
        if m:
            result["description"] = m.group(1).strip()

    # simple scalar fields
    for f in ("department", "agent", "version", "complexity"):
        m = re.search(rf"^{f}:\s*(.+)$", fm_text, re.MULTILINE)
        if m:
            result[f] = m.group(1).strip()

    # related-skills list
    related_match = re.search(
        r"^related-skills:\s*\n((?:\s+-\s+.+\n?)+)",
        fm_text,
        re.MULTILINE,
    )
    if related_match:
        raw = related_match.group(1)
        result["related_skills"] = [
            re.sub(r'^["\']|["\']$', "", item.strip().lstrip("- ").strip())
            for item in raw.strip().splitlines()
            if item.strip().startswith("-")
        ]
    else:
        # inline empty list: related-skills: []
        m = re.search(r"^related-skills:\s*\[\s*\]", fm_text, re.MULTILINE)
        if m:
            result["related_skills"] = []

    # triggers list
    triggers_match = re.search(
        r"^triggers:\s*\n((?:\s+-\s+.+\n?)+)",
        fm_text,
        re.MULTILINE,
    )
    if triggers_match:
        raw = triggers_match.group(1)
        result["triggers"] = [
            re.sub(r'^["\']|["\']$', "", item.strip().lstrip("- ").strip())
            for item in raw.strip().splitlines()
            if item.strip().startswith("-")
        ]
    else:
        result["triggers"] = []

    return result


def load_skill(path: str | Path) -> Skill:
    """
    Load and parse a SKILL.md file into a Skill dataclass.

    Args:
        path: Absolute or relative path to a SKILL.md file.

    Returns:
        Parsed Skill instance.

    Raises:
        FileNotFoundError: If the path does not exist.
        ValueError: If the file lacks valid frontmatter or required fields.
    """
    skill_path = Path(path).resolve()

    if not skill_path.exists():
        raise FileNotFoundError(f"SKILL.md not found: {skill_path}")

    text = skill_path.read_text(encoding="utf-8")

    if not text.startswith("---"):
        raise ValueError(f"No YAML frontmatter found in {skill_path}")

    end = text.find("\n---", 3)
    if end == -1:
        raise ValueError(f"Unclosed YAML frontmatter in {skill_path}")

    fm_text = text[3:end].strip()
    # body is everything after the closing ---
    body = text[end + 4:].strip()

    parsed = _parse_frontmatter_text(fm_text)

    for required in ("name", "department", "agent"):
        if required not in parsed:
            raise ValueError(
                f"Missing required frontmatter field '{required}' in {skill_path}"
            )

    return Skill(
        name=parsed.get("name", ""),
        description=parsed.get("description", ""),
        department=parsed.get("department", ""),
        agent=parsed.get("agent", ""),
        version=parsed.get("version", "1.0.0"),
        complexity=parsed.get("complexity", "medium"),
        related_skills=parsed.get("related_skills", []),
        triggers=parsed.get("triggers", []),
        body=body,
        path=skill_path,
    )
