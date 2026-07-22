# =============================================================================
# JarEngine - Python Game Engine Wrapper (PyGame-based)
# =============================================================================
#
# JarEngine is a lightweight game framework built on top of PyGame
# that simplifies usage while providing higher-level abstractions for
# game development and prototyping.
#
# =============================================================================
# Version: jarengine-v1.8
# Author: Jarjarbin Studio
# Licence: GPL v3
# =============================================================================
#
# This engine is inspired by PyGame, modern game engine design patterns,
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
# This is NOT PyGame itself.
# It is a custom abstraction layer built on top of PyGame.
#
# =============================================================================

from __future__ import annotations

from jarengine.interns.low_classes import (
    JEInternGraphic as _JEInternGraphic,
    JEInternGraphicalObject as _JEInternGraphicalObject
)
from jarengine.interns.base_classe import JEInternBaseClass as _JEInternBaseClass
from jarengine.systems.container import JEContainer as _JEContainer
from jarengine.interns.decorators import documentation as _documentation
from jarengine.systems.bool import JEBool as _JEBool
from jarengine.interns.helpers import assertion_type as _assertion_type

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

        _assertion_type(parent, _JEInternBaseClass, "parent must be of type 'JEInternBaseClass'")

        self._parents.add(parent)
        self.on_parent_added(parent)

    @property
    def children(self):
        return self._children

    def add_child(self, child):

        _assertion_type(child, _JEInternBaseClass, "child must be of type 'JEInternBaseClass'")

        self._children.add(child)

    def on_parent_added(self, parent):
        pass

@_documentation
class JEInternEntityComponent(_JEInternGraphic, JEInternOwnership):

    def __init__(self, owner, _type):
        from jarengine.entity.entity import JEEntity as _JEEntity

        _assertion_type(owner, _JEEntity, "owner must be of type 'JEEntity'")
        _assertion_type(_type, type, "_type must be of type 'type'")

        super().__init__(f"{_type.__name__}({owner.jeid})")
        self.add_parent(owner)
        owner.add_component(self)

    def __call__(self):
        raise NotImplementedError

    def copy(self, new_owner):
        from jarengine.entity.entity import JEEntity as _JEEntity

        _assertion_type(new_owner, _JEEntity, "new_owner must be of type 'JEEntity'")

        raise NotImplementedError

    def __deepcopy__(self, memo):
        raise NotImplementedError

@_documentation
class JEInternSystems(JEInternOwnership):

    def __init__(self, owner):
        from jarengine.games.game import JEGame as _JEGame

        _assertion_type(owner, _JEGame, "owner must be of type 'JEGame'")

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
        from jarengine.entity.entity import JEEntity as _JEEntity

        _assertion_type(entity, _JEEntity, "entity must be of type 'JEEntity'")

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
        _assertion_type(components, _JEContainer, "components must be of type 'JEContainer'")

        try:
            return _JEBool(all(components.get(_type=req) is not None for req in self._required))
        except Exception:
            return _JEBool(0)

    @staticmethod
    def update(window, entity, entities, dt):
        raise NotImplementedError
