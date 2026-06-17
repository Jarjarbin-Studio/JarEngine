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

__all__ = [
    'Audios',
    'Games',
    'Graphics',
    'Systems'
]

import sources.audios as Audios
import sources.games as Games
import sources.graphics as Graphics
import sources.systems as Systems

def init() -> tuple[int, int]:
    return Systems.JEInternPyGame.init()

def quit() -> None:
    Systems.JEInternPyGame.quit()
