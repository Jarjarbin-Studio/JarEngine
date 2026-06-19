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

from sources.interns import JTKInternError as _JTKInternError
from sources.interns.base_classe import JEInternClassBase as _JEInternClassBase
from sources.systems.immutable import JEImmutable as _JEImmutable

@_final
class JEContainer(_JEInternClassBase):

    def __init__(
            self,
            allowed_type: type
        ):
        super().__init__()

        if not isinstance(allowed_type, type):
            raise _JTKInternError.Error.ErrorType(
                f"\n{allowed_type.__name__!r} is not a class type."
            )

        if not issubclass(allowed_type, _JEInternClassBase):
            raise _JTKInternError.Error.ErrorType(
                f"\n{type(allowed_type).__name__!r} isn't of type {_JEInternClassBase.__name__!r}."
            )

        self._data: dict = {}
        self._allowed_type: type = allowed_type

    def __getitem__(self, name: str):
        return self._data[name]

    def __setitem__(self, key: str, value):
        self._data[key] = value

    def add(self, obj: _JEInternClassBase):
        if not isinstance(obj, self._allowed_type):
            raise _JTKInternError.Error.ErrorType(
                f"\n{type(obj).__name__!r} isn't of type {_JEInternClassBase.__name__!r}."
            )

        self._data[obj.name if getattr(obj, "name", None) else str(obj.id)] = obj

    @property
    def data(self) -> _JEImmutable:
        return _JEImmutable(self._data)
