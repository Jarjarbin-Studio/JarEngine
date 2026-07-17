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

from jarengine.interns.high_classes import JEInternEntityComponent
from jarengine.entity.entity import JEEntity
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
