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

from copy import deepcopy as _deepcopy
from typing import final as _final

from jarengine.interns.high_classes import JEInternEntityComponent as _JEInternEntityComponent
from jarengine.interns.decorators import documentation as _documentation
from jarengine.systems.color import JEColor as _JEColor

@_documentation
@_final
class JEFontComponent(_JEInternEntityComponent):
    """FontComponent"""

    def __init__(self, owner, font):
        """JEFontComponent creator"""
        super().__init__(owner, JEFontComponent)
        self._font = font

        def set_font(owner_self, font):
            self._font = font

        def get_font(owner_self):
            return self._font

        owner.set_font = set_font.__get__(owner, type(owner))
        owner.get_font = get_font.__get__(owner, type(owner))

    @property
    def font(self):
        """Get font"""
        return self._font

    @font.setter
    def font(self, font):
        """Set font"""
        self._font = font

    def __call__(self):
        """Get font"""
        return self._font

    def copy(self, new_owner):
        """Copy font"""
        return JEFontComponent(new_owner, _deepcopy(self._font))

@_documentation
@_final
class JETextComponent(_JEInternEntityComponent):
    """TextComponent"""

    def __init__(self, owner, text):
        """JETextComponent creator"""
        super().__init__(owner, JETextComponent)
        self._text = text

        def set_text(owner_self, text):
            self._text = text

        def get_text(owner_self):
            return self._text

        owner.set_text = set_text.__get__(owner, type(owner))
        owner.get_text = get_text.__get__(owner, type(owner))

    @property
    def text(self):
        """Get text"""
        return self._text

    @text.setter
    def text(self, text):
        """Set text"""
        self._text = text

    def __call__(self):
        """Get text"""
        return self._text

    def copy(self, new_owner):
        """Copy text"""
        return JETextComponent(new_owner, _deepcopy(self._text))

@_documentation
@_final
class JETextureComponent(_JEInternEntityComponent):
    """TextureComponent"""

    def __init__(self, owner, texture):
        """JETextureComponent creator"""
        super().__init__(owner, JETextureComponent)
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
class JEColorComponent(_JEInternEntityComponent):
    """ColorComponent"""

    def __init__(self, owner, color):
        """JEColorComponent creator"""
        super().__init__(owner, JEColorComponent)
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

        def update_color(owner_self, *, r = 0, g = 0, b = 0, a = 0):
            self._color.r += r
            self._color.g += g
            self._color.b += b
            self._color.a += a

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
class JEVisibilityComponent(_JEInternEntityComponent):
    """VisibilityComponent"""

    def __init__(self, owner, visibility):
        """JEVisibilityComponent creator"""
        super().__init__(owner, JEVisibilityComponent)
        self._visibility = visibility

        def set_visibility(owner_self, visibility):
            self._visibility = visibility

        def get_visibility(owner_self):
            return self._visibility

        owner.set_visibility = set_visibility.__get__(owner, type(owner))
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
class JELayerComponent(_JEInternEntityComponent):
    """LayerComponent"""

    def __init__(self, owner, layer):
        """JELayerComponent creator"""
        super().__init__(owner, JELayerComponent)
        self._layer = layer

        def set_layer(owner_self, layer):
            self._layer = layer

        def update_layer(owner_self, *, l = 0):
            self._layer += l

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
class JEFlipComponent(_JEInternEntityComponent):
    """FlipComponent"""

    def __init__(self, owner, flip):
        """JEFlipComponent creator"""
        super().__init__(owner, JEFlipComponent)
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
