# =============================================================================
# JarEngine - Python Game Engine Wrapper (Pygame-based)
# =============================================================================
#
# JarEngine is a lightweight game framework built on top of Pygame
# that simplifies usage while providing higher-level abstractions for
# game development and prototyping.
#
# =============================================================================
# Version: jarengine-v1.8
# Author: Jarjarbin Studio
# Licence: GPL v3
# =============================================================================
#
# This engine is inspired by Pygame, modern game engine design patterns,
# and directly influenced by the architecture of NewCSFML.
#
# It is designed for educational purposes and small-to-medium game projects.
#
# It provides structured systems such as entity management, scene handling,
# render abstraction, and advanced modules like particle systems.
#
# =============================================================================
# WARNING:
# =============================================================================
#
# This is NOT Pygame itself.
# It is a custom abstraction layer built on top of Pygame.
#
# =============================================================================

from __future__ import annotations

from jarengine.interns.high_classes import JEInternOwnership as _JEInternOwnership
from jarengine.interns.final_classes import JEInternEmptyComponent as _JEInternEmptyComponent
from jarengine.interns.high_classes import JEInternEntityComponent as _JEInternEntityComponent
from jarengine.interns.low_classes import JEInternGraphicalObject as _JEInternGraphicalObject
from jarengine.systems.container import JEContainer as _JEContainer
from jarengine.systems.bool import JEBool as _JEBool
from jarengine.interns.decorators import documentation as _documentation

@_documentation
class JEEntity(_JEInternGraphicalObject, _JEInternOwnership):

    def __init__(self, *, name = "JEEntity"):
        super().__init__(name)
        self._components = _JEContainer(_JEInternEntityComponent, _JEBool(1))
        self._components.add(_JEInternEmptyComponent(self))

    @property
    def parent(self):
        return self._parents.get(_type=JEEntity, default=None)

    @property
    def components(self):
        return self._components

    def add_component(self, component):
        self._components.add(component)

    def get(self, component):
        for c in self._components:
            if isinstance(c, component):
                return c
        return self._components.get(_type=_JEInternEmptyComponent)

    def copy(self):
        new_entity = JEEntity(name = self.name)
        for c in self._components:
            c.copy(new_entity)
        return new_entity

    def __deepcopy__(self, memo):
        return self.copy()
