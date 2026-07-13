from __future__ import annotations

from jarengine.interns.high_classes import JEInternSystems
from jarengine.entities.entity import JEEntity
from jarengine.systems.container import JEContainer
from jarengine.games.window import JEWindow
from jarengine.games.game import JEGame

class JEMovementSystem(JEInternSystems):
    def __init__(self, owner: JEGame):
        """
            JEMovementSystem

            Parameters:
                owner (JEGame): Game
        """
        ...
    def update(self, window: JEWindow, entity: JEEntity, entities: JEContainer[JEEntity], dt: float):
        """
            Update the movement of an entity

            Parameters:
                window (JEWindow): Window
                entity (JEEntity): Entity
                entities (JEContainer[JEEntity]): Other entities
                dt (float): Time
        """
        ...

class JEAccelerationSystem(JEInternSystems):
    def __init__(self, owner: JEGame):
        """
            JEAccelerationSystem

            Parameters:
                owner (JEGame): Game
        """
        ...
    def update(self, window: JEWindow, entity: JEEntity, entities: JEContainer[JEEntity], dt: float):
        """
            Update the acceleration of an entity

            Parameters:
                window (JEWindow): Window
                entity (JEEntity): Entity
                entities (JEContainer[JEEntity]): Other entities
                dt (float): Time
        """
        ...

class JERenderSystem(JEInternSystems):
    def __init__(self, owner: JEGame):
        """
            JERenderSystem

            Parameters:
                owner (JEGame): Game
        """
        ...
    def update(self, window: JEWindow, entity: JEEntity, entities: JEContainer[JEEntity], dt: float):
        """
            Update the rendering of an entity

            Parameters:
                window (JEWindow): Window
                entity (JEEntity): Entity
                entities (JEContainer[JEEntity]): Other entities
                dt (float): Time
        """
        ...
