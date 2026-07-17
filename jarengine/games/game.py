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
from jarengine.interns.base_classe import JEInternBaseClass as _JEInternBaseClass
from jarengine.interns.config import get_config as _get_config
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

    def __init__(self, *, use_clock = _JEBool(0), use_input = _JEBool(0)):
        if JEGame._is_created:
            return
        JEGame._is_created = _JEBool(1)
        super().__init__()
        self._config = _get_config()
        self._window = None
        self._resources = _JEInternResources()
        self._entities = _JEContainer(_JEEntity)
        self._clock = _JEClock() if use_clock else None
        self._input = _JEInput() if use_input else None
        self._is_open = _JEBool(1)
        self._event_manager = _JEEventHandler()
        self._systems = _JEContainer(_JEInternSystems, _JEBool(1))

    def set_window(self, window):
        if not isinstance(window, _JEWindow):
            raise _JTKExternError.Error.ErrorType(
                f"\n{type(window).__name__!r} isn't of type  {_JEWindow.__name__!r}."
            )
        if self._window:
            raise _JTKExternError.Error.ErrorRuntime(
                f"\nWindow already set."
            )
        self._window = window
        self._clock = _JEClock(window.settings.fps)

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
        return self._input.is_key_down(key)

    def is_mouse_down(self, button):
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
        self._is_open = _JEBool(0)

    @property
    def resources(self):
        return self._resources

    def refresh(self):
        for system in self._systems:
            system.refresh()
        if self._clock:
            self._clock.target_fps = self._window.settings.fps

    def refresh_entity(self, entity):
        for system in self._systems:
            system.refresh_entity(entity)

    def add_entity(self, entity, *, refresh = _JEBool(0)):
        self._entities.add(entity)
        entity.add_parent(self)
        if refresh:
            self.refresh_entity(entity)

    @property
    def entities(self):
        return self._entities

    def add_system(self, system):
        self._systems.add(system)

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
        self._event_manager.process(self)

        if self._clock:
            self._clock.update()

        if self._input:
            self._input.update()

        window = self._window
        dt = self.dt if self._clock else 1 /window.settings.fps

        for system in self._systems:
            for entity in system.cache:
                system.update(
                    window,
                    entity,
                    system.cache,
                    dt
                )

    def display(self):
        _PGExtern.display.flip()

    def __deepcopy__(self, memo):
        return self
