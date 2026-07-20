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

from typing import Optional, Any

from jarbin_toolkit_config import Config as JTKInternConfig
from jarengine.interns.base_classe import JEInternBaseClass
from jarengine.interns.decorators import documentation as _documentation

class JEInternConfig(JTKInternConfig, JEInternBaseClass):
    project_path: Optional[str]         #Path of the project, set at runtime by the init
    config_path: Optional[str]          #Path of the configs (dependent of project_path)
    configs: dict[str, JEInternConfig]  #Opened configs
    def __init__(self, name: str, data: Optional[dict[str, dict[str, Any]]] = None):
        """
            JEInternConfig
            
            Parameters:
                name (str): Name of the configuration
                data (Optional[dict[str, dict[str, Any]]]) = None: Configuration data
        """
        ...

def get(name: str, section: str, setting: str, _type: type = str, default: Optional[Any] = None) -> Any:
    """
        Get a configuration

        Parameters:
            name (str): Name of the configuration
            section (str): Section of the configuration
            setting (str): Setting of the configuration
            _type (type): Wanted type
            default (Optional[Any]): Default value

        Returns:
            Any: Configuration
    """
    ...

def set(name: str, section: str, setting: str, value: Any):
    """
        Set a configuration

        Parameters:
            name (str): Name of the configuration
            section (str): Section of the configuration
            setting (str): Setting of the configuration
            value (Any): New value
    """
    ...

def init_all():
    """
        Init/open all necessary configurations
    """
    ...
