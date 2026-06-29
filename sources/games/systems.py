"""
    JarEngine - Python Game Engine Wrapper (Pygame-based)

    JarEngine is a lightweight game framework built on top of Pygame
    that simplifies usage while providing higher-level abstractions for
    game development and prototyping.

    Version: jarengine-v1.0.0
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

from sources.interns.high_classes import JEInternSystems as _JEInternSystems
from sources.interns.decorators import documentation as _documentation
from sources.interns import PGExtern as _PGExtern
from sources.entities.components_graphics import (
    JEFontComponent as _JEFontComponent,
    JETextComponent as _JETextComponent,
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
class JEMovementSystem(_JEInternSystems):
    """MovementSystem"""

    def __init__(self, owner: "JEGame"):
        """JEMovementSystem creator"""
        super().__init__(owner)
        self._required = [_JEPositionComponent, _JEVelocityComponent]

    def update(self, window, entity, entities, dt):
        """Update entity movement"""
        position = entity.get(_JEPositionComponent)
        velocity = entity.get(_JEVelocityComponent)

        position().x += velocity().x * dt
        position().y += velocity().y * dt

@_documentation
@_final
class JERenderSystem(_JEInternSystems):
    """MovementSystem"""

    def __init__(self, owner: "JEGame"):
        """JERenderSystem creator"""
        super().__init__(owner)
        self._required = [_JEPositionComponent]

    def update(self, window, entity, entities, dt):
        """Update entity rendering"""
        position = entity.get(_JEPositionComponent)

        size = entity.get(_JESizeComponent)
        rotation = entity.get(_JERotationComponent)
        flip = entity.get(_JEFlipComponent)
        color = entity.get(_JEColorComponent)
        visibility = entity.get(_JEVisibilityComponent)
        texture = entity.get(_JETextureComponent)
        text = entity.get(_JETextComponent)
        font = entity.get(_JEFontComponent)

        if not position:
            return

        if visibility and not visibility():
            return

        x = position().x
        y = position().y

        w = size().x if size else 20
        h = size().y if size else 20

        if text and font:
            surface = font().font.render(
                text(),
                True,
                color.rgba if color else (255, 255, 255, 255)
            )
            window.blit(surface, (x, y))

        if texture:
            surface = texture().surface

            if size:
                surface = _PGExtern.transform.scale(
                    surface,
                    (int(w), int(h))
                )

            if rotation:
                surface = _PGExtern.transform.rotate(
                    surface,
                    rotation()
                )

            if flip:
                surface = _PGExtern.transform.flip(
                    surface,
                    bool(flip()[0]),
                    bool(flip()[1])
                )

            if color:
                tint = surface.copy()
                tint.fill(color().rgba, special_flags=_PGExtern.BLEND_RGBA_MULT)
                surface = tint

            window.blit(surface, (x, y))
            return

        if color:
            _PGExtern.draw.rect(
                window.screen,
                color().rgba,
                (x, y, w, h)
            )

@_documentation
@_final
class JEAccelerationSystem(_JEInternSystems):
    """AccelerationSystem"""

    def __init__(self, owner: "JEGame"):
        """JEAccelerationSystem creator"""
        super().__init__(owner)
        self._required = [
            _JEAccelerationComponent,
            _JEVelocityComponent
        ]

    def update(self, window, entity, entities, dt):
        """Update entity acceleration"""

        acceleration = entity.get(_JEAccelerationComponent)
        velocity = entity.get(_JEVelocityComponent)
        mass = entity.get(_JEMassComponent)

        ax = acceleration().x
        ay = acceleration().y

        if mass and mass() > 0:
            ax /= mass()
            ay /= mass()

        velocity().x += ax * dt
        velocity().y += ay * dt