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

from jarbin_toolkit_config import Config as _JTKInternConfig
from sources.interns.decorators import documentation as _documentation

@_documentation
@_final
class JEInternConfig(_JTKInternConfig):
    """Config (Internal API)"""
    __recursive__ = False

    path = (
        "../.je-config"
        if _JTKInternConfig.exist("../.je-config", file_name="je-base.ini") else
        f"{__file__.split('sources')[0]}.je-config/"
    )

    def __init__(self, name):
        """JEInternConfig creator"""
        super().__init__(JEInternConfig.path, {"INFO": {"name": name}}, file_name=f"je-{name}.ini")

def get_config(name = "engine"):
    return JEInternConfig(name)
