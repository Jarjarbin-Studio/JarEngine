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
class JEMouseCode(_JEInternClassBase):

    _instances: dict[int, _Self] = {}
    _name_cache: dict[int, str] = {}

    @classmethod
    def _build_cache(cls) -> None:
        if cls._name_cache:
            return

        cls._name_cache.update({
            _JEInternPyGame.BUTTON_LEFT: "LEFT",
            _JEInternPyGame.BUTTON_MIDDLE: "MIDDLE",
            _JEInternPyGame.BUTTON_RIGHT: "RIGHT",
        })

    def __new__(
            cls,
            mouse: int | None = None
        ) -> _Self:
        if mouse is None:
            return super().__new__(cls)

        if mouse not in cls._instances:
            cls._instances[mouse] = super().__new__(cls)

        return cls._instances[mouse]

    def __init__(
            self,
            mouse: int | None = None
        ) -> None:
        if hasattr(self, "_initialized") or mouse is None:
            return

        super().__init__()
        self._mouse = int(mouse)
        self._build_cache()
        self._name = self._name_cache.get(self._mouse, f"MouseUnknown({self._mouse})")
        self._initialized = True

    def __int__(self) -> int:
        return self._mouse

    @property
    def name(self) -> str:
        return self._name

    def __or__(
            self,
            other: JEMouseCode
        ) -> JEMouseCodeGroup:

        if not isinstance(other, JEMouseCode):
            raise _JTKInternError.Error.ErrorType(
                "\nOther must be JEMouseCode"
            )

        return JEMouseCodeGroup([self, other])

    def __eq__(self, other) -> bool:
        if not isinstance(other, JEMouseCode):
            return NotImplemented
        return self._mouse == other._mouse

    def __hash__(self) -> int:
        return hash(self._mouse)

class JEMouseCodeGroup(_JEInternClassBase):

    def __init__(
            self,
            mouses: list[JEMouseCode]
        ):
        super().__init__()
        self._mouses: list[JEMouseCode] = list(dict.fromkeys(mouses))

    def __or__(
            self,
            other
        ):
        if isinstance(other, JEMouseCode):
            return JEMouseCodeGroup([*self._mouses, other])

        if isinstance(other, JEMouseCodeGroup):
            return JEMouseCodeGroup([*self._mouses, *other._mouses])

        raise _JTKInternError.error.ErrorType(
            "\nInvalid type for union"
        )

    def __iter__(self):
        return iter(self._mouses)

    @property
    def mouses(self):
        return self._mouses

@_final
class JEMouseWatcher(_JEInternClassBase):

    def __init__(
        self,
        on: JEMouseCode | list[JEMouseCode] | JEMouseCodeGroup,
        do: _Callable[["JEGame", "JEEvent"], None]
    ) -> None:

        if not isinstance(on, (JEMouseCode, list, JEMouseCodeGroup)):
            raise _JTKInternError.Error.ErrorType(
                "\nOn must be JEEventCode, list or JEKeyCodeGroup"
            )

        super().__init__()
        self._on: JEMouseCodeGroup = (
            on
            if isinstance(on, JEMouseCodeGroup) else
            JEMouseCodeGroup(
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
    def on(self) -> JEMouseCodeGroup:
        return self._on

    @property
    def do(self) -> str:
        return f"{self._do.__name__}(JEGame, JEEvent)"

JEMouse_Left: JEMouseCode = JEMouseCode(_JEInternPyGame.BUTTON_LEFT)
JEMouse_Middle: JEMouseCode = JEMouseCode(_JEInternPyGame.BUTTON_MIDDLE)
JEMouse_Right: JEMouseCode = JEMouseCode(_JEInternPyGame.BUTTON_RIGHT)
