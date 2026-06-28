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

from sources.interns import PGIntern as _PGIntern
from sources.interns.high_classes import JEInternalOwnership as _JEInternalOwnership
from sources.interns.low_classes import JEInternGraphic as _JEInternGraphic
from sources.interns.decorators import documentation as _documentation

@_documentation
@_final
class JEFont(_JEInternGraphic, _JEInternalOwnership):
    """Texture"""

    base_path = f"{__file__.split('sources')[0]}assets/fonts/"

    def __init__(self, name, path, size) -> None:
        """JETexture creator"""
        super().__init__(name)

        if not "/" in path:
            path = f"{JEFont.base_path}{path}"

        self._path = path
        self._font = _PGIntern.font.Font(path, size)
        self._size = size

    @property
    def font(self):
        """Get texture surface (PGIntern)"""
        return self._font

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
