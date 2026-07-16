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

from typing import (
    final as _final,
    Iterator as _Iterator
)

from jarengine.interns.base_classe import JEInternBaseClass as _JEInternBaseClass
from jarengine.interns.decorators import documentation as _documentation

@_documentation
@_final
class JEColor(_JEInternBaseClass):

    __recursive__ = False

    def __init__(self, r = 0, g = 0, b = 0, a = 255):
        super().__init__()

        self._color = [r, g, b, a]

    @property
    def r(self):
        return self._color[0]

    @r.setter
    def r(self, r):
        self._color[0] = r

    @property
    def g(self):
        return self._color[1]

    @g.setter
    def g(self, g):
        self._color[1] = g

    @property
    def b(self):
        return self._color[2]

    @b.setter
    def b(self, b):
        self._color[2] = b

    @property
    def a(self):
        return self._color[3]

    @a.setter
    def a(self, a):
        self._color[3] = a

    @property
    def rgb(self):
        return tuple(self._color[:3])

    @property
    def rgba(self):
        return tuple(self._color)

    def __iter__(self):
        return iter(self._color)

    def __deepcopy__(self, memo):
        return JEColor(*self._color)
