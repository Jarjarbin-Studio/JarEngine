# =============================================================================
# JarEngine - Python Game Engine Wrapper (Pygame-based)
# =============================================================================
#
# JarEngine is a lightweight game framework built on top of Pygame
# that simplifies usage while providing higher-level abstractions for
# game development and prototyping.
#
# =============================================================================
# Version: jarengine-v1.10
# Author: Jarjarbin Studio
# Licence: GPL v3
# =============================================================================
#
# This engine is inspired by Pygame, modern game engine design patterns,
# and directly influenced by the architecture of NewCSFML.
#
# It is designed for educational purposes and small-to-medium game projects.
#
# It provides structured systems such as entity management, scene handling,
# render abstraction, and advanced modules like particle systems.
#
# =============================================================================
# WARNING:
# =============================================================================
#
# This is NOT Pygame itself.
# It is a custom abstraction layer built on top of Pygame.
#
# =============================================================================

from __future__ import annotations

from typing import Optional

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
    def type(self) -> JEEventCode:
        """
            Get event code of the current event

            Returns:
                JEEventCode: Event code
        """
        ...
    @property
    def key(self) -> Optional[JEKeyCode]:
        """
            Get key code of the current event (None if event unrelated to key)

            Returns:
                Optional[JEKeyCode]: Key code
        """
        ...
    @property
    def mouse(self) -> Optional[JEMouseCode]:
        """
            Get mouse code of the current event (None if event unrelated to mouse)

            Returns:
                Optional[JEMouseCode]: Mouse code
        """
        ...

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
    def process(self, game: JEGame, broadcast: JEBool = JEBool(1)):
        """
            Process PyGame poll event. Activate 'is_single_match' for faster process speed (only if watchers don't have any codes in common).
            
            Parameters:
                game (JEGame): Game
                broadcast (JEBool): Value indicating if event should be processed 1 time, or until the end of watcher list.
        """
        ...
