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

from sources.interns.base_classes import JEInternClassBase as _JEInternClassBase
from sources.interns import (
    JTKInternError as _JTKInternError,
    JEInternPyGame as _JEInternPyGame
)
from sources.systems.bool import JEBool as _JEBool

@_final
class JEEventCode(_JEInternClassBase):

    _instances: dict[int, _Self] = {}

    def __new__(
            cls,
            event: int,
            event_name: str
        ) -> _Self:

        if event not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[event] = instance

        return cls._instances[event]

    def __init__(
            self,
            event: int,
            event_name: str
        ) -> None:
        if hasattr(self, "_initialized"):
            return

        super().__init__()
        self._event: int = int(event)
        self._name: str = event_name

    def __int__(self):
        return self._event

    @staticmethod
    def get_name(
            event: int,
            *,
            error: _JEBool = _JEBool(1)
        ) -> str:
        for k in JEEventCode._instances:
            if k == event:
                return JEEventCode._instances[k]._name

        if error:
            raise _JTKInternError.Error.ErrorType(
                "\nevent not available in current version of JarEngine."
            )
        return "event not available in current version of JarEngine."

JEEvtQuit = JEEventCode(_JEInternPyGame.QUIT, "Quit")
JEEvtButtonLeft = JEEventCode(_JEInternPyGame.BUTTON_LEFT, "ButtonLeft")
JEEvtButtonMiddle = JEEventCode(_JEInternPyGame.BUTTON_MIDDLE, "ButtonMiddle")
JEEvtButtonRight = JEEventCode(_JEInternPyGame.BUTTON_RIGHT, "ButtonRight")
JEEvtHidden = JEEventCode(_JEInternPyGame.HIDDEN, "Hidden")
JEEvtKey_A = JEEventCode(_JEInternPyGame.K_a, "Key_A")
JEEvtKey_B = JEEventCode(_JEInternPyGame.K_b, "Key_B")
JEEvtKey_C = JEEventCode(_JEInternPyGame.K_c, "Key_C")
JEEvtKey_D = JEEventCode(_JEInternPyGame.K_d, "Key_D")
JEEvtKey_E = JEEventCode(_JEInternPyGame.K_e, "Key_E")
JEEvtKey_F = JEEventCode(_JEInternPyGame.K_f, "Key_F")
JEEvtKey_G = JEEventCode(_JEInternPyGame.K_g, "Key_G")
JEEvtKey_H = JEEventCode(_JEInternPyGame.K_h, "Key_H")
JEEvtKey_I = JEEventCode(_JEInternPyGame.K_i, "Key_I")
JEEvtKey_J = JEEventCode(_JEInternPyGame.K_j, "Key_J")
JEEvtKey_K = JEEventCode(_JEInternPyGame.K_k, "Key_K")
JEEvtKey_L = JEEventCode(_JEInternPyGame.K_l, "Key_L")
JEEvtKey_M = JEEventCode(_JEInternPyGame.K_m, "Key_M")
JEEvtKey_N = JEEventCode(_JEInternPyGame.K_n, "Key_N")
JEEvtKey_O = JEEventCode(_JEInternPyGame.K_o, "Key_O")
JEEvtKey_P = JEEventCode(_JEInternPyGame.K_p, "Key_P")
JEEvtKey_Q = JEEventCode(_JEInternPyGame.K_q, "Key_Q")
JEEvtKey_R = JEEventCode(_JEInternPyGame.K_r, "Key_R")
JEEvtKey_S = JEEventCode(_JEInternPyGame.K_s, "Key_S")
JEEvtKey_T = JEEventCode(_JEInternPyGame.K_t, "Key_T")
JEEvtKey_U = JEEventCode(_JEInternPyGame.K_u, "Key_U")
JEEvtKey_V = JEEventCode(_JEInternPyGame.K_v, "Key_V")
JEEvtKey_W = JEEventCode(_JEInternPyGame.K_w, "Key_W")
JEEvtKey_X = JEEventCode(_JEInternPyGame.K_x, "Key_X")
JEEvtKey_Y = JEEventCode(_JEInternPyGame.K_y, "Key_Y")
JEEvtKey_Z = JEEventCode(_JEInternPyGame.K_z, "Key_Z")
JEEvtKey_0 = JEEventCode(_JEInternPyGame.K_0, "Key_0")
JEEvtKey_1 = JEEventCode(_JEInternPyGame.K_1, "Key_1")
JEEvtKey_2 = JEEventCode(_JEInternPyGame.K_2, "Key_2")
JEEvtKey_3 = JEEventCode(_JEInternPyGame.K_3, "Key_3")
JEEvtKey_4 = JEEventCode(_JEInternPyGame.K_4, "Key_4")
JEEvtKey_5 = JEEventCode(_JEInternPyGame.K_5, "Key_5")
JEEvtKey_6 = JEEventCode(_JEInternPyGame.K_6, "Key_6")
JEEvtKey_7 = JEEventCode(_JEInternPyGame.K_7, "Key_7")
JEEvtKey_8 = JEEventCode(_JEInternPyGame.K_8, "Key_8")
JEEvtKey_9 = JEEventCode(_JEInternPyGame.K_9, "Key_9")
JEEvtKey_Enter = JEEventCode(_JEInternPyGame.K_RETURN, "Key_Enter")
JEEvtKey_Backspace = JEEventCode(_JEInternPyGame.K_BACKSPACE, "Key_Backspace")
JEEvtKey_Delete = JEEventCode(_JEInternPyGame.K_DELETE, "Key_Delete")
JEEvtKey_Tab = JEEventCode(_JEInternPyGame.K_TAB, "Key_Tab")
JEEvtKey_Escape = JEEventCode(_JEInternPyGame.K_ESCAPE, "Key_Escape")
JEEvtKey_Up = JEEventCode(_JEInternPyGame.K_UP, "Key_Up")
JEEvtKey_Down = JEEventCode(_JEInternPyGame.K_DOWN, "Key_Down")
JEEvtKey_Left = JEEventCode(_JEInternPyGame.K_LEFT, "Key_Left")
JEEvtKey_Right = JEEventCode(_JEInternPyGame.K_RIGHT, "Key_Right")

