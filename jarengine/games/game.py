"""
    JarEngine - Python Game Engine Wrapper (Pygame-based)

    JarEngine is a lightweight game framework built on top of Pygame
    that simplifies usage while providing higher-level abstractions for
    game development and prototyping.

    Version: jarengine-v1.0.0
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

from jarengine.entities.components_graphics import JELayerComponent as _JELayerComponent
from jarengine.games.window import JEWindow as _JEWindow
from jarengine.games.input import JEInput as _JEInput
from jarengine.events.manager import JEEventHandler as _JEEventHandler
from jarengine.interns.base_classe import JEInternBaseClass as _JEInternBaseClass
from jarengine.interns.config import get_config as _get_config
from jarengine.interns import (
    JTKExternError as _JTKExternError,
    PGExtern as _PGExtern
)
from jarengine.entities.entity import JEEntity as _JEEntity
from jarengine.systems.container import JEContainer as _JEContainer
from jarengine.interns.high_classes import JEInternSystems as _JEInternSystems
from jarengine.interns.final_classes import JEInternRessources as _JEInternRessources
from jarengine.systems.bool import JEBool as _JEBool
from jarengine.systems.clock import JEClock as _JEClock
from jarengine.interns.decorators import documentation as _documentation

@_documentation
@_final
class JEGame(_JEInternBaseClass):
    """Game manager"""

    _instance = None
    _is_created = _JEBool(0)
    __instance_policy__ = "flyweight"
    __instance_limit__ = 1

    def __new__(cls, *args, **kwargs):
        """Instances clamping"""
        if cls._instance is not None:
            raise _JTKExternError.Error.ErrorRuntime(
                "\nInstance already exists. Only one game is allowed."
            )
        cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, *, use_clock = True, use_input = True):
        """JEGame creator"""
        if JEGame._is_created:
            return
        JEGame._is_created = _JEBool(1)
        super().__init__()
        self._config = _get_config()
        self._window = None
        self._ressource = _JEInternRessources()
        self._entities = _JEContainer(_JEEntity)
        self._clock = _JEClock() if use_clock else None
        self._input = _JEInput() if use_input else None
        self._is_open = _JEBool(1)
        self._event_manager = _JEEventHandler()
        self._systems = _JEContainer(_JEInternSystems, _JEBool(1))
        self._is_dirty = _JEBool(1)
        self._cached_entity = []

    def set_window(self, window):
        """Set game window"""
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
        """Get window object"""
        if not self._window:
            raise _JTKExternError.State.ErrorStateNotInitialized(
                "\nWindow not set."
            )
        return self._window

    @property
    def input(self):
        """Get input object"""
        return self._input

    def is_key_down(self, key):
        return self._input.is_key_down(key)

    def is_mouse_down(self, button):
        return self._input.is_mouse_down(button)

    @property
    def clock(self):
        """Get clock object"""
        return self._clock

    @property
    def dt(self):
        """Get clock object"""
        return float(self._clock)

    @property
    def event(self):
        """Get event handler"""
        return self._event_manager

    @property
    def is_open(self):
        """Check if game is open"""
        return self._is_open

    @property
    def ressource(self):
        """Get ressource manager"""
        return self._ressource

    def add_entity(self, entity):
        """Add entity object"""
        self._entities.add(entity)
        self._is_dirty = _JEBool(1)

    @property
    def entities(self):
        """Get entity manager"""
        return self._entities

    def close(self):
        """Close game"""
        self._is_open = _JEBool(0)

    def add_system(self, system):
        """Add system object"""
        self._systems.add(system)

    @property
    def systems(self):
        """Get rendering and update systems"""
        return self._systems

    def update(self):
        """Update game"""

        def render_sort(entity):
            """Sorting key for rendering."""

            layer = entity.get(_JELayerComponent)

            if layer:
                try:
                    return int(layer())
                except Exception:
                    return 0

            return 0

        self._event_manager.process(self)
        self._clock.update()
        self._input.update()

        if self._is_dirty:
            self._cached_entity = sorted(self._entities, key=render_sort)

        for entity in self._cached_entity :
            for system in self._systems:
                if system.accepts(entity.components):
                    system.update(self._window, entity, self._entities, float(self._clock))

    def display(self):
        """Display game"""
        _PGExtern.display.flip()

    def __deepcopy__(self, memo):
        """Deepcopy"""
        return self
