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

class JEKeyCode:
    _instances: dict[int, Self]
    _name_cache: dict[int, str]
    def __init__(self, key: int | None) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str: ...
    def __or__(self, other: JEKeyCode) -> JEKeyCodeGroup: ...
    def __eq__(self, other: JEEventCode) -> bool: ...
    def __hash__(self) -> int: ...

class JEKeyCodeGroup:
    def __init__(self, keys: list[JEKeyCode]) -> None: ...
    def __or__(self, other: JEKeyCode | JEKeyCodeGroup) -> JEKeyCodeGroup: ...
    def __iter__(self): ...
    @property
    def keys(self): ...

class JEKeyWatcher:
    def __init__(self, on: JEKeyCode | list[JEKeyCode] | JEKeyCodeGroup, do: Callable[[JEGame, JEEvent], None], on_press: JEBool) -> None: ...
    def match(self, event: JEEvent) -> bool: ...
    def __call__(self, game: JEGame, event: JEEvent) -> None: ...
    @property
    def on(self) -> JEKeyCodeGroup: ...
    @property
    def params(self) -> JEEventCode: ...
    @property
    def do(self) -> str: ...
