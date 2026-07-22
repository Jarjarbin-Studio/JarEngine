# =============================================================================
# JarEngine - Python Game Engine Wrapper (Pygame-based)
# =============================================================================
#
# JarEngine is a lightweight game framework built on top of Pygame
# that simplifies usage while providing higher-level abstractions for
# game development and prototyping.
#
# =============================================================================
# Version: jarengine-v1.8
# Author: Jarjarbin Studio
# Licence: GPL v3
# =============================================================================
#
# This engine is inspired by Pygame, modern game engine design patterns,
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
# This is NOT Pygame itself.
# It is a custom abstraction layer built on top of Pygame.
#
# =============================================================================

from __future__ import annotations

from copy import deepcopy as _deepcopy
from typing import final as _final

from jarengine.entity.entity import JEEntity as _JEEntity
from jarengine.interns.helpers import assertion_type as _assertion_type
from jarengine.interns.high_classes import JEInternEntityComponent as _JEInternEntityComponent
from jarengine.interns.decorators import documentation as _documentation
from jarengine.systems.vector import JEVector2D as _JEVector2D

@_documentation
@_final
class JEPositionComponent(_JEInternEntityComponent):

    __recursive__ = False

    def __init__(self, owner, position):

        _assertion_type(owner, _JEEntity, "owner must be of type 'JEEntity'")
        _assertion_type(position, (tuple, _JEVector2D), "position must be of type 'tuple' or 'JEVector2D'")

        super().__init__(owner, JEPositionComponent)
        self._position = (
            position
            if isinstance(position, _JEVector2D) else
            _JEVector2D(*position)
        )

        def set_position(owner_self, position):

            _assertion_type(position, (tuple, _JEVector2D), "position must be of type 'tuple' or 'JEVector2D'")

            self.position = position

        def update_position(owner_self, *, x = 0, y = 0):

            _assertion_type(x, (float, int), "x must be of type 'float' or 'int'")
            _assertion_type(y, (float, int), "y must be of type 'float' or 'int'")

            self._position.x += x
            self._position.y += y

        def get_position(owner_self):
            return self.position

        def get_world_position(owner_self):

            position = owner_self.get_position()

            if position is None:
                return _JEVector2D(0, 0)

            x = position.x
            y = position.y

            parent = owner_self.parents.get(_type=type(owner_self), default=None)

            if parent:
                world = parent.get_world_position()

                x += world.x
                y += world.y

            return _JEVector2D(x, y)

        owner.set_position = set_position.__get__(owner, type(owner))
        owner.update_position = update_position.__get__(owner, type(owner))
        owner.get_position = get_position.__get__(owner, type(owner))
        owner.get_world_position = get_world_position.__get__(owner, type(owner))

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = (
            position
            if isinstance(position, _JEVector2D) else
            _JEVector2D(*position)
        )

    def __call__(self):
        return self._position

    def copy(self, new_owner):
        return JEPositionComponent(new_owner, _deepcopy(self._position))

@_documentation
@_final
class JEVelocityComponent(_JEInternEntityComponent):

    __recursive__ = False

    def __init__(self, owner, velocity):
        super().__init__(owner, JEVelocityComponent)
        self._velocity = (
            velocity
            if isinstance(velocity, _JEVector2D) else
            _JEVector2D(*velocity)
        )

        def set_velocity(owner_self, velocity):

            _assertion_type(velocity, (tuple, _JEVector2D), "velocity must be of type 'tuple' or 'JEVector2D'")

            self.velocity = velocity

        def update_velocity(owner_self, *, x = 0, y = 0):

            _assertion_type(x, (float, int), "x must be of type 'float' or 'int'")
            _assertion_type(y, (float, int), "y must be of type 'float' or 'int'")

            self._velocity.x += x
            self._velocity.y += y

        def get_velocity(owner_self):
            return self.velocity

        owner.set_velocity = set_velocity.__get__(owner, type(owner))
        owner.update_velocity = update_velocity.__get__(owner, type(owner))
        owner.get_velocity = get_velocity.__get__(owner, type(owner))

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, velocity):
        self._velocity = (
            velocity
            if isinstance(velocity, _JEVector2D) else
            _JEVector2D(*velocity)
        )

    def __call__(self):
        return self._velocity

    def copy(self, new_owner):
        return JEVelocityComponent(new_owner, _deepcopy(self._velocity))

@_documentation
@_final
class JESizeComponent(_JEInternEntityComponent):

    __recursive__ = False

    def __init__(self, owner, size):
        super().__init__(owner, JESizeComponent)
        self._size = (
            size
            if isinstance(size, _JEVector2D) else
            _JEVector2D(*size)
        )

        def set_size(owner_self, size):

            _assertion_type(size, (tuple, _JEVector2D), "size must be of type 'tuple' or 'JEVector2D'")

            self.size = size

        def update_size(owner_self, *, x = 0, y = 0):

            _assertion_type(x, (float, int), "x must be of type 'float' or 'int'")
            _assertion_type(y, (float, int), "y must be of type 'float' or 'int'")

            self._size.x += x
            self._size.y += y

        def get_size(owner_self):
            return self.size

        owner.set_size = set_size.__get__(owner, type(owner))
        owner.update_size = update_size.__get__(owner, type(owner))
        owner.get_size = get_size.__get__(owner, type(owner))

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = (
            size
            if isinstance(size, _JEVector2D) else
            _JEVector2D(*size)
        )

    def __call__(self):
        return self._size

    def copy(self, new_owner):
        return JESizeComponent(new_owner, _deepcopy(self._size))

@_documentation
@_final
class JERotationComponent(_JEInternEntityComponent):

    __recursive__ = False

    def __init__(self, owner, rotation):
        super().__init__(owner, JERotationComponent)
        self._rotation = rotation

        def set_rotation(owner_self, rotation):
            self.rotation = rotation

        def update_rotation(owner_self, *, r = 0):
            self._rotation += r

        def get_rotation(owner_self):
            return self.rotation

        owner.set_rotation = set_rotation.__get__(owner, type(owner))
        owner.update_rotation = update_rotation.__get__(owner, type(owner))
        owner.get_rotation = get_rotation.__get__(owner, type(owner))

    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        self._rotation = rotation

    def __call__(self):
        return self._rotation

    def copy(self, new_owner):
        return JERotationComponent(new_owner, _deepcopy(self._rotation))
