from __future__ import annotations

from jarengine.interns.high_classes import JEInternEntityComponent
from jarengine.entities.entity import JEEntity
from jarengine.systems.container import JEContainer

class JEGroupComponent(JEInternEntityComponent):
    def __init__(self, owner: JEEntity):
        """
            JEGroupComponent

            Parameters:
                owner (JEEntity): owner of the component
        """
        ...
    @property
    def group(self) -> JEContainer: ...
    @group.setter
    def group(self, entity: JEEntity): ...
    def group_remove(self, entity: JEEntity): ...
    def __call__(self) -> JEContainer: ...
    def copy(self, new_owner: JEEntity) -> JEGroupComponent: ...
