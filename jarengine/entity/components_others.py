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

from jarengine.interns.helpers import (
    assertion_type as _assertion_type,
    safe_cast as _safe_cast
)
from jarengine.interns.high_classes import JEInternEntityComponent as _JEInternEntityComponent
from jarengine.interns.decorators import documentation as _documentation
from jarengine.entity.entity import JEEntity as _JEEntity
import jarengine.interns.log as _log

@_documentation
@_final
class JEGroupComponent(_JEInternEntityComponent):

    def __init__(self, owner):

        _assertion_type(owner, _JEEntity, "owner must be of type 'JEEntity'", True)

        super().__init__(owner, JEGroupComponent)

        def group_add(owner_self, entity):

            _assertion_type(entity, _JEEntity, "entity must be of type 'JEEntity'", True)

            self.group = entity

        def group_remove(owner_self, entity):

            _assertion_type(entity, _JEEntity, "entity must be of type 'JEEntity'", True)

            self.group_remove(entity)

        def get_group(owner_self):
            return self.group

        owner.group_add = group_add.__get__(owner, type(owner))
        owner.group_remove = group_remove.__get__(owner, type(owner))
        owner.get_group = get_group.__get__(owner, type(owner))

        _log.log("DEBUG", "OBJECT", f"JEGroupComponent: Created", self.jeid, owner)

    @property
    def group(self):
        return self.children

    @group.setter
    def group(self, entity):
        self.children.add(entity)
        entity.add_parent(self.parents.get(_type=_JEEntity))

    def group_remove(self, entity):
        self.children.rm(instance=entity)
        entity.parents.rm(instance=self.parents.get(_type=_JEEntity))

    def __call__(self):
        return self.children

    def copy(self, new_owner):
        new_group = JEGroupComponent(new_owner)
        for e in self.children:
            new_group.group = _deepcopy(e)

        _log.log("DEBUG", "ENTITY", f"JEGroupComponent: Copied", self.jeid, new_owner)

        return new_group
