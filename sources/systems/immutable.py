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

from typing import (
    Any as _Any,
    final as _final
)
from types import MappingProxyType as _MappingProxyType

from sources.interns.base_classes import JEInternClassBase as _JEInternClassBase

@_final
class JEImmutable(_JEInternClassBase):

    def __init__(
            self,
            value: _Any
        ) -> None:
        super().__init__()

        self._type: type = type(value)
        self._mpt: _MappingProxyType = _MappingProxyType(value)

    @property
    def type(self) -> type:
        return self._type

    @property
    def data(self) -> _Any:
        return self._type(self._mpt)

    def __str__(self) -> str:
        return f"{self._type(self._mpt)} (Immutable)"

    def __repr__(self) -> str:
        return f"{self._type(self._mpt)!r} (Immutable)"
