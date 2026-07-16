# =============================================================================
# JarEngine - Python Game Engine Wrapper (Pygame-based)
# =============================================================================
#
# JarEngine is a lightweight game framework built on top of Pygame
# that simplifies usage while providing higher-level abstractions for
# game development and prototyping.
#
# =============================================================================
# Version: jarengine-v1.7
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
JarEngine game module.

Provides the main game runtime components, including game control,
window management, live input handling, and game-related systems.
"""

from __future__ import annotations

# Public API exports
from .window import JEWindow
from .game import JEGame
from .input import JEInput

# Submodules
from . import systems as Systems

__all__: list[str] = [
    'JEGame',
    'JEWindow',
    'JEInput',
    'Systems'
]
