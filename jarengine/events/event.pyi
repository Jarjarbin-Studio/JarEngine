from __future__ import annotations

from typing import Callable, Optional

from jarengine.interns.base_classe import JEInternBaseClass
from jarengine.games.game import JEGame
from jarengine.events.manager import JEEvent

class JEEventCode(JEInternBaseClass):
    def __init__(self, event: Optional[int]):
        """
            JEEventCode

            Parameters:
                event (Optional[int]): Event code
        """
        ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str: ...
    def __or__(self, other: JEEventCode) -> JEEventCodeGroup: ...
    def __eq__(self, other: JEEventCode) -> bool: ...
    def __hash__(self) -> int: ...

class JEEventCodeGroup(JEInternBaseClass):
    def __init__(self, events: list[JEEventCode]):
        """
            JEEventCodeGroup

            Parameters:
                events (list[JEEventCode]): Events to store together
        """
        ...
    def __or__(self, other: JEEventCode | JEEventCodeGroup) -> JEEventCodeGroup: ...
    def __iter__(self): ...
    @property
    def events(self): ...

class JEEventWatcher(JEInternBaseClass):
    def __init__(self, on: JEEventCode | list[JEEventCode] | JEEventCodeGroup, do: Callable[[JEGame, JEEvent], None]):
        """
            JEEventWatcher

            Parameters:
                on (JEEventCode | list[JEEventCode] | JEEventCodeGroup): Trigger event(s)
                do (Callable[[JEGame, JEEvent], None]): Action to do once triggered
        """
        ...
    def match(self, event: JEEvent) -> bool: ...
    def __call__(self, game: JEGame, event: JEEvent): ...
    @property
    def on(self) -> JEEventCodeGroup: ...
    @property
    def do(self) -> str: ...
