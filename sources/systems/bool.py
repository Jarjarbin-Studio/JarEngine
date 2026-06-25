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

from typing import (
    Any as _Any,
    final as _final,
    Self as _Self
)
from sources.interns.base_classe import JEInternClassBase as _JEInternClassBase
from sources.interns.decorators import documentation as _documentation

@_documentation
@_final
class JEBool(_JEInternClassBase):
    """Boolean"""

    _instances = {}

    def __new__(cls, value):
        """Instances clamping"""
        val = bool(value)

        if val not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[val] = instance

        return cls._instances[val]

    def __init__(self, value):
        """JEBool creator"""
        if hasattr(self, "_initialized"):
            return

        super().__init__()
        self._bool = bool(value)

    def __bool__(self):
        """Returns boolean value"""
        return self._bool

    @property
    def data(self):
        """Returns boolean value"""
        return bool(self)

    def __deepcopy__(self, memo):
        """Deepcopy"""
        return self
