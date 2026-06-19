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
    final as _final
)

from sources.games.window import JEWindow as _JEWindow
from sources.games.events import JEEventHandler as _JEEventHandler
from sources.interns.base_classe import JEInternClassBase as _JEInternClassBase
from sources.interns.config import (
    JEInternConfig as _JEInternConfig,
    get_game_config as _get_game_config
)
from sources.interns import (
    JTKInternError as _JTKInternError,
    JEInternPyGame as _JEInternPyGame
)
from sources.systems.bool import JEBool as _JEBool

@_final
class JEGame(_JEInternClassBase):

    _instance: _Self = None
    _is_created = _JEBool(0)

    def __new__(
            cls,
            *args,
            **kwargs
        ) -> _Self:
        if cls._instance is not None:
            raise _JTKInternError.Error.ErrorRuntime(
                "\nInstance already exists. Only one game is allowed."
            )

        cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if JEGame._is_created:
            return

        JEGame._is_created = _JEBool(1)
        super().__init__()
        self._window: _JEWindow | None = None
        self._clocks: None = None
        self._config: _JEInternConfig = _get_game_config()
        self._is_open: _JEBool = _JEBool(1)
        self._event_manager: _JEEventHandler = _JEEventHandler()

    def set_window(self, window: _JEWindow):
        if not isinstance(window, _JEWindow):
            raise _JTKInternError.Error.ErrorType(
                f"\n{type(window).__name__!r} isn't of type  {_JEWindow.__name__!r}."
            )
        if self._window:
            raise _JTKInternError.Error.ErrorRuntime(
                f"\nWindow already set."
            )

        self._window = window

    @property
    def wdw(self) -> _JEWindow:
        if not self._window:
            raise _JTKInternError.State.ErrorStateNotInitialized(
                "\nWindow not set."
            )

        return self._window

    @property
    def event(self) -> _JEEventHandler:
        return self._event_manager

    @property
    def is_open(self) -> _JEBool:
        return self._is_open

    def close(self) -> None:
        self._is_open = _JEBool(0)

    def update(self) -> None:
        self._event_manager.process(self)
        _JEInternPyGame.display.flip()

    def __deepcopy__(
            self,
            memo
        ):
        return self
