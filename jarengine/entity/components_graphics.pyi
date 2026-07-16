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

from jarengine.interns.high_classes import JEInternEntityComponent
from jarengine.resources.font import JEFont
from jarengine.entity.entity import JEEntity
from jarengine.resources.texture import JETexture
from jarengine.systems.color import JEColor
from jarengine.systems.bool import JEBool

class JEFontComponent(JEInternEntityComponent):
    def __init__(self, owner: JEEntity, font: JEFont):
        """
            JEFontComponent

            Parameters:
                owner (JEEntity): owner of the component
                font (JESound): font resource
        """
        ...
    @property
    def font(self) -> JEFont: ...
    @font.setter
    def font(self, font: JEFont): ...
    def __call__(self) -> JEFont: ...
    def copy(self, new_owner: JEEntity) -> JEFontComponent: ...

class JETextComponent(JEInternEntityComponent):
    def __init__(self, owner: JEEntity, text: str):
        """
            JETextComponent

            Parameters:
                owner (JEEntity): owner of the component
                text (str): text
        """
        ...
    @property
    def text(self) -> str: ...
    @text.setter
    def text(self, text: str): ...
    def __call__(self) -> str: ...
    def copy(self, new_owner: JEEntity) -> JETextComponent: ...

class JETextureComponent(JEInternEntityComponent):
    def __init__(self, owner: JEEntity, texture: JETexture):
        """
            JETextureComponent

            Parameters:
                owner (JEEntity): owner of the component
                texture (JETexture): texture resource
        """
        ...
    @property
    def texture(self) -> JETexture: ...
    @texture.setter
    def texture(self, texture: JETexture): ...
    def __call__(self) -> JETexture: ...
    def copy(self, new_owner: JEEntity) -> JETextureComponent: ...

class JEColorComponent(JEInternEntityComponent):
    def __init__(self, owner: JEEntity, color: JEColor | tuple[int, int, int] | tuple[int, int, int, int]):
        """
            JEColorComponent

            Parameters:
                owner (JEEntity): owner of the component
                color (JEColor | tuple[int, int, int] | tuple[int, int, int, int]): color (RGB or RGBA chanel)
        """
        ...
    @property
    def color(self) -> JEColor: ...
    @color.setter
    def color(self, color: JEColor | tuple[int, int, int] | tuple[int, int, int, int]): ...
    def __call__(self) -> JEColor: ...
    def copy(self, new_owner: JEEntity) -> JEColorComponent: ...

class JEOutlineComponent(JEInternEntityComponent):
    def __init__(self, owner: JEEntity, color: JEColor | tuple[int, int, int] | tuple[int, int, int, int], size: int):
        """
            JEOutlineComponent

            Parameters:
                owner (JEEntity): owner of the component
                color (JEColor | tuple[int, int, int] | tuple[int, int, int, int]): outline color (RGB or RGBA chanel)
                size (int): size of the outline
        """
        ...
    @property
    def color(self) -> JEColor: ...
    @color.setter
    def color(self, color: JEColor | tuple[int, int, int] | tuple[int, int, int, int]): ...
    @property
    def size(self) -> int: ...
    @size.setter
    def size(self, size: int): ...
    def __call__(self) -> tuple[JEColor, int]: ...
    def copy(self, new_owner: JEEntity) -> JEOutlineComponent: ...

class JEVisibilityComponent(JEInternEntityComponent):
    def __init__(self, owner: JEEntity, visibility: JEBool):
        """
            JEVisibilityComponent

            Parameters:
                owner (JEEntity): owner of the component
                visibility (JEBool): is the entity visible
        """
        ...
    @property
    def visibility(self: JEBool): ...
    @visibility.setter
    def visibility(self, visibility: JEBool): ...
    def __call__(self: JEBool): ...
    def copy(self, new_owner: JEEntity) -> JEVisibilityComponent: ...

class JELayerComponent(JEInternEntityComponent):
    def __init__(self, owner: JEEntity, layer: int):
        """
            JELayerComponent

            Parameters:
                owner (JEEntity): owner of the component
                layer (int): layer placement of the entity
        """
        ...
    @property
    def layer(self: int): ...
    @layer.setter
    def layer(self, layer: int): ...
    def __call__(self: int): ...
    def copy(self, new_owner: JEEntity) -> JELayerComponent: ...

class JEFlipComponent(JEInternEntityComponent):
    def __init__(self, owner: JEEntity, flip: tuple[JEBool, JEBool]):
        """
            JEFlipComponent

            Parameters:
                owner (JEEntity): owner of the component
                flip (tuple[JEBool, JEBool]): flip x and y axis of the entity
        """
        ...
    @property
    def flip(self) -> tuple[JEBool, JEBool]: ...
    @flip.setter
    def flip(self, flip: tuple[JEBool, JEBool]): ...
    def __call__(self: tuple[JEBool, JEBool]): ...
    def copy(self, new_owner: JEEntity) -> JEFlipComponent: ...
