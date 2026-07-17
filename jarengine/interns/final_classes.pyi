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

from types import NoneType

from jarengine.interns.high_classes import JEInternEntityComponent
from jarengine.interns.base_classe import JEInternBaseClass
from jarengine.resources.texture import JETexture
from jarengine.resources.font import JEFont
from jarengine.resources.music import JEMusic
from jarengine.resources.sound import JESound
from jarengine.interns.low_classes import JEInternGraphic
from jarengine.systems.container import JEContainer
from jarengine.entity.entity import JEEntity
from jarengine.systems.vector import JEVector2D


class JEInternEmptyComponent(JEInternEntityComponent):
    def __init__(self, owner: JEEntity):
        """
            JEInternEmptyComponent

            Parameters:
                owner (JEEntity): Entity
        """
        ...
    def __call__(self) -> NoneType:
        """
            None return for the entity checking (not included in any other component)
        """
        ...
    def __bool__(self) -> bool:
        """
            False return for the entity checking (not included in any other component)
        """
        ...
    def copy(self, new_owner: JEEntity) -> JEInternEmptyComponent:
        """
            Copy the empty component to a new entity

            Returns:
                JEInternEmptyComponent: New entity
        """
        ...

class JEInternResources(JEInternBaseClass):
    def __init__(self):
        """
            JEInternResources
        """
        ...
    @property
    def texture(self) -> JEContainer[JETexture]:
        """
            Get textures storage

            Returns:
                JEContainer[JETexture]: Texture resources
        """
        ...
    @property
    def animations(self) -> JEContainer[JEInternGraphic]:
        """
            Get animations storage

            Returns:
                JEContainer[JEInternGraphic]: Animation resources (not implemented)
        """
        ...
    @property
    def font(self) -> JEContainer[JEFont]:
        """
            Get fonts storage

            Returns:
                JEContainer[JEFont]: Font resources
        """
        ...
    @property
    def music(self) -> JEContainer[JEMusic]:
        """
            Get musics storage

            Returns:
                JEContainer[JEMusic]: Music resources
        """
        ...
    @property
    def sound(self) -> JEContainer[JESound]:
        """
            Get sounds storage

            Returns:
                JEContainer[JESound]: Sound resources
        """
        ...

class JEInternWindowSettings(JEInternBaseClass):
    def __init__(self, size: JEVector2D, flags: int,fps: int, depth: int, display: int, vsync: int, title: str):
        """
            JEInternWindowSettings

            Parameters:
                size (JEVector2D): Size
                flags (int): Flags (Not handled by JarEngine)
                fps (int): FPS
                depth (int): Depth (Not handled by JarEngine)
                display (int): Display (Not handled by JarEngine)
                vsync (int): Vsync (Not handled by JarEngine)
                title (str): Title
        """
        ...
    @property
    def size(self) -> JEVector2D:
        """
            Get the size setting

            Returns:
                JEVector2D: Size
        """
        ...
    @size.setter
    def size(self, size: JEVector2D):
        """
            Set the size setting

            Parameters:
                size (JEVector2D): New size
        """
        ...
    @property
    def flags(self) -> int:
        """
            Get the flag setting

            Returns:
                int: Flag
        """
        ...
    @property
    def fps(self) -> int:
        """
            Get the FPS setting

            Returns:
                int: FPS
        """
        ...
    @fps.setter
    def fps(self, fps: int):
        """
            Set the FPS setting

            Parameters:
                fps (int): New FPS
        """
        ...
    @property
    def depth(self) -> int:
        """
            Get the depth setting

            Returns:
                int: Depth
        """
        ...
    @property
    def display(self) -> int:
        """
            Get the display setting

            Returns:
                int: Display
        """
        ...
    @property
    def vsync(self) -> int:
        """
            Get the vsync setting

            Returns:
                int: Vsync
        """
        ...
    @property
    def title(self) -> str:
        """
            Get the title setting

            Returns:
                str: Title
        """
        ...
    @title.setter
    def title(self, title: str):
        """
            Set the title setting

            Parameters:
                title (str): New title
        """
        ...
