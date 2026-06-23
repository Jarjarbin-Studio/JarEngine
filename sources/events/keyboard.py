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

from sources.events.event import JEEventCode as _JEEventCode
from sources.interns.base_classe import JEInternClassBase as _JEInternClassBase
from sources.interns import (
    PGIntern as _PGIntern,
    JTKInternError as _JTKInternError
)
from sources.systems.bool import JEBool as _JEBool
from sources.interns.decorators import documentation as _documentation

@_documentation
@_final
class JEKeyCode(_JEInternClassBase):
    """Key code"""

    _instances: dict[int, _Self] = {}
    _name_cache: dict[int, str] = {}

    @classmethod
    def _build_cache(cls) -> None:
        if cls._name_cache:
            return

        for c in range(ord("a"), ord("z") + 1):
            code = getattr(_PGIntern, f"K_{chr(c)}")
            cls._name_cache[code] = chr(c).upper()

        for i in range(10):
            code = getattr(_PGIntern, f"K_{i}")
            cls._name_cache[code] = str(i)

        cls._name_cache.update({
            _PGIntern.K_RETURN: "ENTER",
            _PGIntern.K_BACKSPACE: "BACKSPACE",
            _PGIntern.K_DELETE: "DELETE",
            _PGIntern.K_TAB: "TAB",
            _PGIntern.K_ESCAPE: "ESCAPE",
            _PGIntern.K_UP: "UP",
            _PGIntern.K_DOWN: "DOWN",
            _PGIntern.K_LEFT: "LEFT",
            _PGIntern.K_RIGHT: "RIGHT",
        })

    def __new__(
            cls,
            key: int | None = None
        ) -> _Self:
        """Instances clamping"""
        if key is None:
            return super().__new__(cls)

        if key not in cls._instances:
            cls._instances[key] = super().__new__(cls)

        return cls._instances[key]

    def __init__(
            self,
            key: int | None = None
        ) -> None:
        """JEKeyCode creator"""
        if hasattr(self, "_initialized") or key is None:
            return

        super().__init__()
        self._key = int(key)
        self._build_cache()
        self._name = self._name_cache.get(self._key, f"KeyUnknown({self._key})")
        self._initialized = True

    def __int__(self) -> int:
        """Get key code"""
        return self._key

    @property
    def name(self) -> str:
        """Get key name"""
        return self._name

    def __or__(
            self,
            other: JEKeyCode
        ) -> JEKeyCodeGroup:
        """Allows same synthax as union (create a JEKeyCodeGroup)"""

        if not isinstance(other, JEKeyCode):
            raise _JTKInternError.Error.ErrorType(
                "\nOther must be JEKeyCode"
            )

        return JEKeyCodeGroup([self, other])

    def __eq__(self, other) -> bool:
        """Compare 2 key"""
        if not isinstance(other, JEKeyCode):
            return NotImplemented
        return int(self) == int(other)

    def __hash__(self) -> int:
        """Hash a key"""
        return hash(self._key)

@_documentation
@_final
class JEKeyCodeGroup(_JEInternClassBase):
    """Key code group"""

    def __init__(
            self,
            keys: list[JEKeyCode]
        ):
        """JEKeyCodeGroup creator"""
        super().__init__()
        self._keys: list[JEKeyCode] = list(dict.fromkeys(keys))

    def __or__(
            self,
            other
        ):
        """Allows same synthax as union (create a JEKeyCodeGroup)"""

        if isinstance(other, JEKeyCode):
            return JEKeyCodeGroup([*self._keys, other])

        if isinstance(other, JEKeyCodeGroup):
            return JEKeyCodeGroup([*self._keys, *other._keys])

        raise _JTKInternError.error.ErrorType(
            "\nInvalid type for union"
        )

    def __iter__(self):
        """Get the iterator of keys"""
        return iter(self._keys)

    @property
    def keys(self):
        """Get the key list"""
        return self._keys

@_documentation
@_final
class JEKeyWatcher(_JEInternClassBase):
    """Key event watcher"""

    def __init__(
        self,
        on: JEKeyCode | list[JEKeyCode] | JEKeyCodeGroup,
        do: _Callable[["JEGame", "JEEvent"], None],
        on_press: _JEBool = _JEBool(1)
    ) -> None:
        """JEKeyWatcher creator"""

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
        self._on_param: _JEEventCode = (
            _JEEventCode(_PGIntern.KEYDOWN)
            if on_press else
            _JEEventCode(_PGIntern.KEYUP)
        )
        self._do: _Callable[["JEGame", "JEEvent"], None] = do

    def match(self, event: "JEEvent") -> bool:
        """Check for key matches"""
        if event.type == self._on_param:
            for rule in self._on:
                if event.key == rule:
                    return True
        return False

    def __call__(self, game: "JEGame", event: "JEEvent") -> None:
        """Call saved function"""
        self._do(game, event)

    @property
    def on(self) -> JEKeyCodeGroup:
        """Get watched keys"""
        return self._on

    @property
    def params(self) -> _JEEventCode:
        """Get event parameter"""
        return self._on_param

    @property
    def do(self) -> str:
        """Get seved function (as str)"""
        return f"{self._do.__name__}(JEGame, JEEvent)"
