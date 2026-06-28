from __future__ import annotations

from sources.interns import PGIntern
from sources.systems.vector import JEVector2D

class JETexture:
    base_path: str
    def __init__(self, name: str, path: str) -> None: ...
    @property
    def surface(self) -> PGIntern.Surface: ...
    @property
    def path(self) -> str: ...
    @property
    def size(self) -> JEVector2D: ...
