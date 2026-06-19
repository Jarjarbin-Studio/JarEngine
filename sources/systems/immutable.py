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
from builtins import type as _type
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
    def type(self) -> _type:
        return self._type

    @property
    def data(self) -> _Any:
        return _unfreeze(self._frozen)

    def __str__(self) -> str:
        return f"{self._frozen} (Immutable)"

    def __repr__(self) -> str:
        return f"{self._frozen!r} (Immutable)"

    def __call__(self) -> _Any:
        data = self.data

        try:
            if self._type in (list, tuple, set, dict):
                return self._type(data)

            return data

        except Exception as err:
            raise TypeError(
                f"JEImmutable: cannot safely reconstruct {self._type.__name__}"
            ) from err

    def __iter__(self) -> _Any:
        data = self.data

        if not hasattr(data, "__iter__"):
            raise TypeError(
                f"JEImmutable: {self._type.__name__} is not iterable"
            )

        return iter(data)

    def __len__(self) -> int:
        value = self.data

        if not hasattr(value, "__len__"):
            raise TypeError(f"{self._type.__name__} has no len()")

        return len(value)

    def __getitem__(
            self,
            item
        ) -> _Any:
        value = self.data

        if not hasattr(value, "__getitem__"):
            raise TypeError(f"{self._type.__name__} is not indexable")

        return value[item]

    def __contains__(
            self,
            item: _Any
        ) -> bool:
        return item in self.data

    def __bool__(self) -> bool:
        return bool(self.data)

    def __reversed__(self) -> _Any:
        value = self.data

        if not hasattr(value, "__reversed__"):
            raise TypeError(f"{self._type.__name__} is not reversible")

        return reversed(value)

    def count(
            self,
            value: _Any
        ) -> int:
        data = self.data
        if not hasattr(data, "count"):
            raise TypeError(f"{self._type.__name__} has no count()")
        return data.count(value)

    def index(
            self,
            value: _Any
        ) -> int:
        data = self.data
        if not hasattr(data, "index"):
            raise TypeError(f"{self._type.__name__} has no index()")
        return data.index(value)

    def keys(self) -> _Any:
        value = self.data
        if not hasattr(value, "keys"):
            raise TypeError(f"{self._type.__name__} is not a mapping")
        return value.keys()

    def values(self) -> _Any:
        value = self.data
        if not hasattr(value, "values"):
            raise TypeError(f"{self._type.__name__} is not a mapping")
        return value.values()

    def items(self) -> _Any:
        value = self.data
        if not hasattr(value, "items"):
            raise TypeError(f"{self._type.__name__} is not a mapping")
        return value.items()

    def get(
            self,
            key: _Any,
            default: _Any = None
        ) -> _Any:
        value = self.data
        if not hasattr(value, "get"):
            raise TypeError(f"{self._type.__name__} has no get()")
        return value.get(key, default)

    def map(
            self,
            func
        ) -> list:
        return list(map(func, self.data))

    def filter(
            self,
            func
        ) -> list:
        return list(filter(func, self.data))

    def any(self) -> bool:
        return any(self.data)

    def all(self) -> bool:
        return all(self.data)

    def to_list(self) -> list:
        value = self.data
        if isinstance(value, (list, tuple, set)):
            return list(value)
        raise TypeError(f"{self._type.__name__} cannot be converted to list")

    def to_dict(self) -> dict:
        value = self.data
        if isinstance(value, dict):
            return dict(value)
        raise TypeError(f"{self._type.__name__} cannot be converted to dict")

    def clone(self) -> JEImmutable:
        return JEImmutable(self.data)

    def __eq__(
            self,
            other: _Any
        ) -> bool:
        return self.data == other

    def __ne__(
            self,
            other: _Any
        ) -> bool:
        return self.data != other