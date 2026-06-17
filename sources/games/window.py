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

from typing import Self

from sources.systems import JTKInternError, JEInternBaseClasses, JEInternClasses, JEInternConfig, JEInternPyGame

class JEInternRessources(JEInternBaseClasses.JEInternClassBase):

    def __init__(self):
        super().__init__()

        self.textures: JEInternClasses.JEInternContainer = JEInternClasses.JEInternContainer(JEInternClasses.JEInternClassGraphic)
        self.animations: JEInternClasses.JEInternContainer = JEInternClasses.JEInternContainer(JEInternClasses.JEInternClassGraphic)
        self.font: JEInternClasses.JEInternContainer = JEInternClasses.JEInternContainer(JEInternClasses.JEInternClassGraphic)

class JEWindow(JEInternBaseClasses.JEInternClassBase):

    _instance: Self = None
    _is_created = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is not None:
            raise JTKInternError.Error.ErrorRuntime(
                "\ninstance already exists. Only one window is allowed."
            )

        cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(
            self,
            size: tuple[int, int] = (0, 0),
            flags: int = 0,
            depth: int = 0,
            display: int = 0,
            vsync: int = 0
        ):

        if JEWindow._is_created:
            return
        JEWindow._is_created = True
        super().__init__()
        self._screen: JEInternPyGame.Surface = JEInternPyGame.display.set_mode(size, flags, depth, display, vsync)
        self.ressource: JEInternRessources = JEInternRessources()
        self._event: list[JEInternPyGame.event.Event] = []
        self._config: JEInternConfig.JTKInternConfig = JEInternConfig.get_window_config()
