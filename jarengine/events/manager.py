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

from jarengine.interns.base_classe import JEInternBaseClass as _JEInternBaseClass
from jarengine.interns import (
    JTKExternError as _JTKExternError,
    PGExtern as _PGExtern
)
from jarengine.events.event import (
    JEEventCode as _JEEventCode,
    JEEventWatcher as _JEEventWatcher
)
from jarengine.events.keyboard import (
    JEKeyCode as _JEKeyCode,
    JEKeyWatcher as _JEKeyWatcher
)
from jarengine.events.mouse import (
    JEMouseCode as _JEMouseCode,
    JEMouseWatcher as _JEMouseWatcher
)
from jarengine.systems.bool import JEBool as _JEBool
from jarengine.interns.decorators import documentation as _documentation

@_documentation
@_final
class JEEvent(_JEInternBaseClass):
    """Event (pygame event ownership)"""

    def __init__(self, event):
        """JEEvent creator"""
        super().__init__()
        self._event = event
        self._type = None
        self._key = None
        self._button = None
        self._pos = None

    @property
    def type(self):
        """Get event type (as JEEventCode)"""
        if not self._type:
            self._type = _JEEventCode(self._event.type)
        return self._type

    @property
    def key(self):
        """Get key (as JEKeyCode)"""
        if not self._key:
            self._key = _JEEventCode(self._event.type) if hasattr(self._event, "key") else None
        return self._key

    @property
    def mouse(self):
        """Get mouse (as JEMouseCode)"""
        if not self._button:
            self._button = _JEEventCode(self._event.type) if hasattr(self._event, "button") else None
        return self._button

@_documentation
@_final
class JEEventHandler(_JEInternBaseClass):
    """Event handler"""

    _instance = None
    _is_created = _JEBool(0)
    __instance_policy__ = "flyweight"
    __instance_limit__ = 1
    __recursive__ = False

    def __new__(cls, *args, **kwargs):
        """Instances clamping"""
        if cls._instance is not None:
            raise _JTKExternError.Error.ErrorRuntime(
                "\nInstance already exists. Only one event handler is allowed."
            )

        cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """JEEventHandler creator"""
        super().__init__()
        JEEventHandler._is_created = _JEBool(1)
        self._watchers = []

    @property
    def watchers(self):
        """Get the list of watched events, keys and mouse"""
        return self._watchers

    def add(self, watcher):
        """Add a watched event, key and mouse"""
        if not isinstance(watcher, (_JEEventWatcher, _JEKeyWatcher, _JEMouseWatcher)):
            raise _JTKExternError.Error.ErrorType(
                "\nOnly JEEventWatcher, JEKeyWatcher and JEMouseWatcher can be added."
            )

        self._watchers.append(watcher)

    def remove(self, event):
        """Remove a watched event, key and mouse by its name"""
        if not self.has(event):
            raise _JTKExternError.Error.ErrorRuntime(
                f"\n{event!r} not found in watcher list."
            )

        for w in self._watchers:
            if int(event) == int(w):
                self._watchers.remove(w)
                return

    def clear(self):
        """clear watcher list"""
        self._watchers.clear()

    def has(self, event):
        """Check if a watcher contains the current event"""
        for w in self._watchers:
            if event == w:
                return _JEBool(1)
        return _JEBool(0)

    def process(self, game, is_single_match: _JEBool = _JEBool(1)):
        """Process events"""
        events = [JEEvent(evt) for evt in _PGExtern.event.get()]

        for event in events:
            for watcher in self._watchers:
                if watcher.match(event):
                    watcher(game, event)
                    if is_single_match:
                        break

    def __deepcopy__(self, memo):
        """Deepcopy"""
        return self
