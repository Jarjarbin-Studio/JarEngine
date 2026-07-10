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

from jarengine.interns.low_classes import JEInternGraphic as _JEInternGraphic
from jarengine.interns.base_classe import JEInternBaseClass as _JEInternBaseClass
from jarengine.interns import JTKExternError as _JTKExternError
from jarengine.systems.container import JEContainer as _JEContainer
from jarengine.interns.decorators import documentation as _documentation
from jarengine.systems.bool import JEBool as _JEBool

@_documentation
class JEInternOwnership(_JEInternBaseClass):
    """Ownership (Internal API)"""

    def __init__(self):
        """JEInternOwnership creator"""
        super().__init__()
        self._parents = _JEContainer(_JEInternBaseClass)
        self._children = _JEContainer(_JEInternBaseClass)

    @property
    def parents(self):
        """Get parents list"""
        return self._parents

    def add_parent(self, parent):
        """Add a parent"""
        self._parents.add(parent)

    @property
    def children(self):
        """Get children list"""
        return self._children

    def add_child(self, child):
        """Add a child"""
        self._children.add(child)

@_documentation
class JEInternEntityComponent(_JEInternGraphic, JEInternOwnership):
    """EntityComponent (Internal API)"""

    def __init__(self, owner, _type):
        """JEInternEntityComponent creator"""
        super().__init__(f"{_type.__name__}({owner.jeid})")
        self.add_parent(owner)
        owner.add_component(self)

    def __call__(self):
        """Get Component"""
        raise NotImplementedError

    def copy(self):
        """Copy Component"""
        raise NotImplementedError

    def __deepcopy__(self, memo):
        return self.copy()

@_documentation
class JEInternSystems(JEInternOwnership):
    """Systems (Internal API)"""

    def __init__(self, owner):
        """JEInternSystems creator"""

        super().__init__()
        self.cache = []
        self._required = []
        self.add_parent(owner)
        owner.add_system(self)

    def refresh(self):
        """Refresh system entity cache."""

        from jarengine.games.game import JEGame as _JEGame

        self.cache.clear()

        game = self.parents.get(_type=_JEGame)

        if not game:
            return

        for entity in game._iter_entities():
            if self.accepts(entity.components):
                self.cache.append(entity)

        self.sort_cache()

    def sort_cache(self):
        """Sort system cache."""
        pass

    def accepts(self, components):
        """Check if all required components are available"""
        try:
            return _JEBool(all(components.get(_type=req) is not None for req in self._required))
        except Exception:
            return _JEBool(0)

    @staticmethod
    def update(window, entity, entities, dt):
        """Update entities"""
        raise NotImplementedError

class JEInternTransform(_JEInternBaseClass):

    _fields = ["x", "y", "z"]

    def _check(self, other):
        if not isinstance(other, type(self)):
            raise _JTKExternError.Error.ErrorType("\nInvalid transform type")

        return type(self)

    def _get(self):
        return (getattr(self, f, 0.0) for f in self._fields)

    def _create(self, x, y, z):
        try:
            return type(self)(x, y, z)
        except TypeError:
            return type(self)(x, y)

    def _apply(self, other):
        for field, value in zip(
            self._fields,
            other
        ):
            if hasattr(self, field):
                setattr(
                    self,
                    field,
                    value
                )

    def __add__(self, other):
        _type = self._check(other)

        x1, y1, z1 = self._get()
        x2, y2, z2 = other._get()

        return self._create(
            x1 + x2,
            y1 + y2,
            z1 + z2
        )

    def __sub__(self, other):
        _type = self._check(other)

        x1, y1, z1 = self._get()
        x2, y2, z2 = other._get()

        return self._create(
            x1 - x2,
            y1 - y2,
            z1 - z2
        )

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            x, y, z = self._get()

            return self._create(
                x * other,
                y * other,
                z * other
            )

        self._check(other)

        x1, y1, z1 = self._get()
        x2, y2, z2 = other._get()

        return self._create(
            x1 * x2,
            y1 * y2,
            z1 * z2
        )

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError()

            x, y, z = self._get()

            return self._create(
                x / other,
                y / other,
                z / other
            )

        self._check(other)

        x1, y1, z1 = self._get()
        x2, y2, z2 = other._get()

        if x2 == 0 or y2 == 0 or z2 == 0:
            raise ZeroDivisionError()

        return self._create(
            x1 / x2,
            y1 / y2,
            z1 / z2
        )

    def __neg__(self):
        x, y, z = self._get()

        return self._create(
            -x,
            -y,
            -z
        )

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False

        x1, y1, z1 = self._get()
        x2, y2, z2 = other._get()

        return (
            x1 == x2 and
            y1 == y2 and
            z1 == z2
        )

    def __iadd__(self, other):
        result = self + other

        self._apply(result)

        return self

    def __isub__(self, other):
        result = self - other

        self._apply(result)

        return self

    def __imul__(self, other):
        result = self * other

        self._apply(result)

        return self

    def __itruediv__(self, other):
        result = self / other

        self._apply(result)

        return self

    def __len__(self):
        """Get vector length"""
        x, y, z = self._get()

        return (
            x ** 2 +
            y ** 2 +
            z ** 2
        ) ** 0.5

    def length(self):
        """Get vector length"""
        return len(self)

    def normalize(self):
        """Normalize vector"""
        length = len(self)

        if length == 0:
            return type(self)()

        return self / length

    def dot(self, other):
        """Dot product"""
        self._check(other)

        x1, y1, z1 = self._get()
        x2, y2, z2 = other._get()

        return (
            x1 * x2 +
            y1 * y2 +
            z1 * z2
        )

    def distance(self, other):
        """Distance between vectors"""
        return len(self - other)

    def copy(self):
        """Copy vector"""
        return type(self)(*self._vector)

    def to_list(self):
        """Convert to list"""
        return list(self._vector)

    def __repr__(self):
        values = ", ".join(str(v) for v in self._vector)
        return f"{type(self).__name__}({values})"
