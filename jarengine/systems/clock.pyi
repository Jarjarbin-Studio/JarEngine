from __future__ import annotations

from jarengine.interns.base_classe import JEInternBaseClass

class JEClock(JEInternBaseClass):
    def __init__(self, fps: int = 60):
        """
            JEClock
            
            Parameters:
                fps (int) = 60: Target fps
        """
        ...
    def update(self):
        """
            Update clock data
        """
        ...
    @property
    def dt(self) -> float:
        """
            Get time

            Returns:
                float: Current dt
        """
        ...
    @property
    def target_fps(self) -> int:
        """
            Get target fps

            Returns:
                int: Target fps
        """
        ...
    @target_fps.setter
    def target_fps(self, value: int):
        """
            Set target fps

            Parameters:
                value (int): New target fps
        """
        ...
    @property
    def fps(self) -> float:
        """
            Get current fps

            Returns:
                float: Current fps
        """
        ...
    def __float__(self) -> float:
        """
            Get time

            Returns:
                float: Current dt
        """
        ...
