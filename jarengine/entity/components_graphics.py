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

from copy import deepcopy as _deepcopy
from typing import final as _final

from jarengine.interns.helpers import (
    assertion_type as _assertion_type,
    safe_cast as _safe_cast
)
from jarengine.interns.high_classes import JEInternEntityComponent as _JEInternEntityComponent
from jarengine.interns.decorators import documentation as _documentation
from jarengine.systems.color import JEColor as _JEColor
from jarengine.interns import PGExtern as _PGExtern
from jarengine.resources.font import JEFont as _JEFont
from jarengine.resources.texture import JETexture as _JETexture
from jarengine.systems.bool import JEBool as _JEBool
from jarengine.entity.entity import JEEntity as _JEEntity

@_documentation
@_final
class JESurfaceComponent(_JEInternEntityComponent):

    def __init__(self, owner, surface):

        _assertion_type(owner, _JEEntity, "owner must be of type 'JEEntity'")
        _assertion_type(surface, _PGExtern.Surface, "surface must be of type 'PyGame.Surface'")

        super().__init__(owner, JESurfaceComponent)
        self._surface = surface

        def set_surface(owner_self, surface):

            _assertion_type(surface, _PGExtern.Surface, "surface must be of type 'PyGame.Surface'")

            self.surface = surface

        def get_surface(owner_self):
            return self.surface

        owner.set_surface = set_surface.__get__(owner, type(owner))
        owner.get_surface = get_surface.__get__(owner, type(owner))

    @property
    def surface(self):
        return self._surface

    @surface.setter
    def surface(self, surface):
        self._surface = surface

    def __call__(self):
        return self._surface

    def copy(self, new_owner):
        return JESurfaceComponent(new_owner, _deepcopy(self._surface))


@_documentation
@_final
class JEFontComponent(_JEInternEntityComponent):

    def __init__(self, owner, font):

        _assertion_type(owner, _JEEntity, "owner must be of type 'JEEntity'")
        _assertion_type(font, _JEFont, "font must be of type 'JEFont'")

        super().__init__(owner, JEFontComponent)
        self._font = font

        def set_font(owner_self, font):

            _assertion_type(font, _JEFont, "font must be of type 'JEFont'")

            self.font = font

        def get_font(owner_self):
            return self.font

        owner.set_font = set_font.__get__(owner, type(owner))
        owner.get_font = get_font.__get__(owner, type(owner))

    @property
    def font(self):
        return self._font

    @font.setter
    def font(self, font):
        self._font = font

    def __call__(self):
        return self._font

    def copy(self, new_owner):
        return JEFontComponent(new_owner, _deepcopy(self._font))

@_documentation
@_final
class JETextComponent(_JEInternEntityComponent):

    __recursive__ = False

    def __init__(self, owner, text):

        _assertion_type(owner, _JEEntity, "owner must be of type 'JEEntity'")
        _assertion_type(text, str, "text must be of type 'str'")

        super().__init__(owner, JETextComponent)
        self._text = text

        def set_text(owner_self, text):

            _assertion_type(text, str, "text must be of type 'str'")

            self.text = text

        def get_text(owner_self):
            return self.text

        owner.set_text = set_text.__get__(owner, type(owner))
        owner.get_text = get_text.__get__(owner, type(owner))

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

    def __call__(self):
        return self._text

    def copy(self, new_owner):
        return JETextComponent(new_owner, _deepcopy(self._text))

@_documentation
@_final
class JETextureComponent(_JEInternEntityComponent):

    def __init__(self, owner, texture):

        _assertion_type(owner, _JEEntity, "owner must be of type 'JEEntity'")
        _assertion_type(texture, _JETexture, "color must be of type 'JETexture'")

        super().__init__(owner, JETextureComponent)
        self._texture = texture

        def set_texture(owner_self, texture):

            _assertion_type(texture, _JETexture, "color must be of type 'JETexture'")

            self.texture = texture

        def get_texture(owner_self):
            return self.texture

        owner.set_texture = set_texture.__get__(owner, type(owner))
        owner.get_texture = get_texture.__get__(owner, type(owner))

    @property
    def texture(self):
        return self._texture

    @texture.setter
    def texture(self, texture):
        self._texture = texture

    def __call__(self):
        return self._texture

    def copy(self, new_owner):
        return JETextureComponent(new_owner, _deepcopy(self._texture))

@_documentation
@_final
class JEColorComponent(_JEInternEntityComponent):

    __recursive__ = False

    def __init__(self, owner, color):

        _assertion_type(owner, _JEEntity, "owner must be of type 'JEEntity'")
        _assertion_type(color, (_JEColor, tuple), "color must be of type 'JEColor'")

        super().__init__(owner, JEColorComponent)
        self._color = (
            color
            if isinstance(color, _JEColor) else
            _JEColor(*color)
        )

        def set_color(owner_self, color):

            _assertion_type(color, (_JEColor, tuple), "color must be of type 'JEColor'")

            self.color = color

        def update_color(owner_self, *, r = 0, g = 0, b = 0, a = 0):

            _assertion_type(r, int, "r must be of type 'int'")
            _assertion_type(g, int, "g must be of type 'int'")
            _assertion_type(b, int, "b must be of type 'int'")
            _assertion_type(a, int, "a must be of type 'int'")

            self._color.r += r
            self._color.g += g
            self._color.b += b
            self._color.a += a

        def get_color(owner_self):
            return self.color

        owner.set_color = set_color.__get__(owner, type(owner))
        owner.update_color = update_color.__get__(owner, type(owner))
        owner.get_color = get_color.__get__(owner, type(owner))

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = (
            color
            if isinstance(color, _JEColor) else
            _JEColor(*color)
        )

    def __call__(self):
        return self._color

    def copy(self, new_owner):
        return JEColorComponent(new_owner, _deepcopy(self._color))

