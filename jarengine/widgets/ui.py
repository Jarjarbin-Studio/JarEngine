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
from jarengine.systems.vector import JEVector2D as _JEVector2D
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
from jarengine.widgets.graphics import JEText as _JEText

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
            _JEVector2D(size[0], size[1])
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

            checkbox = JECheckbox(checked=_JEBool(i == checked), color=color, checked_color=checked_color, outline_color=outline_color, outline_size=outline_size, name=f"{name}:Checkbox{i}", position=position, size=size, layer=layer, visibility=visibility)

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

        self._is_dragging = _JEBool(0)
        self._continuous_callback = _JEBool(0)
        self._callback = lambda value: None
        self._watcher = None
        self._release_watcher = None

        self._cursor = _JEWidget(name=f"{name}:Cursor", position=position, size=cursor_size, layer=layer + 1, visibility=visibility)

        _JEColorComponent(self._cursor, cursor_color)
        self.group_add(self._cursor)

        self._update_cursor()

    def on_parent_added(self, parent):
        if isinstance(parent, _JEGame):
            self._watcher = _JEMouseWatcher(
                _JEMse_Left,
                self._on_click
            )

            self._release_watcher = _JEMouseWatcher(
                _JEMse_Left,
                self._on_release,
                _JEBool(0)
            )

            parent.event.add(self._watcher)
            parent.event.add(self._release_watcher)

        super().on_parent_added(parent)

    def set_callback(self, callback, continuous_callback = _JEBool(1)):
        self._callback = callback
        self._continuous_callback = continuous_callback

    def set_value(self, value):

        self._value = max(
            self._minimum,
            min(self._maximum, value)
        )

        self._update_cursor()

        if self._callback and self._continuous_callback:
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

        size = self.get_size()
        cursor_size = self._cursor.get_size()

        self._cursor.set_position(
            _JEVector2D(
                size.x * ratio - cursor_size.x / 2,
                (size.y - cursor_size.y) / 2
            )
        )

    def _on_click(self, game, event):

        if not self.get_visibility():
            return

        mouse = game.input.mouse_pos()

        if self._is_cursor_hovered(mouse):
            self._is_dragging = _JEBool(1)
            return

        position = self.get_position()
        size = self.get_size()

        inside = (
                position.x <= mouse.x <= position.x + size.x
                and
                position.y <= mouse.y <= position.y + size.y
        )

        if inside:
            self._update_value_from_mouse(mouse)
            self._callback(self._value)

    def _on_release(self, game, event):
        if self._is_dragging and self._callback and not self._continuous_callback:
            self._callback(self._value)

        self._is_dragging = _JEBool(0)

    def _is_cursor_hovered(self, mouse):
        cursor_pos = self._cursor.get_position()
        slider_pos = self.get_position()

        cursor_world = _JEVector2D(
            slider_pos.x + cursor_pos.x,
            slider_pos.y + cursor_pos.y
        )

        cursor_size = self._cursor.get_size()

        return (
                cursor_world.x <= mouse.x <= cursor_world.x + cursor_size.x
                and
                cursor_world.y <= mouse.y <= cursor_world.y + cursor_size.y
        )

    def update(self, dt):
        if not self._is_dragging:
            return

        game = self.parents.get(_type=_JEGame)
        mouse = game.input.mouse_pos()

        self._update_value_from_mouse(mouse)

    def _update_value_from_mouse(self, mouse):
        position = self.get_position()
        size = self.get_size()

        local_x = mouse.x - position.x
        local_y = mouse.y - position.y

        ratio = local_x / size.x

        ratio = max(0, min(1, ratio))

        self.set_value(
            self._minimum +
            ratio * (self._maximum - self._minimum)
        )

@_documentation
class JEProgressBar(_JEWidget):
    def __init__(self, *, minimum = 0.0, maximum = 100.0, value = 0.0, color = _JEColor(100, 100, 100, 255), progress_color = _JEColor(255, 255, 255, 255), name = "JEProgressBar", position = _JEVector2D(0, 0), size = _JEVector2D(200, 20), rotation = 0.0, layer = 0, visibility = _JEBool(1)):
        super().__init__(name=name, position=position, size=size, rotation=rotation, layer=layer, visibility=visibility)

        _JEColorComponent(self, color)
        _JEGroupComponent(self)

        self._minimum = minimum
        self._maximum = maximum
        self._value = value

        self._progress = _JEWidget(name=f"{name}:Progress", position=_JEVector2D(0, 0), size=_JEVector2D(0, size.y), layer=layer + 1, visibility=visibility)

        _JEColorComponent(self._progress, progress_color)

        self.group_add(self._progress)

        self._update_progress()

    def set_value(self, value):
        self._value = max(
            self._minimum,
            min(self._maximum, value)
        )

        self._update_progress()

    def get_value(self):
        return self._value

    def set_range(self, minimum, maximum):
        self._minimum = minimum
        self._maximum = maximum

        self.set_value(self._value)

    def _update_progress(self):
        if self._maximum == self._minimum:
            ratio = 0
        else:
            ratio = (
                (self._value - self._minimum)
                /
                (self._maximum - self._minimum)
            )

        size = self.get_size()

        self._progress.set_size(
            _JEVector2D(
                size.x * ratio,
                size.y
            )
        )

