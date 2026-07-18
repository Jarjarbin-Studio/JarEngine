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

class JESprite(JEWidget):
    def __init__(self, texture: JETexture, *, flip: tuple[JEBool, JEBool] = (JEFalse, JEFalse), name: str = "JESprite", position: JEVector2D | tuple[float, float] = JEVector2D(0, 0), size: JEVector2D | tuple[float, float] = JEVector2D(0, 0), rotation: float = 0.0, layer: int = 0, visibility: JEBool = JETrue):
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
    def __init__(self, text: str, font: JEFont, *, color: Optional[JEColor | tuple[int, int, int] | tuple[int, int, int, int]] = None, flip: tuple[JEBool, JEBool] = (JEFalse, JEFalse), name: str = "JEText", position: JEVector2D | tuple[float, float] = JEVector2D(0, 0), size: JEVector2D | tuple[float, float] = JEVector2D(0, 0), rotation: float = 0.0, layer: int = 0, visibility: JEBool = JETrue):
        """
            JEText

            Parameters:
                text (str): text of the widget
                font (JEFont): font of the text
                color (Optional[JEColor | tuple[int, int, int] | tuple[int, int, int, int]]): color of the text
                flip (tuple[JEBool, JEBool]): flip of the widget
                name (str) = "JEText": name of the widget
                position (JEVector2D | tuple[float, float]) = (0, 0): position of the widget
                size (JEVector2D | tuple[float, float]) = (0, 0): size of the widget
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

class JERectangle(JEWidget):
    def __init__(self, size: JEVector2D | tuple[float, float], *, color: Optional[JEColor | tuple[int, int, int] | tuple[int, int, int, int]] = None, outline_color: Optional[JEColor | tuple[int, int, int] | tuple[int, int, int, int]] = None, outline_size: Optional[int] = 0, name: str = "JERectangle", position: JEVector2D | tuple[float, float] = JEVector2D(0, 0), rotation: float = 0.0, layer: int = 0, visibility: JEBool = JETrue):
        """
            JERectangle

            Parameters:
                size (JEVector2D | tuple[float, float]): size of the rectangle
                color (Optional[JEColor | tuple[int, int, int] | tuple[int, int, int, int]]): color of the rectangle
                outline_color (Optional[JEColor | tuple[int, int, int] | tuple[int, int, int, int]]): outline color of the rectangle
                outline_size  (Optional[int]): outline size
                name (str) = "JERectangle": name of the widget
                position (JEVector2D | tuple[float, float]) = (0, 0): position of the widget
                rotation (float) = 0.0: rotation of the widget
                layer (int) = 0: layer of the widget
                visibility (JEBool) = JETrue: visibility of the widget
        """
        ...
    def set_surface(self, surface: PGExtern.Surface):
        """
            Surface component required. Set surface.

            Parameters:
                surface (PGExtern.Surface): New surface
        """
        ...
    def get_surface(self) -> PGExtern.Surface:
        """
            Surface component surface. Get font.

            Returns:
                PGExtern.Surface: Surface
        """
        ...

class JECircle(JEWidget):
    def __init__(self, radius: float, *, color: Optional[JEColor | tuple[int, int, int] | tuple[int, int, int, int]] = None, outline_color: Optional[JEColor | tuple[int, int, int] | tuple[int, int, int, int]] = None, outline_size: Optional[int] = None, name: str = "JECircle", position: JEVector2D | tuple[float, float] = JEVector2D(0, 0), rotation: float = 0.0, layer: int = 0, visibility: JEBool = JETrue):
        """
            JECircle

            Parameters:
                radius (float): radius of the circle
                color (Optional[JEColor | tuple[int, int, int] | tuple[int, int, int, int]]): color of the circle
                outline_color (Optional[JEColor | tuple[int, int, int] | tuple[int, int, int, int]]): outline color of the circle
                outline_size  (Optional[int]): outline size
                name (str) = "JECircle": name of the widget
                position (JEVector2D | tuple[float, float]) = (0, 0): position of the widget
                rotation (float) = 0.0: rotation of the widget
                layer (int) = 0: layer of the widget
                visibility (JEBool) = JETrue: visibility of the widget
        """
        ...
    def set_surface(self, surface: PGExtern.Surface):
        """
            Surface component required. Set surface.

            Parameters:
                surface (PGExtern.Surface): New surface
        """
        ...
    def get_surface(self) -> PGExtern.Surface:
        """
            Surface component surface. Get font.

            Returns:
                PGExtern.Surface: Surface
        """
        ...

class JELine(JEWidget):
    def __init__(self, start: JEVector2D | tuple[float, float], end: JEVector2D | tuple[float, float], *, color: Optional[JEColor | tuple[int, int, int] | tuple[int, int, int, int]] = None, width: int = 1, name: str = "JELine", rotation: float = 0.0, layer: int = 0, visibility: JEBool = JETrue):
        """
            JELine

            Parameters:
                start (JEVector2D | tuple[float, float]): start of the line
                end (JEVector2D | tuple[float, float]): end of the line
                color (Optional[JEColor | tuple[int, int, int] | tuple[int, int, int, int]]): color of the line
                width (int) = 1: width of the line
                name (str) = "JELine": name of the widget
                rotation (float) = 0.0: rotation of the widget
                layer (int) = 0: layer of the widget
                visibility (JEBool) = JETrue: visibility of the widget
        """
        ...
    def set_surface(self, surface: PGExtern.Surface):
        """
            Surface component required. Set surface.

            Parameters:
                surface (PGExtern.Surface): New surface
        """
        ...
    def get_surface(self) -> PGExtern.Surface:
        """
            Surface component surface. Get font.

            Returns:
                PGExtern.Surface: Surface
        """
        ...

class JEPolygon(JEWidget):
    def __init__(self, points: list[JEVector2D | tuple[float, float]] | tuple[JEVector2D | tuple[float, float], ...], *, color: Optional[JEColor | tuple[int, int, int] | tuple[int, int, int, int]] = None, outline_color: Optional[JEColor | tuple[int, int, int] | tuple[int, int, int, int]] = None, outline_size: Optional[int] = None, name: str = "JEPolygon", rotation: float = 0.0, layer: int = 0, visibility: JEBool = JETrue):
        """
            JEPolygon

            Parameters:
                radius (float): radius of the circle
                color (Optional[JEColor | tuple[int, int, int] | tuple[int, int, int, int]]): color of the circle
                outline_color (Optional[JEColor | tuple[int, int, int] | tuple[int, int, int, int]]): outline color of the circle
                outline_size  (Optional[int]): outline size
                name (str) = "JEPolygon": name of the widget
                position (JEVector2D | tuple[float, float]) = (0, 0): position of the widget
                rotation (float) = 0.0: rotation of the widget
                layer (int) = 0: layer of the widget
                visibility (JEBool) = JETrue: visibility of the widget
        """
        ...
    def set_surface(self, surface: PGExtern.Surface):
        """
            Surface component required. Set surface.

            Parameters:
                surface (PGExtern.Surface): New surface
        """
        ...
    def get_surface(self) -> PGExtern.Surface:
        """
            Surface component surface. Get font.

            Returns:
                PGExtern.Surface: Surface
        """
        ...
