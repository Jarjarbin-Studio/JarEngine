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

from typing import final as _final

from interns.final_classes import JEInternEmptyComponent as _JEInternEmptyComponent
from sources.interns.high_classes import JEInternalEntityComponent as _JEInternalEntityComponent
from sources.interns.low_classes import JEInternGraphicalObject as _JEInternGraphicalObject
from sources.systems.container import JEContainer as _JEContainer
from sources.systems.bool import JEBool as _JEBool
from sources.interns.decorators import documentation as _documentation

@_documentation
@_final
class JEEntity(_JEInternGraphicalObject):
    """Entity"""

    def __init__(
            self,
            name: str = "JEEntity"
        ) -> None:
        """JEEntity creator"""
        super().__init__(name)
        self._components: _JEContainer[_JEInternalEntityComponent] = _JEContainer(_JEInternalEntityComponent, _JEBool(1))
        self._components.add(_JEInternEmptyComponent(self))

    @property
    def components(self) -> _JEContainer[_JEInternalEntityComponent]:
        """Get components"""
        return self._components

    def add_component(
            self,
            component: _JEInternalEntityComponent
        ) -> None:
        """Add component object"""
        self._components.add(component)

    def get(
            self,
            component: type[_JEInternalEntityComponent]
        ) -> _JEInternalEntityComponent:

        for c in self._components:
            if isinstance(c, component):
                return c
        return self._components.get(name=f"JEEmptyComponent({self.jeid})")
