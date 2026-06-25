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

from typing import final as _final

from sources.interns import PGIntern as _PGIntern
from sources.interns.base_classe import JEInternClassBase as _JEInternClassBase
from sources.interns.decorators import documentation as _documentation

@_documentation
@_final
class JEClock(_JEInternClassBase):
    """Clock"""

    def __init__(self, fps = 60):
        """JEClock creator"""

        super().__init__()
        self._clock = _PGIntern.time.Clock()
        self._target_fps = fps
        self._dt = 0.0

    def update(self):
        """Update delta time"""
        self._dt = min(self._clock.tick(self._target_fps) / 1000.0, 1/60)

    @property
    def dt(self):
        """Get delta time"""
        return self._dt

    @property
    def target_fps(self):
        """Get target fps"""
        return self._target_fps

    @target_fps.setter
    def target_fps(self, value):
        """Set target fps"""
        self._target_fps = max(1, value)

    @property
    def fps(self):
        """Get real fps"""
        return self._clock.get_fps()

    def __float__(self):
        """Get dt"""
        return self.dt

    def __deepcopy__(self, memo):
        """Deepcopy"""
        return self
