# =============================================================================
# JarEngine - Python Game Engine Wrapper (Pygame-based)
# =============================================================================
#
# JarEngine is a lightweight game framework built on top of Pygame
# that simplifies usage while providing higher-level abstractions for
# game development and prototyping.
#
# =============================================================================
# Version: jarengine-v1.8
# Author: Jarjarbin Studio
# Licence: GPL v3
# =============================================================================
#
# This engine is inspired by Pygame, modern game engine design patterns,
# and directly influenced by the architecture of NewCSFML.
#
# It is designed for educational purposes and small-to-medium game projects.
#
# It provides structured systems such as entity management, scene handling,
# render abstraction, and advanced modules like particle systems.
#
# =============================================================================
# WARNING:
# =============================================================================
#
# This is NOT Pygame itself.
# It is a custom abstraction layer built on top of Pygame.
#
# =============================================================================

"""
JarEngine internal module.

Provides internal engine classes, configurations, decorators,
and external integrations required by JarEngine.

Warning:
    This module is intended for engine development and advanced usage.
    Users should avoid directly modifying or relying on its internals.
"""

from __future__ import annotations

# Public API exports
from .base_classe import JEInternBaseClass

# Submodules
import pygame as PGExtern
import jarbin_toolkit_time as JTKExternTime
import jarbin_toolkit_console as JTKExternConsole
import jarbin_toolkit_error as JTKExternError
from . import decorators as Decorators
from . import low_classes as LowClasses
from . import high_classes as HighClasses
from . import final_classes as FinalClasses
from . import config as Config


__all__: list[str] = [
    "PGExtern",
    "JEInternBaseClass",
    "LowClasses",
    "HighClasses",
    "FinalClasses",
    "Config",
    "Decorators",
    "JTKExternTime",
    "JTKExternConsole",
    "JTKExternError"
]
