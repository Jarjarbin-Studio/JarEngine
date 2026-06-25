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

from typing import Self

from sources.events.keyboard import JEKeyCode
from sources.events.mouse import JEMouseCode
from sources.systems.bool import JEBool

class JEInput:
    _instance: Self
    _is_created: JEBool
    def __init__(self) -> None: ...
    def update(self) -> None: ...
    def is_key_down(self, key: JEKeyCode) -> bool: ...
    def is_mouse_down(self, button: JEMouseCode) -> bool: ...
    def mouse_pos(self) -> tuple[int, int]: ...
    def __call__(self, code: JEKeyCode | JEMouseCode) -> bool: ...
