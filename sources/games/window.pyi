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

from typing import Self, Any

from sources.interns import PGIntern
from sources.interns.final_classes import JEInternWindowSettings
from sources.systems.color import JEColor
from sources.systems.bool import JEBool

class JEWindow:
    _instance: Self
    _is_created: JEBool
    def __init__(self, *, size: tuple[int, int], flags: int, fps: int, depth: int, display: int, vsync: int, title: str): ...
    @property
    def screen(self) -> PGIntern.Surface: ...
    @property
    def settings(self) -> JEInternWindowSettings: ...
    def fill(self, color: JEColor | tuple[int, int, int] | tuple[int, int, int, int]) -> None: ...
    def blit(self, source: PGIntern.Surface, dest: Any): ...
