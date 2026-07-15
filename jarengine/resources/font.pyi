from __future__ import annotations

from jarengine.interns.low_classes import JEInternResource
from jarengine.interns.high_classes import JEInternOwnership
from jarengine.interns import PGExtern

class JEFont(JEInternResource, JEInternOwnership):
    def __init__(self, name: str, path: str, size: int):
        """
            JEFont

            Parameters:
                name (str): Font name
                path (str): Font path
        """
        ...
    @property
    def font(self) -> PGExtern.font.Font:
        """
            Get PyGame font

            Returns:
                PGExtern.font.Font: Font
        """
        ...
    @property
    def size(self) -> int:
        """
            Get font size

            Returns:
                int: Size
        """
        ...
