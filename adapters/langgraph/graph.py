"""
graph.py — SkillGraph: convenience builder for multi-skill LangGraph graphs.

SkillGraph wraps LangGraph's StateGraph with a fluent API for chaining
Skill OS skills as nodes.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .node import create_async_skill_node, create_skill_node
from .skill import Skill


class SkillGraph:
    """
    Fluent builder for multi-skill LangGraph graphs.

    Each call to add_node() registers a skill as a named node.
    Edges between nodes are added via add_edge().
    Call compile() to get a runnable LangGraph app.

    Example::

        from langchain_anthropic import ChatAnthropic
        from skill_os_langgraph import SkillGraph

        llm = ChatAnthropic(model="claude-sonnet-4-6")

        app = (
            SkillGraph(llm)
            .add_node("research", "agents/engineering/.../SKILL.md")
            .add_node("review",   "agents/engineering/.../SKILL.md")
            .add_edge("research", "review")
            .compile()
        )

        result = app.invoke({"messages": [{"role": "user", "content": "..."}]})
    """

    def __init__(self, llm: Any, *, async_mode: bool = False) -> None:
        """
        Args:
            llm: A LangChain chat model instance.
            async_mode: If True, registers async node functions (ainvoke-compatible).
        """
        self._llm = llm
        self._async_mode = async_mode
        self._nodes: list[tuple[str, str | Path | Skill]] = []
        self._edges: list[tuple[str, str]] = []
        self._entry_point: str | None = None
        self._finish_point: str | None = None

    # ------------------------------------------------------------------
    # Builder API
    # ------------------------------------------------------------------

    def add_node(
        self,
        name: str,
        skill_path_or_skill: str | Path | Skill,
    ) -> "SkillGraph":
        """
        Register a skill as a named node.

        Args:
            name: Node name used in edges and entry/finish points.
            skill_path_or_skill: Path to SKILL.md or a pre-loaded Skill object.

        Returns:
            self, for chaining.
        """
        self._nodes.append((name, skill_path_or_skill))
        return self

    def add_edge(self, source: str, target: str) -> "SkillGraph":
        """
        Add a directed edge between two nodes.

        Args:
            source: Name of the source node.
            target: Name of the target node (use END for terminal nodes).

        Returns:
            self, for chaining.
        """
        self._edges.append((source, target))
        return self

    def set_entry_point(self, name: str) -> "SkillGraph":
        """
        Explicitly set the graph entry point.

        If not called, the first node registered via add_node() is used.
        """
        self._entry_point = name
        return self

    def set_finish_point(self, name: str) -> "SkillGraph":
        """
        Explicitly set the graph finish point (routes to END).

        If not called, the last node registered via add_node() is used.
        """
        self._finish_point = name
        return self

    def compile(self) -> Any:
        """
        Build and compile the LangGraph StateGraph.

        Returns:
            A compiled LangGraph app (supports invoke / ainvoke / stream).

        Raises:
            ImportError: If langgraph is not installed.
            ValueError: If no nodes have been registered.
        """
        try:
            from langgraph.graph import END, StateGraph
            from langgraph.graph.message import MessagesState
        except ImportError as e:
            raise ImportError(
                "langgraph is required: pip install 'skill-os-langgraph[langgraph]'"
            ) from e

        if not self._nodes:
            raise ValueError("SkillGraph has no nodes — call add_node() first.")

        graph = StateGraph(MessagesState)

        # Register all nodes
        node_factory = (
            create_async_skill_node if self._async_mode else create_skill_node
        )
        for node_name, skill_ref in self._nodes:
            node_fn = node_factory(skill_ref, self._llm)
            graph.add_node(node_name, node_fn)

        # Set entry point
        entry = self._entry_point or self._nodes[0][0]
        graph.set_entry_point(entry)

        # Add explicit edges
        registered_edge_sources = {src for src, _ in self._edges}
        for source, target in self._edges:
            if target == "END":
                graph.add_edge(source, END)
            else:
                graph.add_edge(source, target)

        # Auto-wire: last node → END if not already connected
        last_node_name = self._finish_point or self._nodes[-1][0]
        if last_node_name not in registered_edge_sources:
            graph.add_edge(last_node_name, END)

        # Auto-wire sequential chain if no edges were declared
        if not self._edges and len(self._nodes) > 1:
            for i in range(len(self._nodes) - 1):
                src_name = self._nodes[i][0]
                dst_name = self._nodes[i + 1][0]
                graph.add_edge(src_name, dst_name)

        return graph.compile()
