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

from jarengine.interns import PGExtern as _PGExtern
from jarengine.interns.base_classe import JEInternBaseClass as _JEInternBaseClass
from jarengine.interns.decorators import documentation as _documentation

@_documentation
@_final
class JEClock(_JEInternBaseClass):

    __recursive__ = False

    def __init__(self, fps = 60):
        super().__init__()
        self._clock = _PGExtern.time.Clock()
        self._target_fps = fps
        self._dt = 0.0

    def update(self):
        self._dt = min(self._clock.tick(self._target_fps) / 1000.0, 1/60)

    @property
    def dt(self):
        return self._dt

    @property
    def target_fps(self):
        return self._target_fps

    @target_fps.setter
    def target_fps(self, value):
        self._target_fps = max(1, value)

    @property
    def fps(self):
        return self._clock.get_fps()

    def __float__(self):
        return self.dt

    def __deepcopy__(self, memo):
        return self
