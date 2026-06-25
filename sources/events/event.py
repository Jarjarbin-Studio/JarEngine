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
    Callable as _Callable,
    Self as _Self
)

from sources.interns.base_classe import JEInternClassBase as _JEInternClassBase
from sources.interns import (
    JTKInternError as _JTKInternError,
    PGIntern as _PGIntern
)
from sources.interns.decorators import documentation as _documentation

@_documentation
@_final
class JEEventCode(_JEInternClassBase):
    """Event code"""

    _instances = {}
    _name_cache = {}

    @classmethod
    def _build_cache(cls):
        """Build available events"""
        if cls._name_cache:
            return

        cls._name_cache.update({
            _PGIntern.QUIT: "Quit",
            _PGIntern.HIDDEN: "Hidden",
            _PGIntern.KEYDOWN: "KeyDown",
            _PGIntern.KEYUP: "KeyUp",
            _PGIntern.MOUSEBUTTONDOWN: "MouseDown",
            _PGIntern.MOUSEBUTTONUP: "MouseUp"
        })

    def __new__(cls, event = None):
        """Instances clamping"""
        if event is None:
            return super().__new__(cls)

        if event not in cls._instances:
            cls._instances[event] = super().__new__(cls)

        return cls._instances[event]

    def __init__(self, event = None):
        """JEEventCode creator"""
        if hasattr(self, "_initialized") or event is None:
            return

        super().__init__()
        self._event = int(event)
        self._build_cache()
        self._name = self._name_cache.get(self._event, f"EventUnknown({self._event})")
        self._initialized = True

    def __int__(self):
        """Get event code"""
        return self._event

    @property
    def name(self):
        """Get event name"""
        return self._name

    def __or__(self, other):
        """Allows same synthax as union (create a JEEventCodeGroup)"""

        if not isinstance(other, JEEventCode):
            raise _JTKInternError.Error.ErrorType(
                "\nOther must be JEEventCode"
            )

        return JEEventCodeGroup([self, other])

    def __eq__(self, other):
        """Compare 2 events"""
        if not isinstance(other, JEEventCode):
            return NotImplemented
        return int(self) == int(other)

    def __hash__(self):
        """Hash an event"""
        return hash(self._event)

@_documentation
@_final
class JEEventCodeGroup(_JEInternClassBase):
    """Event code group"""

    def __init__(self, events):
        """JEEventCodeGroup creator"""
        super().__init__()
        self._events = list(dict.fromkeys(events))

    def __or__(self, other):
        """Allows same synthax as union (create a JEEventCodeGroup)"""

        if isinstance(other, JEEventCode):
            return JEEventCodeGroup([*self, other])

        if isinstance(other, JEEventCodeGroup):
            return JEEventCodeGroup([*self, *other])

        raise _JTKInternError.error.ErrorType(
            "\nInvalid type for union"
        )

    def __iter__(self):
        """Get the iterator of events"""
        return iter(self._events)

    @property
    def events(self):
        """Get the key event"""
        return self._events

@_documentation
@_final
class JEEventWatcher(_JEInternClassBase):
    """Main event watcher"""

    def __init__(self, on, do):
        """JEEventWatcher creator"""

        if not isinstance(on, (JEEventCode, list, JEEventCodeGroup)):
            raise _JTKInternError.Error.ErrorType(
                "\nOn must be JEEventCode, list or JEEventCodeGroup"
            )

        super().__init__()
        self._on = (
            on
            if isinstance(on, JEEventCodeGroup) else
            JEEventCodeGroup(
                on
                if isinstance(on, list) else
                [on]
            )
        )
        self._do = do

    def match(self, event):
        """Check for event matches"""
        for rule in self._on:
            if event.type == rule:
                return True
        return False

    def __call__(self, game, event):
        """Call saved function"""
        self._do(game, event)

    @property
    def on(self):
        """Get watched events"""
        return self._on

    @property
    def do(self):
        """Get seved function (as str)"""
        return f"{self._do.__name__}(JEGame, JEEvent)"
