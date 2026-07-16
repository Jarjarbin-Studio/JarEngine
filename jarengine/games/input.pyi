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
from jarengine.events.keyboard import JEKeyCode
from jarengine.events.mouse import JEMouseCode
from jarengine.systems.vector import JEVector2D

class JEInput(JEInternBaseClass):
    def __init__(self):
        """
            JEInput
        """
        ...
    def update(self):
        """
            Update keyboard and mouse
        """
        ...
    def is_key_down(self, key: JEKeyCode) -> bool:
        """
            Check if given key is down

            Parameters:
                key (JEKeyCode): Key code

            Returns:
                bool: True if key down, False otherwise
        """
        ...
    def is_mouse_down(self, button: JEMouseCode) -> bool:
        """
            Check if given mouse button is down

            Parameters:
                button (JEMouseCode): Mouse code

            Returns:
                bool: True if mouse button down, False otherwise
        """
        ...
    def mouse_pos(self) -> JEVector2D:
        """
            Get mouse position

            Returns:
                JEVector2D: Mouse position
        """
        ...
    def __call__(self, code: JEKeyCode | JEMouseCode) -> bool:
        """
            Automatically dispatch between 'is_key_down' and 'is_mouse_down'
            
            Parameters:
                code (JEKeyCode | JEMouseCode) Key or mouse button
            
            Returns:
                bool: True if key or mouse down, False otherwise
        """
        ...
