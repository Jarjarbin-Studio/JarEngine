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

from typing import Optional, Callable

from jarengine import JETrue, JEFalse
from jarengine.widgets.widget import JEWidget
from jarengine.systems.vector import JEVector2D
from jarengine.systems.bool import JEBool
from jarengine.systems.color import JEColor
from jarengine.resources.texture import JETexture

class JEButton(JEWidget):
    def __init__(self, *, color: JEColor | tuple[int, int, int] | tuple[int, int, int, int] = JEColor(100, 100, 100, 255), outline_color: Optional[JEColor | tuple[int, int, int] | tuple[int, int, int, int]] = None, outline_size: Optional[int] = None, name = "JEButton", position: JEVector2D | tuple[float, float] = JEVector2D(0, 0), size: JEVector2D | tuple[float, float] = JEVector2D(0, 0), rotation: float = 0.0, layer: int = 0, visibility: JEBool = JETrue):
        """
            JEButton

            Parameters:
                color (JEColor | tuple[int, int, int] | tuple[int, int, int, int]) = JEColor(100, 100, 100, 255): color
                outline_color (Optional[JEColor | tuple[int, int, int] | tuple[int, int, int, int]]) = None: outline color
                outline_size  (Optional[int]) = None: outline size
                position (JEVector2D | tuple[float, float]) = (0, 0): position
                size (JEVector2D | tuple[float, float]) = (0, 0): size
                name (str) = "JEButton": name
                rotation (float) = 0.0: rotation
                layer (int) = 0: layer
                visibility (JEBool) = JETrue: visibility
        """
        ...
    def set_callback(self, callback: Callable[[], None]):
        """
            Set the functino to be called when button clicked
            
            Parameters:
                callback (Callable[[], None]): callback function
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
    def set_outline_color(self, color: JEColor | tuple[int, int, int] | tuple[int, int, int, int]):
        """
            Outline component required. Set outline color.

            Parameters:
                color (JEColor | tuple[int, int, int] | tuple[int, int, int, int]): New outline color
        """
        ...
    def update_outline_color(self, *, r: int = 0, g: int = 0, b: int = 0, a: int = 0):
        """
            Outline component required. Update outline color.

            Parameters:
                r (int) = 0: Outline color r to add to the current outline color r
                g (int) = 0: Outline color g to add to the current outline color g
                b (int) = 0: Outline color b to add to the current outline color b
                a (int) = 0: Outline color a to add to the current outline color a
        """
        ...
    def get_outline_color(self) -> JEColor:
        """
            Outline component required. Get outline color.

            Returns:
                JEColor: Outline color
        """
        ...
    def set_outline_size(self, size: int):
        """
            Outline component required. Set outline size.

            Parameters:
                size (int): New size
        """
        ...
    def update_outline_size(self, *, s: int = 0):
        """
            Outline component required. Update outline size.

            Parameters:
                s (int) = 0: Outline size to add to the current size
        """
        ...
    def get_outline_size(self) -> int:
        """
            Outline component required. Get outline size.

            Returns:
                int: Outline size
        """
        ...

class JEImageButton(JEWidget):
    def __init__(self, texture: JETexture, *, flip: tuple[JEBool, JEBool] = (JEFalse, JEFalse), color: Optional[JEColor | tuple[int, int, int] | tuple[int, int, int, int]] = None, outline_color: Optional[JEColor | tuple[int, int, int] | tuple[int, int, int, int]] = None, outline_size: Optional[int] = None, name="JEImageButton", position: JEVector2D | tuple[float, float] = JEVector2D(0, 0), size: JEVector2D | tuple[float, float] = JEVector2D(0, 0), rotation: float = 0.0, layer: int = 0, visibility: JEBool = JETrue):
        """
            JEImageButton

            Parameters:
                texture (JETexture): texture
                flip (tuple[JEBool, JEBool]) = (JEFalse, JEFalse): flip
                color (Optional[JEColor | tuple[int, int, int] | tuple[int, int, int, int]]) = None: color
                outline_color (Optional[JEColor | tuple[int, int, int] | tuple[int, int, int, int]]) = None: outline color
                outline_size  (Optional[int]) = None: outline size
                position (JEVector2D | tuple[float, float]) = (0, 0): position
                size (JEVector2D | tuple[float, float]) = (0, 0): size
                name (str) = "JEImageButton": name
                rotation (float) = 0.0: rotation
                layer (int) = 0: layer
                visibility (JEBool) = JETrue: visibility
        """
        ...
    def set_callback(self, callback: Callable[[], None]):
        """
            Set the functino to be called when button clicked

            Parameters:
                callback (Callable[[], None]): callback function
        """
        ...
    def set_outline_color(self, color: JEColor | tuple[int, int, int] | tuple[int, int, int, int]):
        """
            Outline component required. Set outline color.

            Parameters:
                color (JEColor | tuple[int, int, int] | tuple[int, int, int, int]): New outline color
        """
        ...
    def update_outline_color(self, *, r: int = 0, g: int = 0, b: int = 0, a: int = 0):
        """
            Outline component required. Update outline color.

            Parameters:
                r (int) = 0: Outline color r to add to the current outline color r
                g (int) = 0: Outline color g to add to the current outline color g
                b (int) = 0: Outline color b to add to the current outline color b
                a (int) = 0: Outline color a to add to the current outline color a
        """
        ...
    def get_outline_color(self) -> JEColor:
        """
            Outline component required. Get outline color.

            Returns:
                JEColor: Outline color
        """
        ...
    def set_outline_size(self, size: int):
        """
            Outline component required. Set outline size.

            Parameters:
                size (int): New size
        """
        ...
    def update_outline_size(self, *, s: int = 0):
        """
            Outline component required. Update outline size.

            Parameters:
                s (int) = 0: Outline size to add to the current size
        """
        ...
    def get_outline_size(self) -> int:
        """
            Outline component required. Get outline size.

            Returns:
                int: Outline size
        """
        ...
    def set_flip(self, flip: tuple[JEBool, JEBool]):
        """
            Flip component required. Set flip.

            Parameters:
                flip (tuple[JEBool, JEBool]): New flip
        """
        ...
    def get_flip(self) -> tuple[JEBool, JEBool]:
        """
            Flip component required. Get flip.

            Returns:
                tuple[JEBool, JEBool]: Flip
        """
        ...
    def set_texture(self, texture: JETexture):
        """
            Texture component required. Set texture.

            Parameters:
                texture (JETexture): new texture ressource
        """
        ...
    def get_texture(self) -> JETexture:
        """
            Texture component required. Get texture.

            Returns:
                JETexture: Texture resource
        """
        ...

class JECheckbox(JEWidget):
    def __init__(self, *, checked: JEBool = JEFalse, color: JEColor | tuple[int, int, int] | tuple[int, int, int, int] = JEColor(100, 100, 100, 255), checked_color: JEColor | tuple[int, int, int] | tuple[int, int, int, int] = JEColor(100, 255, 100, 255), outline_color: Optional[JEColor | tuple[int, int, int] | tuple[int, int, int, int]] = None, outline_size: Optional[int] = None, name="JECheckbox", position: JEVector2D | tuple[float, float] = JEVector2D(0, 0), size: JEVector2D | tuple[float, float] = JEVector2D(0, 0), rotation: float = 0.0, layer: int = 0, visibility: JEBool = JETrue):
        """
            JECheckbox

            Parameters:
                checked (JEBool): checked
                color (JEColor | tuple[int, int, int] | tuple[int, int, int, int]) = JEColor(100, 100, 100, 255): color
                checked_color (JEColor | tuple[int, int, int] | tuple[int, int, int, int]) = JEColor(100, 255, 100, 255): checked color
                outline_color (Optional[JEColor | tuple[int, int, int] | tuple[int, int, int, int]]) = None: outline color
                outline_size  (Optional[int]) = None: outline size
                position (JEVector2D | tuple[float, float]) = (0, 0): position
                size (JEVector2D | tuple[float, float]) = (0, 0): size
                name (str) = "JECheckbox": name
                rotation (float) = 0.0: rotation
                layer (int) = 0: layer
                visibility (JEBool) = JETrue: visibility
        """
        ...
    def set_callback(self, callback: Callable[[JEBool], None]):
        """
            Set the functino to be called when button clicked

            Parameters:
                callback (Callable[[], None]): callback function
        """
        ...
    def set_checked(self, checked: JEBool):
        """
            Set checked status

            Parameters:
                checked (JEBool): checked
        """
        ...
    def is_checked(self) -> JEBool:
        """
            Check status

            Returns:
                JEBool: checked
        """
        ...
    def toggle(self):
        """
            Toggle checked status
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
    def set_outline_color(self, color: JEColor | tuple[int, int, int] | tuple[int, int, int, int]):
        """
            Outline component required. Set outline color.

            Parameters:
                color (JEColor | tuple[int, int, int] | tuple[int, int, int, int]): New outline color
        """
        ...
    def update_outline_color(self, *, r: int = 0, g: int = 0, b: int = 0, a: int = 0):
        """
            Outline component required. Update outline color.

            Parameters:
                r (int) = 0: Outline color r to add to the current outline color r
                g (int) = 0: Outline color g to add to the current outline color g
                b (int) = 0: Outline color b to add to the current outline color b
                a (int) = 0: Outline color a to add to the current outline color a
        """
        ...
    def get_outline_color(self) -> JEColor:
        """
            Outline component required. Get outline color.

            Returns:
                JEColor: Outline color
        """
        ...
    def set_outline_size(self, size: int):
        """
            Outline component required. Set outline size.

            Parameters:
                size (int): New size
        """
        ...
    def update_outline_size(self, *, s: int = 0):
        """
            Outline component required. Update outline size.

            Parameters:
                s (int) = 0: Outline size to add to the current size
        """
        ...
    def get_outline_size(self) -> int:
        """
            Outline component required. Get outline size.

            Returns:
                int: Outline size
        """
        ...
