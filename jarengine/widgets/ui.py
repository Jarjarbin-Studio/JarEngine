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
    JEOutlineComponent as _JEOutlineComponent,
    JEVisibilityComponent as _JEVisibilityComponent
)
from jarengine.entity.components_others import JEGroupComponent as _JEGroupComponent
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
        if not self.get_visibility():
            return

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
        if not self.get_visibility():
            return

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
        if not self.get_visibility():
            return

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

@_documentation
class JERadio(_JEWidget):

    def __init__(self, positions, *, checked = 0, color = _JEColor(100, 100, 100, 255), checked_color = _JEColor(100, 255, 100, 255), outline_color = None, outline_size = None, size = _JEVector2D(30, 30), name = "JERadio", rotation = 0.0, layer = 0, visibility = _JEBool(1)):
        super().__init__(name=name, position=_JEVector2D(0, 0), size=_JEVector2D(0, 0), rotation=rotation, layer=layer, visibility=visibility)

        _JEGroupComponent(self)

        self._selected = checked
        self._callback = lambda index: None

        for i, position in enumerate(positions):

            checkbox = JECheckbox(checked=_JEBool(i == checked), color=color, checked_color=checked_color, outline_color=outline_color, outline_size=outline_size, name=f"{name}:{i}", position=position, size=size, layer=layer, visibility=visibility)

            checkbox.set_callback(
                lambda state, index=i: self._on_checkbox(index, state)
            )

            self.group_add(checkbox)

        def set_visibility(self, visibility):
            self._set_visibility(visibility)

        self.set_visibility = set_visibility.__get__(self, type(self))

    def on_parent_added(self, parent):

        if isinstance(parent, _JEGame):

            for checkbox in self.get_group():
                parent.add_entity(checkbox)

        super().on_parent_added(parent)

    def set_callback(self, callback):
        self._callback = callback

    def get_selected(self):
        return self._selected

    def set_selected(self, index):
        for i, checkbox in enumerate(self.get_group()):
            checkbox.set_checked(
                _JEBool(i == index)
            )

    def _set_visibility(self, visibility):
        self.get(_JEVisibilityComponent).visibility = visibility

        for checkbox in self.get_group():
            checkbox.set_visibility(visibility)

    def _on_checkbox(self, index, checked):

        if not self.get_visibility():
            return

        if index == self._selected:
            self.get_group()[index].set_checked(_JEBool(1))
            return

        for i, checkbox in enumerate(self.get_group()):
            checkbox.set_checked(
                _JEBool(i == index)
            )

        self._selected = index

        if self._callback:
            self._callback(index)

@_documentation
class JESlider(_JEWidget):

    def __init__(self, *, minimum = 0.0, maximum = 100.0, value = 0.0, color = _JEColor(100, 100, 100, 255), cursor_color = _JEColor(255, 255, 255, 255), cursor_size = _JEVector2D(20, 40), name = "JESlider", position = _JEVector2D(0, 0), size = _JEVector2D(200, 10), rotation = 0.0, layer = 0, visibility = _JEBool(1)):
        super().__init__(name=name, position=position, size=size, rotation=rotation, layer=layer, visibility=visibility)

        _JEColorComponent(self, color)
        _JEGroupComponent(self)

        self._minimum = minimum
        self._maximum = maximum
        self._value = value

        self._callback = lambda value: None
        self._watcher = None

        self._cursor = _JEWidget(name="JESliderCursor",
            position=position,
            size=cursor_size,
            layer=layer + 1,
            visibility=visibility
        )

        _JEColorComponent(self._cursor, cursor_color)
        self.group_add(self._cursor)

        self._update_cursor()

    def on_parent_added(self, parent):
        if isinstance(parent, _JEGame):

            self._watcher = _JEMouseWatcher(
                _JEMse_Left,
                self._on_click
            )

            parent.event.add(self._watcher)
            parent.add_entity(self._cursor)

        super().on_parent_added(parent)

    def set_callback(self, callback):
        self._callback = callback

    def set_value(self, value):

        self._value = max(
            self._minimum,
            min(self._maximum, value)
        )

        self._update_cursor()

        if self._callback:
            self._callback(self._value)

    def get_value(self):
        return self._value

    def set_range(self, minimum, maximum):
        self._minimum = minimum
        self._maximum = maximum

        self.set_value(self._value)

    def _update_cursor(self):
        if self._maximum == self._minimum:
            ratio = 0
        else:
            ratio = (self._value - self._minimum) / (self._maximum - self._minimum)

        position = self.get_position()
        size = self.get_size()
        cursor_size = self._cursor.get_size()

        self._cursor.set_position(
            _JEVector2D(
                position.x + size.x * ratio,
                position.y + (size.y - cursor_size.y) / 2
            )
        )

    def _on_click(self, game, event):
        if not self.get_visibility():
            return

        mouse = game.input.mouse_pos()

        position = self.get_position()
        size = self.get_size()

        inside = (
            position.x <= mouse.x <= position.x + size.x
            and
            position.y <= mouse.y <= position.y + size.y
        )

        if inside:
            ratio = (mouse.x - position.x) / size.x

            self.set_value(self._minimum + ratio * (self._maximum - self._minimum))
