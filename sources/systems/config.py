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

from jarbin_toolkit_config import Config as JTKInternConfig

path: str = (
    "../.je-config"
    if JTKInternConfig.exist("../.je-config", file_name="je-base.ini") else
    __file__.replace('sources/systems/config.py', '.je-config/')
)

def get_game_config() -> JTKInternConfig:
    return JTKInternConfig(path, {"INFO": {"name": "je-game.ini"}}, file_name='je-game.ini')

def get_window_config() -> JTKInternConfig:
    return JTKInternConfig(path, {"INFO": {"name": "je-window.ini"}}, file_name='je-window.ini')