@_documentation
@_final
class JEOutlineComponent(_JEInternEntityComponent):

    __recursive__ = False

    def __init__(self, owner, color, size):

        _assertion_type(owner, _JEEntity, "owner must be of type 'JEEntity'")
        _assertion_type(color, (_JEColor, tuple), "color must be of type 'JEColor'")
        _assertion_type(size, int, "size must be of type 'int'")

        super().__init__(owner, JEOutlineComponent)
        self._color = (
            color
            if isinstance(color, _JEColor) else
            _JEColor(*color)
        )
        self._size = size

        def set_outline_color(owner_self, color):

            _assertion_type(color, (_JEColor, tuple), "color must be of type 'JEColor'")

            self.color = color

        def update_outline_color(owner_self, *, r = 0, g = 0, b = 0, a = 0):

            _assertion_type(r, int, "r must be of type 'int'")
            _assertion_type(g, int, "g must be of type 'int'")
            _assertion_type(b, int, "b must be of type 'int'")
            _assertion_type(a, int, "a must be of type 'int'")

            self._color.r += r
            self._color.g += g
            self._color.b += b
            self._color.a += a

        def get_outline_color(owner_self):
            return self.color

        def set_outline_size(owner_self, size):
            self.size = size

        def update_outline_size(owner_self, *, s = 0):

            _assertion_type(s, int, "s must be of type 'int'")

            self._size += s

        def get_outline_size(owner_self):
            return self.size

        owner.set_outline_color = set_outline_color.__get__(owner, type(owner))
        owner.update_outline_color = update_outline_color.__get__(owner, type(owner))
        owner.get_outline_color = get_outline_color.__get__(owner, type(owner))
        owner.set_outline_size = set_outline_size.__get__(owner, type(owner))
        owner.update_outline_size = update_outline_size.__get__(owner, type(owner))
        owner.get_outline_size = get_outline_size.__get__(owner, type(owner))

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = (
            color
            if isinstance(color, _JEColor) else
            _JEColor(*color)
        )

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    def __call__(self):
        return self._color, self._size

    def copy(self, new_owner):
        return JEOutlineComponent(new_owner, _deepcopy(self._color), _deepcopy(self._size))

@_documentation
@_final
class JEVisibilityComponent(_JEInternEntityComponent):

    __recursive__ = False

    def __init__(self, owner, visibility):

        _assertion_type(owner, _JEEntity, "owner must be of type 'JEEntity'")
        _assertion_type(visibility, _JEBool, "visibility must be of type 'JEBool'")

        super().__init__(owner, JEVisibilityComponent)
        self._visibility = visibility

        def set_visibility(owner_self, visibility):

            _assertion_type(visibility, _JEBool, "visibility must be of type 'JEBool'")

            self.visibility = visibility

        def get_visibility(owner_self):
            return self.visibility

        owner.set_visibility = set_visibility.__get__(owner, type(owner))
        owner.get_visibility = get_visibility.__get__(owner, type(owner))

    @property
    def visibility(self):
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        self._visibility = visibility

    def __call__(self):
        return self._visibility

    def copy(self, new_owner):
        return JEVisibilityComponent(new_owner, _deepcopy(self._visibility))

@_documentation
@_final
class JELayerComponent(_JEInternEntityComponent):

    __recursive__ = False

    def __init__(self, owner, layer):

        _assertion_type(owner, _JEEntity, "owner must be of type 'JEEntity'")
        _assertion_type(layer, int, "l must be of type 'int'")

        super().__init__(owner, JELayerComponent)
        self._layer = layer

        def set_layer(owner_self, layer):
            self.layer = layer

        def update_layer(owner_self, *, l = 0):

            _assertion_type(l, int, "l must be of type 'int'")

            self._layer += l

        def get_layer(owner_self):
            return self.layer

        owner.set_layer = set_layer.__get__(owner, type(owner))
        owner.update_layer = update_layer.__get__(owner, type(owner))
        owner.get_layer = get_layer.__get__(owner, type(owner))

    @property
    def layer(self):
        return self._layer

    @layer.setter
    def layer(self, layer):
        self._layer = layer

    def __call__(self):
        return self._layer

    def copy(self, new_owner):
        return JELayerComponent(new_owner, _deepcopy(self._layer))

@_documentation
@_final
class JEFlipComponent(_JEInternEntityComponent):

    __recursive__ = False

    def __init__(self, owner, flip):

        _assertion_type(owner, _JEEntity, "owner must be of type 'JEEntity'")
        _assertion_type(flip, tuple, "flip must be of type 'tuple'")

        super().__init__(owner, JEFlipComponent)
        self.flip = flip

        def set_flip(owner_self, flip):

            _assertion_type(flip, tuple, "flip must be of type 'tuple'")

            self._flip = flip

        def get_flip(owner_self):
            return self.flip

        owner.set_flip = set_flip.__get__(owner, type(owner))
        owner.get_flip = get_flip.__get__(owner, type(owner))

    @property
    def flip(self):
        return self._flip

    @flip.setter
    def flip(self, flip):
        self._flip = flip

    def __call__(self):
        return self._flip

    def copy(self, new_owner):
        return JELayerComponent(new_owner, _deepcopy(self._flip))
