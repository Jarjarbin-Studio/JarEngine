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
    JEInternPyGame as _JEInternPyGame,
    JTKInternError as _JTKInternError
)

@_final
class JEKeyCode(_JEInternClassBase):

    _instances: dict[int, _Self] = {}
    _name_cache: dict[int, str] = {}

    @classmethod
    def _build_cache(cls) -> None:
        if cls._name_cache:
            return

        for c in range(ord("a"), ord("z") + 1):
            code = getattr(_JEInternPyGame, f"K_{chr(c)}")
            cls._name_cache[code] = chr(c).upper()

        for i in range(10):
            code = getattr(_JEInternPyGame, f"K_{i}")
            cls._name_cache[code] = str(i)

        cls._name_cache.update({
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
            key: int | None = None
        ) -> _Self:
        if key is None:
            return super().__new__(cls)

        if key not in cls._instances:
            cls._instances[key] = super().__new__(cls)

        return cls._instances[key]

    def __init__(
            self,
            key: int | None = None
        ) -> None:
        if hasattr(self, "_initialized") or key is None:
            return

        super().__init__()
        self._key = int(key)
        self._build_cache()
        self._name = self._name_cache.get(self._key, f"KeyUnknown({self._key})")
        self._initialized = True

    def __int__(self) -> int:
        return self._key

    @property
    def name(self) -> str:
        return self._name

    def __or__(
            self,
            other: JEKeyCode
        ) -> JEKeyCodeGroup:

        if not isinstance(other, JEKeyCode):
            raise _JTKInternError.Error.ErrorType(
                "\nOther must be JEKeyCode"
            )

        return JEKeyCodeGroup([self, other])

    def __eq__(self, other) -> bool:
        if not isinstance(other, JEKeyCode):
            return NotImplemented
        return self._key == other._key

    def __hash__(self) -> int:
        return hash(self._key)

class JEKeyCodeGroup(_JEInternClassBase):

    def __init__(
            self,
            keys: list[JEKeyCode]
        ):
        super().__init__()
        self._keys: list[JEKeyCode] = list(dict.fromkeys(keys))

    def __or__(
            self,
            other
        ):
        if isinstance(other, JEKeyCode):
            return JEKeyCodeGroup([*self._keys, other])

        if isinstance(other, JEKeyCodeGroup):
            return JEKeyCodeGroup([*self._keys, *other._keys])

        raise _JTKInternError.error.ErrorType(
            "\nInvalid type for union"
        )

    def __iter__(self):
        return iter(self._keys)

    @property
    def keys(self):
        return self._keys

@_final
class JEKeyWatcher(_JEInternClassBase):

    def __init__(
        self,
        on: JEKeyCode | list[JEKeyCode] | JEKeyCodeGroup,
        do: _Callable[["JEGame", "JEEvent"], None]
    ) -> None:

        if not isinstance(on, (JEKeyCode, list, JEKeyCodeGroup)):
            raise _JTKInternError.Error.ErrorType(
                "\nOn must be JEEventCode, list or JEKeyCodeGroup"
            )

        super().__init__()
        self._on: JEKeyCodeGroup = (
            on
            if isinstance(on, JEKeyCodeGroup) else
            JEKeyCodeGroup(
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
    def on(self) -> JEKeyCodeGroup:
        return self._on

    @property
    def do(self) -> str:
        return f"{self._do.__name__}(JEGame, JEEvent)"

JEKey_A: JEKeyCode = JEKeyCode(_JEInternPyGame.K_a)
JEKey_B: JEKeyCode = JEKeyCode(_JEInternPyGame.K_b)
JEKey_C: JEKeyCode = JEKeyCode(_JEInternPyGame.K_c)
JEKey_D: JEKeyCode = JEKeyCode(_JEInternPyGame.K_d)
JEKey_E: JEKeyCode = JEKeyCode(_JEInternPyGame.K_e)
JEKey_F: JEKeyCode = JEKeyCode(_JEInternPyGame.K_f)
JEKey_G: JEKeyCode = JEKeyCode(_JEInternPyGame.K_g)
JEKey_H: JEKeyCode = JEKeyCode(_JEInternPyGame.K_h)
JEKey_I: JEKeyCode = JEKeyCode(_JEInternPyGame.K_i)
JEKey_J: JEKeyCode = JEKeyCode(_JEInternPyGame.K_j)
JEKey_K: JEKeyCode = JEKeyCode(_JEInternPyGame.K_k)
JEKey_L: JEKeyCode = JEKeyCode(_JEInternPyGame.K_l)
JEKey_M: JEKeyCode = JEKeyCode(_JEInternPyGame.K_m)
JEKey_N: JEKeyCode = JEKeyCode(_JEInternPyGame.K_n)
JEKey_O: JEKeyCode = JEKeyCode(_JEInternPyGame.K_o)
JEKey_P: JEKeyCode = JEKeyCode(_JEInternPyGame.K_p)
JEKey_Q: JEKeyCode = JEKeyCode(_JEInternPyGame.K_q)
JEKey_R: JEKeyCode = JEKeyCode(_JEInternPyGame.K_r)
JEKey_S: JEKeyCode = JEKeyCode(_JEInternPyGame.K_s)
JEKey_T: JEKeyCode = JEKeyCode(_JEInternPyGame.K_t)
JEKey_U: JEKeyCode = JEKeyCode(_JEInternPyGame.K_u)
JEKey_V: JEKeyCode = JEKeyCode(_JEInternPyGame.K_v)
JEKey_W: JEKeyCode = JEKeyCode(_JEInternPyGame.K_w)
JEKey_X: JEKeyCode = JEKeyCode(_JEInternPyGame.K_x)
JEKey_Y: JEKeyCode = JEKeyCode(_JEInternPyGame.K_y)
JEKey_Z: JEKeyCode = JEKeyCode(_JEInternPyGame.K_z)
JEKey_0: JEKeyCode = JEKeyCode(_JEInternPyGame.K_0)
JEKey_1: JEKeyCode = JEKeyCode(_JEInternPyGame.K_1)
JEKey_2: JEKeyCode = JEKeyCode(_JEInternPyGame.K_2)
JEKey_3: JEKeyCode = JEKeyCode(_JEInternPyGame.K_3)
JEKey_4: JEKeyCode = JEKeyCode(_JEInternPyGame.K_4)
JEKey_5: JEKeyCode = JEKeyCode(_JEInternPyGame.K_5)
JEKey_6: JEKeyCode = JEKeyCode(_JEInternPyGame.K_6)
JEKey_7: JEKeyCode = JEKeyCode(_JEInternPyGame.K_7)
JEKey_8: JEKeyCode = JEKeyCode(_JEInternPyGame.K_8)
JEKey_9: JEKeyCode = JEKeyCode(_JEInternPyGame.K_9)
JEKey_Enter: JEKeyCode = JEKeyCode(_JEInternPyGame.K_RETURN)
JEKey_Backspace: JEKeyCode = JEKeyCode(_JEInternPyGame.K_BACKSPACE)
JEKey_Delete: JEKeyCode = JEKeyCode(_JEInternPyGame.K_DELETE)
JEKey_Tab: JEKeyCode = JEKeyCode(_JEInternPyGame.K_TAB)
JEKey_Escape: JEKeyCode = JEKeyCode(_JEInternPyGame.K_ESCAPE,)
JEKey_Up: JEKeyCode = JEKeyCode(_JEInternPyGame.K_UP)
JEKey_Down: JEKeyCode = JEKeyCode(_JEInternPyGame.K_DOWN)
JEKey_Left: JEKeyCode = JEKeyCode(_JEInternPyGame.K_LEFT)
JEKey_Right: JEKeyCode = JEKeyCode(_JEInternPyGame.K_RIGHT)
