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

from jarengine.games.game import JEGame as _JEGame
from jarengine.systems.bool import JEBool as _JEBool
from jarengine.widgets.widget import JEWidget as _JEWidget
from jarengine.systems.vector import JEVector2D as _JEVector2D, JEVector2D
from jarengine.systems.color import JEColor as _JEColor
from jarengine.interns.decorators import documentation as _documentation
from jarengine.entity.components_graphics import (
    JEFlipComponent as _JEFlipComponent,
    JETextureComponent as _JETextureComponent,
    JEColorComponent as _JEColorComponent,
    JEOutlineComponent as _JEOutlineComponent
)
from jarengine.events.mouse import JEMouseWatcher as _JEMouseWatcher
from jarengine.constants import JEMse_Left as _JEMse_Left

@_documentation
class JEButton(_JEWidget):

    def __init__(self, *, color = _JEColor(100, 100, 100, 255), outline_color = None, outline_size = None, name = "JEButton", position = _JEVector2D(0, 0), size = _JEVector2D(0, 0), rotation = 0.0, layer = 0, visibility = _JEBool(1)):
        super().__init__(name=name, position=position, size=size, rotation=rotation, layer=layer, visibility=visibility)

        _JEColorComponent(self, color)

        if outline_color and outline_size:
            _JEOutlineComponent(self, (outline_color, outline_size))

        self._callback = lambda: None
        self._watcher = None

    def on_parent_added(self, parent):
        if isinstance(parent, _JEGame):
            self._watcher = _JEMouseWatcher(
                _JEMse_Left,
                self._on_click
            )
            parent.event.add(self._watcher)

        super().on_parent_added(parent)

    def set_callback(self, callback):
        self._callback = callback

    def _on_click(self, game, event):
        mouse = game.input.mouse_pos()
        position = self.get_position()
        size = self.get_size()
        inside = (
            position.x <= mouse.x <= position.x + size.x
            and
            position.y <= mouse.y <= position.y + size.y
        )

        if inside and self._callback:
            self._callback()

@_documentation
class JEImageButton(_JEWidget):

    def __init__(self, texture, *, flip = (_JEBool(0), _JEBool(0)), color = None, outline_color = None, outline_size = None, name = "JEImageButton", position = _JEVector2D(0, 0), size = _JEVector2D(0, 0), rotation = 0.0, layer = 0, visibility = _JEBool(1)):
        size = (
            JEVector2D(size[0], size[1])
            if isinstance(size, tuple) else
            size
        )
        if size.x == 0 and size.y == 0:
            size = texture.size

        super().__init__(name=name, position=position, size=size, rotation=rotation, layer=layer, visibility=visibility)

        _JETextureComponent(self, texture)
        _JEFlipComponent(self, flip)

        if color:
            _JEColorComponent(self, color)

        if outline_color and outline_size:
            _JEOutlineComponent(self, (outline_color, outline_size))

        self._callback = lambda: None
        self._watcher = None

    def on_parent_added(self, parent):
        if isinstance(parent, _JEGame):
            self._watcher = _JEMouseWatcher(
                _JEMse_Left,
                self._on_click
            )
            parent.event.add(self._watcher)

        super().on_parent_added(parent)

    def set_callback(self, callback):
        self._callback = callback

    def _on_click(self, game, event):
        mouse = game.input.mouse_pos()
        position = self.get_position()
        size = self.get_size()
        inside = (
            position.x <= mouse.x <= position.x + size.x
            and
            position.y <= mouse.y <= position.y + size.y
        )

        if inside and self._callback:
            self._callback()

@_documentation
class JECheckbox(_JEWidget):

    def __init__(self, *, checked = _JEBool(0), color = _JEColor(100, 100, 100, 255), checked_color = _JEColor(100, 255, 100, 255), outline_color = None, outline_size = None, name = "JECheckbox", position = _JEVector2D(0, 0), size = _JEVector2D(30, 30), rotation = 0.0, layer = 0, visibility = _JEBool(1)):
        super().__init__(name=name, position=position, size=size, rotation=rotation, layer=layer, visibility=visibility)

        _JEColorComponent(self, checked_color if checked else color)

        if outline_color and outline_size:
            _JEOutlineComponent(self, outline_color, outline_size)

        self._checked = checked
        self._color = color
        self._checked_color = checked_color

        self._callback = lambda value: None
        self._watcher = None

    def on_parent_added(self, parent):
        if isinstance(parent, _JEGame):
            self._watcher = _JEMouseWatcher(
                _JEMse_Left,
                self._on_click
            )
            parent.event.add(self._watcher)

        super().on_parent_added(parent)

    def set_callback(self, callback):
        self._callback = callback

    def set_checked(self, checked):
        self._checked = checked

        color = (
            self._checked_color
            if checked else
            self._color
        )

        self.set_color(color)

    def is_checked(self):
        return self._checked

    def toggle(self):
        self.set_checked(self._checked())

    def _on_click(self, game, event):
        mouse = game.input.mouse_pos()

        position = self.get_position()
        size = self.get_size()

        inside = (
            position.x <= mouse.x <= position.x + size.x
            and
            position.y <= mouse.y <= position.y + size.y
        )

        if inside:
            self.toggle()

            if self._callback:
                self._callback(self._checked)
