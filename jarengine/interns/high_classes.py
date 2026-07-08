"""
    JarEngine - Python Game Engine Wrapper (Pygame-based)

    JarEngine is a lightweight game framework built on top of Pygame
    that simplifies usage while providing higher-level abstractions for
    game development and prototyping.

    Version: jarengine-v1.5
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

from jarengine.interns.low_classes import JEInternGraphic as _JEInternGraphic
from jarengine.interns.base_classe import JEInternBaseClass as _JEInternBaseClass
from jarengine.systems.container import JEContainer as _JEContainer
from jarengine.interns.decorators import documentation as _documentation
from jarengine.systems.bool import JEBool as _JEBool

@_documentation
class JEInternOwnership(_JEInternBaseClass):
    """Ownership (Internal API)"""

    def __init__(self):
        """JEInternOwnership creator"""
        super().__init__()
        self._parents = _JEContainer(_JEInternBaseClass)
        self._children = _JEContainer(_JEInternBaseClass)

    @property
    def parents(self):
        """Get parents list"""
        return self._parents

    def add_parent(self, parent):
        """Add a parent"""
        self._parents.add(parent)

    @property
    def children(self):
        """Get children list"""
        return self._children

    def add_child(self, child):
        """Add a child"""
        self._children.add(child)

@_documentation
class JEInternEntityComponent(_JEInternGraphic, JEInternOwnership):
    """EntityComponent (Internal API)"""

    def __init__(self, owner, _type):
        """JEInternEntityComponent creator"""
        super().__init__(f"{_type.__name__}({owner.jeid})")
        self.add_parent(owner)
        owner.add_component(self)

    def __call__(self):
        """Get Component"""
        raise NotImplementedError

    def copy(self):
        """Copy Component"""
        raise NotImplementedError

    def __deepcopy__(self, memo):
        return self.copy()

@_documentation
class JEInternSystems(JEInternOwnership):
    """Systems (Internal API)"""

    def __init__(self, owner):
        """JEInternSystems creator"""

        super().__init__()
        self.add_parent(owner)
        owner.add_system(self)
        self._required = []

    def accepts(self, components):
        """Check if all required components are available"""
        try:
            return _JEBool(all(components.get(_type=req) is not None for req in self._required))
        except Exception:
            return _JEBool(0)

    @staticmethod
    def update(window, entity, entities, dt):
        """Update entities"""
        raise NotImplementedError
