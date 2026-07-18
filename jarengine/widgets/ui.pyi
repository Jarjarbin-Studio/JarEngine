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

from typing import Optional

from jarengine import JETrue, JEFalse
from jarengine.widgets.widget import JEWidget
from jarengine.systems.vector import JEVector2D
from jarengine.resources.texture import JETexture
from jarengine.systems.bool import JEBool
from jarengine.resources.font import JEFont
from jarengine.systems.color import JEColor
from jarengine.interns import PGExtern

class JEButton(JEWidget):
    def __init__(self, *, name: str = "JEButton", position: JEVector2D | tuple[float, float] = JEVector2D(0, 0), size: JEVector2D | tuple[float, float] = JEVector2D(0, 0), rotation: float = 0.0, layer: int = 0, visibility: JEBool = JETrue):
        """
            JESprite

            Parameters:
                texture (JETexture): texture of the widget
                flip (tuple[JEBool, JEBool]): flip of the widget
                name (str) = "JESprite": name of the widget
                position (JEVector2D | tuple[float, float]) = (0, 0): position of the widget
                size (JEVector2D | tuple[float, float]) = (0, 0): size of the widget
                rotation (float) = 0.0: rotation of the widget
                layer (int) = 0: layer of the widget
                visibility (JEBool) = JETrue: visibility of the widget
        """
        ...
