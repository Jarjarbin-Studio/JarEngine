# =============================================================================
# JarEngine - Python Game Engine Wrapper (Pygame-based)
# =============================================================================
#
# JarEngine is a lightweight game framework built on top of Pygame
# that simplifies usage while providing higher-level abstractions for
# game development and prototyping.
#
# =============================================================================
# Version: jarengine-v1.8
# Author: Jarjarbin Studio
# Licence: GPL v3
# =============================================================================
#
# This engine is inspired by Pygame, modern game engine design patterns,
# and directly influenced by the architecture of NewCSFML.
#
# It is designed for educational purposes and small-to-medium game projects.
#
# It provides structured systems such as entity management, scene handling,
# render abstraction, and advanced modules like particle systems.
#
# =============================================================================
# WARNING:
# =============================================================================
#
# This is NOT Pygame itself.
# It is a custom abstraction layer built on top of Pygame.
#
# =============================================================================

from __future__ import annotations

from typing import (
    final as _final,
    Callable as _Callable
)

from jarengine.events.event import JEEventCode as _JEEventCode
from jarengine.interns.base_classe import JEInternBaseClass as _JEInternBaseClass
from jarengine.interns import (
    PGExtern as _PGExtern,
    JTKExternError as _JTKExternError
)
from jarengine.systems.bool import JEBool as _JEBool
from jarengine.interns.decorators import documentation as _documentation
from jarengine.interns.helpers import (
    assertion_type as _assertion_type,
    safe_cast as _safe_cast
)

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
            _PGExtern.K_RETURN: "Enter",
            _PGExtern.K_BACKSPACE: "Backspace",
            _PGExtern.K_DELETE: "Delete",
            _PGExtern.K_TAB: "Tab",
            _PGExtern.K_ESCAPE: "Escape",
            _PGExtern.K_UP: "Up",
            _PGExtern.K_DOWN: "Down",
            _PGExtern.K_LEFT: "Left",
            _PGExtern.K_RIGHT: "Right",
        })

    def __new__(cls, key = None):
        if key is None:
            return super().__new__(cls)

        if key not in cls._instances:
            cls._instances[key] = super().__new__(cls)

        return cls._instances[key]

    def __init__(self, key = None):

        if key:
            key = _safe_cast( _assertion_type(key, (JEKeyCode, int), "key must be of type 'int'"), int)

        if hasattr(self, "_initialized") or key is None:
            return

        super().__init__()
        self._key = int(key)
        self._build_cache()
        self._name = self._name_cache.get(self._key, f"KeyUnknown({self._key})")
        self._initialized = True

    def __int__(self):
        return self._key

    def __list__(self):
        return [int(self)]

    def __str__(self):
        return self._name

    @property
    def name(self):
        return self._name

    def __or__(self, other):

        other = _safe_cast(_assertion_type(other, JEKeyCode, "other must be of type 'JEKeyCode'"), JEKeyCode)

        return JEKeyCodeGroup([self, other])

    def __eq__(self, other):

        other = _safe_cast(_assertion_type(other, (JEKeyCode, int), "other must be of type 'JEKeyCode'"), JEKeyCode)

        return _JEBool(int(self) == int(other))

    def __hash__(self):
        return hash(self._key)

@_documentation
@_final
class JEKeyCodeGroup(_JEInternBaseClass):

    __recursive__ = False

    def __init__(self, keys):

        keys = _safe_cast(_assertion_type(keys, list, "events must be of type 'list'"), list)

        super().__init__()
        self._keys = list(dict.fromkeys(keys))

    def __or__(self, other):

        other = _safe_cast(_assertion_type(other, (JEKeyCode, JEKeyCodeGroup), "other must be of type 'JEKeyCode' or 'JEKeyCodeGroup'"), JEKeyCodeGroup)

        if isinstance(other, JEKeyCode):
            return JEKeyCodeGroup([*self._keys, other])

        return JEKeyCodeGroup([*self._keys, *other._keys])

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

        _assertion_type(on, (JEKeyCode, list, JEKeyCodeGroup), "on must be of type 'JEKeyCode', 'list' or 'JEKeyCodeGroup'", True)
        _assertion_type(do, _Callable, "do must be of type 'Callable'")
        on_press = _safe_cast(_assertion_type(on_press, _JEBool, "on_press must be of type 'JEBool'"), _JEBool)

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
