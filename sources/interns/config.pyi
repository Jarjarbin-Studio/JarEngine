from __future__ import annotations

from jarbin_toolkit_config import Config as _JTKInternConfig
from sources.interns.decorators import documentation as _documentation

class JEInternConfig(_JTKInternConfig):
    path: str
    def __init__(self, name: str) -> None: ...

def get_config(name: str) -> JEInternConfig: ...
