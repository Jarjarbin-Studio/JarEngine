"""
    JarEngine - Python Game Engine Wrapper (Pygame-based)

    JarEngine is a lightweight game framework built on top of Pygame
    that simplifies usage while providing higher-level abstractions for
    game development and prototyping.

    Version: jarengine-v1.6
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

from typing import final as _final

from jarengine.events.event import JEEventCode as _JEEventCode
from jarengine.interns.base_classe import JEInternBaseClass as _JEInternBaseClass
from jarengine.interns import (
    PGExtern as _PGExtern,
    JTKExternError as _JTKExternError
)
from jarengine.systems.bool import JEBool as _JEBool
from jarengine.interns.decorators import documentation as _documentation

@_documentation
@_final
class JEMouseCode(_JEInternBaseClass):

    _instances = {}
    _name_cache = {}

    __instance_policy__ = "singleton"
    __instance_limit__ = None
    __recursive__ = False

    @classmethod
    def _build_cache(cls):
        if cls._name_cache:
            return

        cls._name_cache.update({
            _PGExtern.BUTTON_LEFT: "LEFT",
            _PGExtern.BUTTON_MIDDLE: "MIDDLE",
            _PGExtern.BUTTON_RIGHT: "RIGHT",
        })

    def __new__(cls, mouse = None):
        if mouse is None:
            return super().__new__(cls)

        if mouse not in cls._instances:
            cls._instances[mouse] = super().__new__(cls)

        return cls._instances[mouse]

    def __init__(self, mouse = None):
        if hasattr(self, "_initialized") or mouse is None:
            return

        super().__init__()
        self._mouse = int(mouse)
        self._build_cache()
        self._name = self._name_cache.get(self._mouse, f"MouseUnknown({self._mouse})")
        self._initialized = True

    def __int__(self):
        return self._mouse

    @property
    def name(self):
        return self._name

    def __or__(self, other):
        if not isinstance(other, JEMouseCode):
            raise _JTKExternError.Error.ErrorType(
                "\nOther must be JEMouseCode"
            )

        return JEMouseCodeGroup([self, other])

    def __eq__(self, other):
        if not isinstance(other, JEMouseCode):
            return NotImplemented
        return int(self) == int(other)

    def __hash__(self):
        return hash(self._mouse)

@_documentation
@_final
class JEMouseCodeGroup(_JEInternBaseClass):

    __recursive__ = False

    def __init__(
            self,
            mouses
        ):
        super().__init__()
        self._mouses = list(dict.fromkeys(mouses))

    def __or__(self, other):
        if isinstance(other, JEMouseCode):
            return JEMouseCodeGroup([*self._mouses, other])

        if isinstance(other, JEMouseCodeGroup):
            return JEMouseCodeGroup([*self._mouses, *other._mouses])

        raise _JTKExternError.error.ErrorType(
            "\nInvalid type for union"
        )

    def __iter__(self):
        return iter(self._mouses)

    @property
    def mouses(self):
        return self._mouses

@_documentation
@_final
class JEMouseWatcher(_JEInternBaseClass):

    __recursive__ = False

    def __init__(self, on, do, on_press = _JEBool(1)):
        if not isinstance(on, (JEMouseCode, list, JEMouseCodeGroup)):
            raise _JTKExternError.Error.ErrorType(
                "\nOn must be JEEventCode, list or JEKeyCodeGroup"
            )

        super().__init__()
        self._on = (
            on
            if isinstance(on, JEMouseCodeGroup) else
            JEMouseCodeGroup(
                on
                if isinstance(on, list) else
                [on]
            )
        )
        self._on_param = (
            _JEEventCode(_PGExtern.MOUSEBUTTONDOWN)
            if on_press else
            _JEEventCode(_PGExtern.MOUSEBUTTONUP)
        )
        self._do = do

    def match(self, event):
        if event.type == self._on_param:
            for rule in self._on:
                if event.mouse == rule:
                    return True
        return False

    def __call__(self, game, event):
        self._do(game, event)

    @property
    def on(self):
        return self._on

    @property
    def params(self):
        return self._on_param

    @property
    def do(self):
        return f"{self._do.__name__}(JEGame, JEEvent)"
