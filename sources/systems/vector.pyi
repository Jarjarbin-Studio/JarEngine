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

class JEVector2D:
    def __init__(self, x: float, y: float) -> None: ...
    @property
    def x(self) -> float: ...
    @x.setter
    def x(self, x: float) -> None: ...
    @property
    def y(self) -> float: ...
    @y.setter
    def y(self, y: float) -> None: ...
    def __iter__(self): ...

class JEVector3D:
    def __init__(self, x: float, y: float, z: float) -> None: ...
    @property
    def x(self) -> float: ...
    @x.setter
    def x(self, x: float) -> None: ...
    @property
    def y(self) -> float: ...
    @y.setter
    def y(self, y: float) -> None: ...
    @property
    def z(self) -> float: ...
    @z.setter
    def z(self, z: float) -> None: ...
    def __iter__(self) -> Iterator[float]: ...
