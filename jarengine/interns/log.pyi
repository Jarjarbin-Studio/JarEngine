# =============================================================================
# JarEngine - Python Game Engine Wrapper (PyGame-based)
# =============================================================================
#
# JarEngine is a lightweight game framework built on top of PyGame
# that simplifies usage while providing higher-level abstractions for
# game development and prototyping.
#
# =============================================================================
# Version: jarengine-v2.0
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

from typing import Any, Optional

from jarbin_toolkit_log import Log as JTKExternLog
from jarengine.interns.base_classe import JEInternBaseClass
from jarengine.interns import JTKExternError


_current_log: Optional[JEInternLog]
_log_levels: list[str]


class JEInternLog(JTKExternLog, JEInternBaseClass):
    project_path: Optional[str]  #Path of the project, set at runtime by the init
    log_path: Optional[str]  #Path of the configs (dependent of project_path)
    def __init__(self, name: str, _session: str):
        """
            Initialize a named JarEngine logger.

            Parameters:
                name: Name identifying this logger.
        """
        ...

def log(status: str, title: str, description: str, jeid: Optional[str] = None, *values: Any):
    """
        Register a log entry.

        Supported statuses are ``INFO``, ``DEBUG``, ``VALID``,
        ``WARN``, ``ERROR``, and ``CRIT``.

        Parameters:
            status: Severity/status of the entry.
            title: Category or scope of the entry.
            description: Message to log.
            jeid: Optional JarEngine identifier.
            *values: Optional values included when value logging is enabled.
    """
    ...
def comment(string: str | JTKExternError.BaseError):
    """
        Add a comment to the log.

        Parameters:
            string: Comment text or a JarEngine error object.
    """
    ...
def save():
    """
        Flush pending log entries to the log file.
    """
    ...
def close():
    """
        Flush and close the active log.
    """
    ...
