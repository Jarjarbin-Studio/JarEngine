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
JarEngine Entity module.

Provides the entity system and built-in components for creating,
customizing, and managing game objects.
"""

from __future__ import annotations

# Public API exports
from .entity import JEEntity

# Submodules
from . import components_physics as Physics
from . import components_graphics as Graphics
from . import components_transforms as Transforms
from . import components_audios as Audios
from . import components_others as Others

__all__: list[str] = [
    'JEEntity',
    'Physics',
    'Graphics',
    'Transforms',
    'Audios',
    'Others'
]
