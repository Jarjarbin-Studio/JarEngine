# =============================================================================
# JarEngine - Python Game Engine Wrapper (Pygame-based)
# =============================================================================
#
# JarEngine is a lightweight game framework built on top of Pygame
# that simplifies usage while providing higher-level abstractions for
# game development and prototyping.
#
# =============================================================================
# Version: jarengine-v1.10
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

from enum import IntEnum

from jarengine.interns.base_classe import JEInternBaseClass as _JEInternBaseClass
from jarengine.interns.decorators import documentation as _documentation
from jarengine.interns import PGExtern as _PGExtern
from jarengine.interns.helpers import assertion_type as _assertion_type
import jarengine.interns.log as _log

class JECompatibility(IntEnum):
    OK = 0
    WARNING = 1
    ERROR = 2

@_documentation
class JEVersion(_PGExtern.version.SoftwareVersion, _JEInternBaseClass):

    __recursive__ = False

    def __init__(self, *args, **kwargs):
        super().__init__()

        _log.log("DEBUG", "OBJECT", f"JEVersion: Created", self.jeid, *args)

    def compatibility(self, other):

        _assertion_type(other, JEVersion, "other must be of type 'JEVersion'", True)

        if self.major != other.major:
            return JECompatibility.ERROR

        if self.minor < other.minor:
            return JECompatibility.ERROR

        if self.minor == other.minor and self.patch < other.patch:
            return JECompatibility.WARNING

        return JECompatibility.OK
