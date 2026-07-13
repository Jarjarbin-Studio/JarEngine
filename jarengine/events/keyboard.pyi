from __future__ import annotations

from typing import Callable, Optional, Iterator

from jarengine.interns.base_classe import JEInternBaseClass
from jarengine.events.event import JEEventCode
from jarengine.games.game import JEGame
from jarengine.events.manager import JEEvent
from jarengine.systems.bool import JEBool

class JEKeyCode(JEInternBaseClass):
    def __init__(self, key: Optional[int]):
        """
            JEEventCode

            Parameters:
                key (Optional[int]): Key code
        """
        ...
    def __int__(self) -> int:
        """
            Get key code

            Returns:
                int: Key code
        """
        ...
    @property
    def name(self) -> str:
        """
        Get key name

            Returns:
                str: Key name
        """
        ...
    def __or__(self, other: JEKeyCode) -> JEKeyCodeGroup:
        """
        Create key group out of "Key1 | Key2"

            Parameters:
                other (JEKeyCode): Keys to store together

            Returns:
                JEKeyCodeGroup: Key group
        """
        ...
    def __eq__(self, other: JEKeyCode) -> JEBool:
        """
        Compare 2 keys

            Parameters:
                other (JEKeyCode): Key to compare with

            Returns:
                JEBool: True if they are equal, False otherwise
        """
        ...
    def __hash__(self) -> int:
        """
        Hash key (for future use)

            Returns:
                int: Key code hash
        """
        ...

class JEKeyCodeGroup(JEInternBaseClass):
    def __init__(self, keys: list[JEKeyCode]):
        """
            JEKeyCodeGroup

            Parameters:
                keys (list[JEKeyCode]): Keys to store together
        """
        ...
    def __or__(self, other: JEKeyCode | JEKeyCodeGroup) -> JEKeyCodeGroup:
        """
        Create key group out of "Key1 | Key2 | Key3"

            Parameters:
                other (JEKeyCode | JEKeyCodeGroup): Keys to store together

            Returns:
                JEKeyCodeGroup: Key group
        """
        ...
    def __iter__(self) -> Iterator[JEKeyCode]:
        """
        Iterate over keys

            Returns:
                Iterator[JEKeyCode]: Iterator
        """
        ...
    @property
    def keys(self) -> list[JEKeyCode]:
        """
        Get keys

            Returns:
                list[JEKeyCode]: List of keys
        """
        ...

class JEKeyWatcher(JEInternBaseClass):
    def __init__(self, on: JEKeyCode | list[JEKeyCode] | JEKeyCodeGroup, do: Callable[[JEGame, JEEvent], None], on_press: JEBool = JEBool(1)):
        """
            JEKeyWatcher

            Parameters:
                on (JEKeyCode | list[JEKeyCode] | JEKeyCodeGroup): Trigger event(s)
                do (Callable[[JEGame, JEEvent], None]): Action to do once triggered
                on_press (JEBool): Do action when key is pressed or released
        """
        ...
    def match(self, event: JEEvent) -> bool:
        """
            Look for a match of the keys with the event

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
    def on(self) -> JEKeyCodeGroup:
        """
            Get the "on" key group of the watcher

            Returns:
                JEKeyCodeGroup: Key group
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
