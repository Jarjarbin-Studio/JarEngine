from __future__ import annotations

from typing import Optional, Any

from jarbin_toolkit_config import Config as JTKInternConfig
from jarengine.interns.base_classe import JEInternBaseClass
from jarengine.interns.decorators import documentation as _documentation

class JEInternConfig(JTKInternConfig, JEInternBaseClass):
    project_path: Optional[str]
    config_path: Optional[str]
    def __init__(self, name: str, data: Optional[dict[str, Any]] = None): ...

def get_config(name: str = "config", data: Optional[dict[str, Any]] = None) -> JEInternConfig: ...
