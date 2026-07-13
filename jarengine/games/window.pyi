from __future__ import annotations

from typing import Any

from jarengine.interns.base_classe import JEInternBaseClass
from jarengine.interns import PGExtern
from jarengine.interns.final_classes import JEInternWindowSettings
from jarengine.systems.color import JEColor
from jarengine.systems.vector import JEVector2D


class JEWindow(JEInternBaseClass):
    def __init__(self, *, size: JEVector2D | tuple[int, int] = JEVector2D(0, 0), flags: int = 0, fps: int = 60, depth: int = 0, display: int = 0, vsync: int = 0, title: str = "JarEngine Game"):
        """
            JEWindow

            Parameters:
                size (JEVector2D | tuple[int, int]) = (0, 0): Size
                flags (int) = 0: Flags (Not handled by JarEngine)
                fps (int) = 60: FPS
                depth (int) = 0: Depth (Not handled by JarEngine)
                display (int) = 0: Display (Not handled by JarEngine)
                vsync (int) = 0: Vsync (Not handled by JarEngine)
                title (str) = "JarEngine Game": Title
        """
        ...
    @property
    def screen(self) -> PGExtern.Surface:
        """
            Get PyGame screen

            Returns:
                PGExtern.Surface: PyGame screen
        """
        ...
    @property
    def settings(self) -> JEInternWindowSettings:
        """
            Get window's settings

            Returns:
                JEInternWindowSettings: window's settings
        """
        ...
    def fill(self, color: JEColor | tuple[int, int, int] | tuple[int, int, int, int]):
        """
            Fill the window with a given color.

            Parameters:
                color (JEColor | tuple[int, int, int] | tuple[int, int, int, int]): Color to fill
        """
        ...
    def blit(self, source: PGExtern.Surface, dest: PGExtern.Surface):
        """
            Copy a PyGame surface to another
            
            Parameters:
                source (PGExtern.Surface): PyGame surface
                dest (PGExtern.Surface): Destination PyGame surface
        """
        ...
