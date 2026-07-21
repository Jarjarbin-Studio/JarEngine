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

from jarengine.interns.base_classe import JEInternBaseClass
from jarengine.interns import PGExtern
from jarengine.interns.final_classes import JEInternWindowSettings
from jarengine.systems.color import JEColor
from jarengine.systems.vector import JEVector2D

class JEWindow(JEInternBaseClass):
    def __init__(self):
        """
            JEWindow
        """
        ...
    @property
    def render_surface(self) -> PGExtern.Surface:
        """
            Get PyGame screen (rendering)

            Returns:
                PGExtern.Surface: PyGame screen
        """
        ...
    @property
    def screen(self) -> PGExtern.Surface:
        """
            Get PyGame screen (window)

            Returns:
                PGExtern.Surface: PyGame screen
        """
        ...
    @property
    def settings(self) -> JEInternWindowSettings:
        """
            Get window's settings

            Returns:
                JEInternWindowSettings: window's settings
        """
        ...
    def fill(self, color: JEColor | tuple[int, int, int] | tuple[int, int, int, int]):
        """
            Fill the window with a given color.

            Parameters:
                color (JEColor | tuple[int, int, int] | tuple[int, int, int, int]): Color to fill
        """
        ...
    def clear(self):
        """
            Clear the rendering surface
        """
        ...
    def blit(self, source: PGExtern.Surface, dest: JEVector2D | tuple[int, int]):
        """
            Copy a PyGame surface to the window
            
            Parameters:
                source (PGExtern.Surface): PyGame surface to copy
                dest (JEVector2D | tuple[int, int]): Destination position
        """
        ...
    def display(self):
        """
            Display the rendering surface in the window
        """
        ...
