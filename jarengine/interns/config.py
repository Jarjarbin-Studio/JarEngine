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

from os.path import exists
from os import mkdir
from typing import final as _final
from datetime import datetime as _datetime

from jarbin_toolkit_config import Config as _JTKInternConfig
from jarengine.interns.base_classe import JEInternBaseClass as _JEInternBaseClass
from jarengine.interns import JTKExternError as _JTKExternError
from jarengine.interns.decorators import documentation as _documentation

@_documentation
@_final
class JEInternConfig(_JTKInternConfig, _JEInternBaseClass):
    __recursive__ = False

    project_path = None
    config_path = None

    def __init__(self, name, data = None):
        if not JEInternConfig.project_path or  not JEInternConfig.config_path:
            raise _JTKExternError.State.ErrorStateNotInitialized("\nJarEngine.init(path) must be called first")
        if not exists(JEInternConfig.config_path):
            mkdir(JEInternConfig.config_path)

        if not data:
            data = {}

        super().__init__(JEInternConfig.config_path, data | {
            "INFO": {
                "name": name,
                "creation": _datetime.now()
            }
        }, file_name=f"je-{name}.ini")

def get_config(name = "config", data = None):
    return JEInternConfig(name, data)
