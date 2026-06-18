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

from sources.interns.base_classes import JEInternClassBase as _JEInternClassBase

@_final
class JEColor(_JEInternClassBase):

    def __init__(
            self,
            r: int = 0,
            g: int = 0,
            b: int = 0,
            a: int = 0
        ) -> None:
        super().__init__()

        self._color: list[int] = [r, g, b, a]

    @property
    def r(self) -> int:
        return self._color[0]

    @property
    def g(self) -> int:
        return self._color[1]

    @property
    def b(self) -> int:
        return self._color[2]

    @property
    def a(self) -> int:
        return self._color[3]

    @property
    def rgb(self) -> tuple[int, ...]:
        return tuple(self._color[:3])

    @property
    def rgba(self) -> tuple[int, ...]:
        return tuple(self._color)
