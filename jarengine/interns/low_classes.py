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

from jarengine.interns.base_classe import JEInternBaseClass as _JEInternBaseClass
from jarengine.systems.bool import JEBool as _JEBool
from jarengine.interns.decorators import documentation as _documentation

@_documentation
class JEInternGraphic(_JEInternBaseClass):

    def __init__(self, name):
        super().__init__()

        self.name = name
        self._name_hash = hash(self.name)
        self._object_hash = hash(self)
        self._destroyed = _JEBool(0)

    def destroy(self):
        self._destroyed = _JEBool(1)

    @property
    def is_alive(self) -> _JEBool:
        return _JEBool(not self._destroyed)

@_documentation
class JEInternGraphicalObject(JEInternGraphic):

    def __init__(self, name):
        super().__init__(name)

        self._dirty = _JEBool(1)

    def update(self, dt):
        raise NotImplementedError

    def mark_dirty(self):
        self._dirty = _JEBool(1)

    def clear_dirty(self):
        self._dirty = _JEBool(0)

    @property
    def is_dirty(self) -> _JEBool:
        return self._dirty

@_documentation
class JEInternResource(JEInternGraphic):

    def __init__(self, name, path):
        super().__init__(name)

        self._path = path

    @property
    def path(self):
        return self._path

    def __deepcopy__(self, memo):
        return self
