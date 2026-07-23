# =============================================================================
# JarEngine - Python Game Engine Wrapper (PyGame-based)
# =============================================================================
#
# JarEngine is a lightweight game framework built on top of PyGame
# that simplifies usage while providing higher-level abstractions for
# game development and prototyping.
#
# =============================================================================
# Version: jarengine-v1.10
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

from typing import final as _final

from jarengine.systems.transform import JETransform as _JETransform
from jarengine.interns.decorators import documentation as _documentation
from jarengine.interns.helpers import (
    assertion_type as _assertion_type,
    safe_cast as _safe_cast
)
import jarengine.interns.log as _log

@_documentation
@_final
class JEVector2D(_JETransform):

    __recursive__ = False

    def __init__(self, x = 0.0, y = 0.0):

        x = _safe_cast(_assertion_type(x, (int, float), "x must be of type 'int' or 'float'"), float)
        y = _safe_cast(_assertion_type(y, (int, float), "y must be of type 'int' or 'float'"), float)

        super().__init__()

        self._vector = [float(x), float(y)]

        _log.log("DEBUG", "OBJECT", f"JEVector2D: Created", self.jeid, x, y)

    @property
    def x(self):
        return self._vector[0]

    @x.setter
    def x(self, x):

        x = _safe_cast(_assertion_type(x, (int, float), "x must be of type 'int' or 'float'"), float)

        self._vector[0] = x

    @property
    def y(self):
        return self._vector[1]

    @y.setter
    def y(self, y):

        y = _safe_cast(_assertion_type(y, (int, float), "y must be of type 'int' or 'float'"), float)

        self._vector[1] = y

    def __iter__(self):
        return iter(self._vector)

    def __deepcopy__(self, memo):
        return JEVector2D(*self._vector)

@_documentation
@_final
class JEVector3D(_JETransform):

    __recursive__ = False

    def __init__(self, x = 0.0, y = 0.0, z = 0.0):

        x = _safe_cast(_assertion_type(x, (int, float), "x must be of type 'int' or 'float'"), float)
        y = _safe_cast(_assertion_type(y, (int, float), "y must be of type 'int' or 'float'"), float)
        z = _safe_cast(_assertion_type(z, (int, float), "z must be of type 'int' or 'float'"), float)

        super().__init__()

        self._vector = [float(x), float(y), float(z)]

        _log.log("DEBUG", "OBJECT", f"JEVector3D: Created", self.jeid, x, y, z)

    @property
    def x(self):
        return self._vector[0]

    @x.setter
    def x(self, x):

        x = _safe_cast(_assertion_type(x, (int, float), "x must be of type 'int' or 'float'"), float)

        self._vector[0] = x

    @property
    def y(self):
        return self._vector[1]

    @y.setter
    def y(self, y):

        y = _safe_cast(_assertion_type(y, (int, float), "y must be of type 'int' or 'float'"), float)

        self._vector[1] = y

    @property
    def z(self):
        return self._vector[2]

    @z.setter
    def z(self, z):

        z = _safe_cast(_assertion_type(z, (int, float), "z must be of type 'int' or 'float'"), float)

        self._vector[2] = z

    def __iter__(self):
        return iter(self._vector)

    def __deepcopy__(self, memo):
        return JEVector3D(*self._vector)
