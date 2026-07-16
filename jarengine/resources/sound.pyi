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

from jarengine.interns.low_classes import JEInternResource
from jarengine.interns.high_classes import JEInternOwnership
from jarengine.interns import PGExtern

class JESound(JEInternResource, JEInternOwnership):
    def __init__(self, name: str, path: str):
        """
            JESound

            Parameters:
                name (str): Sound name
                path (str): Sound path
        """
        ...
    @property
    def sound(self) -> PGExtern.mixer.Sound:
        """
            Get PyGame sound

            Returns:
                PGExtern.mixer.Sound: Sound
        """
        ...
