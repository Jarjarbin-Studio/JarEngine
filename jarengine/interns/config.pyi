# =============================================================================
# JarEngine - Python Game Engine Wrapper (Pygame-based)
# =============================================================================
#
# JarEngine is a lightweight game framework built on top of Pygame
# that simplifies usage while providing higher-level abstractions for
# game development and prototyping.
#
# =============================================================================
# Version: jarengine-v2.0
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

from pathlib import Path
from typing import Optional, Any

from jarbin_toolkit_config import Config as JTKExternConfig

from jarengine.interns.base_classe import JEInternBaseClass

class JEInternConfig(JTKExternConfig, JEInternBaseClass):
    project_path: Optional[str]         #Path of the project, set at runtime by the init
    config_path: Optional[str]          #Path of the configs (dependent of project_path)
    state_path: Optional[str]           #Path to the state configs (dependent of project_path)
    configs: dict[str, JEInternConfig]  #Opened configs
    def __init__(self, name: str, data: Optional[dict[str, dict[str, Any]]] = None, *, directory: Optional[str | Path] = None, metadata: Optional[dict[str, str]] = None, has_extension: bool = True):
        """
            JEInternConfig

            Parameters:
                name (str): Name of the configuration.
                data (Optional[dict[str, dict[str, Any]]], optional): Configuration sections and their options.
                directory (Optional[str | Path], optional): Directory containing the configuration file. Used internally when constructing the underlying Config instance.
                metadata (Optional[dict[str, str]], optional): Metadata associated with the configuration. Used internally by the underlying Config instance.
                has_extension (bool, optional): Whether to append the .ini extension to the filename.
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
