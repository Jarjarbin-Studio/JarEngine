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
from sources.systems.bool import JEBool as _JEBool

@_final
class JEEventCode(_JEInternClassBase):

    _instances: dict[int, _Self] = {}
    _name_cache: dict[int, str] = {}

    @classmethod
    def _build_cache(cls) -> None:
        if cls._name_cache:
            return

        cls._name_cache[_JEInternPyGame.QUIT] = "Quit"
        cls._name_cache[_JEInternPyGame.HIDDEN] = "Hidden"

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
        self._name = self._name_cache.get(self._event, f"Unknown({self._event})")
        self._initialized = True

    def __int__(self) -> int:
        return self._event

    @property
    def name(self) -> str:
        return self._name

JEEvtQuit: JEEventCode = JEEventCode(_JEInternPyGame.QUIT)
JEEvtHidden: JEEventCode = JEEventCode(_JEInternPyGame.HIDDEN)
JEEvtKeyDown: JEEventCode = JEEventCode(_JEInternPyGame.KEYDOWN)
JEEvtMouseButtonDown: JEEventCode = JEEventCode(_JEInternPyGame.MOUSEBUTTONDOWN)

@_final
class JEKey(_JEInternClassBase):

    _instances: dict[int, _Self] = {}
    _cache: dict[int, str] = {}

    @classmethod
    def _build_cache(cls) -> None:
        if cls._cache:
            return

        for c in range(ord("a"), ord("z") + 1):
            code = getattr(_JEInternPyGame, f"K_{chr(c)}")
            cls._cache[code] = chr(c).upper()

        for i in range(10):
            code = getattr(_JEInternPyGame, f"K_{i}")
            cls._cache[code] = str(i)

        cls._cache.update({
            _JEInternPyGame.K_RETURN: "ENTER",
            _JEInternPyGame.K_BACKSPACE: "BACKSPACE",
            _JEInternPyGame.K_DELETE: "DELETE",
            _JEInternPyGame.K_TAB: "TAB",
            _JEInternPyGame.K_ESCAPE: "ESCAPE",
            _JEInternPyGame.K_UP: "UP",
            _JEInternPyGame.K_DOWN: "DOWN",
            _JEInternPyGame.K_LEFT: "LEFT",
            _JEInternPyGame.K_RIGHT: "RIGHT",
        })

    def __new__(
            cls,
            key: int
        ) -> _Self:
        if key not in cls._instances:
            cls._instances[key] = super().__new__(cls)
        return cls._instances[key]

    def __init__(
            self,
            key: int
        ) -> None:
        if hasattr(self, "_initialized"):
            return

        super().__init__()
        self._key = int(key)
        self._build_cache()
        self._name = self._cache.get(self._key, f"UNKNOWN_KEY({self._key})")
        self._initialized = True

    @property
    def name(self) -> str:
        return self._name

    def __int__(self) -> int:
        return self._key

    def __eq__(self, other):
        return int(self) == int(other)

JEKey_A: JEKey = JEKey(_JEInternPyGame.K_a)
JEKey_B: JEKey = JEKey(_JEInternPyGame.K_b)
JEKey_C: JEKey = JEKey(_JEInternPyGame.K_c)
JEKey_D: JEKey = JEKey(_JEInternPyGame.K_d)
JEKey_E: JEKey = JEKey(_JEInternPyGame.K_e)
JEKey_F: JEKey = JEKey(_JEInternPyGame.K_f)
JEKey_G: JEKey = JEKey(_JEInternPyGame.K_g)
JEKey_H: JEKey = JEKey(_JEInternPyGame.K_h)
JEKey_I: JEKey = JEKey(_JEInternPyGame.K_i)
JEKey_J: JEKey = JEKey(_JEInternPyGame.K_j)
JEKey_K: JEKey = JEKey(_JEInternPyGame.K_k)
JEKey_L: JEKey = JEKey(_JEInternPyGame.K_l)
JEKey_M: JEKey = JEKey(_JEInternPyGame.K_m)
JEKey_N: JEKey = JEKey(_JEInternPyGame.K_n)
JEKey_O: JEKey = JEKey(_JEInternPyGame.K_o)
JEKey_P: JEKey = JEKey(_JEInternPyGame.K_p)
JEKey_Q: JEKey = JEKey(_JEInternPyGame.K_q)
JEKey_R: JEKey = JEKey(_JEInternPyGame.K_r)
JEKey_S: JEKey = JEKey(_JEInternPyGame.K_s)
JEKey_T: JEKey = JEKey(_JEInternPyGame.K_t)
JEKey_U: JEKey = JEKey(_JEInternPyGame.K_u)
JEKey_V: JEKey = JEKey(_JEInternPyGame.K_v)
JEKey_W: JEKey = JEKey(_JEInternPyGame.K_w)
JEKey_X: JEKey = JEKey(_JEInternPyGame.K_x)
JEKey_Y: JEKey = JEKey(_JEInternPyGame.K_y)
JEKey_Z: JEKey = JEKey(_JEInternPyGame.K_z)
JEKey_0: JEKey = JEKey(_JEInternPyGame.K_0)
JEKey_1: JEKey = JEKey(_JEInternPyGame.K_1)
JEKey_2: JEKey = JEKey(_JEInternPyGame.K_2)
JEKey_3: JEKey = JEKey(_JEInternPyGame.K_3)
JEKey_4: JEKey = JEKey(_JEInternPyGame.K_4)
JEKey_5: JEKey = JEKey(_JEInternPyGame.K_5)
JEKey_6: JEKey = JEKey(_JEInternPyGame.K_6)
JEKey_7: JEKey = JEKey(_JEInternPyGame.K_7)
JEKey_8: JEKey = JEKey(_JEInternPyGame.K_8)
JEKey_9: JEKey = JEKey(_JEInternPyGame.K_9)
JEKey_Enter: JEKey = JEKey(_JEInternPyGame.K_RETURN)
JEKey_Backspace: JEKey = JEKey(_JEInternPyGame.K_BACKSPACE)
JEKey_Delete: JEKey = JEKey(_JEInternPyGame.K_DELETE)
JEKey_Tab: JEKey = JEKey(_JEInternPyGame.K_TAB)
JEKey_Escape: JEKey = JEKey(_JEInternPyGame.K_ESCAPE,)
JEKey_Up: JEKey = JEKey(_JEInternPyGame.K_UP)
JEKey_Down: JEKey = JEKey(_JEInternPyGame.K_DOWN)
JEKey_Left: JEKey = JEKey(_JEInternPyGame.K_LEFT)
JEKey_Right: JEKey = JEKey(_JEInternPyGame.K_RIGHT)

