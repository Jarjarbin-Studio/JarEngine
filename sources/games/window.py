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
    Self as _Self,
    final as _final,
    Any as _Any
)

from sources.interns.base_classe import JEInternClassBase as _JEInternClassBase
from sources.interns import (
    JTKInternError as _JTKInternError,
    PGIntern as _PGIntern
)
from sources.interns.final_classes import JEInternWindowSettings as _JEInternWindowSettings
from sources.systems.color import JEColor as _JEColor
from sources.systems.bool import JEBool as _JEBool
from sources.interns.decorators import documentation as _documentation

@_documentation
@_final
class JEWindow(_JEInternClassBase):
    """Window manager"""

    _instance = None
    _is_created = _JEBool(0)

    def __new__(cls, *args, **kwargs):
        """Instances clamping"""
        if cls._instance is not None:
            raise _JTKInternError.Error.ErrorRuntime(
                "\nInstance already exists. Only one window is allowed."
            )

        cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, *, size = (0, 0), flags = 0, fps = 60, depth = 0, display = 0, vsync = 0, title = "JarEngine Game"):
        """JEWindow creator"""

        if JEWindow._is_created:
            return
        JEWindow._is_created = _JEBool(1)
        super().__init__()
        self._settings = _JEInternWindowSettings(size, flags, fps, depth, display, vsync, title)
        self._screen = _PGIntern.display.set_mode(size, flags, depth, display, vsync)
        _PGIntern.display.set_caption(title)

    @property
    def screen(self):
        """Get screen surface (PGIntern)"""
        return self._screen

    @property
    def settings(self):
        """Get settings"""
        return self._settings

    def fill(self, color):
        """Fill the screen with given color"""
        self._screen.fill(color.rgba if isinstance(color, _JEColor) else color)

    def blit(self, source, dest):
        self._screen.blit(source, dest)

    def __deepcopy__(self, memo):
        """Deepcopy"""
        return self
