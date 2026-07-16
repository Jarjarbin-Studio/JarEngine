# =============================================================================
# JarEngine - Python Game Engine Wrapper (Pygame-based)
# =============================================================================
#
# JarEngine is a lightweight game framework built on top of Pygame
# that simplifies usage while providing higher-level abstractions for
# game development and prototyping.
#
# =============================================================================
# Version: jarengine-v1.7
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

from typing import final as _final

from jarengine.interns.base_classe import JEInternBaseClass as _JEInternBaseClass
from jarengine.interns import (
    JTKExternError as _JTKExternError,
    PGExtern as _PGExtern
)
from jarengine.systems.bool import JEBool as _JEBool
from jarengine.interns.decorators import documentation as _documentation

@_documentation
@_final
class JEEventCode(_JEInternBaseClass):

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
            _PGExtern.QUIT: "quit",
            _PGExtern.HIDDEN: "Hidden",
            _PGExtern.KEYDOWN: "KeyDown",
            _PGExtern.KEYUP: "KeyUp",
            _PGExtern.MOUSEBUTTONDOWN: "MouseDown",
            _PGExtern.MOUSEBUTTONUP: "MouseUp"
        })

    def __new__(cls, event = None):
        if event is None:
            return super().__new__(cls)

        if event not in cls._instances:
            cls._instances[event] = super().__new__(cls)

        return cls._instances[event]

    def __init__(self, event = None):
        if hasattr(self, "_initialized") or event is None:
            return

        super().__init__()
        self._event = int(event)
        self._build_cache()
        self._name = self._name_cache.get(self._event, f"EventUnknown({self._event})")
        self._initialized = True

    def __int__(self):
        return self._event

    @property
    def name(self):
        return self._name

    def __or__(self, other):
        if not isinstance(other, JEEventCode):
            raise _JTKExternError.Error.ErrorType(
                "\nOther must be JEEventCode"
            )

        return JEEventCodeGroup([self, other])

    def __eq__(self, other):
        if not isinstance(other, JEEventCode):
            return NotImplemented
        return _JEBool(int(self) == int(other))

    def __hash__(self):
        return hash(self._event)

@_documentation
@_final
class JEEventCodeGroup(_JEInternBaseClass):

    __recursive__ = False

    def __init__(self, events):
        super().__init__()
        self._events = list(dict.fromkeys(events))

    def __or__(self, other):
        if isinstance(other, JEEventCode):
            return JEEventCodeGroup([*self, other])

        if isinstance(other, JEEventCodeGroup):
            return JEEventCodeGroup([*self, *other])

        raise _JTKExternError.error.ErrorType(
            "\nInvalid type for union"
        )

    def __iter__(self):
        return iter(self._events)

    @property
    def events(self):
        return self._events

@_documentation
@_final
class JEEventWatcher(_JEInternBaseClass):

    __recursive__ = False

    def __init__(self, on, do):
        if not isinstance(on, (JEEventCode, list, JEEventCodeGroup)):
            raise _JTKExternError.Error.ErrorType(
                "\nOn must be JEEventCode, list or JEEventCodeGroup"
            )

        super().__init__()
        self._on = (
            on
            if isinstance(on, JEEventCodeGroup) else
            JEEventCodeGroup(
                on
                if isinstance(on, list) else
                [on]
            )
        )
        self._do = do

    def match(self, event):
        for rule in self._on:
            if event.type == rule:
                return True
        return False

    def __call__(self, game, event):
        self._do(game, event)

    @property
    def on(self):
        return self._on

    @property
    def do(self):
        return f"{self._do.__name__}(JEGame, JEEvent)"
