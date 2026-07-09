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

from typing import (
    final as _final,
    Generic as _Generic,
    TypeVar as _TypeVar,
    cast as _cast,
)

from copy import deepcopy as _deepcopy

from jarengine.interns.base_classe import JEInternBaseClass as _JEInternBaseClass
from jarengine.interns.decorators import documentation as _documentation

_T = _TypeVar("_T")

def _freeze(value):
    """Return the value into a frozen state"""
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
    """Unfreeze the value"""
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
    """Immutable (object freezing system)"""

    def __init__(self, value) -> None:
        """JEImmutable creator"""
        super().__init__()
        self._original_type = type(value)
        self._frozen = _freeze(value)

    @property
    def data(self):
        """Returns a reconstructed copy of the frozen data. WARNING: not identity-stable."""
        return _cast(_T, _unfreeze(self._frozen))

    @property
    def frozen(self):
        """Internal immutable representation (fast, no reconstruction)."""
        return self._frozen

    @property
    def type(self):
        """Get original type"""
        return self._original_type

    def __str__(self):
        """Get the information of the object"""
        return f"{self._frozen} (Immutable)"

    def __repr__(self):
        """Get the representation of the object"""
        return f"JEImmutable({self._original_type.__name__})"

    def __iter__(self):
        """Iterator over the data"""
        return iter(self.data)

    def __len__(self):
        """Get data length"""
        return len(self.data)

    def __getitem__(self, item):
        """Get an item in the data"""
        return self.data[item]

    def __contains__(self, item):
        """Check if data contains item"""
        return item in self.data

    def __bool__(self):
        """Return boolean of data"""
        return bool(self.data)

    def __reversed__(self):
        """Get reversed version of data"""
        return reversed(self.data)

    def map(self, func):
        """Map the data"""
        return list(map(func, self.data))

    def filter(self, func):
        """Filter the data"""
        return list(filter(func, self.data))

    def any(self):
        """Check if data is any"""
        return any(self.data)

    def all(self):
        """Check if data is all"""
        return all(self.data)

    def count(self, value):
        """Count the number of value occurrence in the data"""
        return self.data.count(value)

    def index(self, value):
        """Get the index of the value occurrence in the data"""
        return self.data.index(value)

    def keys(self):
        """Return the keys of the data"""
        data = self.data
        if not hasattr(data, "keys"):
            raise TypeError("Not a mapping")
        return data.keys()

    def values(self):
        """Return the values of the data"""
        data = self.data
        if not hasattr(data, "values"):
            raise TypeError("Not a mapping")
        return data.values()

    def items(self):
        """Return the items of the data"""
        data = self.data
        if not hasattr(data, "items"):
            raise TypeError("Not a mapping")
        return data.items()

    def get(self, key, default):
        """Get the item with the given key"""
        data = self.data
        if not hasattr(data, "get"):
            raise TypeError("Not a mapping")
        return data.get(key, default)

    def to_list(self):
        """Transform data to a list"""
        return list(self.data)

    def to_dict(self):
        """Transform data to a dict"""
        data = self.data
        if not isinstance(data, dict):
            raise TypeError("Not a dict")
        return dict(data)

    def clone(self):
        """Clone data"""
        return JEImmutable(self.data)

    def __eq__(self, other):
        """Compare data"""
        if isinstance(other, JEImmutable):
            return self.data == other.data
        return self.data == other
