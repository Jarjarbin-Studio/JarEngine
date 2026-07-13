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
class JEKeyCode(_JEInternBaseClass):

    _instances = {}
    _name_cache = {}

    __instance_policy__ = "singleton"
    __instance_limit__ = None
    __recursive__ = False

    @classmethod
    def _build_cache(cls):
        if cls._name_cache:
            return

        for c in range(ord("a"), ord("z") + 1):
            code = getattr(_PGExtern, f"K_{chr(c)}")
            cls._name_cache[code] = chr(c).upper()

        for i in range(10):
            code = getattr(_PGExtern, f"K_{i}")
            cls._name_cache[code] = str(i)

        cls._name_cache.update({
            _PGExtern.K_RETURN: "ENTER",
            _PGExtern.K_BACKSPACE: "BACKSPACE",
            _PGExtern.K_DELETE: "DELETE",
            _PGExtern.K_TAB: "TAB",
            _PGExtern.K_ESCAPE: "ESCAPE",
            _PGExtern.K_UP: "UP",
            _PGExtern.K_DOWN: "DOWN",
            _PGExtern.K_LEFT: "LEFT",
            _PGExtern.K_RIGHT: "RIGHT",
        })

    def __new__(cls, key = None):
        if key is None:
            return super().__new__(cls)

        if key not in cls._instances:
            cls._instances[key] = super().__new__(cls)

        return cls._instances[key]

    def __init__(self, key = None):
        if hasattr(self, "_initialized") or key is None:
            return

        super().__init__()
        self._key = int(key)
        self._build_cache()
        self._name = self._name_cache.get(self._key, f"KeyUnknown({self._key})")
        self._initialized = True

    def __int__(self):
        return self._key

    @property
    def name(self):
        return self._name

    def __or__(self, other):
        if not isinstance(other, JEKeyCode):
            raise _JTKExternError.Error.ErrorType(
                "\nOther must be JEKeyCode"
            )

        return JEKeyCodeGroup([self, other])

    def __eq__(self, other):
        if not isinstance(other, JEKeyCode):
            return NotImplemented
        return _JEBool(int(self) == int(other))

    def __hash__(self):
        return hash(self._key)

@_documentation
@_final
class JEKeyCodeGroup(_JEInternBaseClass):

    __recursive__ = False

    def __init__(self, keys):
        super().__init__()
        self._keys = list(dict.fromkeys(keys))

    def __or__(self, other):
        if isinstance(other, JEKeyCode):
            return JEKeyCodeGroup([*self._keys, other])

        if isinstance(other, JEKeyCodeGroup):
            return JEKeyCodeGroup([*self._keys, *other._keys])

        raise _JTKExternError.error.ErrorType(
            "\nInvalid type for union"
        )

    def __iter__(self):
        return iter(self._keys)

    @property
    def keys(self):
        return self._keys

@_documentation
@_final
class JEKeyWatcher(_JEInternBaseClass):

    __recursive__ = False

    def __init__(self, on, do, on_press = _JEBool(1)):
        if not isinstance(on, (JEKeyCode, list, JEKeyCodeGroup)):
            raise _JTKExternError.Error.ErrorType(
                "\nOn must be JEEventCode, list or JEKeyCodeGroup"
            )

        super().__init__()
        self._on = (
            on
            if isinstance(on, JEKeyCodeGroup) else
            JEKeyCodeGroup(
                on
                if isinstance(on, list) else
                [on]
            )
        )
        self._on_param = (
            _JEEventCode(_PGExtern.KEYDOWN)
            if on_press else
            _JEEventCode(_PGExtern.KEYUP)
        )
        self._do = do

    def match(self, event):
        if event.type == self._on_param:
            for rule in self._on:
                if event.key == rule:
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
