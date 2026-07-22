# =============================================================================
# JarEngine - Python Game Engine Wrapper (PyGame-based)
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

from typing import final as _final

from jarengine.interns import JTKExternError as _JTKExternError
from jarengine.interns.base_classe import JEInternBaseClass as _JEInternBaseClass
from jarengine.interns.decorators import documentation as _documentation
from jarengine.interns.helpers import (
    assertion_type as _assertion_type,
    safe_cast as _safe_cast
)

@_documentation
@_final
class JEColor(_JEInternBaseClass):

    __recursive__ = False

    def __init__(self, r = 0, g = 0, b = 0, a = 255):

        r = _safe_cast(_assertion_type(r, int, "r must be of type 'int'"), int)
        g = _safe_cast(_assertion_type(g, int, "g must be of type 'int'"), int)
        b = _safe_cast(_assertion_type(b, int, "b must be of type 'int'"), int)
        a = _safe_cast(_assertion_type(a, int, "a must be of type 'int'"), int)

        super().__init__()

        self._color = [r, g, b, a]

        for c in self._color:
            if not (0 <= c <= 255):
                raise _JTKExternError.Error.ErrorValue("\nInvalid color, every channels must be between 0 and 255.")

    @property
    def r(self):
        return self._color[0]

    @r.setter
    def r(self, r):

        r = _safe_cast(_assertion_type(r, int, "r must be of type 'int'"), int)

        self._color[0] = r

    @property
    def g(self):
        return self._color[1]

    @g.setter
    def g(self, g):

        g = _safe_cast(_assertion_type(g, int, "g must be of type 'int'"), int)

        self._color[1] = g

    @property
    def b(self):
        return self._color[2]

    @b.setter
    def b(self, b):

        b = _safe_cast(_assertion_type(b, int, "b must be of type 'int'"), int)

        self._color[2] = b

    @property
    def a(self):
        return self._color[3]

    @a.setter
    def a(self, a):

        a = _safe_cast(_assertion_type(a, int, "a must be of type 'int'"), int)

        self._color[3] = a

    @property
    def rgb(self):
        return tuple(self._color[:3])

    @rgb.setter
    def rgb(self, rgb):

        rgb = _safe_cast(_assertion_type(rgb, (tuple, list), "rgb must be of type 'tuple' or 'list'"), tuple)

        self.r = rgb[0]
        self.g = rgb[1]
        self.b = rgb[2]

    @property
    def rgba(self):
        return tuple(self._color)

    @rgba.setter
    def rgba(self, rgba):

        rgba = _safe_cast(_assertion_type(rgba, (tuple, list), "rgba must be of type 'tuple' or 'list'"), tuple)

        self.r = rgba[0]
        self.g = rgba[1]
        self.b = rgba[2]
        self.a = rgba[3]

    def __iter__(self):
        return iter(self._color)

    def __deepcopy__(self, memo):
        return JEColor(*self._color)
