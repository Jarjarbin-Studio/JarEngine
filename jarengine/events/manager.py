# =============================================================================
# JarEngine - Python Game Engine Wrapper (Pygame-based)
# =============================================================================
#
# JarEngine is a lightweight game framework built on top of Pygame
# that simplifies usage while providing higher-level abstractions for
# game development and prototyping.
#
# =============================================================================
# Version: jarengine-v1.10
# Author: Jarjarbin Studio
# Licence: GPL v3
# =============================================================================
#
# This engine is inspired by Pygame, modern game engine design patterns,
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
# This is NOT Pygame itself.
# It is a custom abstraction layer built on top of Pygame.
#
# =============================================================================

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
from jarengine.interns.helpers import (
    assertion_type as _assertion_type,
    safe_cast as _safe_cast
)
import jarengine.interns.log as _log

@_documentation
@_final
class JEEvent(_JEInternBaseClass):

    def __init__(self, event):

        _assertion_type(event, _PGExtern.event.Event, "event must be of type 'PyGame.event.Event'", True)

        super().__init__()
        self._event = event
        self._type = None
        self._key = None
        self._mouse = None
        self._pos = None

        _log.log("DEBUG", "OBJECT", f"JEEvent: Created", self.jeid, event)

    @property
    def type(self):
        if not self._type:
            self._type = _JEEventCode(self._event.type)
        return self._type

    @property
    def key(self):
        if not self._key:
            self._key = _JEKeyCode(self._event.key) if hasattr(self._event, "key") else None
        return self._key

    @property
    def mouse(self):
        if not self._mouse:
            self._mouse = _JEMouseCode(self._event.button) if hasattr(self._event, "button") else None
        return self._mouse

@_documentation
@_final
class JEEventHandler(_JEInternBaseClass):

    _instance = None
    _is_created = _JEBool(0)

    __instance_policy__ = "flyweight"
    __instance_limit__ = 1
    __recursive__ = False

    _game_type = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is not None:
            raise _JTKExternError.Error.ErrorRuntime(
                "\nInstance already exists. Only one event handler is allowed."
            )

        cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        from jarengine.games.game import JEGame as _JEGame

        super().__init__()

        JEEventHandler._game_type = _JEGame
        JEEventHandler._is_created = _JEBool(1)
        self._watchers = []

        _log.log("DEBUG", "OBJECT", f"JEEventHandler: Created", self.jeid)

    @property
    def watchers(self):
        return self._watchers

    def add(self, watcher):

        _assertion_type(watcher, (_JEEventWatcher, _JEKeyWatcher, _JEMouseWatcher), "watcher must be of type 'JEEventWatcher', 'JEKeyWatcher' or 'JEMouseWatcher'", True)

        if not isinstance(watcher, (_JEEventWatcher, _JEKeyWatcher, _JEMouseWatcher)):
            raise _JTKExternError.Error.ErrorType(
                "\nOnly JEEventWatcher, JEKeyWatcher and JEMouseWatcher can be added."
            )

        self._watchers.append(watcher)

        _log.log("INFO", "EVENT", f"JEEventHandler: Watcher added", self.jeid, watcher)

    def remove(self, watcher):

        _assertion_type(watcher, (_JEEventWatcher, _JEKeyWatcher, _JEMouseWatcher), "watcher must be of type 'JEEventWatcher', 'JEKeyWatcher' or 'JEMouseWatcher'", True)

        if not self.has(watcher):
            raise _JTKExternError.Error.ErrorRuntime(
                f"\n{watcher!r} not found in watcher list."
            )

        for w in self._watchers:
            if int(watcher) == int(w):
                self._watchers.remove(w)
                return

        _log.log("INFO", "EVENT", f"JEEventHandler: Watcher removed", self.jeid, watcher)

    def clear(self):
        self._watchers.clear()

        _log.log("INFO", "EVENT", f"JEEventHandler: Cleared", self.jeid)

    def has(self, code):

        _assertion_type(code, (_JEEventCode, _JEKeyCode, _JEMouseCode), "code must be of type 'JEEventCode', 'JEKeyCode' or 'JEMouseCode'", True)

        for w in self._watchers:
            if code == w:
                return _JEBool(1)
        return _JEBool(0)

    def process(self, game, broadcast = _JEBool(1)):
        _assertion_type(game, JEEventHandler._game_type, "game must be of type 'JEGame'", True)
        broadcast = _safe_cast(_assertion_type(broadcast, _JEBool, "game must be of type 'JEBool'"), _JEBool)

        events = [JEEvent(evt) for evt in _PGExtern.event.get()]

        for event in events:
            for watcher in self._watchers:
                if watcher.match(event):
                    watcher(game, event)
                    if broadcast:
                        break

    def __deepcopy__(self, memo):
        return self
