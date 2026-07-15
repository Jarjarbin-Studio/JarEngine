from __future__ import annotations

from typing import Any

from jarengine.interns.base_classe import JEInternBaseClass

class JEBool(JEInternBaseClass):
    def __init__(self, value: Any):
        """
            JEBool

            Parameters:
                value (Any): Value to be represented
        """
        ...
    def __bool__(self) -> bool:
        """
            Get the actual intern boolean (used in conditions)

            Returns:
                bool: Internal boolean
        """
        ...
    def __int__(self) -> int:
        """
            Get int representation of the boolean

            Returns:
                int: Int
        """
        ...
    def __call__(self) -> JEBool:
        """
            Revers the boolean (False <-> True)

            Returns:
                JEBool: Reversed boolean
        """
        ...
    @property
    def b(self) -> bool:
        """
            Get the actual intern boolean (used for dump and debug)

            Returns:
                bool: Internal boolean
        """
        ...
