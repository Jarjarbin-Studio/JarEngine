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

from typing import final as _final

from sources.interns.base_classe import JEInternClassBase as _JEInternClassBase

@_final
class JEVector2D(_JEInternClassBase):

    def __init__(
            self,
            x: float = 0.0,
            y: float = 0.0
        ) -> None:
        super().__init__()

        self._vector: list[float] = [x, y]

    @property
    def x(self) -> float:
        return self._vector[0]

    @property
    def y(self) -> float:
        return self._vector[1]

    def __deepcopy__(
            self,
            memo
        ):
        return JEVector2D(*self._vector)

@_final
class JEVector3D(_JEInternClassBase):

    def __init__(
            self,
            x: float = 0.0,
            y: float = 0.0,
            z: float = 0.0
        ) -> None:
        super().__init__()

        self._vector: list[float] = [x, y, z]

    @property
    def x(self) -> float:
        return self._vector[0]

    @property
    def y(self) -> float:
        return self._vector[1]

    @property
    def z(self) -> float:
        return self._vector[2]

    def __deepcopy__(
            self,
            memo
        ):
        return JEVector2D(*self._vector)
