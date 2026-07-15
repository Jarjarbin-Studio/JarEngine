from __future__ import annotations

from jarengine.interns.high_classes import JEInternOwnership
from jarengine.interns.low_classes import JEInternResource
from jarengine.interns import PGExtern
from jarengine.systems.vector import JEVector2D

class JETexture(JEInternResource, JEInternOwnership):
    def __init__(self, name: str, path: str):
        """
            JETexture
            
            Parameters:
                name (str): Texture name
                path (str): Texture path
        """
        ...
    @property
    def texture(self) -> PGExtern.Surface:
        """
            Get PyGame texture

            Returns:
                PGExtern.Surface: Texture
        """
        ...
    @property
    def size(self) -> JEVector2D:
        """
            Get texture size

            Returns:
                JEVector2D: Size
        """
        ...
