from __future__ import annotations

from jarengine.interns.base_classe import JEInternBaseClass
from jarengine.systems.bool import JEBool

class JEInternGraphic(JEInternBaseClass):
    def __init__(self, name: str):
        """
            JEInternGraphic
            
            Parameters:
                name (str): Name
        """
        ...
    def destroy(self):
        """
            Destroy the graphic object (if not overwritten, only sets a destroy value to JETrue)
        """
        ...
    @property
    def is_alive(self) -> JEBool:
        """
            Check if the graphic object is still alive

            Returns:
                JEBool: Whether the graphic object is still alive
        """
        ...

class JEInternGraphicalObject(JEInternGraphic):
    def __init__(self, name: str):
        """
            JEInternGraphicalObject

            Parameters:
                name (str): Name
        """
        ...
    def update(self, dt: float):
        """
            Update the graphical object
            
            Parameters:
                dt (float): Time
        """
        ...
    def mark_dirty(self):
        """
            Flag graphical object as dirty
        """
        ...
    def clear_dirty(self):
        """
            Clear dirty flag
        """
        ...
    @property
    def is_dirty(self) -> JEBool:
        """
            Check if the graphical object is dirty

            Returns:
                JEBool: Whether the graphical object is dirty
        """
        ...

class JEInternResource(JEInternGraphic):
    def __init__(self, name: str, path: str):
        """
            JEInternResource

            Parameters:
                name (str): Name
                path (str): Path
        """
        ...
    @property
    def path(self) -> str:
        """
            Get resource path

            Returns:
                str: Resource path
        """
        ...
