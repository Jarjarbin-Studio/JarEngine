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

from typing import (
    final as _final
)

from sources.games.window import JEWindow as _JEWindow
from sources.graphics.sprite import JESprite as _JESprite
from sources.interns.base_classe import JEInternClassBase as _JEInternClassBase
from sources.interns.decorators import documentation as _documentation

@_documentation
@_final
class JERenderer(_JEInternClassBase):
    """Rendering functions"""

    def __init__(
            self,
            window: _JEWindow
        ):
        """JERenderer creator"""
        super().__init__()
        self.window = window

    def draw_sprite(
            self,
            sprite: _JESprite
        ):
        """Draw sprite"""
        self.window.screen.blit(sprite.surface, sprite.rect)
