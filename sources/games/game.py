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
    Self as _Self,
    final as _final,
    Optional as _Optional
)

from sources.graphics.sprite import JESprite as _JESprite
from sources.games.renderer import JERenderer as _JERenderer
from sources.games.window import JEWindow as _JEWindow
from sources.games.input import JEInput as _JEInput
from sources.events.manager import JEEventHandler as _JEEventHandler
from sources.events.keyboard import JEKeyCode as _JEKeyCode
from sources.events.mouse import JEMouseCode as _JEMouseCode
from sources.interns.base_classe import JEInternClassBase as _JEInternClassBase
from sources.interns.config import (
    JEInternConfig as _JEInternConfig,
    get_config as _get_config
)
from sources.interns import (
    JTKInternError as _JTKInternError,
    PGIntern as _PGIntern
)
from sources.interns.high_classes import (
    JEInternDrawable as _JEInternDrawable,
    JEInternRessources as _JEInternRessources
)
from sources.systems.bool import JEBool as _JEBool
from sources.systems.clock import JEClock as _JEClock
from sources.interns.decorators import documentation as _documentation

@_documentation
@_final
class JEGame(_JEInternClassBase):
    """Game manager"""

    _instance: _Self = None
    _is_created = _JEBool(0)

    def __new__(
            cls,
            *args,
            **kwargs
        ) -> _Self:
        """Instances clamping"""
        if cls._instance is not None:
            raise _JTKInternError.Error.ErrorRuntime(
                "\nInstance already exists. Only one game is allowed."
            )

        cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(
            self,
            use_clock: bool = True,
            use_input: bool = True
        ) -> None:
        """JEGame creator"""
        if JEGame._is_created:
            return

        JEGame._is_created = _JEBool(1)
        super().__init__()
        self._config: _JEInternConfig = _get_config()
        self._window: _Optional[_JEWindow] = None
        self._ressource: _JEInternRessources = _JEInternRessources()
        self._drawable: _JEInternDrawable = _JEInternDrawable()
        self._clock: _Optional[_JEClock] = _JEClock() if use_clock else None
        self._input: _Optional[_JEInput] = _JEInput() if use_input else None
        self._is_open: _JEBool = _JEBool(1)
        self._event_manager: _JEEventHandler = _JEEventHandler()
        self._renderer: _Optional[_JERenderer] = None

    def set_window(self, window: _JEWindow):
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
        self._renderer = _JERenderer(self._window)

    @property
    def wdw(self) -> _JEWindow:
        """Get window object"""
        if not self._window:
            raise _JTKInternError.State.ErrorStateNotInitialized(
                "\nWindow not set."
            )

        return self._window

    @property
    def input(self) -> _JEInput:
        """Get input object"""
        return self._input

    def is_key_down(
            self,
            key: _JEKeyCode
        ) -> bool:
        return self._input.is_key_down(key)

    def is_mouse_down(
            self,
            button: _JEMouseCode
        ) -> bool:
        return self._input.is_mouse_down(button)

    @property
    def clock(self) -> _JEClock:
        """Get clock object"""
        return self._clock

    @property
    def dt(self) -> float:
        """Get clock object"""
        return float(self._clock)

    @property
    def event(self) -> _JEEventHandler:
        """Get event handler"""
        return self._event_manager

    @property
    def is_open(self) -> _JEBool:
        """Check if game is open"""
        return self._is_open

    @property
    def ressource(self) -> _JEInternRessources:
        """Get ressource manager"""
        return self._ressource

    @property
    def drawable(self) -> _JEInternDrawable:
        """Get drawable manager"""
        return self._drawable

    def close(self) -> None:
        """Close game"""
        self._is_open = _JEBool(0)

    def update(self) -> None:
        """Update game"""
        self._event_manager.process(self)
        self._clock.update()
        self._input.update()

    def display(self) -> None:
        """Display game"""
        _PGIntern.display.flip()

    def draw(self) -> None:
        """Draw game"""
        sprite: _JESprite
        for sprite in self._drawable.sprite:
            if sprite.is_alive():
                self._renderer.draw_sprite(sprite)

    def __deepcopy__(
            self,
            memo
        ):
        """Deepcopy"""
        return self
