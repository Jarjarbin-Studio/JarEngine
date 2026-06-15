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

from types import NoneType
from typing import Self

from sources.systems import JEIntern_Error

class JE_Game:

    _instance: Self = None
    _is_created = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is not None:
            JEIntern_Error.JEIntern_Warning("JEGame", "instance already exists. Only one game is allowed.")
            return cls._instance
        cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if JE_Game._is_created:
            return
        JE_Game._is_created = True
        _screen: NoneType = None
        _ressource: NoneType = None
        _envent: NoneType = None
        _config: NoneType = None
        _clocks: NoneType = None
        _app_state: NoneType = None
