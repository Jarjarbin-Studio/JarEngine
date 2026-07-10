from __future__ import annotations

from jarengine.interns.high_classes import JEInternEntityComponent
from jarengine.entities.entity import JEEntity
from jarengine.systems.vector import JEVector2D

class JEPositionComponent(JEInternEntityComponent):
    def __init__(self, owner: JEEntity, position: JEVector2D | tuple[float, float]):
        """
            JEPositionComponent

            Parameters:
                owner (JEEntity): owner of the component
                position (JEVector2D | tuple[float, float]): position
        """
        ...
    @property
    def position(self) -> JEVector2D: ...
    @position.setter
    def position(self, position: JEVector2D | tuple[float, float]): ...
    def __call__(self) -> JEVector2D: ...
    def copy(self, new_owner: JEEntity) -> JEPositionComponent: ...

class JEVelocityComponent(JEInternEntityComponent):
    def __init__(self, owner: JEEntity, velocity: JEVector2D | tuple[float, float]):
        """
            JEVelocityComponent

            Parameters:
                owner (JEEntity): owner of the component
                velocity (JEVector2D | tuple[float, float]): velocity
        """
        ...
    @property
    def velocity(self) -> JEVector2D: ...
    @velocity.setter
    def velocity(self, velocity: JEVector2D | tuple[float, float]): ...
    def __call__(self) -> JEVector2D: ...
    def copy(self, new_owner: JEEntity) -> JEVelocityComponent: ...

class JESizeComponent(JEInternEntityComponent):
    def __init__(self, owner: JEEntity, size: JEVector2D | tuple[float, float]):
        """
            JESizeComponent

            Parameters:
                owner (JEEntity): owner of the component
                size (JEVector2D | tuple[float, float]): size
        """
        ...
    @property
    def size(self) -> JEVector2D: ...
    @size.setter
    def size(self, size: JEVector2D | tuple[float, float]): ...
    def __call__(self) -> JEVector2D: ...
    def copy(self, new_owner: JEEntity) -> JESizeComponent: ...

class JERotationComponent(JEInternEntityComponent):
    def __init__(self, owner: JEEntity, rotation: float):
        """
            JERotationComponent

            Parameters:
                owner (JEEntity): owner of the component
                rotation (float): rotation
        """
        ...
    @property
    def rotation(self) -> float: ...
    @rotation.setter
    def rotation(self, rotation: float): ...
    def __call__(self) -> float: ...
    def copy(self, new_owner: JEEntity) -> JERotationComponent: ...
