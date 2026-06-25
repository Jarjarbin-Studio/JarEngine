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

from sources.interns.high_classes import JEInternalEntityComponent
from sources.systems.container import JEContainer
from sources.systems.vector import JEVector2D
from sources.graphics.texture import JETexture

class JEEntity:
    def __init__(self, name: str) -> None: ...
    @property
    def components(self) -> JEContainer[JEInternalEntityComponent]: ...
    def add_component(self, component: JEInternalEntityComponent) -> None: ...
    def get(self, component: type[JEInternalEntityComponent]) -> JEInternalEntityComponent: ...


    ## COMPONENTS ##
    # Position #
    def set_position(self, position: JEVector2D | tuple[float, float]) -> None: ...
    def update_position(self, x: float, y: float) -> None: ...
    def get_position(self) -> JEVector2D: ...

    # Velocity #
    def set_velocity(self, velocity: JEVector2D | tuple[float, float]) -> None: ...
    def update_velocity(self, x: float, y: float) -> None: ...
    def get_velocity(self) -> JEVector2D: ...

    # Size #
    def set_size(self, size: JEVector2D | tuple[float, float]) -> None: ...
    def update_size(self, x: float, y: float) -> None: ...
    def get_size(self) -> JEVector2D: ...

    # Texture #
    def set_texture(self, texture: JETexture) -> None: ...
    def get_texture(self) -> JETexture: ...
