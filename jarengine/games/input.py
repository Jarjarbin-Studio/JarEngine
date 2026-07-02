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

from typing import final as _final

from jarengine.interns import (
    JTKExternError as _JTKExternError,
    PGExtern as _PGExtern
)
from jarengine.interns.base_classe import JEInternBaseClass as _JEInternBaseClass
from jarengine.interns.decorators import documentation as _documentation
from jarengine.events.keyboard import JEKeyCode as _JEKeyCode
from jarengine.events.mouse import JEMouseCode as _JEMouseCode
from jarengine.systems.bool import JEBool as _JEBool

@_documentation
@_final
class JEInput(_JEInternBaseClass):
    """Input manager"""

    _instance = None
    _is_created = _JEBool(0)
    __instance_policy__ = "flyweight"
    __instance_limit__ = 1
    __recursive__ = False

    def __new__(cls, *args, **kwargs):
        """Instances clamping"""
        if cls._instance is not None:
            raise _JTKExternError.Error.ErrorRuntime(
                "\nInstance already exists. Only one input manager is allowed."
            )

        cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """JEInput creator"""
        if JEInput._is_created:
            return

        JEInput._is_created = _JEBool(1)
        super().__init__()
        self._keys_down = _PGExtern.key.get_pressed()
        self._mouse_down = _PGExtern.mouse.get_pressed()
        self._mouse_pos = _PGExtern.mouse.get_pos()

    def update(self):
        """Update keyboard and mouse input"""
        self._keys_down = _PGExtern.key.get_pressed()
        self._mouse_down = _PGExtern.mouse.get_pressed()
        self._mouse_pos = _PGExtern.mouse.get_pos()

    def is_key_down(self, key):
        """Check if a key is down"""
        return self._keys_down[int(key)]

    def is_mouse_down(self, button):
        """Check if a mouse button is down"""
        return self._mouse_down[int(button) - 1]

    def mouse_pos(self):
        """Check if a mouse button is up"""
        return self._mouse_pos

    def __call__(self, code):
        """Automatically call the appropriate input manager"""
        if isinstance(code, _JEKeyCode):
            return self.is_key_down(code)
        elif isinstance(code, _JEMouseCode):
            return self.is_mouse_down(code)
        else:
            raise _JTKExternError.Error.ErrorRuntime()
