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

from copy import deepcopy as _deepcopy
from typing import final as _final

from jarengine.entity.entity import JEEntity as _JEEntity
from jarengine.interns.helpers import (
    assertion_type as _assertion_type,
    safe_cast as _safe_cast
)
from jarengine.interns import PGExtern as _PGExtern
from jarengine.interns.high_classes import JEInternEntityComponent as _JEInternEntityComponent
from jarengine.interns.decorators import documentation as _documentation
from jarengine.resources.music import JEMusic as _JEMusic
from jarengine.resources.sound import JESound as _JESound
import jarengine.interns.log as _log
from resources import music


@_documentation
@_final
class JEMusicComponent(_JEInternEntityComponent):

    def __init__(self, owner, music):

        _assertion_type(owner, _JEEntity, "owner must be of type 'JEEntity'", True)
        _assertion_type(music, _JEMusic, "music must be of type 'JEMusic'", True)

        super().__init__(owner, JEMusicComponent)
        self._music = music
        self._loop = 0
        self._volume = 100
        _PGExtern.mixer.music.set_volume(self._volume / 100)

        def set_music(owner_self, music):

            _assertion_type(music, _JEMusic, "music must be of type 'JEMusic'", True)

            self.music = music

        def play_music(owner_self, loop=-1):

            loop = _safe_cast(_assertion_type(loop, int, "loop must be of type 'int'"), int)

            self.play(loop)

        def pause_music(owner_self):
            self.pause()

        def resume_music(owner_self):
            self.resume()

        def stop_music(owner_self):
            self.stop()

        def set_music_volume(owner_self, volume):

            volume = _safe_cast(_assertion_type(volume, (int, float), "volume must be of type 'int' or 'float'"), int)

            self.volume = volume

        def get_music(owner_self):
            return self.music

        owner.set_music = set_music.__get__(owner, type(owner))
        owner.play_music = play_music.__get__(owner, type(owner))
        owner.pause_music = pause_music.__get__(owner, type(owner))
        owner.resume_music = resume_music.__get__(owner, type(owner))
        owner.stop_music = stop_music.__get__(owner, type(owner))
        owner.set_music_volume = set_music_volume.__get__(owner, type(owner))
        owner.get_music = get_music.__get__(owner, type(owner))

        _log.log("DEBUG", "OBJECT", f"JEMusicComponent: Created", self.jeid, owner, music)

    @property
    def music(self):
        return self._music

    @music.setter
    def music(self, music):
        self._music = music

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, volume):
        self._volume = max(0, min(100, volume))
        _PGExtern.mixer.music.set_volume(volume / 100)

    def play(self, loop=-1):
        self._loop = loop

        _PGExtern.mixer.music.load(self._music.path)
        _PGExtern.mixer.music.play(loop)

    def pause(self):
        _PGExtern.mixer.music.pause()

    def resume(self):
        _PGExtern.mixer.music.unpause()

    def stop(self):
        _PGExtern.mixer.music.stop()

    def __call__(self):
        return self._music

    def copy(self, new_owner):

        _log.log("DEBUG", "ENTITY", f"JEFlipComponent: Copied", self.jeid, new_owner)

        return JEMusicComponent(new_owner, _deepcopy(self._music))

@_documentation
@_final
class JESoundComponent(_JEInternEntityComponent):

    def __init__(self, owner, sound):

        _assertion_type(owner, _JEEntity, "owner must be of type 'JEEntity'", True)
        _assertion_type(sound, _JESound, "sound must be of type 'JESound'", True)

        super().__init__(owner, JESoundComponent)
        self._sound = sound
        self._channel = None
        self._volume = 100

        self._sound.sound.set_volume(self._volume / 100)

        def set_sound(owner_self, sound):

            _assertion_type(sound, _JESound, "sound must be of type 'JESound'", True)

            self.sound = sound

        def play_sound(owner_self, loop=0):

            loop = _safe_cast(_assertion_type(loop, (int, float), "loop must be of type 'int' or 'float'"), int)

            return self.play(loop)

        def stop_sound(owner_self):
            self.stop()

        def pause_sound(owner_self):
            self.pause()

        def resume_sound(owner_self):
            self.resume()

        def fade_sound(owner_self, time):

            time = _safe_cast(_assertion_type(time, (int, float), "time must be of type 'int' or 'float'"), int)

            self.fadeout(time)

        def set_sound_volume(owner_self, volume):

            volume = _safe_cast(_assertion_type(volume, (int, float), "volume must be of type 'int' or 'float'"), int)

            self.volume = volume

        def get_sound(owner_self):
            return self.sound

        owner.set_sound = set_sound.__get__(owner, type(owner))
        owner.play_sound = play_sound.__get__(owner, type(owner))
        owner.stop_sound = stop_sound.__get__(owner, type(owner))
        owner.pause_sound = pause_sound.__get__(owner, type(owner))
        owner.resume_sound = resume_sound.__get__(owner, type(owner))
        owner.fade_sound = fade_sound.__get__(owner, type(owner))
        owner.set_sound_volume = set_sound_volume.__get__(owner, type(owner))
        owner.get_sound = get_sound.__get__(owner, type(owner))

        _log.log("DEBUG", "OBJECT", f"JESoundComponent: Created", self.jeid, owner, sound)

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, volume):
        self._volume = max(0, min(100, volume))
        self._sound.sound.set_volume(self._volume / 100)

    def play(self, loop=0):
        self._channel = self._sound.sound.play(loop)
        return self._channel

    def stop(self):
        if self._channel:
            self._channel.stop()

    def pause(self):
        if self._channel:
            self._channel.pause()

    def resume(self):
        if self._channel:
            self._channel.unpause()

    def fadeout(self, milliseconds):
        if self._channel:
            self._channel.fadeout(milliseconds)

    def get_channel(self):
        return self._channel

    def __call__(self):
        return self._sound

    def copy(self, new_owner):

        _log.log("DEBUG", "ENTITY", f"JESoundComponent: Copied", self.jeid, new_owner)

        return JESoundComponent(new_owner, _deepcopy(self._sound))
