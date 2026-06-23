"""
    JarEngine - Python Game Engine Wrapper (Pygame-based)

    JarEngine is a lightweight game framework built on top of Pygame
    that simplifies usage while providing higher-level abstractions for
    game development and prototyping.

    Version: jarengine-v0.1.0
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

from sources.interns.base_classe import JEInternClassBase as _JEInternClassBase
from sources.interns.decorators import documentation as _documentation

@_documentation
@_final
class JEVector2D(_JEInternClassBase):
    """Vector (x, y)"""

    def __init__(
            self,
            x: float = 0.0,
            y: float = 0.0
        ) -> None:
        """JEVector2D creator"""
        super().__init__()

        self._vector: list[float] = [x, y]

    @property
    def x(self) -> float:
        """Get x"""
        return self._vector[0]

    @x.setter
    def x(
            self,
            x: float
        ) -> None:
        """Set x"""
        self._vector[0] = x

    @property
    def y(self) -> float:
        """Get y"""
        return self._vector[1]

    @y.setter
    def y(
            self,
            y: float
        ) -> None:
        """Set x"""
        self._vector[1] = y

    def __iter__(self):
        """Iterator over the vector"""
        return iter(self._vector)

    def __deepcopy__(
            self,
            memo
        ):
        """Deepcopy"""
        return JEVector2D(*self._vector)

@_documentation
@_final
class JEVector3D(_JEInternClassBase):
    """Vector (x, y, z)"""

    def __init__(
            self,
            x: float = 0.0,
            y: float = 0.0,
            z: float = 0.0
        ) -> None:
        """JEVector3D creator"""
        super().__init__()

        self._vector: list[float] = [x, y, z]

    @property
    def x(self) -> float:
        """Get x"""
        return self._vector[0]

    @x.setter
    def x(
            self,
            x: float
        ) -> None:
        """Set x"""
        self._vector[0] = x

    @property
    def y(self) -> float:
        """Get y"""
        return self._vector[1]

    @y.setter
    def y(
            self,
            y: float
        ) -> None:
        """Set y"""
        self._vector[1] = y

    @property
    def z(self) -> float:
        """Get z"""
        return self._vector[2]

    @z.setter
    def z(
            self,
            z: float
        ) -> None:
        """Set z"""
        self._vector[2] = z

    def __iter__(self) -> _Iterator[float]:
        """Iterator over the vector"""
        return iter(self._vector)

    def __deepcopy__(
            self,
            memo
        ):
        """Deepcopy"""
        return JEVector2D(*self._vector)
