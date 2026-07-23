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

from jarengine.interns.base_classe import JEInternBaseClass

class JEClock(JEInternBaseClass):
    def __init__(self, fps: int = 60):
        """
            JEClock
            
            Parameters:
                fps (int) = 60: Target fps
        """
        ...
    def update(self):
        """
            Update clock data
        """
        ...
    @property
    def dt(self) -> float:
        """
            Get time

            Returns:
                float: Current dt
        """
        ...
    @property
    def target_fps(self) -> int:
        """
            Get target fps

            Returns:
                int: Target fps
        """
        ...
    @target_fps.setter
    def target_fps(self, value: int):
        """
            Set target fps

            Parameters:
                value (int): New target fps
        """
        ...
    @property
    def fps(self) -> float:
        """
            Get current fps

            Returns:
                float: Current fps
        """
        ...
    def __float__(self) -> float:
        """
            Get time

            Returns:
                float: Current dt
        """
        ...
