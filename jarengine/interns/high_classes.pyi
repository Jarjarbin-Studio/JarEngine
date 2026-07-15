from __future__ import annotations

from typing import Any

from jarengine.interns.low_classes import JEInternGraphic
from jarengine.entities.entity import JEEntity
from jarengine.games.game import JEGame
from jarengine.games.window import JEWindow
from jarengine.interns.base_classe import JEInternBaseClass
from jarengine.systems.container import JEContainer
from jarengine.systems.bool import JEBool


class JEInternOwnership(JEInternBaseClass):
    def __init__(self):
        """
            JEInternOwnership
        """
        ...
    @property
    def parents(self) -> JEContainer[JEInternBaseClass]:
        """
            Object's parents

            Returns:
                JEContainer[JEInternBaseClass]: Parents
        """
        ...
    def add_parent(self, parent: JEInternBaseClass):
        """
            Add a parent to the object
            
            Parameters:
                parent (JEInternBaseClass): Parent
        """
        ...
    @property
    def children(self) -> JEContainer[JEInternBaseClass]:
        """
            Object's children

            Returns:
                JEContainer[JEInternBaseClass]: Children
        """
        ...
    def add_child(self, child: JEInternBaseClass):
        """
            Add a child to the object

            Parameters:
                child (JEInternBaseClass): Child
        """
        ...

class JEInternEntityComponent(JEInternGraphic, JEInternOwnership):
    def __init__(self, owner: JEEntity, _type: type):
        """
            JEInternEntityComponent
            
            Parameters:
                owner (JEEntity): Entity
                _type (type): Component type
        """
        ...
    def __call__(self) -> Any:
        """
            Get the internal value(s) of the component

            Returns:
                Any: Internal value(s)
        """
        ...

class JEInternSystems(JEInternOwnership):
    cache: list[JEEntity]   #Per-system entity cache (faster computation)
    def __init__(self, owner: JEGame):
        """
            JEInternSystems

            Parameters:
                owner (JEGame): Game
        """
        ...
    def refresh(self):
        """
            Refresh the entity cache (high cost on the CPU)
        """
        ...
    def sort_cache(self):
        """
            Sort the entity cache
        """
        ...
    def accepts(self, components: JEContainer[JEInternEntityComponent]) -> JEBool:
        """
            Check if an entity has the required components to run the system (using its component container)
            
            Parameters:
                components (JEContainer[JEInternEntityComponent]): Entity's components
            
            Returns:
                JEBool: Whether the entity has the required components
        """
        ...
    @staticmethod
    def update(window: JEWindow, entity: JEEntity, entities: JEContainer[JEEntity], dt: float):
        """
            Update the system
            
            Parameters:
                window (JEWindow): Window
                entity (JEEntity): Entity
                entities (JEContainer[JEEntity]): Every entity
                dt (float): Time
        """
        ...
