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
    PGIntern as _PyGameIntern
)
from sources.interns.decorators import documentation as _documentation

@_documentation
@_final
class JEEventCode(_JEInternClassBase):
    """Event code"""

    _instances: dict[int, _Self] = {}
    _name_cache: dict[int, str] = {}

    @classmethod
    def _build_cache(cls) -> None:
        """Build available events"""
        if cls._name_cache:
            return

        cls._name_cache.update({
            _PyGameIntern.QUIT: "Quit",
            _PyGameIntern.HIDDEN: "Hidden",
            _PyGameIntern.KEYDOWN: "KeyDown",
            _PyGameIntern.KEYUP: "KeyUp",
            _PyGameIntern.MOUSEBUTTONDOWN: "MouseDown",
            _PyGameIntern.MOUSEBUTTONUP: "MouseUp"
        })

    def __new__(
            cls,
            event: int | None = None
        ) -> _Self:
        """Instances clamping"""
        if event is None:
            return super().__new__(cls)

        if event not in cls._instances:
            cls._instances[event] = super().__new__(cls)

        return cls._instances[event]

    def __init__(
            self,
            event: int | None = None
        ) -> None:
        """JEEventCode creator"""
        if hasattr(self, "_initialized") or event is None:
            return

        super().__init__()
        self._event = int(event)
        self._build_cache()
        self._name = self._name_cache.get(self._event, f"EventUnknown({self._event})")
        self._initialized = True

    def __int__(self) -> int:
        """Get event code"""
        return self._event

    @property
    def name(self) -> str:
        """Get event name"""
        return self._name

    def __or__(
            self,
            other: JEEventCode
        ) -> JEEventCodeGroup:
        """Allows same synthax as union (create a JEEventCodeGroup)"""

        if not isinstance(other, JEEventCode):
            raise _JTKInternError.Error.ErrorType(
                "\nOther must be JEEventCode"
            )

        return JEEventCodeGroup([self, other])

    def __eq__(self, other) -> bool:
        """Compare 2 events"""
        if not isinstance(other, JEEventCode):
            return NotImplemented
        return self._event == other._event

    def __hash__(self) -> int:
        """Hash an event"""
        return hash(self._event)

@_documentation
@_final
class JEEventCodeGroup(_JEInternClassBase):
    """Event code group"""

    def __init__(
            self,
            events: list[JEEventCode]
        ):
        """JEEventCodeGroup creator"""
        super().__init__()
        self._events: list[JEEventCode] = list(dict.fromkeys(events))

    def __or__(
            self,
            other
        ):
        """Allows same synthax as union (create a JEEventCodeGroup)"""

        if isinstance(other, JEEventCode):
            return JEEventCodeGroup([*self._events, other])

        if isinstance(other, JEEventCodeGroup):
            return JEEventCodeGroup([*self._events, *other._events])

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

    def __init__(
        self,
        on: JEEventCode | list[JEEventCode] | JEEventCodeGroup,
        do: _Callable[["JEGame", "JEEvent"], None]
    ) -> None:
        """JEEventWatcher creator"""

        if not isinstance(on, (JEEventCode, list, JEEventCodeGroup)):
            raise _JTKInternError.Error.ErrorType(
                "\nOn must be JEEventCode, list or JEEventCodeGroup"
            )

        super().__init__()
        self._on: JEEventCodeGroup = (
            on
            if isinstance(on, JEEventCodeGroup) else
            JEEventCodeGroup(
                on
                if isinstance(on, list) else
                [on]
            )
        )
        self._do: _Callable[["JEGame", "JEEvent"], None] = do

    def match(self, event: "JEEvent") -> bool:
        """Check for event matches"""
        for rule in self._on:
            if event.type_code == rule:
                return True
        return False

    def __call__(self, game: "JEGame", event: "JEEvent") -> None:
        """Call saved function"""
        self._do(game, event)

    @property
    def on(self) -> JEEventCodeGroup:
        """Get watched events"""
        return self._on

    @property
    def do(self) -> str:
        """Get seved function (as str)"""
        return f"{self._do.__name__}(JEGame, JEEvent)"

JEEvtQuit: JEEventCode = JEEventCode(_PyGameIntern.QUIT)
JEEvtHidden: JEEventCode = JEEventCode(_PyGameIntern.HIDDEN)
JEEvtKeyDown: JEEventCode = JEEventCode(_PyGameIntern.KEYDOWN)
JEEvtKeyUp: JEEventCode = JEEventCode(_PyGameIntern.KEYUP)
JEEvtMouseDown: JEEventCode = JEEventCode(_PyGameIntern.MOUSEBUTTONDOWN)
JEEvtMouseUp: JEEventCode = JEEventCode(_PyGameIntern.MOUSEBUTTONUP)
