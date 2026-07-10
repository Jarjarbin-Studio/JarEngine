from __future__ import annotations

from typing import Callable, Optional

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
    def __int__(self) -> int: ...
    @property
    def name(self) -> str: ...
    def __or__(self, other: JEKeyCode) -> JEKeyCodeGroup: ...
    def __eq__(self, other: JEEventCode) -> bool: ...
    def __hash__(self) -> int: ...

class JEKeyCodeGroup(JEInternBaseClass):
    def __init__(self, keys: list[JEKeyCode]):
        """
            JEKeyCodeGroup

            Parameters:
                keys (list[JEKeyCode]): Keys to store together
        """
        ...
    def __or__(self, other: JEKeyCode | JEKeyCodeGroup) -> JEKeyCodeGroup: ...
    def __iter__(self): ...
    @property
    def keys(self): ...

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
    def match(self, event: JEEvent) -> bool: ...
    def __call__(self, game: JEGame, event: JEEvent): ...
    @property
    def on(self) -> JEKeyCodeGroup: ...
    @property
    def params(self) -> JEEventCode: ...
    @property
    def do(self) -> str: ...
