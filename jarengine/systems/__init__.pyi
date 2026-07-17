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
JarEngine utility Systems module.

Provides core reusable systems such as vectors, colors,
containers, immutable objects, versions, and data helpers.
"""

from __future__ import annotations

# Public API exports
from .transform import JETransform
from .vector import JEVector2D, JEVector3D
from .color import JEColor
from .bool import JEBool
from .container import JEContainer
from .immutable import JEImmutable
from .version import JEVersion

__all__: list[str] = [
    'JETransform',
    'JEVector2D',
    'JEVector3D',
    'JEColor',
    'JEBool',
    'JEContainer',
    'JEImmutable',
    'JEVersion'
]
