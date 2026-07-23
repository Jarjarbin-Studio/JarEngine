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

from typing import Iterator

from jarengine.systems.transform import JETransform

class JEVector2D(JETransform):
    def __init__(self, x: float = 0.0, y: float = 0.0):
        """
            JEVector2D

            Parameters:
                x (float) = 0.0: X coordinate
                y (float) = 0.0: Y coordinate
        """
        ...
    @property
    def x(self) -> float:
        """
            Get x

            Returns:
                float: X
        """
        ...
    @x.setter
    def x(self, x: float):
        """
            Set x

            Parameters:
                x (float): New x
        """
        ...
    @property
    def y(self) -> float:
        """
            Get y

            Returns:
                float: Y
        """
        ...
    @y.setter
    def y(self, y: float):
        """
            Set y

            Parameters:
                y (float): New y
        """
        ...
    def __iter__(self) -> Iterator[float]:
        """
            Iterate over the vector (x, y)

            Returns:
                Iterator[float]: Iterator x and y
        """
        ...

class JEVector3D(JETransform):
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        """
            JEVector3D

            Parameters:
                x (float) = 0.0: X coordinate
                y (float) = 0.0: Y coordinate
                2 (float) = 0.0: Z coordinate
        """
        ...
    @property
    def x(self) -> float:
        """
            Get x

            Returns:
                float: X
        """
        ...
    @x.setter
    def x(self, x: float):
        """
            Set x

            Parameters:
                x (float): New x
        """
        ...
    @property
    def y(self) -> float:
        """
            Get y

            Returns:
                float: Y
        """
        ...
    @y.setter
    def y(self, y: float):
        """
            Set y

            Parameters:
                y (float): New y
        """
        ...
    @property
    def z(self) -> float:
        """
            Get Z

            Returns:
                float: Z
        """
        ...
    @z.setter
    def z(self, z: float):
        """
            Set z

            Parameters:
                z (float): New z
        """
        ...
    def __iter__(self) -> Iterator[float]:
        """
            Iterate over the vector (x, y, z)

            Returns:
                Iterator[float]: Iterator x, y and z
        """
        ...
