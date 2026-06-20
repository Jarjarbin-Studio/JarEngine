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

__all__ = [
    "JEGame",
    "JEWindow",
    "JEEventManager",
    "JEEvent",
    "JEKeyboard",
    "JEMouse"
]

from sources.games.window import JEWindow
from sources.games.game import JEGame
import sources.games.events_manager as JEEventManager
import sources.games.event as JEEvent
import sources.games.keyboard as JEKeyboard
import sources.games.mouse as JEMouse
