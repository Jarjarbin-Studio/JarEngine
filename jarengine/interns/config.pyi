from __future__ import annotations

from typing import Optional

from jarbin_toolkit_config import Config as _JTKInternConfig
from jarengine.interns.decorators import documentation as _documentation

class JEInternConfig(_JTKInternConfig):
    project_path: Optional[str]
    config_path: Optional[str]
    def __init__(self, name: str, data: Optional[dict]) -> None: ...

def get_config(name: str) -> JEInternConfig: ...
