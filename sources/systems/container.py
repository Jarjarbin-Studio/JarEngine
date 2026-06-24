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
    final as _final,
    TypeVar as _TypeVar,
    Generic as _Generic,
    Optional as _Optional,
    Iterator as _Iterator
)

from sources.interns import JTKInternError as _JTKInternError
from sources.interns.base_classe import JEInternClassBase as _JEInternClassBase
from sources.interns.decorators import documentation as _documentation
from sources.systems.bool import JEBool as _JEBool

_T = _TypeVar("_T", bound=_JEInternClassBase)

@_documentation
@_final
class JEContainer(_Generic[_T], _JEInternClassBase):
    """Container"""

    def __init__(
            self,
            allowed_type: type[_T],
            allow_subclass: _JEBool = _JEBool(0)
        ):
        """JEContainer creator"""
        if not isinstance(allowed_type, type):
            raise _JTKInternError.Error.ErrorType(
                f"\n{allowed_type.__name__!r} is not a class type."
            )

        if not issubclass(allowed_type, _JEInternClassBase):
            raise _JTKInternError.Error.ErrorType(
                f"\n{allowed_type.__name__!r} isn't of type {_JEInternClassBase.__name__!r}."
            )

        super().__init__()
        self._data: dict[str, _T] = {}
        self._allowed_type: type[_T] = allowed_type
        self._allow_subclass: _JEBool = allow_subclass

    def __setitem__(
            self,
            obj
        ) -> None:
        """Add object to container"""
        self.add(obj)

    def add(
            self,
            obj: _T
        ):
        """Add object to container"""
        if not isinstance(obj, self._allowed_type):
            if not (self._allow_subclass and issubclass(type(obj), self._allowed_type)):
                raise _JTKInternError.Error.ErrorType(
                    f"\n{type(obj).__name__!r} isn't of type {self._allowed_type.__name__!r}."
                )

        base_key = str(obj.jeid)
        key = base_key
        n = 1

        while key in self._data:
            key = f"{base_key}({n})"
            n += 1

        if hasattr(obj, "add_parent"):
            obj.add_parent(self)

        self._data[key] = obj

    def __getitem__(
            self,
            *,
            name: _Optional[str] = None,
            jeid: _Optional[str] = None,
            instance: _Optional[_T] = None
        ) -> _T:
        """Get object by name"""
        return self.get(name=name, jeid=jeid, instance=instance)

    def get(
            self,
            *,
            name: _Optional[str] = None,
            jeid: _Optional[str] = None,
            instance: _Optional[_T] = None
        ) -> _Optional[_T]:
        """Get object by name"""
        if not (name or jeid or instance):
            raise _JTKInternError.Error.ErrorKey(
                "\nName, JEID or Instance are required."
            )

        if name:
            for key, obj in self._data.items():
                if obj.name == name:
                    return obj
        elif jeid and jeid in self._data:
            return self._data[jeid]
        elif instance:
            for key, obj in self._data.items():
                if obj == instance:
                    return obj
        raise _JTKInternError.Error.ErrorKey(
            f"\n{name or jeid or instance!r} not in container."
        )

    def rm(
            self,
            *,
            name: _Optional[str] = None,
            jeid: _Optional[str] = None,
            instance: _Optional[_T] = None
        ) -> _Optional[_T]:
        """Remove object by name, jeid or instance"""
        if not (name or jeid or instance):
            raise _JTKInternError.Error.ErrorKey(
                "\nName, JEID or Instance are required."
            )

        if name:
            for key, obj in self._data.items():
                if obj.name == name:
                    return self._data.pop(key)
        elif jeid and jeid in self._data:
            return self._data.pop(jeid)
        elif instance:
            for key, obj in self._data.items():
                if obj == instance:
                    return self._data.pop(key)
        raise _JTKInternError.Error.ErrorKey(
            f"\n{name or jeid or instance!r} not in container."
        )

    def __iter__(self) -> _Iterator[_T]:
        return iter(self._data.values())

    @property
    def data(self) -> _T:
        """Get data"""
        return self._data
