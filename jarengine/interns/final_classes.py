"""
    JarEngine - Python Game Engine Wrapper (Pygame-based)

    JarEngine is a lightweight game framework built on top of Pygame
    that simplifies usage while providing higher-level abstractions for
    game development and prototyping.

    Version: jarengine-v1.6
    Author: Jarjarbin Studio
    Licence: GPL v3

    This engine is inspired by Pygame, modern game engine design patterns,
    and directly influenced by the architecture of NewCSFML.

    It is designed for educational purposes and small-to-medium game projects.

    It provides structured systems such as entity management, scene handling,
    render abstraction, and advanced modules like particle systems.

    WARNING:
        This is NOT Pygame itself.
        It is a custom abstraction layer built on top of Pygame.
"""

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

@_documentation
@_final
class JEInternEmptyComponent(_JEInternEntityComponent):
    """EmptyComponent"""

    def __init__(self, owner):
        """JEEmptyComponent creator"""
        super().__init__(owner, JEInternEmptyComponent)

    def __call__(self) -> _NoneType:
        """Get none"""
        return None

    def __bool__(self) -> bool:
        return False

    def copy(self, new_owner):
        return JEInternEmptyComponent(new_owner)

@_documentation
@_final
class JEInternResources(_JEInternBaseClass):
    """Resources (Internal API)"""

    def __init__(self):
        """JEInternResources creator"""
        super().__init__()

        self._textures = _JEContainer(_JETexture)
        self._animations = _JEContainer(_JEInternGraphic)
        self._font = _JEContainer(_JEFont)
        self._music = _JEContainer(_JEMusic)
        self._sound = _JEContainer(_JESound)

    @property
    def texture(self):
        """Get texture container"""
        return self._textures

    @property
    def animations(self):
        """Get animation container"""
        return self._animations

    @property
    def font(self):
        """Get font container"""
        return self._font

    @property
    def music(self):
        """Get music container"""
        return self._music

    @property
    def sound(self):
        """Get sound container"""
        return self._sound

@_documentation
@_final
class JEInternWindowSettings(_JEInternBaseClass):
    """WindowSettings (Internal API)"""

    def __init__(self, size, flags, fps, depth, display, vsync, title):
        """JEInternWindowSettings creator"""
        super().__init__()

        self._size = size
        self._flags = flags
        self._fps = fps
        self._depth = depth
        self._display = display
        self._vsync = vsync
        self._title = title

    @property
    def size(self):
        """Get size"""
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    @property
    def flags(self):
        """Get flags"""
        return self._flags

    @property
    def fps(self):
        """Get fps"""
        return self._fps

    @fps.setter
    def fps(self, fps):
        self._fps = fps

    @property
    def depth(self):
        """Get depth"""
        return self._depth

    @property
    def display(self):
        """Get display"""
        return self._display

    @property
    def vsync(self):
        """Get vsync"""
        return self._vsync

    @property
    def title(self):
        """Get title"""
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def __deepcopy__(self, memo):
        """Deepcopy"""
        return self
