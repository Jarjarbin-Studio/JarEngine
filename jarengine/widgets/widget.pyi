# =============================================================================
# JarEngine - Python Game Engine Wrapper (Pygame-based)
# =============================================================================
#
# JarEngine is a lightweight game framework built on top of Pygame
# that simplifies usage while providing higher-level abstractions for
# game development and prototyping.
#
# =============================================================================
# Version: jarengine-v1.10
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

from jarengine import JETrue
from jarengine.interns.low_classes import JEInternGraphicalObject
from jarengine.interns.high_classes import JEInternOwnership
from jarengine.systems.bool import JEBool
from jarengine.systems.vector import JEVector2D


class JEWidget(JEInternGraphicalObject, JEInternOwnership):
    def __init__(self, *, name: str = "JEWidget", position: JEVector2D | tuple[float, float] = JEVector2D(0, 0), size: JEVector2D | tuple[float, float] = JEVector2D(0, 0), rotation: float = 0.0, layer: int = 0, visibility: JEBool = JETrue):
        """
            JEWidget

            Parameters:
                name (str) = "JEWidget": name
                position (JEVector2D) = (0, 0): position
                size (JEVector2D) = (0, 0): size
                rotation (float) = 0.0: rotation
                layer (int) = 0: layer
                visibility (JEBool) = JETrue: visibility
        """
        ...
    def copy(self) -> JEWidget:
        """
            Copy recursively (deepcopy) the widget

            Returns:
                JEWidget: New widget
        """
        ...
    def set_visibility(self, visibility: JEBool):
        """
            Set visibility.

            Parameters:
                visibility (JEBool): New visibility
        """
        ...
    def get_visibility(self) -> JEBool:
        """
            Get visibility.

            Returns:
                JEBool: Visibility
        """
        ...
    def set_layer(self, layer: int):
        """
            Set layer.

            Parameters:
                layer (int): New layer
        """
        ...
    def update_layer(self, *, l: int = 0):
        """
            Update layer.

            Parameters:
                l (int) = 0: Layer to add to the current layer
        """
        ...
    def get_layer(self) -> int:
        """
            Get layer.

            Returns:
                int: Layer
        """
        ...
    def set_position(self, position: JEVector2D | tuple[float, float]):
        """
            Set position.

            Parameters:
                position (JEVector2D | tuple[float, float]): New position
        """
        ...
    def update_position(self, *, x: float = 0.0, y: float = 0.0):
        """
            Update position.

            Parameters:
                x (float) = 0.0: Position x to add to the current position x
                y (float) = 0.0: Position y to add to the current position y
        """
        ...
    def get_position(self) -> JEVector2D:
        """
            Get position.

            Returns:
                JEVector2D: Position
        """
        ...
    def get_world_position(self) -> JEVector2D:
        """
            Get world position.

            Returns:
                JEVector2D: World position
        """
        ...
    def set_size(self, size: JEVector2D | tuple[float, float]):
        """
            Set size.

            Parameters:
                size (JEVector2D | tuple[float, float]): New size
        """
        ...
    def update_size(self, *, x: float = 0.0, y: float = 0.0):
        """
            Update size.

            Parameters:
                x (float) = 0.0: Size x to add to the current size x
                y (float) = 0.0: Size y to add to the current size y
        """
        ...
    def get_size(self) -> JEVector2D:
        """
            Get size.

            Returns:
                JEVector2D: Size
        """
        ...
    def set_rotation(self, rotation: float):
        """
            Set rotation.

            Parameters:
                rotation (JEFont): New rotation (degrees)
        """
        ...
    def update_rotation(self, *, r: float = 0.0):
        """
            Update rotation.

            Parameters:
                r (float) = 0.0: Rotation to add to the current rotation (degrees)
        """
        ...
    def get_rotation(self) -> float:
        """
            Set rotation.

            Returns:
                float: Rotation
        """
        ...
