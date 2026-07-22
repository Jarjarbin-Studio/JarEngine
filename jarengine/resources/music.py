# =============================================================================
# JarEngine - Python Game Engine Wrapper (Pygame-based)
# =============================================================================
#
# JarEngine is a lightweight game framework built on top of Pygame
# that simplifies usage while providing higher-level abstractions for
# game development and prototyping.
#
# =============================================================================
# Version: jarengine-v1.8
# Author: Jarjarbin Studio
# Licence: GPL v3
# =============================================================================
#
# This engine is inspired by Pygame, modern game engine design patterns,
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
# This is NOT Pygame itself.
# It is a custom abstraction layer built on top of Pygame.
#
# =============================================================================

from __future__ import annotations

from os.path import exists as _exists
from typing import final as _final

from jarengine.interns.config import (
    get as _get,
    JEInternConfig as _JEInternConfig
)
from jarengine.interns import JTKExternError as _JTKExternError
from jarengine.interns.high_classes import JEInternOwnership as _JEInternOwnership
from jarengine.interns.low_classes import JEInternResource as _JEInternResource
from jarengine.interns.decorators import documentation as _documentation
from jarengine.interns.helpers import (
    assertion_type as _assertion_type,
    asset_path as _asset_path
)

@_documentation
@_final
class JEMusic(_JEInternResource, _JEInternOwnership):

    def __init__(self, name, path):

        _assertion_type(name, str, "name must be of type 'str'")
        _assertion_type(path, str, "path must be of type 'str'")

        super().__init__(name, path)

        if not "/" in path:
            path = _asset_path(_get("assets", "DIRECTORY", "music", str, "musics"), path)

        self._path = path
        if not _exists(path):
            raise _JTKExternError.Special.ErrorSpecialConfig(f"\nInvalid music path. Check assets config at {_JEInternConfig.config_path}")
