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

from jarengine.interns.low_classes import JEInternGraphicalObject
from jarengine.resources.font import JEFont
from jarengine.interns.high_classes import JEInternEntityComponent, JEInternOwnership
from jarengine.systems.container import JEContainer
from jarengine.systems.vector import JEVector2D
from jarengine.resources.texture import JETexture
from jarengine.systems.bool import JEBool
from jarengine.systems.color import JEColor
from jarengine.resources.music import JEMusic
from jarengine.resources.sound import JESound
from jarengine.interns import PGExtern

class JEEntity(JEInternGraphicalObject, JEInternOwnership):
    def __init__(self, *, name: str = "JEEntity"):
        """
            JEEntity

            Parameters:
                name (str) = "JEEntity": name of the entity
        """
        ...
    @property
    def components(self) -> JEContainer[JEInternEntityComponent]:
        """
            Get entity's components

            Returns:
                JEContainer[JEInternEntityComponent]: entity's components
        """
        ...
    def add_component(self, component: JEInternEntityComponent):
        """
            Add a component to the entity
            
            Parameters:
                component (JEInternEntityComponent): Entity component
        """
        ...
    def get(self, component: type) -> JEInternEntityComponent:
        """
            Get a component by its type
            
            Parameters:
                component (type): Type of the component
            
            Returns:
                JEInternEntityComponent: Entity's component
        """
        ...
    def copy(self) -> JEEntity:
        """
            Copy recursively (deepcopy) the entity

            Returns:
                JEEntity: New entity
        """
        ...


    ### COMPONENTS ###
    ## Graphics ##
    # Surface #
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

    # Font #
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

    # Text #
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

    # Texture #
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

    # Color #
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

    # Outline #
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

    # Visibility #
    def set_visibility(self, visibility: JEBool):
        """
            Visibility component required. Set visibility.

            Parameters:
                visibility (JEBool): New visibility
        """
        ...
    def get_visibility(self) -> JEBool:
        """
            Visibility component required. Get visibility.

            Returns:
                JEBool: Visibility
        """
        ...

    # Layer #
    def set_layer(self, layer: int):
        """
            Layer component required. Set layer.

            Parameters:
                layer (int): New layer
        """
        ...
    def update_layer(self, *, l: int = 0):
        """
            Layer component required. Update layer.

            Parameters:
                l (int) = 0: Layer to add to the current layer
        """
        ...
    def get_layer(self) -> int:
        """
            Layer component required. Get layer.

            Returns:
                int: Layer
        """
        ...

    # Flip #
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

    ## Audios ##
    # Music #
    def set_music(self, music: JEMusic):
        """
            Music component required. Set music.

            Parameters:
                music (JEFont): New music ressource
        """
        ...
    def play_music(self, loop: int = -1):
        """
            Music component required. Play music.
            -1 = infinite, n = n+1 repetition

            Parameters:
                loop (int) = -1: Loop the music
        """
        ...
    def pause_music(self):
        """
            Music component required. Pause music.
        """
        ...
    def resume_music(self):
        """
            Music component required. Resume music.
        """
        ...
    def stop_music(self):
        """
            Music component required. Stop music.
        """
        ...
    def set_music_volume(self, volume: int):
        """
            Music component required. Set volume.

            Parameters:
                volume (int): New volume
        """
        ...
    def get_music(self) -> JEMusic:
        """
            Music component required. Get music.

            Returns:
                JEMusic: Music resource
        """
        ...

    # Sound #
    def set_sound(self, sound: JESound):
        """
            Sound component required. Set sound.

            Parameters:
                sound (JESound): New sound
        """
        ...
    def play_sound(self, loop: int = -1):
        """
            Sound component required. Play sound.
            -1 = infinite, n = n+1 repetition

            Parameters:
                loop (int) = -1: Loop the sound
        """
        ...
    def stop_sound(self):
        """
            Sound component required. Stop sound.
        """
        ...
    def pause_sound(self):
        """
            Sound component required. Pause sound.
        """
        ...
    def resume_sound(self):
        """
            Sound component required. Resume sound.
        """
        ...
    def fade_sound(self, milliseconds: int):
        """
            Sound component required. Fade out sound

            Parameters:
                milliseconds (int): Duration (in milliseconds) of the fadeout
        """
        ...
    def set_sound_volume(self, volume: int):
        """
            Sound component required. Set volume.

            Parameters:
                volume (int): New volume
        """
        ...
    def get_sound(self) -> JESound:
        """
            Sound component required. Get sound.

            Returns:
                JESound: Sound resource
        """
        ...


    ## Physics ##
    # Acceleration #
    def set_acceleration(self, acceleration: JEVector2D | tuple[float, float]):
        """
            Acceleration component required. Set acceleration.

            Parameters:
                acceleration (JEVector2D | tuple[float, float]): New acceleration
        """
        ...
    def update_acceleration(self, *, x: float = 0.0, y: float = 0.0):
        """
            Acceleration component required. Update acceleration.

            Parameters:
                x (float) = 0.0: Acceleration x to add to the current acceleration x
                y (float) = 0.0: Acceleration y to add to the current acceleration y
        """
        ...
    def get_acceleration(self) -> JEVector2D:
        """
            Acceleration component required. Get acceleration.

            Returns:
                JEVector2D: Acceleration
        """
        ...

    # Mass #
    def set_mass(self, mass: float):
        """
            Mass component required. Set mass.

            Parameters:
                mass (float): New mass
        """
        ...
    def update_mass(self, *, m: float = 0.0):
        """
            Mass component required. Update mass.

            Parameters:
                m (float) = 0.0: Mass to add to the current mass
        """
        ...
    def get_mass(self) -> float:
        """
            Mass component required. Get mass.

            Returns:
                float: Mass
        """
        ...


    ## Transforms ##
    # Position #
    def set_position(self, position: JEVector2D | tuple[float, float]):
        """
            Position component required. Set position.

            Parameters:
                position (JEVector2D | tuple[float, float]): New position
        """
        ...
    def update_position(self, *, x: float = 0.0, y: float = 0.0):
        """
            Position component required. Update position.

            Parameters:
                x (float) = 0.0: Position x to add to the current position x
                y (float) = 0.0: Position y to add to the current position y
        """
        ...
    def get_position(self) -> JEVector2D:
        """
            Position component required. Get position.

            Returns:
                JEVector2D: Position
        """
        ...

    # Velocity #
    def set_velocity(self, velocity: JEVector2D | tuple[float, float]):
        """
            Velocity component required. Set velocity.

            Parameters:
                velocity (JEVector2D | tuple[float, float]): New velocity
        """
        ...
    def update_velocity(self, *, x: float = 0.0, y: float = 0.0):
        """
            Velocity component required. Update velocity.

            Parameters:
                x (float) = 0.0: Velocity x to add to the current velocity x
                y (float) = 0.0: Velocity y to add to the current velocity y
        """
        ...
    def get_velocity(self) -> JEVector2D:
        """
            Velocity component required. Get velocity.

            Returns:
                JEVector2D: Velocity
        """
        ...

    # Size #
    def set_size(self, size: JEVector2D | tuple[float, float]):
        """
            Size component required. Set size.

            Parameters:
                size (JEVector2D | tuple[float, float]): New size
        """
        ...
    def update_size(self, *, x: float = 0.0, y: float = 0.0):
        """
            Size component required. Update size.

            Parameters:
                x (float) = 0.0: Size x to add to the current size x
                y (float) = 0.0: Size y to add to the current size y
        """
        ...
    def get_size(self) -> JEVector2D:
        """
            Size component required. Get size.

            Returns:
                JEVector2D: Size
        """
        ...

    # Rotation #
    def set_rotation(self, rotation: float):
        """
            Rotation component required. Set rotation.

            Parameters:
                rotation (JEFont): New rotation (degrees)
        """
        ...
    def update_rotation(self, *, r: float = 0.0):
        """
            Rotation component required. Update rotation.

            Parameters:
                r (float) = 0.0: Rotation to add to the current rotation (degrees)
        """
        ...
    def get_rotation(self) -> float:
        """
            Rotation component required. Set rotation.

            Returns:
                float: Rotation
        """
        ...


    ## Others ##
    # Group #
    def group_add(self, entity: JEEntity):
        """
            Group component required. Add entity to group.

            Parameters:
                entity (JEEntity): Entity to add
        """
        ...
    def group_remove(self, entity: JEEntity):
        """
            Group component required. Remove entity from group.

            Parameters:
                entity (JEEntity): Entity to remove
        """
        ...
    def get_group(self) -> JEContainer[JEEntity]:
        """
            Group component required. Get group.

            Returns:
                JEContainer[JEEntity]: Group
        """
        ...
