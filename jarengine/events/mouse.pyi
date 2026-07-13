from __future__ import annotations

from typing import Callable, Optional, Iterator

from jarengine.interns.base_classe import JEInternBaseClass
from jarengine.events.event import JEEventCode
from jarengine.games.game import JEGame
from jarengine.events.manager import JEEvent
from jarengine.systems.bool import JEBool

class JEMouseCode(JEInternBaseClass):
    def __init__(self, mouse: Optional[int]):
        """
            JEEventCode

            Parameters:
                mouse (Optional[int]): Key code
        """
        ...
    def __int__(self) -> int:
        """
            Get mouse code

            Returns:
                int: Mouse code
        """
        ...
    @property
    def name(self) -> str:
        """
        Get mouse name

            Returns:
                str: Mouse name
        """
        ...
    def __or__(self, other: JEMouseCode) -> JEMouseCodeGroup:
        """
        Create mouse group out of "Mouse1 | Mouse2"

            Parameters:
                other (JEMouseCode): Mouses to store together

            Returns:
                JEMouseCodeGroup: Mouse group
        """
        ...
    def __eq__(self, other: JEMouseCode) -> JEBool:
        """
        Compare 2 mouses

            Parameters:
                other (JEMouseCode): Mouse to compare with

            Returns:
                JEBool: True if they are equal, False otherwise
        """
        ...
    def __hash__(self) -> int:
        """
        Hash mouse (for future use)

            Returns:
                int: Mouse code hash
        """
        ...

class JEMouseCodeGroup(JEInternBaseClass):
    def __init__(self, mouses: list[JEMouseCode]):
        """
            JEMouseCodeGroup

            Parameters:
                mouses (list[JEMouseCode]): mouse to store together
        """
        ...
    def __or__(self, other: JEMouseCode | JEMouseCodeGroup) -> JEMouseCodeGroup:
        """
        Create mouse group out of "Mouse1 | Mouse2 | Mouse3"

            Parameters:
                other (JEMouseCode | JEMouseCodeGroup): Mouses to store together

            Returns:
                JEMouseCodeGroup: Mouse group
        """
        ...
    def __iter__(self) -> Iterator[JEMouseCode]:
        """
        Iterate over mouses

            Returns:
                Iterator[JEMouseCode]: Iterator
        """
        ...
    @property
    def mouses(self) -> list[JEMouseCode]:
        """
        Get mouses

            Returns:
                list[JEMouseCode]: List of mouses
        """
        ...

class JEMouseWatcher(JEInternBaseClass):
    def __init__(self, on: JEMouseCode | list[JEMouseCode] | JEMouseCodeGroup, do: Callable[[JEGame, JEEvent], None], on_press: JEBool = JEBool(1)):
        """
            JEMouseWatcher

            Parameters:
                on (JEMouseCode | list[JEMouseCode] | JEMouseCodeGroup): Trigger event(s)
                do (Callable[[JEGame, JEEvent], None]): Action to do once triggered
                on_press (JEBool): Do action when mouse is pressed or released
        """
        ...
    def match(self, event: JEEvent) -> bool:
        """
            Look for a match of the mouses with the event
            
            Parameters:
                event (JEEvent): Event to look for
            
            Returns:
                bool: True if event matches, False otherwise
        """
        ...
    def __call__(self, game: JEGame, event: JEEvent):
        """
            Call the "do" function of the watcher

            Parameters:
                game (JEGame): Game
                event (JEEvent): Current Event
        """
        ...
    @property
    def on(self) -> JEMouseCodeGroup:
        """
            Get the "on" mouse group of the watcher

            Returns:
                JEMouseCodeGroup: Mouse group
        """
        ...
    @property
    def params(self) -> JEEventCode:
        """
            Get the "params" event of the watcher

            Returns:
                JEEventCode: Event code
        """
        ...
    @property
    def do(self) -> str:
        """
            Get the string representation of the "do" function of the watcher

            Returns:
                str: String representation
        """
        ...
