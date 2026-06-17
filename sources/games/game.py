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

from types import NoneType
from typing import Self

from sources.games import JEWindow
from sources.systems import JTKInternError, JEInternBaseClasses, JEInternConfig

class JEGame(JEInternBaseClasses.JEInternClassBase):

    _instance: Self = None
    _is_created = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is not None:
            raise JTKInternError.Error.ErrorRuntime(
                "\ninstance already exists. Only one game is allowed."
            )

        cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        from sources.games.window import JEWindow

        if JEGame._is_created:
            return

        JEGame._is_created = True
        super().__init__()
        self._window: JEWindow | NoneType = None
        self._clocks: NoneType = None
        self._config: JEInternConfig.JTKInternConfig = JEInternConfig.get_game_config()

    def set_window(self, window: JEWindow):
        if not isinstance(window, JEWindow):
            raise JTKInternError.Error.ErrorType(
                f"\n{type(window).__name__!r} isn't of type  {JEWindow.__name__!r}."
            )
        if self._window:
            raise JTKInternError.Error.ErrorRuntime(
                f"\nwindow already set."
            )

        self._window = window

    @property
    def window(self) -> JEWindow:
        if not self._window:
            raise JTKInternError.State.ErrorStateNotInitialized(
                "\nwindow not set."
            )

        return self._window
