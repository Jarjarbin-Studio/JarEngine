"""
    JarEngine - Python Game Engine Wrapper (Pygame-based)

    JarEngine is a lightweight game framework built on top of Pygame
    that simplifies usage while providing higher-level abstractions for
    game development and prototyping.

    Version: jarengine-v0.1.0
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

from typing import final as _final

from sources.interns.low_classes import (
    JEInternGraphic as _JEInternGraphic,
    JEInternGraphicalObject as _JEInternGraphicalObject
)
from sources.interns.base_classe import JEInternClassBase as _JEInternClassBase
from sources.systems.container import JEContainer as _JEContainer
from sources.interns.decorators import documentation as _documentation

@_documentation
@_final
class JEInternRessources(_JEInternClassBase):
    """Ressources (Internal API)"""

    def __init__(self):
        """JEInternRessources creator"""
        super().__init__()

        self._textures: _JEContainer[_JEInternGraphic] = _JEContainer(_JEInternGraphic)
        self._animations: _JEContainer[_JEInternGraphic] = _JEContainer(_JEInternGraphic)
        self._font: _JEContainer[_JEInternGraphic] = _JEContainer(_JEInternGraphic)

    @property
    def texture(self) -> _JEContainer[_JEInternGraphic]:
        """Get texture container"""
        return self._textures

    @property
    def animations(self) -> _JEContainer[_JEInternGraphic]:
        """Get animation container"""
        return self._animations

    @property
    def font(self) -> _JEContainer[_JEInternGraphic]:
        """Get font container"""
        return self._font

@_documentation
@_final
class JEInternDrawable(_JEInternClassBase):
    """Drawable (Internal API)"""

    def __init__(self):
        """JEInternDrawable creator"""
        super().__init__()

        self._sprite: _JEContainer[_JEInternGraphicalObject] = _JEContainer(_JEInternGraphicalObject)

    @property
    def sprite(self) -> _JEContainer[_JEInternGraphic]:
        """Get sprite container"""
        return self._sprite

@_documentation
@_final
class JEInternWindowSettings(_JEInternClassBase):
    """WindowSettings (Internal API)"""

    def __init__(
            self,
            size: tuple[int, int] = (0, 0),
            flags: int = 0,
            fps: int = 60,
            depth: int = 0,
            display: int = 0,
            vsync: int = 0,
            title: str = "JarEngine Game"
        ):
        """JEInternWindowSettings creator"""
        super().__init__()

        self._size: tuple[int, int] = size
        self._flags: int = flags
        self._fps: int = fps
        self._depth: int = depth
        self._display: int = display
        self._vsync: int = vsync
        self._title: str = title

    @property
    def size(self) -> tuple[int, int]:
        """Get size"""
        return self._size

    @property
    def flags(self) -> int:
        """Get flags"""
        return self._flags

    @property
    def fps(self) -> int:
        """Get fps"""
        return self._fps

    @property
    def depth(self) -> int:
        """Get depth"""
        return self._depth

    @property
    def display(self) -> int:
        """Get display"""
        return self._display

    @property
    def vsync(self) -> int:
        """Get vsync"""
        return self._vsync

    @property
    def title(self) -> str:
        """Get title"""
        return self._title

    def __deepcopy__(
            self,
            memo
        ):
        """Deepcopy"""
        return self
