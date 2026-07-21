# =============================================================================
# JarEngine - Python Game Engine Wrapper (PyGame-based)
# =============================================================================
#
# JarEngine is a lightweight game framework built on top of PyGame
# that simplifies usage while providing higher-level abstractions for
# game development and prototyping.
#
# =============================================================================
# Version: jarengine-v1.8
# Author: Jarjarbin Studio
# Licence: GPL v3
# =============================================================================
#
# This engine is inspired by PyGame, modern game engine design patterns,
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

from jarengine.systems.transform import JETransform
from jarengine.systems.vector import JEVector2D, JEVector3D
from jarengine.systems.color import JEColor
from jarengine.systems.bool import JEBool
from jarengine.systems.container import JEContainer
from jarengine.systems.immutable import JEImmutable
from jarengine.systems.version import JEVersion, JECompatibility

__all__ = [
    'JETransform',
    'JEVector2D',
    'JEVector3D',
    'JEColor',
    'JEBool',
    'JEContainer',
    'JEImmutable',
    'JEVersion',
    'JECompatibility'
]
