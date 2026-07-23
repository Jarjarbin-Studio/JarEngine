# =============================================================================
# JarEngine - Python Game Engine Wrapper (PyGame-based)
# =============================================================================
#
# JarEngine is a lightweight game framework built on top of PyGame
# that simplifies usage while providing higher-level abstractions for
# game development and prototyping.
#
# =============================================================================
# Version: jarengine-v1.8
# Author: Jarjarbin Studio
# Licence: GPL v3
# =============================================================================
#
# This engine is inspired by PyGame, modern game engine design patterns,
# and directly influenced by the architecture of NewCSFML.
#
# It is designed for educational purposes and small-to-medium game projects.
#
# It provides structured systems such as entity management, scene handling,
# render abstraction, and advanced modules like particle systems.
#
# =============================================================================
# WARNING:
# =============================================================================
#
# This is NOT PyGame itself.
# It is a custom abstraction layer built on top of PyGame.
#
# =============================================================================

from __future__ import annotations

from typing import final as _final

from jarengine.interns.config import (
    get as _get,
    JEInternConfig as _JEInternConfig
)
from jarengine.interns import (
    PGExtern as _PGExtern,
    JTKExternError as _JTKExternError
)
from jarengine.interns.high_classes import JEInternOwnership as _JEInternOwnership
from jarengine.interns.low_classes import JEInternResource as _JEInternResource
from jarengine.systems.vector import JEVector2D as _JEVector2D
from jarengine.interns.decorators import documentation as _documentation
from jarengine.interns.helpers import (
    assertion_type as _assertion_type,
    asset_path as _asset_path,
    safe_cast as _safe_cast
)
import jarengine.interns.log as _log

@_documentation
@_final
class JETexture(_JEInternResource, _JEInternOwnership):

    def __init__(self, name, path):

        name = _safe_cast(_assertion_type(name, str, "name must be of type 'str'"), str)
        path = _safe_cast(_assertion_type(path, str, "path must be of type 'str'"), str)

        super().__init__(name, path)

        if not "/" in path:
            path = _asset_path(_get("assets", "DIRECTORY", "texture", str, "textures"), path)

        self._path = path
        try:
            self._texture = _PGExtern.image.load(path).convert_alpha()
        except FileNotFoundError:
            raise _JTKExternError.Special.ErrorSpecialConfig(f"\nInvalid texture path. Check assets config at {_JEInternConfig.config_path}")
        self._size = _JEVector2D(self._texture.get_width(), self._texture.get_height())

        _log.log("DEBUG", "OBJECT", f"JETexture: Created", self.jeid, name, path)

    @property
    def texture(self):
        return self._texture

    @property
    def size(self):
        return self._size
