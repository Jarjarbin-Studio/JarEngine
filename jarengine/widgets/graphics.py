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

from jarengine.systems.bool import JEBool as _JEBool
from jarengine.widgets.widget import JEWidget as _JEWidget
from jarengine.entity.components_graphics import (
    JETextComponent as _JETextComponent,
    JEFontComponent as _JEFontComponent,
    JEColorComponent as _JEColorComponent,
    JETextureComponent as _JETextureComponent,
    JEFlipComponent as _JEFlipComponent
)
from jarengine.systems.vector import JEVector2D as _JEVector2D
from jarengine.interns.decorators import documentation as _documentation

@_documentation
class JESprite(_JEWidget):

    def __init__(self, texture, *, flip = (_JEBool(0), _JEBool(0)), name = "JESprite", position = _JEVector2D(0, 0), size = _JEVector2D(0, 0), rotation = 0.0, layer = 0, visibility = _JEBool(1)):
        super().__init__(name=name, position=position, size=size, rotation=rotation, layer=layer, visibility=visibility)

        _JETextureComponent(self, texture)
        _JEFlipComponent(self, flip)

@_documentation
class JEText(_JEWidget):

    def __init__(self, text, font, *, color = None, flip = (_JEBool(0), _JEBool(0)), name = "JESprite", position = _JEVector2D(0, 0), size = _JEVector2D(0, 0), rotation = 0.0, layer = 0, visibility = _JEBool(1)):
        super().__init__(name=name, position=position, size=size, rotation=rotation, layer=layer, visibility=visibility)

        _JETextComponent(self, text)
        _JEFontComponent(self, font)
        _JEFlipComponent(self, flip)
        if color:
            _JEColorComponent(self, color)
