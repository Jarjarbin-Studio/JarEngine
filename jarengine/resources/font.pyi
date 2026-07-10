from __future__ import annotations

from jarengine.interns.low_classes import JEInternResource
from jarengine.interns.high_classes import JEInternOwnership
from jarengine.interns import PGExtern

class JEFont(JEInternResource, JEInternOwnership):
    def __init__(self, name: str, path: str, size: int): ...
    @property
    def font(self) -> PGExtern.font.Font: ...
    @property
    def path(self) -> str: ...
    @property
    def size(self) -> int: ...
