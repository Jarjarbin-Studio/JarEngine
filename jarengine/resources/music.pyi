from __future__ import annotations

from jarengine.interns.low_classes import JEInternResource
from jarengine.interns.high_classes import JEInternOwnership

class JEMusic(JEInternResource, JEInternOwnership):
    def __init__(self, name: str, path: str):
        """
            JEMusic

            Parameters:
                name (str): Music name
                path (str): Music path
        """
        ...
