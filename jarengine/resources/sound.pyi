from __future__ import annotations

from jarengine.interns.low_classes import JEInternResource
from jarengine.interns.high_classes import JEInternOwnership

class JESound(JEInternResource, JEInternOwnership):
    def __init__(self, name: str, path: str) -> None: ...
    @property
    def path(self) -> str: ...
