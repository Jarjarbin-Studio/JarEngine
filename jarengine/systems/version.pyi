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

from jarengine.interns.base_classe import JEInternBaseClass
from jarengine.interns import PGExtern

class JEVersion(PGExtern.version.SoftwareVersion, JEInternBaseClass):
    def __init__(self, major: int, minor: int, patch: int):
        """
            JEVersion

            Parameters:
                major (int): Major version
                minor (int): Minor version
                patch (int): Patch version
        """
        ...
    def __str__(self) -> str:
        """
            Get string of the version

            Returns:
                str: String of the version
        """
        ...
    @property
    def major(self) -> int:
        """
            Get major version

            Returns:
                int: Major version
        """
        ...
    @property
    def minor(self) -> int:
        """
            Get minor version

            Returns:
                int: Minor version
        """
        ...
    @property
    def patch(self) -> int:
        """
            Get patch version

            Returns:
                int: Patch version
        """
        ...
