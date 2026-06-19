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
from copy import deepcopy as _deepcopy

from sources.interns.base_classe import JEInternClassBase as _JEInternClassBase

def _freeze(value: _Any) -> _Any:
    if isinstance(value, (int, float, str, bool, bytes, type(None))):
        return value

    if isinstance(value, tuple):
        return tuple(_freeze(v) for v in value)

    if isinstance(value, list):
        return tuple(_freeze(v) for v in value)

    if isinstance(value, set):
        return frozenset(_freeze(v) for v in value)

    if isinstance(value, dict):
        return frozenset(
            (_freeze(k), _freeze(v))
            for k, v in value.items()
        )

    return _deepcopy(value)


def _unfreeze(value: _Any) -> _Any:
    if isinstance(value, tuple):
        return [_unfreeze(v) for v in value]

    if isinstance(value, frozenset):
        try:
            return {k: _unfreeze(v) for k, v in value}
        except Exception:
            return set(_unfreeze(v) for v in value)

    return value


@_final
class JEImmutable(_JEInternClassBase):

    def __init__(
            self,
            value: _Any
        ) -> None:
        super().__init__()

        self._type: type = type(value)
        self._frozen: _Any = _freeze(value)

    @property
    def type(self) -> type:
        return self._type

    @property
    def data(self) -> _Any:
        return _unfreeze(self._frozen)

    def __str__(self) -> str:
        return f"{self._frozen} (Immutable)"

    def __repr__(self) -> str:
        return f"{self._frozen!r} (Immutable)"
