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

from typing import final as _final

from sources.interns.high_classes import JEInternalRenderingSystems as _JEInternalRenderingSystems
from sources.interns.decorators import documentation as _documentation
from sources.interns import PGIntern as _PGIntern
from sources.entities.components_graphics import (
    JEFlipComponent as _JEFlipComponent,
    JELayerComponent as _JELayerComponent,
    JEVisibilityComponent as _JEVisibilityComponent,
    JETextureComponent as _JETextureComponent,
    JEColorComponent as _JEColorComponent
)
from sources.entities.components_transforms import (
    JEPositionComponent as _JEPositionComponent,
    JERotationComponent as _JERotationComponent,
    JEVelocityComponent as _JEVelocityComponent,
    JESizeComponent as _JESizeComponent
)
from sources.entities.components_physics import (
    JEMassComponent as _JEMassComponent,
    JEAccelerationComponent as _JEAccelerationComponent
)

@_documentation
@_final
class JEMovementSystem(_JEInternalRenderingSystems):
    """MovementSystem"""

    def __init__(self, owner: "JEGame"):
        super().__init__(owner)
        self._required = [_JEPositionComponent, _JEVelocityComponent]

    def update(self, window, entity, entities, dt):
        """Update entities"""
        position = entity.get(_JEPositionComponent)
        velocity = entity.get(_JEVelocityComponent)

        position().x += velocity().x * dt
        position().y += velocity().y * dt

@_documentation
@_final
class JERenderSystem(_JEInternalRenderingSystems):
    """MovementSystem"""

    def __init__(self, owner: "JEGame"):
        super().__init__(owner)
        self._required = [_JETextureComponent, _JEPositionComponent]

    def update(self, window, entity, entities, dt):
        """Update entities"""
        texture = entity.get(_JETextureComponent)
        position = entity.get(_JEPositionComponent)
        size = entity.get(_JESizeComponent)

        surface = texture().surface
        if size:
            surface = _PGIntern.transform.scale(
                surface,
                (int(size().x), int(size().y))
            )

        window.blit(surface, (position().x, position().y))
