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
    JEInternPyGame as _JEInternPyGame
)

@_final
class JEEventCode(_JEInternClassBase):

    _instances: dict[int, _Self] = {}
    _name_cache: dict[int, str] = {}

    @classmethod
    def _build_cache(cls) -> None:
        if cls._name_cache:
            return

        cls._name_cache.update({
            _JEInternPyGame.QUIT: "Quit",
            _JEInternPyGame.HIDDEN: "Hidden",
            _JEInternPyGame.KEYDOWN: "KeyDown",
            _JEInternPyGame.KEYUP: "KeyUp",
            _JEInternPyGame.MOUSEBUTTONDOWN: "MouseDown",
            _JEInternPyGame.MOUSEBUTTONUP: "MouseUp"
        })

    def __new__(
            cls,
            event: int | None = None
        ) -> _Self:
        if event is None:
            return super().__new__(cls)

        if event not in cls._instances:
            cls._instances[event] = super().__new__(cls)

        return cls._instances[event]

    def __init__(
            self,
            event: int | None = None
        ) -> None:
        if hasattr(self, "_initialized") or event is None:
            return

        super().__init__()
        self._event = int(event)
        self._build_cache()
        self._name = self._name_cache.get(self._event, f"EventUnknown({self._event})")
        self._initialized = True

    def __int__(self) -> int:
        return self._event

    @property
    def name(self) -> str:
        return self._name

    def __or__(
            self,
            other: JEEventCode
        ) -> JEEventCodeGroup:

        if not isinstance(other, JEEventCode):
            raise _JTKInternError.Error.ErrorType(
                "\nOther must be JEEventCode"
            )

        return JEEventCodeGroup([self, other])

    def __eq__(self, other) -> bool:
        if not isinstance(other, JEEventCode):
            return NotImplemented
        return self._event == other._event

    def __hash__(self) -> int:
        return hash(self._event)

class JEEventCodeGroup(_JEInternClassBase):

    def __init__(
            self,
            events: list[JEEventCode]
        ):
        super().__init__()
        self._events: list[JEEventCode] = list(dict.fromkeys(events))

    def __or__(
            self,
            other
        ):
        if isinstance(other, JEEventCode):
            return JEEventCodeGroup([*self._events, other])

        if isinstance(other, JEEventCodeGroup):
            return JEEventCodeGroup([*self._events, *other._events])

        raise _JTKInternError.error.ErrorType(
            "\nInvalid type for union"
        )

    def __iter__(self):
        return iter(self._events)

    @property
    def events(self):
        return self._events

@_final
class JEEventWatcher(_JEInternClassBase):

    def __init__(
        self,
        on: JEEventCode | list[JEEventCode] | JEEventCodeGroup,
        do: _Callable[["JEGame", "JEEvent"], None]
    ) -> None:

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
        for rule in self._on:
            if event.type_code == rule:
                return True
        return False

    def __call__(self, game: "JEGame", event: "JEEvent") -> None:
        self._do(game, event)

    @property
    def on(self) -> JEEventCodeGroup:
        return self._on

    @property
    def do(self) -> str:
        return f"{self._do.__name__}(JEGame, JEEvent)"

JEEvtQuit: JEEventCode = JEEventCode(_JEInternPyGame.QUIT)
JEEvtHidden: JEEventCode = JEEventCode(_JEInternPyGame.HIDDEN)
JEEvtKeyDown: JEEventCode = JEEventCode(_JEInternPyGame.KEYDOWN)
JEEvtKeyUp: JEEventCode = JEEventCode(_JEInternPyGame.KEYUP)
JEEvtMouseDown: JEEventCode = JEEventCode(_JEInternPyGame.MOUSEBUTTONDOWN)
JEEvtMouseUp: JEEventCode = JEEventCode(_JEInternPyGame.MOUSEBUTTONUP)
