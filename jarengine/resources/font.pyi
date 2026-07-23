# =============================================================================
# JarEngine - Python Game Engine Wrapper (Pygame-based)
# =============================================================================
#
# JarEngine is a lightweight game framework built on top of Pygame
# that simplifies usage while providing higher-level abstractions for
# game development and prototyping.
#
# =============================================================================
# Version: jarengine-v1.10
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

from jarengine.interns.low_classes import JEInternResource
from jarengine.interns.high_classes import JEInternOwnership
from jarengine.interns import PGExtern

class JEFont(JEInternResource, JEInternOwnership):
    def __init__(self, name: str, path: str, size: int):
        """
            JEFont

            Parameters:
                name (str): Font name
                path (str): Font path
        """
        ...
    @property
    def font(self) -> PGExtern.font.Font:
        """
            Get PyGame font

            Returns:
                PGExtern.font.Font: Font
        """
        ...
    @property
    def size(self) -> int:
        """
            Get font size

            Returns:
                int: Size
        """
        ...
