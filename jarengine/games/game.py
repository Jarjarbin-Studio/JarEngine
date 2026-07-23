# =============================================================================
# JarEngine - Python Game Engine Wrapper (PyGame-based)
# =============================================================================
#
# JarEngine is a lightweight game framework built on top of PyGame
# that simplifies usage while providing higher-level abstractions for
# game development and prototyping.
#
# =============================================================================
# Version: jarengine-v1.8
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

from typing import final as _final

from jarengine.games.window import JEWindow as _JEWindow
from jarengine.games.input import JEInput as _JEInput
from jarengine.events.manager import JEEventHandler as _JEEventHandler
from jarengine.events.keyboard import JEKeyCode as _JEKeyCode
from jarengine.events.mouse import JEMouseCode as _JEMouseCode
from jarengine.interns.base_classe import JEInternBaseClass as _JEInternBaseClass
from jarengine.interns.config import get as _get
from jarengine.interns import (
    JTKExternError as _JTKExternError,
    PGExtern as _PGExtern
)
from jarengine.entity.entity import JEEntity as _JEEntity
from jarengine.systems.container import JEContainer as _JEContainer
from jarengine.interns.high_classes import JEInternSystems as _JEInternSystems
from jarengine.interns.final_classes import JEInternResources as _JEInternResources
from jarengine.systems.bool import JEBool as _JEBool
from jarengine.systems.clock import JEClock as _JEClock
from jarengine.interns.decorators import documentation as _documentation
from jarengine.interns.helpers import (
    assertion_type as _assertion_type,
    safe_cast as _safe_cast,
    enabled as _enabled
)
import jarengine.interns.log as _log

@_documentation
@_final
class JEGame(_JEInternBaseClass):

    _instance = None
    _is_created = _JEBool(0)

    __instance_policy__ = "flyweight"
    __instance_limit__ = 1

    def __new__(cls, *args, **kwargs):
        if cls._instance is not None:
            raise _JTKExternError.Error.ErrorRuntime(
                "\nInstance already exists. Only one game is allowed."
            )
        cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if JEGame._is_created:
            return
        JEGame._is_created = _JEBool(1)
        super().__init__()
        self._window = None
        self._resources = _JEInternResources()
        self._entities = _JEContainer(_JEEntity)
        self._clock = _JEClock() if _get("window", "DISPLAY", "fps") != -1 else None
        self._input = _JEInput() if _enabled("input", "INPUT") else None
        self._is_open = _JEBool(1)
        self._event_manager = _JEEventHandler()
        self._systems = _JEContainer(_JEInternSystems, _JEBool(1))

        _log.log("DEBUG", "OBJECT", f"JEGame: Created", self.jeid)

    def set_window(self, window):

        _assertion_type(window, _JEWindow, "window must be of type 'JEWindow'", True)

        if self._window:
            raise _JTKExternError.Error.ErrorRuntime(
                f"\nWindow already set."
            )
        self._window = window
        self._clock = _JEClock(window.settings.fps)

        _log.log("DEBUG", "ENGINE", f"JEGame: Window added", self.jeid, window)

    @property
    def wdw(self):
        if not self._window:
            raise _JTKExternError.State.ErrorStateNotInitialized(
                "\nWindow not set."
            )
        return self._window

    @property
    def input(self):
        return self._input

    def is_key_down(self, key):

        key = _safe_cast(_assertion_type(key, _JEKeyCode, "key must be of type 'JEKeyCode'"), _JEKeyCode)

        return self._input.is_key_down(key)

    def is_mouse_down(self, button):

        button = _safe_cast(_assertion_type(button, _JEMouseCode, "button must be of type 'JEMouseCode'"), _JEMouseCode)

        return self._input.is_mouse_down(button)

    @property
    def clock(self):
        return self._clock

    @property
    def dt(self):
        return float(self._clock)

    @property
    def event(self):
        return self._event_manager

    @property
    def is_open(self):
        return self._is_open

    def close(self):
        if self._is_open:

            _log.log("DEBUG", "ENGINE", f"JEGame: Closed", self.jeid)

            self._is_open = _JEBool(0)

    @property
    def resources(self):
        return self._resources

    def refresh(self):
        for system in self._systems:
            system.refresh()
        if self._clock:
            self._clock.target_fps = self._window.settings.fps

        _log.log("DEBUG", "ENGINE", f"JEGame: Game refreshed", self.jeid)

    def refresh_entity(self, entity):

        _assertion_type(entity, _JEEntity, "entity must be of type 'JEEntity'", True)

        for system in self._systems:
            system.refresh_entity(entity)

        _log.log("DEBUG", "ENGINE", f"JEGame: Game refreshed for 1 entity", self.jeid)

    def add_entity(self, entity, *, refresh = _JEBool(0)):

        _assertion_type(entity, _JEEntity, "entity must be of type 'JEEntity'", True)
        refresh = _safe_cast(_assertion_type(refresh, _JEBool, "refresh must be of type 'JEBool'"), _JEBool)

        self._entities.add(entity)
        entity.add_parent(self)
        if refresh:
            self.refresh_entity(entity)

    @property
    def entities(self):
        return self._entities

    def add_system(self, system):

        _assertion_type(system, _JEInternSystems, "system must be of type 'JEInternSystems'", True)

        self._systems.add(system)

        _log.log("DEBUG", "ENGINE", f"JEGame: System added", self.jeid, system)

    @property
    def systems(self):
        return self._systems

    def _iter_entities(self):

        def iterate(entity):

            yield entity

            if hasattr(entity, "get_group"):
                for child in entity.get_group():
                    yield from iterate(child)

        for entity in self._entities:
            yield from iterate(entity)

    def update(self):
        self._event_manager.process(self, broadcast = _JEBool(_get('event', 'EVENT', 'event_broadcast', bool, _JEBool(0)))())

        if self._clock:
            self._clock.update()

        if self._input:
            self._input.update()

        window = self._window
        dt = self.dt if self._clock else 1 /window.settings.fps

        for system in self._systems:
            for entity in system.cache:
                entity.update(dt)
                system.update(
                    window,
                    entity,
                    system.cache,
                    dt
                )

        window.display()
        window.clear()

        _log.save()

    def display(self):
        _PGExtern.display.flip()

    def __deepcopy__(self, memo):
        return self
