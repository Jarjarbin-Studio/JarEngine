# =============================================================================
# JarEngine - Python Game Engine Wrapper (Pygame-based)
# =============================================================================
#
# JarEngine is a lightweight game framework built on top of Pygame
# that simplifies usage while providing higher-level abstractions for
# game development and prototyping.
#
# =============================================================================
# Version: jarengine-v1.10
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

from types import NoneType as _NoneType
from typing import final as _final

from jarengine.interns.high_classes import JEInternEntityComponent as _JEInternEntityComponent
from jarengine.interns.low_classes import JEInternGraphic as _JEInternGraphic
from jarengine.interns.base_classe import JEInternBaseClass as _JEInternBaseClass
from jarengine.systems.container import JEContainer as _JEContainer
from jarengine.interns.decorators import documentation as _documentation
from jarengine.resources.texture import JETexture as _JETexture
from jarengine.resources.music import JEMusic as _JEMusic
from jarengine.resources.sound import JESound as _JESound
from jarengine.resources.font import JEFont as _JEFont
from jarengine.interns import PGExtern as _PGExtern
from jarengine.interns.helpers import (
    assertion_type as _assertion_type,
    safe_cast as _safe_cast
)
from jarengine.systems.vector import JEVector2D as _JEVector2D
import jarengine.interns.log as _log

@_documentation
@_final
class JEInternEmptyComponent(_JEInternEntityComponent):

    def __init__(self, owner):
        from jarengine.entity.entity import JEEntity as _JEEntity

        _assertion_type(owner, _JEEntity, "owner must be of type 'JEEntity'", True)

        super().__init__(owner, JEInternEmptyComponent)

        _log.log("DEBUG", "OBJECT", f"JEInternEmptyComponent: Created", self.jeid, owner)

    def __call__(self) -> _NoneType:
        return None

    def __bool__(self) -> bool:
        return False

    def copy(self, new_owner):
        return JEInternEmptyComponent(new_owner)

@_documentation
@_final
class JEInternResources(_JEInternBaseClass):

    def __init__(self):
        super().__init__()

        self._textures = _JEContainer(_JETexture)
        self._animations = _JEContainer(_JEInternGraphic)
        self._font = _JEContainer(_JEFont)
        self._music = _JEContainer(_JEMusic)
        self._sound = _JEContainer(_JESound)

        _log.log("DEBUG", "OBJECT", f"JEInternResources: Created", self.jeid)

    @property
    def texture(self):
        return self._textures

    @property
    def animations(self):
        raise NotImplementedError

    @property
    def font(self):
        return self._font

    @property
    def music(self):
        return self._music

    @property
    def sound(self):
        return self._sound

@_documentation
@_final
class JEInternWindowSettings(_JEInternBaseClass):

    def __init__(self, size, flags, fps, depth, display, vsync, title):

        _assertion_type(size, _JEVector2D, "size must be of type 'JEVector2D'", True)
        flags = _safe_cast(_assertion_type(flags, int, "flags must be of type 'int'"), int)
        fps = _safe_cast(_assertion_type(fps, int, "fps must be of type 'int'"), int)
        depth = _safe_cast(_assertion_type(depth, int, "depth must be of type 'int'"), int)
        display = _safe_cast(_assertion_type(display, int, "display must be of type 'int'"), int)
        vsync = _safe_cast(_assertion_type(vsync, int, "vsync must be of type 'int'"), int)
        title = _safe_cast(_assertion_type(title, str, "title must be of type 'str'"), str)

        super().__init__()

        self._size = size
        self._flags = flags
        self._fps = fps
        self._depth = depth
        self._display = display
        self._vsync = vsync
        self._title = title
        _PGExtern.display.set_caption(title)

        _log.log("DEBUG", "OBJECT", f"JEInternWindowSettings: Created", self.jeid, size, flags, fps, depth, display, vsync, title)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):

        _assertion_type(size, _JEVector2D, "fps must be of type 'JEVector2D'", True)

        _log.log("INFO", "SCENE", f"JEInternWindowSettings: Size set", self.jeid, size)

        self._size = size

    @property
    def flags(self):
        return self._flags

    @property
    def fps(self):
        return self._fps

    @fps.setter
    def fps(self, fps):

        fps = _safe_cast(_assertion_type(fps, int, "fps must be of type 'int'"), int)

        _log.log("INFO", "SCENE", f"JEInternWindowSettings: FPS set", self.jeid, fps)

        self._fps = fps

    @property
    def depth(self):
        return self._depth

    @property
    def display(self):
        return self._display

    @property
    def vsync(self):
        return self._vsync

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):

        title = _safe_cast(_assertion_type(title, str, "title must be of type 'str'"), str)

        _log.log("INFO", "SCENE", f"JEInternWindowSettings: Title set", self.jeid, title)

        self._title = title
        _PGExtern.display.set_caption(title)

    def __deepcopy__(self, memo):
        return self