@_final
class JEMouse(_JEInternClassBase):

    _instances: dict[int, _Self] = {}

    _cache = {
        _JEInternPyGame.BUTTON_LEFT: "LEFT",
        _JEInternPyGame.BUTTON_MIDDLE: "MIDDLE",
        _JEInternPyGame.BUTTON_RIGHT: "RIGHT",
    }

    def __new__(
            cls,
            button: int
        ) -> _Self:
        if button not in cls._instances:
            cls._instances[button] = super().__new__(cls)
        return cls._instances[button]

    def __init__(
            self,
            button: int
        ) -> None:
        if hasattr(self, "_initialized"):
            return

        super().__init__()
        self._button = int(button)
        self._name = self._cache.get(self._button, f"BUTTON_{self._button}")
        self._initialized = True

    @property
    def name(self) -> str:
        return self._name

    def __int__(self) -> int:
        return self._button

    def __eq__(self, other):
        return int(self) == int(other)

JEMouse_Left: JEMouse = JEMouse(_JEInternPyGame.BUTTON_LEFT)
JEMouse_Middle: JEMouse = JEMouse(_JEInternPyGame.BUTTON_MIDDLE)
JEMouse_Right: JEMouse = JEMouse(_JEInternPyGame.BUTTON_RIGHT)

@_final
class JEEvent(_JEInternClassBase):

    def __init__(
            self,
            event: _JEInternPyGame.event.Event
        ) -> None:
        super().__init__()
        self._event = event

        self._type: int = event.type
        self._key: int | None = getattr(event, "key", None)
        self._button: int | None = getattr(event, "button", None)
        self._pos = getattr(event, "pos", None)

    @property
    def type_code(self) -> JEEventCode:
        return JEEventCode(self._type)

    @property
    def key_code(self) -> JEKey | None:
        return JEKey(self._key) if self._key is not None else None

    @property
    def mouse_code(self) -> JEMouse | None:
        return JEMouse(self._button) if self._button is not None else None

@_final
class JEEventWatcher(_JEInternClassBase):

    def __init__(
        self,
        on: JEEventCode | JEKey | JEMouse | list[JEEventCode | JEKey | JEMouse],
        do: _Callable[["JEGame", JEEvent], None],
    ) -> None:

        if not isinstance(on, (JEEventCode, JEKey, JEMouse, list)):
            raise _JTKInternError.Error.ErrorType(
                "on must be JEEventCode, JEKey, JEMouse or list"
            )

        super().__init__()
        self._on = on if isinstance(on, list) else [on]
        self._do = do

    def _match_rule(self, rule, event: JEEvent) -> _JEBool:
        if isinstance(rule, JEEventCode):
            return _JEBool(event.type_code == rule)

        if isinstance(rule, JEKey):
            return _JEBool(
                event.type_code == JEEvtKeyDown
                and event.key_code is not None
                and event.key_code == rule
            )

        if isinstance(rule, JEMouse):
            return _JEBool(
                event.type_code == JEEvtMouseButtonDown
                and event.mouse_code is not None
                and event.mouse_code == rule
            )

        return _JEBool(0)

    def match(self, event: JEEvent) -> bool:
        for rule in self._on:
            if self._match_rule(rule, event):
                return True
        return False

    def __call__(self, game: "JEGame", event: JEEvent) -> None:
        self._do(game, event)

    @property
    def on(self) -> list[JEEventCode | JEKey | JEMouse]:
        return self._on

    @property
    def do(self) -> str:
        return f"{self._do.__name__}(JEGame, JEEvent)"

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

    @property
    def watchers(self) -> list[JEEventWatcher]:
        return self._watchers

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
        events: list[JEEvent] = [JEEvent(evt) for evt in _JEInternPyGame.event.get()]

        for event in events:
            for watcher in self._watchers:
                if watcher.match(event):
                    watcher(game, event)

    def __deepcopy__(
            self,
            memo
        ):
        return self
