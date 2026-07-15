from __future__ import annotations

from jarengine.interns.low_classes import JEInternResource
from jarengine.interns.high_classes import JEInternOwnership
from jarengine.interns import PGExtern

class JESound(JEInternResource, JEInternOwnership):
    def __init__(self, name: str, path: str):
        """
            JESound

            Parameters:
                name (str): Sound name
                path (str): Sound path
        """
        ...
    @property
    def sound(self) -> PGExtern.mixer.Sound:
        """
            Get PyGame sound

            Returns:
                PGExtern.mixer.Sound: Sound
        """
        ...
