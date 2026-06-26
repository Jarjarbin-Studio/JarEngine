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

from copy import deepcopy as _deepcopy
from typing import final as _final

from sources.interns.high_classes import JEInternalEntityComponent as _JEInternalEntityComponent
from sources.interns.decorators import documentation as _documentation
from sources.systems.color import JEColor as _JEColor
from sources.systems.bool import JEBool as _JEBool

@_documentation
@_final
class JETextureComponent(_JEInternalEntityComponent):
    """TextureComponent"""

    def __init__(self, owner, texture):
        """JETextureComponent creator"""
        super().__init__(f"JETextureComponent({owner.jeid})")
        self.add_parent(owner)
        owner.add_component(self)
        self._texture = texture

        def set_texture(owner_self, texture):
            self._texture = texture

        def get_texture(owner_self):
            return self._texture

        owner.set_texture = set_texture.__get__(owner, type(owner))
        owner.get_texture = get_texture.__get__(owner, type(owner))

    @property
    def texture(self):
        """Get texture"""
        return self._texture

    @texture.setter
    def texture(self, texture):
        """Set texture"""
        self._texture = texture

    def __call__(self):
        """Get texture"""
        return self._texture

    def copy(self, new_owner):
        """Copy texture"""
        return JETextureComponent(new_owner, _deepcopy(self._texture))

@_documentation
@_final
class JEColorComponent(_JEInternalEntityComponent):
    """ColorComponent"""

    def __init__(self, owner, color):
        """JEColorComponent creator"""
        super().__init__(f"JEColorComponent({owner.jeid})")
        self.add_parent(owner)
        owner.add_component(self)
        self._color = (
            color
            if isinstance(color, _JEColor) else
            _JEColor(*color)
        )

        def set_color(owner_self, color):
            self._color = (
                color
                if isinstance(color, _JEColor) else
                _JEColor(*color)
            )

        def update_color(owner_self, *, x = 0, y = 0):
            self._color.x += x
            self._color.y += y

        def get_color(owner_self):
            return self._color

        owner.set_color = set_color.__get__(owner, type(owner))
        owner.update_color = update_color.__get__(owner, type(owner))
        owner.get_color = get_color.__get__(owner, type(owner))

    @property
    def color(self):
        """Get color"""
        return self._color

    @color.setter
    def color(self, color):
        """Set color"""
        self._color = (
            color
            if isinstance(color, _JEColor) else
            _JEColor(*color)
        )

    def __call__(self):
        """Get color"""
        return self._color

    def copy(self, new_owner):
        """Copy color"""
        return JEColorComponent(new_owner, _deepcopy(self._color))

@_documentation
@_final
class JEVisibilityComponent(_JEInternalEntityComponent):
    """VisibilityComponent"""

    def __init__(self, owner, visibility):
        """JEVisibilityComponent creator"""
        super().__init__(f"JEVisibilityComponent({owner.jeid})")
        self.add_parent(owner)
        owner.add_component(self)
        self._visibility = visibility

        def set_visibility(owner_self, visibility):
            self._visibility = visibility

        def update_visibility(owner_self, *, v = _JEBool(1)):
            self._visibility.x += v

        def get_visibility(owner_self):
            return self._visibility

        owner.set_visibility = set_visibility.__get__(owner, type(owner))
        owner.update_visibility = update_visibility.__get__(owner, type(owner))
        owner.get_visibility = get_visibility.__get__(owner, type(owner))

    @property
    def visibility(self):
        """Get visibility"""
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Set visibility"""
        self._visibility = visibility

    def __call__(self):
        """Get visibility"""
        return self._visibility

    def copy(self, new_owner):
        """Copy visibility"""
        return JEVisibilityComponent(new_owner, _deepcopy(self._visibility))

@_documentation
@_final
class JELayerComponent(_JEInternalEntityComponent):
    """LayerComponent"""

    def __init__(self, owner, layer):
        """JELayerComponent creator"""
        super().__init__(f"JELayerComponent({owner.jeid})")
        self.add_parent(owner)
        owner.add_component(self)
        self._layer = layer

        def set_layer(owner_self, layer):
            self._layer = layer

        def update_layer(owner_self, *, l = 0):
            self._layer.x += l

        def get_layer(owner_self):
            return self._layer

        owner.set_layer = set_layer.__get__(owner, type(owner))
        owner.update_layer = update_layer.__get__(owner, type(owner))
        owner.get_layer = get_layer.__get__(owner, type(owner))

    @property
    def layer(self):
        """Get layer"""
        return self._layer

    @layer.setter
    def layer(self, layer):
        """Set layer"""
        self._layer = layer

    def __call__(self):
        """Get layer"""
        return self._layer

    def copy(self, new_owner):
        """Copy layer"""
        return JELayerComponent(new_owner, _deepcopy(self._layer))

@_documentation
@_final
class JEFlipComponent(_JEInternalEntityComponent):
    """FlipComponent"""

    def __init__(self, owner, flip):
        """JEFlipComponent creator"""
        super().__init__(f"JEFlipComponent({owner.jeid})")
        self.add_parent(owner)
        owner.add_component(self)
        self._flip = flip

        def set_flip(owner_self, flip):
            self._flip = flip

        def get_flip(owner_self):
            return self._flip

        owner.set_flip = set_flip.__get__(owner, type(owner))
        owner.get_flip = get_flip.__get__(owner, type(owner))

    @property
    def flip(self):
        """Get flip"""
        return self._flip

    @flip.setter
    def flip(self, flip):
        """Set flip"""
        self._flip = flip

    def __call__(self):
        """Get flip"""
        return self._flip

    def copy(self, new_owner):
        """Copy flip"""
        return JELayerComponent(new_owner, _deepcopy(self._flip))
