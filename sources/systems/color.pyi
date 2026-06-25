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

from typing import Iterator

class JEColor:
    def __init__(self, r: int, g: int, b: int, a: int) -> None: ...
    @property
    def r(self) -> int: ...
    @r.setter
    def r(self, r: int) -> None: ...
    @property
    def g(self) -> int: ...
    @g.setter
    def g(self, g: int) -> None: ...
    @property
    def b(self) -> int: ...
    @b.setter
    def b(self, b: int) -> None: ...
    @property
    def a(self) -> int: ...
    @a.setter
    def a(self, a: int) -> None: ...
    @property
    def rgb(self) -> tuple[int, int, int]: ...
    @property
    def rgba(self) -> tuple[int, int, int, int]: ...
    def __iter__(self) -> Iterator[float]: ...
