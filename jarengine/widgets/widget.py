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

from jarengine.entity.entity import JEEntity as _JEEntity
from jarengine.systems.bool import JEBool as _JEBool
from jarengine.entity.components_transforms import (
    JEPositionComponent as _JEPositionComponent,
    JESizeComponent as _JESizeComponent,
    JERotationComponent as _JERotationComponent
)
from jarengine.entity.components_graphics import (
    JEVisibilityComponent as _JEVisibilityComponent,
    JELayerComponent as _JELayerComponent
)
from jarengine.systems.vector import JEVector2D as _JEVector2D
from jarengine.interns.decorators import documentation as _documentation

@_documentation
class JEWidget(_JEEntity):

    def __init__(self, *, name = "JEWidget", position = _JEVector2D(0, 0), size = _JEVector2D(0, 0), rotation = 0.0, layer = 0, visibility = _JEBool(1)):
        super().__init__(name=name)

        _JEPositionComponent(self, position)
        _JESizeComponent(self, size)
        _JERotationComponent(self, rotation)
        _JELayerComponent(self, layer)
        _JEVisibilityComponent(self, visibility)

    def copy(self):
        return super().copy()
