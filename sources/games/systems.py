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
from sources.entities.components import (
    JEPositionComponent as _JEPositionComponent,
    JEVelocityComponent as _JEVelocityComponent,
    JETextureComponent as _JETextureComponent,
    JESizeComponent as _JESizeComponent
)
from sources.entities.entity import JEEntity as _JEEntity
from sources.systems.container import JEContainer as _JEContainer
from sources.interns.decorators import documentation as _documentation
from sources.games.window import JEWindow as _JEWindow
from sources.interns import PGIntern as _PGIntern

@_documentation
@_final
class JEMovementSystem(_JEInternalRenderingSystems):
    """MovementSystem"""

    @staticmethod
    def update(
            window: _JEWindow,
            entities: _JEContainer[_JEEntity],
            dt: float
        ) -> None:
        """Update entities"""
        for e in entities:
            position = e.get(_JEPositionComponent)()
            velocity = e.get(_JEVelocityComponent)()

            if position and velocity:
                position.x += velocity.x * dt
                position.y += velocity.y * dt

@_documentation
@_final
class JERenderSystem(_JEInternalRenderingSystems):
    """MovementSystem"""

    @staticmethod
    def update(
            window: _JEWindow,
            entities: _JEContainer[_JEEntity],
            dt: float
        ) -> None:
        """Update entities"""
        for e in entities:
            texture = e.get(_JETextureComponent)()
            position = e.get(_JEPositionComponent)()
            size = e.get(_JESizeComponent)()

            if not texture or not position:
                continue

            surface = texture.surface
            if size:
                surface = _PGIntern.transform.scale(
                    surface,
                    (int(size.x), int(size.y))
                )

            window.blit(surface, (position.x, position.y))
