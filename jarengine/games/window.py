# =============================================================================
# JarEngine - Python Game Engine Wrapper (PyGame-based)
# =============================================================================
#
# JarEngine is a lightweight game framework built on top of PyGame
# that simplifies usage while providing higher-level abstractions for
# game development and prototyping.
#
# =============================================================================
# Version: jarengine-v1.8
# Author: Jarjarbin Studio
# Licence: GPL v3
# =============================================================================
#
# This engine is inspired by PyGame, modern game engine design patterns,
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
# This is NOT PyGame itself.
# It is a custom abstraction layer built on top of PyGame.
#
# =============================================================================

from __future__ import annotations

from typing import final as _final

from jarengine.interns.base_classe import JEInternBaseClass as _JEInternBaseClass
from jarengine.interns import (
    JTKExternError as _JTKExternError,
    PGExtern as _PGExtern
)
from jarengine.interns.final_classes import JEInternWindowSettings as _JEInternWindowSettings
from jarengine.systems.color import JEColor as _JEColor
from jarengine.systems.bool import JEBool as _JEBool
from jarengine.interns.decorators import documentation as _documentation
from jarengine.systems.vector import JEVector2D as _JEVector2D

@_documentation
@_final
class JEWindow(_JEInternBaseClass):

    _instance = None
    _is_created = _JEBool(0)

    __instance_policy__ = "flyweight"
    __instance_limit__ = 1

    def __new__(cls, *args, **kwargs):
        if cls._instance is not None:
            raise _JTKExternError.Error.ErrorRuntime(
                "\nInstance already exists. Only one window is allowed."
            )

        cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, *, size = (0, 0), flags = 0, fps = 60, depth = 0, display = 0, vsync = 0, title = "JarEngine Game"):
        if JEWindow._is_created:
            return
        JEWindow._is_created = _JEBool(1)
        super().__init__()
        self._render_surface = _PGExtern.Surface(
            list(size),
            _PGExtern.SRCALPHA
        )
        self._screen = _PGExtern.display.set_mode(list(size), flags, depth, display, vsync)
        self._settings = _JEInternWindowSettings(_JEVector2D(*size) if isinstance(size, (tuple, list)) else size, flags, fps, depth, display, vsync, title)

    @property
    def render_surface(self):
        return self._render_surface

    @property
    def screen(self):
        return self._screen

    @property
    def settings(self):
        return self._settings

    def fill(self, color):
        self._render_surface.fill(list(color))

    def clear(self):
        self.fill(_JEColor(0, 0, 0, 0))

    def blit(self, source, dest):
        self._render_surface.blit(source, list(dest))

    def display(self):
        self._screen.fill((0, 0, 0, 255))
        self._screen.blit(
            self._render_surface,
            (0, 0)
        )

    def __deepcopy__(self, memo):
        return self
