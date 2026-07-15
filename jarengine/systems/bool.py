"""
    JarEngine - Python Game Engine Wrapper (Pygame-based)

    JarEngine is a lightweight game framework built on top of Pygame
    that simplifies usage while providing higher-level abstractions for
    game development and prototyping.

    Version: jarengine-v1.6
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

from jarengine.interns.base_classe import JEInternBaseClass as _JEInternBaseClass
from jarengine.interns.decorators import documentation as _documentation

@_documentation
@_final
class JEBool(_JEInternBaseClass):

    _instances = {}
    __instance_policy__ = "flyweight"
    __instance_limit__ = 2
    __recursive__ = False

    def __new__(cls, value):
        val = bool(value)

        if val not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[val] = instance

        return cls._instances[val]

    def __init__(self, value):
        if hasattr(self, "_initialized"):
            return

        super().__init__()
        self._bool = bool(value)

    def __bool__(self):
        return self._bool

    def __int__(self):
        return int(self._bool)

    def __call__(self):
        return JEBool(not self)

    @property
    def b(self):
        return bool(self)

    def __deepcopy__(self, memo):
        return self
