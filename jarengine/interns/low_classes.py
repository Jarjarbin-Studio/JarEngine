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
from jarengine.interns.helpers import (
    assertion_type as _assertion_type,
    safe_cast as _safe_cast
)
import jarengine.interns.log as _log

@_documentation
class JEInternGraphic(_JEInternBaseClass):

    def __init__(self, name):

        name = _safe_cast(_assertion_type(name, str, "name must be of type 'str'"), str)

        super().__init__()

        self.name = name
        self._name_hash = hash(self.name)
        self._object_hash = hash(self)
        self._destroyed = _JEBool(0)

        _log.log("DEBUG", "OBJECT", f"JEInternGraphic: Created", self.jeid, name)

    def destroy(self):
        self._destroyed = _JEBool(1)

    @property
    def is_alive(self):
        return _JEBool(not self._destroyed)

@_documentation
class JEInternGraphicalObject(JEInternGraphic):

    def __init__(self, name):

        name = _safe_cast(_assertion_type(name, str, "name must be of type 'str'"), str)

        super().__init__(name)

        self._dirty = _JEBool(1)

        _log.log("DEBUG", "OBJECT", f"JEInternGraphicalObject: Created", self.jeid, name)

    def update(self, dt):
        pass

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

        name = _safe_cast(_assertion_type(name, str, "name must be of type 'str'"), str)
        path = _safe_cast(_assertion_type(path, str, "path must be of type 'str'"), str)

        super().__init__(name)

        self._path = path

        _log.log("DEBUG", "OBJECT", f"JEInternResource: Created", self.jeid, name, path)

    @property
    def path(self):
        return self._path

    def __deepcopy__(self, memo):
        return self