@_final
class JEEvent(_JEInternClassBase):

    def __init__(
            self,
            event: _JEInternPyGame.event.Event
        ) -> None:
        super().__init__()
        self._event : _JEInternPyGame.event.Event = event

    @property
    def type(self):
        return self._event.type

    @property
    def name(self):
        return JEEventCode.get_name(self.type)

@_final
class JEEventWatcher(_JEInternClassBase):

    def __init__(
            self,
            on: JEEventCode,
            do: _Callable[["JEGame", JEEvent], None],
        ) -> None:
        if not isinstance(on, JEEventCode):
            raise _JTKInternError.Error.ErrorType(
                "\non must be JEEventCode."
            )

        if not isinstance(do, _Callable):
            raise _JTKInternError.Error.ErrorType(
                "\ndo must be Callable."
            )

        super().__init__()
        self._on : JEEventCode = on
        self._do : _Callable[["JEGame", JEEvent], None] = do

    def __int__(self) -> int:
        return int(self._on)

    def __eq__(
            self,
            other: JEEventCode
        ) -> _JEBool:
        if not isinstance(other, JEEventCode):
            raise _JTKInternError.Error.ErrorType(
                "\nJEEventWatcher must be compared with JEEvent."
            )

        return _JEBool(int(self._on) == int(other))

    def __call__(
            self,
            game: "JEGame",
            event: JEEvent
        ) -> None:
        self._do(game, event)


@_final
class JEEventHandler(_JEInternClassBase):

    _instance: _Self = None
    _is_created: _JEBool = _JEBool(0)

    def __new__(
            cls,
            *args,
            **kwargs
        ) -> _Self:
        if cls._instance is not None:
            raise _JTKInternError.Error.ErrorRuntime(
                "\nInstance already exists. Only one event handler is allowed."
            )

        cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        JEEventHandler._is_created = _JEBool(1)
        super().__init__()
        self._watchers: list[JEEventWatcher] = []

    def add(
            self,
            watcher: JEEventWatcher
        ) -> None:
        if not isinstance(watcher, JEEventWatcher):
            raise _JTKInternError.Error.ErrorType(
                "\nOnly JEEventWatcher can be added."
            )

        self._watchers.append(watcher)

    def remove(
            self,
            event: JEEventCode
        ) -> None:
        if not self.has(event):
            raise _JTKInternError.Error.ErrorRuntime(
                f"\n{event!r} not found in watcher list."
            )

        for w in self._watchers:
            if int(event) == int(w):
                self._watchers.remove(w)
                return

    def clear(self) -> None:
        self._watchers.clear()

    def has(
            self,
            event: JEEventCode
        ) -> _JEBool:
        for w in self._watchers:
            if int(event) == int(w):
                return _JEBool(1)
        return _JEBool(0)

    def get_all(self) -> list[JEEventWatcher]:
        return list(self._watchers)

    def process(self, game: "JEGame") -> None:
        events = _JEInternPyGame.event.get()

        for raw_event in events:
            event = JEEvent(raw_event)
            event_code = JEEventCode(event.type, JEEventCode.get_name(event.type, error=_JEBool(0)))

            for watcher in self._watchers:
                if watcher == event_code:
                    watcher(game, event)
