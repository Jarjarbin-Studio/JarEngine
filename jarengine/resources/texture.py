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

from os import getcwd
from os.path import join
from typing import final as _final

from jarengine.interns import PGExtern as _PGExtern
from jarengine.interns.high_classes import JEInternOwnership as _JEInternOwnership
from jarengine.interns.low_classes import JEInternGraphic as _JEInternGraphic
from jarengine.systems.vector import JEVector2D as _JEVector2D
from jarengine.interns.decorators import documentation as _documentation

@_documentation
@_final
class JETexture(_JEInternGraphic, _JEInternOwnership):
    """Texture"""

    base_path = join(getcwd(), "assets/textures/")

    def __init__(self, name, path) -> None:
        """JETexture creator"""
        super().__init__(name)

        if not "/" in path:
            path = f"{JETexture.base_path}{path}"

        self._path = path
        self._surface = _PGExtern.image.load(path).convert_alpha()
        self._size = _JEVector2D(self._surface.get_width(), self._surface.get_height())

    @property
    def surface(self):
        """Get texture surface (PGExtern)"""
        return self._surface

    @property
    def path(self):
        """Get texture path"""
        return self._path

    @property
    def size(self):
        """Get texture size"""
        return self._size

    def __deepcopy__(self, memo):
        return self
