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

from typing import final as _final

from sources.entities.components_graphics import JELayerComponent as _JELayerComponent
from sources.games.window import JEWindow as _JEWindow
from sources.games.input import JEInput as _JEInput
from sources.events.manager import JEEventHandler as _JEEventHandler
from sources.interns.base_classe import JEInternClassBase as _JEInternClassBase
from sources.interns.config import get_config as _get_config
from sources.interns import (
    JTKInternError as _JTKInternError,
    PGIntern as _PGIntern
)
from sources.entities.entity import JEEntity as _JEEntity
from sources.systems.container import JEContainer as _JEContainer
from sources.interns.high_classes import JEInternalRenderingSystems as _JEInternalRenderingSystems
from sources.interns.final_classes import JEInternRessources as _JEInternRessources
from sources.systems.bool import JEBool as _JEBool
from sources.systems.clock import JEClock as _JEClock
from sources.interns.decorators import documentation as _documentation

@_documentation
@_final
class JEGame(_JEInternClassBase):
    """Game manager"""

    _instance = None
    _is_created = _JEBool(0)
    __instance_policy__ = "flyweight"
    __instance_limit__ = 1

    def __new__(cls, *args, **kwargs):
        """Instances clamping"""
        if cls._instance is not None:
            raise _JTKInternError.Error.ErrorRuntime(
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
        self._systems = _JEContainer(_JEInternalRenderingSystems, _JEBool(1))

    def set_window(self, window):
        """Set game window"""
        if not isinstance(window, _JEWindow):
            raise _JTKInternError.Error.ErrorType(
                f"\n{type(window).__name__!r} isn't of type  {_JEWindow.__name__!r}."
            )
        if self._window:
            raise _JTKInternError.Error.ErrorRuntime(
                f"\nWindow already set."
            )
        self._window = window
        self._clock = _JEClock(window.settings.fps)

    @property
    def wdw(self):
        """Get window object"""
        if not self._window:
            raise _JTKInternError.State.ErrorStateNotInitialized(
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

        for entity in sorted(self._entities, key=render_sort):
            for system in self._systems:
                if system.accepts(entity.components):
                    system.update(self._window, entity, self._entities, float(self._clock))

    def display(self):
        """Display game"""
        _PGIntern.display.flip()

    def __deepcopy__(self, memo):
        """Deepcopy"""
        return self
