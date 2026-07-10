"""
    JarEngine - Python Game Engine Wrapper (Pygame-based)

    JarEngine is a lightweight game framework built on top of Pygame
    that simplifies usage while providing higher-level abstractions for
    game development and prototyping.

    Version: jarengine-v1.6
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

from jarengine.interns.high_classes import JEInternSystems as _JEInternSystems
from jarengine.interns.decorators import documentation as _documentation
from jarengine.interns import PGExtern as _PGExtern
from jarengine.entities.entity import JEEntity as _JEEntity
from jarengine.entities.components_graphics import (
    JEFontComponent as _JEFontComponent,
    JETextComponent as _JETextComponent,
    JEFlipComponent as _JEFlipComponent,
    JELayerComponent as _JELayerComponent,
    JEVisibilityComponent as _JEVisibilityComponent,
    JETextureComponent as _JETextureComponent,
    JEColorComponent as _JEColorComponent,
    JEOutlineComponent as _JEOutlineComponent,
)
from jarengine.entities.components_transforms import (
    JEPositionComponent as _JEPositionComponent,
    JERotationComponent as _JERotationComponent,
    JEVelocityComponent as _JEVelocityComponent,
    JESizeComponent as _JESizeComponent,
)
from jarengine.entities.components_physics import (
    JEMassComponent as _JEMassComponent,
    JEAccelerationComponent as _JEAccelerationComponent,
)
from jarengine.entities.components_others import (
    JEGroupComponent as _JEGroupComponent,
)
from jarengine.entities.components_audios import (
    JEMusicComponent as _JEMusicComponent,
    JESoundComponent as _JESoundComponent,
)

@_documentation
@_final
class JEMovementSystem(_JEInternSystems):

    def __init__(self, owner):
        super().__init__(owner)
        self._required = [_JEPositionComponent, _JEVelocityComponent]

    def update(self, window, entity, entities, dt):
        position = entity.get(_JEPositionComponent)
        velocity = entity.get(_JEVelocityComponent)

        position().x += velocity().x * dt
        position().y += velocity().y * dt

@_documentation
@_final
class JEAccelerationSystem(_JEInternSystems):

    def __init__(self, owner):
        super().__init__(owner)
        self._required = [
            _JEAccelerationComponent,
            _JEVelocityComponent
        ]

    def update(self, window, entity, entities, dt):
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

@_documentation
@_final
class JERenderSystem(_JEInternSystems):

    def __init__(self, owner):
        super().__init__(owner)
        self._required = [_JEPositionComponent]

    def sort_cache(self):
        self.cache.sort(
            key=lambda entity:
            entity.get(_JELayerComponent)()
            if entity.get(_JELayerComponent)
            else 0
        )

    def _get_world_position(self, entity):
        position = entity.get(_JEPositionComponent)

        if not position:
            return 0, 0

        x = position().x
        y = position().y

        parent = entity.parents.get(_type=_JEEntity, default=None)

        if parent:
            px, py = self._get_world_position(parent)

            x += px
            y += py

        return x, y

    def _render_text(self, window, x, y, text, font, color, rotation, flip):
        lines = text().split("\n")

        color_value = (
            color().rgba
            if color
            else (255, 255, 255, 255)
        )

        line_height = font().font.get_linesize()

        for line in lines:
            surface = font().font.render(
                line,
                True,
                color_value
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

            window.blit(surface, (x, y))
            y += line_height

    def _render_texture(self, window, x, y, texture, size, rotation, flip, color):
            surface = texture().surface

            if size:
                surface = _PGExtern.transform.scale(
                    surface,
                    (int(size().x), int(size().y))
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
                tint.fill(
                    color().rgba,
                    special_flags=_PGExtern.BLEND_RGBA_MULT
                )
                surface = tint

            window.blit(surface, (x, y))

    def _render_rectangle(self, window, x, y, size, color, outline):
        rectangle = (x, y, int(size().x), int(size().y))

        if color:
            _PGExtern.draw.rect(
                window.screen,
                color().rgba,
                rectangle
            )

        if outline:
            _PGExtern.draw.rect(
                window.screen,
                outline()[0].rgba,
                rectangle,
                outline()[1]
            )

    def update(self, window, entity, entities, dt):
        position = entity.get(_JEPositionComponent)

        size = entity.get(_JESizeComponent)
        rotation = entity.get(_JERotationComponent)
        flip = entity.get(_JEFlipComponent)
        color = entity.get(_JEColorComponent)
        visibility = entity.get(_JEVisibilityComponent)
        texture = entity.get(_JETextureComponent)
        text = entity.get(_JETextComponent)
        font = entity.get(_JEFontComponent)
        outline = entity.get(_JEOutlineComponent)

        if visibility and not visibility():
            return

        x, y = self._get_world_position(entity)

        if text and font:
            self._render_text(window, x, y, text, font, color, rotation, flip)
        elif texture:
            self._render_texture(window, x, y, texture, size, rotation, flip, color)
        elif size and (color or outline):
            self._render_rectangle(window, x, y, size, color, outline)
