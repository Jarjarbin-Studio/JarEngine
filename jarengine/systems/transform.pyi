from __future__ import annotations

from jarengine.interns.base_classe import JEInternBaseClass
from jarengine.systems.bool import JEBool

class JETransform(JEInternBaseClass):
    def __add__(self, other: JETransform) -> JETransform:
        """
            Add 2 vector together
            
            Parameters:
                other (JETransform): Other vector
            
            Returns:
                JETransform: Result vector
        """
        ...
    def __sub__(self, other: JETransform) -> JETransform:
        """
            Subtract 2 vector together

            Parameters:
                other (JETransform): Other vector

            Returns:
                JETransform: Result vector
        """
        ...
    def __mul__(self, other: JETransform) -> JETransform:
        """
            Multiply 2 vector together

            Parameters:
                other (JETransform): Other vector

            Returns:
                JETransform: Result vector
        """
        ...
    def __rmul__(self, other: JETransform) -> JETransform:
        """
            Multiply 2 vector together

            Parameters:
                other (JETransform): Other vector

            Returns:
                JETransform: Result vector
        """
        ...
    def __truediv__(self, other: JETransform) -> JETransform:
        """
            Divide 2 vector together

            Parameters:
                other (JETransform): Other vector

            Returns:
                JETransform: Result vector
        """
        ...
    def __neg__(self) -> JETransform:
        """
            Negate a vector

            Returns:
                JETransform: Result vector
        """
        ...
    def __eq__(self, other: JETransform) -> JEBool:
        """
            Compare 2 vector together

            Parameters:
                other (JETransform): Other vector

            Returns:
                JEBool: Whether the two vectors are equal
        """
        ...
    def __iadd__(self, other: int) -> JETransform:
        """
            Scalar addition of a vector

            Parameters:
                other (int): Scale

            Returns:
                JETransform: Result vector
        """
        ...
    def __isub__(self, other: int) -> JETransform:
        """
            Scalar subtraction of a vector

            Parameters:
                other (int): Scale

            Returns:
                JETransform: Result vector
        """
        ...
    def __imul__(self, other: int) -> JETransform:
        """
            Scalar multiplication of a vector

            Parameters:
                other (int): Scale

            Returns:
                JETransform: Result vector
        """
        ...
    def __itruediv__(self, other: JETransform) -> JETransform:
        """
            Scalar division of a vector

            Parameters:
                other (int): Scale

            Returns:
                JETransform: Result vector
        """
        ...
    def __len__(self) -> float:
        """
            Get the length of the vector

            Returns:
                float: Length
        """
        ...
    def length(self) -> float:
        """
            Get the length of the vector

            Returns:
                float: Length
        """
        ...
    def normalize(self) -> JETransform:
        """
            Get the normalized vector

            Returns:
                JETransform: Result vector
        """
        ...
    def dot(self, other: JETransform) -> float:
        """
            Get the dot product

            Parameters:
                other (JETransform): Other vector

            Returns:
                float: Dot product
        """
        ...
    def distance(self, other: JETransform) -> float:
        """
            Get the distance between two vectors

            Parameters:
                other (JETransform): Other vector

            Returns:
                float: Distance
        """
        ...
    def copy(self) -> JETransform:
        """
            Copy a vector

            Returns:
                JETransform: Result vector
        """
        ...
    def to_list(self) -> list:
        """
            Get the vector as a list

            Returns:
                list: Vector
        """
        ...
    def __repr__(self) -> str:
        """
            Get the string representation of the vector

            Returns:
                str: String representation
        """
        ...
