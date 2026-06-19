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

from typing import Callable as _Callable

from sources.interns import JTKInternAction as _JTKInternAction
from sources.interns.base_classe import JEInternClassBase as _JEInternClassBase
from sources.systems.bool import JEBool as _JEBool

class JEInternGraphic(_JEInternClassBase):

    def __init__(
            self,
            name: str
        ) -> None:
        super().__init__()

        self.name = name
        self._name_hash = hash(self.name)
        self._object_hash = hash(self)
        self._destroyed: _JEBool = _JEBool(0)

    def update(
            self,
            dt: float
        ) -> None:
        pass

    def destroy(self) -> None:
        self._destroyed = _JEBool(1)

    def is_alive(self) -> _JEBool:
        return _JEBool(not self._destroyed)

class JEInternGraphicalObject(JEInternGraphic):

    def __init__(
            self,
            name: str
        ) -> None:
        super().__init__(name)

        self._events: dict[str, _JTKInternAction.Actions] = {}
        self._dirty: _JEBool = _JEBool(1)
        self._enabled: _JEBool = _JEBool(1)

    def update(
            self,
            dt: float
        ) -> None:
        pass

    def enable(self) -> None:
        self._enabled = _JEBool(1)

    def disable(self) -> None:
        self._enabled = _JEBool(0)

    def is_alive(self) -> _JEBool:
        return _JEBool((not self._destroyed) and self._enabled)

    def on(
            self,
            event: str,
            callback: _Callable
        ):

        if not event in self._events:
            self._events[event] = _JTKInternAction.Actions()

        self._events[event] += _JTKInternAction.Action(callback.__name__, callback)

    def emit(
            self,
            event: str
        ) -> None:

        callback: _JTKInternAction.Actions | None = self._events.get(event, None)

        if callback:
            callback()
