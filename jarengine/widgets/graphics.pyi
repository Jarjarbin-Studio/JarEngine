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


class JESprite(JEWidget):
    def __init__(self, texture: JETexture, *, flip: tuple[JEBool, JEBool] = (JEFalse, JEFalse), name: str = "JESprite", position: JEVector2D = JEVector2D(0, 0), size: JEVector2D = JEVector2D(0, 0), rotation: float = 0.0, layer: int = 0, visibility: JEBool = JETrue):
        """
            JESprite

            Parameters:
                texture (JETexture): texture of the widget
                flip (tuple[JEBool, JEBool]): flip of the widget
                name (str) = "JESprite": name of the widget
                position (JEVector2D) = (0, 0): position of the widget
                size (JEVector2D) = (0, 0): size of the widget
                rotation (float) = 0.0: rotation of the widget
                layer (int) = 0: layer of the widget
                visibility (JEBool) = JETrue: visibility of the widget
        """
        ...
    def set_texture(self, texture: JETexture):
        """
            Set texture.

            Parameters:
                texture (JETexture): new texture ressource
        """
        ...
    def get_texture(self) -> JETexture:
        """
            Get texture.

            Returns:
                JETexture: Texture resource
        """
        ...
    def set_flip(self, flip: tuple[JEBool, JEBool]):
        """
            Set flip.

            Parameters:
                flip (tuple[JEBool, JEBool]): New flip
        """
        ...
    def get_flip(self) -> tuple[JEBool, JEBool]:
        """
            Get flip.

            Returns:
                tuple[JEBool, JEBool]: Flip
        """
        ...

class JEText(JEWidget):
    def __init__(self, text: str, font: JEFont, *, color: Optional[JEColor | tuple[int, int, int] | tuple[int, int, int, int]] = None, flip: tuple[JEBool, JEBool] = (JEFalse, JEFalse), name: str = "JESprite", position: JEVector2D = JEVector2D(0, 0), size: JEVector2D = JEVector2D(0, 0), rotation: float = 0.0, layer: int = 0, visibility: JEBool = JETrue):
        """
            JESprite

            Parameters:
                text (str): text of the widget
                font (JEFont): font of the text
                color (JEColor): color of the text
                flip (tuple[JEBool, JEBool]): flip of the widget
                name (str) = "JESprite": name of the widget
                position (JEVector2D) = (0, 0): position of the widget
                size (JEVector2D) = (0, 0): size of the widget
                rotation (float) = 0.0: rotation of the widget
                layer (int) = 0: layer of the widget
                visibility (JEBool) = JETrue: visibility of the widget
        """
        ...
    def set_text(self, text: str):
        """
            Text component required. Set text.

            Parameters:
                text (JEFont): New text
        """
        ...
    def get_text(self) -> str:
        """
            Text component required. Get text.

            Returns:
                str: Text
        """
        ...
    def set_font(self, font: JEFont):
        """
            Font component required. Set font.

            Parameters:
                font (JEFont): New font ressource
        """
        ...
    def get_font(self) -> JEFont:
        """
            Font component required. Get font.

            Returns:
                JEFont: Font resource
        """
        ...
    def set_flip(self, flip: tuple[JEBool, JEBool]):
        """
            Set flip.

            Parameters:
                flip (tuple[JEBool, JEBool]): New flip
        """
        ...
    def get_flip(self) -> tuple[JEBool, JEBool]:
        """
            Get flip.

            Returns:
                tuple[JEBool, JEBool]: Flip
        """
        ...
    def set_color(self, color: JEColor | tuple[int, int, int] | tuple[int, int, int, int]):
        """
            Color component required. Set color.

            Parameters:
                color (JEColor | tuple[int, int, int] | tuple[int, int, int, int]): New color
        """
        ...
    def update_color(self, *, r: int = 0, g: int = 0, b: int = 0, a: int = 0):
        """
            Color component required. Update color.

            Parameters:
                r (int) = 0: Color r to add to the current color r
                g (int) = 0: Color g to add to the current color g
                b (int) = 0: Color b to add to the current color b
                a (int) = 0: Color a to add to the current color a
        """
        ...
    def get_color(self) -> JEColor:
        """
            Color component required. Get color.

            Returns:
                JEColor: Color
        """
        ...
