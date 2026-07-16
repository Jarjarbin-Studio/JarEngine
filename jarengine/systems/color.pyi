from __future__ import annotations

from typing import Iterator

from jarengine.interns.base_classe import JEInternBaseClass

class JEColor(JEInternBaseClass):
    def __init__(self, r: int = 0, g: int = 0, b: int = 0, a: int = 255):
        """
        JEColor

            Parameters:
                r (int) = 0: Red channel (0 - 255)
                g (int) = 0: Green channel (0 - 255)
                b (int) = 0: Blue channel (0 - 255)
                a (int) = 255: Alpha channel (opacity)(0 - 255)
        """
        ...
    @property
    def r(self) -> int:
        """
            Get the red channel value

            Returns:
                int: Red channel
        """
        ...
    @r.setter
    def r(self, r: int):
        """
            Set the red channel value

            Parameters:
                r (int): Red channel value
        """
        ...
    @property
    def g(self) -> int:
        """
            Get the green channel value

            Returns:
                int: Green channel
        """
        ...
    @g.setter
    def g(self, g: int):
        """
            Set the green channel value

            Parameters:
                g (int): Green channel value
        """
        ...
    @property
    def b(self) -> int:
        """
            Get the blue channel value

            Returns:
                int: Blue channel
        """
        ...
    @b.setter
    def b(self, b: int):
        """
            Set the blue channel value

            Parameters:
                b (int): Blue channel value
        """
        ...
    @property
    def a(self) -> int:
        """
            Get the alpha channel value

            Returns:
                int: Alpha channel
        """
        ...
    @a.setter
    def a(self, a: int):
        """
            Set the alpha channel value

            Parameters:
                a (int): Alpha channel value
        """
        ...
    @property
    def rgb(self) -> tuple[int, int, int]:
        """
            Get the RGB value as a tuple

            Returns:
                tuple[int, int, int]: RGB value
        """
        ...
    @property
    def rgba(self) -> tuple[int, int, int, int]:
        """
            Get the RGBA value as a tuple

            Returns:
                tuple[int, int, int, int]: RGBA value
        """
        ...
    def __iter__(self) -> Iterator[float]:
        """
            Iterate over the channels

            Returns:
                Iterator[float]: Color iterator
        """
        ...
