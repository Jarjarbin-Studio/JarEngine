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
    "JEInternPyGame",
    "JEInternBaseClasses",
    "JEInternClasses",
    "JTKInternTime",
    "JTKInternConsole",
    "JTKInternAction",
    "JTKInternError",
    "JEInternLog",
    "JEInternConfig"
]

import pygame as JEInternPyGame
import jarbin_toolkit_time as JTKInternTime
import jarbin_toolkit_console as JTKInternConsole
import jarbin_toolkit_action as JTKInternAction
import jarbin_toolkit_error as JTKInternError

import sources.systems.base_classes as JEInternBaseClasses
import sources.systems.classes as JEInternClasses
import sources.systems.log as JEInternLog
import sources.systems.config as JEInternConfig
