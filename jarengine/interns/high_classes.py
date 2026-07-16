# =============================================================================
# JarEngine - Python Game Engine Wrapper (Pygame-based)
# =============================================================================
#
# JarEngine is a lightweight game framework built on top of Pygame
# that simplifies usage while providing higher-level abstractions for
# game development and prototyping.
#
# =============================================================================
# Version: jarengine-v1.7
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

from jarengine.interns.low_classes import JEInternGraphic as _JEInternGraphic
from jarengine.interns.base_classe import JEInternBaseClass as _JEInternBaseClass
from jarengine.interns import JTKExternError as _JTKExternError
from jarengine.systems.container import JEContainer as _JEContainer
from jarengine.interns.decorators import documentation as _documentation
from jarengine.systems.bool import JEBool as _JEBool

@_documentation
class JEInternOwnership(_JEInternBaseClass):

    def __init__(self):
        super().__init__()
        self._parents = _JEContainer(_JEInternBaseClass)
        self._children = _JEContainer(_JEInternBaseClass)

    @property
    def parents(self):
        return self._parents

    def add_parent(self, parent):
        self._parents.add(parent)

    @property
    def children(self):
        return self._children

    def add_child(self, child):
        self._children.add(child)

@_documentation
class JEInternEntityComponent(_JEInternGraphic, JEInternOwnership):

    def __init__(self, owner, _type):
        super().__init__(f"{_type.__name__}({owner.jeid})")
        self.add_parent(owner)
        owner.add_component(self)

    def __call__(self):
        raise NotImplementedError

    def copy(self):
        raise NotImplementedError

    def __deepcopy__(self, memo):
        return self.copy()

@_documentation
class JEInternSystems(JEInternOwnership):

    def __init__(self, owner):
        super().__init__()
        self.cache = []
        self._required = []
        self.add_parent(owner)
        owner.add_system(self)

    def refresh(self):
        from jarengine.games.game import JEGame as _JEGame

        self.cache.clear()

        game = self.parents.get(_type=_JEGame)

        if not game:
            return

        for entity in game._iter_entities():
            if self.accepts(entity.components):
                self.cache.append(entity)

        self.sort_cache()

    def refresh_entity(self, entity):
        if self.accepts(entity.components):
            if entity not in self.cache:
                self.cache.append(entity)
                self.sort_cache()
            return

        if entity in self.cache:
            self.cache.remove(entity)

    def sort_cache(self):
        pass

    def accepts(self, components):
        try:
            return _JEBool(all(components.get(_type=req) is not None for req in self._required))
        except Exception:
            return _JEBool(0)

    @staticmethod
    def update(window, entity, entities, dt):
        raise NotImplementedError
