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
    Self
)

from sources.interns import PGIntern
from sources.events.event import JEEventCode, JEEventWatcher
from sources.events.keyboard import JEKeyCode, JEKeyWatcher
from sources.events.mouse import JEMouseCode, JEMouseWatcher
from sources.systems.bool import JEBool
from sources.games.game import JEGame

class JEEvent:
    def __init__(self, event: PGIntern.event.Event) -> None: ...
    @property
    def type(self) -> JEEventCode: ...
    @property
    def key(self) -> JEKeyCode | None: ...
    @property
    def mouse(self) -> JEMouseCode | None: ...

class JEEventHandler:
    def __init__(self) -> None: ...
    @property
    def watchers(self) -> list[JEEventWatcher | JEKeyWatcher | JEMouseWatcher]: ...
    def add(self, watcher: JEEventWatcher | JEKeyWatcher | JEMouseWatcher) -> None: ...
    def remove(self, event: JEEventCode | JEKeyCode | JEMouseCode) -> None: ...
    def clear(self) -> None: ...
    def has(self, event: JEEventCode | JEKeyCode | JEMouseCode) -> JEBool: ...
    def process(self, game: JEGame) -> None: ...
