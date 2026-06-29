"""
    JarEngine - Python Game Engine Wrapper (Pygame-based)

    JarEngine is a lightweight game framework built on top of Pygame
    that simplifies usage while providing higher-level abstractions for
    game development and prototyping.

    Version: jarengine-v1.0.0
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
    "PGExtern",
    "JEInternBaseClass",
    "LowClasses",
    "HighClasses",
    "FinalClasses",
    "Config",
    "Decorators",
    "JTKExternTime",
    "JTKExternConsole",
    "JTKExternAction",
    "JTKExternError"
]

import pygame as PGExtern
import jarbin_toolkit_time as JTKExternTime
import jarbin_toolkit_console as JTKExternConsole
import jarbin_toolkit_action as JTKExternAction
import jarbin_toolkit_error as JTKExternError

from sources.interns.base_classe import JEInternBaseClass
import sources.interns.decorators as Decorators
import sources.interns.low_classes as LowClasses
import sources.interns.high_classes as HighClasses
import sources.interns.final_classes as FinalClasses
import sources.interns.config as Config
