from __future__ import annotations

from jarengine.interns.base_classe import JEInternBaseClass
from jarengine.interns import PGExtern

class JEVersion(PGExtern.version.SoftwareVersion, JEInternBaseClass):
    def __init__(self, major: int, minor: int, patch: int):
        """
            JEVersion

            Parameters:
                major (int): Major version
                minor (int): Minor version
                patch (int): Patch version
        """
        ...
    def __str__(self) -> str:
        """
            Get string of the version

            Returns:
                str: String of the version
        """
        ...
    @property
    def major(self) -> int:
        """
            Get major version

            Returns:
                int: Major version
        """
        ...
    @property
    def minor(self) -> int:
        """
            Get minor version

            Returns:
                int: Minor version
        """
        ...
    @property
    def patch(self) -> int:
        """
            Get patch version

            Returns:
                int: Patch version
        """
        ...
