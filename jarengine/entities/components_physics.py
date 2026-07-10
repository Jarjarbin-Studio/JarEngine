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

from copy import deepcopy as _deepcopy
from typing import final as _final

from jarengine.interns.high_classes import JEInternEntityComponent as _JEInternEntityComponent
from jarengine.interns.decorators import documentation as _documentation
from jarengine.systems.vector import JEVector2D as _JEVector2D

@_documentation
@_final
class JEAccelerationComponent(_JEInternEntityComponent):
    """AccelerationComponent"""

    def __init__(self, owner, acceleration):
        super().__init__(owner, JEAccelerationComponent)
        self._acceleration = (
            acceleration
            if isinstance(acceleration, _JEVector2D) else
            _JEVector2D(*acceleration)
        )

        def set_acceleration(owner_self, acceleration):
            self.acceleration =  acceleration

        def update_acceleration(owner_self, *, x = 0, y = 0):
            self._acceleration.x += x
            self._acceleration.y += y

        def get_acceleration(owner_self):
            return self.acceleration

        owner.set_acceleration = set_acceleration.__get__(owner, type(owner))
        owner.update_acceleration = update_acceleration.__get__(owner, type(owner))
        owner.get_acceleration = get_acceleration.__get__(owner, type(owner))

    @property
    def acceleration(self):
        return self._acceleration

    @acceleration.setter
    def acceleration(self, acceleration):
        self._acceleration = (
            acceleration
            if isinstance(acceleration, _JEVector2D) else
            _JEVector2D(*acceleration)
        )

    def __call__(self):
        return self._acceleration

    def copy(self, new_owner):
        return JEAccelerationComponent(new_owner, _deepcopy(self._acceleration))

@_documentation
@_final
class JEMassComponent(_JEInternEntityComponent):

    def __init__(self, owner, mass):
        super().__init__(owner, JEMassComponent)
        self._mass = mass

        def set_mass(owner_self, mass):
            self.mass = mass

        def update_mass(owner_self, *, m = 0):
            self._mass += m

        def get_mass(owner_self):
            return self.mass

        owner.set_mass = set_mass.__get__(owner, type(owner))
        owner.update_mass = update_mass.__get__(owner, type(owner))
        owner.get_mass = get_mass.__get__(owner, type(owner))

    @property
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, mass):
        self._mass = mass

    def __call__(self):
        return self._mass

    def copy(self, new_owner):
        return JEMassComponent(new_owner, _deepcopy(self._mass))
