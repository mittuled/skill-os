"""skill-os CrewAI adapter.

Converts skill-os SKILL.md files into CrewAI ``Agent`` and ``Task`` objects.

Exports
-------
Skill          -- parsed SKILL.md dataclass
skill_to_agent -- build a CrewAI Agent from a skill
skill_to_task  -- build a CrewAI Task from a skill
SkillCrew      -- fluent builder for multi-skill crews
"""

from .agent import skill_to_agent
from .crew import SkillCrew
from .skill import Skill
from .task import skill_to_task

__all__ = [
    "Skill",
    "skill_to_agent",
    "skill_to_task",
    "SkillCrew",
]
