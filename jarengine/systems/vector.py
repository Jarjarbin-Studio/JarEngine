"""
    JarEngine - Python Game Engine Wrapper (Pygame-based)

    JarEngine is a lightweight game framework built on top of Pygame
    that simplifies usage while providing higher-level abstractions for
    game development and prototyping.

    Version: jarengine-v1.6
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

from typing import (
    final as _final,
    Iterator as _Iterator
)

from jarengine.interns.base_classe import JEInternBaseClass as _JEInternBaseClass
from jarengine.interns.decorators import documentation as _documentation

@_documentation
@_final
class JEVector2D(_JEInternBaseClass):
    """Vector (x, y)"""

    __recursive__ = False

    def __init__(self, x = 0.0, y = 0.0):
        """JEVector2D creator"""
        super().__init__()

        self._vector = [x, y]

    @property
    def x(self):
        """Get x"""
        return self._vector[0]

    @x.setter
    def x(self, x):
        """Set x"""
        self._vector[0] = x

    @property
    def y(self):
        """Get y"""
        return self._vector[1]

    @y.setter
    def y(self, y):
        """Set x"""
        self._vector[1] = y

    def __iter__(self):
        """Iterator over the vector"""
        return iter(self._vector)

    def __deepcopy__(self, memo):
        """Deepcopy"""
        return JEVector2D(*self._vector)

@_documentation
@_final
class JEVector3D(_JEInternBaseClass):
    """Vector (x, y, z)"""

    __recursive__ = False

    def __init__(self, x = 0.0, y = 0.0, z = 0.0):
        """JEVector3D creator"""
        super().__init__()

        self._vector: list[float] = [x, y, z]

    @property
    def x(self):
        """Get x"""
        return self._vector[0]

    @x.setter
    def x(self, x):
        """Set x"""
        self._vector[0] = x

    @property
    def y(self):
        """Get y"""
        return self._vector[1]

    @y.setter
    def y(self, y):
        """Set y"""
        self._vector[1] = y

    @property
    def z(self):
        """Get z"""
        return self._vector[2]

    @z.setter
    def z(self, z):
        """Set z"""
        self._vector[2] = z

    def __iter__(self):
        """Iterator over the vector"""
        return iter(self._vector)

    def __deepcopy__(self, memo):
        """Deepcopy"""
        return JEVector2D(*self._vector)
