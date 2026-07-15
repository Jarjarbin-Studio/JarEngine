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

from jarengine.interns.base_classe import JEInternBaseClass as _JEInternBaseClass
from jarengine.interns.decorators import documentation as _documentation
from jarengine.interns import JTKExternError as _JTKExternError
from jarengine.systems.bool import JEBool as _JEBool

@_documentation
class JETransform(_JEInternBaseClass):

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

        return _JEBool(
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
        x, y, z = self._get()

        return (
            x ** 2 +
            y ** 2 +
            z ** 2
        ) ** 0.5

    def length(self):
        return len(self)

    def normalize(self):
        length = len(self)

        if length == 0:
            return type(self)()

        return self / length

    def dot(self, other):
        self._check(other)

        x1, y1, z1 = self._get()
        x2, y2, z2 = other._get()

        return (
            x1 * x2 +
            y1 * y2 +
            z1 * z2
        )

    def distance(self, other):
        return len(self - other)

    def copy(self):
        return type(self)(*self._vector)

    def to_list(self):
        return list(self._vector)

    def __repr__(self):
        values = ", ".join(str(v) for v in self._vector)
        return f"{type(self).__name__}({values})"
