# =============================================================================
# JarEngine - Python Game Engine Wrapper (Pygame-based)
# =============================================================================
#
# JarEngine is a lightweight game framework built on top of Pygame
# that simplifies usage while providing higher-level abstractions for
# game development and prototyping.
#
# =============================================================================
# Version: jarengine-v1.7
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

from jarengine.interns.high_classes import JEInternEntityComponent
from jarengine.entity.entity import JEEntity
from jarengine.systems.vector import JEVector2D

class JEAccelerationComponent(JEInternEntityComponent):
    def __init__(self, owner: JEEntity, acceleration: JEVector2D | tuple[float, float]):
        """
            JEAccelerationComponent

            Parameters:
                owner (JEEntity): owner of the component
                acceleration (JEVector2D | tuple[float, float]): acceleration
        """
        ...
    @property
    def acceleration(self) -> JEVector2D: ...
    @acceleration.setter
    def acceleration(self, acceleration: JEVector2D | tuple[float, float]): ...
    def __call__(self) -> JEVector2D: ...
    def copy(self, new_owner: JEEntity) -> JEAccelerationComponent: ...

class JEMassComponent(JEInternEntityComponent):
    def __init__(self, owner: JEEntity, mass: float):
        """
            JEMassComponent

            Parameters:
                owner (JEEntity): owner of the component
                mass (float): mass of the component
        """
        ...
    @property
    def mass(self) -> float: ...
    @mass.setter
    def mass(self, mass: float): ...
    def __call__(self) -> float: ...
    def copy(self, new_owner: JEEntity) -> JEMassComponent: ...
