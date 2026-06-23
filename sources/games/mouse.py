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

from sources.games.event import (
    JEEventCode as _JEEventCode,
    JEEvtMouseDown as _JEEvtMouseDown,
    JEEvtMouseUp as _JEEvtMouseUp
)
from sources.interns.base_classe import JEInternClassBase as _JEInternClassBase
from sources.interns import (
    PGIntern as _PyGameIntern,
    JTKInternError as _JTKInternError
)
from sources.systems.bool import JEBool as _JEBool
from sources.interns.decorators import documentation as _documentation

@_documentation
@_final
class JEMouseCode(_JEInternClassBase):
    """Mouse code"""

    _instances: dict[int, _Self] = {}
    _name_cache: dict[int, str] = {}

    @classmethod
    def _build_cache(cls) -> None:
        if cls._name_cache:
            return

        cls._name_cache.update({
            _PyGameIntern.BUTTON_LEFT: "LEFT",
            _PyGameIntern.BUTTON_MIDDLE: "MIDDLE",
            _PyGameIntern.BUTTON_RIGHT: "RIGHT",
        })

    def __new__(
            cls,
            mouse: int | None = None
        ) -> _Self:
        """Instances clamping"""
        if mouse is None:
            return super().__new__(cls)

        if mouse not in cls._instances:
            cls._instances[mouse] = super().__new__(cls)

        return cls._instances[mouse]

    def __init__(
            self,
            mouse: int | None = None
        ) -> None:
        """JEMouseCode creator"""
        if hasattr(self, "_initialized") or mouse is None:
            return

        super().__init__()
        self._mouse = int(mouse)
        self._build_cache()
        self._name = self._name_cache.get(self._mouse, f"MouseUnknown({self._mouse})")
        self._initialized = True

    def __int__(self) -> int:
        """Get mouse code"""
        return self._mouse

    @property
    def name(self) -> str:
        """Get mouse name"""
        return self._name

    def __or__(
            self,
            other: JEMouseCode
        ) -> JEMouseCodeGroup:
        """Allows same synthax as union (create a JEMouseCodeGroup)"""

        if not isinstance(other, JEMouseCode):
            raise _JTKInternError.Error.ErrorType(
                "\nOther must be JEMouseCode"
            )

        return JEMouseCodeGroup([self, other])

    def __eq__(self, other) -> bool:
        """Compare 2 mouse"""
        if not isinstance(other, JEMouseCode):
            return NotImplemented
        return self._mouse == other._mouse

    def __hash__(self) -> int:
        """Hash a mouse"""
        return hash(self._mouse)

@_documentation
@_final
class JEMouseCodeGroup(_JEInternClassBase):
    """Mouse code group"""

    def __init__(
            self,
            mouses: list[JEMouseCode]
        ):
        """JEMouseCodeGroup creator"""
        super().__init__()
        self._mouses: list[JEMouseCode] = list(dict.fromkeys(mouses))

    def __or__(
            self,
            other
        ):
        """Allows same synthax as union (create a JEMouseCodeGroup)"""

        if isinstance(other, JEMouseCode):
            return JEMouseCodeGroup([*self._mouses, other])

        if isinstance(other, JEMouseCodeGroup):
            return JEMouseCodeGroup([*self._mouses, *other._mouses])

        raise _JTKInternError.error.ErrorType(
            "\nInvalid type for union"
        )

    def __iter__(self):
        """Get the iterator of mouses"""
        return iter(self._mouses)

    @property
    def mouses(self):
        """Get the key mouse"""
        return self._mouses

@_documentation
@_final
class JEMouseWatcher(_JEInternClassBase):
    """Mouse event watcher"""

    def __init__(
        self,
        on: JEMouseCode | list[JEMouseCode] | JEMouseCodeGroup,
        do: _Callable[["JEGame", "JEEvent"], None],
        on_press: _JEBool = _JEBool(1)
    ) -> None:
        """JEMouseWatcher creator"""

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
        self._on_param: _JEEventCode = (
            _JEEvtMouseDown
            if on_press else
            _JEEvtMouseUp
        )
        self._do: _Callable[["JEGame", "JEEvent"], None] = do

    def match(self, event: "JEEvent") -> bool:
        """Check for mouse matches"""
        if event.type_code == self._on_param:
            for rule in self._on:
                if event.mouse_code == rule:
                    return True
        return False

    def __call__(self, game: "JEGame", event: "JEEvent") -> None:
        """Call saved function"""
        self._do(game, event)

    @property
    def on(self) -> JEMouseCodeGroup:
        """Get watched mouses"""
        return self._on

    @property
    def params(self) -> _JEEventCode:
        """Get event parameter"""
        return self._on_param

    @property
    def do(self) -> str:
        """Get seved function (as str)"""
        return f"{self._do.__name__}(JEGame, JEEvent)"

JEMouse_Left: JEMouseCode = JEMouseCode(_PyGameIntern.BUTTON_LEFT)
JEMouse_Middle: JEMouseCode = JEMouseCode(_PyGameIntern.BUTTON_MIDDLE)
JEMouse_Right: JEMouseCode = JEMouseCode(_PyGameIntern.BUTTON_RIGHT)
