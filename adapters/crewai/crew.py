"""SkillCrew: convenience class for assembling multi-skill CrewAI crews.

Usage::

    from adapters.crewai import SkillCrew
    from crewai import Process

    result = (
        SkillCrew()
        .add("pm", "agents/product/product-manager/requirements-extractor/SKILL.md")
        .add("eng", "agents/engineering/sr-backend-developer/builder/SKILL.md")
        .process(Process.sequential)
        .kickoff(inputs={"feature": "OAuth2 login"})
    )
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from .agent import skill_to_agent
from .skill import Skill
from .task import skill_to_task


class SkillCrew:
    """Fluent builder for a CrewAI ``Crew`` assembled from skill-os skills.

    Each :meth:`add` call registers a (role_alias, skill_path) pair.
    When :meth:`kickoff` is called the crew is assembled lazily:

    1. Each skill is parsed and wrapped into a :class:`crewai.Agent`.
    2. Each agent is paired with a :class:`crewai.Task` derived from the
       same skill.
    3. An optional ``context`` string is injected into every task
       description via the ``inputs`` dict passed to :meth:`kickoff`.
    4. A :class:`crewai.Crew` is built and kicked off.
    """

    def __init__(self) -> None:
        self._entries: List[Tuple[str, str | Path | Skill]] = []
        self._process: Optional[Any] = None
        self._llm: Optional[Any] = None
        self._crew_kwargs: Dict[str, Any] = {}

    # ------------------------------------------------------------------
    # Builder methods (return self for chaining)
    # ------------------------------------------------------------------

    def add(self, alias: str, path_or_skill: "str | Path | Skill") -> "SkillCrew":
        """Register a skill under a human-readable alias.

        Parameters
        ----------
        alias:
            Short label for this agent (e.g. ``"pm"``, ``"eng"``).
            Used only for bookkeeping; CrewAI uses the ``agent.role``.
        path_or_skill:
            Path to a ``SKILL.md`` file or a parsed :class:`Skill`.
        """
        self._entries.append((alias, path_or_skill))
        return self

    def process(self, process: Any) -> "SkillCrew":
        """Set the CrewAI ``Process`` (sequential, hierarchical, etc.)."""
        self._process = process
        return self

    def llm(self, llm: Any) -> "SkillCrew":
        """Set a shared LLM instance passed to every agent."""
        self._llm = llm
        return self

    def crew_kwargs(self, **kwargs: Any) -> "SkillCrew":
        """Pass additional keyword arguments to the ``Crew`` constructor."""
        self._crew_kwargs.update(kwargs)
        return self

    # ------------------------------------------------------------------
    # Terminal method
    # ------------------------------------------------------------------

    def kickoff(self, inputs: Optional[Dict[str, Any]] = None) -> Any:
        """Assemble and run the crew.

        Parameters
        ----------
        inputs:
            Optional dict of runtime inputs forwarded to ``Crew.kickoff``.
            If a ``"context"`` key is present its value is appended to
            every task description (useful for feature descriptions,
            domain constraints, etc.).

        Returns
        -------
        The CrewAI ``CrewOutput`` returned by ``Crew.kickoff``.
        """
        try:
            from crewai import Crew  # type: ignore[import]
        except ImportError as exc:
            raise ImportError(
                "crewai is required for SkillCrew. "
                "Install it with: pip install crewai"
            ) from exc

        if not self._entries:
            raise ValueError("SkillCrew has no skills — call .add() at least once.")

        inputs = inputs or {}
        shared_context = inputs.get("context")

        agents: List[Any] = []
        tasks: List[Any] = []
        previous_tasks: List[Any] = []

        for _alias, path_or_skill in self._entries:
            skill = Skill.from_path_or_skill(path_or_skill)
            agent = skill_to_agent(skill, llm=self._llm)
            task = skill_to_task(
                skill,
                agent=agent,
                context=shared_context,
                context_tasks=previous_tasks if previous_tasks else None,
            )
            agents.append(agent)
            tasks.append(task)
            previous_tasks.append(task)

        crew_kwargs: Dict[str, Any] = {
            "agents": agents,
            "tasks": tasks,
            **self._crew_kwargs,
        }
        if self._process is not None:
            crew_kwargs["process"] = self._process

        crew = Crew(**crew_kwargs)
        return crew.kickoff(inputs=inputs)

    # ------------------------------------------------------------------
    # Introspection helpers
    # ------------------------------------------------------------------

    def __repr__(self) -> str:
        aliases = [alias for alias, _ in self._entries]
        return f"SkillCrew(entries={aliases!r}, process={self._process!r})"
