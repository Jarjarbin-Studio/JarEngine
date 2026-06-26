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

from sources.entities.entity import JEEntity
from sources.systems.vector import JEVector2D

class JEAccelerationComponent:
    def __init__(self, owner: JEEntity, position: JEVector2D | tuple[int, int]) -> None: ...
    @property
    def acceleration(self) -> JEVector2D: ...
    @acceleration.setter
    def acceleration(self, position: JEVector2D | tuple[int, int]) -> None: ...
    def __call__(self) -> JEVector2D: ...
    def copy(self, new_owner: JEEntity) -> JEAccelerationComponent: ...

class JEMassComponent:
    def __init__(self, owner: JEEntity, size: float) -> None: ...
    @property
    def mass(self) -> float: ...
    @mass.setter
    def mass(self, rotation: float): ...
    def __call__(self) -> float: ...
    def copy(self, new_owner: JEEntity) -> JEMassComponent: ...
