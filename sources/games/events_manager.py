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
    final as _final,
    Self as _Self
)

from sources.interns.base_classe import JEInternClassBase as _JEInternClassBase
from sources.interns import (
    JTKInternError as _JTKInternError,
    PGIntern as _PyGameIntern
)
from sources.games.event import (
    JEEventCode as _JEEventCode,
    JEEventWatcher as _JEEventWatcher
)
from sources.games.keyboard import (
    JEKeyCode as _JEKeyCode,
    JEKeyWatcher as _JEKeyWatcher
)
from sources.games.mouse import (
    JEMouseCode as _JEMouseCode,
    JEMouseWatcher as _JEMouseWatcher
)
from sources.systems.bool import JEBool as _JEBool
from sources.interns.decorators import documentation as _documentation

@_documentation
@_final
class JEEvent(_JEInternClassBase):
    """Event (pygame event ownership)"""

    def __init__(
            self,
            event: _PyGameIntern.event.Event
        ) -> None:
        """JEEvent creator"""
        super().__init__()
        self._event = event

        self._type: int = event.type
        self._key: int | None = getattr(event, "key", None)
        self._button: int | None = getattr(event, "button", None)
        self._pos = getattr(event, "pos", None)

    @property
    def type(self) -> _JEEventCode:
        """Get event type (as JEEventCode)"""
        return _JEEventCode(self._type)

    @property
    def key(self) -> _JEKeyCode | None:
        """Get key (as JEKeyCode)"""
        return _JEKeyCode(self._key) if self._key is not None else None

    @property
    def mouse(self) -> _JEMouseCode | None:
        """Get mouse (as JEMouseCode)"""
        return _JEMouseCode(self._button) if self._button is not None else None

@_documentation
@_final
class JEEventHandler(_JEInternClassBase):
    """Event handler"""

    _instance: _Self = None
    _is_created: _JEBool = _JEBool(0)

    def __new__(
            cls,
            *args,
            **kwargs
        ) -> _Self:
        """Instances clamping"""
        if cls._instance is not None:
            raise _JTKInternError.Error.ErrorRuntime(
                "\nInstance already exists. Only one event handler is allowed."
            )

        cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        """JEEventHandler creator"""
        super().__init__()
        JEEventHandler._is_created = _JEBool(1)
        self._watchers: list[_JEEventWatcher | _JEKeyWatcher | _JEMouseWatcher] = []

    @property
    def watchers(self) -> list[_JEEventWatcher | _JEKeyWatcher | _JEMouseWatcher]:
        """Get the list of watched events, keys and mouse"""
        return self._watchers

    def add(
            self,
            watcher: _JEEventWatcher | _JEKeyWatcher | _JEMouseWatcher
        ) -> None:
        """Add a watched event, key and mouse"""
        if not isinstance(watcher, (_JEEventWatcher, _JEKeyWatcher, _JEMouseWatcher)):
            raise _JTKInternError.Error.ErrorType(
                "\nOnly JEEventWatcher, JEKeyWatcher and JEMouseWatcher can be added."
            )

        self._watchers.append(watcher)

    def remove(
            self,
            event: _JEEventCode | _JEKeyCode | _JEMouseCode
        ) -> None:
        """Remove a watched event, key and mouse by its name"""
        if not self.has(event):
            raise _JTKInternError.Error.ErrorRuntime(
                f"\n{event!r} not found in watcher list."
            )

        for w in self._watchers:
            if int(event) == int(w):
                self._watchers.remove(w)
                return

    def clear(self) -> None:
        """clear watcher list"""
        self._watchers.clear()

    def has(
            self,
            event: _JEEventCode | _JEKeyCode | _JEMouseCode
        ) -> _JEBool:
        """Check if a watcher contains the current event"""
        for w in self._watchers:
            if event == w:
                return _JEBool(1)
        return _JEBool(0)

    def process(
            self,
            game: "JEGame"
        ) -> None:
        """Process events"""
        events: list[JEEvent] = [JEEvent(evt) for evt in _PyGameIntern.event.get()]

        for event in events:
            for watcher in self._watchers:
                if watcher.match(event):
                    watcher(game, event)

    def __deepcopy__(
            self,
            memo
        ):
        """Deepcopy"""
        return self
