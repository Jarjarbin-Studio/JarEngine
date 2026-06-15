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

import jarbin_toolkit_error as JTKInternError

def JEIntern_Fatal(err: str, msg: str) -> None:
    print(JTKInternError.BaseError(msg, error=f"Fatal({err})"))
    exit(84)

def JEIntern_Error(err: str, msg: str) -> None:
    print(JTKInternError.BaseError(msg, error=f"Error({err})"))
    exit(1)

def JEIntern_Warning(err: str, msg: str) -> None:
    print(JTKInternError.BaseError(msg, error=f"Warning({err})"))
