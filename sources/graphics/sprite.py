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

from sources.graphics.texture import JETexture as _JETexture
from sources.interns import PGIntern as _PGIntern
from sources.interns.low_classes import JEInternGraphicalObject as _JEInternGraphicalObject
from sources.systems.vector import JEVector2D as _JEVector2D
from sources.interns.decorators import documentation as _documentation

@_documentation
@_final
class JESprite(_JEInternGraphicalObject):
    """Sprite"""

    def __init__(
            self,
            texture: _JETexture,
            *,
            position: _JEVector2D | tuple[int, int] = _JEVector2D(0, 0),
            size: _JEVector2D | tuple[int, int] | None = None,
            name: str = "JESprite"
        ) -> None:
        """JESprite creator"""
        super().__init__(name)
        self._texture: _JETexture = texture
        self._texture.add_parent(self)
        self._position = (
            position
            if isinstance(position, _JEVector2D) else
            _JEVector2D(*position)
        )
        self._size = (
            size
            if size is not None and isinstance(size, _JEVector2D) else
            _JEVector2D(*self._texture.size)
        )
        self._rect: _PGIntern.Rect = _PGIntern.Rect(
            int(self._position.x),
            int(self._position.y),
            int(self._size.x),
            int(self._size.y)
        )

    def _sync_rect(self) -> None:
        """Update sprite internal rect"""
        self._rect.x = int(self._position.x)
        self._rect.y = int(self._position.y)
        self._rect.width = int(self._size.x)
        self._rect.height = int(self._size.y)

    @property
    def position(self) -> _JEVector2D:
        """Get sprite position"""
        return self._position

    @position.setter
    def position(self, value: _JEVector2D | tuple[float, float]) -> None:
        """Set sprite position"""
        self._position = (
            value
            if isinstance(value, _JEVector2D) else
            _JEVector2D(*value)
        )
        self._sync_rect()

    def move(self, dx: float = 0, dy: float = 0) -> None:
        """Move the sprite"""
        self._position.x += dx
        self._position.y += dy
        self._sync_rect()

    @property
    def size(self) -> _JEVector2D:
        """Get sprite size"""
        return self._size

    @size.setter
    def size(self, value: _JEVector2D | tuple[float, float]) -> None:
        """Set sprite size"""
        self._size = (
            value
            if isinstance(value, _JEVector2D) else
            _JEVector2D(*value)
        )
        self._sync_rect()

    def scale(self, dx: float = 0, dy: float = 0) -> None:
        """Scale the sprite"""
        self._size.x += dx
        self._size.y += dy
        self._sync_rect()

    @property
    def texture(self) -> _JETexture:
        """Get the texture"""
        return self._texture

    @property
    def surface(self) -> _PGIntern.Surface:
        """Get sprite surface (PGIntern)"""
        return _PGIntern.transform.scale(
            self._texture.surface,
            (int(self._size.x), int(self._size.y))
        )

    @property
    def rect(self) -> _PGIntern.Rect:
        """Get sprite rect (PGIntern)"""
        return self._rect
