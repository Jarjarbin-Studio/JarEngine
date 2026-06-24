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

from typing import final as _final

from sources.entities.entity import JEEntity as _JEEntity
from sources.interns.high_classes import JEInternalEntityComponent as _JEInternalEntityComponent
from sources.graphics.texture import JETexture as _JETexture
from sources.interns.decorators import documentation as _documentation
from sources.systems.vector import JEVector2D as _JEVector2D

@_documentation
@_final
class JEPositionComponent(_JEInternalEntityComponent):
    """PositionComponent"""

    def __init__(
            self,
            owner: _JEEntity,
            position: _JEVector2D | tuple[int, int]
        ):
        """JEPositionComponent creator"""

        super().__init__(f"JEPositionComponent({owner.jeid})")
        self.add_parent(owner)
        owner.add_component(self)
        self._position: _JEVector2D = (
            position
            if isinstance(position, _JEVector2D) else
            _JEVector2D(*position)
        )

        def set_position(
                owner_self,
                position
            ):
            self._position = position

        def modify_position(
                owner_self,
                *,
                x: float = 0,
                y: float = 0
            ):
            self._position.x += x
            self._position.y += y

        def get_position(owner_self):
            return self._position

        owner.set_position = set_position.__get__(owner, type(owner))
        owner.modify_position = modify_position.__get__(owner, type(owner))
        owner.get_position = get_position.__get__(owner, type(owner))

    @property
    def position(self) -> _JEVector2D:
        """Get position"""
        return self._position

    @position.setter
    def position(self, position: _JEVector2D | tuple[int, int]):
        self._position = (
            position
            if isinstance(position, _JEVector2D) else
            _JEVector2D(*position)
        )

    def __call__(self) -> _JEVector2D:
        """Get position"""
        return self._position

@_documentation
@_final
class JEVelocityComponent(_JEInternalEntityComponent):
    """VelocityComponent"""

    def __init__(
            self,
            owner: _JEEntity,
            velocity: _JEVector2D | tuple[int, int]
        ):
        """JEVelocityComponent creator"""
        super().__init__(f"JEVelocityComponent({owner.jeid})")
        self.add_parent(owner)
        owner.add_component(self)
        self._velocity: _JEVector2D = (
            velocity
            if isinstance(velocity, _JEVector2D) else
            _JEVector2D(*velocity)
        )

        def set_velocity(
                owner_self,
                velocity
            ):
            self._velocity = velocity

        def modify_velocity(
                owner_self,
                *,
                x: float = 0,
                y: float = 0
            ):
            self._velocity.x += x
            self._velocity.y += y

        def get_velocity(owner_self):
            return self._velocity

        owner.set_velocity = set_velocity.__get__(owner, type(owner))
        owner.modify_velocity = modify_velocity.__get__(owner, type(owner))
        owner.get_velocity = get_velocity.__get__(owner, type(owner))

    @property
    def velocity(self) -> _JEVector2D:
        """Get velocity"""
        return self._velocity

    @velocity.setter
    def velocity(self, velocity: _JEVector2D | tuple[int, int]):
        self._velocity = (
            velocity
            if isinstance(velocity, _JEVector2D) else
            _JEVector2D(*velocity)
        )

    def __call__(self) -> _JEVector2D:
        """Get velocity"""
        return self._velocity

@_documentation
@_final
class JESizeComponent(_JEInternalEntityComponent):
    """SizeComponent"""

    def __init__(
            self,
            owner: _JEEntity,
            size: _JEVector2D | tuple[int, int]
        ):
        """JESizeComponent creator"""
        super().__init__(f"JESizeComponent({owner.jeid})")
        self.add_parent(owner)
        owner.add_component(self)
        self._size: _JEVector2D = (
            size
            if isinstance(size, _JEVector2D) else
            _JEVector2D(*size)
        )

        def set_size(
                owner_self,
                size
            ):
            self._size = size

        def modify_size(
                owner_self,
                *,
                x: float = 0,
                y: float = 0
            ):
            self._size.x += x
            self._size.y += y

        def get_size(owner_self):
            return self._size

        owner.set_size = set_size.__get__(owner, type(owner))
        owner.modify_size = modify_size.__get__(owner, type(owner))
        owner.get_size = get_size.__get__(owner, type(owner))

    @property
    def size(self) -> _JEVector2D:
        """Get size"""
        return self._size

    @size.setter
    def size(self, size: _JEVector2D | tuple[int, int]):
        self._size = (
            size
            if isinstance(size, _JEVector2D) else
            _JEVector2D(*size)
        )

    def __call__(self) -> _JEVector2D:
        """Get size"""
        return self._size

@_documentation
@_final
class JETextureComponent(_JEInternalEntityComponent):
    """TextureComponent"""

    def __init__(
            self,
            owner: _JEEntity,
            texture: _JETexture
        ):
        """JETextureComponent creator"""
        super().__init__(f"JETextureComponent({owner.jeid})")
        self.add_parent(owner)
        owner.add_component(self)
        self._texture: _JETexture = texture

        def set_texture(
                owner_self,
                texture
            ):
            self._texture = texture

        def get_texture(owner_self):
            return self._texture

        owner.set_texture = set_texture.__get__(owner, type(owner))
        owner.get_texture = get_texture.__get__(owner, type(owner))

    @property
    def texture(self) -> _JETexture:
        """Get texture"""
        return self._texture

    @texture.setter
    def texture(self, texture: _JETexture):
        self._texture = texture

    def __call__(self) -> _JETexture:
        """Get texture"""
        return self._texture
