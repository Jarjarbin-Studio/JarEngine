# =============================================================================
# JarEngine - Python Game Engine Wrapper (PyGame-based)
# =============================================================================
#
# JarEngine is a lightweight game framework built on top of PyGame
# that simplifies usage while providing higher-level abstractions for
# game development and prototyping.
#
# =============================================================================
# Version: jarengine-v1.7
# Author: Jarjarbin Studio
# Licence: GPL v3
# =============================================================================
#
# This engine is inspired by PyGame, modern game engine design patterns,
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
# This is NOT PyGame itself.
# It is a custom abstraction layer built on top of PyGame.
#
# =============================================================================

from __future__ import annotations

from typing import (
    final as _final,
    Generic as _Generic,
    TypeVar as _TypeVar,
    cast as _cast,
)

from copy import deepcopy as _deepcopy

from jarengine.interns.base_classe import JEInternBaseClass as _JEInternBaseClass
from jarengine.interns.decorators import documentation as _documentation
from jarengine.systems.bool import JEBool as _JEBool

_T = _TypeVar("_T")

def _freeze(value):
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
            (_freeze(k), _freeze(v)) for k, v in value.items()
        )

    try:
        return _deepcopy(value)
    except Exception:
        return value

def _unfreeze(value):
    if isinstance(value, tuple):
        return tuple(_unfreeze(v) for v in value)

    if isinstance(value, frozenset):
        return {
            k: _unfreeze(v) for k, v in value
            if isinstance(value, frozenset)
        }

    return value

@_documentation
@_final
class JEImmutable(_Generic[_T], _JEInternBaseClass):

    def __init__(self, value):
        super().__init__()
        self._original_type = type(value)
        self._frozen = _freeze(value)
        self._reconstruction = _cast(self._original_type, _unfreeze(self._frozen))

    @property
    def type(self):
        return self._original_type

    @property
    def frozen(self):
        return self._frozen

    @property
    def data(self):
        return self._reconstruction

    def __str__(self):
        return f"{self._frozen} (Immutable)"

    def __repr__(self):
        return f"JEImmutable({self._original_type.__name__})"

    def __iter__(self):
        return iter(self._reconstruction)

    def __len__(self):
        return len(self._reconstruction)

    def __getitem__(self, item):
        return self._reconstruction[item]

    def __contains__(self, item):
        return _JEBool(item in self._reconstruction)

    def __bool__(self):
        return bool(self._reconstruction)

    def __reversed__(self):
        return reversed(self._reconstruction)

    def map(self, func):
        return list(map(func, self._reconstruction))

    def filter(self, func):
        return list(filter(func, self._reconstruction))

    def any(self):
        return _JEBool(any(self._reconstruction))

    def all(self):
        return _JEBool(all(self._reconstruction))

    def count(self, value):
        return self._reconstruction.count(value)

    def index(self, value):
        return self._reconstruction.index(value)

    def keys(self):
        data = self._reconstruction
        if not hasattr(data, "keys"):
            raise TypeError("Not a mapping")
        return data.keys()

    def values(self):
        data = self._reconstruction
        if not hasattr(data, "values"):
            raise TypeError("Not a mapping")
        return data.values()

    def items(self):
        data = self._reconstruction
        if not hasattr(data, "items"):
            raise TypeError("Not a mapping")
        return data.items()

    def get(self, key, default):
        data = self._reconstruction
        if not hasattr(data, "get"):
            raise TypeError("Not a mapping")
        return data.get(key, default)

    def to_list(self):
        return list(self._reconstruction)

    def to_dict(self):
        data = self._reconstruction
        if not isinstance(data, dict):
            raise TypeError("Not a dict")
        return dict(data)

    def clone(self):
        return JEImmutable(self._reconstruction)

    def __eq__(self, other):
        return _JEBool(self._reconstruction == other)
