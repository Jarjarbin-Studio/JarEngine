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

from jarengine.interns.high_classes import JEInternEntityComponent
from jarengine.resources.music import JEMusic
from jarengine.resources.sound import JESound
from jarengine.entity.entity import JEEntity
from jarengine.interns import PGExtern

class JEMusicComponent(JEInternEntityComponent):
    def __init__(self, owner: JEEntity, music: JEMusic):
        """
            JEMusicComponent

            Parameters:
                owner (JEEntity): owner of the component
                music (JEMusic): music resource
        """
        ...
    @property
    def music(self) -> JEMusic: ...
    @music.setter
    def music(self, font: JEMusic): ...
    @property
    def volume(self) -> float: ...
    @volume.setter
    def volume(self, volume: float): ...
    def play(self, loop: int): ...
    def pause(self): ...
    def resume(self): ...
    def stop(self): ...
    def __call__(self) -> JEMusic: ...
    def copy(self, new_owner: JEEntity) -> JEMusicComponent: ...

class JESoundComponent(JEInternEntityComponent):
    def __init__(self, owner: JEEntity, sound: JESound):
        """
            JESoundComponent

            Parameters:
                owner (JEEntity): owner of the component
                sound (JESound): sound resource
        """
        ...
    @property
    def sound(self) -> JESound: ...
    @sound.setter
    def sound(self, font: JESound): ...
    @property
    def volume(self) -> float: ...
    @volume.setter
    def volume(self, volume: float): ...
    def play(self, loop: int) -> PGExtern.mixer.Channel: ...
    def pause(self): ...
    def resume(self): ...
    def stop(self): ...
    def fadeout(self, milliseconds: int): ...
    def get_channel(self) -> PGExtern.mixer.Channel: ...
    def __call__(self) -> JEMusic: ...
    def copy(self, new_owner: JEEntity) -> JEMusicComponent: ...
