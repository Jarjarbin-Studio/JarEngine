from __future__ import annotations

from typing import Callable, Optional

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
    def __int__(self) -> int: ...
    @property
    def name(self) -> str: ...
    def __or__(self, other: JEMouseCode) -> JEMouseCodeGroup: ...
    def __eq__(self, other: JEEventCode) -> bool: ...
    def __hash__(self) -> int: ...

class JEMouseCodeGroup(JEInternBaseClass):
    def __init__(self, mouses: list[JEMouseCode]):
        """
            JEMouseCodeGroup

            Parameters:
                mouses (list[JEMouseCode]): mouse to store together
        """
        ...
    def __or__(self, other: JEMouseCode | JEMouseCodeGroup) -> JEMouseCodeGroup: ...
    def __iter__(self): ...
    @property
    def mouses(self): ...

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
    def match(self, event: JEEvent) -> bool: ...
    def __call__(self, game: JEGame, event: JEEvent): ...
    @property
    def on(self) -> JEMouseCodeGroup: ...
    @property
    def params(self) -> JEEventCode: ...
    @property
    def do(self) -> str: ...
