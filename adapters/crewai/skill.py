"""Skill dataclass and parser for the skill-os CrewAI adapter.

Parses SKILL.md files using stdlib regex only — no PyYAML dependency.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional


# ---------------------------------------------------------------------------
# Frontmatter parser (mirrors validate.py logic)
# ---------------------------------------------------------------------------

def _parse_frontmatter(text: str) -> tuple[dict, str]:
    """Extract YAML frontmatter from markdown text.

    Returns (frontmatter_dict, body_text).
    """
    if not text.startswith("---"):
        return {}, text
    end = text.find("---", 3)
    if end == -1:
        return {}, text
    fm_text = text[3:end].strip()
    body = text[end + 3:].strip()

    fm: dict = {}
    current_key: Optional[str] = None
    current_list: Optional[list] = None

    for line in fm_text.split("\n"):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        # List item
        if stripped.startswith("- ") and current_key:
            if current_list is None:
                current_list = []
                fm[current_key] = current_list
            current_list.append(stripped[2:].strip())
            continue

        # Multi-line string continuation (indented)
        if line.startswith("  ") and current_key and current_key in fm and isinstance(fm[current_key], str):
            fm[current_key] += " " + stripped
            continue

        # Key: value
        if ":" in stripped:
            key, _, val = stripped.partition(":")
            key = key.strip()
            val = val.strip()
            current_key = key
            current_list = None
            if val in ("", "|", ">"):
                fm[key] = ""
            else:
                fm[key] = val

    return fm, body


# ---------------------------------------------------------------------------
# Section extractor
# ---------------------------------------------------------------------------

_SECTION_RE = re.compile(r"^##\s+(.+)$", re.MULTILINE)


def _extract_sections(body: str) -> dict[str, str]:
    """Split markdown body into a dict of {heading: content}."""
    matches = list(_SECTION_RE.finditer(body))
    sections: dict[str, str] = {}
    for i, match in enumerate(matches):
        heading = match.group(1).strip()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        content = body[start:end].strip()
        sections[heading] = content
    return sections


# ---------------------------------------------------------------------------
# Skill dataclass
# ---------------------------------------------------------------------------

@dataclass
class Skill:
    """Parsed representation of a skill-os SKILL.md file."""

    # Frontmatter fields
    name: str
    description: str
    department: str
    agent: str
    version: str
    complexity: str
    related_skills: List[str]
    triggers: List[str]

    # Full markdown body (all 9 sections)
    body: str

    # Parsed sections
    sections: dict = field(default_factory=dict)

    # Source path (optional)
    source_path: Optional[Path] = None

    # ------------------------------------------------------------------
    # Convenience section accessors
    # ------------------------------------------------------------------

    @property
    def skill_description(self) -> str:
        return self.sections.get("Skill Description", "")

    @property
    def when_to_use(self) -> str:
        return self.sections.get("When to Use", "")

    @property
    def workflow(self) -> str:
        return self.sections.get("Workflow", "")

    @property
    def anti_patterns(self) -> str:
        return self.sections.get("Anti-Patterns", "")

    @property
    def output(self) -> str:
        return self.sections.get("Output", "")

    @property
    def related_skills_body(self) -> str:
        return self.sections.get("Related Skills", "")

    # ------------------------------------------------------------------
    # Factory
    # ------------------------------------------------------------------

    @classmethod
    def from_file(cls, path: str | Path) -> "Skill":
        """Parse a SKILL.md file and return a Skill instance."""
        path = Path(path)
        if not path.exists():
            raise FileNotFoundError(f"SKILL.md not found: {path}")

        text = path.read_text(encoding="utf-8")
        fm, body = _parse_frontmatter(text)

        sections = _extract_sections(body)

        return cls(
            name=fm.get("name", ""),
            description=fm.get("description", "").strip(),
            department=fm.get("department", ""),
            agent=fm.get("agent", ""),
            version=fm.get("version", "1.0.0"),
            complexity=fm.get("complexity", "medium"),
            related_skills=fm.get("related-skills", []) if isinstance(fm.get("related-skills"), list) else [],
            triggers=fm.get("triggers", []) if isinstance(fm.get("triggers"), list) else [],
            body=body,
            sections=sections,
            source_path=path,
        )

    @classmethod
    def from_path_or_skill(cls, path_or_skill: "str | Path | Skill") -> "Skill":
        """Accept either a file path or an already-parsed Skill instance."""
        if isinstance(path_or_skill, Skill):
            return path_or_skill
        return cls.from_file(path_or_skill)

    def __repr__(self) -> str:
        return f"Skill(name={self.name!r}, agent={self.agent!r}, complexity={self.complexity!r})"
