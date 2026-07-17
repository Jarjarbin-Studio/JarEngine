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

from __future__ import annotations

from jarengine.entity.entity import JEEntity
import jarengine.entity.components_audios as Audios
import jarengine.entity.components_physics as Physics
import jarengine.entity.components_graphics as Graphics
import jarengine.entity.components_transforms as Transforms
import jarengine.entity.components_others as Others

__all__ = [
    'JEEntity',
    'Audios',
    'Physics',
    'Graphics',
    'Transforms',
    'Others'
]
