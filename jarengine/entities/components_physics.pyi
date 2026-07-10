from __future__ import annotations

from jarengine.interns.high_classes import JEInternEntityComponent
from jarengine.entities.entity import JEEntity
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
