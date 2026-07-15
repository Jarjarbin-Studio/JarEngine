from __future__ import annotations

from typing import Optional, Any

from jarbin_toolkit_config import Config as JTKInternConfig
from jarengine.interns.base_classe import JEInternBaseClass
from jarengine.interns.decorators import documentation as _documentation

class JEInternConfig(JTKInternConfig, JEInternBaseClass):
    project_path: Optional[str] #Path of the project, set at runtime by the init
    config_path: Optional[str]  #Path of the configs (dependent of project_path)
    def __init__(self, name: str, data: Optional[dict[str, dict[str, Any]]] = None):
        """
            JEInternConfig
            
            Parameters:
                name (str): Name of the configuration
                data (Optional[dict[str, dict[str, Any]]]) = None: Configuration data
        """
        ...

def get_config(name: str = "config", data: Optional[dict[str, Any]] = None) -> JEInternConfig:
    """
        Get configuration
        
        Parameters:
            name (str): Name of the configuration
            data (Optional[dict[str, dict[str, Any]]]) = None: Configuration data
        
        Returns:
            JEInternConfig: Config
    """
    ...
