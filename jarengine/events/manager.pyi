from __future__ import annotations

from jarengine.interns.base_classe import JEInternBaseClass
from jarengine.interns import PGExtern
from jarengine.events.event import JEEventCode, JEEventWatcher
from jarengine.events.keyboard import JEKeyCode, JEKeyWatcher
from jarengine.events.mouse import JEMouseCode, JEMouseWatcher
from jarengine.systems.bool import JEBool
from jarengine.games.game import JEGame

class JEEvent(JEInternBaseClass):
    def __init__(self, event: PGExtern.event.Event):
        """
            JEEvent

            Parameters:
                event (PGExtern.event.Event): PyGame event
        """
        ...
    @property
    def type(self) -> JEEventCode: ...
    @property
    def key(self) -> JEKeyCode | None: ...
    @property
    def mouse(self) -> JEMouseCode | None: ...

class JEEventHandler(JEInternBaseClass):
    def __init__(self):
        """
            JEEventHandler
        """
        ...
    @property
    def watchers(self) -> list[JEEventWatcher | JEKeyWatcher | JEMouseWatcher]:
        """
            Get watcher list

            Returns:
                list[JEEventWatcher | JEKeyWatcher | JEMouseWatcher]: Watcher list
        """
        ...
    def add(self, watcher: JEEventWatcher | JEKeyWatcher | JEMouseWatcher):
        """
            Add watcher to the event handler
            
            Parameters:
                watcher (JEEventWatcher | JEKeyWatcher | JEMouseWatcher): Watcher to add
        """
        ...
    def remove(self, watcher: JEEventCode | JEKeyCode | JEMouseCode):
        """
            Remove watcher to the event handler

            Parameters:
                watcher (JEEventWatcher | JEKeyWatcher | JEMouseWatcher): Watcher to remove
        """
        ...
    def clear(self):
        """
            Clear the watcher list
        """
        ...
    def has(self, code: JEEventCode | JEKeyCode | JEMouseCode) -> JEBool:
        """
            Check if an event, key or mouse is being watched
            
            Parameters:
                code (JEEventWatcher | JEKeyWatcher | JEMouseWatcher): Code to check
            
            Returns:
                JEBool: JETrue if code is being checked, JEFalse otherwise
        """
        ...
    def process(self, game: JEGame, is_single_match: JEBool = JEBool(1)):
        """
            Process PyGame poll event. Activate 'is_single_match' for faster process speed (only if watchers don't have any codes in common).
            
            Parameters:
                game (JEGame): Game
                is_single_match (JEBool): Value indicating if event should be processed 1 time, or until the end of watcher list.
        """
        ...
