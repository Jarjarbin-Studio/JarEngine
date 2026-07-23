# =============================================================================
# JarEngine - Python Game Engine Wrapper (PyGame-based)
# =============================================================================
#
# JarEngine is a lightweight game framework built on top of PyGame
# that simplifies usage while providing higher-level abstractions for
# game development and prototyping.
#
# =============================================================================
# Version: jarengine-v1.10
# Author: Jarjarbin Studio
# Licence: GPL v3
# =============================================================================
#
# This engine is inspired by PyGame, modern game engine design patterns,
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
# This is NOT PyGame itself.
# It is a custom abstraction layer built on top of PyGame.
#
# =============================================================================

from __future__ import annotations

from typing import (
    final as _final,
    Callable as _Callable
)

from jarengine.events.keyboard import JEKeyCode
from jarengine.events.event import JEEventCode as _JEEventCode
from jarengine.interns.base_classe import JEInternBaseClass as _JEInternBaseClass
from jarengine.interns import PGExtern as _PGExtern
from jarengine.systems.bool import JEBool as _JEBool
from jarengine.interns.decorators import documentation as _documentation
from jarengine.interns.helpers import (
    assertion_type as _assertion_type,
    safe_cast as _safe_cast
)
import jarengine.interns.log as _log

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
            _PGExtern.BUTTON_LEFT: "Left",
            _PGExtern.BUTTON_MIDDLE: "Middle",
            _PGExtern.BUTTON_RIGHT: "Right",
        })

    def __new__(cls, mouse = None):
        if mouse is None:
            return super().__new__(cls)

        if mouse not in cls._instances:
            cls._instances[mouse] = super().__new__(cls)

        return cls._instances[mouse]

    def __init__(self, mouse = None):

        if mouse:
            mouse = _safe_cast(_assertion_type(mouse, (JEMouseCode, int), "mouse must be of type 'int'"), int)

        if hasattr(self, "_initialized") or mouse is None:
            return

        super().__init__()
        self._mouse = int(mouse)
        self._build_cache()
        self._name = self._name_cache.get(self._mouse, f"MouseUnknown({self._mouse})")
        self._initialized = True

        _log.log("DEBUG", "OBJECT", f"JEMouseCode: Created", self.jeid, mouse)

    def __int__(self):
        return self._mouse

    def __list__(self):
        return [int(self)]

    def __str__(self):
        return self._name

    @property
    def name(self):
        return self._name

    def __or__(self, other):

        other = _safe_cast(_assertion_type(other, JEMouseCode, "other must be of type 'JEMouseCode'"), JEMouseCode)

        return JEMouseCodeGroup([self, other])

    def __eq__(self, other):

        other = _safe_cast(_assertion_type(other, (JEMouseCode, int), "other must be of type 'JEMouseCode'"), JEKeyCode)

        return _JEBool(int(self) == int(other))

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

        mouses = _safe_cast(_assertion_type(mouses, list, "events must be of type 'list'"), list)

        super().__init__()
        self._mouses = list(dict.fromkeys(mouses))

        _log.log("DEBUG", "OBJECT", f"JEMouseCodeGroup: Created", self.jeid, mouses)

    def __or__(self, other):

        other = _safe_cast(_assertion_type(other, (JEMouseCode, JEMouseCodeGroup), "other must be of type 'JEMouseCode' or 'JEMouseCodeGroup'"), JEMouseCodeGroup)

        if isinstance(other, JEMouseCode):
            return JEMouseCodeGroup([*self._mouses, other])

        return JEMouseCodeGroup([*self._mouses, *other._mouses])

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

        _assertion_type(on, (JEMouseCode, list, JEMouseCodeGroup), "on must be of type 'JEMouseCode', 'list' or 'JEMouseCodeGroup'", True)
        _assertion_type(do, _Callable, "do must be of type 'Callable'")
        on_press = _safe_cast( _assertion_type(on_press, _JEBool, "on_press must be of type 'JEBool'"), _JEBool)

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

        _log.log("DEBUG", "OBJECT", f"JEMouseWatcher: Created", self.jeid, on, f"{do.__name__}", on_press)

    def match(self, event):

        if event.type == self._on_param:
            for rule in self._on:
                if event.mouse == rule:
                    return True
        return False

    def __call__(self, game, event):

        _log.log("DEBUG", "EVENT", f"JEMouseWatcher: Event triggered", self.jeid, game, event)

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