@_documentation
class JEDropdown(_JEWidget):

    @_documentation
    class JEDropdownOption(_JEWidget):

        def __init__(self, index, text, font, callback, *, color=_JEColor(100, 100, 100, 255), text_color=_JEColor(255, 255, 255, 255), name="JEDropdownOption", position=_JEVector2D(0, 0), size=_JEVector2D(200, 30), rotation=0.0, layer=0, visibility=_JEBool(1)):
            super().__init__(
                name=name,
                position=position,
                size=size,
                rotation=rotation,
                layer=layer,
                visibility=visibility
            )

            _JEGroupComponent(self)

            self._index = index
            self._callback = callback

            self._rectangle = _JEWidget(
                name=f"{name}:Rectangle",
                position=_JEVector2D(0, 0),
                size=size,
                layer=layer,
                visibility=visibility
            )

            _JEColorComponent(self._rectangle, color)

            self._text = _JEText(
                text,
                font,
                color=text_color,
                name=f"{name}:Text",
                position=_JEVector2D(5, 0),
                size=size,
                layer=layer + 1,
                visibility=visibility
            )

            self._button = JEButton(
                color=_JEColor(0, 0, 0, 0),
                name=f"{name}:Button",
                position=_JEVector2D(0, 0),
                size=size,
                layer=layer + 2,
                visibility=visibility
            )

            self._button.set_callback(
                self._on_click
            )

            self.group_add(self._rectangle)
            self.group_add(self._text)
            self.group_add(self._button)

        def _on_click(self):
            if self._callback:
                self._callback(self._index)

    def __init__(self, options, font, *, selected = 0, color = _JEColor(100, 100, 100, 255), option_color = _JEColor(80, 80, 80, 255), text_color = _JEColor(255, 255, 255, 255), option_size = _JEVector2D(200, 30), name = "JEDropdown", position = _JEVector2D(0, 0), size = _JEVector2D(200, 30), rotation = 0.0, layer = 0, visibility = _JEBool(1)):

        super().__init__(name=name, position=position, size=size, rotation=rotation, layer=layer, visibility=visibility)

        _JEGroupComponent(self)

        self._options = options
        self._selected = selected
        self._open = _JEBool(0)

        self._callback = lambda index: None

        self._button = JEButton(
            color=color,
            name=f"{name}:Button",
            position=_JEVector2D(0, 0),
            size=size,
            layer=layer + 1,
            visibility=visibility
        )

        self._text = _JEText(
            options[selected],
            font,
            color=text_color,
            name=f"{name}:Text",
            position=_JEVector2D(5, 0),
            size=size,
            layer=layer + 2,
            visibility=visibility
        )

        self._button.set_callback(
            self.toggle
        )

        self._options_group = _JEWidget(
            name=f"{name}:Options",
            position=_JEVector2D(0, 0),
            size=_JEVector2D(0, 0),
            layer=layer + 10,
            visibility=_JEBool(0)
        )

        _JEGroupComponent(self._options_group)

        self.group_add(self._button)
        self.group_add(self._text)
        self.group_add(self._options_group)

        for index, option in enumerate(options):

            widget = JEDropdown.JEDropdownOption(
                index,
                option,
                font,
                self._select,
                color=option_color,
                text_color=text_color,
                name=f"{name}:Option{index}",
                position=_JEVector2D(
                    0,
                    size.y + index * option_size.y
                ),
                size=option_size,
                layer=layer + 10,
                visibility=visibility
            )

            self._options_group.group_add(widget)

    def on_parent_added(self, parent):
        if isinstance(parent, _JEGame):
            parent.add_entity(self._button)
            parent.add_entity(self._text)
            parent.add_entity(self._options_group)

        super().on_parent_added(parent)

    def set_callback(self, callback):
        self._callback = callback

    def set_selected(self, index):
        if index < 0 or index >= len(self._options):
            return

        self._selected = index

        self._text.set_text(
            self._options[index]
        )

    def get_selected(self):
        return self._selected

    def get_selected_text(self):
        return self._options[self._selected]

    def open(self):
        self._open = _JEBool(1)

        self._options_group.set_visibility(
            _JEBool(1)
        )

        for option in self._options_group.get_group():
            option.set_visibility(
                _JEBool(1)
            )

    def close(self):
        self._open = _JEBool(0)

        self._options_group.set_visibility(
            _JEBool(0)
        )

        for option in self._options_group.get_group():
            option.set_visibility(
                _JEBool(0)
            )

    @property
    def is_open(self):
        return self._open

    def set_visibility(self, visibility):
        self._set_visibility(visibility)

    def _set_visibility(self, visibility):
        self.get(_JEVisibilityComponent).visibility = visibility

        for child in self.get_group():
            child.set_visibility(visibility)

    def toggle(self):
        if self._open:
            self.close()
        else:
            self.open()

    def _select(self, index):
        self.set_selected(index)

        self.close()

        if self._callback:
            self._callback(index)
