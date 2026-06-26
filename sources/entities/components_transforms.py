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

from copy import deepcopy as _deepcopy
from typing import final as _final

from sources.interns.high_classes import JEInternalEntityComponent as _JEInternalEntityComponent
from sources.interns.decorators import documentation as _documentation
from sources.systems.vector import JEVector2D as _JEVector2D

@_documentation
@_final
class JEPositionComponent(_JEInternalEntityComponent):
    """PositionComponent"""

    def __init__(self, owner, position):
        """JEPositionComponent creator"""

        super().__init__(f"JEPositionComponent({owner.jeid})")
        self.add_parent(owner)
        owner.add_component(self)
        self._position = (
            position
            if isinstance(position, _JEVector2D) else
            _JEVector2D(*position)
        )

        def set_position(owner_self, position):
            self._position = (
                position
                if isinstance(position, _JEVector2D) else
                _JEVector2D(*position)
            )

        def update_position(owner_self, *, x = 0, y = 0):
            self._position.x += x
            self._position.y += y

        def get_position(owner_self):
            return self._position

        owner.set_position = set_position.__get__(owner, type(owner))
        owner.update_position = update_position.__get__(owner, type(owner))
        owner.get_position = get_position.__get__(owner, type(owner))

    @property
    def position(self):
        """Get position"""
        return self._position

    @position.setter
    def position(self, position):
        """Set position"""
        self._position = (
            position
            if isinstance(position, _JEVector2D) else
            _JEVector2D(*position)
        )

    def __call__(self):
        """Get position"""
        return self._position

    def copy(self, new_owner):
        """Copy position"""
        return JEPositionComponent(new_owner, _deepcopy(self._position))

@_documentation
@_final
class JEVelocityComponent(_JEInternalEntityComponent):
    """VelocityComponent"""

    def __init__(self, owner, velocity):
        """JEVelocityComponent creator"""
        super().__init__(f"JEVelocityComponent({owner.jeid})")
        self.add_parent(owner)
        owner.add_component(self)
        self._velocity = (
            velocity
            if isinstance(velocity, _JEVector2D) else
            _JEVector2D(*velocity)
        )

        def set_velocity(owner_self, velocity):
            self._velocity = (
                velocity
                if isinstance(velocity, _JEVector2D) else
                _JEVector2D(*velocity)
            )

        def update_velocity(owner_self, *, x = 0, y = 0):
            self._velocity.x += x
            self._velocity.y += y

        def get_velocity(owner_self):
            return self._velocity

        owner.set_velocity = set_velocity.__get__(owner, type(owner))
        owner.update_velocity = update_velocity.__get__(owner, type(owner))
        owner.get_velocity = get_velocity.__get__(owner, type(owner))

    @property
    def velocity(self):
        """Get velocity"""
        return self._velocity

    @velocity.setter
    def velocity(self, velocity):
        """Set velocity"""
        self._velocity = (
            velocity
            if isinstance(velocity, _JEVector2D) else
            _JEVector2D(*velocity)
        )

    def __call__(self):
        """Get velocity"""
        return self._velocity

    def copy(self, new_owner):
        """Copy velocity"""
        return JEVelocityComponent(new_owner, _deepcopy(self._velocity))

@_documentation
@_final
class JESizeComponent(_JEInternalEntityComponent):
    """SizeComponent"""

    def __init__(self, owner, size):
        """JESizeComponent creator"""
        super().__init__(f"JESizeComponent({owner.jeid})")
        self.add_parent(owner)
        owner.add_component(self)
        self._size = (
            size
            if isinstance(size, _JEVector2D) else
            _JEVector2D(*size)
        )

        def set_size(owner_self, size):
            self._size = (
                size
                if isinstance(size, _JEVector2D) else
                _JEVector2D(*size)
            )

        def update_size(owner_self, *, x = 0, y = 0):
            self._size.x += x
            self._size.y += y

        def get_size(owner_self):
            return self._size

        owner.set_size = set_size.__get__(owner, type(owner))
        owner.update_size = update_size.__get__(owner, type(owner))
        owner.get_size = get_size.__get__(owner, type(owner))

    @property
    def size(self):
        """Get size"""
        return self._size

    @size.setter
    def size(self, size):
        """Set size"""
        self._size = (
            size
            if isinstance(size, _JEVector2D) else
            _JEVector2D(*size)
        )

    def __call__(self):
        """Get size"""
        return self._size

    def copy(self, new_owner):
        """Copy size"""
        return JESizeComponent(new_owner, _deepcopy(self._size))

@_documentation
@_final
class JERotationComponent(_JEInternalEntityComponent):
    """RotationComponent"""

    def __init__(self, owner, rotation):
        """JERotationComponent creator"""
        super().__init__(f"JERotationComponent({owner.jeid})")
        self.add_parent(owner)
        owner.add_component(self)
        self._rotation = rotation

        def set_rotation(owner_self, rotation):
            self._rotation = rotation

        def update_rotation(owner_self, *, r = 0):
            self._rotation.x += r

        def get_rotation(owner_self):
            return self._rotation

        owner.set_rotation = set_rotation.__get__(owner, type(owner))
        owner.update_rotation = update_rotation.__get__(owner, type(owner))
        owner.get_rotation = get_rotation.__get__(owner, type(owner))

    @property
    def rotation(self):
        """Get rotation"""
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        """Set rotation"""
        self._rotation = rotation

    def __call__(self):
        """Get rotation"""
        return self._rotation

    def copy(self, new_owner):
        """Copy rotation"""
        return JERotationComponent(new_owner, _deepcopy(self._rotation))
