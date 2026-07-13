from __future__ import annotations

from jarengine.interns.base_classe import JEInternBaseClass
from jarengine.events.keyboard import JEKeyCode
from jarengine.events.mouse import JEMouseCode
from jarengine.systems.vector import JEVector2D

class JEInput(JEInternBaseClass):
    def __init__(self):
        """
            JEInput
        """
        ...
    def update(self):
        """
            Update keyboard and mouse
        """
        ...
    def is_key_down(self, key: JEKeyCode) -> bool:
        """
            Check if given key is down

            Parameters:
                key (JEKeyCode): Key code

            Returns:
                bool: True if key down, False otherwise
        """
        ...
    def is_mouse_down(self, button: JEMouseCode) -> bool:
        """
            Check if given mouse button is down

            Parameters:
                button (JEMouseCode): Mouse code

            Returns:
                bool: True if mouse button down, False otherwise
        """
        ...
    def mouse_pos(self) -> JEVector2D:
        """
            Get mouse position

            Returns:
                JEVector2D: Mouse position
        """
        ...
    def __call__(self, code: JEKeyCode | JEMouseCode) -> bool:
        """
            Automatically dispatch between 'is_key_down' and 'is_mouse_down'
            
            Parameters:
                code (JEKeyCode | JEMouseCode) Key or mouse button
            
            Returns:
                bool: True if key or mouse down, False otherwise
        """
        ...
