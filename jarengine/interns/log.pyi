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

from typing import Optional, Any

from jarengine.interns.base_classe import JEInternBaseClass
from jarengine.interns import JTKExternError

from jarbin_toolkit_log import Log as JTKExternLog

_current_log: Optional[JEInternLog]
_log_levels: list[str]

class JEInternLog(JTKExternLog, JEInternBaseClass):
    project_path: Optional[str]     #Path of the project, set at runtime by the init
    log_path: Optional[str]         #Path of the configs (dependent of project_path)
    def __init__(self, name):
        """
            JEInternLog

            Parameters:
                name (str): Name of the log
        """
        ...
    @property
    def buffer(self) -> list[str]:
        """
            Get the log buffer

            Returns:
                list[str]: log buffer
        """
        ...

def log(status: str, title: str, description: str, jeid: Optional[str] = None, *values: Any):
    """
        Register a new log.
        Status : INFO, DEBUG, VALID, WARN, ERROR, CRIT

        Parameters:
            status (str): status
            title (str): title
            description (str): description
            jeid (str): jeid
            *values (Any): log values
    """
    ...
def comment(string: str | JTKExternError.BaseError):
    """
        Comment a message into the log file

        Parameters:
            string (str | JTKExternError.BaseError): comment message
    """
    ...
def save():
    """
        Save the logs in batch to the file
    """
    ...
def close():
    """
        Close the log
    """
    ...
