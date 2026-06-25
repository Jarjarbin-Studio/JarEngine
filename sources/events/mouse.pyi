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

from typing import Callable, Self

from sources.events.event import JEEventCode
from sources.games.game import JEGame
from sources.events.manager import JEEvent
from sources.systems.bool import JEBool

class JEMouseCode:
    def __init__(self, mouse: int | None) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str: ...
    def __or__(self, other: JEMouseCode) -> JEMouseCodeGroup: ...
    def __eq__(self, other: JEEventCode) -> bool: ...
    def __hash__(self) -> int: ...

class JEMouseCodeGroup:
    def __init__(self, mouses: list[JEMouseCode]) -> None: ...
    def __or__(self, other: JEMouseCode | JEMouseCodeGroup) -> JEMouseCodeGroup: ...
    def __iter__(self): ...
    @property
    def mouses(self): ...

class JEMouseWatcher:
    def __init__(self, on: JEMouseCode | list[JEMouseCode] | JEMouseCodeGroup, do: Callable[[JEGame, JEEvent], None], on_press: JEBool) -> None: ...
    def match(self, event: JEEvent) -> bool: ...
    def __call__(self, game: JEGame, event: JEEvent) -> None: ...
    @property
    def on(self) -> JEMouseCodeGroup: ...
    @property
    def params(self) -> JEEventCode: ...
    @property
    def do(self) -> str: ...
