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

from __future__ import annotations

from typing import Any

from jarengine.interns.base_classe import JEInternBaseClass

class JEBool(JEInternBaseClass):
    def __init__(self, value: Any):
        """
            JEBool

            Parameters:
                value (Any): Value to be represented
        """
        ...
    def __bool__(self) -> bool:
        """
            Get the actual intern boolean (used in conditions)

            Returns:
                bool: Internal boolean
        """
        ...
    def __int__(self) -> int:
        """
            Get int representation of the boolean

            Returns:
                int: Int
        """
        ...
    def __call__(self) -> JEBool:
        """
            Revers the boolean (False <-> True)

            Returns:
                JEBool: Reversed boolean
        """
        ...
    @property
    def b(self) -> bool:
        """
            Get the actual intern boolean (used for dump and debug)

            Returns:
                bool: Internal boolean
        """
        ...
