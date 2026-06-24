"""
    JarEngine - Python Game Engine Wrapper (Pygame-based)

    JarEngine is a lightweight game framework built on top of Pygame
    that simplifies usage while providing higher-level abstractions for
    game development and prototyping.

    Version: jarengine-v0.1.0
    Author: Jarjarbin Studio
    Licence: GPL v3

    This engine is inspired by Pygame, modern game engine design patterns,
    and directly influenced by the architecture of NewCSFML.

    It is designed for educational purposes and small-to-medium game projects.

    It provides structured systems such as entity management, scene handling,
    render abstraction, and advanced modules like particle systems.

    WARNING:
        This is NOT Pygame itself.
        It is a custom abstraction layer built on top of Pygame.
"""

from __future__ import annotations

from sources.interns.low_classes import JEInternGraphic as _JEInternGraphic
from sources.interns.base_classe import JEInternClassBase as _JEInternClassBase
from sources.systems.container import JEContainer as _JEContainer
from sources.interns.decorators import documentation as _documentation

@_documentation
class JEInternalOwnership(_JEInternClassBase):
    """Ownership (Internal API)"""

    def __init__(self) -> None:
        """JEInternalOwnership creator"""
        super().__init__()
        self._parents: _JEContainer[_JEInternClassBase] = _JEContainer(_JEInternClassBase)
        self._children: _JEContainer[_JEInternClassBase] = _JEContainer(_JEInternClassBase)

    @property
    def parents(self) -> _JEContainer[_JEInternClassBase]:
        """Get parents list"""
        return self._parents

    def add_parent(
            self,
            parent: _JEInternClassBase
        ) -> None:
        """Add a parent"""
        self._parents.add(parent)

    @property
    def children(self) -> _JEContainer[_JEInternClassBase]:
        """Get children list"""
        return self._children

    def add_child(
            self,
            child: _JEInternClassBase
        ) -> None:
        """Add a child"""
        self._children.add(child)

@_documentation
class JEInternalEntityComponent(_JEInternGraphic, JEInternalOwnership):
    """EntityComponent (Internal API)"""

    def __init__(self, name: str) -> None:
        """JEInternalEntityComponent creator"""
        super().__init__(name)

@_documentation
class JEInternalRenderingSystems(JEInternalOwnership):
    """EntitySystems (Internal API)"""

    def __init__(
            self,
            owner: "JEGame"
        ):
        """JEPositionComponent creator"""

        super().__init__()
        self.add_parent(owner)
        owner.add_system(self)

    @staticmethod
    def update(
            window: "JEWindow",
            entities: _JEContainer["JEEntity"],
            dt: float
        ) -> None:
        """Update entities"""
        pass
